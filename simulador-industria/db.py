"""Base de datos del simulador de industria.

Carga los CSV/JSON sintéticos del curso en una base SQLite al arrancar, y aísla
las escrituras por equipo mediante una columna `equipo`.

Por qué SQLite y no un Postgres gestionado:
  - Cero infraestructura y cero cuentas nuevas para el alumno.
  - Los alumnos ven SQL real, que es el punto pedagógico.
  - El simulador se despliega como un único contenedor sin dependencias externas.

Los datos base son de SOLO LECTURA y compartidos por todos los equipos.
Lo que cada equipo crea (reclamos, devoluciones, siniestros, bloqueos) queda
aislado en su propio espacio de nombres.
"""

from __future__ import annotations

import csv
import json
import os
import sqlite3
import threading
from pathlib import Path

# El Dockerfile copia los datasets junto al simulador; en desarrollo se leen del repo.
DATASETS_DIR = Path(os.getenv("DATASETS_DIR", Path(__file__).parent.parent / "recursos" / "datasets"))
DB_PATH = os.getenv("DB_PATH", "/tmp/simulador.db")

_lock = threading.Lock()

# Tablas que se cargan desde CSV, por industria. El nombre de la tabla es
# <industria>_<archivo sin extensión>.
TABLAS_CSV: dict[str, list[str]] = {
    "telco": ["clientes", "consumo_datos", "cobertura_distritos", "tickets_reclamos"],
    "banca": ["cuentas", "movimientos", "tarjetas", "alertas_riesgo"],
    "retail": ["catalogo_productos", "stock_tiendas", "pedidos", "devoluciones"],
    "seguros": ["vehiculos", "polizas", "siniestros", "red_clinicas"],
}

# Carpeta real de cada industria dentro de recursos/datasets/
CARPETA = {
    "telco": "telecomunicaciones",
    "banca": "banca",
    "retail": "retail",
    "seguros": "seguros",
}

# Tablas donde los equipos escriben. Reciben una columna `equipo`.
TABLAS_ESCRITURA = {
    "telco_tickets_reclamos",
    "retail_devoluciones",
    "seguros_siniestros",
    "banca_bloqueos",
}


def conectar() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH, check_same_thread=False)
    con.row_factory = sqlite3.Row
    return con


def _crear_tabla_desde_csv(con: sqlite3.Connection, tabla: str, ruta: Path) -> int:
    with open(ruta, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    if not filas:
        return 0

    columnas = list(filas[0].keys())
    if tabla in TABLAS_ESCRITURA:
        columnas.append("equipo")

    cols_sql = ", ".join(f'"{c}" TEXT' for c in columnas)
    con.execute(f'DROP TABLE IF EXISTS "{tabla}"')
    con.execute(f'CREATE TABLE "{tabla}" ({cols_sql})')

    marcadores = ", ".join("?" for _ in columnas)
    for fila in filas:
        valores = [fila.get(c, "") for c in columnas]
        if tabla in TABLAS_ESCRITURA:
            valores[-1] = "_base"  # los datos semilla son de todos
        con.execute(f'INSERT INTO "{tabla}" VALUES ({marcadores})', valores)
    return len(filas)


def inicializar() -> dict[str, int]:
    """Reconstruye la base desde los datasets. Idempotente."""
    with _lock:
        con = conectar()
        resumen: dict[str, int] = {}

        for industria, archivos in TABLAS_CSV.items():
            carpeta = DATASETS_DIR / CARPETA[industria]
            for archivo in archivos:
                ruta = carpeta / f"{archivo}.csv"
                if not ruta.exists():
                    raise FileNotFoundError(
                        f"Falta {ruta}. Ejecuta: python recursos/datasets/generar_datasets.py"
                    )
                tabla = f"{industria}_{archivo}"
                resumen[tabla] = _crear_tabla_desde_csv(con, tabla, ruta)

        # Tabla propia del simulador: bloqueos de tarjeta (no existe como CSV)
        con.execute('DROP TABLE IF EXISTS "banca_bloqueos"')
        con.execute(
            'CREATE TABLE "banca_bloqueos" '
            '("bloqueo_id" TEXT, "tarjeta_id" TEXT, "fecha" TEXT, "equipo" TEXT)'
        )
        resumen["banca_bloqueos"] = 0

        # Los planes de telco viven en JSON, no en CSV
        planes = json.loads((DATASETS_DIR / "telecomunicaciones" / "planes.json").read_text(encoding="utf-8"))
        con.execute('DROP TABLE IF EXISTS "telco_planes"')
        con.execute('CREATE TABLE "telco_planes" ("plan_id" TEXT, "datos_json" TEXT)')
        for p in planes:
            con.execute('INSERT INTO "telco_planes" VALUES (?, ?)',
                        (p["plan_id"], json.dumps(p, ensure_ascii=False)))
        resumen["telco_planes"] = len(planes)

        con.commit()
        con.close()
        return resumen


# ─────────────────────────── consultas ───────────────────────────
def uno(sql: str, params: tuple = ()) -> dict | None:
    con = conectar()
    try:
        fila = con.execute(sql, params).fetchone()
        return dict(fila) if fila else None
    finally:
        con.close()


def varios(sql: str, params: tuple = ()) -> list[dict]:
    con = conectar()
    try:
        return [dict(f) for f in con.execute(sql, params).fetchall()]
    finally:
        con.close()


def escribir(sql: str, params: tuple = ()) -> None:
    with _lock:
        con = conectar()
        try:
            con.execute(sql, params)
            con.commit()
        finally:
            con.close()


def siguiente_id(tabla: str, campo: str, prefijo: str, equipo: str) -> str:
    """Correlativo por equipo: cada equipo tiene su propia numeración."""
    filas = varios(
        f'SELECT "{campo}" AS v FROM "{tabla}" WHERE equipo IN (?, "_base")', (equipo,)
    )
    numeros = []
    for f in filas:
        v = str(f["v"] or "")
        if v.startswith(prefijo) and v[len(prefijo):].isdigit():
            numeros.append(int(v[len(prefijo):]))
    return f"{prefijo}{(max(numeros) + 1 if numeros else 1):05d}"
