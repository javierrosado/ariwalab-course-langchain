"""Demo 1 · Ingesta: de 3 archivos .md a una colección consultable en Qdrant Cloud.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/code/01_ingesta.py

Requiere HF_TOKEN (embeddings) y QDRANT_URL/QDRANT_API_KEY en el .env.

Qué deberías observar:
  1. Los 3 .md del track se parten en chunks — el número de chunks NO es el número de
     archivos: un documento largo produce muchos chunks pequeños.
  2. Cada chunk queda indexado con su `source` en el payload — eso es lo que permite citar.
  3. La colección es idempotente de crear (ensure_collection no falla si ya existe), pero
     NO de indexar: correr esta demo dos veces duplica los puntos. En tu laboratorio,
     indexa una sola vez por corpus.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.documents import Document  # noqa: E402
from langchain_text_splitters import RecursiveCharacterTextSplitter  # noqa: E402

from comun import datos  # noqa: E402
from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"
CHUNK_SIZE, CHUNK_OVERLAP = 400, 60  # ver README.md sección 3 — fijado por track
COLLECTION_NAME = f"kb-{TRACK}-demo"  # colección aparte para no pisar la del laboratorio


def load_documents(track: str) -> list[Document]:
    documents = []
    for path in datos.documentos_rag(track):
        text = path.read_text(encoding="utf-8")
        documents.append(Document(page_content=text, metadata={"source": path.name, "track": track}))
    return documents


def main() -> None:
    print("=" * 72)
    print(f"  DEMO 1 · Ingesta ({TRACK})")
    print("=" * 72)

    documents = load_documents(TRACK)
    print(f"\n  Documentos cargados: {[d.metadata['source'] for d in documents]}")

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(documents)
    print(f"  chunk_size={CHUNK_SIZE} · chunk_overlap={CHUNK_OVERLAP} → {len(chunks)} chunks")

    por_fuente: dict[str, int] = {}
    for c in chunks:
        por_fuente[c.metadata["source"]] = por_fuente.get(c.metadata["source"], 0) + 1
    for fuente, n in por_fuente.items():
        print(f"    · {fuente}: {n} chunks")

    print(f"\n  Indexando en la colección '{COLLECTION_NAME}'...")
    try:
        store = get_vector_store(COLLECTION_NAME)
        store.add_documents(chunks)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al indexar: {type(e).__name__}: {e}")
        print("  Revisa QDRANT_URL, QDRANT_API_KEY y HF_TOKEN en tu .env.")
        return

    print(f"  Listo: {len(chunks)} chunks indexados en '{COLLECTION_NAME}'.")
    print("""
  Fíjate en que el número de chunks es mayor al número de documentos: eso es esperable.
  Corre la demo 2 (02_similitud.py) para ver esta misma colección respondiendo preguntas
  sin compartir palabras con el texto original.
""")


if __name__ == "__main__":
    main()
