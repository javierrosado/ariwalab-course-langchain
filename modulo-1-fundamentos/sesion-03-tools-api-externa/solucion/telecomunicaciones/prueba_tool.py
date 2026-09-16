"""L3 · Telecomunicaciones — AndesMóvil · prueba_tool.py (checkpoint de referencia)

Llama la tool DIRECTAMENTE, sin modelo, en los 3 escenarios obligatorios. Es la
pieza que sostiene la regla del piso (ver assignment-a1.md): separa la calidad de
la tool de la varianza del modelo.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-03-tools-api-externa/solucion/telecomunicaciones/prueba_tool.py

Escenarios 1 y 2 funcionan con DATA_SOURCE=csv (por defecto) o DATA_SOURCE=api.
El escenario 3 necesita DATA_SOURCE=api y el simulador desplegado y respondiendo:
si no lo tienes disponible, el script lo dice explícitamente en vez de fallar
de forma confusa.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from comun import settings as cfg  # noqa: E402

from external_api import get_customer_plan  # noqa: E402

# Identificador real de recursos/datasets/telecomunicaciones/clientes.csv.
LINEA_REAL = "988837195"
LINEA_INEXISTENTE = "900000000"


def escenario_1_exito() -> None:
    print("  Escenario 1 · ÉXITO")
    print("  " + "-" * 68)
    resultado = get_customer_plan.invoke({"numero_linea": LINEA_REAL})
    print(f"  Entrada: numero_linea={LINEA_REAL}")
    print(f"  Salida:  {resultado}")
    assert "No existe" not in resultado, "Se esperaba un plan real, no un mensaje de 'no existe'"
    print("  ✔ El agente citaría este dato real, sin inventar nada.\n")


def escenario_2_dato_inexistente() -> None:
    print("  Escenario 2 · DATO INEXISTENTE")
    print("  " + "-" * 68)
    resultado = get_customer_plan.invoke({"numero_linea": LINEA_INEXISTENTE})
    print(f"  Entrada: numero_linea={LINEA_INEXISTENTE}")
    print(f"  Salida:  {resultado}")
    assert "No existe" in resultado, "La tool debería decir explícitamente que no existe"
    print("  ✔ La tool dice 'no existe' — el agente no tiene margen para inventar un plan.\n")


def escenario_3_servicio_caido() -> None:
    print("  Escenario 3 · SERVICIO CAÍDO (?_fallo=error503)")
    print("  " + "-" * 68)
    if cfg.DATA_SOURCE != "api":
        print("  ⚠ DATA_SOURCE no es 'api': este escenario necesita el simulador real.")
        print("    Pon DATA_SOURCE=api en tu .env y vuelve a correr este script.")
        print("    (comun/api_client.py ya traduce cualquier 5xx a un mensaje para el modelo:")
        print("     'El simulador devolvió 503... Informa al usuario y sugiere reintentar más tarde.')\n")
        return

    # Import tardío y de lo "privado" de api_client a propósito: buscar_uno() no
    # tiene forma de colar un ?_fallo= en la URL, y ese parámetro es justamente el
    # mecanismo de prueba que documenta simulador-industria/docs/GUIA-ALUMNO.md.
    from comun.api_client import RUTAS, SimuladorNoDisponible, _pedir  # noqa: PLC0415

    plantilla = RUTAS[("telecomunicaciones", "clientes.csv", "numero_linea")]
    ruta_con_fallo = plantilla.format(valor=LINEA_REAL) + "?_fallo=error503"
    print(f"  GET {ruta_con_fallo}")
    try:
        _pedir(ruta_con_fallo)
    except SimuladorNoDisponible as e:
        print(f"  Salida: {e}")
        print("  ✔ Excepción controlada, con un mensaje que el modelo puede leer y actuar "
              "en consecuencia (avisar al cliente, no reintentar en bucle).\n")
        return
    print("  ⚠ No se lanzó SimuladorNoDisponible — revisa si el simulador está respondiendo.\n")


def main() -> None:
    print("=" * 72)
    print("  PRUEBA_TOOL · telecomunicaciones · get_customer_plan")
    print("=" * 72 + "\n")
    escenario_1_exito()
    escenario_2_dato_inexistente()
    escenario_3_servicio_caido()
    print("Los 3 escenarios corrieron. Pega estas trazas en tu EVIDENCIA-A1.md.")


if __name__ == "__main__":
    main()
