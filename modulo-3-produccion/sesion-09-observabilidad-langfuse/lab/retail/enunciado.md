# L9 · Retail — MercaSur

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué instrumentas

Tu `agent.py` (v4) del L8, que ya expone `/chat`. Hoy solo le añades el callback — no toques
la lógica de tools ni de guardrails.

## Dónde buscar tus cuellos de botella

`start_return_request` exige confirmación explícita, lo que suele producir 2 llamadas al modelo
por devolución (una para proponer, otra para confirmar) — mira si ese patrón se repite más de
lo esperado. El otro candidato típico: el retriever llamándose en preguntas de seguimiento de
pedido, que debería resolver `track_order`, no la base de conocimiento.

Referencia: [`../../solucion/retail/observability.py`](../../solucion/retail/observability.py).
