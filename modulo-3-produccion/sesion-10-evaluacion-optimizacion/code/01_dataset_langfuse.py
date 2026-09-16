"""Demo 1 · Subir los 30 casos del track a Langfuse Datasets.

Ejecutar desde la raíz del curso:
    python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/01_dataset_langfuse.py

Requiere las credenciales de Langfuse en el .env. Sube (o actualiza, si ya existe)
`recursos/golden/consultas-telecomunicaciones.json` completo como un Dataset de
Langfuse — el mismo golden set que alimentó el L2 (clasificación), el L4 (selección
de tool) y el L5 (categoría OTRO), ahora usado por cuarta vez, completo.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

import json  # noqa: E402

from comun.observability import _configurar_cliente_langfuse  # noqa: E402

TRACK = "telecomunicaciones"


def main() -> None:
    print("=" * 72)
    print(f"  DEMO 1 · dataset de {TRACK} en Langfuse")
    print("=" * 72)

    _configurar_cliente_langfuse()
    from langfuse import get_client

    client = get_client()
    nombre_dataset = f"golden-{TRACK}"

    client.create_dataset(
        name=nombre_dataset,
        description=f"Golden set del curso — {TRACK} (30 casos: 20 con tool + 10 otro)",
    )

    ruta = ROOT / "recursos" / "golden" / f"consultas-{TRACK}.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))

    for caso in datos["consultas"]:
        client.create_dataset_item(
            dataset_name=nombre_dataset,
            input={"consulta": caso["consulta"], "categoria": caso["categoria"]},
            expected_output={
                "tool_esperada": caso["tool_esperada"],
                "respuesta_esperada": caso["respuesta_esperada"],
            },
            metadata={"intencion": caso["intencion"]},
        )

    print(f"\n  {len(datos['consultas'])} casos subidos al dataset '{nombre_dataset}'.")
    print("  Ábrelo en cloud.langfuse.com → Datasets. La demo 4 lo usará para correr v1 vs v2.")


if __name__ == "__main__":
    main()
