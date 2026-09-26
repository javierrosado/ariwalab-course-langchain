# AriwaLabs — presentaciones editables del curso

**14 presentaciones · 122 capítulos pedagógicos · 366 diapositivas.**

Cada capítulo tiene exactamente tres diapositivas: concepto, desarrollo y ejemplo aplicado. Los capítulos agrupan las secciones indicadas abajo; objetivos, logística, pre-work, laboratorios y límites de alcance están incluidos en esa correspondencia. No se han añadido portadas fuera del cómputo.

Fuente de verdad: repositorio `javierrosado/ariwalab-course-langchain`, revisión `27c24090f1662f9473b673d2020e7bffee04490b`. Se consultaron los 366 archivos Markdown y Python de la revisión para contrastar README, preparación, demos, laboratorios, soluciones y módulos comunes. El contenido fuente del curso no se modifica.

## Archivos por sesión

| Sesión | Capítulos | Diapositivas | PPTX | Notas |
|---|---:|---:|---|---|
| Preparación: modelos de lenguaje | 22 | 66 | [00-preparacion-editable-v2.pptx](00-preparacion-editable-v2.pptx) | [00-preparacion-NOTAS-SLIDES.md](00-preparacion-NOTAS-SLIDES.md) |
| Fundamentos de los agentes inteligentes | 12 | 36 | [01-fundamentos-agentes-editable-v2.pptx](01-fundamentos-agentes-editable-v2.pptx) | [01-fundamentos-agentes-NOTAS-SLIDES.md](01-fundamentos-agentes-NOTAS-SLIDES.md) |
| Prompts, mensajes y contratos | 7 | 21 | [02-ecosistema-langchain-editable.pptx](02-ecosistema-langchain-editable.pptx) | [02-ecosistema-langchain-NOTAS-SLIDES.md](02-ecosistema-langchain-NOTAS-SLIDES.md) |
| Herramientas e integración externa | 7 | 21 | [03-tools-api-externa-editable-v2.pptx](03-tools-api-externa-editable-v2.pptx) | [03-tools-api-externa-NOTAS-SLIDES.md](03-tools-api-externa-NOTAS-SLIDES.md) |
| Catálogo de tools e integración | 8 | 24 | [04-tools-multiples-editable-v2.pptx](04-tools-multiples-editable-v2.pptx) | [04-tools-multiples-NOTAS-SLIDES.md](04-tools-multiples-NOTAS-SLIDES.md) |
| Memoria contextual y RAG con Qdrant | 9 | 27 | [05-memoria-rag-editable-v2.pptx](05-memoria-rag-editable-v2.pptx) | [05-memoria-rag-NOTAS-SLIDES.md](05-memoria-rag-NOTAS-SLIDES.md) |
| Automatización, límites y guardrails | 8 | 24 | [06-automatizacion-guardrails-editable-v2.pptx](06-automatizacion-guardrails-editable-v2.pptx) | [06-automatizacion-guardrails-NOTAS-SLIDES.md](06-automatizacion-guardrails-NOTAS-SLIDES.md) |
| Hackathon, clínica y Proyecto M2 | 6 | 18 | [07-hackathon-m2-editable.pptx](07-hackathon-m2-editable.pptx) | [07-hackathon-m2-NOTAS-SLIDES.md](07-hackathon-m2-NOTAS-SLIDES.md) |
| Despliegue con HF Spaces | 8 | 24 | [08-despliegue-hf-spaces-editable-v2.pptx](08-despliegue-hf-spaces-editable-v2.pptx) | [08-despliegue-hf-spaces-NOTAS-SLIDES.md](08-despliegue-hf-spaces-NOTAS-SLIDES.md) |
| Observabilidad y trazabilidad con Langfuse | 7 | 21 | [09-observabilidad-langfuse-editable.pptx](09-observabilidad-langfuse-editable.pptx) | [09-observabilidad-langfuse-NOTAS-SLIDES.md](09-observabilidad-langfuse-NOTAS-SLIDES.md) |
| Evaluación y optimización continua | 7 | 21 | [10-evaluacion-optimizacion-editable.pptx](10-evaluacion-optimizacion-editable.pptx) | [10-evaluacion-optimizacion-NOTAS-SLIDES.md](10-evaluacion-optimizacion-NOTAS-SLIDES.md) |
| Aplicación final y sustentación | 7 | 21 | [11-sustentacion-final-editable-v2.pptx](11-sustentacion-final-editable-v2.pptx) | [11-sustentacion-final-NOTAS-SLIDES.md](11-sustentacion-final-NOTAS-SLIDES.md) |
| Seminario internacional: casos y contraste | 6 | 18 | [12-seminario-internacional-editable.pptx](12-seminario-internacional-editable.pptx) | [12-seminario-internacional-NOTAS-SLIDES.md](12-seminario-internacional-NOTAS-SLIDES.md) |
| Bonus: el mismo agente en Microsoft Foundry | 8 | 24 | [13-bonus-foundry-editable-v2.pptx](13-bonus-foundry-editable-v2.pptx) | [13-bonus-foundry-NOTAS-SLIDES.md](13-bonus-foundry-NOTAS-SLIDES.md) |

