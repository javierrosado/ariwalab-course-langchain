# Conceptos previos por sesión

> Punto 4 del encargo. La audiencia son **ingenieros de software con poco conocimiento de LLMs**:
> se asume solidez en programación y arquitectura, y **cero** en la parte de modelos de lenguaje.
>
> Cada sesión abre con un bloque asíncrono obligatorio de *Conceptos previos* (decisión D07),
> entregable como `sesion-NN/conceptos-previos.md` con tres partes fijas:
> **(a)** glosario mínimo · **(b)** mini-lectura de 20–40 min · **(c)** autoevaluación de 5 preguntas
> con umbral de 80 % para entrar a la sesión síncrona.

---

## Línea base — qué se asume que YA saben (perfil de ingreso)

| Área | Nivel asumido | Si no lo tienen |
|---|---|---|
| Python | Intermedio: funciones, clases, decoradores, `venv`, `pip`, type hints | `00-preparacion/conceptos-previos/python-y-entorno.md` |
| Async | Básico: `async`/`await`, `asyncio.run` | Se refuerza en Sesión 4 (MCP y tools async) |
| HTTP / REST | Sólido: métodos, status codes, JSON, autenticación por API key | Asumido, no se refuerza |
| Git | Básico: clone, branch, commit, push | Asumido |
| Línea de comandos | Básico | Asumido |
| Cloud / Azure | **No se asume** | Solo para el bonus opcional: `modulo-4-plus-foundry/conceptos-previos.md` |
| Docker | **No se asume** | Se introduce en la S8; solo se escribe un `Dockerfile`, no se corre en local |
| LLMs | **No se asume nada** | Sesión 0 completa (obligatoria) |

---

## Sesión 0 (asíncrona, `00-preparacion/`) — Nivelación de LLMs

Prerrequisito de todo el curso. No hay contenido previo.

| Concepto | Por qué lo necesita | Profundidad |
|---|---|---|
| Modelo de lenguaje, entrenamiento, inferencia | Base de todo | Conceptual |
| **Token** y tokenización | Explica costo, límites y truncamiento | Conceptual + demo con `tiktoken` |
| **Ventana de contexto** | Explica por qué un agente "olvida" | Conceptual |
| **Temperature** y determinismo | Explica por qué el mismo prompt da respuestas distintas | Conceptual + demo |
| **Embedding** y similitud coseno | Prerrequisito duro de la Sesión 5 | Conceptual + demo numérica |
| **Alucinación** y groundedness | Justifica RAG y evaluación | Conceptual |
| Costo por 1M de tokens | Justifica optimización (Sesión 10) | Cuadro comparativo |
| Familias de modelos: propietarios vs open-weights | Justifica la decisión HF vs Foundry | Cuadro comparativo |
| API key, `.env`, gestión de secretos | Se usa desde el primer script | Práctico |

---

## Sesión 1 — Fundamentos de los agentes inteligentes

| Concepto previo | Fuente / material | Verificación |
|---|---|---|
| Todo lo de la Sesión 0 | `00-preparacion/` | Autoevaluación 80 % |
| `venv` y aislamiento de dependencias | `python-y-entorno.md` §2 (Entorno virtual) | El alumno llega con el venv creado |
| Variables de entorno y `python-dotenv` | `00-preparacion/conceptos-previos/python-y-entorno.md` §3 (Variables de entorno y el archivo `.env`) | `.env` configurado antes de clase |
| Cuenta de Hugging Face + token de acceso | Guía de alta paso a paso | Token válido |
| Cluster de **Qdrant Cloud** (free tier) | Guía de alta paso a paso | Cluster respondiendo |
| Proyecto de **Langfuse Cloud** (free tier) | Guía de alta paso a paso | Claves generadas |
| Diferencia entre *chat completion* y *agente* | Mini-lectura | Pregunta de autoevaluación |

**Antipatrón a corregir en clase:** el ingeniero de software tiende a pensar el LLM como una API
determinística. La sesión 1 debe romper esa expectativa explícitamente.

---

## Sesión 2 — Ecosistema LangChain: prompts, cadenas y modelos

| Concepto previo | Por qué |
|---|---|
| Roles de mensaje: `system`, `human`, `ai`, `tool` | Es el modelo mental de toda la librería |
| Historial de conversación como **lista de mensajes** (el modelo es *stateless*) | Sin esto no se entiende la memoria de la Sesión 5 |
| **Pydantic v2**: `BaseModel`, `Field`, validación, tipos anidados, `Enum` | Prerrequisito **duro** de structured output y de tools (Sesión 3) |
| f-strings y templates con placeholders | Base de `PromptTemplate` |
| JSON Schema (lectura básica) | Es lo que el modelo recibe realmente |
| Idempotencia y reintentos | Base del manejo de errores |

