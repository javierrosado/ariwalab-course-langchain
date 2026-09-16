# EVIDENCIA-A1 — [nombre del equipo] · [track]

> Reemplaza cada `[placeholder]` con la traza REAL de correr `prueba_tool.py` y tu `agent.py`.
> "Se probó y funcionó" no cuenta como evidencia — la traza pegada sí.

---

## Escenario 1 · Éxito

| Campo | Detalle |
|---|---|
| Identificador usado | [numero_linea / numero_cuenta / pedido_id / placa real] |
| Traza — entrada | ```[mensaje real que le mandaste al agente]``` |
| Traza — salida | ```[respuesta real del agente]``` |
| ¿Citó el dato correctamente? | [sí / no] |

## Escenario 2 · Dato inexistente

| Campo | Detalle |
|---|---|
| Identificador usado | [uno con formato válido pero que no existe] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿El agente inventó un dato o dijo "no existe"? | [...] |

## Escenario 3 · Servicio caído

| Campo | Detalle |
|---|---|
| Cómo se provocó | `?_fallo=error503` sobre [ruta real] |
| Traza — salida de `prueba_tool.py` | ```[...]``` |
| ¿El agente avisó sin entrar en bucle de reintentos? | [...] |

## Reto opcional (si lo hiciste)

| Campo | Detalle |
|---|---|
| Cómo se provocó | `?_fallo=malformado` |
| Qué pasó | [el 200 con JSON inválido — ¿tu tool lo detectó?] |

---

## Qué se decidió en cada caso (3-5 líneas)

[Resumen de las decisiones de diseño que tomaste a partir de lo que viste en los 3 escenarios:
por ejemplo, cómo redactaste el mensaje de error, o por qué elegiste ese tope de iteraciones.]
