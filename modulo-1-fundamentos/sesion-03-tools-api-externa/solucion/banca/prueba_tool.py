"""L3 · Banca — Banco Inti · prueba_tool.py (checkpoint de referencia)

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/solucion/banca/prueba_tool.py

Escenarios 1 y 2 funcionan con DATA_SOURCE=csv (por defecto) o DATA_SOURCE=api.
El escenario 3 necesita DATA_SOURCE=api y el simulador desplegado.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from comun import settings as cfg  # noqa: E402

from external_api import get_account_balance  # noqa: E402

# Identificador real de recursos/datasets/banca/cuentas.csv.
CUENTA_REAL = "191-9450993-0-54"
CUENTA_INEXISTENTE = "191-0000000-0-00"


def escenario_1_exito() -> None:
    print("  Escenario 1 · ÉXITO")
    print("  " + "-" * 68)
    resultado = get_account_balance.invoke({"numero_cuenta": CUENTA_REAL})
    print(f"  Entrada: numero_cuenta={CUENTA_REAL}")
    print(f"  Salida:  {resultado}")
    assert "No existe" not in resultado, "Se esperaba un saldo real, no un mensaje de 'no existe'"
    print("  ✔ El agente citaría este dato real, sin inventar nada.\n")


def escenario_2_dato_inexistente() -> None:
    print("  Escenario 2 · DATO INEXISTENTE")
    print("  " + "-" * 68)
    resultado = get_account_balance.invoke({"numero_cuenta": CUENTA_INEXISTENTE})
    print(f"  Entrada: numero_cuenta={CUENTA_INEXISTENTE}")
    print(f"  Salida:  {resultado}")
    assert "No existe" in resultado, "La tool debería decir explícitamente que no existe"
    print("  ✔ La tool dice 'no existe' — el agente no tiene margen para inventar un saldo.\n")


def escenario_3_servicio_caido() -> None:
    print("  Escenario 3 · SERVICIO CAÍDO (?_fallo=error503)")
    print("  " + "-" * 68)
    if cfg.DATA_SOURCE != "api":
        print("  ⚠ DATA_SOURCE no es 'api': este escenario necesita el simulador real.")
        print("    Pon DATA_SOURCE=api en tu .env y vuelve a correr este script.\n")
        return

    from comun.api_client import RUTAS, SimuladorNoDisponible, _pedir  # noqa: PLC0415

    plantilla = RUTAS[("banca", "cuentas.csv", "numero_cuenta")]
    ruta_con_fallo = plantilla.format(valor=CUENTA_REAL) + "?_fallo=error503"
    print(f"  GET {ruta_con_fallo}")
    try:
        _pedir(ruta_con_fallo)
    except SimuladorNoDisponible as e:
        print(f"  Salida: {e}")
        print("  ✔ Excepción controlada, con un mensaje que el modelo puede leer y actuar.\n")
        return
    print("  ⚠ No se lanzó SimuladorNoDisponible — revisa si el simulador está respondiendo.\n")


def main() -> None:
    print("=" * 72)
    print("  PRUEBA_TOOL · banca · get_account_balance")
    print("=" * 72 + "\n")
    escenario_1_exito()
    escenario_2_dato_inexistente()
    escenario_3_servicio_caido()
    print("Los 3 escenarios corrieron. Pega estas trazas en tu EVIDENCIA-A1.md.")


if __name__ == "__main__":
    main()
