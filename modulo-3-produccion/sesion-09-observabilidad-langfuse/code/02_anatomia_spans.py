"""Demo 2 · Un run con tool + retriever, y los spans que produce.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-09-observabilidad-langfuse/code/02_anatomia_spans.py

Requiere HF_TOKEN, Qdrant y Langfuse en el .env. Usa el catálogo y el retriever de
telecomunicaciones (referencia del docente) para producir la MISMA jerarquía que
dibuja el bloque 2 del README: modelo → tool → modelo → retriever → modelo.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-04-tools-multiples"
                       / "solucion" / "telecomunicaciones"))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-05-memoria-rag"
                       / "solucion" / "telecomunicaciones"))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402

from comun.observability import get_langfuse_handler  # noqa: E402
from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from domain_tools import TOOLS_NUCLEO  # noqa: E402
from knowledge.retriever import retrieve_knowledge_base  # noqa: E402

TRACK = "telecomunicaciones"
ALL_TOOLS = TOOLS_NUCLEO + [retrieve_knowledge_base]
TOOLS_BY_NAME = {t.name: t for t in ALL_TOOLS}


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · anatomía de una traza de agente")
    print(f"  {describe_provider()}")
    print("=" * 72)

    handler = get_langfuse_handler()
    config = {"callbacks": [handler], "run_name": "demo-02-anatomia-spans"}
    model = get_chat_model().bind_tools(ALL_TOOLS)

    history = [
        SystemMessage(content=get_system_prompt(TRACK)),
        HumanMessage(content="¿Cuál es mi plan en la línea 988837195, y aparte, "
                              "cuánto cuesta portar mi número a otro operador?"),
    ]

    for paso in range(4):
        ai_message: AIMessage = model.invoke(history, config=config)
        history.append(ai_message)
        if not ai_message.tool_calls:
            print(f"\n  Respuesta final (paso {paso + 1}): {ai_message.content}")
            break
        for call in ai_message.tool_calls:
            print(f"  [span] tool {call['name']}({call['args']})")
            tool = TOOLS_BY_NAME.get(call["name"])
            resultado = tool.invoke(call["args"], config=config) if tool else "tool no encontrada"
            history.append(ToolMessage(content=str(resultado), tool_call_id=call["id"]))

    print("""
  Abre el trace "demo-02-anatomia-spans" en Langfuse. Deberías ver la jerarquía del
  bloque 2 del README: varias llamadas al modelo intercaladas con spans de tool y
  de retriever. Suma cuánto tiempo se llevó el modelo contra el resto — es la
  primera lectura que pide el bloque 2.
""")


if __name__ == "__main__":
    main()