## Cómo editar y usar las presentaciones

- Los textos son cuadros de texto nativos; las tablas se editan por celda. Los contenedores y conectores también son objetos editables.
- Las notas del orador están incorporadas en cada diapositiva y duplicadas en un archivo NOTAS-SLIDES por sesión. Abra el panel de notas de PowerPoint para consultarlas.
- El lienzo es 16:9, equivalente a 1600 × 900. La fuente de diseño es DejaVu Sans; si su equipo la sustituye, revise los saltos de línea después de reemplazarla por la fuente de su presentación.
- Las tres diapositivas de cada capítulo forman una unidad. Puede ocultar bloques ya conocidos, usar el ejemplo como actividad o dejarlo como práctica posterior. El material es un banco docente; no prescribe aumentar las horas del curso.
- Los casos están identificados como didácticos. No representan políticas comerciales reales ni mediciones realizadas al construir el PPTX. Los ejemplos del seminario son hipotéticos y no se atribuyen a invitados reales.

## Progresión y reutilización

LLM, contexto, tools y control reaparecen con el mismo vocabulario y paleta. S1 presenta la arquitectura; S3 detalla la ejecución de tools; S4 amplía el catálogo; S5 separa memoria y recuperación; S6 añade controles; S8 muestra las fronteras del despliegue; S9 vuelve observable el recorrido; S10 aplica criterios de evaluación; S11 reúne el sistema y sus decisiones. El seminario contrasta esas decisiones. El bonus distingue cambiar de proveedor de alojar un grafo.

## Mapa de capítulos y fuentes

