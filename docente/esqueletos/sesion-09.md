# Esqueleto · Sesión 9 — Monitoreo y trazabilidad con Langfuse

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-3-produccion/sesion-09-observabilidad-langfuse/` |
| Semana · día | Semana 5 · martes |
| Horas | **2.5 h teoría · 3.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (90 T / 80 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L9 · Trazabilidad del agente desplegado** |
| Hitos | **Avance 2 del M3** |

> Usar Langfuse para estudiar observabilidad y trazabilidad. Comprobar que los equipos
> puedan consultar sus trazas antes de iniciar la práctica.

---

## 2. Bloqueante

| Qué | Quién | Para cuándo |
|---|---|---|
| Proyecto de Langfuse Cloud operativo, con los 2 integrantes | cada equipo | Lunes semana 5 |

La cuenta se creó en la **Sesión 0**. Aquí solo se verifica: `python -m comun.check_stack` en verde
en la comprobación 8. El plan Hobby admite **2 usuarios por proyecto** — que es exactamente por
lo que los equipos son de 2.

---

## 3. Objetivos de aprendizaje

1. Distinguir **logs, métricas y trazas**, y decir qué pregunta responde cada uno.
2. Leer una traza de agente: *trace*, *span*, jerarquía padre-hijo.
3. Medir **latencia p50/p95** y **costo por ejecución**, y decir dónde se van ambos.
4. Encontrar un cuello de botella real leyendo trazas, no adivinando.
5. Explicar por qué una traza es un riesgo de fuga de PII, y qué se hace al respecto.

---

## 4. Con qué llega el alumno

**Pre-work de 1 h:**

| # | Concepto | Por qué |
|---|---|---|
| 1 | Observabilidad: logs vs métricas vs trazas | La mayoría solo conoce logs |
| 2 | Traza distribuida: *span*, *trace id*, jerarquía | Un run de agente es exactamente eso |
| 3 | OpenTelemetry, nociones | Langfuse habla OTel; es el puente al Curso 2 |
| 4 | Percentiles: p50 y p95, y por qué no el promedio | Es lo que se lee en el dashboard |
| 5 | *Callback handler* de LangChain | Se instrumenta **sin tocar la lógica** del agente |
| 6 | Qué es PII dentro de una traza | Una traza guarda los prompts completos |

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | El agente ya está desplegado. ¿Y ahora qué hace? | 5 | T | Hoy el agente deja de ser una caja negra |
| 1 | Logs vs métricas vs trazas | 20 | T | Tres preguntas distintas: *¿qué pasó?* · *¿cuánto?* · *¿por dónde pasó?* |
| 2 | **Anatomía de una traza de agente** | 25 | T | Trace → spans: modelo, tool, retriever, reintento de extracción |
| 3 | Latencia p50/p95 y costo por ejecución | 20 | T | Por qué el promedio miente. Dónde se va el dinero |
| 4 | **PII dentro de una traza** | 20 | T | La decisión de §6, y por qué |
| — | **Pausa** | 10 | — | |
| 5 | Práctica: instrumentar y **redesplegar** | 40 | P | El callback, el enmascarador, `git push` |
| 6 | Leer trazas reales y hallar 2 cuellos de botella | 40 | P | Del Space, no de la laptop |

**Teoría 90 · práctica 80 · pausa 10** → con pre-work y lab: **2.5 h / 3.5 h** ✅

### Bloque 2 — la traza que el alumno va a ver

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

Tres lecturas que el alumno debe hacer solo:

| Lo que se ve | Lo que significa |
|---|---|
| 3 llamadas al modelo para 1 pregunta | La fiabilidad se compone: 3 oportunidades de fallar |
| El modelo cuesta 2 570 ms de 3 420 | El cuello no son las tools ni Qdrant: **es el modelo** |
| El retriever se llamó | ¿Hacía falta? Si se llama siempre, el RAG agéntico de la S5 degeneró en tradicional |

> **Los reintentos de `extraer_con_detalle()` aparecen como spans.** Lo que en la S2 fue un número
> impreso en consola, aquí es una línea en la traza de producción. Es la misma medida, cinco
> sesiones después, y ahora sobre tráfico real.

### Bloque 3 — por qué el promedio miente

```
   10 peticiones:  9 × 800 ms  +  1 × 21 000 ms  (cold start)
   promedio  ──► 2 820 ms      "el agente tarda 3 segundos"   ✗
   p50       ──►   800 ms      lo que vive el usuario típico  ✓
   p95       ──► 21 000 ms     lo que vive el peor caso       ✓
