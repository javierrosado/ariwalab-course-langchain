"""L2 · Banca — Banco Inti · prompts.py (checkpoint de referencia)

Plantilla Rol + Contexto + Tarea + Formato, más 2 ejemplos few-shot (regla A5) que
cubren la confusión más común del track: CONSULTA_MOVIMIENTOS vs SOSPECHA_FRAUDE.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schemas import Intencion  # noqa: E402

ROL = "Eres el clasificador de intención de Banco Inti, banco personal peruano."

CONTEXTO = (
    "Las categorías posibles son: CONSULTA_SALDO, CONSULTA_MOVIMIENTOS, CONSULTA_TARJETA, "
    "SOSPECHA_FRAUDE, OTRO. SOSPECHA_FRAUDE es específicamente cuando el cliente dice que un "
    "movimiento no lo hizo él o que algo le parece irregular, no una consulta neutra."
)

FORMATO = "Devuelve un objeto Intencion con categoria, urgencia y entidades (si las hay)."

EJEMPLOS_FEW_SHOT: list[tuple[str, Intencion]] = [
    (
        "Veo un cargo que no reconozco, ¿me listan lo del último mes?",
        Intencion(categoria="CONSULTA_MOVIMIENTOS", urgencia="MEDIA", entidades=None),
    ),
    (
        "Este movimiento no lo hice yo, ¿qué tan riesgoso lo consideran?",
        Intencion(categoria="SOSPECHA_FRAUDE", urgencia="ALTA", entidades=None),
    ),
]


def construir_prompt(consulta: str) -> str:
    """Arma el prompt Rol + Contexto + Tarea + Formato para una consulta concreta."""
    tarea = f'Clasifica esta consulta de un cliente: "{consulta}"'
    return "\n\n".join([ROL, CONTEXTO, tarea, FORMATO])
