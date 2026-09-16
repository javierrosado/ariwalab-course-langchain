"""Demo 3 · El juez sobre 10 casos ya puntuados, con las dos columnas lado a lado.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/03_llm_as_judge.py

Requiere HF_TOKEN. Toma 10 pares (consulta, respuesta) YA puntuados por
`evaluar_exactitud()` (el evaluator determinístico) y le pide al mismo modelo del
curso (Qwen3-32B) que juzgue si la respuesta es correcta. El contenido de la demo son
los DESACUERDOS entre columnas, no el veredicto final — es donde aparece el sesgo.

**El juez responde con `Veredicto`, extraído con `comun.structured.extraer()` (regla
A3) — no con texto libre parseado a mano.** Un juez que se usa para enseñar por qué
`assert respuesta == "esperado"` no sirve, y que él mismo devuelve un "SI"/"NO" sin
validar, contradice lo que la propia sesión enseña (hallazgo H7 de
`docente/esqueletos/VALIDACION-INTEGRAL.md`).
"""

from __future__ import annotations

import sys
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from pydantic import BaseModel, Field  # noqa: E402

from comun.evaluadores import evaluar_exactitud  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida, extraer  # noqa: E402


class Confianza(str, Enum):
    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAJA = "BAJA"


class Veredicto(BaseModel):
    """Veredicto del juez sobre si una respuesta de atención al cliente es correcta."""

    aprueba: bool = Field(description="True si la respuesta contiene el dato correcto")
    motivo: str = Field(description="Justificación en una frase, citando el dato comparado")
    confianza: Confianza = Field(description="Qué tan seguro está el juez de su propio veredicto")

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

Decide si la respuesta contiene ese dato correctamente, con qué confianza, y por qué."""


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · LLM-as-judge vs evaluator determinístico")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()
    desacuerdos = 0

    print(f"\n  {'#'.ljust(3)}{'Determinístico'.ljust(16)}{'Juez'.ljust(8)}"
          f"{'Confianza'.ljust(11)}{'¿Coinciden?'}")
    print("  " + "-" * 62)

    for i, (pregunta, respuesta, esperado) in enumerate(CASOS, 1):
        det = evaluar_exactitud(respuesta, esperado)
        entrada = PROMPT_JUEZ.format(pregunta=pregunta, respuesta=respuesta, esperado=esperado)
        try:
            veredicto = extraer(model, Veredicto, entrada)
        except ExtraccionFallida as e:
            print(f"  {str(i).ljust(3)}{'—'.ljust(16)}{'—'.ljust(8)}{'—'.ljust(11)}"
                  f"✘ el juez no produjo un veredicto válido: {e}")
            continue
        coincide = det == veredicto.aprueba
        desacuerdos += not coincide
        print(f"  {str(i).ljust(3)}{str(det).ljust(16)}{str(veredicto.aprueba).ljust(8)}"
              f"{veredicto.confianza.value.ljust(11)}{'✔' if coincide else '✘ DESACUERDO'}")
        if not coincide:
            print(f"      motivo del juez: {veredicto.motivo}")

    print(f"\n  {desacuerdos}/10 desacuerdos entre el evaluator determinístico y el juez.")
    print("""
  Mira el caso 3 (respuesta larga y muy segura de sí misma) y el caso 10 (falta el dato,
  pero suena convincente): son los candidatos típicos a que el juez apruebe algo que el
  evaluator determinístico correctamente rechaza — verbosidad y autocomplacencia, los
  sesgos del bloque 3 del README. La nota la sostiene la columna determinística.
""")


if __name__ == "__main__":
    main()
