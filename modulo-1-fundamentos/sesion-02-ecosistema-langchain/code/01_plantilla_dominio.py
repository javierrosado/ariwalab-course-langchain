"""Demo 1 · Rol + Contexto + Tarea + Formato sobre el prompt del track.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/01_plantilla_dominio.py

Requiere HF_TOKEN.

Qué deberías observar:
  1. Con las 4 partes, la respuesta es una clasificación limpia y bien formada.
  2. Quitando el bloque FORMATO, el modelo sigue "entendiendo" la tarea pero la salida
     deja de tener una forma predecible — más difícil de parsear que si le hubieras
     quitado el ROL.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from comun.provider import describe_provider, get_chat_model  # noqa: E402

CONSULTA = "Se me corta la llamada cada dos minutos desde ayer, línea 987654321."

ROL = "Eres el clasificador de intención de AndesMóvil, un operador de telefonía móvil en Perú."
CONTEXTO = (
    "Las categorías posibles son: CONSULTA_PLAN, CONSULTA_CONSUMO, AVERIA, RECLAMO, OTRO. "
    "AVERIA es cuando el cliente reporta una falla técnica del servicio."
)
TAREA = f"Clasifica esta consulta de un cliente: \"{CONSULTA}\""
FORMATO = ("Responde en una sola línea con este formato exacto: "
          "categoria=<CATEGORIA> | urgencia=<BAJA|MEDIA|ALTA>")


def construir_prompt(con_formato: bool) -> str:
    partes = [ROL, CONTEXTO, TAREA]
    if con_formato:
        partes.append(FORMATO)
    return "\n\n".join(partes)


def main() -> None:
    print("=" * 72)
    print("  DEMO 1 · Rol + Contexto + Tarea + Formato")
    print(f"  {describe_provider()}")
    print("=" * 72)

    model = get_chat_model()

    print("\n  CON las 4 partes (incluye FORMATO):")
    print(f"  {'-' * 68}")
    try:
        respuesta_completa = model.invoke(construir_prompt(con_formato=True)).content
    except Exception as e:  # noqa: BLE001
        print(f"  ❌ Error: {type(e).__name__}: {e}")
        return
    print(f"  {respuesta_completa}")

    print("\n  SIN el bloque FORMATO (Rol + Contexto + Tarea nada más):")
    print(f"  {'-' * 68}")
    respuesta_sin_formato = model.invoke(construir_prompt(con_formato=False)).content
    print(f"  {respuesta_sin_formato}")

    print("""

  Fíjate en la segunda respuesta: probablemente el modelo sí identificó la categoría
  (el CONTEXTO y la TAREA ya le daban suficiente), pero la forma de la respuesta es
  impredecible — a veces una frase completa, a veces una lista, a veces con
  explicación. Sin FORMATO no tienes nada que parsear de forma confiable. Por eso el
  bloque 4 de hoy (structured output) existe: convierte el FORMATO en una garantía,
  no en una esperanza.
""")


if __name__ == "__main__":
    main()
