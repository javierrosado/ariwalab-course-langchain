"""L4 · Banca — Banco Inti · domain_tools.py (checkpoint de referencia)

Las 4 tools núcleo del track — las 4 son de solo lectura (ver la nota de README.md:
la única acción de escritura del track, el bloqueo de tarjeta, es irreversible y
queda como tool opcional de reto, no como núcleo).

La primera tool (`get_account_balance`) NO se reescribe: se importa tal cual del L3
(Sesión 3) — el mismo patrón con el que la Sesión 5 importa este archivo y la Sesión 6
importa el de la Sesión 5. La cadena L2 → L3 → L4 → L5 → L6 se apoya en código real.
La categoría del L2 (`recursos/golden/consultas-banca.json`, campo `intencion`) es 1:1
con estas 4 tools (campo `tool_esperada`): es el mismo golden set el que mide el L2
(`medir_clasificador.py`) y el L4 (`docente/matriz_seleccion.py`).

Regla A2: cada docstring dice QUÉ hace, CUÁNDO usarla y CUÁNDO NO.

Nota sobre la regla A3: en
telecomunicaciones, retail y seguros, la tool de escritura del núcleo normaliza su
campo de enum con `extraer()` de `comun/structured.py` antes de pedir confirmación.
Banca no lo replica aquí porque, por diseño (ver arriba), **no tiene ninguna tool de
escritura en su núcleo** — la única candidata, `request_card_block`, es opcional y
queda fuera de `TOOLS_NUCLEO`. No hay ningún enum de escritura que validar en este
archivo.
"""

from __future__ import annotations

import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
# La tool del L3 no se reescribe: se importa de su checkpoint de referencia.
sys.path.insert(0, str(ROOT / "modulo-1-fundamentos" / "sesion-03-tools-api-externa"
                       / "solucion" / "banca"))

from langchain_core.tools import tool  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402

from comun import datos  # noqa: E402
from comun.datos import DatoNoEncontrado  # noqa: E402

from external_api import CuentaInput, get_account_balance  # noqa: E402  (del L3, sin reescribir)

TRACK = "banca"
HOY = date(2026, 9, 5)  # fecha de referencia del curso


# ───────────────────── esquemas nuevos del L4 ─────────────────────
# CuentaInput se reutiliza del L3 (import de arriba): get_card_info la necesita
# con el mismo esquema, no con una copia.
class MovimientosInput(BaseModel):
    numero_cuenta: str = Field(description="Número de cuenta en formato 191-XXXXXXX-0-XX")
    dias: int = Field(default=30, ge=1, le=90, description="Días hacia atrás a consultar, entre 1 y 90")


class MovimientoInput(BaseModel):
    movimiento_id: str = Field(description="Identificador del movimiento en formato MOV-NNNNNNN")


# get_account_balance del L3 se usa tal cual (import de arriba).


# ─────────────────────────── tools nuevas del L4 ───────────────────────────
@tool(args_schema=MovimientosInput)
def list_transactions(numero_cuenta: str, dias: int = 30) -> str:
    """Lista los movimientos de una cuenta en los últimos N días, del más reciente al más antiguo.

    Úsala cuando el cliente pregunte por sus consumos, sus últimos movimientos,
    un cargo que no reconoce, o cuánto gastó en un periodo.
    NO la uses para consultar el saldo: para eso usa get_account_balance.
    """
    try:
        datos.buscar_uno("cuentas.csv", "numero_cuenta", numero_cuenta, TRACK)
    except DatoNoEncontrado:
        return f"No existe la cuenta {numero_cuenta}."
    corte = HOY - timedelta(days=dias)
    movs = [m for m in datos.buscar_todos("movimientos.csv", "numero_cuenta", numero_cuenta, TRACK)
            if datetime.strptime(m["fecha"], "%Y-%m-%d").date() >= corte]
    if not movs:
        return f"La cuenta {numero_cuenta} no registra movimientos en los últimos {dias} días."
    movs.sort(key=lambda m: m["fecha"], reverse=True)
    lineas = [f"{m['fecha']} · {m['descripcion']} · S/ {m['monto']} · {m['canal']} · {m['movimiento_id']}"
              for m in movs[:15]]
    total_cargos = sum(float(m["monto"]) for m in movs if m["tipo"] == "CARGO")
    resumen = (f"{len(movs)} movimientos en {dias} días · "
               f"Total de cargos: S/ {abs(total_cargos):.2f}")
    extra = f"\n(Se muestran los 15 más recientes de {len(movs)})" if len(movs) > 15 else ""
    return resumen + "\n" + "\n".join(lineas) + extra


