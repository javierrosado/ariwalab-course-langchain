"""Demo 4 · La URL pública con key correcta, sin key y con key mala.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-08-despliegue-hf-spaces/code/04_llamar_desde_fuera.py \\
        --url https://<space-del-docente>.hf.space --key <API_KEY>

Sin --url, corre en modo --simular: una app FastAPI en memoria (fastapi.testclient),
para que la demo funcione en el aula aunque el Space de referencia del docente no esté
desplegado en este momento (tarea 'u' de sesion-08.md — es responsabilidad de Javier
desplegarlo antes de la semana 4; ver nota en ROADMAP.md).

La demo se corre contra el Space del DOCENTE, ya desplegado — el alumno ve el resultado
antes de desplegar el suyo propio en el laboratorio.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from docente.verificar_despliegue import _app_simulada, _llamar_http  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(description="Demo 4 · llamar al Space desde fuera")
    p.add_argument("--url", help="URL pública del Space del docente")
    p.add_argument("--key", help="API key correcta del Space del docente")
    a = p.parse_args()

    print("=" * 72)
    print("  DEMO 4 · llamando al agente desde fuera de la máquina que lo hospeda")
    print("=" * 72)

    if a.url and a.key:
        base = a.url.rstrip("/") + "/chat"

        def llamar(key):
            return _llamar_http(base, "POST", key, {"mensaje": "¿Qué planes tienen disponibles?"})
    else:
        print("\n  (sin --url/--key: modo --simular con una app en memoria)\n")
        from fastapi.testclient import TestClient

        app, key_correcta = _app_simulada()
        cliente = TestClient(app)

        def llamar(key):
            headers = {"X-API-Key": key} if key is not None else {}
            resp = cliente.post("/chat", headers=headers, json={"mensaje": "hola"})
            return resp.status_code, 0.0

        a.key = key_correcta

    casos = [
        ("Con la API key correcta", a.key),
        ("Sin ninguna API key", None),
        ("Con una API key incorrecta", "esta-key-no-es-la-que-toca"),
    ]
    for titulo, key in casos:
        status, segundos = llamar(key)
        resultado = "200 OK — responde" if status == 200 else f"{status} — rechazado"
        print(f"  {titulo.ljust(32)} -> {resultado}  ({segundos:.2f}s)")

    print("""
  Solo el primer caso debería llegar a invocar al modelo. Los otros dos nunca deben
  gastar cuota de HF Inference del equipo: por eso el guardia de X-API-Key va ANTES
  de llamar a responder(), no después.
""")


if __name__ == "__main__":
    main()
