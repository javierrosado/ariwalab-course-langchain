"""Trazabilidad con Langfuse Cloud (sesiones 9 y 10).

Se instrumenta por callback: el agente no sabe que está siendo observado.
Esa es justamente la lección de la sesión 9 — la observabilidad es una
preocupación transversal, no una responsabilidad del código de negocio.
"""

from __future__ import annotations

import os
import re

from . import settings as cfg

# ─────────────────────── enmascarador de PII (sesión 9) ───────────────────────
# Los mismos patrones que ya usa guardrails.check_output() en el L6 (DNI de 8
# dígitos, tarjeta de 16), más teléfono. Se centralizan aquí porque este módulo
# es transversal a los 4 tracks y no puede depender de un guardrails.py que vive
# en solucion/<track>/. La regla de la S9: si el DNI no puede salir del agente
# hacia el cliente, tampoco puede salir hacia un SaaS de terceros.
_DNI = re.compile(r"\b\d{8}\b")
_TELEFONO = re.compile(r"\b9\d{8}\b")
_TARJETA = re.compile(r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b")

_client_configurado = False


def enmascarar_pii(valor):
    """Enmascara DNI, tarjeta y teléfono dentro de `valor`.

    Recorre dicts y listas recursivamente porque una traza de agente es texto
    anidado en mensajes, tool calls y resultados de tool — no una sola cadena.
    """
    if isinstance(valor, str):
        texto = _TARJETA.sub(lambda m: m.group(0)[:4] + " **** **** ****", valor)
        texto = _TELEFONO.sub(lambda m: m.group(0)[:2] + "*******", texto)
        texto = _DNI.sub(lambda m: m.group(0)[:2] + "******", texto)
        return texto
    if isinstance(valor, dict):
        return {k: enmascarar_pii(v) for k, v in valor.items()}
    if isinstance(valor, (list, tuple)):
        return [enmascarar_pii(v) for v in valor]
    return valor


def _mask_para_langfuse(*, data, **kwargs) -> object:
    """Firma exigida por `Langfuse(mask=...)`: recibe el dato bruto de cada
    span (`start_observation`, `update`, `set_trace_io`) y devuelve la versión
    que de verdad se envía a la nube. Se aplica ANTES del export, nunca después.
    """
    return enmascarar_pii(data)


def _export_env() -> None:
    """Langfuse lee estas variables del entorno del proceso."""
    os.environ["LANGFUSE_PUBLIC_KEY"] = cfg.LANGFUSE_PUBLIC_KEY
    os.environ["LANGFUSE_SECRET_KEY"] = cfg.LANGFUSE_SECRET_KEY
    os.environ["LANGFUSE_HOST"] = cfg.LANGFUSE_HOST


def _configurar_cliente_langfuse() -> None:
    """Inicializa el cliente Langfuse (singleton del SDK v3) con el enmascarador
    ya enganchado. Debe correr una sola vez, antes de crear cualquier
    CallbackHandler — el handler reutiliza este cliente vía `get_client()`.
    """
    global _client_configurado
    if _client_configurado:
        return
    from langfuse import Langfuse

    Langfuse(
        public_key=cfg.LANGFUSE_PUBLIC_KEY,
        secret_key=cfg.LANGFUSE_SECRET_KEY,
        host=cfg.LANGFUSE_HOST,
        mask=_mask_para_langfuse,
    )
    _client_configurado = True


def get_langfuse_handler(**kwargs):
    """Devuelve el CallbackHandler de Langfuse, con el enmascarador de PII
    enganchado (regla de la sesión 9: ninguna traza sale con PII en claro).

    Compatible con langfuse v3 (langfuse.langchain) y v2 (langfuse.callback) —
    en v2 no existe `mask`, así que el enmascarador no aplica y se documenta así.
    """
    cfg.require("LANGFUSE_PUBLIC_KEY", cfg.LANGFUSE_PUBLIC_KEY)
    cfg.require("LANGFUSE_SECRET_KEY", cfg.LANGFUSE_SECRET_KEY)
    _export_env()

    try:  # langfuse >= 3
        from langfuse.langchain import CallbackHandler
        _configurar_cliente_langfuse()
    except ImportError:  # langfuse 2.x — sin soporte de `mask`
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
