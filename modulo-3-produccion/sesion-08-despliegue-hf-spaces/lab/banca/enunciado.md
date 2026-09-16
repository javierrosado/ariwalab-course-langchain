# L8 · Banca — Banco Inti

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué envuelves

Tu `agent.py` (v4) del L6, con `TOOLS_NUCLEO` del L4 (`get_account_balance`,
`list_transactions`, `get_card_info`, `score_transaction_risk` — las 4 de solo lectura) + el
retriever del L5 + los guardrails del L6 ya dentro.

## Variables que necesitas como *Space secrets*

`HF_TOKEN`, `QDRANT_URL`, `QDRANT_API_KEY`, `AGENT_API_KEY`, `COURSE_TRACK=banca`,
`DATA_SOURCE=api`, `SIM_BASE_URL`, `SIM_API_KEY`.

## Recordatorio de la S6

Tu guardrail de salida enmascara DNI y número de tarjeta (`guardrails.check_output`). Prueba
desde fuera (parte 4) con una consulta que dispare `get_card_info` y confirma que la respuesta
que llega por HTTP sigue enmascarada — el enmascarado ocurre dentro de `responder()`, así que
debería sobrevivir intacto al envoltorio HTTP, pero es justo el tipo de regresión silenciosa que
solo se detecta probando **desde fuera**, no leyendo el código.

Referencia: [`../../solucion/banca/api.py`](../../solucion/banca/api.py) y
[`Dockerfile`](../../solucion/banca/Dockerfile).
