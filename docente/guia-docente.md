# Guía del docente — cómo dictar cada sesión

> **Qué es esto.** Un resumen operativo, sesión por sesión, para tener a mano **mientras se
> dicta**: horario, guion minuto a minuto y los errores más frecuentes. Se deriva de los
> contratos pactados en `docente/esqueletos/` — **no los reemplaza**. Ante cualquier duda de
> contenido, guion completo o justificación de una decisión, el esqueleto de la sesión es la
> fuente de verdad; esta guía es el resumen de mesa, no el original.
>
> Si un esqueleto cambia, esta guía queda desactualizada hasta que alguien la revise contra el
> esqueleto de nuevo — no hay generación automática. Es el mismo riesgo que corren
> `docente/cronograma.md` y `docente/labs-incrementales.md`, y se gestiona igual: revisarla
> quede como parte de "cerrar un entregable" cuando se toque un esqueleto (`CLAUDE.md`).

---

## Antes de dictar cualquier sesión

- [ ] `docente/checklist-pre-sesion.md` completado (los 4 servicios SaaS en verde).
- [ ] Leído el esqueleto completo de la sesión en `docente/esqueletos/sesion-NN.md` — esta guía
      es un resumen, no sustituye una lectura previa la primera vez que se dicta.
- [ ] Revisados los "errores esperables" de la sesión anterior: si algo salió mal ahí, puede
      seguir arrastrándose.

---

## Panorama de las 6 semanas

| Semana | Día | Sesión | Horas T/P | Hito |
|---|---|---|---|---|
| 1 | martes | S1 · Fundamentos | 3.5 / 2.5 | Test 1 · elección de track |
| 1 | jueves | S2 · Ecosistema LangChain | 3.0 / 3.0 | Test 2 · pase de entrada Pydantic |
| 2 | martes | S3 · Tools y API externa | 2.5 / 3.5 | **Assignment A1** (100 % Módulo 1) |
| 2 | jueves | S4 · Catálogo de 4 tools | 2.5 / 3.5 | Sustentación A1 · Avance 1 |
| 3 | martes | S5 · Memoria + RAG | 3.0 / 3.0 | Avance 2 · Qdrant operativo |
| 3 | jueves | S6 · Guardrails | 2.5 / 3.5 | Avance 3 |
| 4 | martes | S7 · Hackathon M2 | 1.5 / 4.5 | **Proyecto M2** (100 % Módulo 2) |
| 4 | jueves | S8 · Despliegue HF Spaces | 2.5 / 3.5 | Avance 1 del M3 |
| 5 | martes | S9 · Observabilidad Langfuse | 2.5 / 3.5 | Avance 2 del M3 |
| 5 | jueves | S10 · Evaluación y optimización | 2.5 / 3.5 | Avance 3 del M3 |
| 6 | martes | S11 · Sustentación final | 1.5 / 4.5 | **Proyecto Integrador** (100 % Módulo 3) |
| 6 | jueves | Seminario Internacional | 1.5 / 4.5 | Documento de contraste (formativo) |
| asíncrono | — | Bonus Foundry | ~2 / ~4 | No ponderado |

---

## Sesión 1 · Fundamentos de los agentes inteligentes

**Esqueleto:** [`sesion-01.md`](esqueletos/sesion-01.md) · **Carpeta:** `modulo-1-fundamentos/sesion-01-fundamentos-agentes/`

| # | Bloque | Min |
|---|---|---|
| 0 | Apertura y mapa del curso | 10 |
| 1 | Un LLM solo no es un agente (demo de la tarifa inventada) | 30 |
| 2 | Agente = percepción → razonamiento → acción → entorno | 30 |
| 3 | Workflow vs agente | 20 |
| — | Pausa | 10 |
| 4 | Anatomía de LangChain 1.x | 30 |
| 5 | Modelos abiertos vs cerrados (D28, elegido por medición) | 20 |
| 6 | `comun/provider.py` en vivo | 15 |
| 7 | Test 1 + elección de track | 15 |

**No olvidar:** el antipatrón se rompe con una demo en vivo (preguntar dos veces una tarifa),
nunca con una diapositiva. Elección de track: el equipo propone, el docente balancea para que
los 4 tracks queden representados y Banca no caiga en el equipo más débil.

**Errores esperables más frecuentes:** `401` de Hugging Face (token sin permiso de inferencia) ·
`ModuleNotFoundError: comun` (no se ejecuta desde la raíz) · el modelo responde en inglés (falta
el `system` en español).

---

