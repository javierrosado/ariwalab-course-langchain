"""Demo 3 · Repetir y medir: una prueba que pasa 4 de 5 veces está midiendo.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-07-hackathon-m2/code/03_repetir_y_medir.py

Requiere HF_TOKEN. Usa el agente de referencia de la Sesión 6 (telecomunicaciones).

Qué deberías observar: la misma pregunta, repetida varias veces, no siempre
cumple el mismo invariante. Eso NO es un bug de tu agente ni de esta demo — es
la fiabilidad compuesta medida en testing en vez de en selección de tools.
Un 4/5 es información ("¿por qué falló esa vez?"), no un fallo binario.
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

REPETICIONES = 5
PREGUNTA = "¿Cuánto cuesta el plan Max 89 al mes?"


def cumple_invariante(respuesta: str) -> bool:
    """El invariante de esta demo: la respuesta debe mencionar el precio (89)."""
    return "89" in respuesta


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · Repetir y medir")
    print(f"  {describe_provider()}")
    print("=" * 72)
    print(f"\n  Pregunta (se repite {REPETICIONES} veces): {PREGUNTA}\n")

    resultados = []
    for i in range(1, REPETICIONES + 1):
        try:
            r = responder(PREGUNTA)
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error en el intento {i}: {type(e).__name__}: {e}")
            resultados.append(False)
            continue
        ok = cumple_invariante(r)
        resultados.append(ok)
        print(f"  Intento {i}: {'✔ cumple' if ok else '✘ NO cumple'} el invariante")
        print(f"    \"{r[:120]}{'...' if len(r) > 120 else ''}\"")

    exitos = sum(resultados)
    tasa = 100 * exitos / len(resultados)
    print(f"\n  RESULTADO: {exitos}/{len(resultados)} = {tasa:.0f} % cumplió el invariante")

    print(f"""

  Si el resultado fue {exitos}/{REPETICIONES} y no {REPETICIONES}/{REPETICIONES}: eso NO
  significa que tu agente esté roto. Significa que estás MIDIENDO su fiabilidad en
  esta tarea concreta — que es exactamente lo que un test de un sistema no
  determinístico debe hacer. Un test de un solo intento no te habría dicho esto.
""")


if __name__ == "__main__":
    main()
