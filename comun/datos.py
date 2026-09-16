"""Capa de acceso a datos del curso.

Las tools del agente NO leen archivos ni llaman a APIs: piden los datos aquí.
Este módulo decide de dónde salen, según `DATA_SOURCE` en el `.env`:

    DATA_SOURCE=csv   → lee los datasets locales (Laboratorios 1 y 2)
    DATA_SOURCE=api   → consulta el simulador de industria (Laboratorio 3 en adelante)

Cambiar esa variable no obliga a tocar una sola línea de `domain_tools.py`.
Esa es la lección de arquitectura del Laboratorio 3, y es el mismo principio de
aislamiento que `provider.py` aplica al modelo.
"""

from __future__ import annotations

import csv
import json
from functools import lru_cache
from pathlib import Path

from . import settings as cfg

DATASETS_DIR = cfg.COURSE_ROOT / "recursos" / "datasets"


class DatoNoEncontrado(Exception):
    """El registro solicitado no existe.

    Las tools capturan esta excepción y devuelven un mensaje en lenguaje natural:
    un agente necesita leer 'no existe esa línea' para replantear su plan, no un
    stack trace que no sabe interpretar.
    """


class FuenteNoDisponible(Exception):
    """La fuente de datos falló (red, credencial, servicio caído).

    Es distinta de DatoNoEncontrado: aquí el dato podría existir, pero no se pudo
    consultar. La tool debe distinguirlas, porque el agente actúa distinto ante
    'no existe' que ante 'no pude consultar'.
    """


# ───────────────────────────── modo CSV ─────────────────────────────
@lru_cache(maxsize=None)
def _leer_csv(track: str, archivo: str) -> tuple[dict, ...]:
    ruta = DATASETS_DIR / track / archivo
    if not ruta.exists():
        raise FileNotFoundError(
            f"No existe {ruta}. Ejecuta: python recursos/datasets/generar_datasets.py"
        )
    with open(ruta, encoding="utf-8") as f:
        return tuple(csv.DictReader(f))


@lru_cache(maxsize=None)
def _leer_json(track: str, archivo: str) -> tuple:
    ruta = DATASETS_DIR / track / archivo
    if not ruta.exists():
        raise FileNotFoundError(f"No existe {ruta}")
    return tuple(json.loads(ruta.read_text(encoding="utf-8")))


def tabla(archivo: str, track: str | None = None) -> list[dict]:
    """Devuelve todas las filas de un archivo. Solo disponible en modo CSV."""
    t = track or cfg.COURSE_TRACK
    if archivo.endswith(".json"):
        return [dict(r) for r in _leer_json(t, archivo)]
    return [dict(r) for r in _leer_csv(t, archivo)]


# ───────────────────────── interfaz pública ─────────────────────────
def buscar_uno(archivo: str, campo: str, valor: str, track: str | None = None) -> dict:
    """Devuelve la primera fila cuyo `campo` coincide con `valor`.

    Raises:
        DatoNoEncontrado: si ninguna fila coincide.
        FuenteNoDisponible: si la fuente no se pudo consultar (solo en modo api).
    """
    t = track or cfg.COURSE_TRACK

    if cfg.DATA_SOURCE == "api":
        from . import api_client
        try:
            fila = api_client.buscar_uno(t, archivo, campo, str(valor))
        except api_client.SimuladorNoDisponible as e:
            raise FuenteNoDisponible(str(e)) from e
        except NotImplementedError:
            fila = None  # el simulador no expone esta ruta: se cae a CSV
        else:
            if fila is None:
                raise DatoNoEncontrado(f"No se encontró {campo}='{valor}' en {archivo}")
            return fila

    objetivo = str(valor).strip().upper()
    for fila in tabla(archivo, t):
        if str(fila.get(campo, "")).strip().upper() == objetivo:
            return fila
    raise DatoNoEncontrado(f"No se encontró {campo}='{valor}' en {archivo}")


def buscar_todos(archivo: str, campo: str, valor: str, track: str | None = None) -> list[dict]:
    """Devuelve todas las filas cuyo `campo` coincide con `valor`. Puede ser lista vacía."""
    t = track or cfg.COURSE_TRACK

    if cfg.DATA_SOURCE == "api":
        from . import api_client
        try:
            return api_client.buscar_todos(t, archivo, campo, str(valor))
        except api_client.SimuladorNoDisponible as e:
            raise FuenteNoDisponible(str(e)) from e
        except NotImplementedError:
            pass  # el simulador no expone esta ruta: se cae a CSV

    objetivo = str(valor).strip().upper()
    return [f for f in tabla(archivo, t)
            if str(f.get(campo, "")).strip().upper() == objetivo]


def documentos_rag(track: str | None = None) -> list[Path]:
    """Rutas de los documentos .md que se indexan en Qdrant (sesión 5).

    El corpus documental siempre sale de archivos: no pasa por el simulador,
    porque su destino es la base vectorial, no una consulta transaccional.
    """
    t = track or cfg.COURSE_TRACK
    return sorted((DATASETS_DIR / t).glob("*.md"))


def siguiente_id(archivo: str, campo: str, prefijo: str, track: str | None = None) -> str:
    """Genera el siguiente identificador correlativo de una tabla.

    En modo `api` el correlativo lo asigna el simulador, no el cliente: por eso
    las tools que escriben deben usar el identificador que devuelve la respuesta.
    """
    numeros = []
    for fila in tabla(archivo, track):
        valor = fila.get(campo, "")
        if valor.startswith(prefijo) and valor[len(prefijo):].isdigit():
            numeros.append(int(valor[len(prefijo):]))
    return f"{prefijo}{(max(numeros) + 1 if numeros else 1):05d}"


def describe_fuente() -> str:
    """Una línea legible para imprimir al inicio de cada laboratorio."""
    if cfg.DATA_SOURCE == "api":
        return f"Simulador de industria · {cfg.SIM_BASE_URL} · track={cfg.COURSE_TRACK}"
    return f"Datasets locales · {DATASETS_DIR} · track={cfg.COURSE_TRACK}"
