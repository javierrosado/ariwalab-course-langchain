"""L2 · Retail — MercaSur · schemas.py (checkpoint de referencia)

El esquema `Intencion`, alineado 1:1 con las 4 tools núcleo del L4.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class CategoriaIntencion(str, Enum):
    SEGUIMIENTO_PEDIDO = "SEGUIMIENTO_PEDIDO"    # → track_order (L4)
    CONSULTA_PRODUCTO = "CONSULTA_PRODUCTO"      # → get_product_details (L4)
    CONSULTA_STOCK = "CONSULTA_STOCK"            # → check_stock_by_store (L4)
    DEVOLUCION = "DEVOLUCION"                    # → start_return_request (L4)
    OTRO = "OTRO"                                # → ninguna tool: va a RAG en la S5


class Urgencia(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class Intencion(BaseModel):
    """Clasificación estructurada de una consulta de un cliente de MercaSur."""

    categoria: CategoriaIntencion = Field(
        description=(
            "SEGUIMIENTO_PEDIDO si pregunta dónde está o cuándo llega SU pedido ya hecho. "
            "CONSULTA_PRODUCTO si pregunta precio, características o garantía de un producto "
            "del catálogo (sin haberlo comprado todavía). "
            "CONSULTA_STOCK si pregunta si hay disponibilidad o en qué tienda recoger. "
            "DEVOLUCION si pide cambiar, devolver o reembolsar algo YA RECIBIDO. "
            "OTRO si pregunta por políticas generales de devolución, envíos o métodos de pago "
            "sin referirse a un pedido propio, o es un saludo sin consulta concreta."
        )
    )
    urgencia: Urgencia = Field(description="Nivel de urgencia percibido en el tono del cliente.")
    entidades: str | None = Field(
        default=None,
        description=(
            "El identificador mencionado por el cliente: número de pedido o SKU. "
            "None si no mencionó ninguno."
        ),
    )
