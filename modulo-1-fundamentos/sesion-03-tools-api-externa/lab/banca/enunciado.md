# L3 · Banca — Banco Inti

Sigue las 3 partes de [`../README.md`](../README.md).

## Tu tool

`get_account_balance(numero_cuenta: str) -> str` contra `GET /banca/cuentas/{numero_cuenta}`.

## Tus 3 escenarios

1. **Éxito:** un `numero_cuenta` real de `recursos/datasets/banca/cuentas.csv` (formato
   `191-XXXXXXX-0-XX`).
2. **Dato inexistente:** un número de cuenta con formato válido que no esté en el dataset.
3. **Servicio caído:** la misma cuenta real, con `?_fallo=error503`.

Referencia: `solucion/banca/`.
