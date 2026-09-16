"""L2 · Banca — Banco Inti · schemas.py (checkpoint de referencia)

El esquema `Intencion`, alineado 1:1 con las 4 tools núcleo del L4.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class CategoriaIntencion(str, Enum):
    CONSULTA_SALDO = "CONSULTA_SALDO"                # → get_account_balance (L4)
    CONSULTA_MOVIMIENTOS = "CONSULTA_MOVIMIENTOS"    # → list_transactions (L4)
    CONSULTA_TARJETA = "CONSULTA_TARJETA"            # → get_card_info (L4)
    SOSPECHA_FRAUDE = "SOSPECHA_FRAUDE"              # → score_transaction_risk (L4)
    OTRO = "OTRO"                                     # → ninguna tool: va a RAG en la S5


class Urgencia(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class Intencion(BaseModel):
    """Clasificación estructurada de una consulta de un cliente de Banco Inti."""

    categoria: CategoriaIntencion = Field(
        description=(
            "CONSULTA_SALDO si pregunta cuánto tiene o si su cuenta está activa. "
            "CONSULTA_MOVIMIENTOS si pregunta por sus últimas operaciones o un cargo concreto. "
            "CONSULTA_TARJETA si pregunta por datos de SU tarjeta (línea, vencimiento). "
            "SOSPECHA_FRAUDE si dice que no reconoce un movimiento o sospecha de un cargo. "
            "OTRO si pregunta por comisiones, políticas generales o del banco en abstracto "
            "(no de su cuenta), o es un saludo sin consulta concreta."
        )
    )
    urgencia: Urgencia = Field(description="Nivel de urgencia percibido en el tono del cliente.")
    entidades: str | None = Field(
        default=None,
        description=(
            "El identificador mencionado por el cliente: número de cuenta o de movimiento. "
            "None si no mencionó ninguno."
        ),
    )
