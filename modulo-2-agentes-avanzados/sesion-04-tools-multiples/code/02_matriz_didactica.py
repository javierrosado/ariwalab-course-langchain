"""Demo 2 · Matriz de selección, versión didáctica: 5 consultas en 30 segundos.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-04-tools-multiples/code/02_matriz_didactica.py

Requiere HF_TOKEN en el .env. Es la versión corta de `docente/matriz_seleccion.py` (20
consultas, matriz completa): aquí hay solo 5, elegidas a propósito para que en un solo
vistazo se vea una de cada cosa — un acierto directo, un confusable y un "sin tool" — antes
de correr el instrumento completo sobre tu propio catálogo en el laboratorio.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

NINGUNA = "(ninguna)"

# 5 de las 30 consultas de recursos/golden/consultas-telecomunicaciones.json, elegidas para
# mostrar un caso de cada tipo: 2 directas, 1 confusable, 2 "otro" (sin tool).
INDICES_DEMO = [0, 3, 12, 16, 20]


def load_reference_tools(track: str):
    ruta = ROOT / "proyecto-final" / track / "app" / "tools" / "domain_tools.py"
    spec = importlib.util.spec_from_file_location(f"tools_{track}", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TOOLS_NUCLEO


def load_demo_queries(track: str) -> list[dict]:
    ruta = ROOT / "recursos" / "golden" / f"consultas-{track}.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    todas = datos["consultas"]
    return [todas[i] for i in INDICES_DEMO]


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · Matriz de selección — versión didáctica (5 consultas)")
    print(f"  {describe_provider()}")
    print("=" * 72)

    tools = load_reference_tools("telecomunicaciones")
    consultas = load_demo_queries("telecomunicaciones")
    model = get_chat_model().bind_tools(tools)
    system_prompt = get_system_prompt("telecomunicaciones")

    print(f"\n  {'Categoría'.ljust(12)}{'Esperada'.ljust(24)}{'Obtenida'.ljust(24)}{'¿Acertó?'}")
    print("  " + "-" * 72)

    aciertos = 0
    for c in consultas:
        try:
            r = model.invoke([("system", system_prompt), ("human", c["consulta"])])
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error al llamar al modelo: {type(e).__name__}: {e}")
            return
        llamadas = getattr(r, "tool_calls", None) or []
        obtenida = llamadas[0]["name"] if llamadas else NINGUNA
        esperada = c["tool_esperada"] or NINGUNA
        acierto = obtenida == esperada
        aciertos += acierto
        print(f"  {c['categoria'].ljust(12)}{esperada.ljust(24)}{obtenida.ljust(24)}"
              f"{'✔' if acierto else '✘'}")

    print(f"\n  Acierto: {aciertos}/{len(consultas)}")
    print("""
  Esto es una muestra de 5, no un veredicto: con tan pocas consultas, un solo fallo cambia
  el porcentaje 20 puntos. Para medir de verdad tu catálogo (con las 30 consultas del
  archivo golden y una matriz de confusión completa), corre en el laboratorio:

      python docente/matriz_seleccion.py --track telecomunicaciones \\
          --tools lab/telecomunicaciones/domain_tools.py
""")


if __name__ == "__main__":
    main()
