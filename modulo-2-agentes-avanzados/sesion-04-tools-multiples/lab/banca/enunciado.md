# L4 · Banca — Banco Inti

Sigue las 4 partes de [`../README.md`](../README.md). Esto es lo específico de tu track.

## Tus 3 tools nuevas

| Tool | Dataset que consulta | Nota |
|---|---|---|
| `list_transactions` | `movimientos.csv` | Filtra por `numero_cuenta` y una ventana de días (parámetro `dias`, entre 1 y 90) |
| `get_card_info` | `tarjetas.csv` | **Nunca** devuelve el número completo: solo `ultimos_4_digitos`. Verifícalo en tu propia salida antes de darla por buena |
| `score_transaction_risk` | `movimientos.csv` + `alertas_riesgo.csv` | Devuelve el puntaje (0-100) y el nivel de riesgo; **no** afirmes "es fraude", solo reporta el puntaje y la acción sugerida |

## Sobre la tool de escritura

Tu núcleo de 4 tools es **todo de lectura** (ver la nota en `../README.md`). No implementas
confirmación hoy. Si quieres el reto opcional de `request_card_block` (bloqueo de tarjeta), ese
sí exige el patrón de confirmación explícita — mira su implementación en
`solucion/banca/domain_tools.py` como referencia de la mecánica.

## Qué NO debe pasar

- Que el agente muestre un número de tarjeta completo (16 dígitos) en cualquier respuesta.
- Que el agente confirme o descarte un fraude por su cuenta: siempre reporta el puntaje y deriva
  si es alto.

## Referencia

`solucion/banca/domain_tools.py` y `solucion/banca/agent.py`.
