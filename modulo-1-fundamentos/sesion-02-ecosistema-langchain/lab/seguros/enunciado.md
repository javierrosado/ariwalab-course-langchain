# L2 · Seguros — Andina Seguros

Sigue las 4 partes de [`../README.md`](../README.md).

## Tu Enum `categoria`

`CONSULTA_POLIZA` · `COTIZACION` · `ESTADO_SINIESTRO` · `REPORTE_SINIESTRO` · `OTRO`

## Tu campo `entidades`

Lo que el cliente mencione: placa del vehículo o código de expediente de siniestro.

## Ejemplos few-shot sugeridos (regla A5)

Cubre la confusión más común del track — COTIZACION vs CONSULTA_POLIZA:

- *"Mi SOAT venció, ¿cuánto pagaría por renovarlo?"* → `COTIZACION`
- *"Antes de reportar el choque, ¿mi póliza está vigente?"* → `CONSULTA_POLIZA`

Referencia: `solucion/seguros/`.
