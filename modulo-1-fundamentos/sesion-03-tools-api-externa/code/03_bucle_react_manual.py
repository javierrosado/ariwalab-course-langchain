"""Demo 3 · El bucle ReAct escrito a mano, en ~20 líneas, con tope de iteraciones (A4).

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/code/03_bucle_react_manual.py

Requiere HF_TOKEN.

Qué deberías observar: el "razonamiento" del agente es un `while` normal, que TÚ
controlas — no hay ninguna inteligencia oculta en el bucle. Compáralo con la
demo 4 (create_agent): son la misma lógica, con y sin abstracción.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage  # noqa: E402
from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

TRACK = "telecomunicaciones"
MAX_ITERATIONS = 4


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


# ─────────────────────────── EL BUCLE, ~20 LÍNEAS ───────────────────────────
def run_agent(model, tools, pregunta: str) -> str:
    tools_by_name = {t.name: t for t in tools}
    model_with_tools = model.bind_tools(tools)
    messages = [SystemMessage(content="Eres el asistente de AndesMóvil."),
                HumanMessage(content=pregunta)]

    for iteracion in range(1, MAX_ITERATIONS + 1):
        print(f"    Iteración {iteracion}: el modelo razona...")
        ai_message = model_with_tools.invoke(messages)
        messages.append(ai_message)

        if not ai_message.tool_calls:
            return ai_message.content  # el modelo ya tiene lo que necesita: responde

        for call in ai_message.tool_calls:
            print(f"      → acción: {call['name']}({call['args']})")
            resultado = tools_by_name[call["name"]].invoke(call["args"])
            print(f"      ← observación: {resultado}")
            messages.append(ToolMessage(content=str(resultado), tool_call_id=call["id"]))

    return "No se pudo resolver en el límite de iteraciones. Derivo a un asesor humano."
# ──────────────────────────────────────────────────────────────────────────


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · Bucle ReAct manual (~20 líneas)")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()
    pregunta = "¿Qué plan tengo? Mi línea es 987654321"
    print(f"\n  Pregunta: {pregunta}\n")

    respuesta = run_agent(model, [get_customer_plan], pregunta)
    print(f"\n  Respuesta final: {respuesta}")

    print("""

  Esto es TODO lo que hace un agente por dentro: razonar (invocar al modelo),
  actuar (ejecutar la tool que propuso) y observar (devolverle el resultado),
  repitiendo hasta que el modelo ya no necesita más datos — o hasta el tope de
  iteraciones, que es lo que te protege de un bucle infinito (regla A4). La demo 4
  hace exactamente esto mismo con create_agent().
""")


if __name__ == "__main__":
    main()
