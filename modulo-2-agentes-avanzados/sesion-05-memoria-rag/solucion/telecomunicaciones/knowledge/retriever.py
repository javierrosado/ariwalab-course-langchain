"""L5 · Telecomunicaciones — AndesMóvil · knowledge/retriever.py (checkpoint de referencia)

El retriever expuesto como tool — RAG agéntico: el agente decide cuándo llamarla.
Regla A2: la docstring dice cuándo usarla y cuándo NO.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from langchain_core.tools import tool  # noqa: E402

from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"

_store = None


def _get_store():
    global _store
    if _store is None:
        _store = get_vector_store()
    return _store


@tool
def retrieve_knowledge_base(query: str) -> str:
    """Busca en la base de conocimiento de AndesMóvil: tarifario de planes, condiciones
    de portabilidad y reglamento de reclamos.

    Úsala cuando el cliente pregunte por precios de planes, condiciones o plazos de
    portabilidad, o el procedimiento general para presentar un reclamo.
    NO la uses para el plan, consumo o diagnóstico de UNA línea concreta (usa
    get_customer_plan, get_data_usage o run_line_diagnostics), ni para registrar un
    reclamo nuevo (usa create_complaint_ticket).
    """
    results = _get_store().similarity_search(query, k=3)
    if not results:
        return "No se encontró información relevante en la base de conocimiento."
    return "\n\n".join(
        f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results
    )
