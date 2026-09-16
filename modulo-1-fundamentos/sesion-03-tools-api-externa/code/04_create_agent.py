"""Demo 4 · Lo mismo que la demo 3, con create_agent() — la abstracción, no la magia.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/code/04_create_agent.py

Requiere HF_TOKEN.

Qué deberías observar: el resultado es el mismo que en la demo 3. create_agent()
no razona mejor ni peor que tu bucle manual — implementa el mismo patrón
(Thought → Action → Observation) con un tope de iteraciones ya incorporado, sin
que tengas que escribirlo cada vez. Ahora que viste el bucle a mano, sabes qué hay
detrás de estas 3 líneas.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain.agents import create_agent  # noqa: E402
from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

TRACK = "telecomunicaciones"


class LineaInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")


@tool(args_schema=LineaInput)
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene o si su línea está activa.
    NO la uses para consultar consumo de datos.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return f"No existe la línea {numero_linea}. Verifica el número con el cliente."
    return f"Línea {c['numero_linea']} · Plan: {c['plan_nombre']} · Estado: {c['estado']}"


def main() -> None:
    print("=" * 72)
    print("  DEMO 4 · create_agent() — las mismas ~20 líneas, en 3")
    print(f"  {describe_provider()}")
    print("=" * 72)

    # ── Las 3 líneas ─────────────────────────────────────────────────────
    agente = create_agent(get_chat_model(), [get_customer_plan],
                          system_prompt="Eres el asistente de AndesMóvil.")
    resultado = agente.invoke({"messages": [("human", "¿Qué plan tengo? Mi línea es 987654321")]})
    respuesta = resultado["messages"][-1].content
    # ─────────────────────────────────────────────────────────────────────

    print(f"\n  Respuesta final: {respuesta}")

    print("\n  Traza completa (mismo patrón que el bucle manual de la demo 3):")
    for m in resultado["messages"]:
        tipo = type(m).__name__
        if getattr(m, "tool_calls", None):
            print(f"    {tipo}: propone {m.tool_calls}")
        else:
            print(f"    {tipo}: {m.content}")

    print("""

  Compara esta traza con los prints de la demo 3: son el mismo patrón — Human,
  luego un AIMessage que propone una tool_call, luego un ToolMessage con el
  resultado, luego el AIMessage final. create_agent() no te oculta ese patrón:
  solo te evita escribir el while que lo recorre.
""")


if __name__ == "__main__":
    main()
