"""L4 · Telecomunicaciones — AndesMóvil · domain_tools.py (checkpoint de referencia)

Las 4 tools núcleo del track. La primera (`get_customer_plan`) NO se reescribe: se
importa tal cual del L3 (Sesión 3) — el mismo patrón con el que la Sesión 5 importa
este mismo archivo, y la Sesión 6 importa el de la Sesión 5. La cadena L2 → L3 → L4 →
L5 → L6 se apoya en código real, no solo en la narrativa. Las otras tres tools son el
incremento del L4. `create_complaint_ticket` exige confirmación explícita antes de
registrar el reclamo (regla del bloque 4 de README.md: toda tool de escritura se
implementa con confirmación desde el L4, no se pospone a los guardrails de la S6).

La categoría de intención que el L2 (Sesión 2) le asigna a cada consulta —
`recursos/golden/consultas-telecomunicaciones.json`, campo `intencion`— es 1:1 con
estas 4 tools (campo `tool_esperada` del mismo archivo): `CONSULTA_PLAN` es
`get_customer_plan`, `CONSULTA_CONSUMO` es `get_data_usage`, y así con las 4. Es el
mismo golden set el que mide el L2 (`medir_clasificador.py`) y el L4
(`docente/matriz_seleccion.py`) — no son dos ejercicios que coinciden por casualidad
en la taxonomía, son el mismo problema medido en dos profundidades distintas.

Regla A2: cada docstring dice QUÉ hace, CUÁNDO usarla y CUÁNDO NO.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
# La tool del L3 no se reescribe: se importa de su checkpoint de referencia.
sys.path.insert(0, str(ROOT / "modulo-1-fundamentos" / "sesion-03-tools-api-externa"
                       / "solucion" / "telecomunicaciones"))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402

from external_api import LineaInput, get_customer_plan  # noqa: E402  (del L3, sin reescribir)

TRACK = "telecomunicaciones"


# ───────────────────────────── esquemas nuevos del L4 ─────────────────────────────
# LineaInput se reutiliza del L3 (import de arriba): run_line_diagnostics la necesita
# con el mismo esquema, no con una copia.
class ConsumoInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")
    periodo: str = Field(default="2026-08", description="Periodo de facturación en formato AAAA-MM")


class ReclamoInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")
    tipo: str = Field(description="FACTURACION, CALIDAD_SERVICIO, AVERIA, PORTABILIDAD, CONTRATACION o SUSPENSION")
    descripcion: str = Field(description="Descripción del problema en palabras del cliente, máximo 200 caracteres")
    confirmado_por_cliente: bool = Field(
        default=False,
        description="True solo si el cliente confirmó explícitamente que quiere registrar el reclamo en este turno",
    )


# get_customer_plan del L3 se usa tal cual (import de arriba). Su docstring sigue
# siendo la misma que el modelo leyó desde la Sesión 3 — no cambia entre sesiones.


# ─────────────────────────── tools nuevas del L4 ───────────────────────────
@tool(args_schema=ConsumoInput)
def get_data_usage(numero_linea: str, periodo: str = "2026-08") -> str:
    """Devuelve el consumo de datos, minutos y SMS de una línea en un periodo.

    Úsala cuando el cliente pregunte cuántos gigas ha consumido, cuánto le queda,
    o por qué se le acabaron los datos.
    NO la uses para saber qué plan tiene: para eso usa get_customer_plan.
    """
    filas = [f for f in datos.buscar_todos("consumo_datos.csv", "numero_linea", numero_linea, TRACK)
             if f["periodo"] == periodo]
    if not filas:
        disponibles = sorted({f["periodo"] for f in
                              datos.buscar_todos("consumo_datos.csv", "numero_linea", numero_linea, TRACK)})
        if not disponibles:
            return f"No hay registros de consumo para la línea {numero_linea}."
        return (f"No hay consumo registrado para {numero_linea} en el periodo {periodo}. "
                f"Periodos disponibles: {', '.join(disponibles)}.")
    r = filas[0]
    consumido, incluido = float(r["gb_consumidos"]), float(r["gb_incluidos"])
    restante = max(0.0, incluido - consumido)
    estado = "PAQUETE AGOTADO, navegando a velocidad reducida" if consumido >= incluido else "dentro del paquete"
    return (f"Consumo de {numero_linea} en {periodo}: {consumido} GB de {incluido} GB incluidos "
            f"({restante:.2f} GB disponibles, {estado}). "
            f"Minutos usados: {r['minutos_consumidos']} · SMS enviados: {r['sms_enviados']}")


@tool(args_schema=LineaInput)
def run_line_diagnostics(numero_linea: str) -> str:
    """Ejecuta un diagnóstico técnico de la línea y de la cobertura de su distrito.

    Úsala cuando el cliente reporte que no tiene señal, que la navegación está lenta,
    que se cortan las llamadas, o cualquier falla técnica del servicio.
    NO la uses para consultas de facturación ni de consumo.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return f"No existe la línea {numero_linea}. No se puede ejecutar el diagnóstico."
    try:
        cob = datos.buscar_uno("cobertura_distritos.csv", "distrito", c["distrito"], TRACK)
    except DatoNoEncontrado:
        return (f"Línea {numero_linea} en estado {c['estado']}. "
                f"No hay datos de cobertura para el distrito {c['distrito']}.")
    partes = [f"Diagnóstico de {numero_linea}", f"Estado de la línea: {c['estado']}",
              f"Distrito: {cob['distrito']}", f"Tecnología disponible: {cob['tecnologia']}",
              f"Calidad de señal: {cob['calidad_senal']}"]
    if cob["incidencia_activa"] == "SI":
        partes.append(f"INCIDENCIA ACTIVA EN LA ZONA: {cob['detalle_incidencia']}")
    else:
        partes.append("Sin incidencias reportadas en la zona")
    if c["estado"] == "SUSPENDIDO":
        partes.append("ATENCIÓN: la línea está suspendida, lo que explica la falta de servicio")
    return " · ".join(partes)


