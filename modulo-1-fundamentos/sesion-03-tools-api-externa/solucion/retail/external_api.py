"""L3 · Retail — MercaSur · external_api.py (checkpoint de referencia)

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

TRACK = "retail"


class PedidoInput(BaseModel):
    pedido_id: str = Field(description="Número de pedido en formato MS-2026-NNNNN")


@tool(args_schema=PedidoInput)
def track_order(pedido_id: str) -> str:
    """Devuelve el estado, el courier y el código de rastreo de un pedido.

    Úsala cuando el cliente pregunte dónde está su pedido, cuándo llega,
    o por qué no lo ha recibido.
    NO la uses para iniciar una devolución: eso llega en el Laboratorio 4.
    """
    try:
        p = datos.buscar_uno("pedidos.csv", "pedido_id", pedido_id, TRACK)
    except DatoNoEncontrado:
        return (f"No existe el pedido {pedido_id}. Verifica el número con el cliente: "
                f"el formato es MS-2026-NNNNN y aparece en el correo de confirmación.")
    return (f"Pedido {p['pedido_id']} · Cliente: {p['cliente']} · Comprado el {p['fecha_compra']} · "
            f"Estado: {p['estado']} · Courier: {p['courier']} · Rastreo: {p['codigo_tracking']} · "
            f"Despacho hacia {p['distrito_entrega']}")
