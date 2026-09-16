"""L11 · Retail — MercaSur · app/api.py (checkpoint de referencia)

Idéntico al `api.py` del L8, con un endpoint nuevo: `/chat/stream`, que consume
`responder_streaming()` de esta sesión. `CORSMiddleware` se añade porque
`code/index.html` se abre como archivo local (`file://`) y el navegador bloquearía
la petición al Space sin cabeceras CORS explícitas.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi import FastAPI, Header, HTTPException  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.responses import StreamingResponse  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from agent import responder, responder_streaming  # noqa: E402  (de esta sesión)
from comun import settings as cfg  # noqa: E402

app = FastAPI(title="Agente MercaSur — retail")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # el cliente de referencia se abre como file://, sin origen fijo
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    mensaje: str
    thread_id: str | None = None


class ChatResponse(BaseModel):
    respuesta: str


def _verificar_key(x_api_key: str) -> None:
    if not cfg.AGENT_API_KEY:
        raise HTTPException(500, "AGENT_API_KEY no está configurada en el servidor")
    if x_api_key != cfg.AGENT_API_KEY:
        raise HTTPException(401, "API key inválida o ausente")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest, x_api_key: str = Header(default="")) -> ChatResponse:
    _verificar_key(x_api_key)
    return ChatResponse(respuesta=responder(payload.mensaje, thread_id=payload.thread_id))


@app.post("/chat/stream")
def chat_stream(payload: ChatRequest, x_api_key: str = Header(default="")) -> StreamingResponse:
    """Server-Sent Events: una línea "data: {...}\\n\\n" por fragmento, y "data: [DONE]"
    al terminar. Ver la nota de honestidad en agent.py sobre por qué esto transmite
    palabra por palabra un texto YA validado, no tokens en vivo del modelo.
    """
    _verificar_key(x_api_key)

    def eventos():
        import json
        for fragmento in responder_streaming(payload.mensaje, thread_id=payload.thread_id):
            yield f"data: {json.dumps({'delta': fragmento})}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(eventos(), media_type="text/event-stream")
