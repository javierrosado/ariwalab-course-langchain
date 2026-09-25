# Catálogo de imágenes

Seis mecanismos seleccionados por utilidad pedagógica. Las sesiones restantes reutilizan
estos assets con notas específicas; una sesión no necesita una imagen nueva por cada sección.

| ID | Módulo | Sesión | Sección | Concepto | Archivo | Tipo | Nivel | Objetivo pedagógico | Prioridad | Reutilizable | Industria | Sesiones relacionadas | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IMG-M01-S01-001 | modulo-1-fundamentos | sesion-01-fundamentos-agentes | Mecanismo central | Agentic Loop | `imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/01-agentic-loop.png` | Agentic Loop | L1 | Separar propuesta del modelo y ejecución por el runtime | HIGH | Sí | Transversal; ejemplos en notas | S1; S3; S4; S7 | GENERATED |
| IMG-M01-S02-001 | modulo-1-fundamentos | sesion-02-ecosistema-langchain | Mecanismo central | Structured Output | `imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/01-structured-output.png` | Flujo | L2 | Distinguir validación estructural y recuperación acotada | HIGH | Sí | Transversal; ejemplos en notas | S2; S7 | GENERATED |
| IMG-M02-S05-001 | modulo-2-agentes-avanzados | sesion-05-memoria-rag | Mecanismo central | Memory y RAG | `imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/01-memoria-rag.png` | Comparación | L2 | Separar historial conversacional de recuperación documental | HIGH | Sí | Transversal; ejemplos en notas | S5; S7; S11 | GENERATED |
| IMG-M02-S06-001 | modulo-2-agentes-avanzados | sesion-06-automatizacion-guardrails | Mecanismo central | Guardrails | `imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/01-controles.png` | Arquitectura | L2 | Ubicar controles y explicar su cobertura acotada | HIGH | Sí | Transversal; ejemplos en notas | S6; S7; S11 | GENERATED |
| IMG-M03-S08-001 | modulo-3-produccion | sesion-08-despliegue-hf-spaces | Mecanismo central | Despliegue y observabilidad | `imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/01-despliegue.png` | Arquitectura | L2 | Situar fronteras de API, agente y servicios gestionados | HIGH | Sí | Transversal; ejemplos en notas | S8; S9; S11; Bonus | GENERATED |
| IMG-M03-S10-001 | modulo-3-produccion | sesion-10-evaluacion-optimizacion | Mecanismo central | Evaluation | `imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/01-evaluacion.png` | Flujo | L2 | Comparar versiones con evidencia y límites de medición | HIGH | Sí | Transversal; ejemplos en notas | S10; S11 | GENERATED |

Formato de las imágenes: 1672 × 941, aproximadamente 16:9.
S3/S4/S7/S9/S11/bonus reutilizan estos archivos. S0 tiene diagramas propios, listados a continuación.

## Sesión 0 · Nivelación

Doce diagramas para el estudio asíncrono de S0. Las cifras de 002–004 provienen del texto de
`fundamentos-llm.md` y llevan la etiqueta *ejemplo ilustrativo*; no son mediciones. Los
componentes de 010–012 siguen la documentación oficial consultada el 24-09-2026.
Prompts en [`00-preparacion/PROMPTS-IMAGENES.md`](00-preparacion/PROMPTS-IMAGENES.md) y notas en
[`00-preparacion/NOTAS-SLIDES.md`](00-preparacion/NOTAS-SLIDES.md).

