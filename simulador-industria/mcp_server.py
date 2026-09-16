"""Servidor MCP del simulador de industria.

Expone las 6 herramientas OPCIONALES de los 4 tracks (las que en el curso quedan
como reto del Laboratorio 4) a través del Model Context Protocol.

Se ejecuta de dos formas, a propósito, para que el alumno compare los transportes:

  1. stdio — el agente lanza este archivo como subproceso:
         python mcp_server.py

  2. HTTP  — el mismo servidor montado dentro del simulador FastAPI:
         https://<space>.hf.space/mcp

La lección del Laboratorio 4 es que el agente NO nota la diferencia: son las
mismas herramientas, descubiertas en tiempo de ejecución, y solo cambia por dónde
viajan los mensajes.

| Transporte | Dónde corre | Cuándo conviene |
|------------|-------------|-----------------|
| stdio      | Subproceso local | Herramientas propias, sin red, un solo usuario |
| HTTP       | Servicio remoto  | Herramientas compartidas por varios agentes y equipos |
"""

from __future__ import annotations

from datetime import date

from mcp.server.fastmcp import FastMCP

import db

HOY = date(2026, 9, 5)

mcp = FastMCP("simulador-industria")


# ─────────────────────────── telecomunicaciones ───────────────────────────
@mcp.tool()
def check_portability_eligibility(numero_linea: str) -> str:
    """Verifica si una línea móvil puede portarse a otra operadora.

    Úsala cuando el cliente pregunte por portabilidad o por llevarse su número.
    NO la uses para ejecutar la portabilidad: esta herramienta solo evalúa.
    """
    fila = db.uno("SELECT * FROM telco_clientes WHERE numero_linea = ?", (numero_linea,))
    if not fila:
        return f"No existe la línea {numero_linea}."
    if fila["estado"] == "BAJA":
        return f"La línea {numero_linea} está dada de BAJA y no es portable."
    return (f"La línea {numero_linea} ES PORTABLE (estado {fila['estado']}, plan "
            f"{fila['plan_nombre']}). Una deuda pendiente NO impide la portabilidad, "
            f"aunque sigue siendo exigible. Plazo de ejecución: 24 horas.")


@mcp.tool()
def get_coverage_by_district(distrito: str) -> str:
    """Consulta la cobertura móvil y las incidencias activas de un distrito.

    Úsala cuando el cliente pregunte por la cobertura de una zona.
    NO la uses para diagnosticar una línea concreta.
    """
    fila = db.uno("SELECT * FROM telco_cobertura_distritos WHERE UPPER(distrito) = UPPER(?)", (distrito,))
    if not fila:
        return f"No hay información de cobertura para '{distrito}'."
    inc = (f"INCIDENCIA ACTIVA: {fila['detalle_incidencia']}"
           if fila["incidencia_activa"] == "SI" else "Sin incidencias")
    return (f"Cobertura en {fila['distrito']}: tecnología {fila['tecnologia']} · "
            f"calidad {fila['calidad_senal']} · {inc}")


# ─────────────────────────────── banca ───────────────────────────────
@mcp.tool()
def get_transfer_limits(numero_cuenta: str) -> str:
    """Devuelve los límites de transferencia vigentes de una cuenta.

    Úsala cuando el cliente pregunte cuánto puede transferir al día.
    NO la uses para ejecutar transferencias: el asistente nunca mueve dinero.
    """
    fila = db.uno("SELECT * FROM banca_cuentas WHERE numero_cuenta = ?", (numero_cuenta,))
    if not fila:
        return f"No existe la cuenta {numero_cuenta}."
    limites = {"AHORROS": (3000, 10000), "SUELDO": (5000, 15000), "CORRIENTE": (10000, 50000)}
    diario, mensual = limites.get(fila["tipo_cuenta"], (3000, 10000))
    return (f"Cuenta {numero_cuenta} ({fila['tipo_cuenta']}): límite diario S/ {diario:,} · "
            f"límite mensual S/ {mensual:,} · billetera IntiPay hasta S/ 500 diarios.")


