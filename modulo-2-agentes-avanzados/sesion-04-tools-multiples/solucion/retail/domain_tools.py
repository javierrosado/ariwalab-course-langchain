"""L4 · Retail — MercaSur · domain_tools.py (checkpoint de referencia)

Las 4 tools núcleo del track. La primera (`track_order`) NO se reescribe: se importa
tal cual del L3 (Sesión 3) — el mismo patrón con el que la Sesión 5 importa este
archivo y la Sesión 6 importa el de la Sesión 5. La cadena L2 → L3 → L4 → L5 → L6 se
apoya en código real. La categoría del L2 (`recursos/golden/consultas-retail.json`,
campo `intencion`) es 1:1 con estas 4 tools (campo `tool_esperada`): es el mismo
golden set el que mide el L2 (`medir_clasificador.py`) y el L4
(`docente/matriz_seleccion.py`). Las otras tres tools son el incremento del L4.
`start_return_request` exige confirmación explícita antes de registrar la solicitud
(regla del bloque 4 de README.md).

Regla A2: cada docstring dice QUÉ hace, CUÁNDO usarla y CUÁNDO NO.

Regla A3: `start_return_request` normaliza su `tipo_solucion` con `extraer()` de
`comun/structured.py` antes de pedir confirmación — el mismo módulo del L2, aplicado
aquí por primera vez fuera del clasificador (hallazgo H7 de
`docente/esqueletos/VALIDACION-INTEGRAL.md`).
"""

from __future__ import annotations

import sys
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
# La tool del L3 no se reescribe: se importa de su checkpoint de referencia.
sys.path.insert(0, str(ROOT / "modulo-1-fundamentos" / "sesion-03-tools-api-externa"
                       / "solucion" / "retail"))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402
from comun.provider import get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida, extraer  # noqa: E402

from external_api import PedidoInput, track_order  # noqa: E402  (del L3, sin reescribir)

TRACK = "retail"


# ───────────────────── esquemas nuevos del L4 ─────────────────────
class SkuInput(BaseModel):
    sku: str = Field(description="Código de producto en formato MS-NNNN")


class DevolucionInput(BaseModel):
    pedido_id: str = Field(description="Número de pedido en formato MS-2026-NNNNN")
    motivo: str = Field(description="Motivo del cliente, por ejemplo 'Producto con falla' o 'Talla incorrecta'")
    tipo_solucion: str = Field(default="CAMBIO", description="CAMBIO, REEMBOLSO o NOTA_CREDITO")
    confirmado_por_cliente: bool = Field(
        default=False,
        description="True solo si el cliente confirmó explícitamente que quiere registrar la solicitud",
    )


class TipoSolucion(str, Enum):
    CAMBIO = "CAMBIO"
    REEMBOLSO = "REEMBOLSO"
    NOTA_CREDITO = "NOTA_CREDITO"


class ClasificacionSolucion(BaseModel):
    """Normaliza el tipo de solución contra las 3 categorías válidas, a partir de lo
    que declaró el agente y del motivo real que dio el cliente."""

    tipo_solucion: TipoSolucion = Field(description="La solución que mejor corresponde al motivo")


# track_order del L3 se usa tal cual (import de arriba).


# ─────────────────────────── tools nuevas del L4 ───────────────────────────
@tool(args_schema=SkuInput)
def get_product_details(sku: str) -> str:
    """Devuelve el nombre, la categoría, el precio, la garantía y si un producto admite cambio.

    Úsala cuando el cliente pregunte por las características, el precio o la garantía
    de un producto concreto.
    NO la uses para saber si hay stock: para eso usa check_stock_by_store.
    """
    try:
        p = datos.buscar_uno("catalogo_productos.csv", "sku", sku, TRACK)
    except DatoNoEncontrado:
        return f"No existe el producto {sku} en el catálogo de MercaSur."
    cambio = ("admite cambio por libre voluntad dentro de 30 días"
              if p["permite_cambio"] == "SI"
              else "NO admite cambio por libre voluntad, pero sí conserva la garantía por defecto de fábrica")
    return (f"{p['sku']} · {p['nombre']} · Categoría: {p['categoria']} · Marca: {p['marca']} · "
            f"Precio: S/ {p['precio_soles']} · Garantía: {p['garantia_meses']} meses · {cambio}.")


