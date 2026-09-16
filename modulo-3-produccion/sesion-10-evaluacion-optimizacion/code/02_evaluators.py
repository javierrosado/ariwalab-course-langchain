"""Demo 2 · Los 3 evaluators determinísticos corriendo sobre una respuesta.

Ejecutar desde la raíz del curso (no requiere credenciales):
    python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/02_evaluators.py

Toma 3 filas del golden set de telecomunicaciones y 3 respuestas de agente ya
escritas a mano (una correcta, una con el dato equivocado, una sin cita) para que
se vea con claridad qué mide cada evaluator y por qué son verificables sin juicio:
se pueden correr mil veces y dan lo mismo.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comun.evaluadores import evaluar_caso, resumen  # noqa: E402

CASOS = [
    {
        "caso": {"consulta": "¿Cuál es el plan de la línea 988837195?", "categoria": "directa",
                 "tool_esperada": "get_customer_plan", "respuesta_esperada": None},
        "respuesta": "La línea 988837195 tiene el plan Pro 129.",
        "tool_llamada": "get_customer_plan",
        "contexto": None,
        "titulo": "Correcto: tool acertada, sin cita necesaria (no hay respuesta_esperada)",
    },
    {
        "caso": {"consulta": "¿Cuánto cuesta portar mi número a otro operador?", "categoria": "otro",
                 "tool_esperada": None, "respuesta_esperada": "gratuita"},
        "respuesta": "La portabilidad tiene un costo de S/15.",
        "tool_llamada": None,
        "contexto": "[Fuente: portabilidad.md]\nLa portabilidad numérica es gratuita por ley.",
        "titulo": "Alucinación: el dato NO está en la fuente ni coincide con lo esperado",
    },
    {
        "caso": {"consulta": "¿Cuánto cuesta el plan Max 89 al mes?", "categoria": "otro",
                 "tool_esperada": None, "respuesta_esperada": "S/89"},
        "respuesta": "El plan Max 89 cuesta S/89 al mes.",
        "tool_llamada": None,
        "contexto": "[Fuente: tarifario.md]\nEl plan Max 89 cuesta S/89 mensuales.",
        "titulo": "Correcto y con groundedness: la cifra está en la fuente citada",
    },
]


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · los 3 evaluators determinísticos")
    print("=" * 72)

    resultados = []
    for c in CASOS:
        r = evaluar_caso(c["caso"], c["respuesta"], c["tool_llamada"], c["contexto"])
        resultados.append(r)
        print(f"\n  {c['titulo']}")
        print(f"    tool={r['tool']}  exactitud={r['exactitud']}  groundedness={r['groundedness']}")

    print(f"\n  Resumen (n={len(resultados)}): {resumen(resultados)}")
    print("""
  Corre este script otra vez: el resultado es IDÉNTICO. Eso es lo que distingue a un
  evaluator determinístico del juez de la demo 3 — y lo que lo hace apto para calificar.
""")


if __name__ == "__main__":
    main()
