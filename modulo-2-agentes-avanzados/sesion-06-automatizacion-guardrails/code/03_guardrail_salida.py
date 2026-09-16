"""Demo 3 · Guardrail de salida: un DNI que se coló en la respuesta se enmascara.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/code/03_guardrail_salida.py

No requiere HF_TOKEN: las "respuestas del modelo" están simuladas para mostrar el
guardrail de forma determinista.

Qué deberías observar:
  1. Una respuesta limpia pasa sin cambios.
  2. Una respuesta que reveló un DNI completo se enmascara ANTES de llegar al usuario.
  3. Una respuesta con una promesa prohibida ("te garantizo", "compensación de S/ 200")
     se detecta y se reemplaza, no solo se registra.
"""

from __future__ import annotations

import re

DNI_PATTERN = r"\b\d{8}\b"
CARD_PATTERN = r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b"
FORBIDDEN_PROMISE_PATTERNS = [
    r"te\s+(prometo|garantizo|comprometo)",
    r"compensaci[oó]n\s+de\s+S/",
    r"transferencia\s+(realizada|ejecutada|confirmada)",
]


def mask_pii(text: str) -> str:
    text = re.sub(DNI_PATTERN, lambda m: m.group(0)[:2] + "******", text)
    text = re.sub(CARD_PATTERN, lambda m: "**** **** **** " + m.group(0)[-4:], text)
    return text


def contains_forbidden_promise(text: str) -> str | None:
    lowered = text.lower()
    for pattern in FORBIDDEN_PROMISE_PATTERNS:
        if re.search(pattern, lowered):
            return pattern
    return None


def check_output(raw_response: str) -> str:
    """Guardrail de salida. Devuelve la respuesta segura a mostrar al usuario."""
    if contains_forbidden_promise(raw_response):
        return ("No puedo confirmar eso. Voy a derivar tu caso a un asesor humano para que "
                "revise los detalles contigo.")
    return mask_pii(raw_response)


RAW_RESPONSES = [
    "Tu línea 987654321 tiene el plan Max 89 activo.",
    "El titular registrado es Juan Pérez, DNI 45678912, distrito Miraflores.",
    "Tu tarjeta terminada en 4551 0022 8899 1234 tiene línea de crédito de S/ 5000.",
    "Te garantizo una compensación de S/ 200 por los días sin servicio.",
]


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · Guardrail de salida")
    print("=" * 72)

    for raw in RAW_RESPONSES:
        print(f"\n  Respuesta cruda del modelo: {raw}")
        safe = check_output(raw)
        marca = "✔ sin cambios" if safe == raw else "🔧 modificada"
        print(f"  [{marca}] Respuesta al usuario: {safe}")

    print("""

  Nota que el guardrail de salida no solo "avisa": REEMPLAZA la respuesta insegura. Un
  guardrail que solo registra la filtración en un log no evita que el usuario la reciba.
""")


if __name__ == "__main__":
    main()
