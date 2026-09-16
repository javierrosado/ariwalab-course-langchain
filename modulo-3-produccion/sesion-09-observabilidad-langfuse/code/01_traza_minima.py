"""Demo 1 · El callback puesto y una traza apareciendo en el dashboard en vivo.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-09-observabilidad-langfuse/code/01_traza_minima.py

Requiere HF_TOKEN y las credenciales de Langfuse en el .env (LANGFUSE_PUBLIC_KEY,
LANGFUSE_SECRET_KEY). Después de correr esto, abre tu proyecto en
https://cloud.langfuse.com y busca el trace más reciente — es la primera vez en el
curso que "ver que funcionó" significa abrir un dashboard, no leer la consola.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comun.observability import get_langfuse_handler  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402


def main() -> None:
    print("=" * 72)
    print("  DEMO 1 · una traza mínima en Langfuse")
    print(f"  {describe_provider()}")
    print("=" * 72)

    handler = get_langfuse_handler()
    model = get_chat_model()

    pregunta = "En una frase, ¿qué es un agente de IA?"
    print(f"\n  Pregunta: {pregunta}")

    respuesta = model.invoke(
        [("human", pregunta)],
        config={"callbacks": [handler], "run_name": "demo-01-traza-minima"},
    )
    print(f"  Respuesta: {respuesta.content}")

    print("""
  Abre https://cloud.langfuse.com, entra a tu proyecto y busca el trace
  "demo-01-traza-minima". Deberías ver UN solo span: la llamada al modelo. La
  demo 2 añade tool + retriever para que la jerarquía se parezca a un agente real.
""")


if __name__ == "__main__":
    main()
