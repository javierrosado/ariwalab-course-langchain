"""Demo 4 · RAG agéntico: el retriever como tool — el agente decide si buscar.

Ejecutar desde la raíz del curso, DESPUÉS de 01_ingesta.py:
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/code/04_rag_agentico.py

Requiere HF_TOKEN y Qdrant configurados.

Qué deberías observar: la misma pregunta de saludo de la demo 3 NO dispara ninguna
búsqueda aquí — el agente decide que no la necesita. La de tarifas sí, y la respuesta
debe citar la fuente (columna `source` del payload).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402
from langchain_core.tools import tool  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"
COLLECTION_NAME = f"kb-{TRACK}-demo"
MAX_ITERATIONS = 4

QUESTIONS = [
    "¿Cuánto cuesta el plan Max 89 al mes?",
    "Hola, buenos días",  # aquí SÍ debería abstenerse de buscar
]


def build_retriever_tool(store):
    @tool
    def retrieve_knowledge_base(query: str) -> str:
        """Busca en la base de conocimiento de AndesMóvil (tarifario, portabilidad, reclamos).

        Úsala cuando el cliente pregunte por tarifas, precios de planes, condiciones de
        portabilidad o el procedimiento de reclamos — cualquier dato que no devuelva
        ninguna de tus otras tools.
        NO la uses para saludos, agradecimientos, o preguntas ya resueltas por
        get_customer_plan, get_data_usage, run_line_diagnostics o create_complaint_ticket.
        """
        results = store.similarity_search(query, k=2)
        if not results:
            return "No se encontró información relevante en la base de conocimiento."
        return "\n\n".join(
            f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results
        )

    return retrieve_knowledge_base


def run_agent(model_with_tools, tools_by_name: dict, system_prompt: str, question: str):
    messages = [SystemMessage(content=system_prompt), HumanMessage(content=question)]
    searched = False
    for _ in range(MAX_ITERATIONS):
        ai_message: AIMessage = model_with_tools.invoke(messages)
        messages.append(ai_message)
        if not ai_message.tool_calls:
            return ai_message.content, searched
        for call in ai_message.tool_calls:
            searched = searched or call["name"] == "retrieve_knowledge_base"
            tool_fn = tools_by_name[call["name"]]
            result = tool_fn.invoke(call["args"])
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return "No se pudo resolver en el límite de iteraciones.", searched


def main() -> None:
    print("=" * 72)
    print(f"  DEMO 4 · RAG agéntico ({TRACK})")
    print(f"  {describe_provider()}")
    print("=" * 72)

    try:
        store = get_vector_store(COLLECTION_NAME)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al conectar con Qdrant: {type(e).__name__}: {e}")
        return

    retriever_tool = build_retriever_tool(store)
    tools_by_name = {retriever_tool.name: retriever_tool}
    model = get_chat_model().bind_tools([retriever_tool])
    system_prompt = get_system_prompt(TRACK)

    for question in QUESTIONS:
        print(f"\n  Pregunta: {question}")
        try:
            answer, searched = run_agent(model, tools_by_name, system_prompt, question)
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error: {type(e).__name__}: {e}")
            return
        print(f"  ¿Buscó en la base de conocimiento?: {'sí' if searched else 'no'}")
        print(f"  Respuesta: {answer}")

    print("""

  Compara con la demo 3: ahí "hola, buenos días" también disparaba una búsqueda. Aquí,
  si el agente decidió bien, no la disparó. Esa decisión es la ganancia del RAG agéntico
  — y también su riesgo: un agente puede decidir MAL y no buscar cuando debía. Por eso
  existe la salvaguarda A6 en el system prompt (README.md, sección 6).
""")


if __name__ == "__main__":
    main()
