"""L2 · Banca — Banco Inti · clasificar.py (checkpoint de referencia)

Clasifica una consulta usando extraer() de comun/structured.py. PROHIBIDO usar
with_structured_output() directo aquí.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from comun.structured import ResultadoEstructurado, extraer, extraer_con_detalle  # noqa: E402

from prompts import EJEMPLOS_FEW_SHOT, construir_prompt  # noqa: E402
from schemas import Intencion  # noqa: E402


def clasificar(modelo, consulta: str) -> Intencion:
    """Clasifica una consulta de cliente en un objeto Intencion, con few-shot y validación."""
    prompt = construir_prompt(consulta)
    return extraer(modelo, Intencion, prompt, reintentos=1, ejemplos=EJEMPLOS_FEW_SHOT)


def clasificar_con_detalle(modelo, consulta: str) -> ResultadoEstructurado:
    """Igual que clasificar(), pero conserva cuántos intentos hicieron falta."""
    prompt = construir_prompt(consulta)
    return extraer_con_detalle(modelo, Intencion, prompt, reintentos=1, ejemplos=EJEMPLOS_FEW_SHOT)


if __name__ == "__main__":
    from comun.provider import describe_provider, get_chat_model

    print(f"{describe_provider()}\n")
    modelo = get_chat_model()
    for consulta in [
        "¿Cuánto tengo en mi cuenta 00112233445566?",
        "Este cargo de MOV-2026-0042 no lo hice yo",
        "¿Cuál es la comisión por mantenimiento de cuenta?",
    ]:
        intencion = clasificar(modelo, consulta)
        print(f"  \"{consulta}\"\n  → {intencion}\n")
