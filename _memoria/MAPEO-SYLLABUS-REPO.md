# Mapeo de trazabilidad: Syllabus "IA Agent Building" ↔ Repo `langchain-for-beginners`

> Responde al punto 2 del encargo: qué lecciones del repo cumplen el syllabus
> y qué lecciones del repo conviene agregar aunque no estén en la malla.

Leyenda de cobertura:
`COMPLETA` el repo cubre el tema y sobra material ·
`PARCIAL` el repo cubre parte, hay que escribir el resto ·
`NULA` no existe nada en el repo, se escribe desde cero ·
`AULA` no es contenido técnico, es gestión de aula

---

## A. Trazabilidad sesión por sesión

### Sesión 1 — Fundamentos de los agentes inteligentes · `PARCIAL`

| Tema del PDF | Fuente en el repo | Estado |
|---|---|---|
| ¿Qué es un agente? Percepción, razonamiento, acción, entorno | `05-agents/README.md` §"What Are Agents?" (está en la sesión 5 del repo, se **adelanta** el marco conceptual) | PARCIAL |
| Agentes basados en LLM y casos de uso iniciales | `01-introduction/README.md` §"Real-World Applications" | COMPLETA |
| Instalación y preparación del entorno (Python, venv, dependencias) | `00-course-setup/README.md` completo | COMPLETA (reescribir para HF/Foundry) |
| Primer script con LangChain | `01-introduction/code/01_hello_world.py`, `02_message_types.py`, `03_model_comparison.py` | COMPLETA |

**Se escribe desde cero:** el marco teórico agente = percepción → razonamiento → acción → entorno,
y la taxonomía workflow vs agente, que el repo asume implícito.
**Se adapta:** `00-course-setup` cambia GitHub Models por HF + Foundry.

---

### Sesión 2 — Ecosistema LangChain: prompts, cadenas y modelos · `COMPLETA`

| Tema del PDF | Fuente en el repo | Estado |
|---|---|---|
| Modelos, prompts y cadenas | `02-chat-models/README.md` + `03-prompts-messages-outputs/README.md` | COMPLETA |
| Diseño de prompts y plantillas reutilizables (Rol + Contexto + Tarea + Formato) | `03/code/03_basic_template.py`, `04_template_formats.py`, `05_few_shot.py`, `06_composition.py` | COMPLETA |
| Flujos básicos: entrada → prompt → modelo → salida | `03/code/01_messages_vs_templates.py` | COMPLETA |
| Output parsers / estructuración de la respuesta | `03/code/07_structured_output.py`, `08_pydantic_schemas.py` | COMPLETA |

> El repo **sobra** en esta sesión: 8 ejemplos de código + 4 samples + 2 soluciones para 3 horas de clase.
> Se seleccionan 4 y el resto pasa a material asíncrono opcional.

---

### Sesión 3 — Herramientas, integración externa y sustentación A1 · `COMPLETA`

| Tema del PDF | Fuente en el repo | Estado |
|---|---|---|
| Herramientas en LangChain para ampliar el agente | `04-function-calling-tools/README.md` + `code/01_simple_tool.py`, `02_tool_calling.py`, `03_tool_execution.py` | COMPLETA |
| Integración con API externa: variables de entorno, parsing JSON y errores | `04/solution/weather_tool.py` — **calza casi 1:1 con la referencia a OpenWeatherMap del PDF** | COMPLETA |
| Construcción y prueba documentada de un agente básico (mín. 3 escenarios) | `05-agents/code/01_create_agent_basic.py` | COMPLETA |

---

### Sesión 4 — Tools e integración de herramientas · `COMPLETA`

| Tema del PDF | Fuente en el repo | Estado |
|---|---|---|
| Concepto de tools: ampliación de capacidades | `04-function-calling-tools/README.md` §"The Paradigm Shift" | COMPLETA |
| Integración de múltiples herramientas y selección dinámica | `04/code/04_multiple_tools.py`, `05-agents/code/02_create_agent_multi_tool.py` | COMPLETA |
| Conexión con APIs externas y fuentes de datos | `04/solution/travel_assistant.py`, `05/solution/research_agent.py` | COMPLETA |
| Avance 1 del proyecto: caso de uso y herramientas necesarias | — | AULA |

**Adición del repo (no está en la malla):** `06-mcp` como pre-work asíncrono — hoy es la forma
estándar de conectar tools externas y es alto valor diferencial para el egresado.

---

### Sesión 5 — Memoria contextual y arquitecturas RAG · `COMPLETA`

