"""Rutas REST de las 4 industrias simuladas.

Los cuatro routers viven en un mismo archivo a propósito: puestos en paralelo se
ve que las cuatro industrias tienen la misma forma —consultar, listar, crear— y
que lo único que cambia es el dominio. Esa simetría es la que permite que el
esqueleto de código de los 4 tracks del curso sea idéntico.

Convenciones comunes a todas las rutas:
  · Cabecera `X-API-Key` obligatoria.
  · Parámetro opcional `_fallo` para provocar errores (ver chaos.py).
  · 404 con mensaje explicativo cuando el recurso no existe.
  · Las escrituras quedan aisladas por equipo.
"""

from __future__ import annotations

import json
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

import chaos
import db
from auth import equipo_actual

HOY = date(2026, 9, 5)


def _fallo_param(_fallo: str | None = Query(default=None, description="Provoca un fallo simulado")):
    return _fallo


# ═══════════════════════════ TELECOMUNICACIONES ═══════════════════════════
telco = APIRouter(prefix="/telco", tags=["AndesMóvil · telecomunicaciones"])


class ReclamoIn(BaseModel):
    numero_linea: str = Field(description="Línea de 9 dígitos")
    tipo: str = Field(description="FACTURACION, CALIDAD_SERVICIO, AVERIA, PORTABILIDAD, CONTRATACION o SUSPENSION")
    descripcion: str = Field(max_length=300)


