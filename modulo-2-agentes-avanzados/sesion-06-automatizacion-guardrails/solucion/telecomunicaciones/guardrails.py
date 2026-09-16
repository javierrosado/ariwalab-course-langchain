"""L6 · Telecomunicaciones — AndesMóvil · guardrails.py (checkpoint de referencia)

Los 3 guardrails (entrada, acción, salida) + la lista de prohibidos del track. Mismo
patrón de las demos code/01 a code/03 de la sesión, aplicado al track real.
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
    r"sin\s+restricciones",
    r"soy\s+(el\s+)?supervisor",
    r"es\s+una\s+emergencia",
]


def check_input(message: str) -> tuple[bool, str]:
    """Guardrail de entrada. Devuelve (es_seguro, mensaje_para_el_usuario_si_no)."""
    lowered = message.lower()
    if any(re.search(p, lowered) for p in INJECTION_PATTERNS):
        return False, ("No puedo seguir esa instrucción. Cuéntame tu consulta sobre tu línea "
                       "o tu plan y con gusto te ayudo.")
    return True, ""


# ─────────────────────────── guardrail de acción ───────────────────────────
# Telco no tiene, en su núcleo, ninguna tool que ejecute algo irreversible por sí sola:
# create_complaint_ticket ya exige confirmación explícita (implementada en la Sesión 4).
# Aquí se refuerza esa misma regla, por si el agente cambiara de implementación.
ACTIONS_REQUIRING_CONFIRMATION = {"create_complaint_ticket"}


def check_action(tool_name: str, args: dict) -> tuple[bool, str]:
    """Guardrail de acción. Devuelve (se_ejecuta, motivo_si_no)."""
    if tool_name in ACTIONS_REQUIRING_CONFIRMATION and not args.get("confirmado_por_cliente"):
        return False, f"'{tool_name}' exige confirmación explícita del cliente antes de ejecutarse."
    return True, ""


# ─────────────────────────── guardrail de salida ───────────────────────────
DNI_PATTERN = r"\b\d{8}\b"
FORBIDDEN_OUTPUT_PATTERNS = [
    r"(te )?(ofrezco|otorgo|doy|prometo|garantizo|comprometo).{0,20}(200|compensaci[oó]n|S/\s?\d+)",
    r"portabilidad (aprobada|confirmada|procesada|ejecutada)",
    r"contrato (cancelado|dado de baja)",
    r"(consumo|gb) de (todas las l[ií]neas|otras l[ií]neas)",
]


def check_output(raw_response: str) -> str:
    """Guardrail de salida. Devuelve la respuesta segura a mostrar al usuario."""
    lowered = raw_response.lower()
    if any(re.search(p, lowered) for p in FORBIDDEN_OUTPUT_PATTERNS):
        return ("No puedo confirmar eso. Voy a derivar tu caso a un asesor humano para que "
                "revise los detalles contigo.")
    return re.sub(DNI_PATTERN, lambda m: m.group(0)[:2] + "******", raw_response)


# ─────────────────────────── escalamiento ───────────────────────────
ESCALATION_PATTERNS = [
    r"regulador|osiptel",
    r"segundo reclamo|otro reclamo|ya reclam[eé]",
    r"compensaci[oó]n",
]


def needs_escalation(message: str) -> bool:
    """Deriva a un asesor humano cuando: reclama compensación, insiste con un reclamo
    repetido, o amenaza con acudir al regulador (ver README.md de la sesión, sección 5).
    """
    lowered = message.lower()
    return any(re.search(p, lowered) for p in ESCALATION_PATTERNS)