| Tema del PDF | Fuente en el repo | Estado |
|---|---|---|
| Memoria contextual: continuidad y estado entre interacciones | `02/code/01_multi_turn.py` + `05-agents/code/03_agent_with_memory.py` | COMPLETA |
| Fundamentos de RAG | `08-agentic-rag-systems/README.md` + `code/01a_traditional_rag.py`, `02_agentic_rag.py` | COMPLETA |
| Bases de datos vectoriales y recuperación semántica | `07-documents-embeddings-semantic-search/` (9 code + 6 samples) | COMPLETA |
| Avance 2 del proyecto: memoria y/o RAG en la solución | — | AULA |

**Cambio respecto del repo:** se sustituye `InMemoryVectorStore` por **Qdrant Cloud** (D09), sin fallback (D10),
y los embeddings de Azure por `intfloat/multilingual-e5-large` vía HF Inference API (D15).
El repo no cubre ningún vector store persistente ni gestionado.

---

### Sesión 6 — Automatización de procesos y asistentes · `PARCIAL`

| Tema del PDF | Fuente en el repo | Estado |
|---|---|---|
| Diseño de agentes para automatizar procesos reales | `05-agents/solution/planning_agent.py` | PARCIAL |
| Construcción de asistentes orientados a usuarios | `08/solution/conversational_rag.py` | COMPLETA |
| **Buenas prácticas: validación de entradas y límites de actuación** | `05-agents/code/04_agent_with_middleware.py` (solo el mecanismo, no las prácticas) | **PARCIAL** |
| Avance 3 del proyecto: prototipo funcional | — | AULA |

**Se escribe desde cero:** guardrails de entrada y salida, detección y enmascaramiento de PII/DNI,
límites de actuación (qué NO puede hacer el agente), inyección de prompts, y política de escalamiento
a humano. Crítico para banca y seguros. El repo no lo cubre.

---

### Sesión 7 — Hackathon y sustentación del proyecto M2 · `AULA`

Sin contraparte técnica en el repo. Se aporta: guion de clínica de proyectos,
batería de **pruebas de estrés del agente** (casos extremos, prompts ambiguos, tool failures,
alucinación forzada) y rúbrica de demo.
Insumo parcial: `06-mcp/code/04_mcp_error_handling.py` y `02/code/05_error_handling.py`.

---

### Sesión 8 — Despliegue de agentes en producción · `PARCIAL`

| Tema del PDF | Fuente | Estado |
|---|---|---|
| Preparación del agente para entornos productivos | `09-deploy-to-microsoft-foundry/README.md` Steps 1–4 — **el concepto sirve, la plataforma no** | PARCIAL |
| Variables de entorno, credenciales y dependencias | `09/README.md` Step 2–3 + `.env.example` | COMPLETA |
| Opciones de despliegue (servicios cloud, contenedores) | — | **NULA** |
| Avance 1 del proyecto M3: arquitectura de despliegue | — | AULA |

**Cambio de plataforma (D16):** el repo despliega en Foundry; el curso despliega en **Hugging Face Spaces**
con Docker + FastAPI, porque Foundry se pospone al bloque plus (P4). Se escribe desde cero:
`Dockerfile`, capa FastAPI (`/chat`, `/health`), gestión de *Space secrets* y despliegue por `git push`.
Lo único reutilizable del cap. 09 es el discurso conceptual sobre qué significa "producción" para un agente.

---

### Sesión 9 — Monitoreo y trazabilidad · `NULA`

**No existe nada de observabilidad en el repo.** Se escribe 100 % desde cero, sobre **Langfuse Cloud** (D05 v2):
anatomía de un *trace* y un *span*, instrumentación con el callback de Langfuse, inspección de prompts y
tool calls, latencia y costo por paso, identificación de cuellos de botella sobre el agente ya desplegado.

> **Desviación documentada del PDF:** la malla nombra *LangSmith*. Se cumple el mismo objetivo de
> aprendizaje —observabilidad y trazabilidad de agentes— con la herramienta open source equivalente,
> por el principio P1 del curso. Registrado como riesgo R6.

---

### Sesión 10 — Optimización continua y evaluación · `NULA`

También desde cero: datasets de evaluación en **Langfuse Datasets**, evaluators determinísticos,
LLM-as-judge, métricas de calidad (exactitud, groundedness, tasa de uso correcto de tools),
comparación de versiones de prompt y ciclo de mejora basado en trazas reales. Complemento con RAGAS (D18).

---

### Sesión 11 — Sustentación final integradora · `AULA`

Gestión de aula + entrega. Se aporta rúbrica de panel, guion de demo y checklist de entregables.

---

### Sesión 12 — PLUS · Despliegue en Microsoft Foundry · `COMPLETA`

**Sesión nueva, no está en la malla del PDF** (D17). Es donde el capítulo 09 del repo se usa de verdad.

