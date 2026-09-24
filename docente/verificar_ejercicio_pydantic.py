# -*- coding: utf-8 -*-
"""Verificador del ejercicio obligatorio de Pydantic — pase de entrada de la Sesión 2.

Ejecutar desde la raíz del curso:

    python docente/verificar_ejercicio_pydantic.py --archivo entregas/equipo-01/reclamo.py

QUÉ VERIFICA
------------
El ejercicio de `00-preparacion/conceptos-previos/python-y-entorno.md`, sección
"Ejercicio obligatorio antes de la Sesión 2": un modelo Pydantic `Reclamo` con

    tipo: Enum(FACTURACION, AVERIA, PORTABILIDAD)
    descripcion: str, entre 10 y 200 caracteres
    numero_linea: exactamente 9 dígitos
    requiere_tecnico: bool, default False

POR QUÉ EXISTE
--------------
**Regla: sin este ejercicio entregado, el equipo no hace el L2** (recibe el
checkpoint y usa las 2 h de laboratorio para resolverlo). Con 15 equipos, revisar el
archivo a ojo no escala — y un `BaseModel` que "casi" cumple es peor que uno que no
compila: pasa desapercibido hasta que falla en la S3, con el Assignment A1 encima.

CÓDIGOS DE SALIDA
------------------
0 = las 4 restricciones están bien implementadas
1 = al menos una restricción falta o está mal implementada
2 = el archivo no existe, no define `Reclamo`, o no es un modelo Pydantic válido
"""
from __future__ import annotations

import argparse
import importlib.util
import pathlib
import sys

from pydantic import BaseModel, ValidationError


def cargar_reclamo(ruta: pathlib.Path) -> type[BaseModel]:
    if not ruta.exists():
        raise FileNotFoundError(f"No existe {ruta}")
    spec = importlib.util.spec_from_file_location("entrega_alumno", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "Reclamo"):
        raise ValueError(f"{ruta} no define una clase 'Reclamo'")
    reclamo = mod.Reclamo
    if not (isinstance(reclamo, type) and issubclass(reclamo, BaseModel)):
        raise ValueError(f"'Reclamo' en {ruta} no es una subclase de pydantic.BaseModel")
    return reclamo


def _construye(reclamo: type[BaseModel], **kwargs) -> tuple[bool, str]:
    """Intenta construir el modelo. Devuelve (ok, detalle_del_error_si_fallo)."""
    try:
        reclamo(**kwargs)
        return True, ""
    except ValidationError as e:
        return False, f"{e.error_count()} error(es) de validación"
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"


BASE_VALIDA = {
    "tipo": "AVERIA",
    "descripcion": "Se corta la llamada cada dos minutos.",
    "numero_linea": "987654321",
}


def verificar(reclamo: type[BaseModel]) -> list[tuple[str, bool, str]]:
    """Corre las comprobaciones. Devuelve (nombre, paso, detalle)."""
    resultados = []

    ok, detalle = _construye(reclamo, **BASE_VALIDA)
    resultados.append(("Un Reclamo válido se construye sin error", ok, detalle))

    ok, _ = _construye(reclamo, **{**BASE_VALIDA, "tipo": "SUSPENSION"})
    resultados.append(("`tipo` rechaza un valor fuera del Enum (FACTURACION/AVERIA/PORTABILIDAD)",
                       not ok, "aceptó 'SUSPENSION': el Enum no está restringido a los 3 valores"))

    ok, _ = _construye(reclamo, **{**BASE_VALIDA, "descripcion": "corta"})
    resultados.append(("`descripcion` rechaza menos de 10 caracteres",
                       not ok, "aceptó una descripción de 5 caracteres"))

    ok, _ = _construye(reclamo, **{**BASE_VALIDA, "descripcion": "x" * 201})
    resultados.append(("`descripcion` rechaza más de 200 caracteres",
                       not ok, "aceptó una descripción de 201 caracteres"))

    ok, _ = _construye(reclamo, **{**BASE_VALIDA, "numero_linea": "12345678"})
    resultados.append(("`numero_linea` rechaza 8 dígitos",
                       not ok, "aceptó un número de línea de 8 dígitos"))

    ok, _ = _construye(reclamo, **{**BASE_VALIDA, "numero_linea": "1234567890"})
    resultados.append(("`numero_linea` rechaza 10 dígitos",
                       not ok, "aceptó un número de línea de 10 dígitos"))

    ok, _ = _construye(reclamo, **{**BASE_VALIDA, "numero_linea": "98765432a"})
    resultados.append(("`numero_linea` rechaza caracteres no numéricos",
                       not ok, "aceptó un número de línea con una letra"))

    try:
        instancia = reclamo(**BASE_VALIDA)
        ok = instancia.requiere_tecnico is False
        detalle = "" if ok else f"el default es {instancia.requiere_tecnico!r}, no False"
    except Exception as e:  # noqa: BLE001
        ok, detalle = False, f"{type(e).__name__}: {e}"
    resultados.append(("`requiere_tecnico` es booleano con default False", ok, detalle))

    return resultados


def main() -> int:
    p = argparse.ArgumentParser(description="Verifica el ejercicio de Pydantic (pase de entrada S2)")
    p.add_argument("--archivo", required=True, metavar="RUTA",
                   help="ruta al .py del alumno que define la clase Reclamo")
    a = p.parse_args()

    ruta = pathlib.Path(a.archivo)
    print("\n" + "=" * 70)
    print("  VERIFICADOR DEL EJERCICIO DE PYDANTIC — pase de entrada de la Sesión 2")
    print("=" * 70)
    print(f"  Archivo: {ruta}")

    try:
        reclamo = cargar_reclamo(ruta)
    except (FileNotFoundError, ValueError) as e:
        print(f"\n  ERROR: {e}\n")
        return 2

    resultados = verificar(reclamo)
    print()
    ok_total = True
    for nombre, ok, detalle in resultados:
        marca = "[OK  ]" if ok else "[FALLA]"
        print(f"  {marca} {nombre}")
        if not ok and detalle:
            print(f"          {detalle}")
        ok_total = ok_total and ok

    print()
    if ok_total:
        print("  VEREDICTO: las 4 restricciones están bien implementadas. Pase de entrada superado.\n")
        return 0
    print("  VEREDICTO: hay restricciones sin implementar. Este equipo NO hace el L2 todavía:")
    print("  usa las 2 h de laboratorio para corregir el ejercicio con el checkpoint de la S1.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
