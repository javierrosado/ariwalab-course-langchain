"""L3 · Banca — Banco Inti · external_api.py (checkpoint de referencia)

La primera tool del track. Es exactamente la misma que abre TOOLS_NUCLEO en el
domain_tools.py del L4 (Sesión 4).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402

TRACK = "banca"


class CuentaInput(BaseModel):
    numero_cuenta: str = Field(description="Número de cuenta en formato 191-XXXXXXX-0-XX")


@tool(args_schema=CuentaInput)
def get_account_balance(numero_cuenta: str) -> str:
    """Devuelve el saldo, la moneda y el estado de una cuenta.

    Úsala cuando el cliente pregunte cuánto tiene, su saldo disponible,
    o si su cuenta está activa o bloqueada.
    NO la uses para ver movimientos o consumos: eso llega en el Laboratorio 4.
    """
    try:
        c = datos.buscar_uno("cuentas.csv", "numero_cuenta", numero_cuenta, TRACK)
    except DatoNoEncontrado:
        return (f"No existe la cuenta {numero_cuenta} en Banco Inti. "
                f"Verifica el número con el cliente: el formato es 191-XXXXXXX-0-XX.")
    simbolo = "S/" if c["moneda"] == "PEN" else "USD"
    alerta = " ATENCIÓN: la cuenta está BLOQUEADA." if c["estado"] == "BLOQUEADA" else ""
    return (f"Cuenta {c['numero_cuenta']} ({c['tipo_cuenta']}) · Titular: {c['titular']} · "
            f"Saldo: {simbolo} {c['saldo']} · Estado: {c['estado']}.{alerta}")
