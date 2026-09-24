# Rúbrica · Proyecto Integrador Final — 100 % del Módulo 3

> La cita `modulo-3-produccion/sesion-11-sustentacion-final/proyecto-integrador.md`. La usa el
> panel para calificar la sustentación de la Sesión 11
> (`docente/esqueletos/sesion-11.md`, sección 8).
>
> **Vocabulario de los 4 niveles**, común a las rúbricas del curso: **Insuficiente** (no cumple
> el mínimo) · **En desarrollo** (cumple lo mínimo, con huecos visibles) · **Competente** (cumple
> todo lo pedido, sin lujos) · **Destacado** (cumple todo y además defiende decisiones no obvias).
>
> **Es la única evaluación del curso donde los 5 criterios institucionales aplican completos**
> — hasta la S9 no existía observabilidad que calificar.

---

## Regla de contingencia — Space caído el día de la demo

| Momento | Qué |
|---|---|
| **24 h antes** | El equipo entrega: URL pública, API key para el panel, captura de una traza en Langfuse, salida de `docente/verificar_despliegue.py` en verde |
| El día de la demo, si el Space responde | Se sustenta contra la URL pública |
| El día de la demo, si el Space duerme o falla | Se sustenta **en local, sin penalización** |

**El fundamento es el mismo de la regla del piso del A1:** la nota evalúa el diseño, la
evidencia y la argumentación — no la disponibilidad de un tier gratuito que el equipo no
controla. Si el equipo **no** entregó la evidencia de las 24 h y además el Space falla, ahí sí
hay penalización: el fallo no es del free tier, es de no haber previsto que podía fallar.

---

## Los 5 criterios y su peso

| Criterio | Peso | Qué se mira |
|---|---|---|
| Funcionalidad | 25 % | La demo end-to-end corre: consulta → tool o RAG → respuesta citada |
| Diseño de tools y prompts | 20 % | Las 4 tools con docstrings A2, el system prompt del track, el retriever acotado |
| Guardrails y manejo de errores | 20 % | PII enmascarada, acciones prohibidas, degradación limpia ante fallo |
| Observabilidad y evaluación | 20 % | Trazas reales del Space, 30 casos evaluados, mejora v1→v2 argumentada |
| Comunicación técnica | 15 % | Los 4 movimientos de la demo (S11 §4) y el Q&A |

---

## Funcionalidad — 25 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | La demo no corre de punta a punta, o necesita intervención del equipo fuera del guion |
| En desarrollo | Corre el camino feliz, pero al menos una tool o el RAG falla ante una variación menor de la consulta |
| Competente | La demo end-to-end corre: consulta → tool o RAG → respuesta citada, con el agente desplegado |
| Destacado | Además, el equipo muestra su peor caso conocido en vivo y explica por qué falla — no solo el camino feliz |

## Diseño de tools y prompts — 20 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | Alguna tool no tiene `args_schema`, o el system prompt no usa `get_system_prompt(track)` |
| En desarrollo | Las 4 tools funcionan, pero al menos una docstring no dice "cuándo NO usarla" (regla A2) |
| Competente | Las 4 tools núcleo + el retriever cumplen A2, el system prompt del track está intacto (identidad, jerga, límites, A6) |
| Destacado | El equipo argumenta, con datos de `docente/matriz_seleccion.py`, por qué su catálogo quedó en 4 tools y no más |

## Guardrails y manejo de errores — 20 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | Hay al menos una filtración de los 15 ataques del L6 sin corregir |
| En desarrollo | 0 filtraciones se sostiene, pero la degradación ante un fallo del simulador no es limpia (bucle, mensaje críptico, o silencio) |
| Competente | 0 filtraciones se sostiene, PII enmascarada tanto en la salida al cliente (L6) como en las trazas (L9), y el agente degrada limpiamente ante un fallo del servicio |
| Destacado | Además, el equipo explica la diferencia entre proteger la salida visible y proteger la telemetría, y por qué ambas son la misma regla (S9 bloque 4) |

## Observabilidad y evaluación — 20 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | No hay trazas del Space real, o el golden set no corrió con los 3 evaluators |
| En desarrollo | Hay trazas y evaluación, pero el equipo no puede nombrar qué cambio produjo la diferencia entre v1 y v2 |
| Competente | Trazas reales del Space, 30 casos evaluados con los 3 evaluators determinísticos, y una mejora v1→v2 (o un experimento negativo) argumentada con el cambio que la causó |
| Destacado | El equipo distingue explícitamente el rol del juez (demo) del rol de los evaluators determinísticos (nota), y por qué esa distinción importa |

## Comunicación técnica — 15 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | La demo se pasa del tiempo asignado o el equipo no puede sostener el Q&A |
| En desarrollo | Cumple el tiempo, pero el movimiento 3 (decisión de arquitectura) se queda en "usamos X" sin alternativa descartada ni criterio |
| Competente | Cumple los 4 movimientos del guion de demo (S11 §4) y defiende con claridad ante preguntas del panel |
| Destacado | El equipo muestra dónde **no** funciona su sistema y por qué, en vez de una demo que salió perfecta — es la marca del Destacado (S11 §5) |

---

## Cómo se calcula la nota final

Nota = suma ponderada de los 5 criterios, cada uno en escala 1 (Insuficiente) a 4 (Destacado),
sobre 4, salvo que la **regla de contingencia** de más arriba aplique — en ese caso una demo
local por caída del Space no penaliza ningún criterio, siempre que el equipo haya entregado la
evidencia de las 24 h antes.

## Nomenclatura entre módulos

A1/M2 usan Insuficiente, Básico, Competente y Sobresaliente; la rúbrica final usa
Insuficiente, En desarrollo, Competente y Destacado. La correspondencia ordinal es 1–4.
Aplicar los pesos, criterios y descriptores de la rúbrica correspondiente a cada evaluación.