## Sesión 2 · Ecosistema LangChain: prompts, cadenas y modelos

**Esqueleto:** [`sesion-02.md`](esqueletos/sesion-02.md) · **Carpeta:** `modulo-1-fundamentos/sesion-02-ecosistema-langchain/`

> ⚠️ Pase de entrada obligatorio: el ejercicio de Pydantic (`Reclamo`) se entrega **antes** de
> esta sesión. Sin él, el equipo dedica el laboratorio a resolverlo, no al L2.

| # | Bloque | Min |
|---|---|---|
| 0 | De "primer llamado" a "primer contrato" | 5 |
| 1 | Mensajes, roles y *statelessness* | 25 |
| 2 | Rol + Contexto + Tarea + Formato | 25 |
| 3 | Few-shot (regla A5) | 20 |
| 4 | Structured output: la demo del fallo (en vivo) | 25 |
| 5 | `comun/structured.py` (regla A3) | 20 |
| — | Pausa | 10 |
| 6 | Práctica guiada: esquema `Intencion` del track | 35 |
| 7 | Test 2 | 15 |

**No olvidar:** el bloque 4 tiene que fallar en vivo (Enum inventado, campo vacío) antes de
mostrar la solución del bloque 5 — es el bloque que decide la sesión.

**Errores esperables más frecuentes:** el modelo inventa un valor de Enum (faltan ejemplos
few-shot) · acierto alto en las 20 del curso pero bajo en las 5 propias (consultas ambiguas) ·
todo se clasifica como `OTRO` (los `description` no distinguen entre categorías).

---

## Sesión 3 · Herramientas, integración externa y Assignment A1

**Esqueleto:** [`sesion-03.md`](esqueletos/sesion-03.md) · **Carpeta:** `modulo-1-fundamentos/sesion-03-tools-api-externa/`

> ⚠️ **Bloqueante con fecha:** simulador desplegado y respondiendo, API key por equipo repartida,
> `CHAOS_RATE=0.0` confirmado — todo para el **lunes de la semana 2**, no el día de la sesión.

| # | Bloque | Min |
|---|---|---|
| 0 | Hoy el modelo deja de saber y empieza a consultar | 5 |
| 1 | Function calling: quién genera y quién ejecuta | 25 |
| 2 | La docstring es el prompt (regla A2) | 25 |
| 3 | Errores redactados para el modelo (regla A4) | 20 |
| 4 | Demo: bucle ReAct manual → `create_agent()` | 15 |
| — | Pausa | 10 |
| 5 | Práctica guiada: el primer `@tool` contra el simulador | 40 |
| 6 | Los 3 escenarios con `?_fallo=` | 25 |
| 7 | Rúbrica del A1 y reparto de trabajo | 15 |

**No olvidar:** es la sesión más cara del módulo — el A1 es el 100 % de la nota del Módulo 1.
La regla del piso: si `prueba_tool.py` pasa los 3 escenarios y la docstring cumple A2, el equipo
no baja de Competente aunque el modelo no haya elegido la tool en la demo.

**Errores esperables más frecuentes:** `401` del simulador (API key mal copiada, no reintentar —
reemitir) · el agente reintenta sin parar ante el 503 (falta tope de iteraciones) · funciona con
`DATA_SOURCE=csv` pero no contra la API (Space caído o key no repartida).

---

## Sesión 4 · Tools e integración de herramientas

**Esqueleto:** [`sesion-04.md`](esqueletos/sesion-04.md) · **Carpeta:** `modulo-2-agentes-avanzados/sesion-04-tools-multiples/`

> ⚠️ **Decisión pendiente de Javier, no de Code (`DECISION-PENDIENTE` en el esqueleto):** los
> primeros 20 min son la sustentación del A1, y sumados a los 180 min del guion dan 200 —
> descuadre de 20 min sin resolver. El esqueleto propone 3 salidas (A: la sustentación no
> computa en las 6 h de la S4 · B: recortar 20 min del guion · C: sustentación asíncrona
> grabada) y dice explícitamente que **la decide Javier**. Hasta que se resuelva, el guion de
> abajo asume la salida A.

| # | Bloque | Min |
|---|---|---|
| — | Sustentación del A1 (4 equipos, 5 min c/u) | 20 |
| 0 | De una tool a cuatro | 5 |
| 1 | Catálogo y responsabilidad única | 20 |
| 2 | Selección dinámica: cómo elige y por qué falla | 25 |
| 3 | Por qué 4 y no 6 (regla A1) | 20 |
| 4 | Idempotencia y tope de iteraciones (regla A4) | 20 |
| — | Pausa | 10 |
| 5 | Laboratorio guiado: completar el catálogo | 45 |
| 6 | Medir: correr la matriz de selección propia | 25 |
| 7 | Avance 1 del proyecto | 10 |

