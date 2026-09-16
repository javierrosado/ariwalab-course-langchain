"""Demo 3 · Un solo modelo, cuatro industrias — D21 en vivo.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-01-fundamentos-agentes/code/03_un_modelo_cuatro_industrias.py

Requiere HF_TOKEN en el .env.

Sustituye a la demo `03_model_comparison.py` del repo de Microsoft, que compara MODELOS
distintos. Con la decisión D28 este curso usa un solo modelo para las 4 industrias, así
que esa comparación perdería sentido aquí. En su lugar, esta demo compara PROMPTS de
industria — que es la decisión que sí gobierna este curso (D21, camino A: sin fine-tuning).

Qué deberías observar:
  1. La misma pregunta, el mismo modelo (`Qwen/Qwen3-32B`), cuatro respuestas distintas.
  2. Cada respuesta usa el vocabulario, el tono y los límites de su industria.
  3. Nada de esto vino de reentrenar el modelo: vino de `comun/prompts_industria.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.messages import HumanMessage, SystemMessage  # noqa: E402

from comun.prompts_industria import PROMPTS, get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

SHARED_QUESTION = "Necesito ayuda pero no sé bien a quién más recurrir. ¿Qué me recomiendas hacer?"

LABEL_BY_TRACK = {
    "telecomunicaciones": "AndesMóvil (telco)",
    "banca": "Banco Inti (banca)",
    "retail": "MercaSur (retail)",
    "seguros": "Andina Seguros (seguros)",
}


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · Un modelo, cuatro industrias")
    print(f"  {describe_provider()}")
    print("=" * 72)
    print(f'\n  Pregunta compartida (idéntica en los 4 casos):\n  "{SHARED_QUESTION}"\n')

    model = get_chat_model()

    for track in PROMPTS:  # mismo orden que comun/prompts_industria.PROMPTS
        label = LABEL_BY_TRACK[track]
        print("-" * 72)
        print(f"  {label}")
        print("-" * 72)

        system_prompt = get_system_prompt(track)
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=SHARED_QUESTION),
        ]
        try:
            answer = (model.invoke(messages).content or "").strip()
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error al llamar al modelo: {type(e).__name__}: {e}")
            print("     Revisa HF_TOKEN en tu .env y que tenga permiso de inferencia.")
            return

        print(f"\n  {answer}\n")

    print("=" * 72)
    print("""
  Qué significa esto para el curso

    · Un solo modelo verificado (D28) en vez de cuatro modelos por afinar.
    · Cambiar el tono de un agente es editar texto en prompts_industria.py, no
      reentrenar nada (decisión D26: 5 bloques por industria — identidad, jerga,
      estilo, recuperación obligatoria y límites).
    · Esto es exactamente lo que vas a usar en tu laboratorio de hoy: tu
      `primer_contacto.py` importa `get_system_prompt()` con TU track, no los cuatro.
    · Nota: ninguna de estas cuatro respuestas citó una fuente real todavía —eso
      llega recién en la Sesión 5 con RAG. Hoy el modelo sigue "sonando" a su
      industria, pero sin haber consultado ningún dato real.
""")


if __name__ == "__main__":
    main()
