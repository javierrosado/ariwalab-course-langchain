"""Tools del agente de atención al cliente — AndesMóvil (telecomunicaciones).

4 tools núcleo (Laboratorio 4) + 2 opcionales de reto.

Regla A2 del curso: cada docstring dice QUÉ hace, CUÁNDO usarla y CUÁNDO NO.
La docstring es literalmente el prompt que el modelo lee para decidir; con un
modelo de 7B, una descripción ambigua se traduce en una tool mal elegida.
"""

from __future__ import annotations

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from comun import datos
from comun.datos import DatoNoEncontrado

TRACK = "telecomunicaciones"


# ───────────────────────────── esquemas ─────────────────────────────
class LineaInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos, sin espacios ni guiones")


class ConsumoInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")
    periodo: str = Field(default="2026-08", description="Periodo de facturación en formato AAAA-MM")


class ReclamoInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")
    tipo: str = Field(description="FACTURACION, CALIDAD_SERVICIO, AVERIA, PORTABILIDAD, CONTRATACION o SUSPENSION")
    descripcion: str = Field(description="Descripción del problema en palabras del cliente, máximo 200 caracteres")


class DistritoInput(BaseModel):
    distrito: str = Field(description="Nombre del distrito de Lima o Callao, por ejemplo 'Miraflores'")


# ─────────────────────────── tools núcleo ───────────────────────────
@tool(args_schema=LineaInput)
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene, cuánto paga, desde cuándo es
    cliente, o si su línea está activa o suspendida.
    NO la uses para consultar consumo de datos: para eso usa get_data_usage.
    NO la uses para preguntas generales sobre el catálogo de planes de AndesMóvil:
    esa información está en la base de conocimiento, no aquí.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return (f"No existe la línea {numero_linea} en los registros de AndesMóvil. "
                f"Verifica el número con el cliente: debe tener 9 dígitos.")
    return (f"Línea {c['numero_linea']} · Titular: {c['nombre_titular']} · "
            f"Plan: {c['plan_nombre']} ({c['plan_id']}) · Estado: {c['estado']} · "
            f"Cliente desde: {c['fecha_alta']} · Distrito: {c['distrito']}")


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
def create_complaint_ticket(numero_linea: str, tipo: str, descripcion: str) -> str:
    """Registra un reclamo formal y devuelve su código de seguimiento.

    Úsala SOLO cuando el cliente pida explícitamente registrar un reclamo o manifieste
    disconformidad que no se resolvió con la información entregada.
    NO la uses para consultas ni para pedidos de información: eso no es un reclamo.
    NO la uses más de una vez por conversación sin confirmarlo con el cliente.
    """
    tipos = {"FACTURACION", "CALIDAD_SERVICIO", "AVERIA", "PORTABILIDAD", "CONTRATACION", "SUSPENSION"}
    tipo = tipo.strip().upper()
    if tipo not in tipos:
        return f"Tipo de reclamo inválido: '{tipo}'. Debe ser uno de: {', '.join(sorted(tipos))}."
    try:
        datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return f"No existe la línea {numero_linea}. No se puede registrar el reclamo."
    ticket = datos.siguiente_id("tickets_reclamos.csv", "ticket_id", "REC-2026-", TRACK)
    return (f"Reclamo registrado. Código: {ticket} · Tipo: {tipo} · Línea: {numero_linea} · "
            f"Estado: ABIERTO · Plazo máximo de respuesta: 30 días hábiles. "
            f"Entrega este código al cliente: es su constancia del reclamo.")


# ────────────────────────── tools opcionales ──────────────────────────
@tool(args_schema=LineaInput)
def check_portability_eligibility(numero_linea: str) -> str:
    """Verifica si una línea puede portarse a otra operadora y qué obligaciones quedan pendientes.

    Úsala cuando el cliente pregunte por portabilidad, por irse a otro operador,
    o por llevarse su número.
    NO la uses para ejecutar la portabilidad: esta tool solo evalúa, no tramita.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return f"No existe la línea {numero_linea}."
    if c["estado"] == "BAJA":
        return f"La línea {numero_linea} está dada de BAJA y no es portable."
    planes = {p["plan_id"]: p for p in datos.tabla("planes.json", TRACK)}
    permanencia = planes.get(c["plan_id"], {}).get("permanencia_meses", "no determinada")
    return (f"La línea {numero_linea} ES PORTABLE (estado {c['estado']}). "
            f"Permanencia mínima del plan {c['plan_nombre']}: {permanencia} meses. "
            f"Recuerda: una deuda pendiente NO impide la portabilidad, pero sigue siendo exigible. "
            f"El plazo de ejecución es de 24 horas.")


@tool(args_schema=DistritoInput)
def get_coverage_by_district(distrito: str) -> str:
    """Consulta la cobertura y las incidencias activas de un distrito.

    Úsala cuando el cliente pregunte por la cobertura de una zona antes de contratar,
    o cuando quiera saber si hay una avería general en su distrito.
    NO la uses para diagnosticar una línea concreta: para eso usa run_line_diagnostics.
    """
    try:
        c = datos.buscar_uno("cobertura_distritos.csv", "distrito", distrito, TRACK)
    except DatoNoEncontrado:
        disponibles = [f["distrito"] for f in datos.tabla("cobertura_distritos.csv", TRACK)]
        return (f"No hay información de cobertura para '{distrito}'. "
                f"Distritos con datos: {', '.join(disponibles[:10])}...")
    inc = (f"INCIDENCIA ACTIVA: {c['detalle_incidencia']}"
           if c["incidencia_activa"] == "SI" else "Sin incidencias")
    return (f"Cobertura en {c['distrito']}: tecnología {c['tecnologia']} · "
            f"calidad {c['calidad_senal']} · {inc}")


TOOLS_NUCLEO = [get_customer_plan, get_data_usage, run_line_diagnostics, create_complaint_ticket]
TOOLS_OPCIONALES = [check_portability_eligibility, get_coverage_by_district]