@telco.get("/clientes/{numero_linea}")
async def telco_cliente(numero_linea: str, equipo: str = Depends(equipo_actual),
                        _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM telco_clientes WHERE numero_linea = ?', (numero_linea,))
    if not fila:
        raise HTTPException(404, f"No existe la línea {numero_linea}")
    plan = db.uno('SELECT datos_json FROM telco_planes WHERE plan_id = ?', (fila["plan_id"],))
    fila["plan"] = json.loads(plan["datos_json"]) if plan else None
    return fila


@telco.get("/consumo/{numero_linea}")
async def telco_consumo(numero_linea: str, periodo: str = "2026-08",
                        equipo: str = Depends(equipo_actual),
                        _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM telco_consumo_datos WHERE numero_linea = ? AND periodo = ?',
                  (numero_linea, periodo))
    if not fila:
        disponibles = db.varios('SELECT DISTINCT periodo FROM telco_consumo_datos WHERE numero_linea = ?',
                                (numero_linea,))
        raise HTTPException(404, f"Sin consumo para {numero_linea} en {periodo}. "
                                 f"Periodos: {[d['periodo'] for d in disponibles]}")
    return fila


@telco.get("/cobertura/{distrito}")
async def telco_cobertura(distrito: str, equipo: str = Depends(equipo_actual),
                          _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM telco_cobertura_distritos WHERE UPPER(distrito) = UPPER(?)', (distrito,))
    if not fila:
        raise HTTPException(404, f"Sin datos de cobertura para {distrito}")
    return fila


@telco.post("/reclamos", status_code=201)
async def telco_crear_reclamo(cuerpo: ReclamoIn, equipo: str = Depends(equipo_actual),
                              _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    validos = {"FACTURACION", "CALIDAD_SERVICIO", "AVERIA", "PORTABILIDAD", "CONTRATACION", "SUSPENSION"}
    if cuerpo.tipo.upper() not in validos:
        raise HTTPException(422, f"Tipo inválido. Debe ser uno de: {sorted(validos)}")
    if not db.uno('SELECT 1 FROM telco_clientes WHERE numero_linea = ?', (cuerpo.numero_linea,)):
        raise HTTPException(404, f"No existe la línea {cuerpo.numero_linea}")
    ticket = db.siguiente_id("telco_tickets_reclamos", "ticket_id", "REC-2026-", equipo)
    db.escribir(
        'INSERT INTO telco_tickets_reclamos VALUES (?,?,?,?,?,?,?)',
        (ticket, cuerpo.numero_linea, cuerpo.tipo.upper(), HOY.isoformat(), "ABIERTO", "OSI-SIMUL", equipo),
    )
    return {"ticket_id": ticket, "estado": "ABIERTO", "plazo_dias_habiles": 30}


# ═══════════════════════════════ BANCA ═══════════════════════════════
banca = APIRouter(prefix="/banca", tags=["Banco Inti · banca"])


@banca.get("/cuentas/{numero_cuenta}")
async def banca_cuenta(numero_cuenta: str, equipo: str = Depends(equipo_actual),
                       _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM banca_cuentas WHERE numero_cuenta = ?', (numero_cuenta,))
    if not fila:
        raise HTTPException(404, f"No existe la cuenta {numero_cuenta}")
    fila.pop("dni", None)  # el simulador nunca expone el DNI completo
    return fila


@banca.get("/movimientos/{numero_cuenta}")
async def banca_movimientos(numero_cuenta: str, dias: int = Query(default=30, ge=1, le=90),
                            equipo: str = Depends(equipo_actual),
                            _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    if not db.uno('SELECT 1 FROM banca_cuentas WHERE numero_cuenta = ?', (numero_cuenta,)):
        raise HTTPException(404, f"No existe la cuenta {numero_cuenta}")
    corte = (HOY.toordinal() - dias)
    filas = db.varios('SELECT * FROM banca_movimientos WHERE numero_cuenta = ? ORDER BY fecha DESC',
                      (numero_cuenta,))
    filas = [f for f in filas if date.fromisoformat(f["fecha"]).toordinal() >= corte]
    return {"numero_cuenta": numero_cuenta, "dias": dias, "total": len(filas), "movimientos": filas}


@banca.get("/tarjetas/{numero_cuenta}")
async def banca_tarjetas(numero_cuenta: str, equipo: str = Depends(equipo_actual),
                         _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    filas = db.varios('SELECT * FROM banca_tarjetas WHERE numero_cuenta = ?', (numero_cuenta,))
    bloqueos = {b["tarjeta_id"] for b in
                db.varios('SELECT tarjeta_id FROM banca_bloqueos WHERE equipo = ?', (equipo,))}
    for f in filas:
        if f["tarjeta_id"] in bloqueos:
            f["estado"] = "BLOQUEADA"
    return {"numero_cuenta": numero_cuenta, "tarjetas": filas}


@banca.get("/riesgo/{movimiento_id}")
async def banca_riesgo(movimiento_id: str, equipo: str = Depends(equipo_actual),
                       _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    mov = db.uno('SELECT * FROM banca_movimientos WHERE movimiento_id = ?', (movimiento_id,))
    if not mov:
        raise HTTPException(404, f"No existe el movimiento {movimiento_id}")
    alerta = db.uno('SELECT * FROM banca_alertas_riesgo WHERE movimiento_id = ?', (movimiento_id,))
    score = int(alerta["score_riesgo"]) if alerta else 0
    return {"movimiento": mov, "alerta": alerta, "score_riesgo": score,
            "nivel": "ALTO" if score >= 80 else "MEDIO" if score >= 55 else "BAJO"}


@banca.post("/bloqueos", status_code=201)
async def banca_bloquear(tarjeta_id: str, equipo: str = Depends(equipo_actual),
                         _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    if not db.uno('SELECT 1 FROM banca_tarjetas WHERE tarjeta_id = ?', (tarjeta_id,)):
        raise HTTPException(404, f"No existe la tarjeta {tarjeta_id}")
    bid = db.siguiente_id("banca_bloqueos", "bloqueo_id", "BLQ-", equipo)
    db.escribir('INSERT INTO banca_bloqueos VALUES (?,?,?,?)',
                (bid, tarjeta_id, HOY.isoformat(), equipo))
    return {"bloqueo_id": bid, "tarjeta_id": tarjeta_id, "irreversible": True}


# ═══════════════════════════════ RETAIL ═══════════════════════════════
retail = APIRouter(prefix="/retail", tags=["MercaSur · retail"])


class DevolucionIn(BaseModel):
    pedido_id: str
    motivo: str = Field(max_length=200)
    tipo_solucion: str = Field(default="CAMBIO", description="CAMBIO, REEMBOLSO o NOTA_CREDITO")


@retail.get("/pedidos/{pedido_id}")
async def retail_pedido(pedido_id: str, equipo: str = Depends(equipo_actual),
                        _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM retail_pedidos WHERE pedido_id = ?', (pedido_id,))
    if not fila:
        raise HTTPException(404, f"No existe el pedido {pedido_id}")
    return fila


@retail.get("/productos/{sku}")
async def retail_producto(sku: str, equipo: str = Depends(equipo_actual),
                          _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM retail_catalogo_productos WHERE sku = ?', (sku,))
    if not fila:
        raise HTTPException(404, f"No existe el producto {sku}")
    return fila


@retail.get("/stock/{sku}")
async def retail_stock(sku: str, equipo: str = Depends(equipo_actual),
                       _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    filas = db.varios('SELECT tienda, stock_disponible FROM retail_stock_tiendas WHERE sku = ?', (sku,))
    if not filas:
        raise HTTPException(404, f"Sin información de stock para {sku}")
    total = sum(int(f["stock_disponible"]) for f in filas)
    return {"sku": sku, "total": total, "por_tienda": filas}


@retail.post("/devoluciones", status_code=201)
async def retail_devolucion(cuerpo: DevolucionIn, equipo: str = Depends(equipo_actual),
                            _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    ped = db.uno('SELECT * FROM retail_pedidos WHERE pedido_id = ?', (cuerpo.pedido_id,))
    if not ped:
        raise HTTPException(404, f"No existe el pedido {cuerpo.pedido_id}")
    if ped["estado"] != "ENTREGADO":
        raise HTTPException(409, f"El pedido está en estado {ped['estado']}, no ENTREGADO. "
                                 f"No corresponde una devolución.")
    validos = {"CAMBIO", "REEMBOLSO", "NOTA_CREDITO"}
    if cuerpo.tipo_solucion.upper() not in validos:
        raise HTTPException(422, f"Tipo de solución inválido. Debe ser uno de: {sorted(validos)}")
    dev = db.siguiente_id("retail_devoluciones", "devolucion_id", "DEV-", equipo)
    db.escribir('INSERT INTO retail_devoluciones VALUES (?,?,?,?,?,?,?,?)',
                (dev, cuerpo.pedido_id, ped["sku"], cuerpo.motivo, "SOLICITADA",
                 HOY.isoformat(), cuerpo.tipo_solucion.upper(), equipo))
    return {"devolucion_id": dev, "estado": "SOLICITADA", "sku": ped["sku"]}


@retail.get("/devoluciones")
async def retail_listar_devoluciones(pedido_id: str, equipo: str = Depends(equipo_actual),
                                     _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    filas = db.varios('SELECT * FROM retail_devoluciones WHERE pedido_id = ? AND equipo IN (?, "_base")',
                      (pedido_id, equipo))
    return {"pedido_id": pedido_id, "devoluciones": filas}


# ═══════════════════════════════ SEGUROS ═══════════════════════════════
seguros = APIRouter(prefix="/seguros", tags=["Andina Seguros · seguros"])


class SiniestroIn(BaseModel):
    placa: str
    tipo: str = Field(description="CHOQUE_SIMPLE, ATROPELLO, VOLCADURA, COLISION_MULTIPLE o DESPISTE")
    distrito: str
    cantidad_lesionados: int = Field(ge=0, le=20)


@seguros.get("/polizas/{placa}")
async def seguros_poliza(placa: str, equipo: str = Depends(equipo_actual),
                         _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM seguros_polizas WHERE UPPER(placa) = UPPER(?)', (placa,))
    if not fila:
        raise HTTPException(404, f"No hay póliza para la placa {placa}")
    fila.pop("dni", None)
    fila["dias_para_vencer"] = date.fromisoformat(fila["fin_vigencia"]).toordinal() - HOY.toordinal()
    return fila


@seguros.get("/vehiculos/{placa}")
async def seguros_vehiculo(placa: str, equipo: str = Depends(equipo_actual),
                           _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM seguros_vehiculos WHERE UPPER(placa) = UPPER(?)', (placa,))
    if not fila:
        raise HTTPException(404, f"No hay datos del vehículo {placa}")
    return fila


@seguros.get("/siniestros/{siniestro_id}")
async def seguros_siniestro(siniestro_id: str, equipo: str = Depends(equipo_actual),
                            _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    fila = db.uno('SELECT * FROM seguros_siniestros WHERE siniestro_id = ? AND equipo IN (?, "_base")',
                  (siniestro_id, equipo))
    if not fila:
        raise HTTPException(404, f"No existe el expediente {siniestro_id}")
    return fila


@seguros.post("/siniestros", status_code=201)
async def seguros_abrir_siniestro(cuerpo: SiniestroIn, equipo: str = Depends(equipo_actual),
                                  _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    validos = {"CHOQUE_SIMPLE", "ATROPELLO", "VOLCADURA", "COLISION_MULTIPLE", "DESPISTE"}
    if cuerpo.tipo.upper() not in validos:
        raise HTTPException(422, f"Tipo inválido. Debe ser uno de: {sorted(validos)}")
    pol = db.uno('SELECT * FROM seguros_polizas WHERE UPPER(placa) = UPPER(?)', (cuerpo.placa,))
    if not pol:
        raise HTTPException(404, f"No hay póliza para la placa {cuerpo.placa}")
    if date.fromisoformat(pol["fin_vigencia"]) < HOY:
        raise HTTPException(409, f"La póliza venció el {pol['fin_vigencia']}. Sin cobertura.")
    exp = db.siguiente_id("seguros_siniestros", "siniestro_id", "SIN-2026-", equipo)
    db.escribir('INSERT INTO seguros_siniestros VALUES (?,?,?,?,?,?,?,?,?,?)',
                (exp, pol["poliza_id"], cuerpo.placa.upper(), HOY.isoformat(), cuerpo.tipo.upper(),
                 "REPORTADO", cuerpo.distrito, str(cuerpo.cantidad_lesionados), "0", equipo))
    return {"siniestro_id": exp, "poliza_id": pol["poliza_id"], "estado": "REPORTADO",
            "prioridad_alta": cuerpo.cantidad_lesionados > 0,
            "plazo_pronunciamiento_dias": 30}


@seguros.get("/clinicas")
async def seguros_clinicas(distrito: str | None = None, equipo: str = Depends(equipo_actual),
                           _fallo: str | None = Depends(_fallo_param)):
    if (alt := await chaos.aplicar(_fallo)) is not None:
        return alt
    if distrito:
        filas = db.varios('SELECT * FROM seguros_red_clinicas WHERE UPPER(distrito) = UPPER(?)', (distrito,))
    else:
        filas = db.varios('SELECT * FROM seguros_red_clinicas')
    return {"distrito": distrito, "total": len(filas), "clinicas": filas}


ROUTERS = [telco, banca, retail, seguros]
