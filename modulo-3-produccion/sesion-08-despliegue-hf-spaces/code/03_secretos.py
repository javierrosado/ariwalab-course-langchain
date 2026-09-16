"""Demo 3 · El mismo código leyendo un secreto de `.env` y de una variable del Space.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-08-despliegue-hf-spaces/code/03_secretos.py

No requiere credenciales de modelo. Muestra que `comun.settings` no distingue de dónde
viene la variable de entorno: `os.environ` es idéntico si la puso `python-dotenv` leyendo
tu `.env` local o si la inyectó la plataforma como *Space secret* — es exactamente el punto
del bloque 1 (12-Factor): mismo código, entorno distinto, cero cambios de código.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))


def leer_como_si_fuera_local() -> str:
    """Simula el .env local: python-dotenv ya cargó AGENT_API_KEY en os.environ."""
    from comun import settings as cfg
    return cfg.AGENT_API_KEY


def leer_como_si_fuera_el_space() -> str:
    """Simula un Space secret: la plataforma inyecta la variable directamente en el
    entorno del proceso, sin ningún archivo .env presente. Se fuerza aquí borrando
    cualquier rastro de dotenv para la demo.
    """
    os.environ["AGENT_API_KEY"] = "clave-inyectada-por-la-plataforma"
    # Re-importar comun.settings leería el .env de nuevo si existiera; en el Space real
    # no hay .env en absoluto, así que os.getenv ya basta para demostrar el punto.
    return os.getenv("AGENT_API_KEY", "")


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · el mismo código, dos orígenes de la misma variable")
    print("=" * 72)

    os.environ.setdefault("AGENT_API_KEY", "clave-de-tu-env-local")
    print(f"\n  Leído como si viniera de tu .env local:  {leer_como_si_fuera_local()}")
    print(f"  Leído como si viniera de un Space secret: {leer_como_si_fuera_el_space()}")

    print("""
  El código que lee la variable (comun.settings.AGENT_API_KEY, o un os.getenv directo
  en el Space real) es EL MISMO en ambos casos. Lo único que cambia es quién puso el
  valor en el entorno del proceso: tú con `.env` + python-dotenv, o la plataforma con
  sus *Space secrets*. Por eso nunca hace falta una rama "if estoy en producción" en
  el código del agente — el principio 12-Factor completo.
""")


if __name__ == "__main__":
    main()
