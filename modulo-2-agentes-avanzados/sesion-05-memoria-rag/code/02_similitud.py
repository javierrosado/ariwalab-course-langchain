"""Demo 2 · Similitud: las preguntas del track contra la colección, con su puntaje.

Ejecutar desde la raíz del curso, DESPUÉS de 01_ingesta.py (usa la misma colección):
    python modulo-2-agentes-avanzados/sesion-05-memoria-rag/code/02_similitud.py

Requiere HF_TOKEN y Qdrant configurados.

Qué deberías observar: igual que la demo 3 de la Sesión 0, la columna "palabras comunes"
suele ser baja incluso en los resultados con mejor puntaje — la búsqueda encuentra
significado, no coincidencia léxica.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from comun.vectorstore import get_vector_store  # noqa: E402

TRACK = "telecomunicaciones"
COLLECTION_NAME = f"kb-{TRACK}-demo"

QUESTIONS = [
    "¿Cuántos gigas me quedan este mes?",
    "¿Qué pasa si debo una factura y quiero cambiarme de operador?",
    "¿En cuánto tiempo me responden un reclamo?",
]


def common_words(a: str, b: str) -> int:
    return len(set(a.lower().split()) & set(b.lower().split()))


def main() -> None:
    print("=" * 72)
    print(f"  DEMO 2 · Similitud ({TRACK})")
    print("=" * 72)

    try:
        store = get_vector_store(COLLECTION_NAME)
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error al conectar con Qdrant: {type(e).__name__}: {e}")
        return

    for question in QUESTIONS:
        print(f"\n  Pregunta: {question}")
        try:
            results = store.similarity_search_with_score(question, k=2)
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error al buscar: {type(e).__name__}: {e}")
            print("  ¿Corriste 01_ingesta.py primero?")
            return
        for doc, score in results:
            comunes = common_words(question, doc.page_content)
            fragmento = doc.page_content[:100].replace("\n", " ")
            print(f"    score={score:.3f} · palabras comunes={comunes} · "
                  f"fuente={doc.metadata.get('source')} · \"{fragmento}...\"")

    print("""

  Fíjate en la columna "palabras comunes": los mejores resultados casi nunca comparten
  la mayoría de las palabras con la pregunta. Eso es exactamente lo que una búsqueda con
  `LIKE` o `grep` no puede hacer — es la razón de ser del RAG.
""")


if __name__ == "__main__":
    main()
