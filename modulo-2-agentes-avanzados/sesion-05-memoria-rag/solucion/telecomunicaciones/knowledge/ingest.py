"""L5 · Telecomunicaciones — AndesMóvil · knowledge/ingest.py (checkpoint de referencia)

Carga los 3 .md del track, los trocea y los indexa en Qdrant Cloud.

Ejecutar desde la raíz del curso (una sola vez por corpus: correrlo dos veces duplica
los puntos en la colección):
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/solucion/telecomunicaciones/knowledge/ingest.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from langchain_core.documents import Document  # noqa: E402
from langchain_text_splitters import RecursiveCharacterTextSplitter  # noqa: E402

from comun import datos  # noqa: E402
from comun import settings as cfg  # noqa: E402
from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"
CHUNK_SIZE, CHUNK_OVERLAP = 400, 60  # tarifario: entradas cortas, tabulares, autocontenidas


def load_track_documents(track: str) -> list[Document]:
    documents = []
    for path in datos.documentos_rag(track):
        text = path.read_text(encoding="utf-8")
        documents.append(Document(page_content=text, metadata={"source": path.name, "track": track}))
    return documents


def ingest(collection_name: str | None = None) -> int:
    documents = load_track_documents(TRACK)
    if not documents:
        raise FileNotFoundError(f"No hay documentos .md para el track '{TRACK}'")
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(documents)
    store = get_vector_store(collection_name)
    store.add_documents(chunks)
    return len(chunks)


def main() -> int:
    print(f"Ingesta del track '{TRACK}' → colección '{cfg.QDRANT_COLLECTION}'")
    try:
        n = ingest()
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {type(e).__name__}: {e}")
        print("Revisa QDRANT_URL, QDRANT_API_KEY y HF_TOKEN en tu .env, o usa la colección "
              "de respaldo (kb-telecomunicaciones-respaldo) mientras lo resuelves.")
        return 2
    print(f"Listo: {n} chunks indexados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
