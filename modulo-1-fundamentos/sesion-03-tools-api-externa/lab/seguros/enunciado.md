# L3 · Seguros — Andina Seguros

Sigue las 3 partes de [`../README.md`](../README.md).

## Tu tool

`get_policy_by_plate(placa: str) -> str` contra `GET /seguros/polizas/{placa}`.

## Tus 3 escenarios

1. **Éxito:** una `placa` real de `recursos/datasets/seguros/polizas.csv` (formato `ABC-123`).
2. **Dato inexistente:** una placa con formato válido que no esté en el dataset.
3. **Servicio caído:** la misma placa real, con `?_fallo=error503`.

Referencia: `solucion/seguros/`.
