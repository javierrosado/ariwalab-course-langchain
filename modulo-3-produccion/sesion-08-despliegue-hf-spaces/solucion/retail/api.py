"""L8 · Retail — MercaSur · app/api.py (checkpoint de referencia)

Capa HTTP sobre el `agent.py` (v4) del L6. No reescribe ninguna lógica del agente: la
envuelve. Este es el módulo que arranca `CMD` del `Dockerfile` (`uvicorn app.api:app`).

Ejecutar localmente (antes de desplegar), desde la raíz del curso:
    uvicorn modulo-3-produccion.sesion-08-despliegue-hf-spaces.solucion.retail.api:app \
        --host 0.0.0.0 --port 7860
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-06-automatizacion-guardrails"
                       / "solucion" / "retail"))

from fastapi import FastAPI, Header, HTTPException  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from agent import responder  # noqa: E402  (del L6, que ya trae L4 + L5 dentro)
from comun import settings as cfg  # noqa: E402

app = FastAPI(title="Agente MercaSur — retail")


class ChatRequest(BaseModel):
    mensaje: str
    thread_id: str | None = None


class ChatResponse(BaseModel):
    respuesta: str


@app.get("/health")
def health() -> dict:
    """Sin autenticación: la plataforma lo llama para saber si el Space vive."""
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest, x_api_key: str = Header(default="")) -> ChatResponse:
    """Con X-API-Key: protege la cuota de HF Inference del equipo, no un secreto de negocio."""
    if not cfg.AGENT_API_KEY:
        raise HTTPException(500, "AGENT_API_KEY no está configurada en el servidor")
    if x_api_key != cfg.AGENT_API_KEY:
        raise HTTPException(401, "API key inválida o ausente")
    respuesta = responder(payload.mensaje, thread_id=payload.thread_id)
    return ChatResponse(respuesta=respuesta)
