# L3 · Retail — MercaSur

Sigue las 3 partes de [`../README.md`](../README.md).

## Tu tool

`track_order(pedido_id: str) -> str` contra `GET /retail/pedidos/{pedido_id}`.

## Tus 3 escenarios

1. **Éxito:** un `pedido_id` real de `recursos/datasets/retail/pedidos.csv` (formato
   `MS-2026-NNNNN`).
2. **Dato inexistente:** un número de pedido con formato válido que no esté en el dataset.
3. **Servicio caído:** el mismo pedido real, con `?_fallo=error503`.

Referencia: `solucion/retail/`.
