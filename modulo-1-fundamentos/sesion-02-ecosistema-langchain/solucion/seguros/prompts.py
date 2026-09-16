"""L2 · Seguros — Andina Seguros · prompts.py (checkpoint de referencia)

Plantilla Rol + Contexto + Tarea + Formato, más 2 ejemplos few-shot (regla A5) que
cubren la confusión más común del track: COTIZACION vs CONSULTA_POLIZA.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schemas import Intencion  # noqa: E402

ROL = "Eres el clasificador de intención de Andina Seguros, aseguradora peruana de SOAT."

CONTEXTO = (
    "Las categorías posibles son: CONSULTA_POLIZA, COTIZACION, ESTADO_SINIESTRO, "
    "REPORTE_SINIESTRO, OTRO. COTIZACION es sobre un SOAT nuevo o su renovación (un precio "
    "futuro); CONSULTA_POLIZA es sobre el estado de un SOAT YA contratado."
)

FORMATO = "Devuelve un objeto Intencion con categoria, urgencia y entidades (si las hay)."

EJEMPLOS_FEW_SHOT: list[tuple[str, Intencion]] = [
    (
        "Mi SOAT venció, ¿cuánto pagaría por renovarlo?",
        Intencion(categoria="COTIZACION", urgencia="BAJA", entidades=None),
    ),
    (
        "Antes de reportar el choque quiero confirmar que mi póliza está vigente",
        Intencion(categoria="CONSULTA_POLIZA", urgencia="MEDIA", entidades=None),
    ),
]


def construir_prompt(consulta: str) -> str:
    """Arma el prompt Rol + Contexto + Tarea + Formato para una consulta concreta."""
    tarea = f'Clasifica esta consulta de un cliente: "{consulta}"'
    return "\n\n".join([ROL, CONTEXTO, tarea, FORMATO])
