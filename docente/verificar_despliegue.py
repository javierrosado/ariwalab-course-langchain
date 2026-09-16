# -*- coding: utf-8 -*-
"""Verificador de despliegue — L8: /health sin credencial, /chat con y sin key, desde fuera.

Ejecutar desde la raíz del curso:

    python docente/verificar_despliegue.py --url https://<equipo>-<track>.hf.space --key <API_KEY>
    python docente/verificar_despliegue.py --simular              # sin URL real, prueba el arnés

QUÉ MIDE
--------
Los puntos del criterio de aceptación de la S8 (ver `docente/esqueletos/sesion-08.md` §8):

  1. GET  /health   responde 200 SIN credencial.
  2. POST /chat     responde 200 CON la API key correcta.
  3. POST /chat     responde 401 SIN API key.
  4. POST /chat     responde 401 con una API key incorrecta.

De paso mide la latencia del primer request contra la del segundo, para detectar el
*cold start* del tier gratuito que el equipo debe documentar en `DESPLIEGUE.md`.

Por qué existe (tarea v de `sesion-08.md`): calificar 15 despliegues a mano —abrir cada
URL, probar con y sin key— no escala. Esto lo convierte en 4 comprobaciones deterministas.

CUOTA
-----
4 requests HTTP contra el Space real. `--simular` no toca la red: prueba el arnés contra
una app FastAPI en memoria con `TestClient`.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


# ─────────────────────────────────────────────────────────────────────────────
# Transporte: HTTP real o TestClient en memoria, misma firma para ambos
# ─────────────────────────────────────────────────────────────────────────────
def _llamar_http(url: str, metodo: str, api_key: str | None, cuerpo: dict | None,
                  timeout: float = 30.0) -> tuple[int, float]:
    headers = {"Content-Type": "application/json"}
    if api_key is not None:
        headers["X-API-Key"] = api_key
    data = json.dumps(cuerpo).encode("utf-8") if cuerpo is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=metodo)
    inicio = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, time.perf_counter() - inicio
    except urllib.error.HTTPError as e:
        return e.code, time.perf_counter() - inicio
    except urllib.error.URLError as e:
        raise ConnectionError(f"No se pudo conectar a {url}: {e.reason}") from e


def _app_simulada():
    """Contrato idéntico a solucion/<track>/api.py, sin depender de ningún track."""
    from fastapi import FastAPI, Header, HTTPException

    api_key_correcta = "clave-de-prueba"
    app = FastAPI()

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/chat")
    def chat(payload: dict, x_api_key: str = Header(default="")):
        if x_api_key != api_key_correcta:
            raise HTTPException(401, "API key inválida o ausente")
        return {"respuesta": f"eco: {payload.get('mensaje', '')}"}

    return app, api_key_correcta


def _llamar_test_client(cliente, ruta: str, metodo: str, api_key: str | None,
                        cuerpo: dict | None) -> tuple[int, float]:
    headers = {"X-API-Key": api_key} if api_key is not None else {}
    inicio = time.perf_counter()
    resp = cliente.request(metodo, ruta, headers=headers, json=cuerpo)
    return resp.status_code, time.perf_counter() - inicio


# ─────────────────────────────────────────────────────────────────────────────
# Evaluación
# ─────────────────────────────────────────────────────────────────────────────
def evaluar(base_url: str | None, api_key: str | None, simular: bool) -> list[dict]:
    if simular:
        app, api_key = _app_simulada()
        from fastapi.testclient import TestClient
        cliente = TestClient(app)

        def llamar(ruta, metodo="GET", key=None, cuerpo=None):
            return _llamar_test_client(cliente, ruta, metodo, key, cuerpo)
    else:
        if not base_url or not api_key:
            raise ValueError("Faltan --url y --key (o usa --simular para probar el arnés)")
        base = base_url.rstrip("/")

        def llamar(ruta, metodo="GET", key=None, cuerpo=None):
            return _llamar_http(base + ruta, metodo, key, cuerpo)

    checks = []

    status, t_health = llamar("/health")
    checks.append({"check": "GET /health sin credencial", "ok": status == 200,
                   "detalle": f"status={status}, {t_health:.2f}s (posible cold start)"})

    status, t_chat_ok = llamar("/chat", "POST", api_key, {"mensaje": "hola"})
    checks.append({"check": "POST /chat con API key correcta", "ok": status == 200,
                   "detalle": f"status={status}, {t_chat_ok:.2f}s"})

    status, _ = llamar("/chat", "POST", None, {"mensaje": "hola"})
    checks.append({"check": "POST /chat SIN API key -> 401", "ok": status == 401,
                   "detalle": f"status={status}"})

    status, _ = llamar("/chat", "POST", "clave-incorrecta-xyz", {"mensaje": "hola"})
    checks.append({"check": "POST /chat con API key incorrecta -> 401", "ok": status == 401,
                   "detalle": f"status={status}"})

    if t_health > 3 * max(t_chat_ok, 0.01):
        checks.append({
            "check": "cold start detectado (documentar en DESPLIEGUE.md)",
            "ok": True,
            "detalle": f"1er request {t_health:.2f}s vs 2º {t_chat_ok:.2f}s",
        })

    return checks


def main() -> int:
    p = argparse.ArgumentParser(description="Verificador de despliegue del L8 (HF Spaces)")
    p.add_argument("--url", help="URL pública del Space, ej. https://equipo-track.hf.space")
    p.add_argument("--key", help="API key del equipo (AGENT_API_KEY)")
    p.add_argument("--simular", action="store_true",
                   help="prueba el arnés contra una app en memoria, sin URL real")
    a = p.parse_args()

    print("\n" + "=" * 72)
    print("  VERIFICADOR DE DESPLIEGUE - L8")
    print("=" * 72)
    print(f"  Objetivo: {'app simulada en memoria' if a.simular else a.url}")

    try:
        checks = evaluar(a.url, a.key, a.simular)
    except (ValueError, ConnectionError) as e:
        print(f"\n  ERROR: {e}\n")
        return 2

    print()
    for c in checks:
        marca = "OK " if c["ok"] else "X  "
        print(f"  [{marca}] {c['check']}  -  {c['detalle']}")

    fallos = [c for c in checks if not c["ok"]]
    if fallos:
        print(f"\n  VEREDICTO: {len(fallos)} comprobacion(es) fallida(s). Revisa el Dockerfile,")
        print("  los Space secrets y el guardia de X-API-Key en app/api.py.\n")
        return 1

    print("\n  VEREDICTO: despliegue conforme al criterio de aceptacion de la S8.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
