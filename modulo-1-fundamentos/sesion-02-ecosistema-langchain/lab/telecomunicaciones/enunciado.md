# L2 · Telecomunicaciones — AndesMóvil

Sigue las 4 partes de [`../README.md`](../README.md).

## Tu Enum `categoria`

`CONSULTA_PLAN` · `CONSULTA_CONSUMO` · `AVERIA` · `RECLAMO` · `OTRO`

## Tu campo `entidades`

Lo que el cliente mencione como identificador: normalmente el número de línea (9 dígitos).

## Ejemplos few-shot sugeridos (regla A5)

Cubre la confusión más común del track — AVERIA vs RECLAMO:

- *"Se me cae la llamada todo el tiempo, ya es insoportable"* → `AVERIA`
- *"Quiero un número de seguimiento porque llevo 3 días sin servicio"* → `RECLAMO`

Referencia: `solucion/telecomunicaciones/`.
