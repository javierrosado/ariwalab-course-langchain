"""Simulación de fallos: la parte más didáctica del simulador.

La Sesión 3 del curso exige que el alumno documente TRES escenarios:
éxito, dato inexistente y **API caída**. Sin una forma de provocar el tercero,
ese requisito se cumple de mentira.

Este módulo permite pedir un fallo a voluntad con el parámetro `_fallo`:

    GET /telco/clientes/987654321?_fallo=timeout
    GET /banca/cuentas/191-1234567-0-12?_fallo=error500
    GET /retail/pedidos/MS-2026-00001?_fallo=lento

Lo importante no es el fallo en sí, sino que el alumno descubra que una tool
debe capturar el error y devolver un TEXTO que el agente pueda leer y usar para
replantear su plan. Una excepción sin capturar rompe el bucle ReAct; un mensaje
como "el servicio no responde, intenta más tarde" no lo rompe.
"""

from __future__ import annotations

import asyncio
import random

from fastapi import HTTPException

FALLOS_DISPONIBLES = {
    "timeout": "El servicio tarda 30 segundos y el cliente debe cortar por timeout",
    "error500": "El servicio devuelve 500 Internal Server Error",
    "error503": "El servicio devuelve 503 Service Unavailable",
    "lento": "El servicio responde correctamente pero tarda 5 segundos",
    "vacio": "El servicio responde 200 con un cuerpo vacío",
    "malformado": "El servicio responde 200 con un JSON que no cumple el contrato",
}

# Probabilidad de fallo espontáneo, para que el alumno no asuma que la red es
# perfecta. Se controla con la variable de entorno CHAOS_RATE (0.0 a 1.0).
import os  # noqa: E402

CHAOS_RATE = float(os.getenv("CHAOS_RATE", "0.0"))


async def aplicar(fallo: str | None) -> dict | None:
    """Aplica el fallo pedido. Devuelve un cuerpo alternativo o None para seguir normal."""
    if not fallo and CHAOS_RATE > 0 and random.random() < CHAOS_RATE:
        fallo = random.choice(["error503", "lento"])

    if not fallo:
        return None

    fallo = fallo.strip().lower()

    if fallo == "timeout":
        await asyncio.sleep(30)
        return None
    if fallo == "lento":
        await asyncio.sleep(5)
        return None
    if fallo == "error500":
        raise HTTPException(status_code=500, detail="Internal Server Error (simulado)")
    if fallo == "error503":
        raise HTTPException(
            status_code=503,
            detail="Service Unavailable (simulado). Reintenta en unos segundos.",
        )
    if fallo == "vacio":
        return {}
    if fallo == "malformado":
        return {"resultado": "ok", "datos": "esto no es el contrato esperado"}

    raise HTTPException(
        status_code=400,
        detail=f"Fallo desconocido: '{fallo}'. Disponibles: {', '.join(FALLOS_DISPONIBLES)}",
    )
