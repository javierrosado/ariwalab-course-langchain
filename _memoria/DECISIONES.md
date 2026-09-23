# Registro de decisiones de diseño (ADR del curso)

> Decisiones tomadas y confirmadas por Javier Rosado. Cualquier cambio se registra aquí con fecha.
> **v2.0 — 2026-09-05:** el objetivo del curso pasó a ser **100 % open source + 100 % SaaS**,
> con Foundry como bloque *plus* al final. Esto invalidó D05, D06(parcial), D09, D10 y D13 de la v1.

---

## Principios rectores (v2)

| P | Principio | Implicación |
|---|---|---|
| **P1** | **Todo open source** | Modelo, framework, embeddings, vector store, observabilidad y evaluación son productos de código abierto |
| **P2** | **Todo en línea (SaaS), nada en local** | Se usan las nubes gestionadas de esos productos; la laptop del alumno solo corre Python y el editor |
| **P3** | **Costo mínimo** | Solo planes gratuitos; se prefiere el free tier permanente sobre el de créditos |
| **P4** | **Foundry es el *plus* final** | Va después de terminar todo con open source; es la puerta de entrada al Curso 2 (100 % Foundry) |

---

## Decisiones vigentes

| ID | Decisión | Elegido | Alternativas descartadas | Consecuencia |
|---|---|---|---|---|
| D01 | Organización de industrias | **4 tracks paralelos**: cada equipo elige UNA industria en el Lab 1 y la lleva hasta la app final | Rotación por lab; caso troncal + 3 variantes | Material de laboratorio ×4 con esqueleto idéntico |
| D02 | Alcance de la 1ra iteración | **Plan curricular primero**, luego construcción | Todo de una vez; plan + M1 | Este entregable es diseño |
| D03 | Formato de laboratorios | **Scripts `.py`** (`code/` + `lab/` + `solucion/`) | Notebooks; ambos | Versionable en git |
| D04 | Persistencia de memoria | En **`ariwalab-course-langchain/_memoria/`** | Dentro del repo de Microsoft; ambas | El repo base queda intacto para `git pull` |
| D05 | **Observabilidad** *(v2)* | **Langfuse Cloud** — open source (MIT) + SaaS | LangSmith (SaaS **propietario**); Langfuse self-hosted (viola P2); Phoenix; OTel+Jaeger | Cumple P1 y P2. Se desvía del texto del PDF, que nombra LangSmith: se documenta la equivalencia pedagógica |
| D06 | Proveedor y modelo | **Hugging Face** · **`Qwen3-32B`** (denso, Apache 2.0, tool calling nativo, 100+ idiomas, 32K contexto) | GitHub Models; Foundry como troncal; modelos locales; `Qwen2.5-7B-Instruct` y los otros 3 candidatos probados | Ver D28: elegido por medición contra el endpoint real |
| D07 | Estructura temporal | 11 sesiones del PDF + bloque de *Conceptos previos* asíncrono en cada una | Sin agregados | La nivelación va en el 50 % asíncrono ya declarado |
| D08 | Aplicación final | **FastAPI + cliente HTML simple** | Streamlit; Chainlit; solo agente hosted | Alineado a Docker y al protocolo Responses de la S12 |
| D09 | **Vector store** *(v2)* | **Qdrant Cloud** — Apache 2.0 + nube gestionada | Azure AI Search (**eliminado**, no es open source); Chroma embebido (viola P2); Chroma Cloud (free tier por créditos); Supabase/pgvector (pausa por inactividad); Weaviate Cloud (sandbox caduca a 14 días) | Free tier **permanente verificado**: 1 GB RAM / 4 GB disco, sin tarjeta |
| D10 | **Fallback de vector store** *(v2)* | **Ninguno.** Qdrant Cloud es el único backend | Chroma; FAISS; `InMemoryVectorStore` | `comun/vectorstore.py` implementa un solo backend; la cuenta de Qdrant es hito bloqueante de la semana 4. **Nota (S5, 2026-09-16):** las colecciones de respaldo `kb-<track>-respaldo` no son una excepción a esta decisión — viven en el **mismo** cluster de Qdrant Cloud, indexadas con el mismo `ingest.py`, en solo lectura para el alumno. No hay fallback de *tecnología*: sigue siendo Qdrant y solo Qdrant; lo que hay es una colección alternativa dentro del mismo servicio, para cuando la ingesta de un equipo falla a mitad de sesión |
| D11 | Idioma del código | Identificadores en inglés, comentarios y docstrings en español | Todo en español; todo en inglés | El código se lee igual que la documentación de LangChain |
| D12 | Datos | **100 % sintéticos**, marcas ficticias (AndesMóvil, Banco Inti, MercaSur, Andina Seguros) | Datos reales; marcas reales peruanas | Cero riesgo legal; el repo del curso es publicable |
| D13 | **Arquitectura de proveedor** *(v2)* | **`comun/provider.py`** con `get_chat_model()` / `get_embeddings()` conmutado por `AI_PROVIDER` | Instanciar el modelo en cada archivo | `huggingface` en S1–S11; `foundry` en S12 **sin tocar el código del agente**. El switch ES la lección del bloque plus |
| D14 | Evaluación académica | Test formativo + Assignment por módulo, rúbrica de 4 niveles | Rúbrica institucional propia | Sujeto a plantilla de la universidad |
| **D15** | **Embeddings** | **HF Inference API** · `intfloat/multilingual-e5-large` | Embeddings de Foundry (**eliminado**); `sentence-transformers` local (viola P2); MiniLM; BGE-M3 | Buen rendimiento en español, que es el idioma de todos los datasets |
| **D16** | **Despliegue de la S8** | **Hugging Face Spaces** (Docker + FastAPI) | Render (duerme el servicio); Fly.io / Railway (piden tarjeta); solo Docker local (viola P2) | Free tier CPU sin tarjeta; mismo ecosistema que el modelo |
| **D17** | **Ubicación de Foundry** *(revisada)* | **Módulo bonus asíncrono**, liberado al cerrar la S11 | Sesión 12 formal (**derogada**: llevaba el curso a 78 h); Seminario Internacional; bloque final de la S11 | La malla del PDF queda intacta en **72 h**, sin trámite académico. El bloque plus no tiene clase en vivo: se compensa con guía detallada |
| **D18** | **Evaluación (S10)** | **Langfuse Datasets + evaluators**, complementado con RAGAS | LangSmith evaluators (propietario) | Una sola herramienta cubre S9 y S10 |
| **D20** | **Diseñar para que la fiabilidad se componga** | **3-4 tools** por agente, docstrings con "cuándo NO", `with_structured_output` con validación y reintento, tope de iteraciones, few-shot en prompts críticos | Asumir que el modelo acierta siempre | Con 93 % de precisión por llamada, una tarea de 3 pasos sale bien el 80 % de las veces y una de 5 el 70 %. Se reduce el número de pasos y se hace cada paso inequívoco |
| **D21** | **Personalización por industria** *(resuelta 2026-09-10)* | **CAMINO A: sin fine-tuning.** Un solo modelo base para las 4 industrias (`Qwen3-32B`, ver D28). La personalización vive en el **system prompt** (`comun/prompts_industria.py`) y en la **colección de Qdrant** | Camino B (LoRA de estilo, **descartado** para la 1ra edición); fine-tuning de conocimiento; bases distintos por industria | Un modelo que verificar en vez de 4. Disuelve 7 riesgos, salva la justificación del RAG (S5) y la portabilidad del bonus |
| **D26** | **Mecanismo de personalización** | **System prompt de 5 bloques** por industria: identidad · jerga del sector · estilo general · recuperación obligatoria (A6) · límites y escalamiento | Prompt monolítico; personalización solo por RAG | Cambiar el tono de un agente cuesta un commit, no un reentrenamiento. El bloque 5 es la primera capa de los guardrails del L6 |
| **D27** | **Calendario de dictado** *(revisada 2026-09-10)* | **2 sesiones por semana de 3 h → 6 semanas**, 12 h semanales por alumno | 3 sesiones/semana (4 semanas, 18 h — **descartada** por dedicación excesiva); 1 sesión/semana (12 semanas) | Punto de equilibrio: sostiene la continuidad sin exigir dedicación completa, y deja 3-4 días de margen entre sesiones para recuperar |
| **D28** | **Modelo del curso** *(verificado 2026-09-10)* | **`Qwen/Qwen3-32B`** · `HF_ENABLE_THINKING=false` | `Qwen3-30B-A3B`, `Qwen3-8B` y `Llama-3.3-70B-Instruct`: **los tres fallaron** las comprobaciones críticas contra el endpoint real. `Qwen2.5-7B-Instruct`: descartado por los benchmarks de 2026 | **Elegido por medición, no por catálogo.** De 4 candidatos probados con `check_stack --candidatos`, fue el único que pasó tool calling y bucle ReAct. **Modo non-thinking explícito** para que las trazas de razonamiento no interfieran con el parseo de `tool_call` |
| **D22** | **Simulador de industria** | **Un solo servicio** que simula las 4 empresas ficticias y expone el mismo dominio por REST, SQL y MCP. Los alumnos construyen el agente, no el simulador | 4 simuladores independientes; 3 servicios separados por superficie | Un despliegue y un mantenimiento. La redundancia de superficies es deliberada: enseña que la fuente cambia y la tool no |
| **D23** | **Dónde vive el simulador** | **HF Spaces, desplegado por el docente.** Cada equipo consume una URL real con su propia API key | Un Space por equipo; `localhost` (viola P2) | Respeta "nada en local", enseña autenticación real y errores de red. Exige aislar las escrituras por equipo |
| **D24** | **Base de datos del simulador** | **SQLite interno**, reconstruido desde los CSV en cada arranque | Supabase o Neon (una cuenta más, pausa por inactividad); sin capa de BD | Cero infraestructura y cero cuentas nuevas. El simulador vuelve a un estado conocido al reiniciarse |
| **D25** | **Transporte de MCP** | **Los dos: stdio y HTTP**, como comparación didáctica en el L4 | Solo stdio; solo HTTP | El agente no nota la diferencia: mismas herramientas, distinto transporte. Es lo que más enseña sobre MCP |
| **D19** | **Tamaño de equipo** | **2 personas por equipo** | Equipos de 3-4 con 1 proyecto Langfuse por alumno; cuenta compartida; cuenta paga del aula | Impuesto por el límite de 2 usuarios del plan Hobby de Langfuse. Con 4 tracks se necesitan ≥ 8 alumnos; más equipos = más proyectos que revisar |
| **D29** | **Rúbricas del cierre del M3** *(2026-09-17)* | **Una sola rúbrica, `recursos/rubricas/rubrica-final.md`**, para el Proyecto Integrador de la S11 | `rubrica-m3.md` y `rubrica-demo.md` por separado, como preveía el `ROADMAP.md` original (Fase 8) | En este curso el "proyecto de cierre del Módulo 3" y la "sustentación ante panel" **son el mismo evento** (S11 §2 y §8 del esqueleto): no hay una demo separada de un proyecto separado, como sí los hay en el Módulo 2 (A1 en la S3, sustentación en la S4). `rubrica-final.md` ya incluye "Comunicación técnica" (15 %) como uno de sus 5 criterios, cubriendo lo que habría sido `rubrica-demo.md`. Duplicar el archivo habría creado dos rúbricas que calificar sobre el mismo evento, con riesgo real de que diverjan con el tiempo |

