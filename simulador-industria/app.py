"""Simulador de industria — aplicación principal.

Un solo servicio que simula cuatro empresas peruanas ficticias y expone el mismo
dominio por tres superficies distintas:

    REST  ──►  /telco  /banca  /retail  /seguros
    SQL   ──►  SQLite interno (los alumnos lo consultan a través de la API)
    MCP   ──►  /mcp  (HTTP) y mcp_server.py (stdio)

Ejecutar en local:
    uvicorn app:app --reload --port 8000

Documentación interactiva:
    http://localhost:8000/docs
"""

from __future__ import annotations

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

import chaos
import db
from routers import ROUTERS

VERSION = "1.0.0"


@asynccontextmanager
async def ciclo_de_vida(app: FastAPI):
    resumen = db.inicializar()
    total = sum(resumen.values())
    print(f"[simulador] Base construida: {len(resumen)} tablas, {total} filas")
    yield
    print("[simulador] Apagando")


app = FastAPI(
    title="Simulador de Industria · Curso IA Agent Building",
    description=(
        "Simula cuatro empresas peruanas ficticias contra las cuales corren los "
        "laboratorios del curso: **AndesMóvil** (telecomunicaciones), **Banco Inti** "
        "(banca), **MercaSur** (retail) y **Andina Seguros** (seguros).\n\n"
        "Todas las rutas exigen la cabecera `X-API-Key` con la clave de tu equipo.\n\n"
        "Para practicar el manejo de errores, cualquier ruta acepta el parámetro "
        "`_fallo` con uno de estos valores: `timeout`, `error500`, `error503`, "
        "`lento`, `vacio`, `malformado`."
    ),
    version=VERSION,
    lifespan=ciclo_de_vida,
)

for router in ROUTERS:
    app.include_router(router)


@app.get("/", tags=["meta"])
async def raiz():
    """Información del simulador y cómo empezar a usarlo."""
    return {
        "servicio": "Simulador de Industria · Curso IA Agent Building",
        "version": VERSION,
        "industrias": {
            "telco": "AndesMóvil · atención al cliente móvil postpago",
            "banca": "Banco Inti · banca personal y detección de fraude",
            "retail": "MercaSur · post-venta de e-commerce",
            "seguros": "Andina Seguros · SOAT y siniestros vehiculares",
        },
        "superficies": {
            "rest": "/telco, /banca, /retail, /seguros",
            "mcp_http": "/mcp",
            "mcp_stdio": "python mcp_server.py",
            "documentacion": "/docs",
        },
        "autenticacion": "Cabecera X-API-Key con la clave de tu equipo",
        "simulacion_de_fallos": list(chaos.FALLOS_DISPONIBLES),
        "aviso": "Todos los datos son sintéticos y todas las empresas son ficticias.",
    }


@app.get("/health", tags=["meta"])
async def health():
    """Comprobación de vida. No requiere API key."""
    try:
        n = db.uno("SELECT COUNT(*) AS n FROM telco_clientes")
        return {"estado": "ok", "version": VERSION, "clientes_telco": n["n"] if n else 0}
    except Exception as e:  # noqa: BLE001
        return JSONResponse(status_code=503, content={"estado": "degradado", "detalle": str(e)})


@app.get("/fallos", tags=["meta"])
async def fallos_disponibles():
    """Catálogo de fallos que se pueden provocar con el parámetro `_fallo`.

    Existe para que el alumno pueda documentar el escenario "API caída" que exige
    la Sesión 3, en vez de simularlo de mentira.
    """
    return {
        "uso": "Agrega ?_fallo=<nombre> a cualquier ruta",
        "ejemplo": "/telco/clientes/987654321?_fallo=error503",
        "fallos": chaos.FALLOS_DISPONIBLES,
        "chaos_rate": chaos.CHAOS_RATE,
        "nota": (
            "Una tool bien escrita captura el error y devuelve un TEXTO que el agente "
            "pueda leer. Una excepción sin capturar rompe el bucle ReAct."
        ),
    }


# ── MCP por HTTP ───────────────────────────────────────────────────────────
# Se monta solo si la librería está disponible, para que el simulador arranque
# igual en entornos donde no se instaló el SDK de MCP.
if os.getenv("HABILITAR_MCP_HTTP", "1") == "1":
    try:
        from mcp_server import mcp as servidor_mcp

        app.mount("/mcp", servidor_mcp.streamable_http_app())
        print("[simulador] MCP por HTTP montado en /mcp")
    except Exception as e:  # noqa: BLE001
        print(f"[simulador] MCP por HTTP no disponible: {type(e).__name__}: {e}")
