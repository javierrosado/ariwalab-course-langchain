"""L2 · Seguros — Andina Seguros · schemas.py (checkpoint de referencia)

El esquema `Intencion`, alineado 1:1 con las 4 tools núcleo del L4.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class CategoriaIntencion(str, Enum):
    CONSULTA_POLIZA = "CONSULTA_POLIZA"        # → get_policy_by_plate (L4)
    COTIZACION = "COTIZACION"                  # → quote_soat (L4)
    ESTADO_SINIESTRO = "ESTADO_SINIESTRO"      # → get_claim_status (L4)
    REPORTE_SINIESTRO = "REPORTE_SINIESTRO"    # → open_claim (L4)
    OTRO = "OTRO"                              # → ninguna tool: va a RAG en la S5


class Urgencia(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class Intencion(BaseModel):
    """Clasificación estructurada de una consulta de un cliente de Andina Seguros."""

    categoria: CategoriaIntencion = Field(
        description=(
            "CONSULTA_POLIZA si pregunta si SU SOAT está vigente o hasta cuándo. "
            "COTIZACION si pregunta cuánto costaría un SOAT nuevo o una renovación. "
            "ESTADO_SINIESTRO si pregunta en qué va un expediente YA reportado. "
            "REPORTE_SINIESTRO si está comunicando un accidente que AÚN no ha reportado. "
            "OTRO si pregunta por coberturas, exclusiones o el condicionado en general (no "
            "sobre su propio caso), o es un saludo sin consulta concreta."
        )
    )
    urgencia: Urgencia = Field(
        description="Nivel de urgencia percibido. ALTA si menciona lesionados o un accidente reciente."
    )
    entidades: str | None = Field(
        default=None,
        description=(
            "El identificador mencionado por el cliente: placa del vehículo o código de "
            "expediente de siniestro. None si no mencionó ninguno."
        ),
    )
