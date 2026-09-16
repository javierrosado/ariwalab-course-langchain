"""L5 · memory.py (checkpoint de referencia) — estado conversacional por thread_id.

El modelo es stateless: "recordar" es tu código reenviando el historial relevante en
cada llamada. Aquí, en memoria del proceso — alcanza para el curso. En producción
(Sesión 8) este estado viviría en una base de datos o en un checkpointer persistente,
para sobrevivir a un reinicio del servidor.
"""

from __future__ import annotations

_HISTORIES: dict[str, list] = {}


def get_history(thread_id: str) -> list:
    """Devuelve (y crea si no existe) el historial de mensajes de una conversación."""
    return _HISTORIES.setdefault(thread_id, [])


def append_message(thread_id: str, message) -> None:
    """Agrega un mensaje (HumanMessage, AIMessage o ToolMessage) al historial del thread."""
    get_history(thread_id).append(message)


def reset(thread_id: str) -> None:
    """Borra el historial de una conversación — útil para pruebas y para 'nueva conversación'."""
    _HISTORIES.pop(thread_id, None)
