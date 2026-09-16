# L9 · Seguros — Andina Seguros

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué instrumentas

Tu `agent.py` (v4) del L8, que ya expone `/chat`. Hoy solo le añades el callback — no toques
la lógica de tools ni de guardrails.

## Dónde buscar tus cuellos de botella

`open_claim` exige confirmación explícita, igual que en retail. El otro candidato típico: el
retriever de condicionados (chunking 600/100, el más grande de los 4 tracks) puede tardar más
que en los otros tracks — compara tu latencia de span de retriever contra la de otro equipo.

Referencia: [`../../solucion/seguros/observability.py`](../../solucion/seguros/observability.py).
