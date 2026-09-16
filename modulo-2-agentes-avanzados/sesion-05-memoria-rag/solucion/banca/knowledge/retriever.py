"""L5 · Banca — Banco Inti · knowledge/retriever.py (checkpoint de referencia)

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
    """Busca en la base de conocimiento de Banco Inti: tarifario de comisiones, política
    de fraude y condiciones del contrato de tarjeta.

    Úsala cuando el cliente pregunte cuánto cobra el banco por un servicio, qué hace el
    banco ante una alerta de fraude en general, o las condiciones de su tarjeta (pago
    mínimo, fecha de facturación, comisión por consumo internacional).
    NO la uses para el saldo, movimientos, datos de SU tarjeta o el score de riesgo de
    UN movimiento concreto (usa get_account_balance, list_transactions, get_card_info
    o score_transaction_risk).
    """
    results = _get_store().similarity_search(query, k=3)
    if not results:
        return "No se encontró información relevante en la base de conocimiento."
    return "\n\n".join(
        f"[Fuente: {d.metadata.get('source')}]\n{d.page_content}" for d in results
    )
