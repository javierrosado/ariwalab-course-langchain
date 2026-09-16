# L3 · Telecomunicaciones — AndesMóvil

Sigue las 3 partes de [`../README.md`](../README.md).

## Tu tool

`get_customer_plan(numero_linea: str) -> str` contra `GET /telco/clientes/{numero_linea}`.

## Tus 3 escenarios

1. **Éxito:** un `numero_linea` real de `recursos/datasets/telecomunicaciones/clientes.csv`.
2. **Dato inexistente:** un número de línea de 9 dígitos que no esté en el dataset.
3. **Servicio caído:** la misma línea real, con `?_fallo=error503`.

Referencia: `solucion/telecomunicaciones/`.
