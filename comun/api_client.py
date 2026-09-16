"""Cliente HTTP del simulador de industria.

Traduce las consultas genéricas de `datos.py` a las rutas REST del simulador.
Ninguna tool usa este módulo directamente: lo hace `datos.py` cuando
`DATA_SOURCE=api` en el `.env`.

Por qué existe esta capa
------------------------
El simulador expone recursos (`/telco/clientes/{linea}`), mientras que las tools
piden filas (`buscar_uno("clientes.csv", "numero_linea", X)`). Este módulo hace
la traducción, y por eso el alumno puede cambiar `DATA_SOURCE=csv` por
`DATA_SOURCE=api` sin editar una sola línea de sus herramientas.

Esa es la lección del Laboratorio 3.
"""

from __future__ import annotations

import httpx

from . import settings as cfg

# (track, archivo, campo de búsqueda) → plantilla de ruta
RUTAS: dict[tuple[str, str, str], str] = {
    ("telecomunicaciones", "clientes.csv", "numero_linea"): "/telco/clientes/{valor}",
    ("telecomunicaciones", "cobertura_distritos.csv", "distrito"): "/telco/cobertura/{valor}",
    ("banca", "cuentas.csv", "numero_cuenta"): "/banca/cuentas/{valor}",
    ("banca", "movimientos.csv", "movimiento_id"): "/banca/riesgo/{valor}",
    ("retail", "pedidos.csv", "pedido_id"): "/retail/pedidos/{valor}",
    ("retail", "catalogo_productos.csv", "sku"): "/retail/productos/{valor}",
    ("seguros", "polizas.csv", "placa"): "/seguros/polizas/{valor}",
    ("seguros", "vehiculos.csv", "placa"): "/seguros/vehiculos/{valor}",
    ("seguros", "siniestros.csv", "siniestro_id"): "/seguros/siniestros/{valor}",
}

# Rutas que devuelven listas, con la clave del array dentro de la respuesta
RUTAS_LISTA: dict[tuple[str, str, str], tuple[str, str]] = {
    ("banca", "movimientos.csv", "numero_cuenta"): ("/banca/movimientos/{valor}?dias=90", "movimientos"),
    ("banca", "tarjetas.csv", "numero_cuenta"): ("/banca/tarjetas/{valor}", "tarjetas"),
    ("retail", "stock_tiendas.csv", "sku"): ("/retail/stock/{valor}", "por_tienda"),
    ("retail", "devoluciones.csv", "pedido_id"): ("/retail/devoluciones?pedido_id={valor}", "devoluciones"),
    ("seguros", "red_clinicas.csv", "distrito"): ("/seguros/clinicas?distrito={valor}", "clinicas"),
}


class SimuladorNoDisponible(Exception):
    """El simulador no respondió. Las tools lo traducen a un mensaje para el agente."""


def _cliente() -> httpx.Client:
    base = cfg.require("SIM_BASE_URL", cfg.SIM_BASE_URL).rstrip("/")
    return httpx.Client(
        base_url=base,
        headers={"X-API-Key": cfg.require("SIM_API_KEY", cfg.SIM_API_KEY)},
        timeout=cfg.SIM_TIMEOUT,
    )


def _pedir(ruta: str) -> dict | None:
    """Hace la petición y traduce los errores HTTP a algo que una tool pueda explicar."""
    try:
        with _cliente() as c:
            r = c.get(ruta)
    except httpx.TimeoutException as e:
        raise SimuladorNoDisponible(
            "El servicio del simulador no respondió a tiempo. Informa al usuario que "
            "el sistema está lento e invítalo a reintentar."
        ) from e
    except httpx.HTTPError as e:
        raise SimuladorNoDisponible(
            f"No se pudo contactar al simulador ({type(e).__name__}). "
            f"Verifica SIM_BASE_URL en tu .env."
        ) from e

    if r.status_code == 404:
        return None
    if r.status_code == 401:
        raise SimuladorNoDisponible(
            "Credencial rechazada por el simulador (401). Verifica SIM_API_KEY en tu .env. "
            "Reintentar no soluciona un 401."
        )
    if r.status_code >= 500:
        raise SimuladorNoDisponible(
            f"El simulador devolvió {r.status_code}. Es un fallo del servicio, no del dato. "
            f"Informa al usuario y sugiere reintentar más tarde."
        )
    r.raise_for_status()
    return r.json()


def buscar_uno(track: str, archivo: str, campo: str, valor: str) -> dict | None:
    clave = (track, archivo, campo)
    if clave not in RUTAS:
        raise NotImplementedError(
            f"El simulador no expone {archivo} por {campo}. "
            f"Usa DATA_SOURCE=csv para este dato, o agrega la ruta en api_client.RUTAS."
        )
    return _pedir(RUTAS[clave].format(valor=valor))


def buscar_todos(track: str, archivo: str, campo: str, valor: str) -> list[dict]:
    clave = (track, archivo, campo)
    if clave not in RUTAS_LISTA:
        raise NotImplementedError(
            f"El simulador no expone listas de {archivo} por {campo}. "
            f"Usa DATA_SOURCE=csv para este dato."
        )
    plantilla, llave = RUTAS_LISTA[clave]
    cuerpo = _pedir(plantilla.format(valor=valor))
    if not cuerpo:
        return []
    return cuerpo.get(llave, [])


def salud() -> dict:
    """Comprueba que el simulador está vivo. No requiere API key."""
    base = cfg.require("SIM_BASE_URL", cfg.SIM_BASE_URL).rstrip("/")
    with httpx.Client(base_url=base, timeout=cfg.SIM_TIMEOUT) as c:
        return c.get("/health").json()
