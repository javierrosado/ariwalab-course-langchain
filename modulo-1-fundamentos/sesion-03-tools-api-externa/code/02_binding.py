"""Demo 2 · bind_tools() e imprimir el tool_call SIN ejecutarlo. LA DEMO DE LA SESIÓN.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/code/02_binding.py

Requiere HF_TOKEN.

Qué deberías observar: el modelo devuelve un `tool_call` — un nombre y unos
argumentos en JSON. Este script NO invoca la tool con ese resultado. Nada pasó
todavía: ninguna base de datos fue consultada, ningún archivo fue leído. El modelo
solo escribió una intención. Es el diagrama del bloque 1 del README, visto con
tus propios ojos.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun.provider import describe_provider, get_chat_model  # noqa: E402


class LineaInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")


@tool(args_schema=LineaInput)
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene o si su línea está activa.
    NO la uses para consultar consumo de datos.
    """
    raise RuntimeError("Esta demo nunca debería llegar a ejecutar la tool de verdad.")


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · bind_tools() — el modelo propone, nadie ejecuta")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()
    model_with_tools = model.bind_tools([get_customer_plan])

    pregunta = "¿Qué plan tengo? Mi línea es 987654321"
    print(f"\n  Pregunta: {pregunta}\n")

    try:
        respuesta = model_with_tools.invoke(pregunta)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error: {type(e).__name__}: {e}")
        return

    print(f"  respuesta.content = {respuesta.content!r}  (vacío o casi: el modelo no 'contestó')")
    print(f"  respuesta.tool_calls = {respuesta.tool_calls}")

    print("""

  Repite conmigo: NO se ejecutó get_customer_plan. Si lo hubiéramos hecho, este
  script habría reventado con el RuntimeError de la línea 34 — a propósito, para que
  quede clarísimo si alguien "hace trampa" y la invoca. El modelo solo produjo el
  diccionario de tool_calls de arriba: un nombre y unos argumentos en JSON. Convertir
  eso en una llamada real es una decisión de TU código, que tomas en la demo 3.
""")


if __name__ == "__main__":
    main()
