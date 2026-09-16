"""L4 · Seguros — Andina Seguros · agent.py (checkpoint de referencia)

Ensambla las 4 tools de domain_tools.py con el modelo, en un bucle manual
Thought → Action → Observation con tope de iteraciones (regla A4).

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-04-tools-multiples/solucion/seguros/agent.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

from domain_tools import TOOLS_NUCLEO  # noqa: E402

MAX_ITERATIONS = 4
TRACK = "seguros"

_tools_by_name = {t.name: t for t in TOOLS_NUCLEO}
_model = None


def get_model():
    global _model
    if _model is None:
        _model = get_chat_model().bind_tools(TOOLS_NUCLEO)
    return _model


def responder(mensaje: str) -> str:
    """Contrato usado por docente/matriz_seleccion.py y docente/verificar_guardrails.py:
    recibe un mensaje y devuelve la respuesta del agente, en una conversación nueva.
    """
    messages = [SystemMessage(content=get_system_prompt(TRACK)), HumanMessage(content=mensaje)]
    model = get_model()
    for _ in range(MAX_ITERATIONS):
        ai_message: AIMessage = model.invoke(messages)
        messages.append(ai_message)
        if not ai_message.tool_calls:
            return ai_message.content
        for call in ai_message.tool_calls:
            tool = _tools_by_name.get(call["name"])
            if tool is None:
                result = f"Error: tool '{call['name']}' no existe en este catálogo."
            else:
                try:
                    result = tool.invoke(call["args"])
                except Exception as e:  # noqa: BLE001
                    result = f"Error al ejecutar {call['name']}: {type(e).__name__}: {e}"
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return ("No pude resolver tu consulta en el número de pasos permitido. "
            "Te derivo con un asesor humano.")


if __name__ == "__main__":
    print("=" * 72)
    print(f"  Agente · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)
    for pregunta in [
        "¿Mi SOAT está vigente? La placa es ABC-123",
        "Acabo de chocar en Ate, placa ABC-123, sin heridos",
    ]:
        print(f"\n  Tú: {pregunta}")
        print(f"  Agente: {responder(pregunta)}")
