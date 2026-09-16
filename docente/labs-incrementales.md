# Laboratorios incrementales

> Puntos 6 y 9 del encargo. **Un solo repositorio por equipo** que crece laboratorio a laboratorio.
> Nada se tira: cada lab recibe el artefacto del anterior y le agrega una capa.
> Stack **100 % open source y 100 % SaaS**; nada corre en la laptop del alumno salvo Python.
> El Lab 12 es el *plus* **opcional y asíncrono**: el mismo agente, sin cambios de código, en Microsoft Foundry.
> **Equipos de 2 personas** (D19), por el límite del plan gratuito de Langfuse.

---

## 1. Artefacto acumulativo — cómo crece el proyecto

```
proyecto-final/<track>/
├── .env                        L1   HF · Qdrant · Langfuse · track
├── requirements.txt            L1
├── data/                       L1   datasets sintéticos del track
├── app/
│   ├── provider.py             L1   get_chat_model() / get_embeddings()  [huggingface|foundry]
│   ├── schemas.py              L2   modelos Pydantic del dominio
│   ├── prompts.py              L2   plantillas Rol+Contexto+Tarea+Formato
│   ├── tools/
│   │   ├── external_api.py     L3   1 tool contra API externa
│   │   └── domain_tools.py     L4   catálogo de 6 tools del dominio
│   ├── knowledge/
│   │   ├── ingest.py           L5   carga + chunking + embeddings → Qdrant Cloud
│   │   └── retriever.py        L5   tool de recuperación
│   ├── memory.py               L5   estado conversacional por thread_id
│   ├── guardrails.py           L6   validación, PII, límites, escalamiento
│   ├── agent.py                L3→L6 crece en cada lab
│   ├── api.py                  L8   FastAPI (/chat, /health)
│   ├── observability.py        L9   callback de Langfuse
│   └── web/index.html          L11  cliente HTML
├── Dockerfile                  L8   imagen para HF Spaces
├── tests/                      L7   pruebas de estrés y casos borde
├── evals/                      L10  golden dataset + evaluators
├── host/                       L12  main.py (ResponsesHostServer) + azure.yaml
└── README.md                   L1→L12 documentación viva
```

> ⚠️ **Aclaración que debió estar aquí desde el L1.** El diagrama de arriba describe la
> estructura que debe tener el **repositorio de cada equipo** — usa `proyecto-final/<track>/`
> como nombre de carpeta ilustrativo. Es una ruta **distinta** de `proyecto-final/<track>/` en
> **este** repositorio del curso, que es la **implementación de referencia del docente** (ya
> escrita, la que leen `docente/verificar_tools.py` y `docente/matriz_seleccion.py`). Ver la
> tabla completa en `README.md` raíz, sección "`proyecto-final/`: qué es y qué no es". Un alumno
> nunca copia la del curso: construye la suya, laboratorio a laboratorio.

---

## 2. Cadena de laboratorios

| Lab | Sesión | Nombre | Entrada | Salida nueva | Servicio SaaS nuevo | Base en el repo |
|---|---|---|---|---|---|---|
| **L1** | 1 | Entorno y primer agente-cero | — | `.env`, `provider.py`, `data/` | HF | `01-introduction/code/*` |
| **L2** | 2 | Clasificador de intención | L1 | `schemas.py`, `prompts.py` | — | `03/code/03,05,07,08` |
| **L3** | 3 | Primera tool + API externa | L2 | `tools/external_api.py`, `agent.py` v1 | — | `04/solution/weather_tool.py`, `05/code/01` |
| **L4** | 4 | Catálogo de **4 tools** | L3 | `tools/domain_tools.py`, `agent.py` v2 | — | `04/code/04`, `05/code/02` |
| **L5** | 5 | Memoria + RAG en Qdrant Cloud | L4 | `knowledge/`, `memory.py`, `agent.py` v3 | **Qdrant Cloud** | `07/*`, `08/code/02`, `05/code/03` |
| **L6** | 6 | Guardrails y límites | L5 | `guardrails.py`, `agent.py` v4 | — | `05/code/04`, `02/code/05` |
| **L7** | 7 | Hackathon: pruebas de estrés | L6 | `tests/`, `agent.py` v5 endurecido | — | `06/code/04`, `02/samples/robust_chat.py` |
| **L8** | 8 | Contenedor y despliegue en HF Spaces | L7 | `Dockerfile`, `app/api.py`, URL pública | **HF Spaces** | contenido nuevo |
| **L9** | 9 | Trazabilidad con Langfuse | L8 | `observability.py`, agente instrumentado | **Langfuse Cloud** | contenido nuevo |
| **L10** | 10 | Evaluación y optimización | L9 | `evals/`, golden dataset, prompts v2 | — | contenido nuevo |
| **L11** | 11 | Aplicación final y sustentación | L10 | `app/web/index.html`, app desplegada | — | contenido nuevo |
| **L12** | bonus | **PLUS · el mismo agente en Foundry** *(asíncrono, opcional)* | L11 | `host/main.py`, `host/azure.yaml` | **Microsoft Foundry** | `09/code/*` |

