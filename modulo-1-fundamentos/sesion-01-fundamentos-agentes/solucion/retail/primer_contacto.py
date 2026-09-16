"""L1 · Retail — MercaSur · primer_contacto.py (checkpoint de referencia)

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-01-fundamentos-agentes/solucion/retail/primer_contacto.py

Requiere HF_TOKEN en el .env y, si tu equipo eligió este track, COURSE_TRACK=retail.

Le hace al modelo 3 preguntas reales de un cliente de MercaSur. Sin tools, sin Pydantic,
sin agente: es el punto de partida, no el destino (ver README.md de la sesión, sección 11).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

TRACK = "retail"

QUESTIONS = [
    "¿Cuál es la política de cambios y devoluciones si mi producto llegó dañado?",
    "¿Cuánto tiempo de garantía tienen los electrodomésticos que venden?",
    "¿Qué hago si mi pedido no llega en la fecha que me estimaron?",
]

# Reto opcional (no evaluado): descomenta esta línea para ver al modelo inventar un dato
# que solo existe en el sistema de pedidos real. No hay ninguna herramienta que lo evite.
# QUESTIONS.append("¿En qué estado está mi pedido PED-00842?")


def main() -> None:
    print("=" * 72)
    print(f"  Primer contacto · {TRACK}")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()
    system_prompt = get_system_prompt(TRACK)

    for question in QUESTIONS:
        print(f"\n  Pregunta: {question}")
        try:
            answer = model.invoke(
                [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question},
                ]
            )
        except Exception as e:  # noqa: BLE001
            print(f"  ❌ Error al llamar al modelo: {type(e).__name__}: {e}")
            print("     Revisa HF_TOKEN en tu .env y que tenga permiso de inferencia.")
            return
        print(f"  Respuesta: {answer.content}\n")
        print("  " + "-" * 68)


if __name__ == "__main__":
    main()
