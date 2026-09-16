"""Demo 1 · El agente detrás de `/chat` y `/health`, con uvicorn.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-08-despliegue-hf-spaces/code/01_api_local.py

Requiere HF_TOKEN en el .env (el agente de referencia hace llamadas reales al modelo).
No hace falta Docker ni una cuenta de HF Spaces: esto corre en tu máquina para que veas
la capa HTTP ANTES de empaquetarla — el mismo `app/api.py` que despliega el L8, corriendo
localmente con `uvicorn`, exactamente lo que la plataforma hace por dentro del contenedor.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-06-automatizacion-guardrails"
                       / "solucion" / "telecomunicaciones"))

import os  # noqa: E402

os.environ.setdefault("AGENT_API_KEY", "clave-de-demo-local")

from fastapi import FastAPI, Header, HTTPException  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from agent import responder  # noqa: E402  (del L6)
from comun import settings as cfg  # noqa: E402

app = FastAPI(title="Demo 1 · agente local detrás de FastAPI")


class ChatRequest(BaseModel):
    mensaje: str


class ChatResponse(BaseModel):
    respuesta: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest, x_api_key: str = Header(default="")):
    if x_api_key != cfg.AGENT_API_KEY:
        raise HTTPException(401, "API key inválida o ausente")
    return ChatResponse(respuesta=responder(payload.mensaje))


if __name__ == "__main__":
    import uvicorn

    print("=" * 72)
    print("  DEMO 1 · api.py local, con uvicorn")
    print(f"  AGENT_API_KEY de prueba: {cfg.AGENT_API_KEY}")
    print("  Prueba en otra terminal:")
    print("    curl http://127.0.0.1:8000/health")
    print(f'    curl -X POST http://127.0.0.1:8000/chat -H "X-API-Key: {cfg.AGENT_API_KEY}" '
          '-H "Content-Type: application/json" -d \'{"mensaje": "hola"}\'')
    print("=" * 72)
    uvicorn.run(app, host="127.0.0.1", port=8000)
