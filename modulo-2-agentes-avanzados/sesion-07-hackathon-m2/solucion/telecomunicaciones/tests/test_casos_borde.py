# -*- coding: utf-8 -*-
"""L7 · Telecomunicaciones — AndesMóvil · tests/test_casos_borde.py (checkpoint de referencia)

Las 4 familias de caso borde (ver README.md de la sesión, bloque 0), probadas con
INVARIANTES y REPETICIÓN — nunca con `assert respuesta == esperado`.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-07-hackathon-m2/solucion/telecomunicaciones/tests/test_casos_borde.py
    python .../test_casos_borde.py --repeticiones 3     # prueba barata
    python .../test_casos_borde.py --chaos               # fuerza fallos del simulador (DATA_SOURCE=api)

QUÉ MIDE CADA FAMILIA
----------------------
1. Entrada ambigua       — el agente no se cae con dos intenciones en un turno.
2. Dato ausente          — no inventa un dato en el turno 4 de una conversación.
3. Servicio caído        — no entra en bucle ante un fallo de la tool.
4. Salida fuera de formato — comun/structured.py nunca deja pasar un objeto inválido.

CÓDIGOS DE SALIDA
------------------
0 = las 4 familias superan su umbral · 1 = al menos una por debajo · 2 = error de configuración
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
                       / "solucion" / "telecomunicaciones"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pydantic import BaseModel, Field  # noqa: E402

from comun import settings as cfg  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida, extraer  # noqa: E402

from agent import responder  # noqa: E402  (checkpoint de referencia de la S6)
from invariantes import dice_no_existe, no_esta_vacia  # noqa: E402

UMBRAL = 0.6  # con pocas repeticiones, exigir 100 % mide temperatura del modelo, no diseño


def tasa_exito(mensaje_fn, verificador, n: int) -> tuple[float, list[str]]:
    """Corre `mensaje_fn()` n veces (cada una en una conversación aislada) y mide
    qué fracción de las respuestas cumple `verificador`."""
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
    """Dos intenciones en un turno: el agente debe responder algo con contenido,
    no quedarse en blanco ni reventar."""
    mensaje = ("Quiero saber cuánto he consumido de datos y también reportar que se "
               "me corta la llamada, mi línea es 988837195")
    return tasa_exito(lambda thread: responder(mensaje, thread_id=thread), no_esta_vacia, n)


def familia_2_dato_ausente(n: int) -> tuple[float, list[str]]:
    """Un identificador que no existe, en el turno 4 de una conversación."""
    def escenario(thread: str) -> str:
        responder("Hola, tengo una consulta", thread_id=thread)
        responder("Es sobre mi línea", thread_id=thread)
        responder("¿Está activa?", thread_id=thread)
        return responder("Mi número es 900000000, ¿qué plan tengo?", thread_id=thread)
    return tasa_exito(escenario, dice_no_existe, n)


def familia_3_servicio_caido(n: int, chaos: bool) -> tuple[float, list[str]]:
    """El agente no debe entrar en bucle ni caerse si la tool subyacente falla.

    Aquí es donde se MIDE la regla A4 (VALIDACION-INTEGRAL H2: hasta ahora se
    enseñaba y nunca se comprobaba). El parche de abajo hace que la tool falle
    SIEMPRE, no una vez — así el agente agota su tope de iteraciones
    (MAX_ITERATIONS en agent.py) en cada intento. `responder()` es una función
    síncrona con un `for _ in range(MAX_ITERATIONS)`: por construcción, no puede
    colgarse. Lo que este test verifica es lo otro: que al agotar el tope,
    devuelve un mensaje explícito al usuario (no_esta_vacia) en vez de fallar
    en silencio o propagar una excepción sin capturar.

    Con DATA_SOURCE=api y --chaos, se prueba contra el simulador real con
    ?_fallo=error503 (ver GUIA-ALUMNO.md). Sin eso, se simula el fallo
    parcheando temporalmente comun.datos.buscar_uno para que lance una excepción
    — la misma clase de fallo, sin depender de que el simulador esté desplegado.
    """
    if chaos and cfg.DATA_SOURCE == "api":
        mensaje = "¿Qué plan tengo? Mi línea es 988837195"  # el _fallo lo agrega el docente al correr el simulador con CHAOS_RATE
        return tasa_exito(lambda thread: responder(mensaje, thread_id=thread), no_esta_vacia, n)

    import comun.datos as datos_mod  # noqa: PLC0415

    original = datos_mod.buscar_uno

    def buscar_uno_roto(*args, **kwargs):
        raise datos_mod.FuenteNoDisponible("Simulado para la prueba: el servicio no respondió.")

    datos_mod.buscar_uno = buscar_uno_roto
    try:
        mensaje = "¿Qué plan tengo? Mi línea es 988837195"
        return tasa_exito(lambda thread: responder(mensaje, thread_id=thread), no_esta_vacia, n)
    finally:
        datos_mod.buscar_uno = original


class _EsquemaEstricto(BaseModel):
    """Esquema deliberadamente exigente, para forzar el camino de reintento/fallo."""

    class Categoria(str, Enum):
        A = "A"
        B = "B"

    categoria: Categoria = Field(description="Responde EXACTAMENTE 'A' o 'B', nada más")
    numero_exacto: int = Field(description="Un número entero entre 1 y 2, ni más ni menos")


def familia_4_salida_fuera_de_formato(n: int) -> tuple[float, list[str]]:
    """comun/structured.py nunca debe dejar pasar un objeto inválido: o produce un
    objeto válido, o falla con ExtraccionFallida. Cualquier otra cosa (un None
    que revienta después, una excepción sin capturar) es lo que se prueba aquí.
    """
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
            ok = True  # el invariante es "nunca un fallo silencioso", y esto es un fallo CONTROLADO
            trazas.append(f"[OK] ExtraccionFallida controlada: {e}")
        except Exception as e:  # noqa: BLE001
            ok = False  # esto sí sería un fallo silencioso: no debería pasar
            trazas.append(f"[FALLA] excepción no controlada: {type(e).__name__}: {e}")
        exitos += ok
    return exitos / n, trazas


def main() -> int:
    p = argparse.ArgumentParser(description="Pruebas de estrés por invariantes — telecomunicaciones")
    p.add_argument("--repeticiones", type=int, default=5, help="repeticiones por familia (por defecto 5)")
    p.add_argument("--chaos", action="store_true",
                   help="para la familia 3, usa el simulador real en vez de simular el fallo localmente")
    a = p.parse_args()

    print("\n" + "=" * 72)
    print("  PRUEBAS DE ESTRÉS POR INVARIANTES · telecomunicaciones")
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
    print("  Documenta el caso en INFORME-L7.md — un caso que falla es evidencia, no un error tuyo.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
