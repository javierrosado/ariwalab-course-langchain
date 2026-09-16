"""Demo 1 · Primer llamado: describe_provider() + un modelo real, sin instalar nada.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-01-fundamentos-agentes/code/01_primer_llamado.py

Requiere HF_TOKEN en el .env.

Qué deberías observar:
  1. describe_provider() te dice, en una línea, qué modelo y qué track están activos —
     sin que este script sepa nada de Hugging Face ni de URLs.
  2. El modelo responde a una pregunta real de tu industria.
  3. Ningún archivo de este curso escribe `ChatOpenAI(...)` directamente: todo pasa por
     `comun/provider.py` (decisión D13). Búscalo en este archivo: no está.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.settings import COURSE_TRACK  # noqa: E402

QUESTION_BY_TRACK = {
    "telecomunicaciones": "¿Qué debo hacer si mi línea se queda sin señal en pleno centro de Lima?",
    "banca": "¿Qué debo hacer si veo un cargo en mi cuenta que no reconozco?",
    "retail": "¿Qué hago si mi pedido llegó incompleto?",
    "seguros": "¿Qué debo hacer inmediatamente después de un choque leve?",
}


def main() -> None:
    print("=" * 72)
    print("  DEMO 1 · Primer llamado")
    print("=" * 72)

    print(f"\n  {describe_provider()}\n")

    question = QUESTION_BY_TRACK.get(
        COURSE_TRACK, "¿Qué es un agente de IA, explicado a un ingeniero de software?"
    )
    print(f"  Pregunta ({COURSE_TRACK}): {question}\n")

    model = get_chat_model()
    try:
        answer = model.invoke(question)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al llamar al modelo: {type(e).__name__}: {e}")
        print("     Revisa HF_TOKEN en tu .env y que tenga permiso de inferencia.")
        return

    print(f"  Respuesta:\n\n  {answer.content}\n")

    print("-" * 72)
    print("""
  Fíjate en que:
    · Este script no importa `langchain_openai` ni sabe la URL del proveedor.
    · Si cambiaras AI_PROVIDER a "foundry" en tu .env, este mismo código seguiría
      funcionando sin tocar una línea (eso es lo que hace posible el bonus del módulo 4).
    · La respuesta suena convincente, pero el modelo NO consultó ningún sistema real
      todavía: no tiene tools. Vuelve a leer la sección 2 del README de esta sesión.
""")


if __name__ == "__main__":
    main()
