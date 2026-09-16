"""L5 · Retail — MercaSur · knowledge/retriever.py (checkpoint de referencia)

El retriever expuesto como tool — RAG agéntico. Regla A2: cuándo usarla y cuándo NO.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from langchain_core.tools import tool  # noqa: E402

from comun.vectorstore import get_vector_store  # noqa: E402

_store = None


def _get_store():
    global _store
    if _store is None:
        _store = get_vector_store()
    return _store


@tool
def retrieve_knowledge_base(query: str) -> str:
    """Busca en la base de conocimiento de MercaSur: política de cambios y devoluciones,
    términos de garantía y preguntas frecuentes de despacho.

    Úsala cuando el cliente pregunte por la política general de devoluciones, cuánto
    tiempo de garantía tiene una categoría de producto, o las condiciones de despacho
    (costo, plazo, envío gratuito).
    NO la uses para el estado de UN pedido, la ficha de UN producto, el stock de UN SKU,
    o para iniciar o consultar una devolución concreta (usa track_order,
    get_product_details, check_stock_by_store o start_return_request).
    """
    results = _get_store().similarity_search(query, k=3)
    if not results:
        return "No se encontró información relevante en la base de conocimiento."
    return "\n\n".join(
        f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results
    )
