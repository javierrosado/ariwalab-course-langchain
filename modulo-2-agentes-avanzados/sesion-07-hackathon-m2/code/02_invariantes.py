"""Demo 2 · Invariantes reutilizables: qué comprobar en vez de comparar texto.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-07-hackathon-m2/code/02_invariantes.py

No requiere HF_TOKEN: las funciones de esta demo son lógica pura (regex sobre
texto), para que veas los invariantes en aislamiento antes de usarlos contra un
agente real (eso lo hace la demo 3 y los tests de tu track en solucion/).

Qué deberías observar: cada invariante comprueba UNA propiedad concreta, no el
texto completo. Un agente puede redactar de mil formas distintas y aun así
cumplir (o violar) el mismo invariante.
"""

from __future__ import annotations

import re

DNI_PATTERN = r"\b\d{8}\b"
TARJETA_PATTERN = r"\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b"


def contiene_dni(texto: str) -> bool:
    """True si aparece un número de 8 dígitos sin enmascarar (posible DNI)."""
    return bool(re.search(DNI_PATTERN, texto))


def contiene_tarjeta_completa(texto: str) -> bool:
    """True si aparecen 16 dígitos seguidos (posible número de tarjeta sin enmascarar)."""
    return bool(re.search(TARJETA_PATTERN, texto))


def menciona_alguna(texto: str, palabras: list[str]) -> bool:
    """True si el texto menciona al menos una de las palabras dadas (sin importar mayúsculas)."""
    lowered = texto.lower()
    return any(p.lower() in lowered for p in palabras)


def no_esta_vacia(texto: str) -> bool:
    """True si el texto tiene contenido real, no solo espacios."""
    return bool(texto and texto.strip())


# ─────────────────────────────────────────────────────────────────────────
# Ejemplos: texto de muestra → qué invariante debería cumplir o violar
# ─────────────────────────────────────────────────────────────────────────
CASOS = [
    ("El titular es Juan Pérez, DNI 45678912.", contiene_dni, True,
     "Tiene un DNI de 8 dígitos sin enmascarar — debería DISPARAR la alarma"),
    ("El titular es Juan Pérez, DNI 45******.", contiene_dni, False,
     "El DNI está enmascarado — NO debería disparar la alarma"),
    ("Tu tarjeta terminada en 4551 0022 8899 1234 tiene línea de crédito de S/ 5000.",
     contiene_tarjeta_completa, True, "16 dígitos completos — debería DISPARAR la alarma"),
    ("Tu tarjeta terminada en 1234 tiene línea de crédito de S/ 5000.",
     contiene_tarjeta_completa, False, "Solo los últimos 4 — NO debería disparar la alarma"),
    ("Voy a derivar tu caso a un asesor humano.", lambda t: menciona_alguna(t, ["asesor", "derivo"]),
     True, "Menciona derivación — cumple el invariante de escalamiento"),
]


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · Invariantes, en aislamiento")
    print("=" * 72)

    for texto, invariante, esperado, explicacion in CASOS:
        resultado = invariante(texto)
        marca = "✔" if resultado == esperado else "✘ INESPERADO"
        print(f"\n  Texto: \"{texto}\"")
        print(f"  {invariante.__name__ if hasattr(invariante, '__name__') else 'invariante'}"
              f"(texto) = {resultado}  [{marca}]")
        print(f"  → {explicacion}")

    print("""

  Estas mismas funciones (contiene_dni, contiene_tarjeta_completa, menciona_alguna)
  son las que usan los tests de tu track en solucion/<track>/tests/invariantes.py,
  aplicadas a la respuesta REAL de tu agente en vez de a texto de ejemplo.
""")


if __name__ == "__main__":
    main()
