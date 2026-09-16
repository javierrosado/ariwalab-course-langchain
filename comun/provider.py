"""Capa de proveedor de modelos — el corazón arquitectónico del curso.

Ningún laboratorio instancia un modelo directamente: todos piden get_chat_model().
Por eso, en el bonus de Foundry basta con cambiar AI_PROVIDER en el .env y el
código del agente (agent.py, tools/, guardrails.py, schemas.py) no se toca.

Ambos proveedores se consumen por la API compatible con OpenAI:
  - Hugging Face: router de Inference Providers (https://router.huggingface.co/v1)
  - Foundry:      endpoint /openai/v1 del proyecto
Esto no es casualidad: es lo que permite que el mismo objeto ChatOpenAI sirva
para los dos y que el tool calling se comporte igual.
"""

from __future__ import annotations

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from . import settings as cfg


def resolve_chat_model_id() -> str:
    """Resuelve qué modelo usar.

    Las cuatro industrias comparten el MISMO modelo (decisión D21, camino A): lo que
    las diferencia es el system prompt y la colección de Qdrant, no los pesos.

    `TRACK_MODELS` queda como punto de extensión por si en una edición futura se
    afina un modelo por industria; hoy está vacío y no se usa.
    """
    if cfg.AI_PROVIDER == "foundry":
        return cfg.AI_MODEL
    return cfg.TRACK_MODELS.get(cfg.COURSE_TRACK) or cfg.HF_CHAT_MODEL


def get_chat_model(temperature: float = 0.0, **kwargs) -> ChatOpenAI:
    """Devuelve el modelo de chat del proveedor activo.

    Args:
        temperature: 0.0 para tareas deterministas (tools, clasificación),
            valores altos solo para redacción libre.
    """
    if cfg.AI_PROVIDER == "huggingface":
        # Qwen3 alterna modo "thinking" y "non-thinking". Para agentes se fija
        # non-thinking de forma explícita: no se deja al default del proveedor.
        extra = {"chat_template_kwargs": {"enable_thinking": cfg.HF_ENABLE_THINKING}}
        return ChatOpenAI(
            model=resolve_chat_model_id(),
            base_url=cfg.HF_BASE_URL,
            api_key=cfg.require("HF_TOKEN", cfg.HF_TOKEN),
            temperature=temperature,
            model_kwargs={"extra_body": extra},
            **kwargs,
        )

    if cfg.AI_PROVIDER == "foundry":
        return ChatOpenAI(
            model=cfg.AI_MODEL,
            base_url=cfg.require("AI_ENDPOINT", cfg.AI_ENDPOINT),
            api_key=cfg.require("AI_API_KEY", cfg.AI_API_KEY),
            temperature=temperature,
            **kwargs,
        )

    raise ValueError(
        f"AI_PROVIDER='{cfg.AI_PROVIDER}' no es válido. "
        f"Usa uno de: {cfg.VALID_PROVIDERS}"
    )


def get_embeddings():
    """Devuelve el modelo de embeddings del proveedor activo.

    En Hugging Face se usa HuggingFaceEndpointEmbeddings porque el router
    compatible con OpenAI no expone de forma uniforme feature-extraction.
    """
    if cfg.AI_PROVIDER == "huggingface":
        from langchain_huggingface import HuggingFaceEndpointEmbeddings

        return HuggingFaceEndpointEmbeddings(
            model=cfg.HF_EMBEDDING_MODEL,
            huggingfacehub_api_token=cfg.require("HF_TOKEN", cfg.HF_TOKEN),
        )

    if cfg.AI_PROVIDER == "foundry":
        return OpenAIEmbeddings(
            model=cfg.AI_EMBEDDING_MODEL,
            base_url=cfg.require("AI_ENDPOINT", cfg.AI_ENDPOINT),
            api_key=cfg.require("AI_API_KEY", cfg.AI_API_KEY),
        )

    raise ValueError(f"AI_PROVIDER='{cfg.AI_PROVIDER}' no es válido.")


def describe_provider() -> str:
    """Una línea legible para imprimir al inicio de cada laboratorio."""
    if cfg.AI_PROVIDER == "huggingface":
        return (
            f"Hugging Face · track={cfg.COURSE_TRACK} · "
            f"{resolve_chat_model_id()} · {cfg.HF_BASE_URL}"
        )
    return f"Microsoft Foundry · {cfg.AI_MODEL} · {cfg.AI_ENDPOINT}"
