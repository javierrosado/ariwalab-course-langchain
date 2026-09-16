"""Tools del asistente de banca personal — Banco Inti.

4 tools núcleo (Laboratorio 4) + 2 opcionales de reto.

Este es el track con guardrails más estrictos: ninguna tool mueve dinero,
ninguna expone el número completo de una tarjeta, y las acciones irreversibles
solo se preparan, nunca se ejecutan sin confirmación explícita del cliente.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from comun import datos
from comun.datos import DatoNoEncontrado

TRACK = "banca"
HOY = date(2026, 9, 5)  # fecha de referencia del curso


# ───────────────────────────── esquemas ─────────────────────────────
class CuentaInput(BaseModel):
    numero_cuenta: str = Field(description="Número de cuenta en formato 191-XXXXXXX-0-XX")


class MovimientosInput(BaseModel):
    numero_cuenta: str = Field(description="Número de cuenta en formato 191-XXXXXXX-0-XX")
    dias: int = Field(default=30, ge=1, le=90, description="Días hacia atrás a consultar, entre 1 y 90")


class MovimientoInput(BaseModel):
    movimiento_id: str = Field(description="Identificador del movimiento en formato MOV-NNNNNNN")


class BloqueoInput(BaseModel):
    tarjeta_id: str = Field(description="Identificador de la tarjeta en formato TC-NNNNN")
    confirmado_por_cliente: bool = Field(
        default=False,
        description="True solo si el cliente confirmó explícitamente el bloqueo en este turno de la conversación",
    )


# ─────────────────────────── tools núcleo ───────────────────────────
@tool(args_schema=CuentaInput)
def get_account_balance(numero_cuenta: str) -> str:
    """Devuelve el saldo, la moneda y el estado de una cuenta.

    Úsala cuando el cliente pregunte cuánto tiene, su saldo disponible,
    o si su cuenta está activa o bloqueada.
    NO la uses para ver movimientos o consumos: para eso usa list_transactions.
    """
    try:
        c = datos.buscar_uno("cuentas.csv", "numero_cuenta", numero_cuenta, TRACK)
    except DatoNoEncontrado:
        return (f"No existe la cuenta {numero_cuenta} en Banco Inti. "
                f"Verifica el número con el cliente: el formato es 191-XXXXXXX-0-XX.")
    simbolo = "S/" if c["moneda"] == "PEN" else "USD"
    alerta = " ATENCIÓN: la cuenta está BLOQUEADA." if c["estado"] == "BLOQUEADA" else ""
    return (f"Cuenta {c['numero_cuenta']} ({c['tipo_cuenta']}) · Titular: {c['titular']} · "
            f"Saldo: {simbolo} {c['saldo']} · Estado: {c['estado']}.{alerta}")


@tool(args_schema=MovimientosInput)
def list_transactions(numero_cuenta: str, dias: int = 30) -> str:
    """Lista los movimientos de una cuenta en los últimos N días, del más reciente al más antiguo.

    Úsala cuando el cliente pregunte por sus consumos, sus últimos movimientos,
    un cargo que no reconoce, o cuánto gastó en un periodo.
    NO la uses para consultar el saldo: para eso usa get_account_balance.
    """
    try:
        datos.buscar_uno("cuentas.csv", "numero_cuenta", numero_cuenta, TRACK)
    except DatoNoEncontrado:
        return f"No existe la cuenta {numero_cuenta}."
    corte = HOY - timedelta(days=dias)
    movs = [m for m in datos.buscar_todos("movimientos.csv", "numero_cuenta", numero_cuenta, TRACK)
            if datetime.strptime(m["fecha"], "%Y-%m-%d").date() >= corte]
    if not movs:
        return f"La cuenta {numero_cuenta} no registra movimientos en los últimos {dias} días."
    movs.sort(key=lambda m: m["fecha"], reverse=True)
    lineas = [f"{m['fecha']} · {m['descripcion']} · S/ {m['monto']} · {m['canal']} · {m['movimiento_id']}"
              for m in movs[:15]]
    total_cargos = sum(float(m["monto"]) for m in movs if m["tipo"] == "CARGO")
    resumen = (f"{len(movs)} movimientos en {dias} días · "
               f"Total de cargos: S/ {abs(total_cargos):.2f}")
    extra = f"\n(Se muestran los 15 más recientes de {len(movs)})" if len(movs) > 15 else ""
    return resumen + "\n" + "\n".join(lineas) + extra


@tool(args_schema=CuentaInput)
def get_card_info(numero_cuenta: str) -> str:
    """Devuelve los datos de la tarjeta asociada a una cuenta, con el número enmascarado.

    Úsala cuando el cliente pregunte por su tarjeta, su línea de crédito,
    su fecha de facturación o si su tarjeta está activa.
    NO la uses para bloquear la tarjeta: para eso usa request_card_block.
    Esta tool NUNCA devuelve el número completo de la tarjeta, solo los últimos 4 dígitos.
    """
    tarjetas = datos.buscar_todos("tarjetas.csv", "numero_cuenta", numero_cuenta, TRACK)
    if not tarjetas:
        return f"La cuenta {numero_cuenta} no tiene tarjetas asociadas registradas."
    salida = []
    for t in tarjetas:
        salida.append(
            f"Tarjeta {t['tarjeta_id']} ({t['marca']}) terminada en {t['ultimos_4_digitos']} · "
            f"Estado: {t['estado']} · Línea de crédito: S/ {t['linea_credito']} · "
            f"Facturación el día {t['dia_facturacion']} de cada mes"
        )
    return "\n".join(salida)


@tool(args_schema=MovimientoInput)
def score_transaction_risk(movimiento_id: str) -> str:
    """Devuelve el puntaje de riesgo de fraude de un movimiento y el motivo de la alerta.

    Úsala cuando el cliente diga que no reconoce una operación, sospeche de un cargo,
    o pregunte por qué le llegó una alerta de seguridad.
    NO la uses para listar movimientos: primero usa list_transactions para obtener el
    movimiento_id, y recién entonces evalúa el riesgo de ese movimiento concreto.
    """
    try:
        mov = datos.buscar_uno("movimientos.csv", "movimiento_id", movimiento_id, TRACK)
    except DatoNoEncontrado:
        return (f"No existe el movimiento {movimiento_id}. "
                f"Usa list_transactions para obtener los identificadores válidos.")
    alertas = datos.buscar_todos("alertas_riesgo.csv", "movimiento_id", movimiento_id, TRACK)
    base = (f"Movimiento {movimiento_id}: {mov['descripcion']} · S/ {mov['monto']} · "
            f"{mov['fecha']} · canal {mov['canal']} · ubicación {mov['ubicacion']}")
    if not alertas:
        return base + "\nSin alerta de riesgo asociada: el puntaje quedó por debajo de 55 (riesgo bajo)."
    a = alertas[0]
    score = int(a["score_riesgo"])
    nivel = "ALTO" if score >= 80 else "MEDIO"
    accion = ("Riesgo ALTO: requiere confirmación del cliente y derivación a un asesor humano."
              if score >= 80 else
              "Riesgo MEDIO: la operación se procesó y se notificó al cliente.")
    return (base + f"\nAlerta {a['alerta_id']} · Puntaje: {score}/100 (riesgo {nivel}) · "
            f"Motivo: {a['motivo']} · Estado: {a['estado']}\n{accion}")


# ────────────────────────── tools opcionales ──────────────────────────
@tool(args_schema=CuentaInput)
def get_transfer_limits(numero_cuenta: str) -> str:
    """Devuelve los límites de transferencia vigentes de una cuenta.

    Úsala cuando el cliente pregunte cuánto puede transferir al día o por qué le
    rechazaron una transferencia por monto.
    NO la uses para ejecutar transferencias: el asistente NUNCA transfiere dinero.
    """
    try:
        c = datos.buscar_uno("cuentas.csv", "numero_cuenta", numero_cuenta, TRACK)
    except DatoNoEncontrado:
        return f"No existe la cuenta {numero_cuenta}."
    limites = {"AHORROS": (3000, 10000), "SUELDO": (5000, 15000), "CORRIENTE": (10000, 50000)}
    diario, mensual = limites.get(c["tipo_cuenta"], (3000, 10000))
    return (f"Cuenta {numero_cuenta} ({c['tipo_cuenta']}): límite diario S/ {diario:,} · "
            f"límite mensual S/ {mensual:,} · billetera IntiPay hasta S/ 500 diarios. "
            f"El cliente puede modificar sus límites desde la aplicación.")


@tool(args_schema=BloqueoInput)
def request_card_block(tarjeta_id: str, confirmado_por_cliente: bool = False) -> str:
    """Prepara el bloqueo de una tarjeta. El bloqueo es IRREVERSIBLE.

    Úsala cuando el cliente reporte robo, pérdida o uso no autorizado de su tarjeta.
    Llámala primero con confirmado_por_cliente=False para obtener el mensaje de
    confirmación, y solo vuelve a llamarla con True si el cliente confirma explícitamente.
    NO la uses por iniciativa propia ni ante una simple sospecha sin pedido del cliente.
    """
    try:
        t = datos.buscar_uno("tarjetas.csv", "tarjeta_id", tarjeta_id, TRACK)
    except DatoNoEncontrado:
        return f"No existe la tarjeta {tarjeta_id}."
    if t["estado"] == "BLOQUEADA":
        return f"La tarjeta {tarjeta_id} terminada en {t['ultimos_4_digitos']} ya está BLOQUEADA."
    if not confirmado_por_cliente:
        return (f"CONFIRMACIÓN REQUERIDA. Vas a bloquear la tarjeta {t['marca']} terminada en "
                f"{t['ultimos_4_digitos']}. El bloqueo es IRREVERSIBLE: la tarjeta no se reactiva, "
                f"se repone con un plástico nuevo y otro número. Pregunta al cliente si confirma "
                f"y solo entonces vuelve a llamar esta tool con confirmado_por_cliente=True.")
    return (f"Bloqueo registrado para la tarjeta terminada en {t['ultimos_4_digitos']}. "
            f"La reposición es gratuita la primera vez en el año. "
            f"DERIVA AHORA la conversación a un asesor humano para completar el trámite.")


TOOLS_NUCLEO = [get_account_balance, list_transactions, get_card_info, score_transaction_risk]
TOOLS_OPCIONALES = [get_transfer_limits, request_card_block]
