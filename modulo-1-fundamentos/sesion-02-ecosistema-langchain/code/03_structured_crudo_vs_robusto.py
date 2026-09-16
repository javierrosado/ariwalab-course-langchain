"""Demo 3 · La misma extracción por dos caminos: crudo vs con comun/structured.py.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/03_structured_crudo_vs_robusto.py

Requiere HF_TOKEN. ES LA DEMO QUE TIENE QUE FALLAR EN VIVO (ver README.md, bloque 4):
con una consulta ambigua y un esquema sin few-shot, `with_structured_output()` solo
puede devolver un enum inventado o un campo vacío que revienta más adelante.

Qué deberías observar:
  1. El camino CRUDO puede fallar de forma silenciosa: no lanza una excepción clara,
     simplemente el objeto queda con datos inválidos o el código revienta después.
  2. El camino ROBUSTO (extraer_con_detalle) valida, reintenta con el error concreto,
     y si de verdad no se puede, falla con ExtraccionFallida — nunca en silencio.
"""

from __future__ import annotations

import sys
from enum import Enum
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from pydantic import BaseModel, Field  # noqa: E402

from comun.provider import describe_provider, get_chat_model  # noqa: E402
from comun.structured import ExtraccionFallida, extraer_con_detalle  # noqa: E402


class CategoriaTelco(str, Enum):
    CONSULTA_PLAN = "CONSULTA_PLAN"
    CONSULTA_CONSUMO = "CONSULTA_CONSUMO"
    AVERIA = "AVERIA"
    RECLAMO = "RECLAMO"
    OTRO = "OTRO"


class UrgenciaTelco(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class Intencion(BaseModel):
    """Clasificación de una consulta de cliente, sin few-shot (a propósito, para esta demo)."""
    categoria: CategoriaTelco = Field(description="Categoría de la consulta")
    urgencia: UrgenciaTelco = Field(description="Nivel de urgencia percibido")


# Consulta ambigua a propósito: no usa ninguna palabra literal de las categorías.
CONSULTA_AMBIGUA = "Oye, esto que me está pasando con mi línea ya me tiene mal, atiéndanme."


def camino_crudo(modelo, consulta: str) -> None:
    print("  CAMINO CRUDO — with_structured_output() directo, sin validar")
    print("  " + "-" * 68)
    estructurado = modelo.with_structured_output(Intencion)
    try:
        resultado = estructurado.invoke(consulta)
    except Exception as e:  # noqa: BLE001
        print(f"  El proveedor devolvió un error: {type(e).__name__}: {e}")
        print("  (con with_structured_output() solo, este error no se distingue de uno de red)")
        return
    if resultado is None:
        print("  ⚠️  El modelo devolvió None. El siguiente código que use resultado.categoria")
        print("      va a reventar con AttributeError, TRES LÍNEAS MÁS ABAJO de aquí.")
        return
    print(f"  Resultado: {resultado}")
    print("  (si llegaste hasta aquí, esta vez no falló — pero nada te avisó de que PODÍA)")


def camino_robusto(modelo, consulta: str) -> None:
    print("\n  CAMINO ROBUSTO — extraer_con_detalle() de comun/structured.py")
    print("  " + "-" * 68)
    try:
        r = extraer_con_detalle(modelo, Intencion, consulta, reintentos=1)
    except ExtraccionFallida as e:
        print(f"  ExtraccionFallida (controlada, no un crash): {e}")
        return
    print(f"  Resultado: {r.datos}")
    print(f"  Intentos: {r.intentos} · ¿al primer intento?: {r.al_primer_intento}")
    if r.errores:
        print(f"  Errores en el camino: {r.errores}")


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · Structured output: crudo vs robusto")
    print(f"  {describe_provider()}")
    print("=" * 72)
    print(f"\n  Consulta ambigua: \"{CONSULTA_AMBIGUA}\"\n")

    modelo = get_chat_model()
    camino_crudo(modelo, CONSULTA_AMBIGUA)
    camino_robusto(modelo, CONSULTA_AMBIGUA)

    print("""

  La diferencia no es que uno "funcione mejor": es que el camino robusto SIEMPRE
  termina en uno de dos estados conocidos (un Intencion válido, o una excepción
  controlada), mientras que el crudo puede terminar en un tercer estado -silencioso-
  que revienta en otro archivo, minutos después, sin ninguna pista de dónde vino.
""")


if __name__ == "__main__":
    main()
