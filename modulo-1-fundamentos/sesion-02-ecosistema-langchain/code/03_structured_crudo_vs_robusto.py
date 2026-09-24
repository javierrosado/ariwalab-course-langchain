"""Demo 3 · La misma extracción por dos caminos: crudo vs con comun/structured.py.

Ejecutar desde la raíz del curso:
    python modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/03_structured_crudo_vs_robusto.py

Requiere HF_TOKEN. El fallo no está garantizado: con esquema Pydantic, la integración
valida durante invoke. Una consulta ambigua también puede producir un objeto válido.
Para fallos reproducibles, ver docente/verificar_structured.py.

Qué deberías observar:
  1. El camino CRUDO puede lanzar errores de validación o del proveedor durante invoke.
  2. El camino ROBUSTO (extraer_con_detalle) comprueba el retorno y reintenta,
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
    print("  CAMINO CRUDO — with_structured_output() directo, sin wrapper de recuperación")
    print("  " + "-" * 68)
    estructurado = modelo.with_structured_output(Intencion)
    try:
        resultado = estructurado.invoke(consulta)
    except Exception as e:  # noqa: BLE001
        print(f"  El proveedor devolvió un error: {type(e).__name__}: {e}")
        print("  (el tipo de excepción ayuda a distinguir validación, parser o proveedor)")
        return
    if resultado is None:
        print("  ⚠️  El modelo devolvió None. El siguiente código que use resultado.categoria")
        print("      va a reventar con AttributeError, TRES LÍNEAS MÁS ABAJO de aquí.")
        return
    print(f"  Resultado: {resultado}")
    print("  (salida válida estructuralmente; comprobar también si la clasificación es correcta)")


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

  Ambos caminos usan la validación del esquema Pydantic. El wrapper añade
  comprobación del retorno, un reintento correctivo y ExtraccionFallida al agotar
  ese presupuesto. Un esquema válido no garantiza una clasificación correcta.
""")


if __name__ == "__main__":
    main()
