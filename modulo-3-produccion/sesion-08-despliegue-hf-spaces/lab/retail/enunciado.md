# L8 · Retail — MercaSur

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué envuelves

Tu `agent.py` (v4) del L6, con `TOOLS_NUCLEO` del L4 (`track_order`, `check_stock_by_store`,
`get_product_details`, `start_return_request`) + el retriever del L5 + los guardrails del L6 ya
dentro.

## Variables que necesitas como *Space secrets*

`HF_TOKEN`, `QDRANT_URL`, `QDRANT_API_KEY`, `AGENT_API_KEY`, `COURSE_TRACK=retail`,
`DATA_SOURCE=api`, `SIM_BASE_URL`, `SIM_API_KEY`.

## Recordatorio de la S4

`start_return_request` exige `confirmado_por_cliente=true`. Verifica en tu prueba desde fuera
(parte 4) que esa confirmación siga exigiéndose a través del `/chat` — es la única tool de
escritura de tu catálogo, y es la que más conviene probar dos veces.

Referencia: [`../../solucion/retail/api.py`](../../solucion/retail/api.py) y
[`Dockerfile`](../../solucion/retail/Dockerfile).