```

---

## 6. Decisión: las trazas van con la PII enmascarada

Las trazas pasan por **el mismo enmascarador que el alumno escribió en el L6**.

| Qué | Cómo |
|---|---|
| Dónde se aplica | En el callback, antes de enviar a Langfuse |
| Con qué código | El de `guardrails.py` del L6 — no se escribe uno nuevo |
| Qué se enmascara | DNI, número de tarjeta, teléfono, dirección |
| Qué se conserva | Todo lo demás: la estructura de la traza, las tools, los tiempos, el costo |

**El argumento, que es la lección:**

> Si el DNI no puede salir del agente **hacia el cliente**, tampoco puede salir **hacia un SaaS de
> terceros**. Un guardrail que solo protege la salida visible y deja la telemetría en claro no es un
> guardrail: es una apariencia.

Y el costo hay que decirlo también: **se pierde algo de capacidad de depuración.** Cuando una traza
muestra `numero_linea: 98*******`, el docente no puede reproducir el caso exacto sin pedirle el dato
al equipo. Es el compromiso real que se firma en producción, y aquí se firma a propósito.

> Los datos del curso son sintéticos, así que el riesgo material es cero. Se enmascara igual,
> porque el hábito es lo que se está enseñando. Conviene decirlo así, sin fingir un riesgo que no
> existe.

---

## 7. Las 3 demos · `code/`

| Archivo | Qué demuestra |
|---|---|
| `01_traza_minima.py` | El callback puesto y una traza apareciendo en el dashboard en vivo |
| `02_anatomia_spans.py` | Un run con tool + retriever, y los spans que produce |
| `03_pii_en_traza.py` | La misma consulta con y sin el enmascarador: lo que Langfuse llega a almacenar |

La demo 3 se corre **antes** de que el alumno instrumente el suyo. Ver el DNI completo dentro de
una traza de un servicio ajeno es más convincente que cualquier explicación.

---

## 8. Laboratorio L9

| Parte | Min | Qué hace el alumno |
|---|---|---|
| 1 | 25 | `observability.py`: callback de Langfuse + enmascarador del L6 |
| 2 | 20 | Cargar las claves como **Space secrets** y redesplegar |
| 3 | 30 | Generar tráfico real: 20 consultas del golden set contra la URL pública |
| 4 | 45 | Leer las trazas, medir p50/p95 y documentar **2 cuellos de botella** |

### Entregables

| Entregable | Ruta |
|---|---|
| `app/observability.py` | repo del equipo |
| Space redesplegado y trazando | URL en `DESPLIEGUE.md` |
| `INFORME-L9.md` con 2 cuellos de botella | `lab/<track>/` |

### Criterio de aceptación

- Las trazas provienen del **Space desplegado**, no de la laptop. Se comprueba en el dashboard.
- **Ninguna traza contiene PII sin enmascarar.**
- **2 cuellos de botella documentados** con evidencia: captura de la traza, el número medido, y qué
  se propone cambiar.

### Los cuellos que van a encontrar

No se les adelantan, pero el docente los conoce:

| Cuello | Cómo se ve en la traza | Qué lo causa |
|---|---|---|
| El retriever se llama siempre | Un span de retriever en el 100 % de los traces | La docstring del retriever no dice cuándo NO (S5) |
| El historial crece | Tokens de entrada subiendo turno a turno | El modelo es stateless: se reenvía todo (S2) |
| Reintentos de extracción | Spans duplicados de una misma llamada | El esquema pide demasiado en un solo paso (S2) |
| *Cold start* | Un trace de 20 s aislado entre traces de 1 s | El tier gratuito duerme (S8) |

---

## 9. Avance 2 del M3

Media página: los 2 cuellos, el número que los evidencia, y **cuál se va a atacar en la S10** — que
es exactamente el insumo del A/B de prompts de la siguiente sesión.

---

## 10. Qué **no** entra

| No entra | Va en |
|---|---|
| Datasets, evaluators, LLM-as-judge | S10 |
| Optimizar de verdad (solo se identifica) | S10 |
| Alertas y on-call | fuera de alcance |
| Azure Monitor / OTel exporters | Curso 2 |

---

## 12. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| No aparece ninguna traza | Las claves no se cargaron como Space secrets | Es la lección de la S8, repetida |
| Aparecen trazas de la laptop y del Space mezcladas | Mismo proyecto de Langfuse para ambos | Separar por *tag* de entorno: es lo que se hace en producción |
| La traza tiene un solo span | El callback se pasó al modelo y no al agente | Va en el agente: solo así se ve la jerarquía |
| p95 = p50 | Muy pocas peticiones | Los percentiles necesitan volumen: es la parte 3 del lab |
| Aparece un DNI completo | El enmascarador se aplicó a la salida pero no al prompt | Justo el punto del bloque 4 |
