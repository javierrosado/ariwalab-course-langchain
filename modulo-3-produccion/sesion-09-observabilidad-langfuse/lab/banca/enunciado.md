# L9 · Banca — Banco Inti

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué instrumentas

Tu `agent.py` (v4) del L8, que ya expone `/chat`. Hoy solo le añades el callback — no toques
la lógica de tools ni de guardrails.

## Dónde buscar tus cuellos de botella

Tus 4 tools son de solo lectura; el candidato más probable no es una tool cara, sino el
historial de conversación creciendo turno a turno (el modelo es *stateless*: se reenvía todo,
S2) o el retriever llamándose en preguntas de saldo/movimientos que no debería tocar la base de
conocimiento en absoluto.

Referencia: [`../../solucion/banca/observability.py`](../../solucion/banca/observability.py).
