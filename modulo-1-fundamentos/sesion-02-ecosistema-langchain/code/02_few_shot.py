"""Demo 2 · El mismo clasificador con 0, 2 y 4 ejemplos few-shot (regla A5).

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/02_few_shot.py

Requiere HF_TOKEN.

Qué deberías observar: en las consultas AMBIGUAS, pasar de 0 a 2 ejemplos suele
arreglar la clasificación. Pasar de 2 a 4 casi nunca cambia nada — el 3.º y 4.º
ejemplo rinden mucho menos que el 1.º y 2.º, y solo suman tokens.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from comun.provider import describe_provider, get_chat_model  # noqa: E402

SISTEMA = (
    "Eres el clasificador de intención de AndesMóvil. Categorías: CONSULTA_PLAN, "
    "CONSULTA_CONSUMO, AVERIA, RECLAMO, OTRO. Responde SOLO con la categoría, una palabra."
)

# Ejemplos ordenados: los 2 primeros cubren la confusión más común
# (AVERIA vs RECLAMO); los 2 últimos son variaciones menores que aportan poco.
EJEMPLOS = [
    ("Se me cae la llamada todo el tiempo, ya es insoportable", "AVERIA"),
    ("Quiero un número de seguimiento porque llevo 3 días sin servicio", "RECLAMO"),
    ("No tengo señal desde esta mañana", "AVERIA"),
    ("Registren mi queja formal, por favor", "RECLAMO"),
]

# Consultas deliberadamente ambiguas entre AVERIA y RECLAMO.
CONSULTAS_AMBIGUAS = [
    "Mi internet no funciona y quiero que quede constancia por escrito",
    "Llevo dos días sin poder llamar, esto ya me tiene cansado",
]


def construir_mensajes(consulta: str, n_ejemplos: int) -> list[tuple[str, str]]:
    mensajes = [("system", SISTEMA)]
    for texto, categoria in EJEMPLOS[:n_ejemplos]:
        mensajes.append(("human", texto))
        mensajes.append(("ai", categoria))
    mensajes.append(("human", consulta))
    return mensajes


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · Few-shot: 0, 2 y 4 ejemplos")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()

    for consulta in CONSULTAS_AMBIGUAS:
        print(f"\n  Consulta ambigua: \"{consulta}\"")
        for n in (0, 2, 4):
            mensajes = construir_mensajes(consulta, n)
            try:
                respuesta = model.invoke(mensajes).content.strip()
            except Exception as e:  # noqa: BLE001
                print(f"  ❌ Error: {type(e).__name__}: {e}")
                return
            print(f"    {n} ejemplos → {respuesta}")

    print("""

  Compara la columna de 0 ejemplos contra la de 2: es donde suele verse el cambio.
  La de 4 casi nunca difiere de la de 2 — y sin embargo pagaste el doble de tokens
  de ejemplos en cada llamada. Esa es la regla A5 medida, no opinada.
""")


if __name__ == "__main__":
    main()