| Tema | Fuente en el repo | Estado |
|---|---|---|
| Qué es un hosted agent y el protocolo Responses | `09/README.md` §"What You'll Build" | COMPLETA |
| Envolver un `create_agent()` para hosting | `09/code/main.py` (`ResponsesHostServer`) | COMPLETA |
| Configuración del proyecto Foundry y credenciales | `09/README.md` Steps 2–4 + `.env.example` | COMPLETA |
| Despliegue con `azd` | `09/code/azure.yaml`, `09/README.md` Step 5 | COMPLETA |
| Modelo de recursos de Azure explicado recurso por recurso | — | **NULA** — se escribe como antesala del Curso 2 |
| Cuadro comparativo open source vs Foundry | — | **NULA** — es el entregable evaluado del bloque |

Artefactos reutilizables casi tal cual: `09/code/main.py`, `azure.yaml`, `requirements.txt`.

---

## B. Resumen de cobertura

| Cobertura | Sesiones | % del curso |
|---|---|---|
| COMPLETA con el repo | 2, 3, 4, 5, 12 | 42 % |
| PARCIAL (repo + contenido nuevo) | 1, 6, 8 | 25 % |
| NULA (100 % autoría) | 9, 10 | 17 % |
| AULA (gestión, sin código base) | 7, 11 | 17 % |

**Conclusión (v2):** el cambio a stack open source **redujo** lo reutilizable del repo.
El repo sigue cubriendo bien los Módulos 1 y 2, pero:
- el capítulo 09 ya **no** sirve para la S8 (cambió la plataforma a HF Spaces) — se mudó a la S12;
- los capítulos 07 y 08 sirven conceptualmente, pero **todo su código de vector store se reescribe** para Qdrant Cloud;
- las sesiones 9 y 10 siguen siendo autoría íntegra.

---

## C. Lecciones del repo que NO están en la malla y SÍ se deben agregar

| Prioridad | Contenido del repo | Por qué agregarlo | Dónde se inserta |
|---|---|---|---|
| **Alta** | `06-mcp` completo (MCP, stdio, multi-server, servidores propios) | Es el estándar de facto para conectar agentes a sistemas empresariales. Un egresado sin MCP en 2026 llega incompleto. Encaja natural con "conexión con APIs externas y fuentes de datos" de la Sesión 4 | Pre-work asíncrono de la Sesión 4 + tool MCP opcional en el proyecto |
| **Alta** | `02/code/06_token_tracking.py` + §"Cost Optimization Strategies" | Costo por token es la primera pregunta de cualquier comité de inversión. La malla no lo menciona en ninguna sesión | Sesión 2 (teoría) y Sesión 10 (métrica de optimización) |
| **Alta** | `02/code/05_error_handling.py` + `samples/robust_chat.py` (retries, backoff) | Un agente sin manejo de errores no llega a producción. Refuerza "límites de actuación" de la Sesión 6 | Sesión 6 |
| **Media** | `03/code/07-08` structured outputs con Pydantic | El PDF solo dice "output parsers". Structured output tipado es lo que hace un agente integrable a un core bancario | Sesión 2 (ya incluido, se enfatiza) |
| **Media** | `02/code/02_streaming.py` | UX de asistentes conversacionales; necesario para la app FastAPI final | Sesión 2 (teoría) y Sesión 11 (app) |
| **Media** | `05-agents/samples/basic_agent_manual_loop.py` (ReAct manual) | Ver el bucle ReAct a mano antes de usar `create_agent()` evita que el alumno lo trate como caja negra | Sesión 3, como demo de 15 min |
| **Media** | `07/code/09_embedding_relationships.py` + `samples/multilingual_search.py` | Comportamiento de embeddings **en español** — relevante porque todos los datasets del curso son en español | Sesión 5 |
| **Baja** | `05-agents/code/04_agent_with_middleware.py` | Mecanismo base sobre el que se construyen los guardrails de la Sesión 6 | Sesión 6 |

## D. Contenido que no está ni en el repo ni en la malla, y hace falta para esta audiencia

| Contenido | Justificación | Dónde |
|---|---|---|
| Nivelación de LLMs (token, ventana de contexto, temperatura, embedding, alucinación, costo) | Punto 3 del encargo: ingenieros de software con **poco conocimiento de LLMs** | `00-preparacion/` asíncrono |
| Seguridad: prompt injection, exfiltración vía tools, PII/Ley 29733 de Protección de Datos Personales (Perú) | Obligatorio para los tracks de banca y seguros | Sesión 6 |
| LangGraph (mención y cuándo usarlo vs `create_agent()`) | El alumno se topará con LangGraph al primer requerimiento de flujo con estado | Sesión 6, teoría 20 min |
| Capa de aplicación (FastAPI + cliente) | El PDF pide "aplicación final" pero el repo no tiene UI | Sesiones 8 y 11 |
