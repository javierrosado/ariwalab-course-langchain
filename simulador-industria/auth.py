"""Autenticación por API key y aislamiento por equipo.

Cada equipo del curso recibe una API key. La key identifica al equipo, y el
equipo determina qué escrituras ve: las suyas y las de la semilla, nunca las de
otro equipo.

Esto no es solo higiene del simulador: es el mecanismo por el que el alumno
aprende, en la Sesión 3, que una API real exige credenciales y que un 401 no se
arregla reintentando.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from fastapi import Header, HTTPException

RUTA_EQUIPOS = Path(os.getenv("EQUIPOS_FILE", Path(__file__).parent / "equipos.json"))


def _cargar_equipos() -> dict[str, str]:
    """Devuelve {api_key: nombre_equipo}."""
    if RUTA_EQUIPOS.exists():
        return json.loads(RUTA_EQUIPOS.read_text(encoding="utf-8"))
    # Fallback para desarrollo local sin archivo de equipos
    return {"demo-key-0000": "demo"}


EQUIPOS = _cargar_equipos()


async def equipo_actual(x_api_key: str | None = Header(default=None)) -> str:
    """Dependencia de FastAPI: valida la API key y devuelve el nombre del equipo.

    El alumno debe enviar la cabecera `X-API-Key` en cada petición. Si falta o es
    inválida, recibe un 401 — que es exactamente el error que debe aprender a
    manejar dentro de una tool, devolviendo un mensaje legible al agente en vez
    de dejar que la excepción rompa el bucle ReAct.
    """
    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="Falta la cabecera X-API-Key. Cada equipo tiene su propia clave.",
        )
    equipo = EQUIPOS.get(x_api_key)
    if not equipo:
        raise HTTPException(
            status_code=401,
            detail="API key inválida. Verifica SIM_API_KEY en tu archivo .env.",
        )
    return equipo