> **Riesgo:** Pydantic es el prerrequisito que más falla. Si el equipo no lo domina,
> las Sesiones 3, 4 y 6 se caen. Incluir un ejercicio obligatorio de Pydantic en el pre-work.

---

## Sesión 3 — Herramientas, integración externa y agente básico

| Concepto previo | Por qué |
|---|---|
| Docstrings de Python | **La docstring de la tool ES el prompt** que el modelo lee para decidir usarla |
| Decoradores de Python | El `@tool` de LangChain es un decorador |
| Consumo de API REST con `requests` / `httpx` | La tool llama a una API externa |
| Parsing de JSON y manejo de `KeyError` / timeouts | El PDF lo pide explícitamente |
| Manejo de excepciones y `try/except` con mensajes útiles al modelo | Un error mal devuelto rompe el bucle del agente |
| **Separación planificar / ejecutar**: el LLM *genera* la llamada, tu código la *ejecuta* | Es el concepto central de la sesión |
| Structured output (Sesión 2) | Los args de la tool son un schema Pydantic |

---

## Sesión 4 — Tools múltiples e integración de herramientas

| Concepto previo | Por qué |
|---|---|
| Todo lo de la Sesión 3 | Acumulativo |
| **Patrón ReAct**: Thought → Action → Observation | Es lo que hace `create_agent()` por dentro |
| Bucle de agente y límite de iteraciones | Para diagnosticar agentes que se cuelgan |
| `async`/`await` en Python | `MultiServerMCPClient` y varias tools son async |
| Subprocesos y stdio (para MCP) | Pre-work asíncrono de MCP |
| Diseño de interfaces / SRP | Una tool = una responsabilidad; se enseña como principio de diseño |
| Idempotencia de operaciones | Una tool puede ser invocada dos veces por el agente |

---

## Sesión 5 — Memoria contextual y arquitecturas RAG

| Concepto previo | Por qué |
|---|---|
| Embeddings y similitud coseno (Sesión 0) | Prerrequisito **duro** |
| Vectores y dimensionalidad (nociones de álgebra lineal) | Para entender qué se está midiendo |
| Diferencia búsqueda léxica (BM25/`LIKE`) vs semántica | Justifica todo el capítulo |
| **Chunking**: tamaño y solapamiento, y su trade-off | Determina la calidad del RAG |
| Índices y recuperación en base de datos | Analogía con lo que ya saben |
| Estado conversacional: `thread_id`, checkpointer | Base de la memoria del agente |
| Nociones de base vectorial gestionada: colección, punto, payload, filtro (Qdrant) | Decisión D09 |
| Modelo de embeddings multilingüe y por qué importa en español | Todos los datasets del curso son en español (D15) |
| Costo de embeber un corpus | Se re-embebe en cada cambio de chunking |

---

## Sesión 6 — Automatización, asistentes y guardrails

| Concepto previo | Por qué |
|---|---|
| Middleware / interceptores (patrón que ya conocen de web) | `create_agent()` usa el mismo concepto |
| Validación de entrada y *sanitización* | Base de los guardrails |
| **Prompt injection** y exfiltración vía tools | Amenaza específica de agentes; no la conocen |
| PII y **Ley 29733** (Protección de Datos Personales, Perú) | Obligatorio para banca y seguros |
| Principio de mínimo privilegio | Se aplica al catálogo de tools del agente |
| Máquinas de estado / flujos con estado | Antesala de LangGraph |
| Diseño de escalamiento a humano (*human-in-the-loop*) | Requisito de negocio en los 4 tracks |

---

## Sesión 7 — Hackathon y sustentación M2

| Concepto previo | Por qué |
|---|---|
| Diseño de casos de prueba y casos borde | Las pruebas de estrés que pide el PDF |
| Pruebas no determinísticas: por qué `assert ==` no sirve con un LLM | Cambia su forma de testear |
| Git: ramas y *pull request* | Trabajo en equipo sobre el proyecto |
| Comunicación técnica y demo en 10 minutos | Es evaluado |

---

## Sesión 8 — Despliegue de agentes en producción (HF Spaces)

| Concepto previo | Por qué |
|---|---|
| 12-Factor App (config por entorno) | Marco mental del despliegue |
| **Contenedores**: imagen, capa, `Dockerfile`, `EXPOSE`, `CMD` | Se escribe un `Dockerfile` real; **no se corre Docker en local** (P2), lo construye el Space |
| **FastAPI**: rutas, Pydantic como request/response, ASGI, `uvicorn` | Decisión D08 |
| Puerto, health check y por qué una plataforma lo exige | `/health` es requisito del Space |
| Gestión de secretos en la nube (*Space secrets*) vs `.env` local | Nunca subir credenciales al repo (invariante I7) |
| Git remoto y `git push` a un remote distinto de GitHub | Es el mecanismo de despliegue de HF Spaces |
| Diferencia entre *cold start* y servicio siempre activo | Explica la latencia del primer request en tiers gratuitos |

