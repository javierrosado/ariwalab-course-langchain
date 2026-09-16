"""L3 · Seguros — Andina Seguros · prueba_tool.py (checkpoint de referencia)

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/solucion/seguros/prueba_tool.py

Escenarios 1 y 2 funcionan con DATA_SOURCE=csv (por defecto) o DATA_SOURCE=api.
El escenario 3 necesita DATA_SOURCE=api y el simulador desplegado.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from comun import settings as cfg  # noqa: E402

from external_api import get_policy_by_plate  # noqa: E402

# Identificador real de recursos/datasets/seguros/polizas.csv.
PLACA_REAL = "VEX-958"
PLACA_INEXISTENTE = "ZZZ-000"


def escenario_1_exito() -> None:
    print("  Escenario 1 · ÉXITO")
    print("  " + "-" * 68)
    resultado = get_policy_by_plate.invoke({"placa": PLACA_REAL})
    print(f"  Entrada: placa={PLACA_REAL}")
    print(f"  Salida:  {resultado}")
    assert "No hay ninguna" not in resultado, "Se esperaba una póliza real"
    print("  ✔ El agente citaría este dato real, sin inventar nada.\n")


def escenario_2_dato_inexistente() -> None:
    print("  Escenario 2 · DATO INEXISTENTE")
    print("  " + "-" * 68)
    resultado = get_policy_by_plate.invoke({"placa": PLACA_INEXISTENTE})
    print(f"  Entrada: placa={PLACA_INEXISTENTE}")
    print(f"  Salida:  {resultado}")
    assert "No hay ninguna" in resultado, "La tool debería decir explícitamente que no existe"
    print("  ✔ La tool dice 'no hay póliza' — el agente no tiene margen para inventar una.\n")


def escenario_3_servicio_caido() -> None:
    print("  Escenario 3 · SERVICIO CAÍDO (?_fallo=error503)")
    print("  " + "-" * 68)
    if cfg.DATA_SOURCE != "api":
        print("  ⚠ DATA_SOURCE no es 'api': este escenario necesita el simulador real.")
        print("    Pon DATA_SOURCE=api en tu .env y vuelve a correr este script.\n")
        return

    from comun.api_client import RUTAS, SimuladorNoDisponible, _pedir  # noqa: PLC0415

    plantilla = RUTAS[("seguros", "polizas.csv", "placa")]
    ruta_con_fallo = plantilla.format(valor=PLACA_REAL) + "?_fallo=error503"
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
    print("  PRUEBA_TOOL · seguros · get_policy_by_plate")
    print("=" * 72 + "\n")
    escenario_1_exito()
    escenario_2_dato_inexistente()
    escenario_3_servicio_caido()
    print("Los 3 escenarios corrieron. Pega estas trazas en tu EVIDENCIA-A1.md.")


if __name__ == "__main__":
    main()