**No olvidar:** aclarar que `proyecto-final/` en el repo del curso es la referencia del docente,
nunca el repositorio del alumno — el alumno mide su propio catálogo con
`--tools lab/<track>/domain_tools.py`, no contra la referencia.

**Errores esperables más frecuentes:** acierto < 85 % concentrado en dos tools (docstrings que
se solapan) · dos reclamos duplicados (tool de escritura sin confirmación) · MCP no conecta
(transporte mal elegido o URL del Space).

---

## Sesión 5 · Memoria contextual y RAG con Qdrant Cloud

**Esqueleto:** [`sesion-05.md`](esqueletos/sesion-05.md) · **Carpeta:** `modulo-2-agentes-avanzados/sesion-05-memoria-rag/`

> ⚠️ **Bloqueante con fecha:** cluster de Qdrant Healthy en cada equipo y colecciones de respaldo
> indexadas, para el **lunes de la semana 3**. Es la sesión más frágil operativamente del curso.

| # | Bloque | Min |
|---|---|---|
| 0 | El agente que no recuerda y el que no sabe | 5 |
| 1 | Estado conversacional y `thread_id` | 20 |
| 2 | Embeddings aplicados al dominio | 15 |
| 3 | Chunking y su trade-off | 20 |
| 4 | Qdrant: colección, punto, payload, filtros | 20 |
| 5 | RAG tradicional vs RAG agéntico | 25 |
| 6 | Salvaguarda A6 y la fundamentación | 15 |
| — | Pausa | 10 |
| 7 | Laboratorio guiado: ingesta del corpus del track | 35 |
| 8 | Avance 2 del proyecto | 15 |

**No olvidar la demo clave** (`demo-parametrico-vs-recuperable.py`, 5 minutos, no se recorta):
preguntar una tarifa, editar el documento en Qdrant, preguntar lo mismo y mostrar que la
respuesta cambia citando el mismo documento — es la demostración física de por qué el
conocimiento va al RAG y no al fine-tuning (D21).

**Errores esperables más frecuentes:** la ingesta falla a mitad (cuota de embeddings agotada →
usar la colección de respaldo) · el agente busca ante "hola" (falta "cuándo NO" en la docstring
del retriever) · el turno 3 no recuerda (revisar `memory.py`).

---

## Sesión 6 · Automatización, asistentes y guardrails

**Esqueleto:** [`sesion-06.md`](esqueletos/sesion-06.md) · **Carpeta:** `modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/`

| # | Bloque | Min |
|---|---|---|
| 0 | Lo que el agente NO debe hacer | 5 |
| 1 | Inyección de prompt | 25 |
| 2 | PII y Ley 29733 | 20 |
| 3 | Límites de actuación y escalamiento | 20 |
| 4 | Middleware: dónde se enganchan (+ few-shot A5 y mención de LangGraph) | 20 |
| — | Pausa | 10 |
| 5 | Laboratorio guiado: `guardrails.py` | 50 |
| 6 | Correr la batería de 15 ataques | 20 |
| 7 | Avance 3 del proyecto | 10 |

**No olvidar:** abrir la sesión conectándola con la S5 (bloque 0bis del esqueleto) — el corpus
que el agente empezó a citar es también una superficie de ataque nueva, y el filtro por
metadatos que ya escribieron es su primer guardrail sin saberlo. Al cerrar el bloque 4, la
mención de 2-3 min de LangGraph (por qué este curso no lo cubre) responde una pregunta que el
aula va a hacer de todas formas.

**Errores esperables más frecuentes:** un DNI aparece en la respuesta (falta el guardrail de
salida) · el agente promete una compensación (la prohibición está solo en el prompt, no en
código) · el escalamiento nunca se dispara (falta una condición que lo active).

---

## Sesión 7 · Hackathon, clínica y sustentación del Proyecto M2

**Esqueleto:** [`sesion-07.md`](esqueletos/sesion-07.md) · **Carpeta:** `modulo-2-agentes-avanzados/sesion-07-hackathon-m2/`

> ⚠️ Anunciar `CHAOS_RATE=0.1` **antes** de activarlo (es la sesión que vale el 100 % del
> Módulo 2 — un fallo aleatorio no anunciado sería una trampa) y volver a `0.0` al terminar.

