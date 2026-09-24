"""Base vectorial del curso — Qdrant Cloud, backend único.

No hay fallback local a propósito: el curso es 100 % SaaS. Si el cluster de
Qdrant no responde, el laboratorio debe fallar de forma ruidosa, no degradarse
en silencio a una base en memoria que oculte el problema.
"""

from __future__ import annotations

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore

from . import settings as cfg
from .provider import get_embeddings

# Dimensión de intfloat/multilingual-e5-large.
# Si cambias HF_EMBEDDING_MODEL, ajusta este valor o usa probe_embedding_dim().
DEFAULT_VECTOR_SIZE = 1024


def get_client() -> QdrantClient:
    """Cliente de Qdrant Cloud."""
    return QdrantClient(
        url=cfg.require("QDRANT_URL", cfg.QDRANT_URL),
        api_key=cfg.require("QDRANT_API_KEY", cfg.QDRANT_API_KEY),
    )


def probe_embedding_dim() -> int:
    """Consulta al modelo cuántas dimensiones devuelve. Evita hardcodear mal."""
    return len(get_embeddings().embed_query("dimensión de prueba"))


def ensure_collection(
    collection_name: str | None = None,
    vector_size: int | None = None,
) -> str:
    """Crea la colección si no existe. Idempotente: se puede llamar en cada lab."""
    name = collection_name or cfg.QDRANT_COLLECTION
    client = get_client()

    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(
                size=vector_size or DEFAULT_VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )
    return name


def get_vector_store(collection_name: str | None = None) -> QdrantVectorStore:
    """Vector store listo para indexar y recuperar."""
    name = ensure_collection(collection_name)
    return QdrantVectorStore(
        client=get_client(),
        collection_name=name,
        embedding=get_embeddings(),
    )
