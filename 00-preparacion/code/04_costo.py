"""Demo 4 · Costo: por qué el historial es lo caro, no la última pregunta.

Ejecutar desde la raíz del curso:
    python 00-preparacion/code/04_costo.py

No requiere credenciales ni conexión: es una simulación aritmética.

Qué deberías observar:
  1. El costo por turno CRECE aunque las preguntas sean igual de cortas.
  2. Lo que crece es la ENTRADA, porque el historial se reenvía completo.
  3. Las estrategias de control de costo atacan la entrada, no la salida.
"""

from __future__ import annotations

# Precios de referencia por millón de tokens. Son valores ILUSTRATIVOS para el
# ejercicio: los precios reales varían por proveedor y cambian con el tiempo.
PRECIO_ENTRADA_POR_MILLON = 0.20
PRECIO_SALIDA_POR_MILLON = 0.60

SYSTEM_PROMPT = 1_000       # instrucciones + guardrails
ESQUEMAS_TOOLS = 1_200      # 4 herramientas
FRAGMENTOS_RAG = 2_000      # 4 chunks recuperados
PREGUNTA_USUARIO = 40       # el usuario escribe poco
RESPUESTA_AGENTE = 160      # el agente responde breve

TURNOS = 12
CONVERSACIONES_POR_DIA = 500


def costo(entrada: int, salida: int) -> float:
    return (entrada / 1_000_000 * PRECIO_ENTRADA_POR_MILLON
            + salida / 1_000_000 * PRECIO_SALIDA_POR_MILLON)


def barra(valor: float, maximo: float, ancho: int = 30) -> str:
    lleno = max(1, round(valor / maximo * ancho)) if maximo else 0
    return "█" * lleno


def main() -> None:
    print("=" * 78)
    print("  DEMO 4 · Anatomía del costo de una conversación")
    print("=" * 78)
    print(f"""
  Supuestos del ejercicio (precios ilustrativos, no reales):

    system prompt + guardrails    {SYSTEM_PROMPT:>6} tokens   (fijo en cada llamada)
    esquemas de 4 herramientas    {ESQUEMAS_TOOLS:>6} tokens   (fijo en cada llamada)
    fragmentos recuperados        {FRAGMENTOS_RAG:>6} tokens   (fijo en cada llamada)
    pregunta del usuario          {PREGUNTA_USUARIO:>6} tokens   (por turno)
    respuesta del agente          {RESPUESTA_AGENTE:>6} tokens   (por turno)

    entrada  USD {PRECIO_ENTRADA_POR_MILLON:.2f} / millón de tokens
    salida   USD {PRECIO_SALIDA_POR_MILLON:.2f} / millón de tokens
""")

    print(f"  {'Turno':>5} {'Entrada':>9} {'Salida':>7} {'Costo turno':>12} {'Acumulado':>11}")
    print("  " + "-" * 60)

    historial = 0
    acumulado = 0.0
    filas = []

    for turno in range(1, TURNOS + 1):
        entrada = SYSTEM_PROMPT + ESQUEMAS_TOOLS + FRAGMENTOS_RAG + historial + PREGUNTA_USUARIO
        salida = RESPUESTA_AGENTE
        c = costo(entrada, salida)
        acumulado += c
        filas.append((turno, entrada, salida, c, acumulado))
        print(f"  {turno:>5} {entrada:>9,} {salida:>7} {c:>12.6f} {acumulado:>11.6f}")
        # El turno completo se suma al historial de la siguiente llamada
        historial += PREGUNTA_USUARIO + RESPUESTA_AGENTE

    primero, ultimo = filas[0], filas[-1]
    crecimiento = ultimo[1] / primero[1]

    print("\n\n  Crecimiento de la entrada por turno\n")
    maximo = ultimo[1]
    for turno, entrada, _, _, _ in filas:
        print(f"  {turno:>3} {barra(entrada, maximo)} {entrada:>7,}")

    print(f"""

  Lectura del resultado

    La pregunta del usuario ocupa siempre {PREGUNTA_USUARIO} tokens, pero la entrada pasó de
    {primero[1]:,} a {ultimo[1]:,} tokens: se multiplicó por {crecimiento:.2f}.

    Lo que creció fue el HISTORIAL. El modelo es stateless: no recuerda nada,
    así que tu código le reenvía la conversación completa en cada llamada.

    Además, {SYSTEM_PROMPT + ESQUEMAS_TOOLS + FRAGMENTOS_RAG:,} tokens de cada llamada son fijos
    (prompt, herramientas y fragmentos recuperados). Eso se paga incluso cuando
    el usuario solo escribe "¿y el mes pasado?".

  Proyección a producción

    Costo de una conversación de {TURNOS} turnos:   USD {acumulado:.4f}
    {CONVERSACIONES_POR_DIA} conversaciones al día:               USD {acumulado * CONVERSACIONES_POR_DIA:.2f}
    Al mes (30 días):                       USD {acumulado * CONVERSACIONES_POR_DIA * 30:.2f}
    Al año:                                 USD {acumulado * CONVERSACIONES_POR_DIA * 365:.2f}

  Las cuatro palancas de optimización, y cuánto pesan

    1. Recortar o resumir el historial          ataca la parte que CRECE
    2. Recuperar 2 fragmentos en vez de 4       ahorra ~{FRAGMENTOS_RAG // 2:,} tokens por llamada
    3. Enlazar 4 herramientas y no 8            ahorra ~{ESQUEMAS_TOOLS:,} tokens por llamada
    4. Acortar el system prompt                 ahorra hasta ~{SYSTEM_PROMPT // 2:,} tokens por llamada

    Fíjate en que ninguna toca la respuesta del agente. Optimizar la salida es
    lo primero que intenta todo el mundo y es lo que menos rinde.

    En la sesión 10 medirás esto sobre trazas reales de tu propio agente en
    Langfuse, en vez de estimarlo como aquí.
""")


if __name__ == "__main__":
    main()
