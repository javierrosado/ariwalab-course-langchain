"""L9 · Telecomunicaciones — AndesMóvil · observability.py (checkpoint de referencia)

Wrapper de una línea sobre comun.observability, para que agent.py no importe comun/
directamente (mismo patrón que ya usa con guardrails.py y domain_tools.py). El
enmascarador de PII (DNI, tarjeta, teléfono) ya queda enganchado al configurar el
cliente de Langfuse en comun.observability — no se repite aquí.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from comun.observability import get_callbacks  # noqa: E402,F401
