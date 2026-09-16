"""L5 · Telecomunicaciones — AndesMóvil · agent.py v3 (checkpoint de referencia)

Las 4 tools del L4 + el retriever del L5 (RAG agéntico) + memoria por thread_id.
Mismo bucle manual con tope de iteraciones de las sesiones anteriores.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/solucion/telecomunicaciones/agent.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
# Reutiliza las tools del L4 (con la confirmación ya incorporada) en vez de duplicarlas.
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-04-tools-multiples"
                       / "solucion" / "telecomunicaciones"))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

import memory  # noqa: E402
from domain_tools import TOOLS_NUCLEO  # noqa: E402  (del L4)
from knowledge.retriever import retrieve_knowledge_base  # noqa: E402  (del L5)

MAX_ITERATIONS = 4
TRACK = "telecomunicaciones"

ALL_TOOLS = TOOLS_NUCLEO + [retrieve_knowledge_base]
_tools_by_name = {t.name: t for t in ALL_TOOLS}
_model = None


def get_model():
    global _model
    if _model is None:
        _model = get_chat_model().bind_tools(ALL_TOOLS)
    return _model


def responder(mensaje: str, thread_id: str = "default") -> str:
    """Responde dentro de la conversación identificada por thread_id, con memoria."""
    history = memory.get_history(thread_id)
    if not history:
        history.append(SystemMessage(content=get_system_prompt(TRACK)))
    human = HumanMessage(content=mensaje)
    history.append(human)

    model = get_model()
    for _ in range(MAX_ITERATIONS):
        ai_message: AIMessage = model.invoke(history)
        history.append(ai_message)
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
            history.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return ("No pude resolver tu consulta en el número de pasos permitido. "
            "Te derivo con un asesor humano.")


if __name__ == "__main__":
    print("=" * 72)
    print(f"  Agente v3 (con RAG y memoria) · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)

    thread = "demo-conversacion-1"
    for pregunta in [
        "¿Cuánto cuesta el plan Max 89 al mes?",       # va al RAG
        "¿Y cuántos gigas incluye?",                    # depende de la memoria del turno anterior
        "Ahora sí, mi línea es 987654321, ¿qué plan tengo?",  # va a una tool
    ]:
        print(f"\n  Tú: {pregunta}")
        print(f"  Agente: {responder(pregunta, thread_id=thread)}")
