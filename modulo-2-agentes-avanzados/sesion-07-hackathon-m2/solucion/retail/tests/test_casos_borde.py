# -*- coding: utf-8 -*-
"""L7 · Retail — MercaSur · tests/test_casos_borde.py (checkpoint de referencia)

Las 4 familias de caso borde, probadas con INVARIANTES y REPETICIÓN.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-07-hackathon-m2/solucion/retail/tests/test_casos_borde.py

Códigos de salida: 0 = las 4 familias superan su umbral · 1 = al menos una por debajo · 2 = error
"""
from __future__ import annotations

import argparse
import sys
import uuid
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modulo-2-agentes-avanzados" / "sesion-06-automatizacion-guardrails"
                       / "solucion" / "retail"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pydantic import BaseModel, Field  # noqa: E402

from comun import settings as cfg  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida, extraer  # noqa: E402

from agent import responder  # noqa: E402  (checkpoint de referencia de la S6)
from invariantes import dice_no_existe, no_esta_vacia  # noqa: E402

UMBRAL = 0.6


def tasa_exito(mensaje_fn, verificador, n: int) -> tuple[float, list[str]]:
    exitos = 0
    trazas = []
    for _ in range(n):
        thread = f"borde-{uuid.uuid4()}"
        try:
            respuesta = mensaje_fn(thread)
        except Exception as e:  # noqa: BLE001
            trazas.append(f"[error] {type(e).__name__}: {e}")
            continue
        ok = verificador(respuesta)
        trazas.append(f"[{'OK' if ok else 'FALLA'}] {respuesta[:100]}")
        exitos += ok
    return exitos / n, trazas


def familia_1_entrada_ambigua(n: int) -> tuple[float, list[str]]:
    mensaje = "¿Dónde está mi pedido? Y si llegó dañado, quiero devolverlo ya. Pedido MS-2026-00001"
    return tasa_exito(lambda thread: responder(mensaje, thread_id=thread), no_esta_vacia, n)


def familia_2_dato_ausente(n: int) -> tuple[float, list[str]]:
    def escenario(thread: str) -> str:
        responder("Hola, tengo una consulta sobre un pedido", thread_id=thread)
        responder("Es sobre el estado de mi compra", thread_id=thread)
        responder("¿Cuánto demora en llegar normalmente?", thread_id=thread)
        return responder("Mi pedido es MS-2026-99999, ¿dónde está?", thread_id=thread)
    return tasa_exito(escenario, dice_no_existe, n)


def familia_3_servicio_caido(n: int, chaos: bool) -> tuple[float, list[str]]:
    """Mide la regla A4: con la tool fallando siempre,
    el agente agota MAX_ITERATIONS en agent.py y debe devolver un mensaje
    explícito, no colgarse ni propagar una excepción sin capturar.
    """
    if chaos and cfg.DATA_SOURCE == "api":
        mensaje = "¿Dónde está mi pedido MS-2026-00001?"
        return tasa_exito(lambda thread: responder(mensaje, thread_id=thread), no_esta_vacia, n)

    import comun.datos as datos_mod  # noqa: PLC0415

    original = datos_mod.buscar_uno

    def buscar_uno_roto(*args, **kwargs):
        raise datos_mod.FuenteNoDisponible("Simulado para la prueba: el servicio no respondió.")

    datos_mod.buscar_uno = buscar_uno_roto
    try:
        mensaje = "¿Dónde está mi pedido MS-2026-00001?"
        return tasa_exito(lambda thread: responder(mensaje, thread_id=thread), no_esta_vacia, n)
    finally:
        datos_mod.buscar_uno = original


class _EsquemaEstricto(BaseModel):
    class Categoria(str, Enum):
        A = "A"
        B = "B"

    categoria: Categoria = Field(description="Responde EXACTAMENTE 'A' o 'B', nada más")
    numero_exacto: int = Field(description="Un número entero entre 1 y 2, ni más ni menos")


def familia_4_salida_fuera_de_formato(n: int) -> tuple[float, list[str]]:
    modelo = get_chat_model()
    entrada = "Cuéntame sobre el clima de Lima en un párrafo largo, sin categorías."
    exitos = 0
    trazas = []
    for _ in range(n):
        try:
            resultado = extraer(modelo, _EsquemaEstricto, entrada, reintentos=1)
            ok = isinstance(resultado, _EsquemaEstricto)
            trazas.append(f"[OK] objeto válido: {resultado}")
        except ExtraccionFallida as e:
            ok = True
            trazas.append(f"[OK] ExtraccionFallida controlada: {e}")
        except Exception as e:  # noqa: BLE001
            ok = False
            trazas.append(f"[FALLA] excepción no controlada: {type(e).__name__}: {e}")
        exitos += ok
    return exitos / n, trazas


def main() -> int:
    p = argparse.ArgumentParser(description="Pruebas de estrés por invariantes — retail")
    p.add_argument("--repeticiones", type=int, default=5)
    p.add_argument("--chaos", action="store_true")
    a = p.parse_args()

    print("\n" + "=" * 72)
    print("  PRUEBAS DE ESTRÉS POR INVARIANTES · retail")
    print(f"  {describe_provider()}")
    print("=" * 72)

    familias = {
        "1. Entrada ambigua": lambda: familia_1_entrada_ambigua(a.repeticiones),
        "2. Dato ausente": lambda: familia_2_dato_ausente(a.repeticiones),
        "3. Servicio caído": lambda: familia_3_servicio_caido(a.repeticiones, a.chaos),
        "4. Salida fuera de formato": lambda: familia_4_salida_fuera_de_formato(a.repeticiones),
    }

    todas_pasan = True
    for nombre, fn in familias.items():
        print(f"\n{nombre} ({a.repeticiones} repeticiones)")
        print("-" * 68)
        try:
            tasa, trazas = fn()
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR al preparar la familia: {type(e).__name__}: {e}")
            return 2
        for t in trazas:
            print(f"  {t}")
        veredicto = "✔ pasa" if tasa >= UMBRAL else "✘ por debajo del umbral"
        print(f"  Tasa: {tasa:.0%} (umbral {UMBRAL:.0%}) {veredicto}")
        todas_pasan = todas_pasan and tasa >= UMBRAL

    print(f"\n{'=' * 72}")
    if todas_pasan:
        print("  VEREDICTO: las 4 familias superan el umbral.\n")
        return 0
    print("  VEREDICTO: al menos una familia está por debajo del umbral.")
    print("  Documenta el caso en INFORME-L7.md.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
