"""Tools del agente de post-venta — MercaSur (retail).

4 tools núcleo (Laboratorio 4) + 2 opcionales de reto.
"""

from __future__ import annotations

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from comun import datos
from comun.datos import DatoNoEncontrado

TRACK = "retail"


# ───────────────────────────── esquemas ─────────────────────────────
class PedidoInput(BaseModel):
    pedido_id: str = Field(description="Número de pedido en formato MS-2026-NNNNN")


class SkuInput(BaseModel):
    sku: str = Field(description="Código de producto en formato MS-NNNN")


class DevolucionInput(BaseModel):
    pedido_id: str = Field(description="Número de pedido en formato MS-2026-NNNNN")
    motivo: str = Field(description="Motivo del cliente, por ejemplo 'Producto con falla' o 'Talla incorrecta'")
    tipo_solucion: str = Field(default="CAMBIO", description="CAMBIO, REEMBOLSO o NOTA_CREDITO")


class EntregaInput(BaseModel):
    distrito: str = Field(description="Distrito de entrega, por ejemplo 'Los Olivos'")
    monto_compra: float = Field(description="Monto total de la compra en soles")


# ─────────────────────────── tools núcleo ───────────────────────────
@tool(args_schema=PedidoInput)
def track_order(pedido_id: str) -> str:
    """Devuelve el estado, el courier y el código de rastreo de un pedido.

    Úsala cuando el cliente pregunte dónde está su pedido, cuándo llega,
    o por qué no lo ha recibido.
    NO la uses para iniciar una devolución: para eso usa start_return_request.
    """
    try:
        p = datos.buscar_uno("pedidos.csv", "pedido_id", pedido_id, TRACK)
    except DatoNoEncontrado:
        return (f"No existe el pedido {pedido_id}. Verifica el número con el cliente: "
                f"el formato es MS-2026-NNNNN y aparece en el correo de confirmación.")
    significado = {
        "EN_PREPARACION": "El pedido está siendo alistado en el almacén",
        "EN_RUTA": "El pedido fue entregado al courier y está en camino",
        "ENTREGADO": "El pedido fue recibido y firmado",
        "LISTO_PARA_RECOJO": "El pedido está disponible para recojo",
        "DEVUELTO": "El pedido regresó al almacén tras intentos fallidos de entrega",
        "CANCELADO": "El pedido fue anulado antes del despacho",
    }
    aviso = ""
    if p["estado"] == "DEVUELTO":
        aviso = (" IMPORTANTE: el pedido permanece 15 días calendario a disposición del cliente; "
                 "pasado ese plazo se procesa el reembolso automático.")
    return (f"Pedido {p['pedido_id']} · Cliente: {p['cliente']} · Comprado el {p['fecha_compra']} · "
            f"Estado: {p['estado']} ({significado.get(p['estado'], 'estado desconocido')}) · "
            f"Courier: {p['courier']} · Rastreo: {p['codigo_tracking']} · "
            f"Despacho desde {p['tienda_despacho']} hacia {p['distrito_entrega']}.{aviso}")


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
def start_return_request(pedido_id: str, motivo: str, tipo_solucion: str = "CAMBIO") -> str:
    """Inicia una solicitud de cambio o devolución y devuelve su código de seguimiento.

    Úsala cuando el cliente pida devolver, cambiar o reembolsar un producto ya recibido.
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
    tipos = {"CAMBIO", "REEMBOLSO", "NOTA_CREDITO"}
    tipo_solucion = tipo_solucion.strip().upper()
    if tipo_solucion not in tipos:
        return f"Tipo de solución inválido: '{tipo_solucion}'. Debe ser uno de: {', '.join(sorted(tipos))}."
    dev_id = datos.siguiente_id("devoluciones.csv", "devolucion_id", "DEV-", TRACK)
    plazos = {"CAMBIO": "3 a 5 días hábiles", "REEMBOLSO": "7 a 15 días hábiles",
              "NOTA_CREDITO": "inmediata, válida 12 meses"}
    return (f"Solicitud registrada. Código: {dev_id} · Pedido: {pedido_id} · Producto: {p['sku']} · "
            f"Motivo: {motivo} · Solución solicitada: {tipo_solucion} ({plazos[tipo_solucion]}) · "
            f"Estado: SOLICITADA. Entrega este código al cliente para su seguimiento.")


# ────────────────────────── tools opcionales ──────────────────────────
@tool(args_schema=EntregaInput)
def estimate_delivery(distrito: str, monto_compra: float) -> str:
    """Calcula el costo y el plazo de despacho para un distrito y un monto de compra.

    Úsala cuando el cliente pregunte cuánto cuesta el envío o en cuánto tiempo llega
    antes de comprar.
    NO la uses para consultar un pedido ya hecho: para eso usa track_order.
    """
    lima = {"Miraflores","San Isidro","Santiago de Surco","La Molina","San Borja","Jesús María","Lince",
            "Magdalena del Mar","Pueblo Libre","San Miguel","Comas","San Juan de Lurigancho",
            "Villa El Salvador","Ate","Callao","Chorrillos","Barranco","Surquillo","Los Olivos","Independencia"}
    es_lima = distrito.strip().title() in lima or distrito.strip() in lima
    umbral, costo, plazo = (149.0, 12.90, "3 a 5 días hábiles") if es_lima else (299.0, 24.90, "5 a 9 días hábiles")
    zona = "Lima Metropolitana y Callao" if es_lima else "provincias"
    if monto_compra >= umbral:
        return (f"Despacho a {distrito} ({zona}): GRATUITO por superar S/ {umbral:.2f}. "
                f"Plazo estimado: {plazo}.")
    falta = umbral - monto_compra
    return (f"Despacho a {distrito} ({zona}): S/ {costo:.2f}. Plazo estimado: {plazo}. "
            f"Con S/ {falta:.2f} adicionales el despacho sería gratuito.")


@tool(args_schema=PedidoInput)
def get_return_status(pedido_id: str) -> str:
    """Consulta el estado de las devoluciones asociadas a un pedido.

    Úsala cuando el cliente pregunte en qué va su cambio o su reembolso.
    NO la uses para iniciar una devolución nueva: para eso usa start_return_request.
    """
    devs = datos.buscar_todos("devoluciones.csv", "pedido_id", pedido_id, TRACK)
    if not devs:
        return f"El pedido {pedido_id} no tiene solicitudes de devolución registradas."
    return "\n".join(
        f"{d['devolucion_id']} · Producto {d['sku']} · Motivo: {d['motivo']} · "
        f"Solución: {d['tipo_solucion']} · Estado: {d['estado']} · Solicitada el {d['fecha_solicitud']}"
        for d in devs
    )


TOOLS_NUCLEO = [track_order, get_product_details, check_stock_by_store, start_return_request]
TOOLS_OPCIONALES = [estimate_delivery, get_return_status]
