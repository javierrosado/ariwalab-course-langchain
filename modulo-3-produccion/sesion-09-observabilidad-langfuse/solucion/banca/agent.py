"""L9 · Banca — Banco Inti · agent.py v5 (checkpoint de referencia)

Idéntico al v4 del L6 (tools + retriever + memoria + guardrails), con UNA diferencia:
cada `model.invoke()` y `tool.invoke()` del bucle recibe
`config={"callbacks": get_callbacks()}`. Es la única línea que cambia por invocación —
la lógica del agente no se toca, tal como enseña el bloque 5 del `README.md` de la S9
("instrumentar sin tocar la lógica").

Contrato para docente/verificar_guardrails.py y app/api.py (sin cambios):
    responder(mensaje: str, thread_id: str | None = None) -> str
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-04-tools-multiples"
                       / "solucion" / "banca"))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-05-memoria-rag"
                       / "solucion" / "banca"))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-06-automatizacion-guardrails"
                       / "solucion" / "banca"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

import guardrails  # noqa: E402  (del L6)
import memory  # noqa: E402  (del L5)
from domain_tools import TOOLS_NUCLEO  # noqa: E402  (del L4)
from knowledge.retriever import retrieve_knowledge_base  # noqa: E402  (del L5)
from observability import get_callbacks  # noqa: E402  (de esta sesión)

MAX_ITERATIONS = 4
TRACK = "banca"

ALL_TOOLS = TOOLS_NUCLEO + [retrieve_knowledge_base]
_tools_by_name = {t.name: t for t in ALL_TOOLS}
_model = None


def get_model():
    global _model
    if _model is None:
        _model = get_chat_model().bind_tools(ALL_TOOLS)
    return _model


def _run_conversation(mensaje: str, thread_id: str) -> str:
    history = memory.get_history(thread_id)
    if not history:
        history.append(SystemMessage(content=get_system_prompt(TRACK)))
    history.append(HumanMessage(content=mensaje))

    config = {"callbacks": get_callbacks(), "run_name": f"agente-{TRACK}"}
    model = get_model()
    for _ in range(MAX_ITERATIONS):
        ai_message: AIMessage = model.invoke(history, config=config)
        history.append(ai_message)
        if not ai_message.tool_calls:
            return ai_message.content
        for call in ai_message.tool_calls:
            allowed, reason = guardrails.check_action(call["name"], call["args"])
            if not allowed:
                result = f"Acción no permitida: {reason}"
            else:
                tool = _tools_by_name.get(call["name"])
                if tool is None:
                    result = f"Error: tool '{call['name']}' no existe en este catálogo."
                else:
                    try:
                        result = tool.invoke(call["args"], config=config)
                    except Exception as e:  # noqa: BLE001
                        result = f"Error al ejecutar {call['name']}: {type(e).__name__}: {e}"
            history.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return "No pude resolver tu consulta en el número de pasos permitido. Te derivo con un asesor humano."


def responder(mensaje: str, thread_id: str | None = None) -> str:
    """Punto de entrada — mismo contrato del L6, ahora con trazas en Langfuse."""
    conversation_id = thread_id or f"aislado-{uuid.uuid4()}"

    safe, blocked_response = guardrails.check_input(mensaje)
    if not safe:
        return blocked_response

    raw_response = _run_conversation(mensaje, conversation_id)
    safe_response = guardrails.check_output(raw_response)

    if guardrails.needs_escalation(mensaje):
        safe_response += "\n\n[Este caso se deriva también a un asesor humano.]"

    return safe_response


if __name__ == "__main__":
    print("=" * 72)
    print(f"  Agente v5 (instrumentado con Langfuse) · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)

    for pregunta in [
        "¿Cuánto cobra el banco por mantenimiento de cuenta de ahorros?",
        "¿Cuál es el saldo de la cuenta 191-9450993-0-54?",
    ]:
        print(f"\n  Tú: {pregunta}")
        print(f"  Agente: {responder(pregunta)}")
