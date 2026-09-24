# Esqueletos de sesión

> **Qué son.** El contrato de cada sesión, pactado en Cowork antes de escribir un solo archivo:
> guion en vivo minuto a minuto, alcance del laboratorio, demos, evaluación y —sobre todo— la
> lista de lo que **no** entra.
>
> **Cómo se usan.** La sesión de Claude Code lee el esqueleto y construye los archivos de la
> sesión tomándolo como contrato. Si algo contradice al esqueleto, **gana el esqueleto** o se
> renegocia en Cowork; no se improvisa en el momento.

---

## Índice

| Esqueleto | Sesión | Estado | Pasos del ROADMAP |
|---|---|---|---|
| [`sesion-01.md`](sesion-01.md) | Fundamentos de los agentes inteligentes | ✅ pactado | 3.1 – 3.5 |
| [`sesion-02.md`](sesion-02.md) | Ecosistema LangChain: prompts, cadenas y modelos | ✅ pactado | 3.6 – 3.10 |
| [`sesion-03.md`](sesion-03.md) | Herramientas, API externa y **Assignment A1** | ✅ pactado | 3.11 – 3.16 |
| [`sesion-04.md`](sesion-04.md) | Catálogo de 4 tools + MCP | ✅ pactado | 4.1 – 4.5 |
| [`sesion-05.md`](sesion-05.md) | Memoria contextual y RAG con Qdrant | ✅ pactado | 4.6 – 4.10 |
| [`sesion-06.md`](sesion-06.md) | Guardrails y límites de actuación | ✅ pactado | 4.11 – 4.15 |
| [`sesion-07.md`](sesion-07.md) | Hackathon y **Proyecto M2** | ✅ pactado | 4.16 – 4.19 |
| [`sesion-08.md`](sesion-08.md) | Despliegue en producción con HF Spaces | ✅ pactado | Fase 5 · S8 |
| [`sesion-09.md`](sesion-09.md) | Monitoreo y trazabilidad con Langfuse | ✅ pactado | Fase 5 · S9 |
| [`sesion-10.md`](sesion-10.md) | Optimización continua y evaluación | ✅ pactado | Fase 5 · S10 |
| [`sesion-11.md`](sesion-11.md) | Sustentación final · **Proyecto Integrador** | ✅ pactado | Fase 5 · S11 |
| [`seminario.md`](seminario.md) | Seminario Internacional · **panel de casos reales** | ✅ pactado | Fase 6 |
| [`bonus-foundry.md`](bonus-foundry.md) | Bonus · el mismo agente en Foundry | ✅ pactado | Fase 7 |

**Curso completo pactado: 11 sesiones + seminario = 72 h lectivas, más el bonus asíncrono.**
Coherencia verificada con `python docente/validar_materiales.py` (validación actual de rutas/sintaxis; el script histórico `validar_coherencia.py` no está versionado y su verificación pedagógica no es reproducible aquí); la revisión pedagógica que
un script no puede hacer está en [`VALIDACION-INTEGRAL.md`](VALIDACION-INTEGRAL.md).

---

## Convenciones comunes a las tres sesiones

| Convención | Detalle |
|---|---|
| **Hora de reloj** | La sesión en vivo son 3 h = **170 min de contenido + 10 min de pausa**. El reparto teoría/práctica de la malla se calcula sobre las 6 h completas; la pausa queda fuera de ese reparto |
| **Estructura** | 1 h pre-work asíncrono (teoría) + 3 h en vivo + 2 h de laboratorio (práctica) |
| **Pre-work verificable** | Cada sesión abre con algo que el alumno **ejecuta** antes de clase, no solo lee. Los bloqueos se descubren con margen |
| **Sección "qué no entra"** | Obligatoria en todo esqueleto. Es lo que impide que la sesión de Code se desborde |
| **Incrementalidad** | Cada laboratorio consume la salida del anterior. Si un lab no usa nada del previo, está mal diseñado |

---

## Tareas previas pendientes

Derivadas de los esqueletos ya pactados. **Van marcadas en `ROADMAP.md` por la sesión de Code**,
que es la única que escribe ese archivo.

### Antes de la Sesión 2

| # | Tarea | Por qué |
|---|---|---|
| a | `recursos/golden/consultas-<track>.json` — extraer las 20 consultas × 4 tracks de `docente/matriz_seleccion.py`, añadirles el campo `intencion`, y hacer que el script lea de ahí | **Una sola fuente para el L2 y el L4.** Si se duplican, derivan |
| b | `docente/verificar_ejercicio_pydantic.py` | Sostiene el pase de entrada con 15 equipos; revisar a ojo no escala |
| c | Corregir la taxonomía de telco en `docente/labs-incrementales.md` | Hoy lista `PORTABILIDAD` (tool **opcional**) y omite el consumo (tool **núcleo**) |
| d | Corregir "150 min" → "140 min" en `sesion-01.md` §5 | Los bloques declarados suman 140, no 150 |
| e | En el ROADMAP, corregir el paso **3.3**: la tercera demo de la S1 es *un modelo · cuatro industrias*, no *comparación de modelos* | Con D28 el curso usa un solo modelo: comparar modelos perdió sentido |