| ID | Módulo | Sesión | Sección | Concepto | Archivo | Tipo | Nivel | Objetivo pedagógico | Prioridad | Reutilizable | Industria | Sesiones relacionadas | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IMG-S00-001 | 00-preparacion | S0 | README · Ruta de estudio | Ruta de nivelación | `imagenes/00-preparacion/01-ruta-sesion-0.png` | Flujo | L1 | Mostrar orden, tiempos y condición bloqueante de S0 | MEDIUM | No | Transversal | S0; S1 | GENERATED |
| IMG-S00-002 | 00-preparacion | S0 | fundamentos-llm §1, §2, §5 | LLM vs API; temperatura | `imagenes/00-preparacion/02-llm-no-es-una-api.png` | Comparación | L1 | Romper la expectativa de determinismo y contrato fijo | HIGH | Sí | Seguros en el ejemplo | S0; S1; S10 | GENERATED |
| IMG-S00-003 | 00-preparacion | S0 | fundamentos-llm §3, §4, §8 | Tokens, contexto y costo | `imagenes/00-preparacion/03-tokens-contexto-costo.png` | Mecanismo | L2 | Explicar por qué el historial reenviado domina el costo | HIGH | Sí | Transversal | S0; S5; S10 | GENERATED |
| IMG-S00-004 | 00-preparacion | S0 | fundamentos-llm §7 | Embeddings | `imagenes/00-preparacion/04-embeddings-significado.png` | Mecanismo | L1 | Mostrar búsqueda por significado y la escala de similitud coseno | HIGH | Sí | Telco en el ejemplo | S0; S5 | GENERATED |
| IMG-S00-005 | 00-preparacion | S0 | fundamentos-llm §6, §10 | Alucinación; fine-tuning vs RAG | `imagenes/00-preparacion/05-alucinacion-conocimiento.png` | Comparación | L1 | Ubicar las tres defensas y separar estilo de conocimiento | HIGH | Sí | Seguros y Telco en el ejemplo | S0; S3; S4; S5; S6 | GENERATED |
| IMG-S00-006 | 00-preparacion | S0 | python-y-entorno | Entorno y configuración | `imagenes/00-preparacion/06-entorno-configuracion.png` | Arquitectura | L2 | Situar .env, settings, provider y el cambio de proveedor | MEDIUM | Sí | Transversal | S0; S2; S8; Bonus | GENERATED |
| IMG-S00-007 | 00-preparacion | S0 | alta-de-cuentas | Cuentas del curso | `imagenes/00-preparacion/07-tres-cuentas.png` | Flujo | L1 | Mostrar cuándo se usa cada cuenta y cómo se verifica el stack | MEDIUM | No | Transversal | S0; S1; S5; S9 | GENERATED |
| IMG-S00-008 | 00-preparacion | S0 | Complemento de fundamentos-llm §2 | Anatomía de un LLM | `imagenes/00-preparacion/08-anatomia-llm.png` | Mecanismo | L1 | Nombrar las partes de un LLM y ubicar pesos y control de la aplicación | HIGH | Sí | Telco en el ejemplo | S0; S1; S5 | GENERATED |
| IMG-S00-009 | 00-preparacion | S0 | fundamentos-llm §1 | Ejemplo API vs LLM | `imagenes/00-preparacion/09-ejemplo-api-vs-llm.png` | Comparación | L3 | Contrastar contrato fijo y salida probabilística con un caso del simulador | HIGH | Sí | Telco (AndesMóvil) | S0; S1; S3 | GENERATED |
| IMG-S00-010 | 00-preparacion | S0 | alta-de-cuentas · Hugging Face | Hugging Face | `imagenes/00-preparacion/10-hugging-face.png` | Arquitectura | L2 | Distinguir componentes ofrecidos y usados de Hugging Face | MEDIUM | Sí | Transversal | S0; S1; S5; S8 | GENERATED |
| IMG-S00-011 | 00-preparacion | S0 | alta-de-cuentas · Qdrant Cloud | Qdrant Cloud | `imagenes/00-preparacion/11-qdrant-cloud.png` | Arquitectura | L2 | Distinguir componentes ofrecidos y usados de Qdrant Cloud | MEDIUM | Sí | Transversal | S0; S5; S7 | GENERATED |
| IMG-S00-012 | 00-preparacion | S0 | alta-de-cuentas · Langfuse Cloud | Langfuse Cloud | `imagenes/00-preparacion/12-langfuse-cloud.png` | Arquitectura | L2 | Distinguir componentes ofrecidos y usados de Langfuse Cloud | MEDIUM | Sí | Transversal | S0; S9; S10 | GENERATED |
