"""L10 · Telecomunicaciones — AndesMóvil · evals/dataset.py (checkpoint de referencia)

Carga las 30 filas de `recursos/golden/consultas-telecomunicaciones.json` y las sube
como Langfuse Dataset. Mismo código que `code/01_dataset_langfuse.py`, ya fijado a
este track.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-10-evaluacion-optimizacion/solucion/telecomunicaciones/evals/dataset.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))

from comun.observability import _configurar_cliente_langfuse  # noqa: E402

TRACK = "telecomunicaciones"
NOMBRE_DATASET = f"golden-{TRACK}"


def cargar_casos() -> list[dict]:
    ruta = ROOT / "recursos" / "golden" / f"consultas-{TRACK}.json"
    return json.loads(ruta.read_text(encoding="utf-8"))["consultas"]


def subir_dataset() -> int:
    _configurar_cliente_langfuse()
    from langfuse import get_client

    client = get_client()
    client.create_dataset(
        name=NOMBRE_DATASET,
        description=f"Golden set del curso — {TRACK} (30 casos: 20 con tool + 10 otro)",
    )
    casos = cargar_casos()
    for caso in casos:
        client.create_dataset_item(
            dataset_name=NOMBRE_DATASET,
            input={"consulta": caso["consulta"], "categoria": caso["categoria"]},
            expected_output={
                "tool_esperada": caso["tool_esperada"],
                "respuesta_esperada": caso["respuesta_esperada"],
            },
            metadata={"intencion": caso["intencion"]},
        )
    return len(casos)


if __name__ == "__main__":
    n = subir_dataset()
    print(f"{n} casos subidos al dataset '{NOMBRE_DATASET}' en Langfuse.")
