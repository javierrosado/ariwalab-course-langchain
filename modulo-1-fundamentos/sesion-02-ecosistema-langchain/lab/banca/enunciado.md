# L2 · Banca — Banco Inti

Sigue las 4 partes de [`../README.md`](../README.md).

## Tu Enum `categoria`

`CONSULTA_SALDO` · `CONSULTA_MOVIMIENTOS` · `CONSULTA_TARJETA` · `SOSPECHA_FRAUDE` · `OTRO`

## Tu campo `entidades`

Lo que el cliente mencione: número de cuenta o identificador de movimiento.

## Ejemplos few-shot sugeridos (regla A5)

Cubre la confusión más común del track — CONSULTA_MOVIMIENTOS vs SOSPECHA_FRAUDE:

- *"Veo un cargo que no reconozco, ¿me listan lo del último mes?"* → `CONSULTA_MOVIMIENTOS`
- *"Este movimiento no lo hice yo, ¿qué tan riesgoso es?"* → `SOSPECHA_FRAUDE`

Referencia: `solucion/banca/`.
