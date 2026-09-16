"""Demo 1 · Tokenización: por qué el español cuesta más.

Ejecutar desde la raíz del curso:
    python 00-preparacion/code/01_tokens.py

No requiere credenciales. La primera ejecución descarga el tokenizador de Qwen
(unos pocos MB desde Hugging Face); si no hay red o no está `transformers`,
el script cae a una estimación por caracteres y lo dice.

Qué deberías observar:
  1. Un token NO es una palabra: es un fragmento.
  2. El mismo significado cuesta más tokens en español que en inglés.
  3. Las palabras técnicas y los nombres propios se parten en muchos trozos.
"""

from __future__ import annotations

MODELO = "Qwen/Qwen3-32B"

PARES = [
    ("¿Cuánto saldo tengo disponible?", "How much balance do I have?"),
    ("Quiero solicitar la portabilidad numérica de mi línea.",
     "I want to request number portability for my line."),
    ("El SOAT cubre gastos médicos hasta cinco unidades impositivas tributarias.",
     "The mandatory insurance covers medical expenses up to five tax units."),
    ("Mi refrigeradora llegó dañada y necesito una devolución.",
     "My refrigerator arrived damaged and I need a refund."),
]

PALABRAS_SUELTAS = [
    "hola", "portabilidad", "desgravamen", "siniestro",
    "Ninahuanca", "AndesMóvil", "987654321", "S/ 45.20",
]


def cargar_tokenizador():
    """Devuelve (funcion_tokenizar, es_real). Cae a estimación si no hay tokenizador."""
    try:
        from transformers import AutoTokenizer
    except ImportError:
        print("⚠️  `transformers` no está instalado. Usando ESTIMACIÓN por caracteres.")
        print("    Para ver la tokenización real: pip install transformers\n")
        return None, False

    try:
        tok = AutoTokenizer.from_pretrained(MODELO)
        return tok, True
    except Exception as e:  # noqa: BLE001 — sin red, o modelo no accesible
        print(f"⚠️  No se pudo descargar el tokenizador ({type(e).__name__}).")
        print("    Usando ESTIMACIÓN por caracteres.\n")
        return None, False


def contar(texto: str, tok, real: bool) -> int:
    if real:
        return len(tok.encode(texto))
    # Estimación gruesa: ~4 caracteres por token. Sirve para ver la proporción,
    # no para calcular costos reales.
    return max(1, round(len(texto) / 4))


def trozos(texto: str, tok, real: bool) -> list[str]:
    if not real:
        return ["(estimación: sin desglose)"]
    return [tok.decode([t]) for t in tok.encode(texto)]


def main() -> None:
    tok, real = cargar_tokenizador()
    etiqueta = "TOKENIZACIÓN REAL" if real else "ESTIMACIÓN"

    print("=" * 72)
    print(f"  DEMO 1 · Tokenización — {etiqueta}")
    print(f"  Modelo: {MODELO}")
    print("=" * 72)

    # ── Parte 1: palabras sueltas ──────────────────────────────────────────
    print("\n1) Un token no es una palabra\n")
    print(f"  {'Texto':<16} {'Tokens':>7}   Desglose")
    print("  " + "-" * 68)
    for p in PALABRAS_SUELTAS:
        n = contar(p, tok, real)
        desglose = " | ".join(trozos(p, tok, real)) if real else ""
        print(f"  {p:<16} {n:>7}   {desglose}")

    # ── Parte 2: español vs inglés ─────────────────────────────────────────
    print("\n\n2) El mismo significado en español y en inglés\n")
    print(f"  {'Español':>8} {'Inglés':>8} {'Sobrecosto':>11}   Frase")
    print("  " + "-" * 68)
    total_es = total_en = 0
    for es, en in PARES:
        n_es, n_en = contar(es, tok, real), contar(en, tok, real)
        total_es += n_es
        total_en += n_en
        pct = (n_es / n_en - 1) * 100 if n_en else 0
        print(f"  {n_es:>8} {n_en:>8} {pct:>10.0f}%   {es[:44]}")

    sobrecosto = (total_es / total_en - 1) * 100 if total_en else 0
    print("  " + "-" * 68)
    print(f"  {total_es:>8} {total_en:>8} {sobrecosto:>10.0f}%   TOTAL")

    # ── Conclusión ─────────────────────────────────────────────────────────
    print(f"""

3) Qué significa esto para tu agente

   El español cuesta alrededor de un {sobrecosto:.0f}% más de tokens que el inglés.
   Como TODO se mide en tokens —el costo, el límite de contexto y la latencia—,
   un curso en español opera con menos margen que el mismo curso en inglés.

   Regla práctica en español:  1 token ≈ 0.75 palabras

   Presupuesto de una llamada del agente que construirás:

       system prompt + guardrails    ~1 000 tokens
       4 esquemas de herramientas    ~1 200 tokens
       4 fragmentos recuperados      ~2 000 tokens
       historial de conversación     ~1 500 tokens
                                     ──────────────
                                     ~5 700 tokens por llamada

   La ventana de Qwen3-32B es de 32 768 tokens: hay margen de sobra.
   El contexto nunca es el problema en este curso; el razonamiento sí.
""")


if __name__ == "__main__":
    main()
