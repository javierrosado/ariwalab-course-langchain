"""L3 · Seguros — Andina Seguros · external_api.py (checkpoint de referencia)

La primera tool del track. Es exactamente la misma que abre TOOLS_NUCLEO en el
domain_tools.py del L4 (Sesión 4).
"""

from __future__ import annotations

import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402

TRACK = "seguros"
HOY = date(2026, 9, 5)  # fecha de referencia del curso


class PlacaInput(BaseModel):
    placa: str = Field(description="Placa del vehículo en formato ABC-123")


@tool(args_schema=PlacaInput)
def get_policy_by_plate(placa: str) -> str:
    """Devuelve la póliza SOAT asociada a una placa, con su vigencia y estado.

    Úsala cuando el cliente pregunte si su SOAT está vigente, hasta cuándo,
    o quiera los datos de su póliza.
    NO la uses para cotizar una póliza nueva: eso llega en el Laboratorio 4.
    """
    try:
        p = datos.buscar_uno("polizas.csv", "placa", placa, TRACK)
    except DatoNoEncontrado:
        return (f"No hay ninguna póliza de Andina Seguros para la placa {placa}. "
                f"Verifica la placa con el cliente: el formato es ABC-123.")
    fin = datetime.strptime(p["fin_vigencia"], "%Y-%m-%d").date()
    dias = (fin - HOY).days
    estado = f"VENCIDA hace {abs(dias)} días." if dias < 0 else f"VIGENTE, vence en {dias} días."
    return (f"Póliza {p['poliza_id']} · Placa {p['placa']} · Titular: {p['titular']} · "
            f"Vigencia: {p['inicio_vigencia']} al {p['fin_vigencia']} · {estado}")
