# -*- coding: utf-8 -*-
"""Matriz de selección de herramientas — la regla A1 convertida en un número.

Ejecutar desde la raíz del curso:

    python docente/matriz_seleccion.py --simular            # sin credenciales, gratis
    python docente/matriz_seleccion.py --track banca        # un track, 30 llamadas
    python docente/matriz_seleccion.py                      # los 4 tracks, 120 llamadas

    # Laboratorio 4: medir el catálogo del ALUMNO, no la referencia del docente
    python docente/matriz_seleccion.py --track banca --tools lab/banca/domain_tools.py

QUÉ MIDE
--------
Que el modelo **elija** la herramienta correcta. No que la ejecute: cada consulta es una
sola llamada al modelo con las 4 tools núcleo enlazadas, y se compara el `tool_call` que
propuso contra el esperado. Aislar la selección es deliberado — si el laboratorio 4 falla,
esto dice si el problema está en la elección o en la ejecución.

POR QUÉ IMPORTA
---------------
El curso usa un modelo genérico sin afinar (D21). Lo único que guía su elección son las
docstrings de las tools (regla A2). Y como la fiabilidad se compone —93 % por llamada es
80 % en una tarea de tres pasos— un 70 % de acierto en la selección hace que el
laboratorio 4 no funcione, sin ningún error visible en el código.

LO QUE HAY QUE MIRAR NO ES EL PORCENTAJE, ES LA MATRIZ
------------------------------------------------------
"El modelo elige mal" no es accionable. "get_data_usage se elige 4 veces cuando se
esperaba get_customer_plan" sí lo es: hay que separar esas dos docstrings diciendo en cada
una cuándo NO usarla. La matriz de confusión es la salida útil de este script.

CUOTA
-----
Cada track cuesta 30 llamadas al modelo (ver recursos/golden/consultas-<track>.json). Usa
`--muestra 6` para una prueba barata y `--simular` para probar el arnés sin gastar nada.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import pathlib
import sys
from collections import Counter, defaultdict

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

NINGUNA = "(ninguna)"
UMBRAL_POR_DEFECTO = 85.0

TRACKS = {
    "telecomunicaciones": "AndesMóvil",
    "banca": "Banco Inti",
    "retail": "MercaSur",
    "seguros": "Andina Seguros",
}

# ─────────────────────────────────────────────────────────────────────────────
# El banco de consultas vive en recursos/golden/consultas-<track>.json — es la MISMA
# fuente que usan el L2 (clasificación de intención) y el L5 (categoría "otro" = las
# preguntas que debe responder el RAG). No lo dupliques aquí: si hace falta ajustar una
# consulta, se ajusta en el JSON y este script la recoge automáticamente.
#
# Categorías del JSON, heredadas del diseño original de este script:
#   directa      — una intención clara por cada tool núcleo
#   confusable   — redactada a propósito cerca del límite entre dos tools
#   otro         — tarifas, coberturas, políticas y saludos: el modelo NO debe
#                  llamar a nada (van a RAG en la sesión 5, o son conversación)
#
# Las "otro" son las más valiosas para esta matriz: la regla A2 exige que cada
# docstring diga "cuándo NO usarla", y esto comprueba si esa frase está funcionando.
# ─────────────────────────────────────────────────────────────────────────────
import json  # noqa: E402


def cargar_consultas(track: str) -> list[tuple[str, str]]:
    """Lee recursos/golden/consultas-<track>.json y lo aplana a (consulta, tool_esperada).

    Desde la Sesión 2, cada entrada tiene DOS campos que no hay que confundir:
    `intencion` es la categoría de la taxonomía del L2 (CONSULTA_PLAN, AVERIA, ...),
    y `tool_esperada` es el nombre de la tool que esa categoría dispara (o None si es
    OTRO). Esta matriz mide selección de TOOLS, así que lee `tool_esperada`.
    """
    ruta = RAIZ / "recursos" / "golden" / f"consultas-{track}.json"
    if not ruta.exists():
        raise FileNotFoundError(
            f"No existe {ruta}. El banco de consultas de este script vive ahí, "
            f"no en este archivo.")
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    return [(c["consulta"], c["tool_esperada"] or NINGUNA) for c in datos["consultas"]]




# ─────────────────────────────────────────────────────────────────────────────
# Carga de las tools reales
# ─────────────────────────────────────────────────────────────────────────────
def cargar_tools(track: str, ruta_tools: str | None = None):
    """Carga TOOLS_NUCLEO desde `ruta_tools`, o de la referencia del docente si no se pasa.

    `ruta_tools` es lo que el Laboratorio 4 necesita: el alumno mide SU catálogo
    (`lab/<track>/domain_tools.py`), no `proyecto-final/`, que es la implementación
    de referencia del docente, no el repositorio del alumno (ver README.md, sección
    "proyecto-final/: qué es y qué no es").
    """
    ruta = pathlib.Path(ruta_tools) if ruta_tools else (
        RAIZ / "proyecto-final" / track / "app" / "tools" / "domain_tools.py")
    if not ruta.exists():
        raise FileNotFoundError(f"No existe {ruta}")
    spec = importlib.util.spec_from_file_location(f"tools_{track}", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "TOOLS_NUCLEO"):
        raise ValueError(f"{ruta} no define TOOLS_NUCLEO (lista de las 4 tools núcleo)")
    return list(mod.TOOLS_NUCLEO)


# ─────────────────────────────────────────────────────────────────────────────
# Modelo simulado — para probar el arnés sin credenciales ni cuota
# ─────────────────────────────────────────────────────────────────────────────
class _ToolsEnlazadas:
    def __init__(self, padre, nombres):
        self.padre = padre
        self.nombres = nombres

    def invoke(self, mensajes):
        consulta = mensajes[-1][1] if isinstance(mensajes[-1], tuple) else mensajes[-1].content
        esperada = self.padre.respuestas.get(consulta, NINGUNA)
        self.padre.n += 1
        # Inyecta fallos deterministas para que la matriz muestre confusiones reales
        # y el arnés demuestre que sabe detectarlas.
        if self.padre.n in self.padre.posiciones_fallo and esperada != NINGUNA:
            otras = [n for n in self.nombres if n != esperada]
            devuelta = otras[self.padre.n % len(otras)] if otras else NINGUNA
        else:
            devuelta = esperada
        return _Respuesta([] if devuelta == NINGUNA else [{"name": devuelta, "args": {}, "id": "sim"}])


class _Respuesta:
    def __init__(self, tool_calls):
        self.tool_calls = tool_calls
        self.content = ""


class ModeloSimulado:
    """Devuelve siempre la tool esperada, salvo en N posiciones fijas por track."""

    def __init__(self, consultas, fallos: int):
        self.respuestas = {c: e for c, e in consultas}
        self.n = 0
        # Posiciones repartidas, no las primeras: así los fallos caen en confusables.
        paso = max(1, len(consultas) // max(1, fallos))
        self.posiciones_fallo = {min(len(consultas), 3 + i * paso) for i in range(fallos)}

    def bind_tools(self, tools):
        return _ToolsEnlazadas(self, [t.name for t in tools])


# ─────────────────────────────────────────────────────────────────────────────
# Ejecución
# ─────────────────────────────────────────────────────────────────────────────
def validar_banco(track: str, consultas: list[tuple[str, str]], nombres: list[str]) -> None:
    """El banco de consultas se desactualiza si alguien renombra una tool.

    Sin esto, un nombre mal escrito produciría una fila con 0 % y el profesor
    culparía al modelo de un error de tipeo. Falla ruidosamente en su lugar.
    """
    esperadas = {e for _, e in consultas} - {NINGUNA}
    huerfanas = sorted(esperadas - set(nombres))
    if huerfanas:
        raise ValueError(
            f"[{track}] el banco de consultas espera tools que ya no existen: "
            f"{', '.join(huerfanas)}. Tools núcleo actuales: {', '.join(nombres)}. "
            f"Actualiza recursos/golden/consultas-{track}.json.")
    sin_probar = sorted(set(nombres) - esperadas)
    if sin_probar:
        print(f"  AVISO: sin consultas de prueba para {', '.join(sin_probar)}")


def evaluar_track(track: str, simular: bool, fallos: int, muestra: int | None,
                  ruta_tools: str | None = None):
    tools = cargar_tools(track, ruta_tools)
    consultas = cargar_consultas(track)
    validar_banco(track, consultas, [t.name for t in tools])
    if muestra:
        consultas = consultas[:muestra]

    if simular:
        modelo = ModeloSimulado(consultas, fallos)
        sistema = f"[simulado] {track}"
    else:
        from comun.prompts_industria import get_system_prompt
        from comun.provider import get_chat_model

        modelo = get_chat_model()
        sistema = get_system_prompt(track)

    enlazado = modelo.bind_tools(tools)

    filas = []
    for consulta, esperada in consultas:
        try:
            r = enlazado.invoke([("system", sistema), ("human", consulta)])
            llamadas = getattr(r, "tool_calls", None) or []
            obtenida = llamadas[0]["name"] if llamadas else NINGUNA
            n_llamadas = len(llamadas)
            error = ""
        except Exception as e:  # noqa: BLE001
            obtenida, n_llamadas, error = "(error)", 0, f"{type(e).__name__}: {e}"[:120]
        filas.append({
            "track": track,
            "consulta": consulta,
            "esperada": esperada,
            "obtenida": obtenida,
            "acierto": obtenida == esperada,
            "tool_calls": n_llamadas,
            "error": error,
        })
    return [t.name for t in tools], filas


# ─────────────────────────────────────────────────────────────────────────────
# Reporte
# ─────────────────────────────────────────────────────────────────────────────
def imprimir_matriz(nombres_tools: list[str], filas: list[dict]):
    """Filas = tool esperada, columnas = tool elegida. La diagonal son los aciertos.

    Las columnas van numeradas porque los nombres de las tools no caben; el número
    de cada columna es el mismo que el de su fila, así la diagonal se lee de un vistazo.
    """
    etiquetas = nombres_tools + [NINGUNA]
    extras = sorted({f["obtenida"] for f in filas} - set(etiquetas))
    columnas = etiquetas + extras
    conteo: dict[tuple[str, str], int] = Counter((f["esperada"], f["obtenida"]) for f in filas)

    w0 = max(len(e) for e in etiquetas) + 6
    encabezados = [f"[{i}]" for i in range(1, len(columnas) + 1)]

    print("\n  " + "esperada / elegida".ljust(w0)
          + "".join(h.rjust(6) for h in encabezados) + "    total     %")
    print("  " + "─" * (w0 + 6 * len(columnas) + 14))
    for i, esp in enumerate(etiquetas, start=1):
        total = sum(conteo[(esp, o)] for o in columnas)
        if total == 0:
            continue
        ok = conteo[(esp, esp)]
        celdas = "".join(("·" if conteo[(esp, o)] == 0 else str(conteo[(esp, o)])).rjust(6)
                         for o in columnas)
        etiqueta = f"[{i}] {esp}"
        print(f"  {etiqueta.ljust(w0)}{celdas}{str(total).rjust(9)}{100 * ok / total:6.0f}")
    if extras:
        legenda = "  ".join(f"[{len(etiquetas) + j}] {n}" for j, n in enumerate(extras, start=1))
        print(f"\n  Columnas extra: {legenda}")


def diagnostico(filas: list[dict]) -> list[str]:
    """Convierte los errores en instrucciones accionables sobre docstrings."""
    pares = Counter((f["esperada"], f["obtenida"]) for f in filas if not f["acierto"])
    lineas = []
    for (esp, obt), n in pares.most_common(5):
        if obt == "(error)":
            lineas.append(f"  · {n}× fallo de infraestructura al consultar (revisa el token y la cuota)")
        elif esp == NINGUNA:
            lineas.append(
                f"  · {n}× llamó a `{obt}` cuando no debía llamar a nada → "
                f"añade a su docstring **cuándo NO usarla** (regla A2): tarifas, coberturas "
                f"y políticas se responden con RAG, no con esta tool")
        elif obt == NINGUNA:
            lineas.append(
                f"  · {n}× no llamó a ninguna tool cuando esperábamos `{esp}` → "
                f"su docstring no describe bien el caso de uso; empieza con un verbo y "
                f"nombra el dato que devuelve")
        else:
            lineas.append(
                f"  · {n}× eligió `{obt}` donde esperábamos `{esp}` → "
                f"esas dos docstrings se solapan: escribe en `{obt}` que NO sirve para "
                f"este caso y en `{esp}` la señal que la distingue")
    return lineas


def main() -> int:
    p = argparse.ArgumentParser(description="Matriz de selección de herramientas por track")
    p.add_argument("--track", choices=list(TRACKS), action="append",
                   help="track a evaluar (repetible). Por defecto, los cuatro")
    p.add_argument("--simular", action="store_true",
                   help="usa un modelo simulado: sin credenciales, sin cuota, resultado determinista")
    p.add_argument("--fallos", type=int, default=2,
                   help="con --simular, cuántos errores inyectar por track (por defecto 2)")
    p.add_argument("--muestra", type=int, default=None,
                   help="evalúa solo las primeras N consultas de cada track (prueba barata)")
    p.add_argument("--umbral", type=float, default=UMBRAL_POR_DEFECTO,
                   help=f"%% mínimo de acierto exigido por track (por defecto {UMBRAL_POR_DEFECTO:.0f})")
    p.add_argument("--csv", metavar="RUTA", help="vuelca el detalle consulta a consulta en un CSV")
    p.add_argument("--verbose", action="store_true", help="imprime cada consulta y su resultado")
    p.add_argument("--tools", metavar="RUTA",
                   help="ruta a un domain_tools.py propio (Laboratorio 4: mide TU catálogo, "
                        "no la referencia del docente). Exige un único --track")
    a = p.parse_args()

    tracks = a.track or list(TRACKS)

    if a.tools and len(tracks) != 1:
        print("\n  ERROR: --tools exige un único --track (no tiene sentido medir un archivo")
        print("  de tools contra los 4 tracks a la vez).\n")
        return 2

    n_llamadas = sum(len(cargar_consultas(t)[: a.muestra] if a.muestra else cargar_consultas(t))
                     for t in tracks)

    print("\n" + "=" * 78)
    print("  MATRIZ DE SELECCIÓN DE HERRAMIENTAS")
    print("=" * 78)
    if a.simular:
        print(f"  Modo SIMULADO — {a.fallos} error(es) inyectado(s) por track, sin llamadas reales")
    else:
        try:
            from comun.provider import describe_provider

            print(f"  {describe_provider()}")
        except Exception as e:  # noqa: BLE001
            print(f"\n  ERROR: no se pudo preparar el modelo — {type(e).__name__}: {e}")
            print("  Revisa el .env y la instalación (pip install -r requirements.txt).")
            print("  Para probar el arnés sin credenciales: --simular")
            return 2
        print(f"  {n_llamadas} llamadas al modelo · umbral {a.umbral:.0f} % por track")

    todas: list[dict] = []
    veredictos = {}

    for track in tracks:
        print(f"\n{'─' * 78}\nTRACK {track.upper()} — {TRACKS[track]}")
        if a.tools:
            print(f"  Catálogo evaluado: {a.tools} (no la referencia del docente)")
        try:
            nombres, filas = evaluar_track(track, a.simular, a.fallos, a.muestra, a.tools)
        except (FileNotFoundError, ValueError) as e:
            print(f"  ERROR: {e}")
            return 2
        except Exception as e:  # noqa: BLE001 — credenciales, red o dependencias
            print(f"  ERROR al preparar el track: {type(e).__name__}: {e}")
            print("  Para probar el arnés sin credenciales: --simular")
            return 2
        todas += filas

        if a.verbose:
            for f in filas:
                marca = "OK  " if f["acierto"] else "FALLA"
                print(f"  [{marca}] {f['consulta'][:58]:60} esperada={f['esperada']:24} "
                      f"obtenida={f['obtenida']}")

        aciertos = sum(f["acierto"] for f in filas)
        pct = 100 * aciertos / len(filas)
        veredictos[track] = pct
        imprimir_matriz(nombres, filas)
        print(f"\n  Acierto: {aciertos}/{len(filas)} = {pct:.1f} %  "
              f"{'✔ pasa' if pct >= a.umbral else '✘ POR DEBAJO DEL UMBRAL'}")

        if aciertos < len(filas):
            print("\n  Qué corregir:")
            for l in diagnostico(filas):
                print(l)

    # Recall por tool, útil cuando una sola herramienta arrastra el promedio
    por_tool = defaultdict(lambda: [0, 0])
    for f in todas:
        por_tool[f["esperada"]][1] += 1
        por_tool[f["esperada"]][0] += int(f["acierto"])

    print(f"\n{'═' * 78}\nRESUMEN")
    print(f"\n  {'Track'.ljust(22)}{'Acierto'.rjust(10)}{'Umbral'.rjust(10)}{'  Veredicto'}")
    print("  " + "─" * 56)
    for t, pct in veredictos.items():
        print(f"  {t.ljust(22)}{f'{pct:.1f} %'.rjust(10)}{f'{a.umbral:.0f} %'.rjust(10)}"
              f"{'  ✔ pasa' if pct >= a.umbral else '  ✘ falla'}")

    print(f"\n  {'Herramienta esperada'.ljust(30)}{'Acierto'.rjust(7)}{'%'.rjust(9)}")
    print("  " + "─" * 46)
    for nombre, (ok, tot) in sorted(por_tool.items(), key=lambda kv: (kv[1][0] / kv[1][1], kv[0])):
        print(f"  {nombre.ljust(30)}{f'{ok}/{tot}'.rjust(7)}{f'{100 * ok / tot:.0f} %'.rjust(9)}")

    if a.csv:
        ruta = pathlib.Path(a.csv)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(todas[0].keys()))
            w.writeheader()
            w.writerows(todas)
        print(f"\n  Detalle escrito en {ruta}")

    global_pct = 100 * sum(f["acierto"] for f in todas) / len(todas)
    peor = min(veredictos.values())
    print(f"\n  GLOBAL: {global_pct:.1f} %  ·  peor track: {peor:.1f} %")
    if peor >= a.umbral:
        print("\n  VEREDICTO: la selección de herramientas es suficiente para el laboratorio 4.\n")
        return 0
    print("\n  VEREDICTO: hay al menos un track por debajo del umbral. Corrige las docstrings")
    print("  señaladas arriba y vuelve a ejecutar. No enseñes el laboratorio 4 así.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