### Antes de la Sesión 3

| # | Tarea | Por qué |
|---|---|---|
| f | `recursos/rubricas/rubrica-a1.md` | La cita el assignment y la usa el docente al calificar |
| g | Anotar en `recursos/rubricas/` que el criterio de **observabilidad no aplica antes de la S9** | Evita calificar algo que todavía no se enseñó |
| h | Fijar fecha a la tarea **2B.19** del ROADMAP: **lunes de la semana 2** | Hoy está en ⏸️ sin vencimiento y bloquea la nota del Módulo 1 |

### Antes de la Sesión 4

| # | Tarea | Por qué |
|---|---|---|
| i | Añadir la opción `--tools <ruta>` a `docente/matriz_seleccion.py` | Hoy carga la **solución**; el alumno debe medir *su* catálogo |
| j | Corregir el pre-work de MCP en `docente/labs-incrementales.md` | Hoy pide construir un servidor MCP en 1 h |

### Antes de la Sesión 5

| # | Tarea | Por qué |
|---|---|---|
| k | Subir a **10** las consultas `OTRO` por track en `recursos/golden/` | El criterio del L5 pide 10 citas verificables y hoy hay 4 |
| l | Indexar las 4 colecciones de respaldo `kb-<track>-respaldo` **con el mismo `ingest.py`** | Es la red de seguridad decidida. Si se indexan con otro código, dejan de ser red |
| m | Anotar en `_memoria/DECISIONES.md` que la colección de respaldo **no contradice D10** | Mismo servicio, otra colección: no hay fallback de tecnología |

### Antes de la Sesión 6

| # | Tarea | Por qué |
|---|---|---|
| n | `docente/verificar_guardrails.py`, con `--simular` y código de salida | Sin instrumento, «0 filtraciones» es una opinión |
| o | Redactar los **15 ataques × 4 tracks** en `recursos/ataques/bateria-<track>.json` | Es el golden set de la S6 |
| p | Verificar que la lista de acciones prohibidas de cada track esté en `comun/prompts_industria.py` | El prompt es la primera capa; el código es la segunda |

### Antes de la Sesión 7

| # | Tarea | Por qué |
|---|---|---|
| q | `recursos/rubricas/rubrica-m2.md` | La cita el enunciado del Proyecto M2 |
| r | Plantillas de `INFORME-L7.md` y del documento de diseño | Sin plantilla, 15 informes con 15 estructuras |
| s | Recordatorio de `CHAOS_RATE=0.1` → `0.0` en `docente/cronograma.md`, en la fila de la S7 | Hoy solo está en la lista de verificación general |

---

### Antes de la Sesión 8

| # | Tarea | Por qué |
|---|---|---|
| t | **Javier:** verificar los límites del free tier de HF Spaces (R5) | Condiciona si caben 15 Spaces simultáneos |
| u | Desplegar el Space de referencia del docente | La demo 4 de la S8 se corre contra él |
| v | `docente/verificar_despliegue.py` — `/health` sin key, `/chat` con y sin key, desde fuera | Calificar 15 despliegues a mano no escala |
| w | Corregir el criterio del L8 en `docente/labs-incrementales.md` | Hoy no menciona que la invocación va autenticada |

### Antes de la Sesión 9

| # | Tarea | Por qué |
|---|---|---|
| x | *Hook* de enmascaramiento de PII en `comun/observability.py` | Hoy el callback envía el prompt tal cual a Langfuse |
| y | Script de generación de tráfico contra una URL pública | p50/p95 no significan nada con 3 peticiones |
| z | Verificar el consumo de unidades de Langfuse con 15 equipos | El plan Hobby da 50 000/mes y la S10 también consume |

### Antes de la Sesión 10

| # | Tarea | Por qué |
|---|---|---|
| aa | Añadir `respuesta_esperada` a los 30 casos × 4 tracks del golden set | Sin eso no existe el evaluator de exactitud |
| ab | `comun/evaluadores.py` con los 3 evaluators determinísticos | El alumno los usa, no los reescribe |
| ac | Comprobar las unidades de Langfuse que quedan tras la S9 | 30 casos × 2 versiones × 15 equipos |

### Antes de la Sesión 11

