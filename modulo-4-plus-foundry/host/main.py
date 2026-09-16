"""Bonus · Foundry — host/main.py (checkpoint de referencia)

Envuelve el agente del curso con `ResponsesHostServer` de `langchain_azure_ai.agents.hosting`
(paquete `langchain-azure-ai[hosting]`, en preview — ver el riesgo R8 en
`docente/esqueletos/bonus-foundry.md` §8: **re-verifícalo contra tu propio proyecto de
Foundry antes de confiar en este archivo**, la API de un paquete en preview puede cambiar
entre versiones).

LO QUE SÍ PORTA SIN TOCARSE: `comun.provider.get_chat_model()` (decisión D13), las 4 tools
núcleo del track (L4) y el retriever (L5) — se siguen importando exactamente igual que en
el resto del curso. Cambiar `AI_PROVIDER=huggingface` a `AI_PROVIDER=foundry` en el `.env`
(o como variable del entorno de Foundry) es el único cambio real.

LO QUE NO PORTA TAL CUAL: los guardrails del L6 y la memoria del L5, porque están escritos
como una función Python con un bucle manual (`agent.py` del curso), y `ResponsesHostServer`
espera un grafo de LangGraph ya compilado (lo que produce `create_agent()`). Portar los
guardrails como middleware de LangGraph es una construcción real pero más profunda —
queda señalada aquí, no resuelta, y es exactamente el tipo de trabajo que cubre el Curso 2
(ver `puente-curso-2.md`).

Ejecutar localmente (requiere `pip install -U "langchain-azure-ai[hosting]>=1.2.9" azure-identity`
y las variables FOUNDRY_PROJECT_ENDPOINT / FOUNDRY_MODEL_NAME, o AI_ENDPOINT / AI_API_KEY /
AI_MODEL / AI_PROVIDER=foundry del .env del curso):
    python modulo-4-plus-foundry/host/main.py
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from langchain.agents import create_agent  # noqa: E402

from comun import settings as cfg  # noqa: E402
from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402


def _cargar_tools_del_track(track: str) -> list:
    """Importa TOOLS_NUCLEO y el retriever del track, con el mismo sys.path chaining
    que usa cada `agent.py` del curso desde el L6 en adelante.
    """
    sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-04-tools-multiples"
                           / "solucion" / track))
    sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-05-memoria-rag"
                           / "solucion" / track))

    domain_tools = importlib.import_module("domain_tools")
    retriever_mod = importlib.import_module("knowledge.retriever")
    return list(domain_tools.TOOLS_NUCLEO) + [retriever_mod.retrieve_knowledge_base]


def construir_agente():
    track = cfg.COURSE_TRACK
    modelo = get_chat_model()
    tools = _cargar_tools_del_track(track)
    return create_agent(modelo, tools=tools, system_prompt=get_system_prompt(track))


def main() -> None:
    if cfg.AI_PROVIDER != "foundry":
        print(f"Aviso: AI_PROVIDER='{cfg.AI_PROVIDER}', no 'foundry'. "
              f"Este host está pensado para correr contra Foundry.")
    print(f"Construyendo el agente de {cfg.COURSE_TRACK} sobre {describe_provider()}...")

    grafo = construir_agente()

    from langchain_azure_ai.agents.hosting import ResponsesHostServer

    puerto = int(os.environ.get("PORT", "8088"))
    print(f"Sirviendo en 0.0.0.0:{puerto}/responses")
    ResponsesHostServer(grafo).run(port=puerto)


if __name__ == "__main__":
    main()
