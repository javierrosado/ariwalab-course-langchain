"""L6 · Banca — Banco Inti · guardrails.py (checkpoint de referencia)

Los 3 guardrails (entrada, acción, salida) + la lista de prohibidos del track — el más
estricto del curso: ninguna tool mueve dinero y ninguna expone la tarjeta completa.
"""

from __future__ import annotations

import re

# ─────────────────────────── guardrail de entrada ───────────────────────────
INJECTION_PATTERNS = [
    r"ignora\s+(tus\s+)?(instrucciones|reglas)",
    r"olvida\s+(que\s+eres|tus\s+instrucciones)",
    r"act[uú]a\s+como\s+(el|un|una)\s+(gerente|administrador|supervisor|perito)",
    r"(nueva\s+)?instrucci[oó]n\s+del\s+sistema",
    r"esto\s+es\s+una\s+(prueba|simulaci[oó]n|auditor[ií]a)\s+(del\s+sistema|interna)",
    r"sin\s+restricciones|permisos\s+totales|acceso\s+total",
    r"soy\s+(el\s+)?supervisor",
    r"es\s+una\s+emergencia",
]


def check_input(message: str) -> tuple[bool, str]:
    """Guardrail de entrada. Devuelve (es_seguro, mensaje_para_el_usuario_si_no)."""
    lowered = message.lower()
    if any(re.search(p, lowered) for p in INJECTION_PATTERNS):
        return False, ("No puedo seguir esa instrucción. Cuéntame tu consulta sobre tu cuenta "
                       "o tu tarjeta y con gusto te ayudo.")
    return True, ""


# ─────────────────────────── guardrail de acción ───────────────────────────
# Banco Inti no tiene, en su núcleo, ninguna tool de escritura (ver README.md de la
# Sesión 4). Esta lista existe para el reto opcional (request_card_block) y para que
# ninguna futura tool de escritura se cuele sin este control.
PROHIBITED_ACTIONS = {"transfer_funds", "execute_transfer", "make_payment"}
ACTIONS_REQUIRING_CONFIRMATION = {"request_card_block"}


def check_action(tool_name: str, args: dict) -> tuple[bool, str]:
    """Guardrail de acción. Devuelve (se_ejecuta, motivo_si_no)."""
    if tool_name in PROHIBITED_ACTIONS:
        return False, f"'{tool_name}' está prohibida: el asistente nunca mueve dinero."
    if tool_name in ACTIONS_REQUIRING_CONFIRMATION and not args.get("confirmado_por_cliente"):
        return False, f"'{tool_name}' exige confirmación explícita del cliente antes de ejecutarse."
    return True, ""


# ─────────────────────────── guardrail de salida ───────────────────────────
DNI_PATTERN = r"\b\d{8}\b"
CARD_PATTERN = r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b"
CVV_PATTERN = r"\bcvv\s*(es|:)?\s*\d{3}\b"
FORBIDDEN_OUTPUT_PATTERNS = [
    r"transferencia (realizada|ejecutada|procesada|confirmada|hecha)",
    r"(es|confirmado como|se trata de) fraude",
    r"comisi[oó]n (anulada|exonerada|devuelta|eliminada)",
    r"acceso concedido|permisos totales",
]


def check_output(raw_response: str) -> str:
    """Guardrail de salida. Devuelve la respuesta segura a mostrar al usuario."""
    lowered = raw_response.lower()
    if any(re.search(p, lowered) for p in FORBIDDEN_OUTPUT_PATTERNS):
        return ("No puedo confirmar eso. Voy a derivar tu caso a un asesor humano para que "
                "revise los detalles contigo.")
    masked = re.sub(DNI_PATTERN, lambda m: m.group(0)[:2] + "******", raw_response)
    masked = re.sub(CARD_PATTERN, lambda m: "**** **** **** " + re.sub(r"[ -]", "", m.group(0))[-4:], masked)
    masked = re.sub(CVV_PATTERN, "CVV ***", masked, flags=re.IGNORECASE)
    return masked


# ─────────────────────────── escalamiento ───────────────────────────
ESCALATION_PATTERNS = [
    r"fraude|sospech\w*",
    r"bloque\w*\s+(mi\s+)?tarjeta",
    r"compart[ií]\s+(mi|mis)\s+(clave|contrase[ñn]a|c[oó]digo)",
]


def needs_escalation(message: str) -> bool:
    """Deriva de inmediato ante sospecha de fraude, pedido de bloqueo de tarjeta, o si
    el cliente compartió sus claves con un tercero (ver README.md, sección 5).
    """
    lowered = message.lower()
    return any(re.search(p, lowered) for p in ESCALATION_PATTERNS)
