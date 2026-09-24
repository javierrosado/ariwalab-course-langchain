"""Configuración central del curso.

Carga el .env de la raíz del curso y expone los valores como constantes tipadas.
Ningún otro módulo debe leer os.getenv directamente: así hay un único lugar
donde ver qué variables necesita el curso.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# La raíz del curso es el directorio padre de comun/
COURSE_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(COURSE_ROOT / ".env")

# ---------- Proveedor de modelos ----------
# "huggingface" durante las sesiones 1-11 | "foundry" solo en el bonus
AI_PROVIDER: str = os.getenv("AI_PROVIDER", "huggingface").strip().lower()

# ---------- Hugging Face (open source, en línea) ----------
HF_TOKEN: str = os.getenv("HF_TOKEN", "")
HF_BASE_URL: str = os.getenv("HF_BASE_URL", "https://router.huggingface.co/v1")
# Modelo de referencia. Verificar disponibilidad, Tool Calling y bucle ReAct
# antes de cada edición con python -m comun.check_stack --solo-modelo.
HF_CHAT_MODEL: str = os.getenv("HF_CHAT_MODEL", "Qwen/Qwen3-32B")

# Qwen3 alterna entre modo "thinking" y "non-thinking". Para agentes conviene
# non-thinking: es más rápido, más barato y las trazas de razonamiento pueden
# interferir con el parseo de tool_call en algunos stacks de servicio.
HF_ENABLE_THINKING: bool = os.getenv("HF_ENABLE_THINKING", "false").strip().lower() == "true"
HF_EMBEDDING_MODEL: str = os.getenv("HF_EMBEDDING_MODEL", "intfloat/multilingual-e5-large")

# Personalización por industria: las 4 industrias comparten el MISMO modelo.
# Lo que las diferencia es el system prompt (comun/prompts_industria.py) y su
# colección de Qdrant, no los pesos.
#
# TRACK_MODELS queda como punto de extensión por si en una edición futura se afina
# un modelo por industria. Hoy está vacío y no se usa.
TRACK_MODELS: dict[str, str] = {
    "telecomunicaciones": os.getenv("HF_MODEL_TELCO", ""),
    "banca": os.getenv("HF_MODEL_BANCA", ""),
    "retail": os.getenv("HF_MODEL_RETAIL", ""),
    "seguros": os.getenv("HF_MODEL_SEGUROS", ""),
}

# ---------- Microsoft Foundry (solo bonus) ----------
AI_ENDPOINT: str = os.getenv("AI_ENDPOINT", "")
AI_API_KEY: str = os.getenv("AI_API_KEY", "")
AI_MODEL: str = os.getenv("AI_MODEL", "gpt-5-mini")
AI_EMBEDDING_MODEL: str = os.getenv("AI_EMBEDDING_MODEL", "text-embedding-3-small")

# ---------- Fuente de datos de las tools ----------
# "csv" → datasets locales (Laboratorios 1 y 2)
# "api" → simulador de industria (Laboratorio 3 en adelante)
DATA_SOURCE: str = os.getenv("DATA_SOURCE", "csv").strip().lower()
SIM_BASE_URL: str = os.getenv("SIM_BASE_URL", "http://localhost:8000")
SIM_API_KEY: str = os.getenv("SIM_API_KEY", "")
SIM_TIMEOUT: float = float(os.getenv("SIM_TIMEOUT", "10"))

# Servidor MCP del simulador (Laboratorio 4)
MCP_TRANSPORT: str = os.getenv("MCP_TRANSPORT", "stdio").strip().lower()  # stdio | http
MCP_HTTP_URL: str = os.getenv("MCP_HTTP_URL", "http://localhost:8000/mcp")
MCP_STDIO_CMD: str = os.getenv("MCP_STDIO_CMD", "python")
MCP_STDIO_ARGS: str = os.getenv("MCP_STDIO_ARGS", "simulador-industria/mcp_server.py")

# ---------- Qdrant Cloud ----------
QDRANT_URL: str = os.getenv("QDRANT_URL", "")
QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
QDRANT_COLLECTION: str = os.getenv("QDRANT_COLLECTION", "kb-demo")

# ---------- Langfuse Cloud ----------
LANGFUSE_PUBLIC_KEY: str = os.getenv("LANGFUSE_PUBLIC_KEY", "")
LANGFUSE_SECRET_KEY: str = os.getenv("LANGFUSE_SECRET_KEY", "")
LANGFUSE_HOST: str = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

# ---------- Track de industria ----------
COURSE_TRACK: str = os.getenv("COURSE_TRACK", "telecomunicaciones").strip().lower()

# ---------- API del agente desplegado (sesión 8) ----------
# Vive como Space secret en producción, nunca en el repo. La protege porque
# gasta cuota de HF Inference del equipo, no porque los datos sean confidenciales.
AGENT_API_KEY: str = os.getenv("AGENT_API_KEY", "")

VALID_TRACKS = ("telecomunicaciones", "banca", "retail", "seguros")
VALID_PROVIDERS = ("huggingface", "foundry")
VALID_DATA_SOURCES = ("csv", "api")


def require(name: str, value: str) -> str:
    """Falla temprano y con un mensaje útil si falta una variable de entorno."""
    if not value:
        raise RuntimeError(
            f"Falta la variable {name} en {COURSE_ROOT / '.env'}. "
            f"Copia .env.example a .env y complétala."
        )
    return value