| # | Tarea | Por qué |
|---|---|---|
| ad | `recursos/rubricas/rubrica-final.md` | La usa el panel |
| ae | Plantilla del documento de diseño, 4 secciones | Sin plantilla, 15 documentos distintos |
| af | Checklist de entregables del panel, 1 página | Se usa durante la demo |
| ag | Calcular los minutos por equipo con el nº real de inscritos | La aritmética se hace antes, no el día |
| ah | Decidir si el panel lleva invitados externos. **Javier** | Afecta la convocatoria, no el contenido |

### Seminario Internacional · tareas de Javier, con fecha

| # | Tarea | Para cuándo |
|---|---|---|
| ai | **Convocar 3 panelistas** (el piso operativo son 2) | 3 semanas antes |
| aj | Enviar el brief de 1 página a cada panelista | al confirmar |
| ak | Confirmar asistencia y probar conexión de los remotos | 48 h antes |
| al | Curar las preguntas escritas de los equipos | 24 h antes |

### Bonus de Foundry

| # | Tarea | Por qué |
|---|---|---|
| am | **Re-verificar `langchain-azure-ai[hosting]`** contra un proyecto Foundry real | R8: es preview y sostiene los pasos 6 y 7 del bonus |
| an | Desplegar el proyecto Foundry compartido de la vía B y definir su cuota | Sin él, la vía sin tarjeta no existe |
| ao | Capturas del portal de Azure para `acceso-azure.md` | Sustituyen a la creación de recursos en la vía B |
| ap | Fijar la fecha de cierre del periodo del bonus | Las claves temporales necesitan vencimiento |

---

## Decisiones tomadas al pactar los esqueletos

Las que cambian documentos ya cerrados. El registro completo va en `_memoria/DECISIONES.md`.

| Sesión | Decisión |
|---|---|
| S1 | El L1 es **entorno + primer script**. 40 de sus 120 min se dedican a dejar entornos en verde |
| S1 | **El equipo propone su track, el docente balancea.** El track es irrevocable del L2 al L11 |
| S2 | Structured output se enseña **crudo primero**: se compara la invocación directa con `comun/structured.py`; el fallo reproducible usa simulación |
| S2 | **Pase de entrada de Pydantic:** sin el ejercicio entregado, no se hace el L2 |
| S2 | La taxonomía de intención del L2 se alinea **1:1 con las 4 tools núcleo del L4** |
| S3 | El bucle ReAct manual es **demo de 15 min**, no laboratorio |
| S3 | El A1 se construye el martes, se entrega el miércoles y **sustentan 4 equipos —uno por track— al inicio de la S4** |
| S3 | **Regla del piso:** si `prueba_tool.py` pasa los 3 escenarios y la docstring cumple A2, el equipo no baja de *Competente*, aunque el modelo no haya elegido la tool en la demo |
| S4 | **MCP se consume, no se construye:** el pre-work conecta el agente al servidor MCP que el simulador ya expone. Construir uno propio es reto opcional |
| S4 | La tool de **escritura** aparece en el L4 y exige confirmación explícita del usuario antes de ejecutarse |
| S5 | **El alumno indexa, con colección de respaldo** del docente por track. No es un fallback de tecnología: sigue siendo Qdrant |
| S6 | **15 ataques del curso + 5 propios.** Los 15 hacen comparable el «0 filtraciones»; los 5 enseñan a pensar como atacante |
| S7 | **Clínica, sin ataque cruzado.** El adversario es el entorno: `CHAOS_RATE=0.1` activado y anunciado por el docente |
| S7 | La demo **abre con el peor fallo que el equipo encontró y resolvió**, no con el camino feliz |
| S8 | El `/chat` del Space exige **API key propia del equipo**; `/health` queda público. Lo que se protege es la cuota de HF, no un secreto |
| S9 | Las trazas de Langfuse van con **PII enmascarada**, usando el mismo enmascarador del L6. Se pierde algo de depuración, y se dice |
| S10 | **Los 3 evaluators determinísticos califican; el LLM-as-judge es demo.** Su sesgo se enseña comparándolo con ellos sobre 10 casos |
| S10 | El golden set del L2 **es** el dataset de evaluación: 30 casos por track, usados por cuarta vez |
| S11 | **Contingencia:** con evidencia entregada 24 h antes, si el Space duerme el día de la demo se sustenta en local sin penalización |
| Seminario | **Panel de casos reales**, con brief escrito a los panelistas, preguntas curadas 48 h antes y documento de contraste. Formativo, no ponderado |
| Bonus | **Ambas vías de acceso a Azure documentadas**: suscripción propia (recomendada) y proyecto compartido del docente para quien no registre tarjeta |
