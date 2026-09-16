# L4 · Telecomunicaciones — AndesMóvil

Sigue las 4 partes de [`../README.md`](../README.md). Esto es lo específico de tu track.

## Tus 3 tools nuevas

| Tool | Dataset que consulta | Nota |
|---|---|---|
| `get_data_usage` | `consumo_datos.csv` | Filtra por `numero_linea` y `periodo` (formato `AAAA-MM`) |
| `run_line_diagnostics` | `clientes.csv` + `cobertura_distritos.csv` | Combina el estado de la línea con la cobertura de su distrito |
| `create_complaint_ticket` **(escritura)** | `tickets_reclamos.csv` | Genera un código `REC-2026-NNNNN` con `datos.siguiente_id()`. **Exige confirmación** antes de registrar el reclamo — nunca la ejecutes ante la primera mención de disconformidad, solo cuando el cliente lo pida explícitamente o confirme que quiere registrarlo |

## Qué NO debe pasar

- Que `create_complaint_ticket` se llame dos veces por el mismo motivo sin que el cliente lo pida.
- Que el agente use `run_line_diagnostics` para preguntas de facturación, o `get_data_usage` para
  preguntas de plan (son las confusiones que ya viste en la demo 2 de `code/`).

## Referencia

`solucion/telecomunicaciones/domain_tools.py` y `solucion/telecomunicaciones/agent.py`.