## Sesión 9 — Monitoreo y trazabilidad con Langfuse

| Concepto previo | Por qué |
|---|---|
| Observabilidad: logs vs métricas vs **trazas** | La mayoría solo conoce logs |
| **Traza distribuida**: span, trace id, jerarquía padre-hijo | Un run de agente es exactamente eso |
| OpenTelemetry (nociones) | Langfuse habla OTel; es lo que conectará con Azure Monitor en el Curso 2 |
| Latencia p50/p95 y percentiles | Métricas que se leerán en el dashboard |
| Costo por ejecución y por token (Sesión 0) | Se monitorea en Langfuse |
| Proyecto de Langfuse Cloud + `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | Alta hecha en el L1; se verifica antes de la sesión |
| Concepto de *callback handler* en LangChain | Es cómo se instrumenta el agente sin tocar su lógica |
| Qué es PII en una traza | Una traza guarda los prompts: riesgo de fuga |

---

## Sesión 10 — Optimización continua y evaluación

| Concepto previo | Por qué |
|---|---|
| Conjunto de prueba / *golden dataset* | Base de la evaluación |
| Precisión, recall, F1 (nociones) | Métricas de las tools y del retriever |
| **Groundedness** y fidelidad a la fuente | Métrica central de RAG |
| **LLM-as-judge**: qué es y sus sesgos | Técnica principal de la sesión |
| Prueba A/B y significancia | Comparar dos versiones de prompt |
| Regresión y CI | Evaluación automatizada en el pipeline |

---

## Sesión 11 — Sustentación final integradora

| Concepto previo | Por qué |
|---|---|
| Todo lo anterior | Es integradora |
| Diagramas de arquitectura (C4 o similar) | Se exige en el documento de diseño |
| Documentación de API (OpenAPI/Swagger de FastAPI) | Parte del entregable |
| Argumentación de decisiones de arquitectura | Es lo que el panel evalúa |

---

## Bonus asíncrono — PLUS · Despliegue en Microsoft Foundry

Único bloque que sale del stack open source. Es **opcional, asíncrono y no ponderado**.
Todo lo de las sesiones 1 a 11 es prerrequisito.

| Concepto previo | Por qué |
|---|---|
| **Modelo de recursos de Azure**: suscripción → grupo de recursos → recurso → proyecto | Sin este mapa mental, el portal de Azure es ruido |
| Qué es un *deployment* de modelo dentro de un proyecto Foundry | Es lo que consume `AI_ENDPOINT` |
| Autenticación: API key vs identidad (`azd auth login`) | Se usan las dos en la misma sesión, para cosas distintas |
| **Azure Developer CLI (`azd`)**: `azd auth login`, `azd up` | Es el mecanismo de despliegue del cap. 09 del repo |
| Protocolo **Responses** y qué es un *hosted agent* | Modelo de ejecución de Foundry |
| Rol **Foundry Project Manager** | Sin ese permiso el despliegue falla; se verifica antes de empezar el bonus |
| Inversión de dependencias / patrón adaptador | Es la razón por la que solo cambia `provider.py` y nada más |
| Nociones de costo cloud: consumo vs plan gratuito | Base del cuadro comparativo que se entrega |

**Nota:** esta sesión es deliberadamente superficial en Azure. La profundidad recurso por recurso
es el contenido del **Curso 2**.

---

## Mapa de dependencias de conceptos

```
        Sesión 0: token · contexto · embedding · temperatura · costo
                                  │
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              mensajes/roles  Pydantic v2   .env/secretos
                    │             │             │
                    └──────┬──────┘             │
                           ▼                    │
                    tools (@tool + docstring) ◄─┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
           ReAct / agente      chunking + similitud
                │                     │
                └──────────┬──────────┘
                           ▼
                    RAG agéntico
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        guardrails    despliegue   observabilidad
              │            │            │
              └────────────┼────────────┘
                           ▼
                    evaluación y mejora
```

**Los tres cuellos de botella reales** (donde se cae el curso si no se atienden):
`Pydantic v2` (S2) · `embeddings + chunking` (S5) · `contenedores y despliegue` (S8).

Los fundamentos de Azure ya **no** son cuello de botella del curso: se concentran en la S12,
que es un plus y no bloquea ninguna evaluación ponderada.