### Preparación: modelos de lenguaje

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Ruta de preparación | 1, 2, 3 | [Ruta de estudio y resultados](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/README.md) |
| 2 | API y LLM: qué puedes verificar | 4, 5, 6 | [Fundamentos §1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 3 | Generación token a token | 7, 8, 9 | [Fundamentos §2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 4 | Tokens: unidades del texto | 10, 11, 12 | [Fundamentos §3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 5 | Contexto: presupuesto por llamada | 13, 14, 15 | [Fundamentos §4 · A](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 6 | Dónde vive la conversación | 16, 17, 18 | [Fundamentos §4 · B](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 7 | Temperatura y variación | 19, 20, 21 | [Fundamentos §5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 8 | Alucinación: plausible y falsa | 22, 23, 24 | [Fundamentos §6 · A](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 9 | Tres defensas complementarias | 25, 26, 27 | [Fundamentos §6 · B](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 10 | Embeddings: representación vectorial | 28, 29, 30 | [Fundamentos §7 · A](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 11 | Búsqueda semántica | 31, 32, 33 | [Fundamentos §7 · B](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 12 | Costo de una conversación | 34, 35, 36 | [Fundamentos §8 · A](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/code/04_costo.py) |
| 13 | Reducir contexto con criterio | 37, 38, 39 | [Fundamentos §8 · B](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/code/04_costo.py) |
| 14 | Pesos abiertos e inferencia en nube | 40, 41, 42 | [Fundamentos §9](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 15 | Prompt, RAG y fine-tuning | 43, 44, 45 | [Fundamentos §10](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/fundamentos-llm.md) |
| 16 | Python: aislar y verificar | 46, 47, 48 | [Python y entorno §§1–2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/python-y-entorno.md) |
| 17 | Configuración y secretos | 49, 50, 51 | [Python y entorno §§3–4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/python-y-entorno.md) |
| 18 | Pydantic y el contrato de salida | 52, 53, 54 | [Python y entorno §5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/python-y-entorno.md) |
| 19 | Tres cuentas, tres funciones | 55, 56, 57 | [Alta de cuentas §§1–3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/alta-de-cuentas.md) |
| 20 | Diagnóstico por capas | 58, 59, 60 | [Errores frecuentes y verificación](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/conceptos-previos/python-y-entorno.md) |
| 21 | Cuatro demos para observar | 61, 62, 63 | [code/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/code/README.md) |
| 22 | Salida de S0 y siguiente paso | 64, 65, 66 | [Autoevaluación y checklist](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/00-preparacion/autoevaluacion.md) |

### Fundamentos de los agentes inteligentes

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Objetivos de aprendizaje | 1, 2, 3 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 2 | LLM y fuente de verdad | 4, 5, 6 | [§2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 3 | Un LLM solo no es un agente | 7, 8, 9 | [§3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 4 | El ciclo del agente | 10, 11, 12 | [§4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 5 | Workflow frente a agente | 13, 14, 15 | [§5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 6 | Anatomía de LangChain 1.x | 16, 17, 18 | [§6](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 7 | Modelos abiertos y cerrados | 19, 20, 21 | [§7](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 8 | La capa comun/provider.py | 22, 23, 24 | [§8](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 9 | De la apertura al laboratorio L1 | 25, 26, 27 | [§9 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 10 | Elección del track | 28, 29, 30 | [§10](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 11 | Alcance de S1 y evolución posterior | 31, 32, 33 | [§11](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |
| 12 | Siguiente paso: del texto al contrato | 34, 35, 36 | [§12](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md) |

### Prompts, mensajes y contratos

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Del primer llamado al primer contrato | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |
| 2 | Mensajes, roles y statelessness | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |
| 3 | Rol, contexto, tarea y formato | 7, 8, 9 | [§2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |
| 4 | Few-shot para desambiguar | 10, 11, 12 | [§3 · regla A5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |
| 5 | Salida estructurada y validación | 13, 14, 15 | [§4 y comun/structured.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |
| 6 | Medir el clasificador en L2 | 16, 17, 18 | [§5 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |
| 7 | Puente hacia herramientas | 19, 20, 21 | [Qué NO entra hoy y conexión L3/L4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md) |

### Herramientas e integración externa

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Del conocimiento a la consulta | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |
| 2 | Function calling: proponer y ejecutar | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |
| 3 | Docstring y esquema de argumentos | 7, 8, 9 | [§2 · regla A2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |
| 4 | Errores que el modelo puede usar | 10, 11, 12 | [§3 · regla A4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |
| 5 | Bucle manual y create_agent | 13, 14, 15 | [§4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |
| 6 | Laboratorio L3 y Assignment A1 | 16, 17, 18 | [§5 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |
| 7 | Del primer conector al catálogo | 19, 20, 21 | [proyecto-final y Qué NO entra hoy](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md) |

### Catálogo de tools e integración

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | De una tool a cuatro | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 2 | Responsabilidad única en el catálogo | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 3 | Selección dinámica y confusiones | 7, 8, 9 | [§2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 4 | Few-shot para elegir herramientas | 10, 11, 12 | [§2.1 · regla A5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 5 | Cuatro tools núcleo y alcance | 13, 14, 15 | [§3 · regla A1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 6 | Idempotencia y límite de iteraciones | 16, 17, 18 | [§4 · regla A4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 7 | MCP: exponer y descubrir tools | 19, 20, 21 | [Pre-work MCP y conceptos-previos](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |
| 8 | Laboratorio L4: integrar y medir | 22, 23, 24 | [§5, proyecto-final y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md) |

### Memoria contextual y RAG con Qdrant

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | No recuerda y no sabe | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 2 | Estado por thread_id | 4, 5, 6 | [§1 y solucion/*/memory.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 3 | Embeddings del dominio | 7, 8, 9 | [§2 y comun/provider.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 4 | Chunking y contexto de la cláusula | 10, 11, 12 | [§3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 5 | Colección, punto y payload | 13, 14, 15 | [§4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 6 | RAG tradicional y RAG agéntico | 16, 17, 18 | [§5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 7 | Recuperar y citar: salvaguarda A6 | 19, 20, 21 | [§6 y comun/prompts_industria.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 8 | Conocimiento recuperable y actualización | 22, 23, 24 | [Demo paramétrico vs recuperable](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |
| 9 | Laboratorio L5: integrar memoria y RAG | 25, 26, 27 | [lab/README.md y requisitos de entrada](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md) |

### Automatización, límites y guardrails

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | De habilitar a limitar | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 2 | Inyección de prompt | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 3 | PII y minimización | 7, 8, 9 | [§2 y demos de entrada/salida](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 4 | Límites de actuación | 10, 11, 12 | [§3 y demo de acción](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 5 | Guardrail de salida | 13, 14, 15 | [§4 y code/03_guardrail_salida.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 6 | Middleware y puntos de enganche | 16, 17, 18 | [§4 y solucion/*/agent.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 7 | Límites por industria y derivación | 19, 20, 21 | [§5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |
| 8 | Laboratorio L6: probar los límites | 22, 23, 24 | [§6 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md) |

### Hackathon, clínica y Proyecto M2

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Probar comportamiento no determinístico | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md) |
| 2 | Guardrails y estrés: fallos diferentes | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md) |
| 3 | Cuatro familias de casos borde | 7, 8, 9 | [§0 y §2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md) |
| 4 | Clínica de 45 minutos | 10, 11, 12 | [§2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md) |
| 5 | Demo y argumentación del Proyecto M2 | 13, 14, 15 | [§3 y §4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md) |
| 6 | Cerrar M2 y preparar producción | 16, 17, 18 | [§4–§5 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md) |

### Despliegue con HF Spaces

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Del script a un servicio invocable | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 2 | Configuración por entorno | 4, 5, 6 | [§1 · 12-Factor](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 3 | Dockerfile: describir el arranque | 7, 8, 9 | [§2 y solucion/*/Dockerfile](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 4 | FastAPI: health y chat | 10, 11, 12 | [§3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 5 | Secretos en el Space | 13, 14, 15 | [§4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 6 | Cold start y latencia percibida | 16, 17, 18 | [§5](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 7 | Laboratorio L8: despliegue verificable | 19, 20, 21 | [§6 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |
| 8 | De disponibilidad a observabilidad | 22, 23, 24 | [§7 y conexión S9](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md) |

### Observabilidad y trazabilidad con Langfuse

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Hacer visible la ejecución | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |
| 2 | Logs, métricas y trazas | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |
| 3 | Anatomía de una traza | 7, 8, 9 | [§2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |
| 4 | p50, p95 y promedio | 10, 11, 12 | [§3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |
| 5 | PII en la telemetría | 13, 14, 15 | [§4 y comun/observability.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |
| 6 | Laboratorio L9: dos cuellos de botella | 16, 17, 18 | [§5 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |
| 7 | De trazas a evaluación | 19, 20, 21 | [§6 y conexión S10](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) |

### Evaluación y optimización continua

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Mejorar con evidencia | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |
| 2 | El golden dataset del curso | 4, 5, 6 | [§1](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |
| 3 | Tres evaluadores determinísticos | 7, 8, 9 | [§2 y comun/evaluadores.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |
| 4 | LLM-as-judge: uso y sesgos | 10, 11, 12 | [§3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |
| 5 | Mejora, variación y repetición | 13, 14, 15 | [§4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |
| 6 | Laboratorio L10: un cambio dirigido | 16, 17, 18 | [§5 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |
| 7 | Preparar evidencia para la sustentación | 19, 20, 21 | [§6 y conexión S11](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md) |

### Aplicación final y sustentación

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Cerrar el proyecto acumulativo | 1, 2, 3 | [Objetivos y §2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |
| 2 | Cliente web y streaming | 4, 5, 6 | [Objetivos, code/README.md y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |
| 3 | Argumentar una decisión de arquitectura | 7, 8, 9 | [§0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |
| 4 | Guion de diez minutos | 10, 11, 12 | [§0 · guion de demo](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |
| 5 | Contingencia y evidencia anticipada | 13, 14, 15 | [§6](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |
| 6 | Documento de diseño de cuatro páginas | 16, 17, 18 | [§7](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |
| 7 | Rúbrica, laboratorio y cierre | 19, 20, 21 | [§§8–10 y lab/README.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-11-sustentacion-final/README.md) |

### Seminario internacional: casos y contraste

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Escuchar decisiones de industria | 1, 2, 3 | [Objetivos y §0](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/seminario-internacional/README.md) |
| 2 | Tres mecanismos para un panel útil | 4, 5, 6 | [§2](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/seminario-internacional/README.md) |
| 3 | Guion del seminario en vivo | 7, 8, 9 | [§3](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/seminario-internacional/README.md) |
| 4 | Preparar tres preguntas | 10, 11, 12 | [§4 y preparacion.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/seminario-internacional/README.md) |
| 5 | Documento de contraste | 13, 14, 15 | [§5 y plantilla-contraste.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/seminario-internacional/README.md) |
| 6 | Cierre formativo del curso | 16, 17, 18 | [§6 y cronograma](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/seminario-internacional/README.md) |

### Bonus: el mismo agente en Microsoft Foundry

| Capítulo | Título | Slides | Sección fuente |
|---:|---|---|---|
| 1 | Modelo de recursos de Azure | 1, 2, 3 | [Paso 1 y acceso-azure.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 2 | Dos vías de acceso | 4, 5, 6 | [Paso 2 y acceso-azure.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 3 | Deployment y variables del destino | 7, 8, 9 | [Paso 3 y acceso-azure.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 4 | El switch del proveedor | 10, 11, 12 | [Paso 4](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 5 | Hosted agent y protocolo Responses | 13, 14, 15 | [Paso 5 y host/main.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 6 | Envolver el agente: qué porta | 16, 17, 18 | [Paso 6 y host/main.py](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 7 | Desplegar con azd | 19, 20, 21 | [Paso 7 y host/azure.yaml](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
| 8 | Comparar siete dimensiones | 22, 23, 24 | [Paso 8 y plantilla-comparativa.md](https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-4-plus-foundry/README.md) |
