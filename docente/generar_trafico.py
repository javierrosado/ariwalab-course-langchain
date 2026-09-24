# -*- coding: utf-8 -*-
"""Generador de tráfico — L9 parte 3: 20 consultas reales contra el Space desplegado.

Ejecutar desde la raíz del curso:

    python docente/generar_trafico.py --url https://<equipo>-<track>.hf.space \\
        --key <API_KEY> --track telecomunicaciones
    python docente/generar_trafico.py --simular --track telecomunicaciones   # sin URL real

QUÉ HACE
--------
Envía las 20 consultas "con tool" de `recursos/golden/consultas-<track>.json` contra
`/chat` del Space **ya desplegado** (no contra la laptop: la S9 exige trazas reales,
no de desarrollo) y reporta p50/p95 de latencia — la misma lectura que enseña el
bloque 3 del `README.md` de la sesión ("por qué el promedio miente").

Por qué existe: la parte 3 del laboratorio necesita
volumen para que p50/p95 signifiquen algo. Una sola llamada no tiene percentil.

CUOTA
-----
20 llamadas HTTP reales contra el Space del equipo (gasta cuota de HF Inference del
equipo, no del docente). `--simular` no toca la red.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

TRACKS = ["telecomunicaciones", "banca", "retail", "seguros"]


def cargar_consultas(track: str, n: int) -> list[str]:
    ruta = RAIZ / "recursos" / "golden" / f"consultas-{track}.json"
    if not ruta.exists():
        raise FileNotFoundError(f"No existe {ruta}")
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    con_tool = [c["consulta"] for c in datos["consultas"] if c["tool_esperada"]]
    return con_tool[:n]


def _pedir_http(url: str, api_key: str, mensaje: str, timeout: float = 60.0) -> tuple[int, float]:
    cuerpo = json.dumps({"mensaje": mensaje}).encode("utf-8")
    req = urllib.request.Request(
        url, data=cuerpo, method="POST",
        headers={"Content-Type": "application/json", "X-API-Key": api_key},
    )
    inicio = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            resp.read()
            return resp.status, time.perf_counter() - inicio
    except urllib.error.HTTPError as e:
        e.read()
        return e.code, time.perf_counter() - inicio
    except urllib.error.URLError as e:
        raise ConnectionError(f"No se pudo conectar a {url}: {e.reason}") from e


def _pedir_simulado(cliente, mensaje: str, indice: int) -> tuple[int, float]:
    # Latencia artificial con algo de variación, para que p50/p95 no coincidan y el
    # ejercicio de lectura del bloque 3 tenga sentido incluso sin red real.
    time.sleep(0.01 * (indice % 5))
    inicio = time.perf_counter()
    resp = cliente.post("/chat", headers={"X-API-Key": "clave-de-prueba"},
                        json={"mensaje": mensaje})
    return resp.status_code, time.perf_counter() - inicio


def percentil(valores: list[float], p: float) -> float:
    ordenados = sorted(valores)
    k = (len(ordenados) - 1) * p
    piso, techo = math.floor(k), math.ceil(k)
    if piso == techo:
        return ordenados[int(k)]
    return ordenados[piso] + (ordenados[techo] - ordenados[piso]) * (k - piso)


def generar(track: str, url: str | None, api_key: str | None, simular: bool) -> list[dict]:
    consultas = cargar_consultas(track, 20)
    if not consultas:
        raise ValueError(f"{track}: el golden set no tiene consultas con tool_esperada")

    if simular:
        from docente.verificar_despliegue import _app_simulada
        from fastapi.testclient import TestClient
        app, _ = _app_simulada()
        cliente = TestClient(app)
        pedir = lambda i, m: _pedir_simulado(cliente, m, i)  # noqa: E731
    else:
        if not url or not api_key:
            raise ValueError("Faltan --url y --key (o usa --simular)")
        base = url.rstrip("/") + "/chat"
        pedir = lambda i, m: _pedir_http(base, api_key, m)  # noqa: E731

    filas = []
    for i, consulta in enumerate(consultas):
        try:
            status, segundos = pedir(i, consulta)
            error = "" if status == 200 else f"HTTP {status}"
        except Exception as e:  # noqa: BLE001
            status, segundos, error = 0, 0.0, f"{type(e).__name__}: {e}"[:120]
        filas.append({"consulta": consulta, "status": status, "segundos": segundos, "error": error})
        print(f"  [{i + 1:2d}/20] {segundos:6.2f}s  status={status}  {consulta[:50]}")

    return filas


def main() -> int:
    p = argparse.ArgumentParser(description="Generador de tráfico para el L9 (Langfuse)")
    p.add_argument("--track", choices=TRACKS, required=True)
    p.add_argument("--url", help="URL pública del Space, ej. https://equipo-track.hf.space")
    p.add_argument("--key", help="API key del equipo (AGENT_API_KEY)")
    p.add_argument("--simular", action="store_true",
                   help="prueba el arnés contra una app en memoria, sin URL real")
    a = p.parse_args()

    print("\n" + "=" * 72)
    print(f"  GENERADOR DE TRAFICO - L9 - {a.track}")
    print("=" * 72)
    print(f"  Objetivo: {'app simulada en memoria' if a.simular else a.url}\n")

    try:
        filas = generar(a.track, a.url, a.key, a.simular)
    except (FileNotFoundError, ValueError, ConnectionError) as e:
        print(f"\n  ERROR: {e}\n")
        return 2

    exitosas = [f["segundos"] for f in filas if not f["error"]]
    errores = [f for f in filas if f["error"]]

    print(f"\n  {len(exitosas)}/{len(filas)} peticiones exitosas")
    if exitosas:
        promedio = sum(exitosas) / len(exitosas)
        print(f"  promedio = {promedio:.2f}s   p50 = {percentil(exitosas, 0.50):.2f}s   "
              f"p95 = {percentil(exitosas, 0.95):.2f}s")
        print("\n  Recuerda leer p50/p95, no el promedio (bloque 3 del README de la S9):")
        print("  el promedio se distorsiona con un solo cold start; los percentiles no.")
    if errores:
        print(f"\n  {len(errores)} peticion(es) con error:")
        for f in errores:
            print(f"  · {f['consulta'][:50]}: {f['error']}")

    if not exitosas:
        print("\n  VEREDICTO: ninguna peticion tuvo exito. Revisa la URL y la API key.\n")
        return 1

    print("\n  Trafico generado. Abre el dashboard de Langfuse para leer las trazas.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