@tool(args_schema=ReclamoInput)
def create_complaint_ticket(numero_linea: str, tipo: str, descripcion: str,
                            confirmado_por_cliente: bool = False) -> str:
    """Registra un reclamo formal y devuelve su código de seguimiento. Requiere confirmación.

    Úsala SOLO cuando el cliente pida explícitamente registrar un reclamo o manifieste
    disconformidad que no se resolvió con la información entregada.
    Llámala primero con confirmado_por_cliente=False para obtener el mensaje de
    confirmación, y solo vuelve a llamarla con True si el cliente confirma explícitamente.
    NO la uses para consultas ni para pedidos de información: eso no es un reclamo.
    NO la uses más de una vez por conversación para el mismo motivo.
    """
    tipos = {"FACTURACION", "CALIDAD_SERVICIO", "AVERIA", "PORTABILIDAD", "CONTRATACION", "SUSPENSION"}
    tipo = tipo.strip().upper()
    if tipo not in tipos:
        return f"Tipo de reclamo inválido: '{tipo}'. Debe ser uno de: {', '.join(sorted(tipos))}."
    try:
        datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return f"No existe la línea {numero_linea}. No se puede registrar el reclamo."
    if not confirmado_por_cliente:
        return (f"CONFIRMACIÓN REQUERIDA. Vas a registrar un reclamo de tipo {tipo} para la línea "
                f"{numero_linea}: \"{descripcion}\". Pregunta al cliente si confirma y solo entonces "
                f"vuelve a llamar esta tool con confirmado_por_cliente=True.")
    ticket = datos.siguiente_id("tickets_reclamos.csv", "ticket_id", "REC-2026-", TRACK)
    return (f"Reclamo registrado. Código: {ticket} · Tipo: {tipo} · Línea: {numero_linea} · "
            f"Estado: ABIERTO · Plazo máximo de respuesta: 30 días hábiles. "
            f"Entrega este código al cliente: es su constancia del reclamo.")


TOOLS_NUCLEO = [get_customer_plan, get_data_usage, run_line_diagnostics, create_complaint_ticket]
