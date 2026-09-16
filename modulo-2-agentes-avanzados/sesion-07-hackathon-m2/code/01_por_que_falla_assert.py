"""Demo 1 · Por qué `assert respuesta == "esperado"` falla con un agente real.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-07-hackathon-m2/code/01_por_que_falla_assert.py

Requiere HF_TOKEN. Usa el agente de referencia de la Sesión 6 (telecomunicaciones).

Qué deberías observar:
  1. La misma pregunta, hecha dos veces, produce dos textos distintos incluso
     cuando el CONTENIDO es correcto en ambos casos.
  2. `assert respuesta == esperado` falla las dos veces (o casi), aunque el agente
     "acertó" las dos veces desde el punto de vista de negocio.
  3. Un invariante (`"Max 89" in respuesta` o similar) SÍ captura lo que de verdad
     importa: que el dato correcto esté ahí, sin exigir el texto exacto.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-06-automatizacion-guardrails"
                       / "solucion" / "telecomunicaciones"))

from comun.provider import describe_provider  # noqa: E402

from agent import responder  # noqa: E402  (checkpoint de referencia de la S6)

PREGUNTA = "¿Cuánto cuesta el plan Max 89 al mes?"
DATO_QUE_IMPORTA = "89"  # el precio, no el texto exacto de la respuesta


def assert_exacto(respuesta: str, esperado: str) -> bool:
    return respuesta.strip() == esperado.strip()


def assert_invariante(respuesta: str, dato: str) -> bool:
    return dato in respuesta


def main() -> None:
    print("=" * 72)
    print("  DEMO 1 · Por qué falla assert ==")
    print(f"  {describe_provider()}")
    print("=" * 72)
    print(f"\n  Pregunta (se hace 2 veces): {PREGUNTA}\n")

    respuestas = []
    for i in (1, 2):
        try:
            r = responder(PREGUNTA)
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error: {type(e).__name__}: {e}")
            return
        respuestas.append(r)
        print(f"  Intento {i}: {r[:200]}{'...' if len(r) > 200 else ''}\n")

    print("  " + "-" * 68)
    print(f"  ¿Las dos respuestas son EXACTAMENTE iguales? "
          f"{'sí' if respuestas[0].strip() == respuestas[1].strip() else 'no'}")
    print(f"  assert respuesta == respuesta_anterior  → "
          f"{'PASA' if assert_exacto(respuestas[0], respuestas[1]) else 'FALLA'}")
    print(f"\n  ¿Las dos mencionan el dato correcto ({DATO_QUE_IMPORTA})?")
    for i, r in enumerate(respuestas, start=1):
        print(f"    Intento {i}: assert '{DATO_QUE_IMPORTA}' in respuesta → "
              f"{'PASA' if assert_invariante(r, DATO_QUE_IMPORTA) else 'FALLA'}")

    print("""

  La comparación exacta depende de cómo el modelo decidió REDACTAR la respuesta esa
  vez — cambia con el fraseo, el orden de las palabras, hasta con espacios. El
  invariante depende de si el DATO correcto está presente, que es lo único que le
  importa a tu cliente. Por eso el L7 se prueba con invariantes, no con igualdades.
""")


if __name__ == "__main__":
    main()
