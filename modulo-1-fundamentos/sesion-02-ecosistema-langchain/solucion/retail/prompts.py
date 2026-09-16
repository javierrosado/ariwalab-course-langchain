"""L2 · Retail — MercaSur · prompts.py (checkpoint de referencia)

Plantilla Rol + Contexto + Tarea + Formato, más 2 ejemplos few-shot (regla A5) que
cubren la confusión más común del track: SEGUIMIENTO_PEDIDO vs DEVOLUCION.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schemas import Intencion  # noqa: E402

ROL = "Eres el clasificador de intención de MercaSur, retail peruano con tienda online."

CONTEXTO = (
    "Las categorías posibles son: SEGUIMIENTO_PEDIDO, CONSULTA_PRODUCTO, CONSULTA_STOCK, "
    "DEVOLUCION, OTRO. DEVOLUCION es solo cuando el producto YA llegó y algo salió mal; si el "
    "pedido sigue en camino, es SEGUIMIENTO_PEDIDO aunque el cliente esté molesto."
)

FORMATO = "Devuelve un objeto Intencion con categoria, urgencia y entidades (si las hay)."

EJEMPLOS_FEW_SHOT: list[tuple[str, Intencion]] = [
    (
        "Mi pedido dice entregado pero no lo he recibido",
        Intencion(categoria="SEGUIMIENTO_PEDIDO", urgencia="ALTA", entidades=None),
    ),
    (
        "Compré esto y vino fallado, quiero cambiarlo",
        Intencion(categoria="DEVOLUCION", urgencia="MEDIA", entidades=None),
    ),
]


def construir_prompt(consulta: str) -> str:
    """Arma el prompt Rol + Contexto + Tarea + Formato para una consulta concreta."""
    tarea = f'Clasifica esta consulta de un cliente: "{consulta}"'
    return "\n\n".join([ROL, CONTEXTO, tarea, FORMATO])
