# Referencia de la API del simulador

> **Generado automáticamente** por `generar_referencia_api.py` ejecutando el
> simulador contra los datasets reales del curso. No editar a mano.

Todos los ejemplos de esta página son peticiones reales con respuestas reales.

## Antes de empezar

```bash
export SIM_BASE_URL="http://localhost:8000"   # o la URL de tu Space
export SIM_API_KEY="demo-key-0000"            # la clave de tu equipo
```

Todas las rutas de industria exigen la cabecera `X-API-Key`. Las rutas meta
(`/`, `/health`, `/fallos`, `/docs`) no la piden.

---

## Índice

| Industria | Rutas |
|-----------|-------|
| [Telecomunicaciones](#telecomunicaciones--andesmóvil) | 4 |
| [Banca](#banca--banco-inti) | 5 |
| [Retail](#retail--mercasur) | 5 |
| [Seguros](#seguros--andina-seguros) | 5 |
| [Meta y errores](#meta-y-manejo-de-errores) | 3 |

---

## Telecomunicaciones · AndesMóvil

#### `GET /telco/clientes/988837195`

Devuelve el titular, el plan contratado y el estado de la línea. El objeto `plan` viene anidado con las condiciones completas.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/telco/clientes/988837195"
```

**Respuesta** · `200`

```json
{
  "numero_linea": "988837195",
  "nombre_titular": "Iván Ramírez Rojas",
  "dni": "22707453",
  "plan_id": "AM-PRO-129",
  "plan_nombre": "Pro 129",
  "estado": "ACTIVO",
  "fecha_alta": "2025-10-07",
  "distrito": "Lince",
  "plan": {
    "plan_id": "AM-PRO-129",
    "nombre": "Pro 129",
    "precio_soles": 129.0,
    "gb_datos": 60,
    "minutos": "Ilimitados",
    "sms": "Ilimitados",
    "roaming_latam": true,
    "permanencia_meses": 18,
    "redes_sociales_libres": [
      "WhatsApp",
      "Facebook",
      "Instagram",
      "TikTok",
      "YouTube"
    ]
  }
}
```

#### `GET /telco/consumo/988837195?periodo=2026-08`

El parámetro `periodo` usa formato `AAAA-MM`. Si no existe, el 404 indica qué periodos sí tienen datos.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/telco/consumo/988837195?periodo=2026-08"
```

**Respuesta** · `200`

```json
{
  "numero_linea": "988837195",
  "periodo": "2026-08",
  "gb_consumidos": "24.88",
  "gb_incluidos": "60",
  "minutos_consumidos": "510",
  "sms_enviados": "42"
}
```

#### `GET /telco/cobertura/Miraflores`

`incidencia_activa` en `SI` significa que hay una avería general en la zona: explica por sí sola la falla que reporta el cliente.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/telco/cobertura/Miraflores"
```

**Respuesta** · `200`

```json
{
  "distrito": "Miraflores",
  "tecnologia": "4G/5G",
  "calidad_senal": "EXCELENTE",
  "incidencia_activa": "NO",
  "detalle_incidencia": "Saturación en hora punta"
}
```

#### `POST /telco/reclamos`

Registra un reclamo formal. El `ticket_id` es la constancia del cliente y **debe entregarse siempre**. Tipos válidos: `FACTURACION`, `CALIDAD_SERVICIO`, `AVERIA`, `PORTABILIDAD`, `CONTRATACION`, `SUSPENSION`.

**Petición**

```bash
curl -X POST -H "X-API-Key: $SIM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"numero_linea": "988837195", "tipo": "AVERIA", "descripcion": "Sin señal desde ayer"}' \
  "$SIM_BASE_URL/telco/reclamos"
```

**Respuesta** · `201`

```json
{
  "ticket_id": "REC-2026-00041",
  "estado": "ABIERTO",
  "plazo_dias_habiles": 30
}
```

---

## Banca · Banco Inti

#### `GET /banca/cuentas/191-9450993-0-54`

**El simulador nunca devuelve el DNI del titular.** La fuente ya viene saneada, así que los guardrails del L6 no parten de cero.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/banca/cuentas/191-9450993-0-54"
```

**Respuesta** · `200`

```json
{
  "numero_cuenta": "191-9450993-0-54",
  "titular": "Lucía Chávez Zegarra",
  "tipo_cuenta": "AHORROS",
  "moneda": "PEN",
  "saldo": "14375.51",
  "estado": "ACTIVA",
  "fecha_apertura": "2022-07-23"
}
```

#### `GET /banca/movimientos/191-9450993-0-54?dias=30`

`dias` acepta entre 1 y 90. *(Ejemplo recortado a 3 movimientos.)*

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/banca/movimientos/191-9450993-0-54?dias=30"
```

**Respuesta** · `200`

```json
{
  "numero_cuenta": "191-9450993-0-54",
  "dias": 30,
  "total": 2,
  "movimientos": [
    {
      "movimiento_id": "MOV-0000003",
      "numero_cuenta": "191-9450993-0-54",
      "fecha": "2026-08-25",
      "descripcion": "Transferencia P2P",
      "monto": "-251.48",
      "tipo": "CARGO",
      "canal": "APP",
      "ubicacion": "Lince"
    },
    {
      "movimiento_id": "MOV-0000006",
      "numero_cuenta": "191-9450993-0-54",
      "fecha": "2026-08-17",
      "descripcion": "StreamAndina",
      "monto": "-535.1",
      "tipo": "CARGO",
      "canal": "POS",
      "ubicacion": "Miraflores"
    }
  ]
}
```

#### `GET /banca/tarjetas/191-9450993-0-54`

Solo los **últimos 4 dígitos**, nunca el número completo. Si el equipo bloqueó la tarjeta, el estado aparece como `BLOQUEADA`.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/banca/tarjetas/191-9450993-0-54"
```

**Respuesta** · `200`

```json
{
  "numero_cuenta": "191-9450993-0-54",
  "tarjetas": [
    {
      "tarjeta_id": "TC-00001",
      "numero_cuenta": "191-9450993-0-54",
      "ultimos_4_digitos": "6738",
      "marca": "CLASICA",
      "estado": "BLOQUEADA",
      "linea_credito": "3500",
      "dia_facturacion": "10"
    }
  ]
}
```

#### `GET /banca/riesgo/MOV-0000001`

`nivel` es `ALTO` con puntaje ≥ 80, `MEDIO` entre 55 y 79, `BAJO` por debajo. Un riesgo ALTO exige derivación a un humano.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/banca/riesgo/MOV-0000001"
```

**Respuesta** · `200`

```json
{
  "movimiento": {
    "movimiento_id": "MOV-0000001",
    "numero_cuenta": "191-9450993-0-54",
    "fecha": "2026-06-29",
    "descripcion": "Farmacia Pacha",
    "monto": "-829.24",
    "tipo": "CARGO",
    "canal": "TRANSFERENCIA_DIFERIDA",
    "ubicacion": "San Juan de Lurigancho"
  },
  "alerta": null,
  "score_riesgo": 0,
  "nivel": "BAJO"
}
```

---

## Retail · MercaSur

#### `GET /retail/pedidos/MS-2026-00001`

Estados posibles: `EN_PREPARACION`, `EN_RUTA`, `ENTREGADO`, `LISTO_PARA_RECOJO`, `DEVUELTO`, `CANCELADO`.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/retail/pedidos/MS-2026-00001"
```

**Respuesta** · `200`

```json
{
  "pedido_id": "MS-2026-00001",
  "cliente": "José Paredes Vargas",
  "fecha_compra": "2026-07-26",
  "estado": "ENTREGADO",
  "sku": "MS-1040",
  "cantidad": "1",
  "total_soles": "1028.05",
  "courier": "Andes Courier",
  "codigo_tracking": "TRK96336983",
  "tienda_despacho": "MercaSur Norte",
  "distrito_entrega": "San Isidro"
}
```

#### `GET /retail/productos/MS-1001`

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/retail/productos/MS-1001"
```

**Respuesta** · `200`

```json
{
  "sku": "MS-1001",
  "nombre": "Laptop Pacha Basic",
  "categoria": "Tecnología",
  "marca": "Wayra",
  "precio_soles": "1517.05",
  "garantia_meses": "12",
  "permite_cambio": "SI"
}
```

#### `GET /retail/stock/MS-1001`

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/retail/stock/MS-1001"
```

**Respuesta** · `200`

```json
{
  "sku": "MS-1001",
  "total": 104,
  "por_tienda": [
    {
      "tienda": "MercaSur Surco",
      "stock_disponible": "33"
    },
    {
      "tienda": "MercaSur Norte",
      "stock_disponible": "34"
    },
    {
      "tienda": "MercaSur San Miguel",
      "stock_disponible": "16"
    },
    {
      "tienda": "MercaSur Salaverry",
      "stock_disponible": "9"
    },
    {
      "tienda": "MercaSur Sur",
      "stock_disponible": "8"
    },
    {
      "tienda": "Almacén Central MercaSur",
      "stock_disponible": "4"
    }
  ]
}
```

#### `POST /retail/devoluciones`

**Solo procede sobre pedidos `ENTREGADO`.** Si el pedido está en otro estado, el simulador devuelve `409` con la explicación.

**Petición**

```bash
curl -X POST -H "X-API-Key: $SIM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pedido_id": "MS-2026-00001", "motivo": "Llegó dañado", "tipo_solucion": "CAMBIO"}' \
  "$SIM_BASE_URL/retail/devoluciones"
```

**Respuesta** · `201`

```json
{
  "devolucion_id": "DEV-00031",
  "estado": "SOLICITADA",
  "sku": "MS-1040"
}
```

---

## Seguros · Andina Seguros

#### `GET /seguros/polizas/VEX-958`

`dias_para_vencer` viene calculado. Negativo significa vencida. Tampoco expone el DNI del titular.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/seguros/polizas/VEX-958"
```

**Respuesta** · `200`

```json
{
  "poliza_id": "SOAT-2026-00001",
  "placa": "VEX-958",
  "titular": "Ricardo Huamán Torres",
  "tipo_poliza": "SOAT",
  "inicio_vigencia": "2026-05-11",
  "fin_vigencia": "2027-05-11",
  "prima_soles": "107.5",
  "estado": "VIGENTE",
  "modalidad": "FISICO",
  "dias_para_vencer": 248
}
```

#### `GET /seguros/vehiculos/VEX-958`

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/seguros/vehiculos/VEX-958"
```

**Respuesta** · `200`

```json
{
  "placa": "VEX-958",
  "marca": "Toyota",
  "modelo": "Corolla",
  "anio": "2022",
  "categoria": "M1",
  "descripcion_categoria": "Automóvil particular hasta 9 asientos",
  "asientos": "5",
  "uso": "PARTICULAR"
}
```

#### `POST /seguros/siniestros`

`prioridad_alta` llega en `true` cuando hay lesionados: es la señal de que el agente **debe derivar al canal humano de inmediato**.

**Petición**

```bash
curl -X POST -H "X-API-Key: $SIM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"placa": "VEX-958", "tipo": "CHOQUE_SIMPLE", "distrito": "Ate", "cantidad_lesionados": 2}' \
  "$SIM_BASE_URL/seguros/siniestros"
```

**Respuesta** · `201`

```json
{
  "siniestro_id": "SIN-2026-00036",
  "poliza_id": "SOAT-2026-00001",
  "estado": "REPORTADO",
  "prioridad_alta": true,
  "plazo_pronunciamiento_dias": 30
}
```

#### `GET /seguros/siniestros/SIN-2026-00036`

Un equipo solo ve **sus propios** expedientes y los de la semilla.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/seguros/siniestros/SIN-2026-00036"
```

**Respuesta** · `200`

```json
{
  "siniestro_id": "SIN-2026-00036",
  "poliza_id": "SOAT-2026-00001",
  "placa": "VEX-958",
  "fecha_ocurrencia": "2026-09-05",
  "tipo": "CHOQUE_SIMPLE",
  "estado": "REPORTADO",
  "distrito": "Ate",
  "cantidad_lesionados": "2",
  "monto_estimado_soles": "0",
  "equipo": "demo"
}
```

#### `GET /seguros/clinicas?distrito=Ate`

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/seguros/clinicas?distrito=Ate"
```

**Respuesta** · `200`

```json
{
  "distrito": "Ate",
  "total": 1,
  "clinicas": [
    {
      "clinica": "Clínica Los Andes Este",
      "distrito": "Ate",
      "direccion": "Carretera Central km 6.5",
      "telefono": "01-500-1204",
      "atiende_24h": "SI"
    }
  ]
}
```

---

## Meta y manejo de errores

#### `GET /health`

No requiere API key. Úsala en el checklist previo a cada sesión.

**Petición**

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/health"
```

**Respuesta** · `200`

```json
{
  "estado": "ok",
  "version": "1.0.0",
  "clientes_telco": 50
}
```

### Códigos de error y qué debe hacer la tool

| Código | Significado | Qué debe hacer tu tool |
|--------|-------------|------------------------|
| `401` | Falta o es inválida la API key | Mensaje claro al agente. **Reintentar no sirve** |
| `404` | El recurso no existe | Devolver *"no existe X, verifica el dato"* |
| `409` | Conflicto de estado del negocio | Explicar la regla que se incumplió |
| `422` | Argumento inválido | Indicar los valores admitidos |
| `500` / `503` | Fallo del servicio | *"el sistema no responde, reintenta más tarde"* |
| *timeout* | El servicio no respondió | Cortar y avisar; nunca colgar el agente |

**Ejemplo de 401** (sin cabecera `X-API-Key`)

```json
{
  "detail": "Falta la cabecera X-API-Key. Cada equipo tiene su propia clave."
}
```

**Ejemplo de 404**

```json
{
  "detail": "No existe la línea 999999999"
}
```

### Provocar fallos a voluntad

Cualquier ruta acepta el parámetro `_fallo`. Existe para que puedas documentar
el escenario *"API caída"* que exige la Sesión 3 en vez de simularlo de mentira.

| Valor | Qué ocurre |
|-------|------------|
| `timeout` | El servicio tarda 30 segundos y el cliente debe cortar por timeout |
| `error500` | El servicio devuelve 500 Internal Server Error |
| `error503` | El servicio devuelve 503 Service Unavailable |
| `lento` | El servicio responde correctamente pero tarda 5 segundos |
| `vacio` | El servicio responde 200 con un cuerpo vacío |
| `malformado` | El servicio responde 200 con un JSON que no cumple el contrato |

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/telco/clientes/988837195?_fallo=error503"
```

Respuesta · `503`

```json
{
  "detail": "Service Unavailable (simulado). Reintenta en unos segundos."
}
```

---

## Nota sobre los datos

Todas las empresas son ficticias y todos los datos son sintéticos.
Los identificadores de los ejemplos provienen de los datasets del curso, así que
puedes copiarlos y ejecutarlos tal cual.
