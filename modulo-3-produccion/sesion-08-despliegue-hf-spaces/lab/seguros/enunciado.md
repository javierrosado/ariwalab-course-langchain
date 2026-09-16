# L8 · Seguros — Andina Seguros

Sigue las 4 partes de [`../README.md`](../README.md).

## Qué envuelves

Tu `agent.py` (v4) del L6, con `TOOLS_NUCLEO` del L4 (`get_policy_by_plate`, `quote_soat`,
`get_claim_status`, `open_claim`) + el retriever del L5 + los guardrails del L6 ya dentro.

## Variables que necesitas como *Space secrets*

`HF_TOKEN`, `QDRANT_URL`, `QDRANT_API_KEY`, `AGENT_API_KEY`, `COURSE_TRACK=seguros`,
`DATA_SOURCE=api`, `SIM_BASE_URL`, `SIM_API_KEY`.

## Recordatorio de la S4 y la S6

`open_claim` exige `confirmado_por_cliente=true`, y tu lista de prohibidos incluye no asesorar
sobre responsabilidad en un accidente. Prueba desde fuera (parte 4) con una consulta que
pregunte "¿de quién fue la culpa?" y confirma que el guardrail de salida sigue derivando el
caso a través del `/chat`, no solo en tu terminal local.

Referencia: [`../../solucion/seguros/api.py`](../../solucion/seguros/api.py) y
[`Dockerfile`](../../solucion/seguros/Dockerfile).
