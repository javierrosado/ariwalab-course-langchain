# L9 · Telecomunicaciones — AndesMóvil

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué instrumentas

Tu `agent.py` (v4) del L8, que ya expone `/chat`. Hoy solo le añades el callback — no toques
la lógica de tools ni de guardrails.

## Dónde buscar tus cuellos de botella

Con 4 tools de lectura + `create_complaint_ticket` (escritura) + el retriever, los candidatos
más probables son: el retriever llamándose en consultas que ya traen el número de línea (no
debería, según su docstring del L5), y reintentos de `extraer_con_detalle()` si tu esquema de
clasificación del L2 quedó demasiado exigente.

Referencia: [`../../solucion/telecomunicaciones/observability.py`](../../solucion/telecomunicaciones/observability.py).
