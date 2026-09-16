# INFORME-L7 — Pruebas de estrés · [nombre del equipo] · [track]

> Reemplaza cada `[placeholder]`. **No borres una fila sin llenarla**: una familia sin casos es
> una familia que no se probó. Mínimo **10 casos**, con **al menos 2 por familia**. Cada caso
> necesita una traza real (entrada y salida reales, no una descripción de memoria) — "probamos
> varios escenarios y funcionó" no cuenta como evidencia (ver `docente/esqueletos/sesion-07.md`,
> tabla de errores esperables).
>
> **Recomendación de orden:** abre con el peor caso que encontraron y resolvieron, no con el
> camino feliz — es lo que pide el guion de la clínica (`sesion-07.md` §7).

---

## Resumen

| Campo | Valor |
|---|---|
| Equipo | [nombres] |
| Track | [telecomunicaciones / banca / retail / seguros] |
| Fecha de la clínica | [AAAA-MM-DD] |
| Casos documentados | [N] (mínimo 10) |
| Casos resueltos | [N] de [N] |
| Peor caso encontrado | [una frase] |

---

## Caso 0 — el peor que encontramos (abre la demo con este)

| Campo | Detalle |
|---|---|
| Familia | [entrada ambigua / dato ausente / servicio caído / salida fuera de formato] |
| Qué se probó | [la acción exacta, con el mensaje real enviado al agente] |
| Traza — entrada | ```[mensaje real del usuario]``` |
| Traza — salida (antes de arreglarlo) | ```[respuesta real del agente, con el fallo]``` |
| Qué se cambió | [el cambio de código o de prompt] |
| Traza — salida (después) | ```[respuesta real, ya corregida]``` |

---

## Familia 1 · Entrada ambigua

*Dos intenciones en un solo turno — ¿qué hace el agente?*

### Caso 1.1

| Campo | Detalle |
|---|---|
| Qué se probó | [mensaje real con dos intenciones] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿Se resolvió? | [sí / no, y qué falta] |
| Qué se cambió | [...] |

### Caso 1.2

| Campo | Detalle |
|---|---|
| Qué se probó | [...] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿Se resolvió? | [...] |
| Qué se cambió | [...] |

---

## Familia 2 · Dato ausente

*Un identificador que no existe, o un campo vacío — dentro de una conversación larga (turno 3+).*

### Caso 2.1

| Campo | Detalle |
|---|---|
| Qué se probó | [...] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿Se resolvió? | [...] |
| Qué se cambió | [...] |

### Caso 2.2

| Campo | Detalle |
|---|---|
| Qué se probó | [...] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿Se resolvió? | [...] |
| Qué se cambió | [...] |

---

## Familia 3 · Servicio caído

*`CHAOS_RATE=0.1` — falla sin avisar, a mitad de conversación. Usa `?_fallo=timeout|error500|error503|lento|vacio|malformado` para forzarlo si el azar no coopera.*

### Caso 3.1

| Campo | Detalle |
|---|---|
| Fallo forzado | [timeout / error500 / error503 / lento / vacio / malformado] |
| Qué se probó | [...] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿Perdió el hilo de la conversación? | [sí / no] |
| Qué se cambió | [...] |

### Caso 3.2

| Campo | Detalle |
|---|---|
| Fallo forzado | [...] |
| Qué se probó | [...] |
| Traza — entrada | ```[...]``` |
| Traza — salida | ```[...]``` |
| ¿Perdió el hilo de la conversación? | [...] |
| Qué se cambió | [...] |

---

## Familia 4 · Salida fuera de formato

*El modelo devuelve algo que no cumple el esquema — aquí se cobra `comun/structured.py` de la S2.*

### Caso 4.1

| Campo | Detalle |
|---|---|
| Qué se probó | [entrada rara que empuja al modelo a salirse del esquema] |
| Traza — salida cruda del modelo | ```[...]``` |
| ¿`extraer()` lo capturó y reintentó? | [sí / no] |
| Qué se cambió | [...] |

### Caso 4.2

| Campo | Detalle |
|---|---|
| Qué se probó | [...] |
| Traza — salida cruda del modelo | ```[...]``` |
| ¿`extraer()` lo capturó y reintentó? | [...] |
| Qué se cambió | [...] |

---

## Casos adicionales (si superan los 10 mínimos)

Repite la estructura de arriba por cada caso extra, indicando su familia.

---

## Reflexión final (5-8 líneas)

[¿Qué patrón de fallo se repitió más? ¿Qué parte del diseño (memoria, guardrails, structured
output) fue la que más sostuvo al agente bajo el caos? ¿Qué harían distinto si empezaran de
nuevo?]
