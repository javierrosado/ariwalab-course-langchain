# Plan curricular — Curso "IA Agent Building" en español

**Basado en:** malla `IA Agent Building` (Continental Florida University) + repo `microsoft/langchain-for-beginners`
**Audiencia:** ingenieros de software con poco conocimiento de LLMs
**Principio rector:** stack abierto con inferencia y servicios gestionados en línea;
los clientes, scripts y demos Python pueden ejecutarse en la máquina del alumno.
**Foundry:** **módulo bonus asíncrono** al final, como puerta de entrada al Curso 2 (que sí será 100 % Foundry).
**Duración:** 12 sesiones de 6 h · **72 horas lectivas** · 50 % síncrono / 50 % asíncrono
**Calendario:** 2 sesiones por semana de 3 h síncronas → **6 semanas** (ver `docente/cronograma.md`)
**Balance:** 40 % teoría / 60 % práctica
**Autor:** Javier Rosado · Ariwa Labs

---

## 1. Los dos principios que gobiernan el stack

```
┌──────────────────────────────────────────────────────────────────────┐
│  PRINCIPIO 1 · OPEN SOURCE                                           │
│  Modelo, framework, embeddings, vector store, observabilidad y       │
│  evaluación son productos de código abierto.                         │
│                                                                       │
│  PRINCIPIO 2 · TODO EN LÍNEA (SaaS)                                  │
│  La inferencia y los servicios usan las nubes       │
│  gestionadas de esos mismos productos, en sus planes gratuitos.       │
│                                                                       │
│  EXCEPCIÓN · Módulo bonus = Microsoft Foundry, el "plus" del curso.   │
└──────────────────────────────────────────────────────────────────────┘
```

**Por qué importa la combinación:** open source *self-hosted* obligaría a Docker y RAM en la laptop
de cada alumno; SaaS propietario rompería el principio de apertura. La intersección —producto abierto,
nube gestionada, plan gratuito— es la única que cumple ambas condiciones.

---

## 2. Stack tecnológico

| Capa | Tecnología | Licencia | Modalidad | Plan gratuito |
|---|---|---|---|---|
| Orquestación | LangChain 1.x / LangGraph | MIT ✅ | librería | — |
| Modelo de chat | **HF** · `Qwen3-32B` — **el mismo para las 4 industrias** | Apache 2.0 ✅ | SaaS | verificar disponibilidad y cuota antes de clase |
| Personalización | **System prompt por industria** (`comun/prompts_industria.py`) + colección Qdrant | — | código | sin costo |
| Embeddings | **HF Inference API** · `intfloat/multilingual-e5-large` | MIT ✅ | SaaS | créditos mensuales · ⚠️ verificar |
| Vector store | **Qdrant Cloud** | Apache 2.0 ✅ | SaaS | **1 GB RAM / 4 GB disco · gratis para siempre, sin tarjeta** ✔ verificado |
| Tools externas | `@tool` + `langchain-mcp-adapters` (MCP) | MIT ✅ | librería | — |
| Observabilidad | **Langfuse Cloud** | MIT ✅ | SaaS | **50k unidades/mes · sin tarjeta · 30 días retención · 2 usuarios** ✔ verificado |
| Evaluación | Langfuse datasets + evaluators · RAGAS | MIT / Apache ✅ | SaaS | incluido en las 50k unidades |
| API | FastAPI | MIT ✅ | librería | — |
| Despliegue (S8) | **Hugging Face Spaces** (Docker) | plataforma ✅ | SaaS | tier CPU gratuito, sin tarjeta |
| Repositorio | GitHub | — | SaaS | gratuito |
| **Plus (bonus)** | **Microsoft Foundry** hosted agent + `azd` | propietario | SaaS | requiere suscripción Azure |

### `.env` unificado del curso

