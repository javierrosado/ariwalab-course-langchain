"""L10 · Seguros — Andina Seguros · evals/evaluadores.py (checkpoint de referencia)

Reexporta los 3 evaluators determinísticos de `comun/evaluadores.py` — no se
reescriben desde cero. Mismo patrón que
`observability.py` en la S9: un archivo por track que expone lo compartido, para
que `agent.py` y los scripts de evaluación de este track no importen `comun/`
directamente.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))

from comun.evaluadores import (  # noqa: E402,F401
    evaluar_caso,
    evaluar_exactitud,
    evaluar_groundedness,
    evaluar_tool,
    resumen,
)
