"""L4 · Seguros — Andina Seguros · domain_tools.py (checkpoint de referencia)

Las 4 tools núcleo del track. La primera (`get_policy_by_plate`) es la del L3; las
otras tres son el incremento del L4. `open_claim` exige confirmación explícita antes
de abrir el expediente (regla del bloque 4 de README.md).

Regla A2: cada docstring dice QUÉ hace, CUÁNDO usarla y CUÁNDO NO.
"""

from __future__ import annotations

import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402

TRACK = "seguros"
HOY = date(2026, 9, 5)  # fecha de referencia del curso


# ───────────────────────────── esquemas ─────────────────────────────
class PlacaInput(BaseModel):
    placa: str = Field(description="Placa del vehículo en formato ABC-123")


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


# ─────────────────────────── tool del L3 (ya la tenías) ───────────────────────────
@tool(args_schema=PlacaInput)
def get_policy_by_plate(placa: str) -> str:
    """Devuelve la póliza SOAT asociada a una placa, con su vigencia y estado.

    Úsala cuando el cliente pregunte si su SOAT está vigente, hasta cuándo,
    o quiera los datos de su póliza.
    NO la uses para cotizar una póliza nueva: para eso usa quote_soat.
    """
    try:
        p = datos.buscar_uno("polizas.csv", "placa", placa, TRACK)
    except DatoNoEncontrado:
        return (f"No hay ninguna póliza de Andina Seguros para la placa {placa}. "
                f"Verifica la placa con el cliente: el formato es ABC-123.")
    fin = datetime.strptime(p["fin_vigencia"], "%Y-%m-%d").date()
    dias = (fin - HOY).days
    if dias < 0:
        estado = f"VENCIDA hace {abs(dias)} días. El vehículo circula en infracción."
    elif dias <= 30:
        estado = f"VIGENTE, pero vence en {dias} días. Conviene renovar."
    else:
        estado = f"VIGENTE, vence en {dias} días."
    return (f"Póliza {p['poliza_id']} · Placa {p['placa']} · Titular: {p['titular']} · "
            f"Vigencia: {p['inicio_vigencia']} al {p['fin_vigencia']} · Prima: S/ {p['prima_soles']} · "
            f"Modalidad: {p['modalidad']} · {estado}")


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
    tipos = {"CHOQUE_SIMPLE", "ATROPELLO", "VOLCADURA", "COLISION_MULTIPLE", "DESPISTE"}
    tipo = tipo.strip().upper()
    if tipo not in tipos:
        return f"Tipo de siniestro inválido: '{tipo}'. Debe ser uno de: {', '.join(sorted(tipos))}."
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
        return (f"CONFIRMACIÓN REQUERIDA. Vas a abrir un expediente de {tipo} para la placa {placa} "
                f"en {distrito}. Pregunta al cliente si confirma y solo entonces vuelve a llamar "
                f"esta tool con confirmado_por_cliente=True.")
    exp = datos.siguiente_id("siniestros.csv", "siniestro_id", "SIN-2026-", TRACK)
    urgencia = ""
    if cantidad_lesionados > 0:
        urgencia = (f"\nPRIORIDAD ALTA: {cantidad_lesionados} lesionado(s). Recuerda al cliente que los "
                    f"establecimientos de salud DEBEN atender sin exigir pago previo. "
                    f"DERIVA DE INMEDIATO al canal humano de siniestros.")
    return (f"Expediente abierto. Código: {exp} · Póliza: {p['poliza_id']} · Placa: {placa} · "
            f"Tipo: {tipo} · Distrito: {distrito} · Estado: REPORTADO. "
            f"Documentación requerida: documento de identidad de las víctimas, parte policial y "
            f"certificado médico de atención. Plazo de pronunciamiento: 30 días calendario desde "
            f"la presentación completa.{urgencia}")


TOOLS_NUCLEO = [get_policy_by_plate, quote_soat, get_claim_status, open_claim]