```dotenv
# ---------- Modelo (open source, vía Hugging Face) ----------
AI_PROVIDER=huggingface              # huggingface | foundry  (foundry solo en bonus)
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx
HF_EMBEDDING_MODEL=intfloat/multilingual-e5-large

# Un solo modelo para las 4 industrias.
# La personalización vive en el system prompt y en la colección de Qdrant.
HF_CHAT_MODEL=Qwen/Qwen3-32B
HF_ENABLE_THINKING=false

# ---------- Vector store (Qdrant Cloud) ----------
QDRANT_URL=https://xxxxxxxx.us-east.aws.cloud.qdrant.io:6333
QDRANT_API_KEY=xxxxxxxxxxxxxxxx
QDRANT_COLLECTION=kb-<track>

# ---------- Observabilidad y evaluación (Langfuse Cloud) ----------
LANGFUSE_PUBLIC_KEY=pk-lf-xxxxxxxx
LANGFUSE_SECRET_KEY=sk-lf-xxxxxxxx
LANGFUSE_HOST=https://cloud.langfuse.com

# ---------- Track de industria ----------
COURSE_TRACK=telecomunicaciones      # telecomunicaciones | banca | retail | seguros

# ---------- SOLO módulo bonus · plus Foundry ----------
# AI_PROVIDER=foundry
# AI_ENDPOINT=https://<recurso>.services.ai.azure.com/models
# AI_API_KEY=<clave>
# AI_MODEL=gpt-5-mini
# AZURE_SUBSCRIPTION_ID=<subscription-id>
# FOUNDRY_PROJECT_ENDPOINT=https://<recurso>.services.ai.azure.com/api/projects/<proyecto>
# AZURE_AI_PROJECT_ID=/subscriptions/.../projects/<proyecto>
# AZURE_LOCATION=<region>
```

`comun/provider.py` conmuta por `AI_PROVIDER`: durante las 11 sesiones siempre vale `huggingface`;
en el bonus se estudia el cambio de cliente de chat a `foundry`. El hosting necesita un
grafo compatible y el cambio de embeddings requiere comprobar compatibilidad y reindexar si cambia el modelo.

---

## 3. Modelo semanal

Cada una de las 12 sesiones tiene la misma forma de 6 horas, y se dictan **2 por semana**:

```
┌─────────────────────────────────────────────────────────────────┐
│  ASÍNCRONO (1 h)   │   SÍNCRONO (3 h)        │ ASÍNCRONO (2 h)  │
│  Conceptos previos │   Sesión en vivo        │ Laboratorio      │
│  · glosario        │   · teoría + demo       │ · incremental    │
│  · mini-lectura    │   · lab guiado          │ · sobre el       │
│  · autoeval. 80 %  │   · avance de proyecto  │   track elegido  │
└─────────────────────────────────────────────────────────────────┘
        TEORÍA              MIXTO                    PRÁCTICA
```

El bloque de **Conceptos previos** (punto 4 del encargo) es **bloqueante**: sin 80 % en la
autoevaluación el alumno no entra a la sesión síncrona.
Detalle en [`docente/prerrequisitos-por-sesion.md`](docente/prerrequisitos-por-sesion.md).

---

## 4. Malla con balance teoría/práctica

| # | Sesión | Módulo | Teoría | Práctica | Total | Lab |
|---|---|---|---|---|---|---|
| 0 | *Nivelación de LLMs* (asíncrona, no computa) | — | — | — | — | — |
| 1 | Fundamentos de los agentes inteligentes | M1 | 3.5 | 2.5 | 6 | L1 |
| 2 | Ecosistema LangChain: prompts, cadenas y modelos | M1 | 3.0 | 3.0 | 6 | L2 |
| 3 | Herramientas, integración externa y sustentación A1 | M1 | 2.5 | 3.5 | 6 | L3 |
| | **Subtotal Módulo 1** | | **9.0** | **9.0** | **18** | |
| 4 | Tools e integración de herramientas | M2 | 2.5 | 3.5 | 6 | L4 |
| 5 | Memoria contextual y RAG con Qdrant Cloud | M2 | 3.0 | 3.0 | 6 | L5 |
| 6 | Automatización, asistentes y guardrails | M2 | 2.5 | 3.5 | 6 | L6 |
| 7 | Hackathon y sustentación del proyecto | M2 | 1.5 | 4.5 | 6 | L7 |
| | **Subtotal Módulo 2** | | **9.5** | **14.5** | **24** | |
| 8 | Despliegue en producción con HF Spaces | M3 | 2.5 | 3.5 | 6 | L8 |
| 9 | Monitoreo y trazabilidad con Langfuse | M3 | 2.5 | 3.5 | 6 | L9 |
| 10 | Optimización continua y evaluación | M3 | 2.5 | 3.5 | 6 | L10 |
| 11 | Sustentación final integradora | M3 | 1.5 | 4.5 | 6 | L11 |
| | **Subtotal Módulo 3** | | **9.0** | **15.0** | **24** | |
| S | Seminario Internacional | — | 1.5 | 4.5 | 6 | — |
| | **TOTAL LECTIVO** | | **29.0** | **43.0** | **72** | |
| B | **BONUS asíncrono · Foundry** *(no computa horas lectivas)* | M4 | ~2 | ~4 | ~6 | L12 |