| # | Bloque | Min |
|---|---|---|
| 0 | Cómo se prueba lo no determinístico (invariantes, familias, repetición) | 30 |
| — | Pausa | 10 |
| 1 | Clínica con el caos activado | 45 |
| 2 | Ronda de demos | 90 |
| 3 | Cierre y entrega | 5 |

**No olvidar la aritmética de la ronda:** con 15 equipos son 4 min de demo + 2 de preguntas, al
límite sin margen. Si el aula supera los 15 equipos, la ronda no cabe y se parte entre la S7 y
los primeros 20 min de la S8 (mismo patrón que la sustentación del A1).

**Errores esperables más frecuentes:** el informe describe casos en vez de mostrar trazas reales
· los 10 casos son todos de la familia "dato ausente" (exigir al menos 2 de cada una de las 4
familias) · el equipo culpa al caos de todo en vez de distinguir fallo del entorno de fallo
propio.

---

## Sesión 8 · Despliegue en producción con HF Spaces

**Esqueleto:** [`sesion-08.md`](esqueletos/sesion-08.md) · **Carpeta:** `modulo-3-produccion/sesion-08-despliegue-hf-spaces/`

> ⚠️ Verificar antes de la semana 4: límites del free tier de HF Spaces (riesgo R5, tarea de
> Javier) y el Space de referencia del docente ya desplegado (la demo 4 corre contra él).

| # | Bloque | Min |
|---|---|---|
| 0 | Qué es "producción" para un agente | 10 |
| 1 | 12-Factor y config por entorno | 15 |
| 2 | El Dockerfile, línea por línea (no se ejecuta en local, P2) | 20 |
| 3 | FastAPI: `/chat` y `/health` — qué va autenticado | 20 |
| 4 | Secretos en la nube | 15 |
| 5 | *Cold start* y el free tier | 10 |
| — | Pausa | 10 |
| 6 | Práctica: `api.py` + `Dockerfile` | 45 |
| 7 | Desplegar y probar desde fuera | 35 |

**No olvidar:** `/health` va sin credencial (la plataforma lo necesita para saber si el Space
vive); `/chat` exige `X-API-Key` — se protege la cuota, no un secreto de negocio. Verificar con
`docente/verificar_despliegue.py`.

**Errores esperables más frecuentes:** el Space queda en *Build error* (falta una dependencia en
`requirements.txt`) · `401` desde fuera (la key no se cargó como Space secret) · un token
aparece en el historial de git (revocar y regenerar, no basta con borrar el commit).

---

## Sesión 9 · Monitoreo y trazabilidad con Langfuse

**Esqueleto:** [`sesion-09.md`](esqueletos/sesion-09.md) · **Carpeta:** `modulo-3-produccion/sesion-09-observabilidad-langfuse/`

> ⚠️ **Bloqueante:** proyecto de Langfuse Cloud operativo con los 2 integrantes, para el lunes de
> la semana 5. Desviación documentada del PDF (riesgo R6): el sílabo nombra LangSmith
> (propietario); el curso usa Langfuse por P1 — decirlo en 2 minutos de arquitectura.

| # | Bloque | Min |
|---|---|---|
| 0 | El agente ya está desplegado. ¿Y ahora qué hace? | 5 |
| 1 | Logs vs métricas vs trazas | 20 |
| 2 | Anatomía de una traza de agente | 25 |
| 3 | Latencia p50/p95 y costo por ejecución | 20 |
| 4 | PII dentro de una traza (decisión: se enmascara igual que en el L6) | 20 |
| — | Pausa | 10 |
| 5 | Práctica: instrumentar y redesplegar | 40 |
| 6 | Leer trazas reales y hallar 2 cuellos de botella | 40 |

**No olvidar:** la demo 3 (PII con y sin enmascarar) se corre **antes** de que el alumno
instrumente el suyo — ver el DNI completo en una traza ajena convence más que cualquier
explicación.

**Errores esperables más frecuentes:** no aparece ninguna traza (claves no cargadas como Space
secrets) · la traza tiene un solo span (el callback se pasó al modelo, no al agente) · aparece
un DNI completo (el enmascarador se aplicó a la salida pero no al prompt).

---

## Sesión 10 · Optimización continua y evaluación

**Esqueleto:** [`sesion-10.md`](esqueletos/sesion-10.md) · **Carpeta:** `modulo-3-produccion/sesion-10-evaluacion-optimizacion/`

