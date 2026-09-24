# Sesión 9 — Monitoreo y trazabilidad con Langfuse

> Semana 5 · martes · **2.5 h teoría + 3.5 h práctica = 6 h**.

Antes de esta sesión: pre-work de 1 h ([`conceptos-previos.md`](conceptos-previos.md)) y tu
Space del L8 ya desplegado y respondiendo.

> **Desviación documentada del PDF (riesgo R6).** El sílabo original nombra *LangSmith*. El
> curso cumple el mismo objetivo —observabilidad y trazabilidad de agentes— con **Langfuse**,
> por el principio P1: LangSmith es propietario, Langfuse es open source y tiene un plan Hobby
> gratuito suficiente para el curso. Es una decisión de arquitectura, no una excusa: el alumno
> debe salir sabiendo que la herramienta del sílabo existe y por qué el curso usó la equivalente
> abierta.

---

## 1. Objetivos de aprendizaje

1. Distinguir **logs, métricas y trazas**, y decir qué pregunta responde cada uno.
2. Leer una traza de agente: *trace*, *span*, jerarquía padre-hijo.
3. Medir **latencia p50/p95** y **costo por ejecución**, y decir dónde se van ambos.
4. Encontrar un cuello de botella real leyendo trazas, no adivinando.
5. Explicar por qué una traza es un riesgo de fuga de PII, y qué se hace al respecto.

---

## 0. El agente ya está desplegado. ¿Y ahora qué hace?

Hasta el L8, el agente era una caja negra que respondía. Hoy deja de serlo: cada ejecución
queda registrada como una **traza** que puedes leer después, sin haber estado presente cuando
ocurrió.

---

## 1. Logs vs métricas vs trazas

Tres preguntas distintas:

| | Pregunta que responde |
|---|---|
| **Logs** | ¿Qué pasó, en texto libre? |
| **Métricas** | ¿Cuánto, agregado en el tiempo? |
| **Trazas** | ¿Por dónde pasó ESTA ejecución en particular? |

La mayoría de quien empieza solo conoce logs. Un agente con tools, retriever y varias llamadas
al modelo por turno necesita el tercero: un log te dice que algo pasó, una traza te dice **en
qué orden** y **cuánto costó cada paso**.

---

## 2. Anatomía de una traza de agente

```
   TRACE  «consulta de cliente»                                   3 420 ms
   │
   ├── SPAN  llamada al modelo (decidir)                          1 180 ms
   │         └── el modelo propone: get_customer_plan
   ├── SPAN  tool get_customer_plan                                 240 ms
   ├── SPAN  llamada al modelo (decidir)                            980 ms
   │         └── el modelo propone: recuperar del corpus
   ├── SPAN  retriever kb-telecomunicaciones                        610 ms
   └── SPAN  llamada al modelo (redactar)                           410 ms
```

Tres lecturas que debes hacer solo:

| Lo que se ve | Lo que significa |
|---|---|
| 3 llamadas al modelo para 1 pregunta | La fiabilidad se compone: 3 oportunidades de fallar (D20) |
| El modelo cuesta 2 570 ms de 3 420 | El cuello no son las tools ni Qdrant: **es el modelo** |
| El retriever se llamó | ¿Hacía falta? Si se llama siempre, el RAG agéntico de la S5 degeneró en tradicional |

> **Alcance de la instrumentación:** el checkpoint pasa callbacks a cada invocación.
> No llama a `extraer_con_detalle()` dentro del bucle y ese helper no recibe callbacks
> explícitos. No esperar sus reintentos en esta traza. Un árbol único por petición requiere
> un contexto padre: verificarlo en Langfuse antes de interpretar este dibujo como salida real.

---

## 3. Latencia p50/p95 y por qué el promedio miente

```
   10 peticiones:  9 × 800 ms  +  1 × 21 000 ms  (cold start)
   promedio  ──► 2 820 ms      "el agente tarda 3 segundos"   ✗
   p50       ──►   800 ms      lo que vive el usuario típico  ✓
   p95       ──► 21 000 ms     cola de latencia (nearest rank en este ejemplo)       ✓
```

Un *cold start* influye en el promedio y también puede cambiar el p95. Con diez muestras,
el método nearest rank toma ceil(0.95 × 10) = 10: aquí coincide con el máximo. Otros métodos
interpolan. Declarar método, tamaño de muestra y separación entre arranque frío y tráfico estable.

---

## 4. PII dentro de una traza — decisión del curso

Las trazas pasan por el **mismo enmascarador del L6** (`guardrails.py`), aplicado antes de
exportar a Langfuse (ver `comun/observability.py`).

| Qué | Cómo |
|---|---|
| Dónde se aplica | En el cliente de Langfuse, antes de enviar cualquier span |
| Con qué código | Patrones equivalentes para DNI/tarjeta, implementados en comun/observability.py, más teléfono |
| Qué se enmascara | DNI, número de tarjeta, teléfono |
| Qué se conserva | La estructura de la traza, las tools, los tiempos, el costo |

**El argumento, que es la lección:** si el DNI no puede salir del agente hacia el cliente,
tampoco puede salir hacia un SaaS de terceros. Un guardrail que solo protege la salida visible
y deja la telemetría en claro no es un guardrail: es una apariencia.

El costo hay que decirlo también: **se pierde algo de capacidad de depuración.** Cuando una
traza muestra `numero_linea: 98*******`, no puedes reproducir el caso exacto sin pedirle el
dato al equipo. Es el compromiso real que se firma en producción, y aquí se firma a propósito
— aunque el riesgo material sea cero (los datos del curso son sintéticos), el hábito es lo que
se enseña.

---

## 5. Las 3 demos y el laboratorio

Ver [`code/README.md`](code/README.md) para las demos y [`lab/README.md`](lab/README.md) para
el Laboratorio 9 completo (instrumentación, redespliegue y Avance 2 del proyecto).

---

## 6. Qué NO entra hoy

| No entra | Va en |
|---|---|
| Datasets, evaluators, LLM-as-judge | S10 |
| Optimizar de verdad (solo se identifica) | S10 |
| Alertas y on-call | fuera de alcance |
| Azure Monitor / OTel exporters | Curso 2 |