@tool(args_schema=CuentaInput)
def get_card_info(numero_cuenta: str) -> str:
    """Devuelve los datos de la tarjeta asociada a una cuenta, con el número enmascarado.

    Úsala cuando el cliente pregunte por su tarjeta, su línea de crédito,
    su fecha de facturación o si su tarjeta está activa.
    NO la uses para bloquear la tarjeta: esa acción no está en el núcleo (ver reto opcional).
    Esta tool NUNCA devuelve el número completo de la tarjeta, solo los últimos 4 dígitos.
    """
    tarjetas = datos.buscar_todos("tarjetas.csv", "numero_cuenta", numero_cuenta, TRACK)
    if not tarjetas:
        return f"La cuenta {numero_cuenta} no tiene tarjetas asociadas registradas."
    salida = []
    for t in tarjetas:
        salida.append(
            f"Tarjeta {t['tarjeta_id']} ({t['marca']}) terminada en {t['ultimos_4_digitos']} · "
            f"Estado: {t['estado']} · Línea de crédito: S/ {t['linea_credito']} · "
            f"Facturación el día {t['dia_facturacion']} de cada mes"
        )
    return "\n".join(salida)


@tool(args_schema=MovimientoInput)
def score_transaction_risk(movimiento_id: str) -> str:
    """Devuelve el puntaje de riesgo de fraude de un movimiento y el motivo de la alerta.

    Úsala cuando el cliente diga que no reconoce una operación, sospeche de un cargo,
    o pregunte por qué le llegó una alerta de seguridad.
    NO la uses para listar movimientos: primero usa list_transactions para obtener el
    movimiento_id, y recién entonces evalúa el riesgo de ese movimiento concreto.
    NO afirmes ni descartes fraude por tu cuenta: reporta el puntaje y la acción sugerida.
    """
    try:
        mov = datos.buscar_uno("movimientos.csv", "movimiento_id", movimiento_id, TRACK)
    except DatoNoEncontrado:
        return (f"No existe el movimiento {movimiento_id}. "
                f"Usa list_transactions para obtener los identificadores válidos.")
    alertas = datos.buscar_todos("alertas_riesgo.csv", "movimiento_id", movimiento_id, TRACK)
    base = (f"Movimiento {movimiento_id}: {mov['descripcion']} · S/ {mov['monto']} · "
            f"{mov['fecha']} · canal {mov['canal']} · ubicación {mov['ubicacion']}")
    if not alertas:
        return base + "\nSin alerta de riesgo asociada: el puntaje quedó por debajo de 55 (riesgo bajo)."
    a = alertas[0]
    score = int(a["score_riesgo"])
    nivel = "ALTO" if score >= 80 else "MEDIO"
    accion = ("Riesgo ALTO: requiere confirmación del cliente y derivación a un asesor humano."
              if score >= 80 else
              "Riesgo MEDIO: la operación se procesó y se notificó al cliente.")
    return (base + f"\nAlerta {a['alerta_id']} · Puntaje: {score}/100 (riesgo {nivel}) · "
            f"Motivo: {a['motivo']} · Estado: {a['estado']}\n{accion}")


TOOLS_NUCLEO = [get_account_balance, list_transactions, get_card_info, score_transaction_risk]
