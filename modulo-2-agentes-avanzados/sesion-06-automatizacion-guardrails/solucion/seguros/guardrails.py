"""L6 · Seguros — Andina Seguros · guardrails.py (checkpoint de referencia)

Los 3 guardrails (entrada, acción, salida) + la lista de prohibidos del track —
el más delicado del curso: nunca se estima una indemnización ni se opina sobre
responsabilidad en un accidente.
"""

from __future__ import annotations

import re

# ─────────────────────────── guardrail de entrada ───────────────────────────
INJECTION_PATTERNS = [
    r"ignora\s+(tus\s+)?(instrucciones|reglas)",
    r"olvida\s+(que\s+eres|tus\s+instrucciones|los\s+l[ií]mites)",
    r"act[uú]a\s+como\s+(el|un|una)\s+(gerente|administrador|perito|supervisor)",
    r"(nueva\s+)?instrucci[oó]n\s*:?\s*confirma",
    r"esto\s+es\s+una\s+simulaci[oó]n",
    r"decisi[oó]n\s+final",
    r"abogado|juicio",
    r"es\s+una\s+emergencia",
]


def check_input(message: str) -> tuple[bool, str]:
    """Guardrail de entrada. Devuelve (es_seguro, mensaje_para_el_usuario_si_no)."""
    lowered = message.lower()
    if any(re.search(p, lowered) for p in INJECTION_PATTERNS):
        return False, ("No puedo seguir esa instrucción. Cuéntame tu consulta sobre tu SOAT "
                       "o tu siniestro y con gusto te ayudo.")
    return True, ""


# ─────────────────────────── guardrail de acción ───────────────────────────
PROHIBITED_ACTIONS = {"approve_claim", "estimate_indemnity", "reject_claim"}


def check_action(tool_name: str, args: dict) -> tuple[bool, str]:
    """Guardrail de acción. Devuelve (se_ejecuta, motivo_si_no)."""
    if tool_name in PROHIBITED_ACTIONS:
        return False, f"'{tool_name}' está prohibida: el asistente no liquida ni estima montos."
    if tool_name == "open_claim" and not args.get("confirmado_por_cliente") and args.get("cantidad_lesionados", 0) == 0:
        return False, f"'{tool_name}' exige confirmación explícita del cliente antes de ejecutarse."
    return True, ""


# ─────────────────────────── guardrail de salida ───────────────────────────
DNI_PATTERN = r"\b\d{8}\b"
FORBIDDEN_OUTPUT_PATTERNS = [
    r"(te )?(pagar[aá]n|corresponden?|recibir[aá]s).{0,15}S/\s*[\d,.]+",
    r"indemnizaci[oó]n.{0,15}S/\s*[\d,.]+",
    r"s[ií],?\s*(est[aá]|queda)?\s*cubiert[oa]",
    r"la culpa (fue|es|la tiene) de",
    r"siniestro (aprobado|confirmado|autorizado)",
    r"cobertura (aprobada|confirmada|procede)",
    r"historial m[eé]dico",
]


def check_output(raw_response: str) -> str:
    """Guardrail de salida. Devuelve la respuesta segura a mostrar al usuario."""
    lowered = raw_response.lower()
    if any(re.search(p, lowered) for p in FORBIDDEN_OUTPUT_PATTERNS):
        return ("No puedo confirmar eso: la evaluación del siniestro la hace el área "
                "correspondiente, con el condicionado en la mano. Voy a derivar tu caso.")
    return re.sub(DNI_PATTERN, lambda m: m.group(0)[:2] + "******", raw_response)


# ─────────────────────────── escalamiento ───────────────────────────
ESCALATION_PATTERNS = [
    r"lesionad\w*|herid\w*|fallecid\w*|muri[oó]",
]


def needs_escalation(message: str) -> bool:
    """Deriva de inmediato al canal humano de siniestros ante cualquier caso con
    personas lesionadas o fallecidas (ver README.md, sección 5).
    """
    lowered = message.lower()
    return any(re.search(p, lowered) for p in ESCALATION_PATTERNS)