> **Calendario:** 2 sesiones por semana de 3 h síncronas → el curso se completa en
> **6 semanas**, con 12 h semanales de dedicación por alumno. La malla, las horas y el balance no
> cambian: solo el reparto en el calendario. Detalle y riesgos del ritmo en `docente/cronograma.md`.

**Balance:** 29 / 72 = **40.3 % teoría** · 43 / 72 = **59.7 % práctica** ✅
**Síncrono/asíncrono:** 36 h / 36 h = **50 / 50** ✅
**Malla oficial:** 11 semanas + Seminario = 72 h ✅ **sin cambios, no requiere aprobación académica**

> El bloque de Foundry es **bonus asíncrono**: guía autoguiada fuera de las horas
> lectivas, disponible desde el cierre de la S11. No condiciona ninguna evaluación ponderada.

---

## 4bis. Diseñar para que la fiabilidad se componga

Las 4 industrias comparten `Qwen3-32B`. La razón de estas seis reglas no es el tamaño del
modelo: es que **la fiabilidad se compone a lo largo del bucle ReAct**.

| Precisión por llamada | 3 pasos | 5 pasos |
|---|---|---|
| 88 % | 68 % | 53 % |
| 93 % | 80 % | 70 % |
| 97 % | 91 % | 86 % |

La tabla usa pⁿ bajo supuestos de independencia y probabilidad constante por paso; no es
una medición del agente. Los fallos pueden estar correlacionados. Por eso
se reduce el número de pasos y se hace cada paso lo más inequívoco posible:

| # | Regla | Dónde aplica |
|---|---|---|
| A1 | **4 tools núcleo de negocio**; desde L5 se añade un retriever. Medir otro catálogo si se incorporan opcionales | L4 en adelante |
| A2 | Docstrings con verbo + cuándo usarla + **cuándo NO** | Todas las tools |
| A3 | `with_structured_output()` con validación y un reintento | L2 en adelante |
| A4 | Tope duro de iteraciones + errores de tool redactados para el modelo | L3 en adelante |
| A5 | Few-shot en los prompts críticos | L2, L4, L6 |
| A6 | Obligar a recuperar ante afirmaciones sobre tarifas, coberturas o políticas | L5 |

> **A2 no es una concesión al modelo pequeño, es una mejora del curso.** Un 72B perdona
> descripciones ambiguas y el alumno nunca descubre por qué importan. Un 7B no perdona: obliga
> a diseñar bien las herramientas, que es exactamente lo que un curso de agentes debe enseñar.

Especificación completa de los modelos: [Personalización por industria](docente/modelos-por-industria.md)

---

## 4ter. Cómo se personaliza cada industria

Los cuatro tracks usan **el mismo modelo**. Lo que hace que un agente suene a telco, banco,
retailer o aseguradora son dos piezas, ambas editables como texto:

| Pieza | Dónde vive | Qué aporta |
|---|---|---|
| **System prompt** | `comun/prompts_industria.py` | Identidad, jerga del sector, límites de actuación y escalamiento |
| **Base de conocimiento** | Colección de Qdrant por track | Tarifarios, condicionados y políticas, citables y auditables |

```python
from comun.prompts_industria import get_system_prompt

agente = create_agent(get_chat_model(), tools=TOOLS_NUCLEO,
                      system_prompt=get_system_prompt())   # resuelve por COURSE_TRACK
```

**Ninguna cifra de negocio está en el prompt.** Todas viven en los documentos, para poder
citarlas, auditarlas y actualizarlas sin tocar el agente.

> El curso personaliza el comportamiento con prompts y recupera el conocimiento mediante RAG;
> no incluye entrenamiento de pesos.

---

## 5. Contenido por sesión

### Módulo 1 · Introducción a los agentes inteligentes (S1–S3; semanas 1–2)

