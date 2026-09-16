"""Trazabilidad con Langfuse Cloud (sesiones 9 y 10).

Se instrumenta por callback: el agente no sabe que está siendo observado.
Esa es justamente la lección de la sesión 9 — la observabilidad es una
preocupación transversal, no una responsabilidad del código de negocio.
"""

from __future__ import annotations

import os

from . import settings as cfg


def _export_env() -> None:
    """Langfuse lee estas variables del entorno del proceso."""
    os.environ["LANGFUSE_PUBLIC_KEY"] = cfg.LANGFUSE_PUBLIC_KEY
    os.environ["LANGFUSE_SECRET_KEY"] = cfg.LANGFUSE_SECRET_KEY
    os.environ["LANGFUSE_HOST"] = cfg.LANGFUSE_HOST


def get_langfuse_handler(**kwargs):
    """Devuelve el CallbackHandler de Langfuse.

    Compatible con langfuse v3 (langfuse.langchain) y v2 (langfuse.callback).
    """
    cfg.require("LANGFUSE_PUBLIC_KEY", cfg.LANGFUSE_PUBLIC_KEY)
    cfg.require("LANGFUSE_SECRET_KEY", cfg.LANGFUSE_SECRET_KEY)
    _export_env()

    try:  # langfuse >= 3
        from langfuse.langchain import CallbackHandler
    except ImportError:  # langfuse 2.x
        from langfuse.callback import CallbackHandler

    return CallbackHandler(**kwargs)


def get_callbacks(enabled: bool = True) -> list:
    """Lista de callbacks para pasar a invoke(config={"callbacks": ...}).

    Devuelve [] si Langfuse no está configurado, para que los laboratorios
    de las sesiones 1 a 8 corran sin necesitar cuenta de Langfuse.
    """
    if not enabled or not (cfg.LANGFUSE_PUBLIC_KEY and cfg.LANGFUSE_SECRET_KEY):
        return []
    return [get_langfuse_handler()]
