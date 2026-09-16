"""L1 · Banca — Banco Inti · primer_contacto.py (checkpoint de referencia)

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-01-fundamentos-agentes/solucion/banca/primer_contacto.py

Requiere HF_TOKEN en el .env y, si tu equipo eligió este track, COURSE_TRACK=banca.

Le hace al modelo 3 preguntas reales de un cliente de Banco Inti. Sin tools, sin Pydantic,
sin agente: es el punto de partida, no el destino (ver README.md de la sesión, sección 11).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from comun.prompts_industria import get_system_prompt  # noqa: E402
from comun.provider import describe_provider, get_chat_model  # noqa: E402

TRACK = "banca"

QUESTIONS = [
    "¿Cuánto cobra el banco por mantenimiento de cuenta de ahorros y por una transferencia "
    "interbancaria?",
    "¿Qué pasos sigue el banco si detecta una operación sospechosa en mi tarjeta?",
    "¿Qué cubre exactamente el seguro de protección de mi tarjeta de crédito?",
]

# Reto opcional (no evaluado): descomenta esta línea para ver al modelo inventar un dato
# que solo existe en el core bancario real. No hay ninguna herramienta que lo evite.
# QUESTIONS.append("¿Cuál es el saldo disponible de la cuenta 191-2233445-0-11?")


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
