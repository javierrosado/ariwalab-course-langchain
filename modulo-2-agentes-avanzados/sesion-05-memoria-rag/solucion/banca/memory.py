"""L5 · memory.py (checkpoint de referencia) — estado conversacional por thread_id.

El modelo es stateless: "recordar" es tu código reenviando el historial relevante en
cada llamada. Aquí, en memoria del proceso — alcanza para el curso.
"""

from __future__ import annotations

_HISTORIES: dict[str, list] = {}


def get_history(thread_id: str) -> list:
    """Devuelve (y crea si no existe) el historial de mensajes de una conversación."""
    return _HISTORIES.setdefault(thread_id, [])


def append_message(thread_id: str, message) -> None:
    """Agrega un mensaje al historial del thread."""
    get_history(thread_id).append(message)


def reset(thread_id: str) -> None:
    """Borra el historial de una conversación."""
    _HISTORIES.pop(thread_id, None)