# ─────────────────────────────── retail ───────────────────────────────
@mcp.tool()
def estimate_delivery(distrito: str, monto_compra: float) -> str:
    """Calcula el costo y el plazo de despacho para un distrito y un monto.

    Úsala cuando el cliente pregunte cuánto cuesta el envío antes de comprar.
    NO la uses para consultar un pedido ya realizado.
    """
    lima = {"MIRAFLORES", "SAN ISIDRO", "SANTIAGO DE SURCO", "LA MOLINA", "SAN BORJA",
            "JESÚS MARÍA", "LINCE", "MAGDALENA DEL MAR", "PUEBLO LIBRE", "SAN MIGUEL",
            "COMAS", "SAN JUAN DE LURIGANCHO", "VILLA EL SALVADOR", "ATE", "CALLAO",
            "CHORRILLOS", "BARRANCO", "SURQUILLO", "LOS OLIVOS", "INDEPENDENCIA"}
    es_lima = distrito.strip().upper() in lima
    umbral, costo, plazo = ((149.0, 12.90, "3 a 5 días hábiles") if es_lima
                            else (299.0, 24.90, "5 a 9 días hábiles"))
    zona = "Lima Metropolitana y Callao" if es_lima else "provincias"
    if monto_compra >= umbral:
        return f"Despacho a {distrito} ({zona}): GRATUITO por superar S/ {umbral:.2f}. Plazo: {plazo}."
    return (f"Despacho a {distrito} ({zona}): S/ {costo:.2f}. Plazo: {plazo}. "
            f"Con S/ {umbral - monto_compra:.2f} más sería gratuito.")


# ─────────────────────────────── seguros ───────────────────────────────
@mcp.tool()
def list_affiliated_clinics(distrito: str) -> str:
    """Lista las clínicas de la red afiliada en un distrito.

    Úsala cuando el cliente pregunte dónde atenderse o a qué clínica llevar a un lesionado.
    NO la uses para consultar coberturas ni montos.
    """
    filas = db.varios("SELECT * FROM seguros_red_clinicas WHERE UPPER(distrito) = UPPER(?)", (distrito,))
    if not filas:
        todas = db.varios("SELECT clinica, distrito FROM seguros_red_clinicas LIMIT 4")
        opciones = " · ".join(f"{c['clinica']} ({c['distrito']})" for c in todas)
        return (f"No hay clínicas afiliadas en {distrito}. Otras opciones: {opciones}. "
                f"Ante una emergencia, cualquier establecimiento debe atender sin exigir pago.")
    return "\n".join(
        f"{c['clinica']} · {c['direccion']}, {c['distrito']} · Tel. {c['telefono']} · "
        f"{'Atiende 24 horas' if c['atiende_24h'] == 'SI' else 'Horario diurno'}"
        for c in filas
    )


@mcp.tool()
def get_vehicle_info(placa: str) -> str:
    """Devuelve los datos del vehículo registrado bajo una placa.

    Úsala para confirmar categoría, año o uso antes de cotizar.
    NO la uses si solo preguntan por la vigencia de la póliza.
    """
    fila = db.uno("SELECT * FROM seguros_vehiculos WHERE UPPER(placa) = UPPER(?)", (placa,))
    if not fila:
        return f"No hay datos del vehículo con placa {placa}."
    return (f"Placa {fila['placa']} · {fila['marca']} {fila['modelo']} {fila['anio']} · "
            f"Categoría {fila['categoria']} ({fila['descripcion_categoria']}) · "
            f"{fila['asientos']} asientos · Uso: {fila['uso']}")


if __name__ == "__main__":
    # Transporte stdio: el agente lanza este archivo como subproceso.
    db.inicializar()
    mcp.run(transport="stdio")
