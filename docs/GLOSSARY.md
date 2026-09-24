# Terminología canónica

Este documento fija el uso editorial. [El glosario para alumnos](../recursos/glosario.md)
conserva explicaciones y ejemplos extensos. “Primera aparición” indica el punto de entrada
didáctico del recorrido, no la primera coincidencia al ordenar archivos alfabéticamente.
El glosario de S0 anticipa términos que se desarrollan después; consultar el
[mapa de progresión](COURSE-MAP.md) para implementación y evaluación.

| Término preferido | Definición | Primera aparición | Uso recomendado | Evitar por ambigüedad |
|---|---|---|---|---|
| LLM | Modelo de lenguaje entrenado para generar secuencias de tokens a partir del contexto | S0, fundamentos | Distinguir modelo de aplicación agente | “Base de datos que sabe todo” |
| Model / Chat model | Interfaz de un modelo conversacional que recibe mensajes y devuelve mensajes | S0/glosario; S1 | `get_chat_model()` en ejemplos del curso | “Agente” para una llamada aislada |
| Messages | Registros de conversación con rol, contenido y, cuando corresponde, Tool Calls | S1, demo 2 | `SystemMessage`, `HumanMessage`, `AIMessage`, `ToolMessage` | Confundir mensaje `tool` con función tool |
| System Prompt | Instrucciones de comportamiento aportadas por la aplicación | S0/glosario; S1 | Identidad, tarea y límites; no autorización ejecutable | “Garantía de seguridad” |
| Prompt Engineering | Diseño y evaluación de instrucciones, ejemplos y contexto | S2 | Medir cambios con el mismo conjunto de casos | “Entrenar pesos” al editar un prompt |
| Few-shot | Ejemplos incluidos en el contexto de una llamada | S0/glosario; S2 | Comparar su efecto y costo | “Fine-tuning” |
| Structured Output | Salida conforme a un esquema, validada según la integración utilizada | S0/glosario; S2 | Distinguir validez del esquema de veracidad del dato | “JSON siempre correcto” |
| Pydantic | Biblioteca de esquemas y validación de datos de Python | S0, Python | `BaseModel`, restricciones y errores de validación | “El LLM ejecuta la clase” |
| Tool | Función o capacidad que el runtime expone al modelo mediante un contrato | S0/glosario; S1 mapa | Nombre, descripción, argumentos y ejecución controlada | “API externa” si es una función local |
| Tool Calling | Propuesta estructurada de invocar una tool; la aplicación ejecuta | S1 mapa; S3 | Separar propuesta, validación, ejecución y resultado | “El modelo ejecuta Python” |
| Function Calling | Nombre usado para Tool Calling de funciones | S3 | Explicar equivalencia al introducirlo; preferir Tool Calling después | Presentarlos como dos capacidades sin relación |
| Agent | Sistema que usa un modelo para decidir acciones dentro de un bucle controlado | S0/glosario; S1 | Diferenciar modelo, runtime, herramientas y entorno | Exigir memoria persistente a todo agente |
| Agentic Loop | Ciclo decisión → acción → observación hasta respuesta o límite | S1 | Distinguir vueltas del bucle y cantidad de herramientas disponibles | “Número de tools = número de pasos” |
| ReAct | Patrón que combina razonamiento y acciones con observaciones | S0/glosario; S1 | Relacionarlo con el bucle S3; no exigir razonamiento interno expuesto | “Todo agente imprime Thought” |
| Workflow | Flujo cuyas transiciones decide la lógica de aplicación, incluyendo condiciones y ciclos | S1 | Comparar quién decide la ruta, código o modelo | “Secuencia siempre lineal” |
| MCP | Protocolo de conexión entre clientes y servidores que exponen capacidades | S0/glosario; S4 | Distinguir protocolo, transporte, descubrimiento y ejecución | “Biblioteca LangChain” |
| Memory | Estado que la aplicación conserva y vuelve a aportar al modelo | S1/S2 | En L5: historial por `thread_id` en un diccionario por proceso | Equipararla con RAG o pesos del modelo |
| Middleware | Intercepción de pasos de ejecución; LangChain también define una API específica | S1 mapa; S6 | L6 enseña wrappers manuales, no `AgentMiddleware` | Dar por utilizada la API nativa |
| Guardrail | Control que detecta, bloquea o transforma comportamientos definidos | S0/glosario; S6 | Declarar cobertura y límites del control | “Garantía contra todos los ataques” |
| Human-in-the-loop | Intervención humana real en una decisión de ejecución | S0/glosario; S4 | Una aprobación verificable debe proceder de una persona autenticada | Equipararlo con un booleano propuesto por el LLM |
| RAG | Recuperación de fuentes que se aportan como contexto para generar una respuesta | S0; S5 implementación | Separar ingesta, recuperación y generación | “El modelo aprende esos documentos en sus pesos” |
| RAG agéntico | El agente decide invocar recuperación como una herramienta | S0/glosario; S5 | La política A6 orienta; comprobar llamadas y fuentes | “Recuperación garantizada por prompt” |
| Embedding | Representación vectorial producida por un modelo | S0 | Mismo espacio de embeddings para indexación y consulta | Reutilizar vectores de otro modelo por tener igual dimensión |
| Vector Store | Almacén e índice para recuperar por similitud vectorial y filtros | S0/glosario; S5 | Distinguir almacenamiento, embedding y retriever | “Memoria conversacional” |
| Qdrant | Tecnología de base vectorial utilizada como servicio gestionado | S0 cuentas; S5 | Colección, punto, vector, payload y filtros | “El modelo de embeddings” |
| Chunking | División del corpus en fragmentos para indexación y recuperación | S0/glosario; S5 | Declarar unidad y solapamiento del splitter utilizado | “Un tamaño universalmente óptimo” |
| Retriever | Componente que selecciona documentos o fragmentos para una consulta | S0/glosario; S5 | `retrieve_knowledge_base` cuenta como tool en RAG agéntico | Confundirlo con generación de respuestas |
| Observability | Capacidad de investigar ejecuciones mediante señales instrumentadas | S0/glosario; S9 | Logs, métricas y trazas con alcance explícito | “Instrumentación automática de todo” |
| Langfuse | Plataforma de observabilidad y evaluación usada en S9/S10 | S0 cuentas | El callback instrumenta llamadas; revisar agrupación y PII | “LangSmith” como nombre de este componente |
| Trace / Span | Traza de ejecución y operación delimitada dentro de ella | S0/glosario; S9 | Un nombre compartido no demuestra parentesco entre spans | “Un log equivale a una traza completa” |
| Evaluation | Medición de un comportamiento frente a criterios y casos definidos | S2 medición; S10 formalización | Registrar entradas, versión, resultados y aplicabilidad | “Una respuesta bonita demuestra calidad” |
| Golden dataset | Conjunto de casos con expectativas explícitas | S2 | 30 casos por track; conservar finalidad de cada campo | Tratar casos usados para ajustar prompts como prueba independiente |
| Groundedness | Grado de respaldo de las afirmaciones por las fuentes recuperadas | S0/glosario; S5 | S10 usa un proxy léxico de cobertura limitada | “Coincidencia de subcadena demuestra cita válida” |
| LLM-as-judge | Evaluación realizada por otro llamado a un modelo según instrucciones | S10 | Demo y análisis de sesgos, no fuente de la nota | “Juez objetivo infalible” |
| Multi-agent | Sistema que coordina varios agentes | Sin unidad lectiva identificada | Mencionar ausencia de implementación y evaluación | Confundir cuatro tracks independientes con cuatro agentes coordinados |
| Microsoft Foundry | Plataforma utilizada en el bonus para modelos y hosting gestionado | S1 anticipación; bonus | Separar cambio de proveedor, embeddings y adaptación del host | “Un switch conserva automáticamente todos los controles” |
| Streaming / SSE | Envío progresivo de eventos al cliente | S11 | Checkpoint transmite fragmentos después de validar respuesta completa | “Tokens en vivo del modelo” para el checkpoint actual |
| Idempotencia | Repetir una operación conserva el efecto de una sola ejecución | S4 | Una lectura puede devolver datos nuevos; confirmación no deduplica escrituras | “Idempotente = siempre devuelve idéntico texto” |

Los nombres técnicos en código conservan su forma original. Las variantes históricas de los
niveles de rúbrica se corresponden por posición (1–4), pero su unificación requiere confirmar
la nomenclatura institucional: CONS-020. No cambiar pesos ni criterios por una normalización editorial.
