# L8 · Telecomunicaciones — AndesMóvil

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué envuelves

Tu `agent.py` (v4) del L6, con `TOOLS_NUCLEO` del L4 (`get_customer_plan`, `get_data_usage`,
`run_line_diagnostics`, `create_complaint_ticket`) + el retriever del L5 + los guardrails del L6
ya dentro. Hoy no tocas esa lógica: la expones por `/chat`.

## Variables que necesitas como *Space secrets*

`HF_TOKEN`, `QDRANT_URL`, `QDRANT_API_KEY`, `AGENT_API_KEY`, `COURSE_TRACK=telecomunicaciones`,
`DATA_SOURCE=api`, `SIM_BASE_URL`, `SIM_API_KEY`.

## Recordatorio de la S4

`create_complaint_ticket` exige `confirmado_por_cliente=true`. Verifica en tu prueba desde
fuera (parte 4) que el guardia de confirmación siga funcionando **a través** de la API — es
fácil que se rompa si el cliente HTTP no propaga bien los argumentos de la tool.

Referencia: [`../../solucion/telecomunicaciones/api.py`](../../solucion/telecomunicaciones/api.py)
y [`Dockerfile`](../../solucion/telecomunicaciones/Dockerfile).