| # | Bloque | Min |
|---|---|---|
| 0 | Mejorar con evidencia, no con intuición | 5 |
| 1 | El golden dataset era el de siempre | 15 |
| 2 | Los 3 evaluators determinísticos | 25 |
| 3 | LLM-as-judge y sus sesgos | 25 |
| 4 | A/B de prompts: cuándo una mejora es real | 20 |
| — | Pausa | 10 |
| 5 | Práctica: los 30 casos en Langfuse Datasets | 35 |
| 6 | Optimizar y medir v2 | 45 |

**No olvidar:** decir explícitamente que las 30 consultas del golden set son las mismas que
alimentaron el L2 y el L4 — el alumno lleva nueve sesiones usándolas sin saber que eran un
conjunto de evaluación desde el primer día. **El juez es demo; la nota la sostienen los 3
evaluators determinísticos.**

**Errores esperables más frecuentes:** v2 mejora 2 puntos y el equipo lo celebra (ruido de
muestreo con 30 casos — correr otra vez) · el juez aprueba todo (autocomplacencia) ·
groundedness = 100 % siempre (el evaluator solo comprueba que hay cita, no que la sostenga).

---

## Sesión 11 · Aplicación final y sustentación

**Esqueleto:** [`sesion-11.md`](esqueletos/sesion-11.md) · **Carpeta:** `modulo-3-produccion/sesion-11-sustentacion-final/`

> ⚠️ **Entrega anticipada, 24 h antes:** URL pública, API key para el panel, captura de una
> traza en Langfuse, y `docente/verificar_despliegue.py` en verde — condición de la regla de
> contingencia si el Space cae el día de la demo.

| # | Bloque | Min |
|---|---|---|
| 0 | Cómo se argumenta ante un panel | 30 |
| — | Pausa | 10 |
| 1 | Ensayo cronometrado por equipo | 30 |
| 2 | Sustentaciones ante panel | 105 |
| 3 | Cierre del módulo (se libera el bonus de Foundry) | 5 |

**No olvidar la aritmética de la ronda antes del día** (tarea ag de Javier, con el número real
de inscritos): 8 min por equipo es el piso — por debajo no hay Q&A de verdad. Regla de
contingencia: si el Space cae y el equipo entregó la evidencia de 24 h, se sustenta en local
**sin penalización**; si no la entregó y además el Space falla, ahí sí hay penalización.

**Errores esperables más frecuentes:** la demo narra el código en vez de argumentar una decisión
(no se preparó el movimiento 3) · el Space duerme justo al empezar (despertarlo 5 min antes,
está en el checklist del panel) · el cliente web no hace streaming, solo espera (se pierde el
objetivo 1, se anota pero no invalida la demo).

---

## Seminario Internacional

**Esqueleto:** [`seminario.md`](esqueletos/seminario.md) · **Carpeta:** `modulo-3-produccion/seminario-internacional/`

Ver [`guion-docente.md`](../modulo-3-produccion/seminario-internacional/guion-docente.md) de la
propia sesión — ya es una guía de conducción completa (tiempos, curaduría de preguntas, Plan B
si solo llega un panelista) y no se duplica aquí.

---

## Bonus · El mismo agente en Microsoft Foundry

**Esqueleto:** [`bonus-foundry.md`](esqueletos/bonus-foundry.md) · **Carpeta:** `modulo-4-plus-foundry/`

Asíncrono, autoguiado, no ponderado — no hay guion de docente en vivo que dictar. La única
acción del docente es liberar el bloque al cerrar la S11 y estar disponible para la asesoría de
1 h opcional que menciona `docente/cronograma.md`.

> ⚠️ Antes de liberarlo cada edición: re-verificar `langchain-azure-ai[hosting]` contra un
> proyecto Foundry real (riesgo R8, tarea am) — es un paquete en preview.

---

## Decisiones pendientes que el docente debe cerrar antes de dictar

Estas no las resuelve Code — están señaladas así en sus propios esqueletos:

| Sesión | Qué falta decidir | Dónde está el detalle |
|---|---|---|
| S4 | El descuadre de 20 min entre la sustentación del A1 y el guion de 180 min (3 salidas propuestas) | `sesion-04.md` §4, nota `DECISION-PENDIENTE` |
| Bonus Foundry | Si el proyecto compartido de la Vía B ya tiene cuota definida y fecha de cierre | `bonus-foundry.md` §10, tareas an/ap |
| Seminario | Convocatoria de panelistas, confirmación y curaduría final de preguntas | `guion-docente.md` del Seminario, tareas ai-aj-ak-al |