**S1 — Fundamentos de los agentes inteligentes**
Teoría: qué es un agente (percepción → razonamiento → acción → entorno); workflow vs agente;
por qué un LLM solo no es un agente; anatomía de LangChain; panorama de modelos abiertos vs cerrados.
Práctica: alta de cuentas HF, Qdrant Cloud y Langfuse; `.env`; `provider.py`; primer script contra
un modelo open-weights en línea.
Formativo: **Test 1** + primer script funcional.

**S2 — Ecosistema LangChain: prompts, cadenas y modelos**
Teoría: mensajes y roles; el modelo es *stateless*; Rol + Contexto + Tarea + Formato; few-shot;
composición de plantillas; structured output con Pydantic; tokens y costo.
Práctica: plantillas del dominio + clasificador de intención tipado.
Formativo: **Test 2** + cadena con parser.
*Adiciones del repo:* streaming, manejo de errores con reintentos, conteo de tokens.

**S3 — Herramientas, integración externa y sustentación A1**
Teoría: function calling; el LLM **genera** la llamada, tu código la **ejecuta**; la docstring como
prompt; diseño de tools; bucle ReAct manual (demo 15 min).
Práctica: tool contra API externa del track, parsing JSON, manejo de errores; agente básico.
**Assignment A1 — Agente básico con API externa (100 % del Módulo 1).**

### Módulo 2 · Desarrollo y aplicaciones de agentes (S4–S7; semanas 2–4)

**S4 — Tools e integración de herramientas**
Teoría: catálogo de tools y selección dinámica; responsabilidad única aplicada a tools; idempotencia;
límite de iteraciones; **por qué la fiabilidad compuesta obliga a escribir mejores descripciones** (A2).
Práctica: **4 tools** del dominio + agente que elige correctamente (A1).
*Pre-work asíncrono:* **MCP** (adición del repo, cap. 06).
Avance 1 del proyecto.

**S5 — Memoria contextual y arquitecturas RAG**
Teoría: estado conversacional y `thread_id`; embeddings y similitud coseno; chunking y su trade-off;
RAG tradicional vs **RAG agéntico**; qué es una base vectorial gestionada; colecciones y payload en Qdrant.
Práctica: indexar el corpus del track en **Qdrant Cloud**, tool de recuperación, agente que decide
cuándo buscar y cita fuentes.
**Salvaguarda A6:** el system prompt obliga a recuperar ante cualquier afirmación sobre tarifas,
coberturas o políticas. No es solo una defensa técnica: es un requisito de auditoría — una
respuesta sin fuente no es verificable.
Avance 2 del proyecto.

**S6 — Automatización de procesos y asistentes**
Teoría: agentes para procesos reales; middleware; **guardrails**; prompt injection; PII y Ley 29733;
límites de actuación; escalamiento a humano; cuándo pasar a LangGraph.
Práctica: `guardrails.py` + batería de 15 ataques.
Avance 3 del proyecto.

**S7 — Hackathon y sustentación del proyecto**
Teoría: cómo se prueba lo no determinístico.
Práctica: clínica de proyectos, pruebas de estrés, demo en vivo, retroalimentación de pares.
**Proyecto M2 — Agente avanzado con tools, memoria y RAG. Demo + documento de diseño.**

### Módulo 3 · Implementación y monitoreo en ambientes reales (S8–S11; semanas 4–6)

**S8 — Despliegue de agentes en producción (HF Spaces)**
Teoría: 12-Factor; gestión de secretos en la nube; contenedores e imagen Docker; qué significa
"producción" para un agente; opciones de despliegue del ecosistema abierto.
Práctica: `Dockerfile`, app **FastAPI** con `/chat` y `/health`, despliegue a **Hugging Face Spaces**
por git push, secretos como *Space secrets*, URL pública funcionando.
Avance 1 M3: arquitectura de despliegue.

**S9 — Monitoreo y trazabilidad con Langfuse**
Teoría: logs vs métricas vs trazas; span, trace y jerarquía; latencia p50/p95; costo por ejecución;
PII dentro de una traza.
Práctica: instrumentar el agente con el callback de Langfuse, leer trazas del agente ya desplegado,
hallar 2 cuellos de botella reales.
Avance 2 M3.
*Nota de trazabilidad con la malla:* el PDF nombra LangSmith; se cumple el objetivo pedagógico
—observabilidad y trazabilidad de agentes— con la herramienta open source equivalente.

