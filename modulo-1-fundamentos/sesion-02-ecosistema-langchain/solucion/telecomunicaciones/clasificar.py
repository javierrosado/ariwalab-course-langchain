"""L2 · Telecomunicaciones — AndesMóvil · clasificar.py (checkpoint de referencia)

Clasifica una consulta usando extraer() de comun/structured.py. PROHIBIDO usar
with_structured_output() directo aquí: es exactamente el camino que la demo 3 de
code/ mostró que falla en silencio.
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
    """Igual que clasificar(), pero conserva cuántos intentos hicieron falta.

    Lo usa medir_clasificador.py: el primer dato de fiabilidad que el curso mide con
    las manos, y que se retoma en la Sesión 10.
    """
    prompt = construir_prompt(consulta)
    return extraer_con_detalle(modelo, Intencion, prompt, reintentos=1, ejemplos=EJEMPLOS_FEW_SHOT)


if __name__ == "__main__":
    from comun.provider import describe_provider, get_chat_model

    print(f"{describe_provider()}\n")
    modelo = get_chat_model()
    for consulta in [
        "¿Cuántos gigas me quedan? Mi línea es 987654321",
        "No tengo señal desde ayer, línea 912345678",
        "¿Cuánto cuesta el plan Max 89?",
    ]:
        intencion = clasificar(modelo, consulta)
        print(f"  \"{consulta}\"\n  → {intencion}\n")
