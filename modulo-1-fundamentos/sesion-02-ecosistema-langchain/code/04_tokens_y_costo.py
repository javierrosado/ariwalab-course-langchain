"""Demo 4 · Conteo de tokens: con y sin few-shot, y con historial creciente.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/04_tokens_y_costo.py

No requiere HF_TOKEN: usa el mismo tokenizador (real si `transformers` está instalado,
estimación si no) que la demo 1 de la Sesión 0 — no gasta cuota, es aritmética.

Qué deberías observar:
  1. El few-shot se paga EN CADA LLAMADA, no una sola vez: 4 ejemplos cuestan lo mismo
     en el turno 1 que en el turno 10.
  2. El historial de conversación crece más rápido que el few-shot fijo: a partir de
     cierto turno, el historial —no los ejemplos— domina el costo.
"""

from __future__ import annotations

MODELO = "Qwen/Qwen3-32B"

SISTEMA = (
    "Eres el clasificador de intención de AndesMóvil. Categorías: CONSULTA_PLAN, "
    "CONSULTA_CONSUMO, AVERIA, RECLAMO, OTRO. Responde SOLO con la categoría."
)

EJEMPLOS_FEW_SHOT = [
    ("Se me cae la llamada todo el tiempo", "AVERIA"),
    ("Quiero un número de seguimiento de mi queja", "RECLAMO"),
    ("No tengo señal desde esta mañana", "AVERIA"),
    ("Registren mi reclamo formal, por favor", "RECLAMO"),
]

PREGUNTA_USUARIO = "¿Cuántos gigas me quedan este mes? Mi línea es 987654321"
RESPUESTA_MODELO = "CONSULTA_CONSUMO"


def cargar_tokenizador():
    try:
        from transformers import AutoTokenizer
        return AutoTokenizer.from_pretrained(MODELO), True
    except Exception:  # noqa: BLE001 — sin red o sin `transformers`
        return None, False


def contar(texto: str, tok, real: bool) -> int:
    if real:
        return len(tok.encode(texto))
    return max(1, round(len(texto) / 4))  # ~4 caracteres por token, ver Sesión 0


def main() -> None:
    tok, real = cargar_tokenizador()
    etiqueta = "TOKENIZACIÓN REAL" if real else "ESTIMACIÓN (instala `transformers` para la real)"

    print("=" * 72)
    print(f"  DEMO 4 · Tokens y costo — {etiqueta}")
    print("=" * 72)

    # ── Parte 1: costo fijo del few-shot ────────────────────────────────────
    print("\n1) El few-shot se paga en cada llamada\n")
    costo_sistema = contar(SISTEMA, tok, real)
    costo_ejemplos = [contar(f"{p} {r}", tok, real) for p, r in EJEMPLOS_FEW_SHOT]
    print(f"  System prompt: {costo_sistema} tokens (fijo, va en cada llamada)")
    acumulado = 0
    for i, c in enumerate(costo_ejemplos, start=1):
        acumulado += c
        print(f"  + ejemplo {i}: {c} tokens (acumulado few-shot: {acumulado})")
    print(f"\n  Con 4 ejemplos, cada llamada del clasificador arrastra {acumulado} tokens "
          f"SOLO de few-shot, se use o no la conversación es nueva.")

    # ── Parte 2: costo creciente del historial ──────────────────────────────
    print("\n\n2) El historial crece más rápido que el few-shot fijo\n")
    turno = {"role": "human/ai", "texto": f"{PREGUNTA_USUARIO} {RESPUESTA_MODELO}"}
    costo_turno = contar(turno["texto"], tok, real)
    print(f"  {'Turno':>6} {'Historial (tokens)':>20} {'Few-shot fijo':>16} {'Total':>10}")
    print("  " + "-" * 58)
    for n_turno in (1, 3, 5, 10, 20):
        costo_historial = costo_sistema + n_turno * costo_turno
        total = costo_historial + acumulado
        print(f"  {n_turno:>6} {costo_historial:>20} {acumulado:>16} {total:>10}")

    print(f"""

3) Qué significa esto para tu clasificador

   El few-shot cuesta lo mismo siempre: {acumulado} tokens, turno 1 o turno 20.
   El historial, en cambio, CRECE. Para un clasificador de un solo turno (como el
   L2 de hoy, que no arrastra conversación) el few-shot es casi todo el costo extra.
   Para un AGENTE de varios turnos (lo que construyes desde la S3), el historial
   termina dominando — por eso optimizar el historial rinde más que optimizar el
   few-shot a partir de cierto punto de la conversación.
""")


if __name__ == "__main__":
    main()