**S10 — Optimización continua y evaluación**
Teoría: golden dataset; evaluators; groundedness; LLM-as-judge y sus sesgos; A/B de prompts.
Práctica: 30 casos en Langfuse Datasets, evaluators automáticos, medición v1 vs v2, optimización
basada en trazas reales.
Avance 3 M3.

**S11 — Sustentación final integradora**
Práctica: entrega de la solución desplegada y monitoreada; demo ante panel; Q&A técnico.
**Proyecto Integrador Final — Agente open source desplegado y monitoreado.**

### Módulo 4 · PLUS · bonus asíncrono (fuera de las 72 h)

**Bonus — Despliegue en Microsoft Foundry**

Guía autoguiada que se libera al cerrar la S11. No hay sesión síncrona: el alumno la recorre a su ritmo.
Se ofrece una asesoría opcional de 1 h para quien tenga suscripción de Azure.
Teoría: qué es un *hosted agent*; protocolo Responses; el modelo de recursos de Azure
(suscripción → grupo de recursos → proyecto Foundry → despliegue de modelo); cuándo conviene
una nube gestionada frente al stack abierto; comparación de costo, soberanía del dato y operación.
Práctica: cambiar `AI_PROVIDER=foundry` **sin tocar el código del agente**, envolver con
`ResponsesHostServer`, `azure.yaml`, `azd auth login`, `azd up`, verificación en el playground.
**Cierre:** cuadro comparativo open source vs Foundry hecho por los propios alumnos + proyección
al Curso 2 ("100 % Foundry, recurso por recurso").

---

## 6. Sistema de evaluación

| Instrumento | Momento | Peso | Evidencia |
|---|---|---|---|
| Autoevaluación de conceptos previos | Cada sesión | Habilitante (80 %) | Habilita, no califica |
| Test 1 / Test 2 formativos | S1 / S2 | Formativo | Cuestionario |
| **Assignment A1** | S3 | **100 % Módulo 1** | Agente básico con API externa + 3 escenarios |
| Ejercicios guiados | S4, S5, S6 | Formativo | Labs L4–L6 |
| **Proyecto M2** | S7 | **100 % Módulo 2** | Agente con tools + memoria + RAG · demo + diseño |
| Ejercicios guiados | S8, S9, S10 | Formativo | Labs L8–L10 |
| **Proyecto Integrador Final** | S11 | **100 % Módulo 3** | Agente desplegado y monitoreado · panel |
| Reto plus Foundry | Bonus | Certificación adicional / no ponderado | Agente corriendo en Foundry + cuadro comparativo |

Rúbrica de 4 niveles (Insuficiente / En desarrollo / Competente / Destacado) sobre 5 criterios:
funcionalidad · diseño de tools y prompts · guardrails y manejo de errores · evidencia de
observabilidad y evaluación · comunicación técnica. Plantillas en `recursos/rubricas/`.

---

## 7. Estructura de carpetas

```
ariwalab-course-langchain/
├── README.md · PLAN-CURRICULAR.md
├── docs/                mapa pedagógico, glosario y guía editorial
├── comun/               provider.py · vectorstore.py · observability.py · utils
├── 00-preparacion/      Sesión 0: nivelación de LLMs + alta de las 3 cuentas SaaS
├── modulo-1-fundamentos/           sesiones 01–03
├── modulo-2-agentes-avanzados/     sesiones 04–07
├── modulo-3-produccion/            sesiones 08–11
├── modulo-4-plus-foundry/          bonus asíncrono de Foundry
├── proyecto-final/      telecomunicaciones · banca · retail · seguros
├── recursos/            glosario.md · datasets/ · rubricas/ · plantillas/
└── docente/             prerrequisitos · labs-incrementales · casos-de-uso · cronograma
```

Cada `sesion-NN/` contiene `README.md` (teoría), `conceptos-previos.md`, `code/`, `lab/` y `solucion/`.

---

## 8. Bonus y preparación del dictado

Foundry es un bloque asíncrono opcional, fuera de las 72 horas y de la nota.
El docente verifica servicios, cuotas y acceso antes de cada edición con la
[guía de verificación](VERIFICACION.md) y el [checklist previo](docente/checklist-pre-sesion.md).
El [mapa pedagógico](docs/COURSE-MAP.md) relaciona conceptos, prácticas y evaluaciones.