---

## 3. Detalle de cada laboratorio

### L1 · Entorno y primer agente-cero
- **Objetivo:** cuentas creadas y un script que llama a un modelo open-weights **en línea** y responde una pregunta del dominio.
- **Alta de servicios:** Hugging Face (token), Qdrant Cloud (cluster) y Langfuse Cloud (proyecto) — las tres se crean aquí aunque se usen después, para que ningún equipo se bloquee más adelante.
- **Elección de track (regla fijada en la Sesión 1): el equipo propone, el docente balancea.**
  Cada equipo de 2 declara su track al cerrar la Sesión 1 en vivo; el docente ajusta la
  propuesta para que los 4 tracks queden representados en la sustentación final y para que
  Banca —el más exigente en guardrails y structured output— no caiga en el equipo más débil.
  El track es **irrevocable**: L2 a L11 se construyen sobre él. Ver el detalle en
  `docente/casos-de-uso-industrias.md`.
- **Criterio:** el script corre sin instalar ningún motor de inferencia ni base de datos en la laptop.

### L2 · Clasificador de intención
- **Objetivo:** convertir texto libre del cliente en estructura tipada (`Intencion`: categoría +
  urgencia + entidades) con Pydantic, clasificando **obligatoriamente** con `extraer()` de
  `comun/structured.py` — `with_structured_output()` directo está prohibido en el lab.
- **Taxonomía — alineada 1:1 con las 4 tools núcleo del L4** (`docente/esqueletos/sesion-02.md`
  §6; corregido aquí: la versión anterior de esta fila listaba `PORTABILIDAD`, que es una tool
  **opcional**, y omitía el consumo, que sí es núcleo):
  - **telecomunicaciones:** `CONSULTA_PLAN` · `CONSULTA_CONSUMO` · `AVERIA` · `RECLAMO` · `OTRO`
  - **banca:** `CONSULTA_SALDO` · `CONSULTA_MOVIMIENTOS` · `CONSULTA_TARJETA` · `SOSPECHA_FRAUDE` · `OTRO`
  - **retail:** `SEGUIMIENTO_PEDIDO` · `CONSULTA_PRODUCTO` · `CONSULTA_STOCK` · `DEVOLUCION` · `OTRO`
  - **seguros:** `CONSULTA_POLIZA` · `COTIZACION` · `ESTADO_SINIESTRO` · `REPORTE_SINIESTRO` · `OTRO`
- **Criterio:** ≥ 90 % de acierto sobre las 26 consultas del golden set
  (`recursos/golden/consultas-<track>.json`, campo `intencion` — incluye la categoría `OTRO`)
  + 5 consultas propias del equipo, reportadas aparte sobre las 31.

### L3 · Primera tool + API externa
- **Objetivo:** el modelo deja de "saber" y empieza a "consultar".
- **Criterio:** 3 escenarios documentados (éxito, dato inexistente, API caída) — es el **Assignment A1**.
- **Riesgo a vigilar:** aquí se prueba por primera vez el tool calling del modelo de HF (R1 del ADR).

### L4 · Catálogo de 4 tools
- **Objetivo:** selección dinámica de herramienta según la tarea.
- **Por qué 4 y no 6 (A1):** la precisión de selección cae notoriamente pasadas 4-5 herramientas, y los errores se multiplican a lo largo del bucle. Las 2 tools restantes de cada track quedan como reto opcional.
- **Criterio:** matriz consulta × tool esperada con ≥ 85 % de selección correcta.
- **Pre-work asíncrono (decidido en `docente/esqueletos/sesion-04.md`): MCP se consume, no se
  construye.** El alumno conecta su agente al servidor MCP que el simulador ya expone (6 tools,
  transportes stdio y HTTP) con `langchain-mcp-adapters` / `MultiServerMCPClient` — ver
  `simulador-industria/docs/GUIA-MCP.md`. Construir un servidor MCP propio con 2 tools pasa a ser
  el **reto opcional** del L4, no el pre-work: no cabe en 1 hora para quien escribió su primera
  tool hace dos días.

### L5 · Memoria + RAG en Qdrant Cloud
- **Objetivo:** el agente responde con la documentación real del negocio y recuerda la conversación.
- **Incremento:** corpus del track embebido con `multilingual-e5-large` (HF Inference) e indexado en una colección de **Qdrant Cloud**; `thread_id` para la memoria.
- **Salvaguarda A6:** el system prompt de la industria (`comun/prompts_industria.py`) obliga a recuperar y citar ante cualquier afirmación sobre tarifas, coberturas o políticas. No es solo una defensa técnica: es un requisito de auditoría — una respuesta sin fuente no es verificable.
- **Prerrequisito bloqueante:** cluster de Qdrant operativo **antes** de la sesión 5. Sin fallback (D10).
- **Criterio:** el agente **decide** cuándo buscar (RAG agéntico) y **cita la fuente**; 10 preguntas con cita verificable.

