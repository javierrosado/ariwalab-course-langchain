"""Demo 2 · Temperatura: por qué la misma pregunta da respuestas distintas.

Ejecutar desde la raíz del curso:
    python 00-preparacion/code/02_temperatura.py

Requiere HF_TOKEN en el .env.

Qué deberías observar:
  1. A temperatura 0 las tres ejecuciones se parecen mucho entre sí.
  2. A temperatura 1.5 divergen, y a veces se vuelven poco fiables.
  3. Temperatura 0 NO garantiza respuestas idénticas: reduce la variabilidad,
     no la elimina. Diseña asumiéndolo.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from comun.provider import get_chat_model, describe_provider  # noqa: E402

PREGUNTA = "En una sola frase, explica qué es un agente de IA a un ingeniero de software."
TEMPERATURAS = [0.0, 0.7, 1.5]
REPETICIONES = 3


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · Temperatura")
    print(f"  {describe_provider()}")
    print("=" * 72)
    print(f"\n  Pregunta: {PREGUNTA}\n")

    resultados: dict[float, list[str]] = {}

    for temp in TEMPERATURAS:
        print(f"\n  ── temperature = {temp} " + "─" * 45)
        modelo = get_chat_model(temperature=temp)
        respuestas = []
        for i in range(1, REPETICIONES + 1):
            try:
                texto = (modelo.invoke(PREGUNTA).content or "").strip().replace("\n", " ")
            except Exception as e:  # noqa: BLE001
                print(f"\n  ❌ Error al llamar al modelo: {type(e).__name__}: {e}")
                print("     Revisa HF_TOKEN en tu .env y que tenga permiso de inferencia.")
                return
            respuestas.append(texto)
            print(f"   {i}. {texto[:150]}{'...' if len(texto) > 150 else ''}")
        resultados[temp] = respuestas

    # ── Medición simple de divergencia ─────────────────────────────────────
    print("\n\n  ── ¿Cuánto se parecen entre sí? " + "─" * 37)
    print(f"\n  {'Temperatura':>12} {'Idénticas':>11} {'Palabras compartidas':>22}")
    print("  " + "-" * 48)

    for temp, respuestas in resultados.items():
        identicas = "sí" if len(set(respuestas)) == 1 else "no"
        conjuntos = [set(r.lower().split()) for r in respuestas]
        comunes = set.intersection(*conjuntos) if conjuntos else set()
        union = set.union(*conjuntos) if conjuntos else set()
        solapamiento = len(comunes) / len(union) * 100 if union else 0
        print(f"  {temp:>12} {identicas:>11} {solapamiento:>21.0f}%")

    print("""

  Qué significa esto

    · temperature=0    → úsala SIEMPRE en agentes, tools y clasificación.
                         Necesitas que la elección de herramienta sea reproducible.

    · temperature=0.7  → conversación con el usuario final, donde variar está bien.

    · temperature=1.5  → redacción creativa. Nunca en un flujo de negocio.

  Fíjate en que ni siquiera con temperature=0 las respuestas son necesariamente
  idénticas. Hay no determinismo en el hardware y el paralelismo del servidor.
  Por eso, en la sesión 10, evaluarás tu agente con métricas y no con
  comparaciones exactas de texto.
""")


if __name__ == "__main__":
    main()
