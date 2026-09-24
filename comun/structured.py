"""Salida estructurada fiable — la regla A3 convertida en código.

`with_structured_output()` con una clase Pydantic aplica validación del esquema.
Este wrapper administra errores de la integración y comprueba el contrato del
retorno. Validez estructural no implica exactitud semántica.

Este módulo añade lo que falta:

  1. **Comprueba** el tipo del resultado; la integración realiza la validación Pydantic.
  2. **Reintenta** una vez, devolviéndole al modelo el error concreto que cometió.
  3. **Falla con claridad** si el reintento tampoco sirve, en vez de propagar un
     `None` que reventará tres líneas más abajo.

Uso normal:

    from comun.structured import extraer

    intencion = extraer(get_chat_model(), Intencion, consulta_del_cliente)

Uso didáctico (Laboratorio 2), cuando quieres ver cuántos intentos hicieron falta:

    r = extraer_con_detalle(get_chat_model(), Intencion, consulta)
    print(f"{r.intentos} intento(s), errores: {r.errores}")
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)


class ExtraccionFallida(Exception):
    """El modelo no logró producir una salida válida ni tras el reintento.

    Las tools capturan esta excepción y devuelven un mensaje legible al agente:
    'no pude interpretar la consulta, ¿puedes reformularla?'. Nunca la dejan
    escapar, porque una excepción sin capturar rompe el bucle ReAct.
    """


@dataclass
class ResultadoEstructurado:
    """Resultado de la extracción, con la traza de lo que costó conseguirlo."""

    datos: BaseModel
    intentos: int
    errores: list[str] = field(default_factory=list)

    @property
    def al_primer_intento(self) -> bool:
        return self.intentos == 1


def _instruccion_correctiva(esquema: type[BaseModel], error: str) -> str:
    """Le dice al modelo qué hizo mal, con el esquema delante.

    Un reintento sin explicación repite el mismo error. Un reintento que nombra
    el campo y la restricción incumplida acierta la mayoría de las veces.
    """
    campos = ", ".join(esquema.model_json_schema().get("required", [])) or "todos"
    return (
        f"Tu respuesta anterior no cumplió el formato requerido.\n"
        f"Error: {error}\n"
        f"Campos obligatorios: {campos}\n"
        f"Devuelve ÚNICAMENTE el objeto pedido, con todos los campos obligatorios "
        f"y respetando los tipos y los valores permitidos de cada uno."
    )


def extraer_con_detalle(
    modelo,
    esquema: type[T],
    entrada: str,
    reintentos: int = 1,
    ejemplos: list[tuple[str, T]] | None = None,
) -> ResultadoEstructurado:
    """Extrae una estructura tipada, validando y reintentando si hace falta.

    Args:
        modelo: el chat model, normalmente de `get_chat_model()`.
        esquema: la clase Pydantic que describe la salida esperada.
        entrada: el texto del que se extrae.
        reintentos: cuántas veces reintentar tras un fallo. 1 es el presupuesto predeterminado
            del curso para acotar costo y latencia; el fallo final requiere diagnóstico.
        ejemplos: few-shot opcional (regla A5). Pares (texto, objeto esperado).
            Rinde especialmente cuando el esquema tiene enums o campos ambiguos.

    Returns:
        ResultadoEstructurado con los datos, el número de intentos y los errores.

    Raises:
        ExtraccionFallida: si ningún intento produjo una salida válida.
    """
    estructurado = modelo.with_structured_output(esquema)

    mensajes: list = []
    if ejemplos:
        for texto, esperado in ejemplos:
            mensajes.append({"role": "user", "content": texto})
            mensajes.append({"role": "assistant", "content": esperado.model_dump_json()})
    mensajes.append({"role": "user", "content": entrada})

    errores: list[str] = []

    for intento in range(1, reintentos + 2):
        try:
            salida = estructurado.invoke(mensajes)
        except ValidationError as e:
            error = f"validación: {e.error_count()} campo(s) inválido(s)"
        except Exception as e:  # noqa: BLE001 — el proveedor puede fallar de muchas formas
            error = f"{type(e).__name__}: {e}"
        else:
            if salida is None:
                error = "el modelo devolvió None en vez del objeto pedido"
            elif not isinstance(salida, esquema):
                error = f"devolvió {type(salida).__name__} en vez de {esquema.__name__}"
            else:
                return ResultadoEstructurado(datos=salida, intentos=intento, errores=errores)

        errores.append(error)
        if intento <= reintentos:
            # El reintento lleva la instrucción correctiva: repetir la misma
            # petición sin explicar el error produce el mismo error.
            mensajes.append({"role": "user",
                             "content": _instruccion_correctiva(esquema, error)})

    raise ExtraccionFallida(
        f"No se pudo extraer {esquema.__name__} tras {reintentos + 1} intento(s). "
        f"Errores: {' | '.join(errores)}"
    )


def extraer(
    modelo,
    esquema: type[T],
    entrada: str,
    reintentos: int = 1,
    ejemplos: list[tuple[str, T]] | None = None,
) -> T:
    """Igual que `extraer_con_detalle`, pero devuelve solo el objeto.

    Es la forma que usarás en el 90 % de los casos.
    """
    return extraer_con_detalle(modelo, esquema, entrada, reintentos, ejemplos).datos  # type: ignore[return-value]
