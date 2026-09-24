"""L4 · Seguros — Andina Seguros · domain_tools.py (checkpoint de referencia)

Las 4 tools núcleo del track. La primera (`get_policy_by_plate`) NO se reescribe: se
importa tal cual del L3 (Sesión 3) — el mismo patrón con el que la Sesión 5 importa
este archivo y la Sesión 6 importa el de la Sesión 5. La cadena L2 → L3 → L4 → L5 →
L6 se apoya en código real. La categoría del L2 (`recursos/golden/consultas-seguros.json`,
campo `intencion`) es 1:1 con estas 4 tools (campo `tool_esperada`): es el mismo
golden set el que mide el L2 (`medir_clasificador.py`) y el L4
(`docente/matriz_seleccion.py`). Las otras tres tools son el incremento del L4.
`open_claim` exige confirmación explícita antes de abrir el expediente (regla del
bloque 4 de README.md).

Regla A2: cada docstring dice QUÉ hace, CUÁNDO usarla y CUÁNDO NO.

Regla A3: `open_claim` normaliza su `tipo` con `extraer()` de `comun/structured.py`
antes de pedir confirmación — el mismo módulo del L2, aplicado aquí por primera vez
fuera del clasificador.
"""

from __future__ import annotations

import sys
from datetime import date, datetime
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
# La tool del L3 no se reescribe: se importa de su checkpoint de referencia.
sys.path.insert(0, str(ROOT / "modulo-1-fundamentos" / "sesion-03-tools-api-externa"
                       / "solucion" / "seguros"))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402
from comun.provider import get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida, extraer  # noqa: E402

from external_api import PlacaInput, get_policy_by_plate  # noqa: E402  (del L3, sin reescribir)

TRACK = "seguros"
HOY = date(2026, 9, 5)  # fecha de referencia del curso


# ───────────────────── esquemas nuevos del L4 ─────────────────────
# PlacaInput se reutiliza del L3 (import de arriba): quote_soat la necesita con el
# mismo esquema, no con una copia.
class SiniestroInput(BaseModel):
    siniestro_id: str = Field(description="Código de expediente en formato SIN-2026-NNNNN")


class AperturaInput(BaseModel):
    placa: str = Field(description="Placa del vehículo asegurado en formato ABC-123")
    tipo: str = Field(description="CHOQUE_SIMPLE, ATROPELLO, VOLCADURA, COLISION_MULTIPLE o DESPISTE")
    distrito: str = Field(description="Distrito donde ocurrió el accidente")
    cantidad_lesionados: int = Field(ge=0, le=20, description="Número de personas lesionadas, 0 si no hay")
    confirmado_por_cliente: bool = Field(
        default=False,
        description="True solo si el cliente confirmó explícitamente que quiere abrir el expediente",
    )


class TipoSiniestro(str, Enum):
    CHOQUE_SIMPLE = "CHOQUE_SIMPLE"
    ATROPELLO = "ATROPELLO"
    VOLCADURA = "VOLCADURA"
    COLISION_MULTIPLE = "COLISION_MULTIPLE"
    DESPISTE = "DESPISTE"


class ClasificacionSiniestro(BaseModel):
    """Normaliza el tipo de siniestro contra las 5 categorías válidas, a partir de lo
    que declaró el agente — el relato del accidente manda si no coinciden."""

    tipo: TipoSiniestro = Field(description="La categoría que mejor corresponde al accidente")


# get_policy_by_plate del L3 se usa tal cual (import de arriba).


# ─────────────────────────── tools nuevas del L4 ───────────────────────────
@tool(args_schema=PlacaInput)
def quote_soat(placa: str) -> str:
    """Cotiza la prima del SOAT para un vehículo según su categoría y uso.

    Úsala cuando el cliente pregunte cuánto le costaría el SOAT o quiera renovar.
    NO la uses para consultar una póliza ya contratada: para eso usa get_policy_by_plate.
    """
    try:
        v = datos.buscar_uno("vehiculos.csv", "placa", placa, TRACK)
    except DatoNoEncontrado:
        return (f"No hay datos del vehículo con placa {placa}. "
                f"Para cotizar necesitamos la categoría del vehículo: pídele al cliente su tarjeta de propiedad.")
    base = {"M1": 92.0, "M2": 420.0, "N1": 150.0, "L5": 210.0}[v["categoria"]]
    recargo_uso = {"PARTICULAR": 1.0, "COMERCIAL": 1.25, "TAXI": 1.40}[v["uso"]]
    antiguedad = HOY.year - int(v["anio"])
    recargo_antiguedad = 1.15 if antiguedad > 10 else 1.0
    prima = base * recargo_uso * recargo_antiguedad
    detalle = [f"categoría {v['categoria']} (S/ {base:.2f})"]
    if recargo_uso > 1:
        detalle.append(f"uso {v['uso']} (+{int((recargo_uso - 1) * 100)}%)")
    if recargo_antiguedad > 1:
        detalle.append(f"antigüedad {antiguedad} años (+15%)")
    return (f"Cotización SOAT para {placa} ({v['marca']} {v['modelo']} {v['anio']}, "
            f"{v['descripcion_categoria']}): S/ {prima:.2f} anuales. "
            f"Cálculo: {' · '.join(detalle)}. Vigencia de 12 meses desde la contratación.")


