"""Demo 3 · El juez sobre 10 casos ya puntuados, con las dos columnas lado a lado.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/03_llm_as_judge.py

Requiere HF_TOKEN. Toma 10 pares (consulta, respuesta) YA puntuados por
`evaluar_exactitud()` (el evaluator determinístico) y le pide al mismo modelo del
curso (Qwen3-32B) que juzgue si la respuesta es correcta. El contenido de la demo son
los DESACUERDOS entre columnas, no el veredicto final — es donde aparece el sesgo.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comun.evaluadores import evaluar_exactitud  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

# 10 pares (consulta, respuesta_del_agente, respuesta_esperada) — construidos para que
# aparezcan los 4 sesgos del bloque 3 del README: verbosidad (caso 3), autocomplacencia
# (casos 6 y 9 son ambiguos a propósito), y para posición (no aplica: aquí es un solo
# candidato, no una comparación A/B).
CASOS = [
    ("¿Cuánto cuesta el plan Max 89?", "El plan Max 89 cuesta S/89 al mes.", "S/89"),
    ("¿Cuánto dura la garantía de un producto?", "La garantía es de 12 meses.", "12 meses"),
    ("¿Cuál es el horario de atención?", "Atendemos las 24 horas del día, los 365 días del "
     "año, sin excepción, para brindarte siempre el mejor servicio posible.", "24 horas"),
    ("¿Cuánto es el límite de transferencia diario?", "El límite es S/5000 diarios.", "S/5000"),
    ("¿Qué cubre el SOAT?", "El SOAT cubre gastos médicos y de sepelio.", "gastos médicos"),
    ("¿Puedo cambiar de plan cuando quiera?", "Sí, puedes cambiar de plan en cualquier "
     "momento sin costo.", "sin costo"),
    ("¿Cuánto tarda una devolución?", "El reembolso se procesa en 5 días hábiles.",
     "5 días hábiles"),
    ("¿Qué pasa si pierdo mi tarjeta?", "Debes bloquearla de inmediato llamando a la línea "
     "de atención.", "bloquearla de inmediato"),
    ("¿Cuál es la cobertura de la línea prepago?", "La cobertura es nacional.", "nacional"),
    ("¿Cuánto es la comisión por mantenimiento?", "No cobramos ninguna comisión de "
     "mantenimiento este mes ni el próximo.", "S/12"),
]

PROMPT_JUEZ = """Eres un juez que evalúa si una respuesta de atención al cliente es correcta.

Pregunta: {pregunta}
Respuesta del agente: {respuesta}
Dato que debería aparecer: {esperado}

Responde SOLO con "SI" si la respuesta contiene ese dato correctamente, o "NO" si no lo
contiene o lo contradice. No expliques, no repitas la pregunta."""


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · LLM-as-judge vs evaluator determinístico")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()
    desacuerdos = 0

    print(f"\n  {'#'.ljust(3)}{'Determinístico'.ljust(16)}{'Juez'.ljust(8)}{'¿Coinciden?'}")
    print("  " + "-" * 50)

    for i, (pregunta, respuesta, esperado) in enumerate(CASOS, 1):
        det = evaluar_exactitud(respuesta, esperado)
        veredicto_juez = model.invoke([
            ("human", PROMPT_JUEZ.format(pregunta=pregunta, respuesta=respuesta, esperado=esperado))
        ]).content.strip().upper()
        juez = veredicto_juez.startswith("SI")
        coincide = det == juez
        desacuerdos += not coincide
        print(f"  {str(i).ljust(3)}{str(det).ljust(16)}{str(juez).ljust(8)}"
              f"{'✔' if coincide else '✘ DESACUERDO'}")

    print(f"\n  {desacuerdos}/10 desacuerdos entre el evaluator determinístico y el juez.")
    print("""
  Mira el caso 3 (respuesta larga y muy segura de sí misma) y el caso 10 (falta el dato,
  pero suena convincente): son los candidatos típicos a que el juez apruebe algo que el
  evaluator determinístico correctamente rechaza — verbosidad y autocomplacencia, los
  sesgos del bloque 3 del README. La nota la sostiene la columna determinística.
""")


if __name__ == "__main__":
    main()
