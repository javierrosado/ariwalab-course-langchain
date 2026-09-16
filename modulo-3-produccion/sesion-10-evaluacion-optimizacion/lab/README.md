# Laboratorio L10 · Evaluación y optimización

**Objetivo:** medir con evidencia, no con intuición, y decidir un cambio con el número.

**Duración:** 2 h.

**Punto de partida:** tu `agent.py` (v5) del L9, instrumentado, y tu `INFORME-L9.md` con 2
cuellos de botella documentados.

---

## Parte 1 · Cargar tus 30 casos en Langfuse Datasets (25 min)

Adapta `code/01_dataset_langfuse.py` a tu track (o corre el de referencia, que ya usa
`consultas-<tu-track>.json`). Confirma en el dashboard que el dataset tiene los 30 casos.

## Parte 2 · Correr la línea base v1 (25 min)

Usa `evals/evaluadores.py` (checkpoint de referencia: reexporta `comun.evaluadores`) sobre las
30 consultas contra tu `agent.py` actual. Registra las 3 métricas (uso de tool, exactitud,
groundedness) en `INFORME-L10.md`.

## Parte 3 · Aplicar UN cambio dirigido a un cuello del L9 (40 min)

Debe ser **uno solo y trazable** al Avance 2:

| Cuello hallado en el L9 | Cambio típico en el L10 |
|---|---|
| El retriever se llama siempre | Escribir el "cuándo NO" en su docstring |
| Dos tools se confunden | Separar ambas docstrings (lo que dice la matriz) |
| El historial dispara el costo | Recortar o resumir el historial |
| Reintentos frecuentes de extracción | Partir el esquema en dos, o añadir few-shot |

**Un cambio por medición.** Si cambias tres cosas a la vez y mejora, no sabrás cuál sirvió — y
en la siguiente iteración no sabrás qué conservar.

## Parte 4 · Correr v2, comparar y decidir (30 min)

Vuelve a correr las 30 consultas con el cambio aplicado. Compara contra v1 en una tabla. Si no
mejoró, documenta la hipótesis y por qué se descartó — un experimento negativo bien documentado
vale lo mismo que uno positivo.

---

## Entregables

| Entregable | Ruta |
|---|---|
| `evals/dataset.py` y `evals/evaluadores.py` | tu repositorio de equipo |
| Dataset de 30 casos visible en Langfuse | tu proyecto de equipo |
| `INFORME-L10.md` con la tabla v1 vs v2 | `lab/<tu-track>/` |
| **Avance 3 del M3** | `lab/<tu-track>/avance-3-m3.md` |

Ver las plantillas en [`solucion/telecomunicaciones/`](../solucion/telecomunicaciones/).

## Criterio de aceptación

- Los **30 casos** corriendo con los 3 evaluators.
- **Mejora medible de v1 a v2**, con tabla comparativa por métrica — o, si no mejoró, la
  hipótesis y por qué se descartó, igual de válido.
- El informe **nombra el cambio** que produjo la mejora (o el intento) y el cuello del L9 que
  atacaba.

## Cada track

| Track | Enunciado |
|---|---|
| Telecomunicaciones · AndesMóvil | [`telecomunicaciones/enunciado.md`](telecomunicaciones/enunciado.md) |
| Banca · Banco Inti | [`banca/enunciado.md`](banca/enunciado.md) |
| Retail · MercaSur | [`retail/enunciado.md`](retail/enunciado.md) |
| Seguros · Andina Seguros | [`seguros/enunciado.md`](seguros/enunciado.md) |
