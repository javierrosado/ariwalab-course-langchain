"""L2 · Telecomunicaciones — AndesMóvil · medir_clasificador.py (checkpoint de referencia)

Corre las 26 consultas de recursos/golden/consultas-telecomunicaciones.json contra
clasificar_con_detalle(), e imprime acierto, matriz de confusión y cuántas
extracciones necesitaron reintento.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-02-ecosistema-langchain/solucion/telecomunicaciones/medir_clasificador.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida  # noqa: E402

from clasificar import clasificar_con_detalle  # noqa: E402

TRACK = "telecomunicaciones"
UMBRAL = 90.0

# 5 consultas propias del equipo — reemplázalas por las tuyas antes de reportar.
CONSULTAS_PROPIAS: list[tuple[str, str]] = [
    ("Quiero cambiar mi número de titular, ¿qué necesito?", "OTRO"),
    ("Se me traba la app pero la línea sí tiene señal", "AVERIA"),
    ("¿Cuántos minutos me quedan este mes? Línea 998877665", "CONSULTA_CONSUMO"),
    ("Denme un código de reclamo, ya es la tercera vez que llamo", "RECLAMO"),
    ("¿Mi plan incluye roaming internacional?", "CONSULTA_PLAN"),
]


def cargar_golden() -> list[tuple[str, str]]:
    ruta = ROOT / "recursos" / "golden" / f"consultas-{TRACK}.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    return [(c["consulta"], c["intencion"]) for c in datos["consultas"]]


def evaluar(modelo, casos: list[tuple[str, str]]) -> list[dict]:
    filas = []
    for consulta, esperada in casos:
        try:
            r = clasificar_con_detalle(modelo, consulta)
            obtenida = r.datos.categoria.value
            intentos = r.intentos
        except ExtraccionFallida as e:
            obtenida, intentos = "(fallo)", None
            print(f"  ⚠ ExtraccionFallida en \"{consulta[:50]}\": {e}")
        filas.append({
            "consulta": consulta, "esperada": esperada, "obtenida": obtenida,
            "acierto": obtenida == esperada, "intentos": intentos,
        })
    return filas


def imprimir_matriz(filas: list[dict]) -> None:
    categorias = sorted({f["esperada"] for f in filas} | {f["obtenida"] for f in filas})
    conteo = Counter((f["esperada"], f["obtenida"]) for f in filas)
    ancho = max(len(c) for c in categorias) + 4
    print("\n  " + "esperada \\ obtenida".ljust(ancho) +
          "".join(c[:10].rjust(12) for c in categorias))
    for esp in categorias:
        fila = "".join(str(conteo[(esp, obt)]).rjust(12) if conteo[(esp, obt)] else "·".rjust(12)
                       for obt in categorias)
        print(f"  {esp.ljust(ancho)}{fila}")


def main() -> None:
    print("=" * 72)
    print(f"  MEDIR CLASIFICADOR · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)

    modelo = get_chat_model()
    golden = cargar_golden()

    print(f"\n  Evaluando {len(golden)} consultas del golden set del curso...")
    filas_golden = evaluar(modelo, golden)
    aciertos = sum(f["acierto"] for f in filas_golden)
    pct = 100 * aciertos / len(filas_golden)

    imprimir_matriz(filas_golden)
    print(f"\n  Acierto sobre el golden set: {aciertos}/{len(filas_golden)} = {pct:.1f} % "
          f"{'✔ pasa' if pct >= UMBRAL else '✘ por debajo del umbral'} (umbral {UMBRAL:.0f} %)")

    con_reintento = [f for f in filas_golden if f["intentos"] and f["intentos"] > 1]
    print(f"  Extracciones que necesitaron reintento: {len(con_reintento)}/{len(filas_golden)}")

    print(f"\n  Evaluando {len(CONSULTAS_PROPIAS)} consultas propias del equipo...")
    filas_propias = evaluar(modelo, CONSULTAS_PROPIAS)
    aciertos_propias = sum(f["acierto"] for f in filas_propias)

    total = len(filas_golden) + len(filas_propias)
    aciertos_total = aciertos + aciertos_propias
    print(f"\n  RESUMEN FINAL: {aciertos_total}/{total} = {100 * aciertos_total / total:.1f} % "
          f"sobre el golden set + las 5 propias")


if __name__ == "__main__":
    main()