---

## Decisiones derogadas

| ID | Versión 1 | Motivo de la derogación |
|---|---|---|
| D05 v1 | LangSmith troncal + observabilidad de Foundry | LangSmith es SaaS propietario → viola P1; Foundry se pospone a la S12 → viola P4 |
| D09 v1 | Embeddings de Foundry + Azure AI Search | Ninguno de los dos es open source → viola P1 |
| D10 v1 | Fallback a Chroma local | Chroma embebido corre en local → viola P2 |
| D13 v1 | HF y Foundry intercambiables durante todo el curso | Foundry se concentra en la S12 → P4 |

---

## Riesgos abiertos

| # | Riesgo | Severidad | Mitigación |
|---|---|---|---|
| ~~R1~~ | ~~Tool calling sin verificar~~ | ✅ **RESUELTO 2026-09-10** | Verificado con `check_stack --candidatos`: `Qwen3-32B` pasa las comprobaciones críticas. Repetir la verificación 2 semanas antes de cada dictado, por si cambia la disponibilidad del proveedor |
| **R17** | **Modo thinking de Qwen3 activo por default del proveedor** (nuevo) | Media | `HF_ENABLE_THINKING=false` se fija explícitamente en `provider.py` vía `chat_template_kwargs`. Verificar en la comprobación 3 que el `tool_call` se parsea limpio |
| **R18** | **Costo del modelo: 32B denso en vez de un MoE** (nuevo) | Media | El candidato barato (`Qwen3-30B-A3B`, 3.3B activos) falló la verificación. Un 32B denso consume más cuota por llamada, lo que agrava R2. Verificar los límites del free tier antes del dictado |
| **R2** | **Cuotas del free tier de HF Inference** con 30 alumnos golpeando el endpoint en clase en vivo | Alta | ⚠️ **Pendiente de verificar** los límites vigentes del plan gratuito de HF. Si son insuficientes: cuenta PRO del docente para las demos y trabajo asíncrono escalonado para los alumnos |
| **R3** | Langfuse Cloud limita el plan Hobby a 2 usuarios | **Resuelto** | **Equipos de 2 personas** (D19). Encaja exacto con el límite y ambos integrantes ven las trazas del agente |
| **R4** | **Qdrant Cloud free tier: 1 GB RAM / 4 GB disco, un solo nodo** | Baja | Suficiente para los corpus sintéticos del curso (< 50 MB por track). Limitar el tamaño de los datasets por diseño |
| **R5** | **HF Spaces free tier** puede tener límites de inactividad o de recursos | Media | ⚠️ Verificar antes del dictado. Alternativa preparada: Render |
| **R6** | La malla del PDF nombra **LangSmith** y el curso usará **Langfuse** | Media | Documentar la equivalencia pedagógica en el sílabo; demo de LangSmith de 20 min si la universidad lo exige literalmente |
| **R7** | Horas por encima de las 72 h declaradas | **Resuelto** | Foundry pasó a bonus asíncrono (D17 v2): el curso vuelve a **72 h exactas** |
| **R8** | `langchain-azure-ai[hosting]` está en preview (solo afecta a la S12) | Baja | Fijar versiones exactas y probar antes de cada dictado |
| **R10** | **Structured output no siempre válido** | 🟢 **Mitigada** *(era alta)* | `with_structured_output()` falla en la minoría de los casos, y la fiabilidad se compone. Mitigada en código: **`comun/structured.py`** valida contra el esquema, reintenta una vez devolviéndole al modelo el error concreto y lanza `ExtraccionFallida` en vez de propagar un `None`. Verificada por `docente/verificar_structured.py` (36 comprobaciones, sin credenciales) |
| **R11** | **Bucle ReAct: la fiabilidad se compone** | 🟡 **Medida** *(era alta)* | Máximo 4 tools, tope de iteraciones y errores de tool redactados para el modelo (D20). Deja de ser una apuesta: **`docente/matriz_seleccion.py`** mide el acierto de selección con 20 consultas por track y una matriz de confusión que señala qué docstring corregir. Umbral 85 %; por debajo, el laboratorio 4 no se dicta. **Falta ejecutarlo contra el endpoint real** (lo hace Javier: 80 llamadas) |
| **R12** | El agente responde de memoria en vez de llamar al RAG | **Baja** *(era crítica)* | Muy reducido por D21: un modelo base no conoce el tarifario de AndesMóvil. Se conservan la salvaguarda A6 y el criterio C6 por auditoría: una respuesta sin fuente no es verificable |
| ~~R13~~ | ~~Contradicción modelo ↔ datasets~~ | **Disuelta** | Sin fine-tuning no hay corpus de entrenamiento que pueda contradecir a los datasets (D21) |
| **R15** | Dedicación semanal del alumno | **Media** *(era alta)* | Bajó a **12 h/semana** con el calendario de 6 semanas (D27). Se mantiene: declarar la dedicación antes de la inscripción y repartir los checkpoints de recuperación proactivamente |
| **R16** | Aprovisionamiento de cuentas | **Media** *(era alta)* | Con 6 semanas, Qdrant se necesita en la semana 3 y Langfuse en la semana 5. Hay margen para rescatar a un rezagado, pero no para empezar de cero: todo se cierra en la semana 0 |
| **R14** | **El simulador es un punto único de fallo** (nuevo) | Alta | Si el Space cae, se caen los labs L3 a L11 de todos los equipos a la vez. Mitigación: `DATA_SOURCE=csv` como modo degradado —las tools siguen funcionando— y el docente verifica `/health` 24 h antes de cada sesión |
| **R9** | **Dependencia de 4 servicios SaaS externos** (HF, Qdrant, Langfuse, Spaces): si uno cae, la sesión se cae | Media | Checkpoint de recuperación por lab (I5); el docente valida los 4 servicios 24 h antes de cada sesión |

> **Nota sobre planes gratuitos:** Qdrant Cloud y Langfuse Cloud fueron verificados contra sus
> páginas oficiales de precios el 2026-09-05. Los de Hugging Face (Inference y Spaces) quedaron
> **pendientes de verificación** y deben confirmarse antes de comprometer el diseño.
