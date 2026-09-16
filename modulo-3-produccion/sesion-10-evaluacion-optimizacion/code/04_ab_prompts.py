"""Demo 4 · El mismo dataset contra dos versiones del prompt, con la tabla de salida.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/04_ab_prompts.py

Requiere HF_TOKEN. Corre las 10 consultas OTRO del golden set de telecomunicaciones
contra dos versiones del system prompt: v1 (el de `comun/prompts_industria.py`) y v2
(la misma, con una línea añadida que insiste en citar la fuente exacta antes de
afirmar una cifra). Mide exactitud con `comun.evaluadores` en ambas — el punto de la
demo es la TABLA comparativa, no que v2 gane.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comun.evaluadores import evaluar_exactitud  # noqa: E402
from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

TRACK = "telecomunicaciones"

PROMPT_V1 = get_system_prompt(TRACK)
PROMPT_V2 = PROMPT_V1 + (
    "\n\nAntes de afirmar cualquier tarifa, plazo o cifra concreta, cita textualmente el "
    "dato exacto del documento recuperado. Si no recuperaste el dato, dilo en vez de estimarlo."
)


def correr_version(model, prompt_sistema: str, casos: list[dict]) -> list[bool]:
    resultados = []
    for c in casos:
        r = model.invoke([("system", prompt_sistema), ("human", c["consulta"])])
        resultados.append(evaluar_exactitud(r.content, c["respuesta_esperada"]))
    return resultados


def main() -> None:
    print("=" * 72)
    print(f"  DEMO 4 · A/B de prompts — {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)

    ruta = ROOT / "recursos" / "golden" / f"consultas-{TRACK}.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    casos_otro = [c for c in datos["consultas"] if c["categoria"] == "otro"]

    model = get_chat_model()

    print(f"\n  Corriendo v1 sobre {len(casos_otro)} consultas OTRO...")
    v1 = correr_version(model, PROMPT_V1, casos_otro)
    print(f"  Corriendo v2 sobre {len(casos_otro)} consultas OTRO...")
    v2 = correr_version(model, PROMPT_V2, casos_otro)

    print(f"\n  {'Consulta'.ljust(50)}{'v1'.ljust(6)}{'v2'}")
    print("  " + "-" * 62)
    for c, r1, r2 in zip(casos_otro, v1, v2):
        print(f"  {c['consulta'][:47].ljust(50)}{str(r1).ljust(6)}{r2}")

    n = len(casos_otro)
    print(f"\n  v1: {sum(v1)}/{n} = {100 * sum(v1) / n:.1f} %")
    print(f"  v2: {sum(v2)}/{n} = {100 * sum(v2) / n:.1f} %")
    print(f"""
  Diferencia: {sum(v2) - sum(v1)} caso(s) de {n}. Antes de reportar esto como "v2 mejoró",
  recuerda el bloque 4 del README: con {n} casos, una diferencia de 1-2 aciertos puede ser
  ruido de muestreo. Corre la demo otra vez y compara si el resultado se sostiene.
""")


if __name__ == "__main__":
    main()