@tool(args_schema=SiniestroInput)
def get_claim_status(siniestro_id: str) -> str:
    """Consulta el estado de un expediente de siniestro por su código.

    Úsala cuando el cliente pregunte en qué va su trámite o cuándo le pagarán.
    NO uses esta tool para afirmar montos a pagar: el monto lo determina el área de
    siniestros, no el asistente.
    """
    try:
        s = datos.buscar_uno("siniestros.csv", "siniestro_id", siniestro_id, TRACK)
    except DatoNoEncontrado:
        return (f"No existe el expediente {siniestro_id}. "
                f"El formato es SIN-2026-NNNNN y se entregó al reportar el siniestro.")
    significado = {
        "REPORTADO": "El siniestro fue comunicado y se generó el expediente",
        "EN_EVALUACION": "Se está revisando la documentación y la cobertura",
        "OBSERVADO": "Falta documentación o hay inconsistencias por subsanar",
        "APROBADO": "La cobertura fue reconocida y está en proceso de pago",
        "LIQUIDADO": "El pago fue efectuado a los beneficiarios",
    }
    aviso = ""
    if s["estado"] == "OBSERVADO":
        aviso = " ACCIÓN REQUERIDA: el cliente debe subsanar la documentación; el plazo está suspendido."
    if int(s["cantidad_lesionados"]) > 0:
        aviso += " Este expediente registra lesionados: DERIVA la conversación al canal humano."
    return (f"Expediente {s['siniestro_id']} · Póliza {s['poliza_id']} · Placa {s['placa']} · "
            f"Ocurrido el {s['fecha_ocurrencia']} en {s['distrito']} · Tipo: {s['tipo']} · "
            f"Lesionados: {s['cantidad_lesionados']} · Estado: {s['estado']} "
            f"({significado.get(s['estado'], 'estado desconocido')}).{aviso}")


@tool(args_schema=AperturaInput)
def open_claim(placa: str, tipo: str, distrito: str, cantidad_lesionados: int,
              confirmado_por_cliente: bool = False) -> str:
    """Registra el reporte inicial de un siniestro y devuelve su código. Requiere confirmación.

    Úsala cuando el cliente comunique un accidente de tránsito que aún no ha reportado.
    Llámala primero con confirmado_por_cliente=False para obtener el mensaje de
    confirmación, y solo vuelve a llamarla con True si el cliente confirma explícitamente
    — salvo que haya lesionados: en ese caso la prioridad es derivar, no esperar.
    NO la uses para consultar un siniestro existente: para eso usa get_claim_status.
    Esta tool SOLO registra el reporte: no aprueba, no liquida y no estima indemnizaciones.
    """
    # Regla A3: el tipo de siniestro no se acepta tal cual — se normaliza contra las 5
    # categorías válidas con extraer() (comun/structured.py), ANTES de la confirmación
    # (o de la derivación por lesionados): un expediente no se abre con un tipo dudoso.
    try:
        clasificacion = extraer(
            get_chat_model(), ClasificacionSiniestro,
            f"Tipo declarado: {tipo}\nDistrito: {distrito}\nLesionados: {cantidad_lesionados}",
        )
    except ExtraccionFallida:
        return (f"Tipo de siniestro inválido: '{tipo}'. Debe ser uno de: "
                f"{', '.join(t.value for t in TipoSiniestro)}.")
    tipo_validado = clasificacion.tipo.value

    try:
        p = datos.buscar_uno("polizas.csv", "placa", placa, TRACK)
    except DatoNoEncontrado:
        return f"No hay póliza registrada para la placa {placa}. No se puede abrir el expediente."
    fin = datetime.strptime(p["fin_vigencia"], "%Y-%m-%d").date()
    if fin < HOY:
        return (f"La póliza de {placa} venció el {p['fin_vigencia']}. "
                f"Un siniestro fuera de vigencia no tiene cobertura del SOAT. "
                f"DERIVA al canal humano para orientar al cliente.")
    if not confirmado_por_cliente and cantidad_lesionados == 0:
        return (f"CONFIRMACIÓN REQUERIDA. Vas a abrir un expediente de {tipo_validado} para la placa "
                f"{placa} en {distrito}. Pregunta al cliente si confirma y solo entonces vuelve a "
                f"llamar esta tool con confirmado_por_cliente=True.")
    exp = datos.siguiente_id("siniestros.csv", "siniestro_id", "SIN-2026-", TRACK)
    urgencia = ""
    if cantidad_lesionados > 0:
        urgencia = (f"\nPRIORIDAD ALTA: {cantidad_lesionados} lesionado(s). Recuerda al cliente que los "
                    f"establecimientos de salud DEBEN atender sin exigir pago previo. "
                    f"DERIVA DE INMEDIATO al canal humano de siniestros.")
    return (f"Expediente abierto. Código: {exp} · Póliza: {p['poliza_id']} · Placa: {placa} · "
            f"Tipo: {tipo_validado} · Distrito: {distrito} · Estado: REPORTADO. "
            f"Documentación requerida: documento de identidad de las víctimas, parte policial y "
            f"certificado médico de atención. Plazo de pronunciamiento: 30 días calendario desde "
            f"la presentación completa.{urgencia}")


TOOLS_NUCLEO = [get_policy_by_plate, quote_soat, get_claim_status, open_claim]