@tool(args_schema=SkuInput)
def check_stock_by_store(sku: str) -> str:
    """Devuelve el stock disponible de un producto en cada tienda MercaSur.

    Úsala cuando el cliente pregunte si hay disponibilidad, en qué tienda puede
    recogerlo, o si puede cambiar su producto por otro igual.
    NO la uses para consultar el precio o la garantía: para eso usa get_product_details.
    """
    filas = datos.buscar_todos("stock_tiendas.csv", "sku", sku, TRACK)
    if not filas:
        return f"No hay información de stock para el producto {sku}."
    con_stock = [f for f in filas if int(f["stock_disponible"]) > 0]
    if not con_stock:
        return f"El producto {sku} está SIN STOCK en todas las tiendas MercaSur."
    detalle = " · ".join(f"{f['tienda']}: {f['stock_disponible']} unidades" for f in con_stock)
    total = sum(int(f["stock_disponible"]) for f in con_stock)
    return f"Stock de {sku}: {total} unidades en {len(con_stock)} tiendas. {detalle}"


@tool(args_schema=DevolucionInput)
def start_return_request(pedido_id: str, motivo: str, tipo_solucion: str = "CAMBIO",
                         confirmado_por_cliente: bool = False) -> str:
    """Inicia una solicitud de cambio o devolución y devuelve su código. Requiere confirmación.

    Úsala cuando el cliente pida devolver, cambiar o reembolsar un producto ya recibido.
    Llámala primero con confirmado_por_cliente=False para obtener el mensaje de
    confirmación, y solo vuelve a llamarla con True si el cliente confirma explícitamente.
    NO la uses si el pedido aún no fue entregado: en ese caso corresponde una anulación,
    no una devolución.
    NO apruebes la devolución: esta tool solo registra la solicitud; la autorización
    corresponde al área de post-venta.
    """
    try:
        p = datos.buscar_uno("pedidos.csv", "pedido_id", pedido_id, TRACK)
    except DatoNoEncontrado:
        return f"No existe el pedido {pedido_id}."
    if p["estado"] != "ENTREGADO":
        return (f"El pedido {pedido_id} está en estado {p['estado']}, no ENTREGADO. "
                f"No corresponde una devolución: consulta con el cliente si desea anular el pedido.")

    # Regla A3: el tipo de solución no se acepta tal cual — se normaliza contra las 3
    # categorías válidas con extraer() (comun/structured.py), ANTES de pedir
    # confirmación: no tiene sentido confirmarle al cliente una solución inválida.
    try:
        clasificacion = extraer(
            get_chat_model(), ClasificacionSolucion,
            f"Solución declarada: {tipo_solucion}\nMotivo del cliente: {motivo}",
        )
    except ExtraccionFallida:
        return (f"Tipo de solución inválido: '{tipo_solucion}'. Debe ser uno de: "
                f"{', '.join(t.value for t in TipoSolucion)}.")
    tipo_validado = clasificacion.tipo_solucion.value

    if not confirmado_por_cliente:
        return (f"CONFIRMACIÓN REQUERIDA. Vas a registrar una solicitud de {tipo_validado} para el "
                f"pedido {pedido_id} por el motivo: \"{motivo}\". Pregunta al cliente si confirma y "
                f"solo entonces vuelve a llamar esta tool con confirmado_por_cliente=True.")
    dev_id = datos.siguiente_id("devoluciones.csv", "devolucion_id", "DEV-", TRACK)
    plazos = {"CAMBIO": "3 a 5 días hábiles", "REEMBOLSO": "7 a 15 días hábiles",
              "NOTA_CREDITO": "inmediata, válida 12 meses"}
    return (f"Solicitud registrada. Código: {dev_id} · Pedido: {pedido_id} · Producto: {p['sku']} · "
            f"Motivo: {motivo} · Solución solicitada: {tipo_validado} ({plazos[tipo_validado]}) · "
            f"Estado: SOLICITADA. Entrega este código al cliente para su seguimiento.")


TOOLS_NUCLEO = [track_order, get_product_details, check_stock_by_store, start_return_request]
