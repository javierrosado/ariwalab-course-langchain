"""Demo 3 · Embeddings: buscar por significado, no por palabras.

Ejecutar desde la raíz del curso:
    python 00-preparacion/code/03_embeddings.py

Requiere HF_TOKEN en el .env.

Qué deberías observar:
  1. Dos frases SIN ninguna palabra en común pueden tener similitud alta.
  2. Dos frases que comparten palabras pueden tener similitud baja.
  3. Eso es exactamente lo que la búsqueda por palabras clave no puede hacer,
     y es la base del RAG que construirás en la sesión 5.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from comun.provider import get_embeddings  # noqa: E402

CONSULTA = "¿Cuántos gigas me quedan este mes?"

CANDIDATAS = [
    "Consulta del consumo de datos disponibles en el ciclo actual.",
    "El plan Max 89 incluye 30 GB de datos de alta velocidad.",
    "Quiero cancelar mi contrato y llevarme mi número a otra operadora.",
    "El SOAT cubre gastos médicos hasta cinco unidades impositivas tributarias.",
    "Me quedan pocos megas y navego lentísimo desde ayer.",
]


def coseno(a: list[float], b: list[float]) -> float:
    punto = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return punto / (na * nb) if na and nb else 0.0


def palabras_comunes(a: str, b: str) -> int:
    vacias = {"de", "la", "el", "en", "y", "a", "los", "las", "un", "una",
              "mi", "me", "que", "por", "con", "del", "al", "este", "su"}
    sa = {p.strip("¿?¡!.,").lower() for p in a.split()} - vacias
    sb = {p.strip("¿?¡!.,").lower() for p in b.split()} - vacias
    return len(sa & sb)


def barra(valor: float, ancho: int = 24) -> str:
    lleno = max(0, min(ancho, round(valor * ancho)))
    return "█" * lleno + "·" * (ancho - lleno)


def main() -> None:
    print("=" * 78)
    print("  DEMO 3 · Embeddings y similitud semántica")
    print("=" * 78)
    print(f"\n  Consulta de referencia:\n    «{CONSULTA}»\n")

    try:
        emb = get_embeddings()
        vectores = emb.embed_documents([CONSULTA] + CANDIDATAS)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al generar embeddings: {type(e).__name__}: {e}")
        print("     Revisa HF_TOKEN en tu .env y que tenga permiso de inferencia.")
        return

    base, resto = vectores[0], vectores[1:]
    print(f"  Dimensiones del vector: {len(base)}\n")

    filas = []
    for texto, vec in zip(CANDIDATAS, resto):
        filas.append((coseno(base, vec), palabras_comunes(CONSULTA, texto), texto))
    filas.sort(reverse=True)

    print(f"  {'Similitud':>9}  {'Palabras':>8}  Frase")
    print(f"  {'':>9}  {'comunes':>8}")
    print("  " + "-" * 74)
    for sim, comunes, texto in filas:
        print(f"  {sim:>9.3f}  {comunes:>8}  {barra(sim)}")
        print(f"  {'':>9}  {'':>8}  {texto[:60]}")
    print("  " + "-" * 74)

    mejor_sim, mejor_com, mejor_txt = filas[0]

    print(f"""

  Lo interesante está en la columna "palabras comunes"

    La frase más parecida a la consulta es:

      «{mejor_txt}»

    con una similitud de {mejor_sim:.3f} y solo {mejor_com} palabra(s) en común.

    Una búsqueda por palabras clave (LIKE, BM25) habría fallado con esa frase, y
    en cambio habría devuelto cualquier texto que contuviera "gigas" o "mes"
    aunque hablara de otra cosa.

  Cómo se usa esto en el curso

    Sesión 5: partirás los documentos de tu industria en fragmentos, los
    convertirás en vectores como estos, y los guardarás en Qdrant Cloud.
    Cuando el cliente pregunte algo, buscarás los fragmentos más cercanos
    y se los darás al modelo como contexto. Eso es RAG.

  Interpretación de los valores

      > 0.8   muy relacionados
    0.5-0.8   relacionados
      < 0.5   poco o nada relacionados
""")


if __name__ == "__main__":
    main()
