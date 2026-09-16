"""L5 · Seguros — Andina Seguros · knowledge/retriever.py (checkpoint de referencia)

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
    """Busca en la base de conocimiento de Andina Seguros: condicionado general del
    SOAT, tabla de coberturas y topes en UIT, exclusiones y procedimiento de siniestro.

    Úsala ante cualquier pregunta sobre qué cubre el SOAT, hasta qué monto, qué está
    excluido, o cuáles son los pasos generales para reportar un siniestro.
    NO la uses para la vigencia de UNA póliza, cotizar, el estado de UN expediente
    concreto o abrir un siniestro (usa get_policy_by_plate, quote_soat, get_claim_status
    u open_claim). Toda cifra de cobertura debe salir de aquí, nunca de memoria.
    """
    results = _get_store().similarity_search(query, k=3)
    if not results:
        return "No se encontró información relevante en la base de conocimiento."
    return "\n\n".join(
        f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results
    )
