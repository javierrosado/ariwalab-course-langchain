# L4 · Retail — MercaSur

Sigue las 4 partes de [`../README.md`](../README.md). Esto es lo específico de tu track.

## Tus 3 tools nuevas

| Tool | Dataset que consulta | Nota |
|---|---|---|
| `get_product_details` | `catalogo_productos.csv` | Precio, garantía y si el producto admite cambio por libre voluntad |
| `check_stock_by_store` | `stock_tiendas.csv` | Devuelve el stock por tienda; si todas están en 0, dilo explícitamente |
| `start_return_request` **(escritura)** | `devoluciones.csv` | Solo si el pedido está `ENTREGADO`. Genera un código `DEV-NNNNN`. **Exige confirmación** antes de registrar la solicitud, y no aprueba nada: solo registra |

## Qué NO debe pasar

- Que `start_return_request` se llame sobre un pedido que no está `ENTREGADO` (corresponde
  anulación, no devolución).
- Que el agente prometa una fecha de entrega que no reportó `track_order`.

## Referencia

`solucion/retail/domain_tools.py` y `solucion/retail/agent.py`.
