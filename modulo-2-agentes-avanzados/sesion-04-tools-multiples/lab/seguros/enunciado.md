# L4 · Seguros — Andina Seguros

Sigue las 4 partes de [`../README.md`](../README.md). Esto es lo específico de tu track.

## Tus 3 tools nuevas

| Tool | Dataset que consulta | Nota |
|---|---|---|
| `quote_soat` | `vehiculos.csv` | Prima por categoría, uso y antigüedad — nunca inventes la fórmula, replica la de la referencia |
| `get_claim_status` | `siniestros.csv` | Si hay lesionados registrados, la respuesta debe indicar que se derive al canal humano |
| `open_claim` **(escritura)** | `polizas.csv` + `siniestros.csv` | Genera un expediente `SIN-2026-NNNNN`. **Exige confirmación** antes de abrir el expediente. Si `cantidad_lesionados > 0`, la prioridad es máxima: deriva de inmediato, incluso ya con el expediente abierto |

## Qué NO debe pasar

- Que el agente estime cuánto se le pagará a alguien: eso no lo hace ninguna tool ni el agente.
- Que `open_claim` se ejecute sin confirmar, o que no derive al canal humano ante lesionados.

## Referencia

`solucion/seguros/domain_tools.py` y `solucion/seguros/agent.py`.
