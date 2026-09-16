# -*- coding: utf-8 -*-
"""Verificador de las tools de los 4 tracks.

Ejecutar desde la raíz del curso:
    python docente/verificar_tools.py

Comprueba, sin necesidad de credenciales ni de un modelo:
  1. Que toda tool corre con datos existentes y devuelve texto útil.
  2. Que toda tool corre con datos INEXISTENTES sin lanzar excepción,
     devolviendo un mensaje que el agente pueda leer y usar para replantear.
  3. Que toda docstring cumple la regla A2: dice cuándo NO usar la tool.
  4. Que ningún track supera las 4 tools núcleo (regla A1, modelo de 7B).
"""

import csv
import importlib.util
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

TRACKS = ["telecomunicaciones", "banca", "retail", "seguros"]
ok = True


def cargar(track: str):
    ruta = RAIZ / "proyecto-final" / track / "app" / "tools" / "domain_tools.py"
    spec = importlib.util.spec_from_file_location(f"tools_{track}", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fila(track: str, archivo: str) -> dict:
    with open(RAIZ / "recursos" / "datasets" / track / archivo, encoding="utf-8") as f:
        return next(csv.DictReader(f))


def check(label, cond, extra=""):
    global ok
    print(f"    [{'OK  ' if cond else 'FALLA'}] {label}{(' — ' + extra) if extra else ''}")
    ok &= bool(cond)


# Casos de prueba: (nombre_tool, argumentos_validos, argumentos_invalidos)
def casos(track: str) -> list[tuple]:
    if track == "telecomunicaciones":
        ln = fila(track, "clientes.csv")["numero_linea"]
        return [
            ("get_customer_plan", {"numero_linea": ln}, {"numero_linea": "999999999"}),
            ("get_data_usage", {"numero_linea": ln, "periodo": "2026-08"}, {"numero_linea": ln, "periodo": "1999-01"}),
            ("run_line_diagnostics", {"numero_linea": ln}, {"numero_linea": "999999999"}),
            ("create_complaint_ticket", {"numero_linea": ln, "tipo": "AVERIA", "descripcion": "Sin señal"},
                                        {"numero_linea": ln, "tipo": "INVENTADO", "descripcion": "x"}),
            ("check_portability_eligibility", {"numero_linea": ln}, {"numero_linea": "999999999"}),
            ("get_coverage_by_district", {"distrito": "Miraflores"}, {"distrito": "Atlantida"}),
        ]
    if track == "banca":
        cta = fila(track, "cuentas.csv")["numero_cuenta"]
        mov = fila(track, "movimientos.csv")["movimiento_id"]
        tar = fila(track, "tarjetas.csv")["tarjeta_id"]
        return [
            ("get_account_balance", {"numero_cuenta": cta}, {"numero_cuenta": "191-0000000-0-00"}),
            ("list_transactions", {"numero_cuenta": cta, "dias": 90}, {"numero_cuenta": "191-0000000-0-00", "dias": 30}),
            ("get_card_info", {"numero_cuenta": cta}, {"numero_cuenta": "191-0000000-0-00"}),
            ("score_transaction_risk", {"movimiento_id": mov}, {"movimiento_id": "MOV-9999999"}),
            ("get_transfer_limits", {"numero_cuenta": cta}, {"numero_cuenta": "191-0000000-0-00"}),
            ("request_card_block", {"tarjeta_id": tar, "confirmado_por_cliente": False}, {"tarjeta_id": "TC-99999"}),
        ]
    if track == "retail":
        ped = fila(track, "pedidos.csv")["pedido_id"]
        sku = fila(track, "catalogo_productos.csv")["sku"]
        return [
            ("track_order", {"pedido_id": ped}, {"pedido_id": "MS-2026-99999"}),
            ("get_product_details", {"sku": sku}, {"sku": "MS-0000"}),
            ("check_stock_by_store", {"sku": sku}, {"sku": "MS-0000"}),
            ("start_return_request", {"pedido_id": ped, "motivo": "Llegó dañado", "tipo_solucion": "CAMBIO"},
                                     {"pedido_id": "MS-2026-99999", "motivo": "x", "tipo_solucion": "CAMBIO"}),
            ("estimate_delivery", {"distrito": "Los Olivos", "monto_compra": 200.0},
                                  {"distrito": "Atlantida", "monto_compra": 10.0}),
            ("get_return_status", {"pedido_id": ped}, {"pedido_id": "MS-2026-99999"}),
        ]
    placa = fila(track, "polizas.csv")["placa"]
    sin_id = fila(track, "siniestros.csv")["siniestro_id"]
    return [
        ("get_policy_by_plate", {"placa": placa}, {"placa": "ZZZ-999"}),
        ("quote_soat", {"placa": placa}, {"placa": "ZZZ-999"}),
        ("get_claim_status", {"siniestro_id": sin_id}, {"siniestro_id": "SIN-2026-99999"}),
        ("open_claim", {"placa": placa, "tipo": "CHOQUE_SIMPLE", "distrito": "Ate", "cantidad_lesionados": 0},
                       {"placa": "ZZZ-999", "tipo": "CHOQUE_SIMPLE", "distrito": "Ate", "cantidad_lesionados": 0}),
        ("list_affiliated_clinics", {"distrito": "Ate"}, {"distrito": "Atlantida"}),
        ("get_vehicle_info", {"placa": placa}, {"placa": "ZZZ-999"}),
    ]


print("\n" + "=" * 70)
print("  VERIFICADOR DE TOOLS — 4 tracks × 6 tools")
print("=" * 70)

total_tools = 0
for track in TRACKS:
    print(f"\n  ── {track}")
    mod = cargar(track)
    check("máximo 4 tools núcleo (regla A1)", len(mod.TOOLS_NUCLEO) <= 4,
          f"{len(mod.TOOLS_NUCLEO)} núcleo + {len(mod.TOOLS_OPCIONALES)} opcionales")

    for nombre, args_ok, args_malos in casos(track):
        total_tools += 1
        t = getattr(mod, nombre)

        # A2: la docstring debe decir cuándo NO usar la tool
        doc = (t.description or "")
        check(f"{nombre}: docstring cumple A2 (dice 'NO la uses')", "NO la uses" in doc or "NO uses" in doc)

        # Camino feliz
        try:
            r = t.invoke(args_ok)
            check(f"{nombre}: caso válido devuelve texto", isinstance(r, str) and len(r) > 20,
                  r.split("\n")[0][:70])
        except Exception as e:
            check(f"{nombre}: caso válido devuelve texto", False, f"EXCEPCIÓN {type(e).__name__}: {e}")

        # Camino de error: no debe lanzar excepción
        try:
            r = t.invoke(args_malos)
            util = isinstance(r, str) and len(r) > 20
            check(f"{nombre}: caso inválido no lanza excepción", util, r.split("\n")[0][:70])
        except Exception as e:
            check(f"{nombre}: caso inválido no lanza excepción", False, f"EXCEPCIÓN {type(e).__name__}: {e}")

print("\n" + "-" * 70)
print(f"  {total_tools} tools verificadas en {len(TRACKS)} tracks")
print("  " + ("TODAS LAS VERIFICACIONES PASARON" if ok else "HAY FALLAS — revisar arriba"))
print("-" * 70 + "\n")
sys.exit(0 if ok else 1)
