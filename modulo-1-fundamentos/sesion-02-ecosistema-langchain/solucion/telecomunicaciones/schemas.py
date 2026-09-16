"""L2 · Telecomunicaciones — AndesMóvil · schemas.py (checkpoint de referencia)

El esquema `Intencion`: lo que el modelo debe producir a partir de una consulta libre
del cliente. La categoría está alineada 1:1 con las 4 tools núcleo del L4 — no es
casualidad, es la decisión de diseño de la Sesión 2: la categoría que clasificas hoy
es la tool que tu agente deberá elegir en el L4.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class CategoriaIntencion(str, Enum):
    CONSULTA_PLAN = "CONSULTA_PLAN"          # → get_customer_plan (L4)
    CONSULTA_CONSUMO = "CONSULTA_CONSUMO"    # → get_data_usage (L4)
    AVERIA = "AVERIA"                        # → run_line_diagnostics (L4)
    RECLAMO = "RECLAMO"                      # → create_complaint_ticket (L4)
    OTRO = "OTRO"                            # → ninguna tool: va a RAG en la S5


class Urgencia(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class Intencion(BaseModel):
    """Clasificación estructurada de una consulta de un cliente de AndesMóvil."""

    categoria: CategoriaIntencion = Field(
        description=(
            "CONSULTA_PLAN SOLO si pregunta por SU PROPIO plan ya contratado (cuál tiene, "
            "desde cuándo, si está activo) usando posesivos como 'mi plan'. "
            "CONSULTA_CONSUMO si pregunta por gigas, minutos o SMS consumidos. "
            "AVERIA si reporta una falla técnica (sin señal, se corta, lento). "
            "RECLAMO si pide explícitamente registrar una queja formal. "
            "OTRO si pregunta por el PRECIO o las condiciones de CUALQUIER plan del catálogo "
            "general (no el propio), tarifas, políticas o portabilidad en general, o si es un "
            "saludo sin consulta concreta. NO uses CONSULTA_PLAN para preguntas de precio: "
            "'¿cuánto cuesta el plan X?' es OTRO, no CONSULTA_PLAN."
        )
    )
    urgencia: Urgencia = Field(description="Nivel de urgencia percibido en el tono del cliente.")
    entidades: str | None = Field(
        default=None,
        description=(
            "El identificador que el cliente haya mencionado, por ejemplo el número de línea "
            "de 9 dígitos. None si no mencionó ninguno."
        ),
    )
