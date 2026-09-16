"""L3 · Telecomunicaciones — AndesMóvil · external_api.py (checkpoint de referencia)

La primera tool del track. Es exactamente la misma que abre TOOLS_NUCLEO en el
domain_tools.py del L4 (Sesión 4) — no es un ejercicio aislado, es el primer cuarto
de ese catálogo. `datos.buscar_uno()` va al simulador real cuando DATA_SOURCE=api en
el .env, y a los CSV locales cuando DATA_SOURCE=csv, sin que esta tool note la
diferencia: esa indirección es la lección del laboratorio.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

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

    Úsala cuando el cliente pregunte qué plan tiene, cuánto paga, desde cuándo es
    cliente, o si su línea está activa o suspendida.
    NO la uses para consultar consumo de datos: eso llega en el Laboratorio 4.
    NO la uses para preguntas generales sobre el catálogo de planes de AndesMóvil:
    esa información está en la base de conocimiento (Sesión 5), no aquí.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return (f"No existe la línea {numero_linea} en los registros de AndesMóvil. "
                f"Verifica el número con el cliente: debe tener 9 dígitos.")
    return (f"Línea {c['numero_linea']} · Titular: {c['nombre_titular']} · "
            f"Plan: {c['plan_nombre']} ({c['plan_id']}) · Estado: {c['estado']} · "
            f"Cliente desde: {c['fecha_alta']} · Distrito: {c['distrito']}")
