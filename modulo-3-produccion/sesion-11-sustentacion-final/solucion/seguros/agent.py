"""L11 · Seguros — Andina Seguros · agent.py v6 (checkpoint de referencia)

Idéntico al v5 del L9 (tools + retriever + memoria + guardrails + trazas), con UNA
función nueva: `responder_streaming()`, que consume `app/api.py`'s `/chat/stream`.

Nota de honestidad sobre el streaming. El guardrail de salida (`check_output`) solo
puede evaluar el texto COMPLETO de la respuesta, y debe correr ANTES de que cualquier
fragmento llegue al cliente: si se transmitiera token a token en vivo desde el modelo,
un guardrail que detecta el problema al final ya habría dejado escapar el contenido
dañino de todas formas (el cliente ya lo habría visto). Por eso `responder_streaming`
resuelve el bucle completo SIN transmitir nada (reutiliza `_run_conversation`, igual
que `responder`), valida con `guardrails.check_output()`, y solo entonces transmite el
resultado ya seguro, palabra por palabra — el cliente experimenta el mismo streaming
por Server-Sent Events, con la garantía de seguridad del L6 intacta. Es la razón por la
que un guardrail de salida por texto completo y un streaming de tokens en vivo del
modelo no son compatibles sin cambios de diseño más profundos: aquí se prioriza el
guardrail, tal como pide la sesión 6.

Contrato para docente/verificar_guardrails.py y app/api.py (sin cambios en responder):
    responder(mensaje: str, thread_id: str | None = None) -> str
    responder_streaming(mensaje: str, thread_id: str | None = None) -> Iterator[str]
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-04-tools-multiples"
                       / "solucion" / "seguros"))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-05-memoria-rag"
                       / "solucion" / "seguros"))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-06-automatizacion-guardrails"
                       / "solucion" / "seguros"))
sys.path.insert(0, str(ROOT / "modulo-3-produccion" / "sesion-09-observabilidad-langfuse"
                       / "solucion" / "seguros"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

import guardrails  # noqa: E402  (del L6)
import memory  # noqa: E402  (del L5)
from domain_tools import TOOLS_NUCLEO  # noqa: E402  (del L4)
from knowledge.retriever import retrieve_knowledge_base  # noqa: E402  (del L5)
from observability import get_callbacks  # noqa: E402  (de la S9)

MAX_ITERATIONS = 4
TRACK = "seguros"

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
    """Punto de entrada sin streaming — mismo contrato desde el L6."""
    conversation_id = thread_id or f"aislado-{uuid.uuid4()}"

    safe, blocked_response = guardrails.check_input(mensaje)
    if not safe:
        return blocked_response

    raw_response = _run_conversation(mensaje, conversation_id)
    safe_response = guardrails.check_output(raw_response)

    if guardrails.needs_escalation(mensaje):
        safe_response += "\n\n[Este caso se deriva también a un asesor humano.]"

    return safe_response


def responder_streaming(mensaje: str, thread_id: str | None = None):
    """Punto de entrada con streaming — ver la nota de honestidad al inicio del archivo:
    resuelve todo el bucle primero, valida con los guardrails, y SOLO ENTONCES
    transmite el resultado ya seguro, palabra por palabra.
    """
    conversation_id = thread_id or f"aislado-{uuid.uuid4()}"

    safe, blocked_response = guardrails.check_input(mensaje)
    if not safe:
        yield blocked_response
        return

    raw_response = _run_conversation(mensaje, conversation_id)
    safe_response = guardrails.check_output(raw_response)

    for palabra in safe_response.split(" "):
        yield palabra + " "

    if guardrails.needs_escalation(mensaje):
        yield "\n\n[Este caso se deriva también a un asesor humano.]"


if __name__ == "__main__":
    print("=" * 72)
    print(f"  Agente v6 (con streaming) · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)

    pregunta = "¿Cuál es el estado del expediente VEX-958?"
    print(f"\n  Tú: {pregunta}")
    print("  Agente (streaming): ", end="", flush=True)
    for fragmento in responder_streaming(pregunta):
        print(fragmento, end="", flush=True)
    print()
