# L2 · Retail — MercaSur

Sigue las 4 partes de [`../README.md`](../README.md).

## Tu Enum `categoria`

`SEGUIMIENTO_PEDIDO` · `CONSULTA_PRODUCTO` · `CONSULTA_STOCK` · `DEVOLUCION` · `OTRO`

## Tu campo `entidades`

Lo que el cliente mencione: número de pedido o SKU del producto.

## Ejemplos few-shot sugeridos (regla A5)

Cubre la confusión más común del track — SEGUIMIENTO_PEDIDO vs DEVOLUCION:

- *"Mi pedido dice entregado pero no lo he recibido"* → `SEGUIMIENTO_PEDIDO`
- *"Compré esto y vino fallado, quiero cambiarlo"* → `DEVOLUCION`

Referencia: `solucion/retail/`.
