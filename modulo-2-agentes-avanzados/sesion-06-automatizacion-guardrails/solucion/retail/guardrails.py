"""L6 · Retail — MercaSur · guardrails.py (checkpoint de referencia)

Los 3 guardrails (entrada, acción, salida) + la lista de prohibidos del track.
"""

from __future__ import annotations

import re

# ─────────────────────────── guardrail de entrada ───────────────────────────
INJECTION_PATTERNS = [
    r"ignora\s+(tus\s+)?(instrucciones|reglas|pol[ií]ticas)",
    r"olvida\s+(que\s+eres|tus\s+instrucciones|las\s+reglas)",
    r"act[uú]a\s+como\s+(el|un|una)\s+(gerente|administrador|supervisor)",
    r"(nueva\s+)?instrucci[oó]n\s+del\s+sistema",
    r"esto\s+es\s+una\s+(prueba|simulaci[oó]n|auditor[ií]a)\s+(del\s+sistema|interna)",
    r"sin\s+restricciones|autorizaci[oó]n\s+total",
    r"periodista|noticias",
    r"es\s+urgente|me\s+despide",
]


def check_input(message: str) -> tuple[bool, str]:
    """Guardrail de entrada. Devuelve (es_seguro, mensaje_para_el_usuario_si_no)."""
    lowered = message.lower()
    if any(re.search(p, lowered) for p in INJECTION_PATTERNS):
        return False, ("No puedo seguir esa instrucción. Cuéntame tu consulta sobre tu pedido "
                       "y con gusto te ayudo.")
    return True, ""


# ─────────────────────────── guardrail de acción ───────────────────────────
PROHIBITED_ACTIONS = {"force_approve_return", "override_delivery_policy"}


def check_action(tool_name: str, args: dict) -> tuple[bool, str]:
    """Guardrail de acción. Devuelve (se_ejecuta, motivo_si_no)."""
    if tool_name in PROHIBITED_ACTIONS:
        return False, f"'{tool_name}' está prohibida: el asistente no aprueba devoluciones ni fuerza plazos."
    if tool_name == "start_return_request" and not args.get("confirmado_por_cliente"):
        return False, f"'{tool_name}' exige confirmación explícita del cliente antes de ejecutarse."
    return True, ""


# ─────────────────────────── guardrail de salida ───────────────────────────
FORBIDDEN_OUTPUT_PATTERNS = [
    r"devoluci[oó]n (aprobada|autorizada|confirmada|aceptada)",
    r"(garantiz|asegur)\w*.{0,20}24\s*horas",
    r"50\s?%.{0,20}(descuento|aprobado|autorizado)",
    r"reembolsad[oa]|reembolso (realizado|procesado|confirmado|hecho)",
    r"(aqu[ií] tienes|te doy|usa) (el|este) cup[oó]n",
]


def check_output(raw_response: str) -> str:
    """Guardrail de salida. Devuelve la respuesta segura a mostrar al usuario."""
    lowered = raw_response.lower()
    if any(re.search(p, lowered) for p in FORBIDDEN_OUTPUT_PATTERNS):
        return ("No puedo confirmar eso todavía: el área de post-venta debe autorizarlo. "
                "Voy a derivar tu caso.")
    return raw_response


# ─────────────────────────── escalamiento ───────────────────────────
ESCALATION_PATTERNS = [
    r"libro de reclamaciones",
    r"insist\w*.{0,20}(devoluci[oó]n|fuera de pol[ií]tica)",
    r"dos intentos|varios intentos|no me lo entregan",
]


def needs_escalation(message: str) -> bool:
    """Deriva a post-venta cuando el cliente insiste con una devolución fuera de
    política, hay entregas fallidas repetidas, o pide el Libro de Reclamaciones.
    """
    lowered = message.lower()
    return any(re.search(p, lowered) for p in ESCALATION_PATTERNS)
