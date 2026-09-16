"""Demo 2 · Tipos de mensaje: el mismo `human`, con y sin `system`.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-01-fundamentos-agentes/code/02_tipos_de_mensaje.py

Requiere HF_TOKEN en el .env.

Qué deberías observar:
  1. `HumanMessage` es lo que escribe el usuario; `SystemMessage` es la instrucción que
     tú, el desarrollador, le das al modelo ANTES de la conversación.
  2. La misma pregunta, con distinto `system`, cambia de tono y de límites sin que la
     pregunta del cliente haya cambiado ni una palabra.
  3. Sin `system`, el modelo responde con su comportamiento por defecto: genérico,
     sin el vocabulario ni los límites de tu industria.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.messages import HumanMessage, SystemMessage  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.settings import COURSE_TRACK  # noqa: E402

CUSTOMER_QUESTION = "Llevo dos días esperando una respuesta. Esto es pésimo, ¿me van a ayudar o no?"


def ask(model, messages: list) -> str:
    return (model.invoke(messages).content or "").strip()


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · Tipos de mensaje: system, human, ai")
    print(f"  {describe_provider()}")
    print("=" * 72)

    print(f"\n  Mensaje del cliente (HumanMessage):\n  \"{CUSTOMER_QUESTION}\"\n")

    model = get_chat_model()

    # ── Sin system: comportamiento genérico del modelo ──────────────────────
    print("-" * 72)
    print("  SIN system prompt")
    print("-" * 72)
    try:
        without_system = ask(model, [HumanMessage(content=CUSTOMER_QUESTION)])
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al llamar al modelo: {type(e).__name__}: {e}")
        print("     Revisa HF_TOKEN en tu .env y que tenga permiso de inferencia.")
        return
    print(f"\n  {without_system}\n")

    # ── Con system: personalización de la industria del track activo ───────
    print("-" * 72)
    print(f"  CON system prompt de la industria ({COURSE_TRACK})")
    print("-" * 72)
    industry_prompt = get_system_prompt(COURSE_TRACK)
    with_system = ask(
        model,
        [
            SystemMessage(content=industry_prompt),
            HumanMessage(content=CUSTOMER_QUESTION),
        ],
    )
    print(f"\n  {with_system}\n")

    print("=" * 72)
    print("""
  Qué deberías notar

    · La pregunta del cliente (HumanMessage) fue idéntica en los dos casos.
    · El `system` no le agregó información nueva al modelo: le dio un ROL, un
      vocabulario y unos límites. Compara el tono de las dos respuestas.
    · Un `AIMessage` (la respuesta del modelo) también se puede reenviar como parte
      del historial en la siguiente llamada — así es como funciona la "memoria" de
      un agente (lo vas a construir de verdad en la Sesión 5).
    · El `system` que acabas de usar es el mismo que usará tu agente desde el
      Laboratorio 1: `comun/prompts_industria.get_system_prompt()`.
""")


if __name__ == "__main__":
    main()
