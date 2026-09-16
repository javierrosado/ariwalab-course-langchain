"""L3 · Telecomunicaciones — AndesMóvil · agent.py v1 (checkpoint de referencia)

create_agent() con la única tool de hoy y el system prompt del track. Se vuelve
agent.py v3 en la Sesión 5 y v4 en la Sesión 6 — este es su primer capítulo.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/solucion/telecomunicaciones/agent.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from langchain.agents import create_agent  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

from external_api import get_customer_plan  # noqa: E402

TRACK = "telecomunicaciones"

_agente = None


def get_agente():
    global _agente
    if _agente is None:
        _agente = create_agent(get_chat_model(), [get_customer_plan],
                               system_prompt=get_system_prompt(TRACK))
    return _agente


def responder(mensaje: str) -> str:
    resultado = get_agente().invoke({"messages": [("human", mensaje)]})
    return resultado["messages"][-1].content


if __name__ == "__main__":
    print("=" * 72)
    print(f"  Agente v1 · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)
    for pregunta in [
        "¿Qué plan tengo? Mi línea es 987654321",
        "¿Qué plan tiene la línea 000000000?",
    ]:
        print(f"\n  Tú: {pregunta}")
        print(f"  Agente: {responder(pregunta)}")