### L6 · Guardrails y límites
- **Objetivo:** que el agente sea desplegable en una industria regulada.
- **Incremento:** middleware de validación, enmascaramiento de DNI/tarjeta, lista de acciones prohibidas, escalamiento a humano, defensa ante prompt injection.
- **Criterio:** batería de 15 ataques con **0 filtraciones**.

### L7 · Hackathon — pruebas de estrés
- **Objetivo:** romper el agente propio y el del equipo vecino.
- **Criterio:** demo en vivo + informe con ≥ 10 casos borde y su resolución. Es el **Proyecto M2**.

### L8 · Contenedor y despliegue en HF Spaces
- **Objetivo:** sacar el agente del entorno de desarrollo y darle una URL pública.
- **Incremento:** `Dockerfile`, API **FastAPI** con `/chat` y `/health`, Space creado, secretos cargados como *Space secrets* (nunca en el repo), despliegue por `git push`.
- **Criterio:** cualquiera puede invocar el agente por HTTP desde fuera, sin credenciales del alumno en el código.

### L9 · Trazabilidad con Langfuse
- **Objetivo:** ver por dentro qué hizo el agente en cada ejecución **ya desplegado**.
- **Incremento:** callback de Langfuse en el agente; trazas del Space real, no de la laptop.
- **Criterio:** identificar y documentar **2 cuellos de botella reales** a partir de trazas propias.

### L10 · Evaluación y optimización
- **Objetivo:** mejorar con evidencia, no con intuición.
- **Incremento:** golden dataset de 30 casos en Langfuse Datasets, evaluators (exactitud, groundedness, uso correcto de tools), LLM-as-judge, prompts v2.
- **Criterio:** mejora medible entre v1 y v2 sobre el mismo dataset, con tabla comparativa.

### L11 · Aplicación final
- **Objetivo:** entregar el producto.
- **Incremento:** cliente HTML con streaming contra la API, despliegue final, documento de diseño con diagrama de arquitectura.
- **Criterio:** demo end-to-end ante panel. Es el **Proyecto Integrador Final**.

### L12 · PLUS · el mismo agente en Microsoft Foundry *(bonus asíncrono, opcional)*
- **Objetivo:** demostrar que una arquitectura bien diseñada es portable, y abrir el Curso 2.
- **Incremento:** `AI_PROVIDER=foundry` en el `.env`, wrapper `ResponsesHostServer`, `azure.yaml`, `azd up`.
- **La lección:** `agent.py`, `tools/`, `guardrails.py` y `schemas.py` **no se tocan**. Solo cambia `provider.py` por configuración. Eso es lo que se evalúa.
- **Entregable:** agente respondiendo en el playground de Foundry + **cuadro comparativo open source vs Foundry** hecho por el equipo (costo, soberanía del dato, operación, velocidad de despliegue, vendor lock-in).
- **Criterio:** el equipo argumenta cuándo elegiría cada uno. Ese argumento es la evaluación del bloque plus.
- **No ponderado:** al ser bonus, no afecta la nota de ningún módulo. Quien no tenga suscripción de Azure no queda en desventaja.

---

## 4. Invariantes de la incrementalidad

| # | Regla | Motivo |
|---|---|---|
| I1 | Ningún lab reescribe desde cero lo del anterior | Punto 9 del encargo |
| I2 | Cada lab entrega un **README actualizado** del proyecto | El documento de diseño final se escribe solo |
| I3 | Cada lab cierra con el proyecto **ejecutable**; nunca se deja roto entre sesiones | Un equipo que falta puede retomar |
| I4 | El esqueleto de código es **idéntico en los 4 tracks**; cambian datos, tools y prompts | El docente mantiene una sola base |
| I5 | Se entrega un **checkpoint de recuperación** por lab (`solucion/`) | Con 4 tracks paralelos el docente no puede rescatar en vivo a un equipo atrasado |
| I6 | **Nada se instala en la laptop** salvo Python y las librerías cliente | Principio P2 del curso |
| I7 | Las credenciales viven en `.env` (local) y en *secrets* del Space (nube), **nunca en el repo** | Se enseña desde el L1, no desde el L8 |
| I8 | El código del agente **no conoce a su proveedor**: todo pasa por `provider.py` | Es lo que hace posible el L12 sin reescribir nada |
| I9 | Máximo **4 tools** enlazadas a la vez y toda docstring dice **cuándo NO** usar la tool | La fiabilidad se compone a lo largo del bucle (D20) |

> **I8 es la columna vertebral del curso.** Si se rompe en cualquier lab, el bloque plus de Foundry
> deja de funcionar y se pierde la lección de arquitectura que justifica todo el diseño.
