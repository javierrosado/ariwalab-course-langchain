"""Demo 3 · RAG tradicional: buscar siempre y pegar el contexto.

Ejecutar desde la raíz del curso, DESPUÉS de 01_ingesta.py:
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/code/03_rag_tradicional.py

Requiere HF_TOKEN y Qdrant configurados.

Qué deberías observar: incluso "hola, buenos días" dispara una búsqueda en Qdrant. Eso
es exactamente lo que distingue a este patrón del RAG agéntico de la demo 4: aquí no hay
decisión, siempre se busca.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"
COLLECTION_NAME = f"kb-{TRACK}-demo"

QUESTIONS = [
    "¿Cuánto cuesta el plan Max 89 al mes?",
    "Hola, buenos días",  # aquí NO hace falta buscar, pero el patrón tradicional busca igual
]


def answer_traditional(store, model, question: str) -> str:
    results = store.similarity_search(question, k=2)
    context = "\n\n".join(f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results)
    prompt = (
        f"{get_system_prompt(TRACK)}\n\n"
        f"CONTEXTO RECUPERADO:\n{context}\n\n"
        f"Responde la pregunta del cliente usando SOLO el contexto de arriba, citando la fuente.\n"
        f"Pregunta: {question}"
    )
    return model.invoke(prompt).content


def main() -> None:
    print("=" * 72)
    print(f"  DEMO 3 · RAG tradicional ({TRACK})")
    print(f"  {describe_provider()}")
    print("=" * 72)

    try:
        store = get_vector_store(COLLECTION_NAME)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al conectar con Qdrant: {type(e).__name__}: {e}")
        return
    model = get_chat_model()

    for question in QUESTIONS:
        print(f"\n  Pregunta: {question}")
        print("  (buscando en Qdrant... siempre, sin decidir)")
        try:
            answer = answer_traditional(store, model, question)
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error: {type(e).__name__}: {e}")
            return
        print(f"  Respuesta: {answer}")

    print("""

  Nota el costo del segundo caso: "hola, buenos días" no necesitaba ningún dato del
  tarifario, y aun así se gastó una búsqueda en Qdrant y tokens de contexto en la
  llamada al modelo. Ese es el precio del RAG tradicional: control total, pero sin
  criterio. Compáralo con la demo 4.
""")


if __name__ == "__main__":
    main()
