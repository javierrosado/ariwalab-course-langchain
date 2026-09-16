"""Demo 3 · La misma consulta con y sin el enmascarador: lo que Langfuse llega a almacenar.

Ejecutar desde la raíz del curso (no requiere credenciales):
    python modulo-3-produccion/sesion-09-observabilidad-langfuse/code/03_pii_en_traza.py

Se corre ANTES de que el alumno instrumente el suyo (parte 1 del lab). Ver el DNI
completo dentro de una traza de un servicio ajeno es más convincente que cualquier
explicación — aquí se muestra la transformación exacta que aplica
`comun.observability.enmascarar_pii()` antes de que cualquier dato salga hacia Langfuse.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comun.observability import enmascarar_pii  # noqa: E402

CONVERSACION_SIN_ENMASCARAR = {
    "mensaje_cliente": "Soy el titular con DNI 45678912, mi línea es 987654321, y la "
                        "tarjeta con la que pago mi plan es 4111 1111 1111 1111.",
    "respuesta_agente": "Confirmado, DNI 45678912. Tu línea 987654321 tiene el plan Max 89.",
}


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · PII dentro de una traza, con y sin enmascarador")
    print("=" * 72)

    print("\n  SIN enmascarar (lo que Langfuse almacenaría sin la decisión de la S9):")
    for campo, valor in CONVERSACION_SIN_ENMASCARAR.items():
        print(f"    {campo}: {valor}")

    enmascarada = enmascarar_pii(CONVERSACION_SIN_ENMASCARAR)
    print("\n  CON enmascarador (lo que de verdad sale hacia Langfuse):")
    for campo, valor in enmascarada.items():
        print(f"    {campo}: {valor}")

    print("""
  El DNI, la línea y la tarjeta quedan parcialmente ocultos ANTES de exportar. Nota
  el costo: si tuvieras que depurar un caso real leyendo la traza, ya no podrías ver
  el número completo — tendrías que pedírselo al equipo o al cliente. Es el
  compromiso real de producción, firmado a propósito (bloque 4 del README).
""")


if __name__ == "__main__":
    main()
