"""Demo 1 · Un agente con las 4 tools del track (telecomunicaciones).

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-04-tools-multiples/code/01_multi_tool.py

Requiere HF_TOKEN en el .env. Usa la implementación de referencia del docente
(proyecto-final/telecomunicaciones/), no la del alumno: es una demo del docente, no el L4.

Qué deberías observar:
  1. El mismo agente, con las mismas 4 tools enlazadas, elige distinto según cómo se
     formule la pregunta — el modelo decide con el nombre y la docstring, nunca con tu
     código.
  2. Una pregunta de tarifa NO dispara ninguna tool: todavía no hay RAG (eso es la S5),
     así que el agente debería decir que no tiene esa información, no inventarla.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage  # noqa: E402

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402


def load_reference_tools(track: str):
    """Carga TOOLS_NUCLEO de la implementación de referencia del docente (proyecto-final/).

    Es una demo del docente: usa la referencia a propósito. En tu propio Laboratorio 4
    escribirás y medirás TU catálogo (lab/<track>/domain_tools.py), no este.
    """
    ruta = ROOT / "proyecto-final" / track / "app" / "tools" / "domain_tools.py"
    spec = importlib.util.spec_from_file_location(f"tools_{track}", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TOOLS_NUCLEO


TOOLS_NUCLEO = load_reference_tools("telecomunicaciones")
MAX_ITERATIONS = 4

QUESTIONS = [
    "¿Cuántos gigas me quedan? Mi línea es 987654321",
    "No tengo señal desde ayer, la línea es 912345678",
    "Quiero dejar un reclamo por avería, llevo tres días sin servicio, línea 987654321",
    "¿Cuánto cuesta el plan Max 89 al mes?",  # sin tool: debe ir a RAG (S5), hoy no existe
]


def run_agent(model_with_tools, tools_by_name: dict, system_prompt: str, question: str):
    messages = [SystemMessage(content=system_prompt), HumanMessage(content=question)]
    tool_calls_made = []
    for _ in range(MAX_ITERATIONS):
        ai_message: AIMessage = model_with_tools.invoke(messages)
        messages.append(ai_message)
        if not ai_message.tool_calls:
            return ai_message.content, tool_calls_made
        for call in ai_message.tool_calls:
            tool_calls_made.append(call["name"])
            tool = tools_by_name[call["name"]]
            try:
                result = tool.invoke(call["args"])
            except Exception as e:  # noqa: BLE001
                result = f"Error al ejecutar {call['name']}: {type(e).__name__}: {e}"
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return "No se pudo resolver en el límite de iteraciones.", tool_calls_made


def main() -> None:
    print("=" * 72)
    print("  DEMO 1 · Un agente, 4 tools (telecomunicaciones)")
    print(f"  {describe_provider()}")
    print("=" * 72)

    tools_by_name = {t.name: t for t in TOOLS_NUCLEO}
    model = get_chat_model()
    model_with_tools = model.bind_tools(TOOLS_NUCLEO)
    system_prompt = get_system_prompt("telecomunicaciones")

    for question in QUESTIONS:
        print(f"\n  Pregunta: {question}")
        try:
            answer, calls = run_agent(model_with_tools, tools_by_name, system_prompt, question)
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error: {type(e).__name__}: {e}")
            return
        print(f"  Tools llamadas: {calls or '(ninguna)'}")
        print(f"  Respuesta: {answer}")
        print("  " + "-" * 68)

    print("""
  Fíjate en la última pregunta: es una de tarifas. El agente no debería haber llamado a
  ninguna tool (no hay ninguna que responda eso), y tampoco debería haber inventado un
  precio. Si lo hizo, es la demostración en vivo de por qué el sistema prompt lleva la
  salvaguarda A6 desde la Sesión 5 en adelante.
""")


if __name__ == "__main__":
    main()
