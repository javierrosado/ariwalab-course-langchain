"""L2 · Telecomunicaciones — AndesMóvil · prompts.py (checkpoint de referencia)

Plantilla Rol + Contexto + Tarea + Formato, más 2 ejemplos few-shot (regla A5) que
cubren la confusión más común del track: AVERIA vs RECLAMO.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schemas import Intencion  # noqa: E402

ROL = "Eres el clasificador de intención de AndesMóvil, operador de telefonía móvil en Perú."

CONTEXTO = (
    "Las categorías posibles son: CONSULTA_PLAN, CONSULTA_CONSUMO, AVERIA, RECLAMO, OTRO. "
    "AVERIA es cuando el cliente reporta que algo no funciona técnicamente. RECLAMO es cuando "
    "pide explícitamente que se registre una queja formal, no solo que se resuelva su problema."
)

FORMATO = "Devuelve un objeto Intencion con categoria, urgencia y entidades (si las hay)."

# Pares (consulta, Intencion esperada) — pasan al modelo como ejemplos few-shot.
# Elegidos por medición, no a priori (ver README.md, sección 3): estos dos son los que
# de verdad movían la aguja al correr medir_clasificador.py contra el modelo real.
EJEMPLOS_FEW_SHOT: list[tuple[str, Intencion]] = [
    (
        "Se me cae la llamada todo el tiempo, ya es insoportable",
        Intencion(categoria="AVERIA", urgencia="ALTA", entidades=None),
    ),
    (
        # La confusión que más costaba: preguntar el PRECIO de un plan (OTRO, va a RAG en
        # la S5) se confundía con preguntar por EL PROPIO plan (CONSULTA_PLAN).
        "¿Cuánto cuesta el plan Max 89 al mes?",
        Intencion(categoria="OTRO", urgencia="BAJA", entidades=None),
    ),
]


def construir_prompt(consulta: str) -> str:
    """Arma el prompt Rol + Contexto + Tarea + Formato para una consulta concreta."""
    tarea = f'Clasifica esta consulta de un cliente: "{consulta}"'
    return "\n\n".join([ROL, CONTEXTO, tarea, FORMATO])
