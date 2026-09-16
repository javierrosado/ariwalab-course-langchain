"""Demo 1 · @tool + args_schema, invocada directamente desde Python.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/code/01_tool_simple.py

No requiere HF_TOKEN: esta demo no llama a ningún modelo. Usa DATA_SOURCE=csv (el
valor por defecto del .env), así que tampoco necesita el simulador desplegado.

Qué deberías observar: una tool es una función normal de Python. Sin ningún modelo
de por medio, `get_customer_plan.invoke(...)` funciona exactamente igual. El modelo
no le agrega magia a la tool: solo decide cuándo llamarla.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402

TRACK = "telecomunicaciones"


class LineaInput(BaseModel):
    numero_linea: str = Field(description="Número de línea móvil de 9 dígitos, sin espacios ni guiones")


@tool(args_schema=LineaInput)
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene, si su línea está activa
    o en qué distrito está registrada.
    NO la uses para consultar consumo de datos ni para registrar un reclamo.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return f"No existe la línea {numero_linea} en los registros de AndesMóvil."
    return (f"Línea {c['numero_linea']} · Titular: {c['nombre_titular']} · "
            f"Plan: {c['plan_nombre']} · Estado: {c['estado']}")


def main() -> None:
    print("=" * 72)
    print("  DEMO 1 · @tool invocada directamente, sin modelo")
    print("=" * 72)

    print(f"\n  Nombre de la tool: {get_customer_plan.name}")
    print(f"  Descripción (lo que lee el modelo):\n{get_customer_plan.description}\n")
    print(f"  Esquema de argumentos: {get_customer_plan.args}")

    print("\n  Invocándola directamente, SIN ningún modelo:")
    resultado = get_customer_plan.invoke({"numero_linea": "987654321"})
    print(f"  → {resultado}")

    print("""

  Fíjate en que no hubo ningún LLM en esta demo. `get_customer_plan` es una función
  de Python común y corriente, decorada con @tool. Lo único que el decorador agrega
  es la capacidad de describirse a sí misma (.name, .description, .args) para que
  un modelo, más adelante, pueda decidir invocarla. Eso es todo lo que hace @tool.
""")


if __name__ == "__main__":
    main()
