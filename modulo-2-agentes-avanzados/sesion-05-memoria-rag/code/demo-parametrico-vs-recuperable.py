"""LA DEMO CLAVE · Conocimiento paramétrico vs recuperable — por qué el dato va al RAG.

Ejecutar desde la raíz del curso, DESPUÉS de 01_ingesta.py (usa la misma colección):
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/code/demo-parametrico-vs-recuperable.py

Requiere HF_TOKEN y Qdrant configurados. Dura 5 minutos en vivo. NO LA RECORTES: sostiene
la personalización con prompts y RAG del curso entero.

────────────────────────────── GUION PARA EL DOCENTE ──────────────────────────────

  1. Pregunta al modelo: "¿cuánto cuesta el plan Max 89?"
     → responde citando el tarifario (el precio ORIGINAL indexado).

  2. EDITA el documento en Qdrant: el precio del Max 89 sube (este script lo hace por ti,
     con edit_price_in_qdrant()).

  3. Pregunta LO MISMO otra vez.
     → responde con el precio NUEVO, citando el MISMO documento fuente.

  4. La pregunta al aula, en voz alta, antes de seguir:
     "¿Qué habría hecho falta para lograr este mismo cambio si el precio hubiera estado
     memorizado en los pesos del modelo, en vez de en un documento?"
     (Respuesta que se busca: reentrenar o afinar el modelo — horas o días, y una tarea
     de ingeniería de ML completa, para cambiar UN precio.)

  Este es el argumento completo de por qué el conocimiento que cambia con frecuencia
  (tarifas, coberturas, políticas) vive en el RAG, y el prompt/modelo solo aportan el
  tono y el comportamiento.
─────────────────────────────────────────────────────────────────────────────────────
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.documents import Document  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"
COLLECTION_NAME = f"kb-{TRACK}-demo"
QUESTION = "¿Cuánto cuesta el plan Max 89 al mes?"

# Un documento de una sola línea, autocontenido a propósito, para que la demo sea legible
# en pantalla y el cambio de precio sea inequívoco (no depende del tarifario completo).
# Qdrant exige que el id de un punto sea un entero o un UUID: se deriva uno fijo a partir
# de un nombre legible, para poder REEMPLAZAR (upsert) siempre el mismo punto.
DEMO_DOC_ID = str(uuid.uuid5(uuid.NAMESPACE_DNS, "demo-plan-max-89"))
ORIGINAL_PRICE_TEXT = "El plan Max 89 de AndesMóvil cuesta S/ 89.00 al mes, con 40 GB incluidos."
UPDATED_PRICE_TEXT = "El plan Max 89 de AndesMóvil cuesta S/ 99.00 al mes, con 40 GB incluidos."


def ask(store, model, question: str) -> str:
    results = store.similarity_search(question, k=1)
    context = "\n".join(f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results)
    prompt = (
        f"{get_system_prompt(TRACK)}\n\nCONTEXTO RECUPERADO:\n{context}\n\n"
        f"Responde SOLO con el contexto de arriba, citando la fuente.\nPregunta: {question}"
    )
    return model.invoke(prompt).content


def seed_demo_document(store, text: str) -> None:
    """Indexa (o reemplaza) el documento de la demo con un id fijo, para poder editarlo."""
    store.add_documents(
        [Document(page_content=text, metadata={"source": "demo-en-vivo"})],
        ids=[DEMO_DOC_ID],
    )


def main() -> None:
    print("=" * 72)
    print("  LA DEMO CLAVE · Paramétrico vs recuperable")
    print(f"  {describe_provider()}")
    print("=" * 72)

    try:
        store = get_vector_store(COLLECTION_NAME)
        model = get_chat_model()
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al preparar el stack: {type(e).__name__}: {e}")
        return

    print(f"\n  Paso 1 — Indexando el precio ORIGINAL: \"{ORIGINAL_PRICE_TEXT}\"")
    seed_demo_document(store, ORIGINAL_PRICE_TEXT)

    print(f"\n  Paso 2 — Pregunta: {QUESTION}")
    print(f"  Respuesta: {ask(store, model, QUESTION)}")

    input("\n  >>> Presiona ENTER para EDITAR el documento en Qdrant (subir el precio)...")

    print(f"\n  Paso 3 — Reemplazando el mismo documento con el precio NUEVO: "
          f"\"{UPDATED_PRICE_TEXT}\"")
    seed_demo_document(store, UPDATED_PRICE_TEXT)

    print(f"\n  Paso 4 — La MISMA pregunta otra vez: {QUESTION}")
    print(f"  Respuesta: {ask(store, model, QUESTION)}")

    print("""

  ─────────────────────────────────────────────────────────────────────────
  PREGUNTA AL AULA:

    ¿Qué habría hecho falta para lograr este mismo cambio de precio si
    hubiera estado memorizado en los PESOS del modelo, en vez de en un
    documento de Qdrant?

    (La respuesta que se busca: reentrenar o afinar el modelo — un proceso
    de horas o días — para cambiar UN precio. Aquí bastó con editar texto.)
  ─────────────────────────────────────────────────────────────────────────

  Esto es la personalización con prompts y RAG hecha física: el conocimiento
  que cambia va al RAG; el modelo y el prompt solo aportan tono y comportamiento.
""")


if __name__ == "__main__":
    main()
