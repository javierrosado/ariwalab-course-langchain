# Contexto persistente — Repo base `microsoft/langchain-for-beginners`

> Archivo de memoria del proyecto. Se lee al inicio de cualquier sesión de trabajo
> sobre el curso para no volver a analizar el repo desde cero.
> Ubicación del repo analizado: `C:\personal\microsoft\langchain-for-beginners`
> Fecha de análisis: 2026-09-05

---

## 1. Identidad del repo

| Atributo | Valor |
|---|---|
| Origen | `github.com/microsoft/langchain-for-beginners` |
| Licencia | MIT |
| Estructura | 10 capítulos (00 setup + 01..09) |
| Idioma | Inglés |
| Enfoque pedagógico | *Agent-first*: tools → agentes → RAG agéntico |
| Formato por capítulo | `README.md` + `code/` + `samples/` + `solution/` + `assignment.md` |

## 2. Stack real verificado (`requirements.txt`)

```
langchain>=1.1.0
langchain-core>=1.1.0
langchain-openai>=1.1.0
langchain-azure-ai[hosting]>=1.2.8
langchain-mcp-adapters>=0.1.14
azure-ai-projects>=2.2.0
python-dotenv>=1.2.1
```

APIs clave usadas en el código:
- `ChatOpenAI(model, base_url, api_key)` — patrón dominante (compatible OpenAI)
- `init_chat_model("azure_ai:<model>")` — capa agnóstica (cap. 02)
- `@tool` + `args_schema` Pydantic (cap. 04)
- `create_agent(model, tools, system_prompt)` — API de agentes de LangChain 1.x (cap. 05)
- `MultiServerMCPClient` vía `langchain-mcp-adapters` (cap. 06)
- `InMemoryVectorStore` + `OpenAIEmbeddings` (cap. 07/08)
- `ResponsesHostServer` de `langchain_azure_ai.agents.hosting` (cap. 09)

Variables de entorno del repo: `AI_API_KEY`, `AI_ENDPOINT`, `AI_MODEL`,
`AI_EMBEDDING_MODEL`, y para el cap. 09: `AZURE_SUBSCRIPTION_ID`,
`FOUNDRY_PROJECT_ENDPOINT`, `AZURE_AI_PROJECT_ID`, `AZURE_LOCATION`.

## 3. Inventario por capítulo

| Cap | Tema | README | Archivos de código | Reutilización para el curso |
|---|---|---|---|---|
| 00 | Course Setup | 9.7 KB | `scripts/test_setup.py` | Alta — se reescribe para HF + Foundry |
| 01 | Introduction | 19.3 KB | 3 code + 1 sample + 2 solution | Alta — analogía "ferretería", primer call |
| 02 | Chat Models | 40.4 KB | 6 code + 3 samples + 2 solution | **Muy alta** — es el capítulo más rico |
| 03 | Prompts / Structured Outputs | 23.5 KB | 8 code + 4 samples + 2 solution | **Muy alta** — Pydantic, few-shot, composición |
| 04 | Function Calling & Tools | 27.3 KB | 4 code + 2 solution | **Muy alta** — `weather_tool.py` calza con el PDF |
| 05 | Agents | 28.9 KB | 4 code + 2 samples + 2 solution | **Muy alta** — ReAct, middleware, memoria |
| 06 | MCP | 33.0 KB | 4 code + 1 server + 1 sample + 3 solution | Media — no está en la malla, se agrega |
| 07 | Documents & Embeddings | 20.2 KB | 9 code + 6 samples + 2 solution | Alta — chunking, similitud coseno |
| 08 | Agentic RAG | 18.5 KB | 3 code + 2 samples + 2 solution | **Muy alta** — RAG tradicional vs agéntico |
| 09 | Deploy to Foundry | 17.0 KB | `main.py`, `azure.yaml`, `requirements.txt` | **Muy alta** — es el punto 7 del encargo |

Total: ~238 KB de README + 81 archivos `.py`.

## 4. Cadena de prerrequisitos declarada por el propio repo

```
00 setup
  └── 01 introduction
        └── 02 chat-models
              └── 03 prompts-messages-outputs
                    └── 04 function-calling-tools
                          ├── 05 agents
                          │     ├── 06 mcp
                          │     └── 07 documents-embeddings
                          └──────────┬──────────┘
                                     └── 08 agentic-rag
                                           └── 09 deploy-to-foundry
```

## 5. Hallazgos / defectos detectados

| # | Hallazgo | Impacto en el curso |
|---|---|---|
| H1 | `README.md` enlaza `GLOSSARY.md` pero **ese archivo no existe** en la copia local | Se construye un glosario propio en español en `recursos/glosario.md` |
| H2 | No existe ningún capítulo de **observabilidad** (ni LangSmith ni ninguna otra) | Sesiones 9 y 10 se escriben desde cero sobre Langfuse Cloud |
| H3 | No existe contenido de **evaluación de agentes** (datasets, evaluators, LLM-as-judge) | Sesión 10 se escribe desde cero |
| H4 | No existe **capa de aplicación / UI** | Se agrega FastAPI + cliente HTML en sesiones 8 y 11 |
| H5 | No hay **guardrails / validación de entradas / PII** | Se agrega en sesión 6 (lo exige el PDF) |
| H6 | Vector store es `InMemoryVectorStore` (volátil) | Se migra a **Qdrant Cloud** (open source + SaaS) como único backend |
| H7 | El cap. 04 usa `04-function-calling-tools/` **sin carpeta `samples/`** | Solo afecta a la copia de plantillas |
| H8 | Todo el código instancia el modelo con `ChatOpenAI` **inline en cada archivo** | Se centraliza en `comun/provider.py` (decisión D13) |
| H9 | El repo depende de **GitHub Models** como default | Descartado (D06); se reemplaza por **HF Inference Providers** con modelos open-weights |
| H10 | Todo el repo asume **modelos y servicios de Azure** (embeddings, Foundry) | Ninguno es open source: se reemplazan por HF Inference + Qdrant Cloud + Langfuse Cloud |
| H11 | El cap. 09 despliega **solo** a Foundry; no hay ninguna ruta de despliegue abierta | La S8 del curso (HF Spaces + Docker) se escribe desde cero; el cap. 09 se reubica en la S12 |

## 6. Qué se toma y qué NO se toma del repo

**Se toma tal cual (traducido y re-contextualizado):**
las explicaciones conceptuales, las analogías (ferretería, amigo experto, personal de restaurante,
gerente con especialistas, USB-C, biblioteca inteligente, estudiante aplicado), los mapas de
conceptos, los cuadros de decisión y la secuencia pedagógica agent-first.

**Se reescribe:** todos los ejemplos de código, porque cambian de dominio (genérico → industria peruana)
y de stack completo (GitHub Models → HF Inference · `InMemoryVectorStore` → Qdrant Cloud ·
embeddings de Azure → `multilingual-e5-large` · sin observabilidad → Langfuse Cloud).

**No se toma:** badges, secciones de contribución, enlaces a Discord de Microsoft y cursos hermanos.
