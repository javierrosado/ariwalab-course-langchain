"""Verificador de comun/structured.py — la regla A3 convertida en código.

Ejecutar desde la raíz del curso:
    python docente/verificar_structured.py

36 comprobaciones con un modelo simulado. No requiere red, token de Hugging Face
ni ninguna credencial: el objetivo es probar la *lógica* de validación y reintento,
no el modelo. Un modelo real haría la prueba lenta, cara y no repetible — y jamás
fallaría a demanda, que es justo lo que aquí hay que verificar.
"""
from __future__ import annotations

import sys
from enum import Enum
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pydantic import BaseModel, Field, ValidationError  # noqa: E402

from comun.structured import (  # noqa: E402
    ExtraccionFallida,
    ResultadoEstructurado,
    _instruccion_correctiva,
    extraer,
    extraer_con_detalle,
)

ok = True


def chk(label, cond, extra=""):
    global ok
    print(f"  [{'OK  ' if cond else 'FALLA'}] {label}{(' — ' + str(extra)[:70]) if extra else ''}")
    ok &= bool(cond)


# ─────────────────────────────────────────────────────────────────────────────
# Esquema de prueba: el mismo que usan los alumnos en el Laboratorio 2
# ─────────────────────────────────────────────────────────────────────────────
class Urgencia(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"


class Intencion(BaseModel):
    """Consulta de cliente ya clasificada."""

    categoria: str = Field(description="Categoría de la consulta")
    urgencia: Urgencia = Field(description="Nivel de urgencia")
    numero_linea: str | None = Field(default=None, description="Línea si la mencionó")


class Otra(BaseModel):
    valor: int


VALIDO = Intencion(categoria="AVERIA", urgencia=Urgencia.ALTA, numero_linea="987654321")


# ─────────────────────────────────────────────────────────────────────────────
# Modelo simulado: devuelve un guion de resultados, uno por invocación
# ─────────────────────────────────────────────────────────────────────────────
class _Estructurado:
    def __init__(self, padre, esquema):
        self.padre = padre
        self.esquema = esquema

    def invoke(self, mensajes):
        # Guardamos una copia: el módulo muta la lista entre intentos y queremos
        # poder inspeccionar qué se envió en cada uno.
        self.padre.llamadas.append(list(mensajes))
        if not self.padre.guion:
            raise AssertionError("el guion del modelo simulado se agotó")
        siguiente = self.padre.guion.pop(0)
        if isinstance(siguiente, Exception):
            raise siguiente
        return siguiente


class ModeloFalso:
    """Imita lo justo de un chat model: `.with_structured_output(...).invoke(...)`.

    `guion` es la lista de resultados por invocación. Un elemento puede ser un
    objeto (se devuelve), `None` (se devuelve) o una excepción (se lanza).
    """

    def __init__(self, *guion):
        self.guion = list(guion)
        self.llamadas: list[list] = []
        self.esquema_recibido = None

    def with_structured_output(self, esquema):
        self.esquema_recibido = esquema
        return _Estructurado(self, esquema)


def _error_de_validacion() -> ValidationError:
    try:
        Intencion(categoria="AVERIA", urgencia="INVENTADA")
    except ValidationError as e:
        return e
    raise AssertionError("se esperaba un ValidationError")


print("\nCAMINO FELIZ")
m = ModeloFalso(VALIDO)
r = extraer_con_detalle(m, Intencion, "no tengo señal desde ayer")
chk("devuelve ResultadoEstructurado", isinstance(r, ResultadoEstructurado))
chk("los datos son la instancia del esquema", r.datos is VALIDO)
chk("un solo intento", r.intentos == 1, r.intentos)
chk("al_primer_intento es True", r.al_primer_intento is True)
chk("sin errores registrados", r.errores == [])
chk("una sola llamada al modelo", len(m.llamadas) == 1, len(m.llamadas))
chk("pasa el esquema a with_structured_output", m.esquema_recibido is Intencion)
chk("envía la entrada como mensaje de usuario",
    m.llamadas[0] == [{"role": "user", "content": "no tengo señal desde ayer"}])

print("\nREINTENTO TRAS UN FALLO")
m = ModeloFalso(None, VALIDO)
r = extraer_con_detalle(m, Intencion, "no tengo señal")
chk("None dispara el reintento y luego acierta", r.datos is VALIDO and r.intentos == 2, r.intentos)
chk("registra el error del primer intento", len(r.errores) == 1 and "None" in r.errores[0], r.errores)
chk("al_primer_intento es False", r.al_primer_intento is False)
segunda = m.llamadas[1]
chk("el reintento reenvía la entrada original", segunda[0]["content"] == "no tengo señal")
chk("el reintento añade la instrucción correctiva",
    len(segunda) == 2 and "no cumplió el formato" in segunda[1]["content"])
chk("la instrucción nombra los campos obligatorios",
    "categoria" in segunda[1]["content"] and "urgencia" in segunda[1]["content"])

print("\nOTRAS FORMAS DE FALLAR")
m = ModeloFalso(_error_de_validacion(), VALIDO)
r = extraer_con_detalle(m, Intencion, "x")
chk("ValidationError → reintenta y acierta", r.datos is VALIDO and r.intentos == 2)
chk("el error dice cuántos campos fallaron", "validación" in r.errores[0], r.errores[0])

m = ModeloFalso(Otra(valor=1), VALIDO)
r = extraer_con_detalle(m, Intencion, "x")
chk("tipo equivocado → reintenta y acierta", r.datos is VALIDO and r.intentos == 2)
chk("el error nombra ambos tipos",
    "Otra" in r.errores[0] and "Intencion" in r.errores[0], r.errores[0])

m = ModeloFalso(TimeoutError("el proveedor tardó demasiado"), VALIDO)
r = extraer_con_detalle(m, Intencion, "x")
chk("excepción del proveedor → reintenta y acierta", r.datos is VALIDO and r.intentos == 2)
chk("el error conserva el tipo de excepción", r.errores[0].startswith("TimeoutError:"), r.errores[0])

print("\nFALLO DEFINITIVO")
m = ModeloFalso(None, None)
try:
    extraer_con_detalle(m, Intencion, "x")
except ExtraccionFallida as e:
    chk("dos fallos → ExtraccionFallida", True, str(e)[:60])
    chk("el mensaje nombra el esquema", "Intencion" in str(e))
    chk("el mensaje cuenta los intentos", "2 intento" in str(e), str(e)[:70])
    chk("el mensaje acumula ambos errores", str(e).count("None") >= 2)
else:
    chk("dos fallos → ExtraccionFallida", False, "no lanzó la excepción")
chk("no reintenta más de lo pedido", len(m.llamadas) == 2, len(m.llamadas))

print("\nPRESUPUESTO DE REINTENTOS")
m = ModeloFalso(None, VALIDO)
try:
    extraer_con_detalle(m, Intencion, "x", reintentos=0)
    chk("reintentos=0 falla al primer error", False, "no lanzó la excepción")
except ExtraccionFallida:
    chk("reintentos=0 falla al primer error", True)
chk("reintentos=0 hace una sola llamada", len(m.llamadas) == 1, len(m.llamadas))

m = ModeloFalso(None, None, VALIDO)
r = extraer_con_detalle(m, Intencion, "x", reintentos=2)
chk("reintentos=2 permite un tercer intento", r.intentos == 3 and r.datos is VALIDO, r.intentos)

print("\nFEW-SHOT (regla A5)")
ejemplo = Intencion(categoria="FACTURACION", urgencia=Urgencia.BAJA)
m = ModeloFalso(VALIDO)
extraer_con_detalle(m, Intencion, "no tengo señal",
                    ejemplos=[("me cobraron de más", ejemplo)])
env = m.llamadas[0]
chk("el ejemplo va antes de la entrada", len(env) == 3 and env[2]["content"] == "no tengo señal", len(env))
chk("el ejemplo es un par user/assistant",
    env[0]["role"] == "user" and env[1]["role"] == "assistant")
chk("el assistant lleva el objeto serializado en JSON",
    '"categoria":"FACTURACION"' in env[1]["content"].replace(" ", ""), env[1]["content"][:60])

print("\nATAJO extraer()")
m = ModeloFalso(VALIDO)
chk("extraer() devuelve el objeto, no el detalle", extraer(m, Intencion, "x") is VALIDO)
m = ModeloFalso(None, None)
try:
    extraer(m, Intencion, "x")
    chk("extraer() propaga ExtraccionFallida", False, "no lanzó la excepción")
except ExtraccionFallida:
    chk("extraer() propaga ExtraccionFallida", True)

print("\nINSTRUCCIÓN CORRECTIVA")
txt = _instruccion_correctiva(Intencion, "urgencia: valor no permitido")
chk("incluye el error concreto", "urgencia: valor no permitido" in txt)
chk("no incluye los campos opcionales como obligatorios", "numero_linea" not in txt, txt[-80:])


class SinObligatorios(BaseModel):
    a: int = 0


chk("esquema sin campos obligatorios no rompe",
    "todos" in _instruccion_correctiva(SinObligatorios, "x"))

print("\n" + ("TODAS LAS VERIFICACIONES PASARON" if ok else "HAY FALLAS"))
sys.exit(0 if ok else 1)
