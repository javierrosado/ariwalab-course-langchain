# Informe de entrega — revisión de consistencia

`prompt.txt` solicita **análisis y modificaciones**, con commits y preparación de PR.
Esta ejecución produjo una revisión documentada y cambios en `feature/curso-final`.
**No equivale a la versión final aceptada del curso**: hay hallazgos abiertos, decisiones
del autor y verificaciones cloud pendientes. El PR queda preparado como borrador local.

## Resultado medible

| Elemento | Resultado |
|---|---|
| Módulos analizados | 4, más nivelación, seminario y recursos compartidos |
| Sesiones recorridas | S0, S1–S11, seminario y bonus |
| Inventario inicial | 425 archivos versionados |
| Markdown revisados estructuralmente | 201 iniciales; análisis semántico dirigido según reporte |
| Markdown existentes modificados | 36 |
| Markdown nuevos | 38 |
| Código revisado estructuralmente | 183 Python iniciales; revisión semántica de helpers, demos, checkpoints y verificadores relevantes |
| Código existente modificado | 3 Python: docstrings y mensajes didácticos; sin cambio funcional de agentes |
| Código nuevo | docente/validar_materiales.py |
| Inconsistencias registradas | 27 |
| Inconsistencias corregidas | 17 FIXED |
| Pendientes | 5 OPEN + 5 DECISION REQUIRED |
| Imágenes identificadas / generadas | 6 / 6 |
| Imágenes pendientes de generación | 0 del catálogo seleccionado |
| Reutilización | 2 assets usados en 7 contextos adicionales: S3/S4/S7 y S9/S11/seminario/bonus |
| NOTAS-SLIDES.md | 14; S0 usa demos existentes sin imagen nueva |
| Archivos existentes modificados | 39 |
| Nuevos archivos | 46 |
| Total de archivos en el cambio | 85 |
| PR | Borrador local; sin push, aprobación ni merge |

## Pruebas y alcance

Pasaron datasets, tools, Structured Output, matriz simulada, guardrails simulados sin
filtraciones, simulador TestClient y validación de materiales. La simulación de guardrails
con una filtración por track terminó en salida 1, como corresponde al caso negativo del arnés.
No es una medición de seguridad del agente. El validador final comprobó 239 Markdown,
184 Python y 874 enlaces locales, con cero errores. Detalle: [VALIDATION-REPORT](VALIDATION-REPORT.md).

El control de whitespace pasa al reconocer CRLF mediante `core.whitespace=cr-at-eol`.
Los commits contienen únicamente diferencias de esta revisión; los finales de línea previos
se conservan en el árbol de trabajo. Por ello `git status` puede seguir mostrando archivos
modificados después de los commits sin que exista una diferencia de contenido nueva.

## Pendientes y recomendación

- Resolver embeddings del bonus antes de ejecutar RAG con otro proveedor (CONS-010).
- Decidir alcance de aprobación humana real, aplicabilidad de evaluadores, tiempo de S4 y nombres de rúbricas.
- Cerrar formulaciones históricas, agrupación de trazas, runner de evaluación y verificaciones de servicios pendientes.
- Revisar material con el autor y validar despliegues/cuotas antes de declarar el curso listo para dictado.

Las decisiones conservan alternativas e impacto en [COURSE-CONSISTENCY-REPORT](COURSE-CONSISTENCY-REPORT.md).
El cambio de modalidad de S4 o de política de embeddings no se infirió de la ausencia de respuesta.

## Assets, prompts y notas

Los seis PNG finales están dentro de `imagenes/`, generados con **imagegen integrado**.
[Catálogo](../imagenes/CATALOGO-IMAGENES.md), [Design System](../imagenes/DESIGN-SYSTEM.md).
Cada carpeta de imagen contiene `PROMPTS-IMAGENES.md`; las carpetas de sesiones que reutilizan
assets enlazan el prompt original. El registro de generación conserva hashes y dimensiones.

## Archivos existentes modificados

- [00-preparacion/autoevaluacion.md](../00-preparacion/autoevaluacion.md)
- [CLAUDE.md](../CLAUDE.md)
- [PLAN-CURRICULAR.md](../PLAN-CURRICULAR.md)
- [README.md](../README.md)
- [ROADMAP.md](../ROADMAP.md)
- [comun/evaluadores.py](../comun/evaluadores.py)
- [comun/structured.py](../comun/structured.py)
- [docente/esqueletos/README.md](../docente/esqueletos/README.md)
- [docente/esqueletos/VALIDACION-INTEGRAL.md](../docente/esqueletos/VALIDACION-INTEGRAL.md)
- [docente/esqueletos/sesion-02.md](../docente/esqueletos/sesion-02.md)
- [docente/guia-docente.md](../docente/guia-docente.md)
- [docente/presentaciones/bonus-foundry.md](../docente/presentaciones/bonus-foundry.md)
- [docente/presentaciones/sesion-02.md](../docente/presentaciones/sesion-02.md)
- [docente/presentaciones/sesion-04.md](../docente/presentaciones/sesion-04.md)
- [docente/presentaciones/sesion-09.md](../docente/presentaciones/sesion-09.md)
- [docente/presentaciones/sesion-10.md](../docente/presentaciones/sesion-10.md)
- [modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md](../modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md)
- [modulo-1-fundamentos/sesion-01-fundamentos-agentes/conceptos-previos.md](../modulo-1-fundamentos/sesion-01-fundamentos-agentes/conceptos-previos.md)
- [modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md](../modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md)
- [modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/03_structured_crudo_vs_robusto.py](../modulo-1-fundamentos/sesion-02-ecosistema-langchain/code/03_structured_crudo_vs_robusto.py)
- [modulo-1-fundamentos/sesion-02-ecosistema-langchain/conceptos-previos.md](../modulo-1-fundamentos/sesion-02-ecosistema-langchain/conceptos-previos.md)
- [modulo-1-fundamentos/sesion-03-tools-api-externa/README.md](../modulo-1-fundamentos/sesion-03-tools-api-externa/README.md)
- [modulo-1-fundamentos/sesion-03-tools-api-externa/assignment-a1.md](../modulo-1-fundamentos/sesion-03-tools-api-externa/assignment-a1.md)
- [modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md](../modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md)
- [modulo-2-agentes-avanzados/sesion-04-tools-multiples/pre-work-mcp.md](../modulo-2-agentes-avanzados/sesion-04-tools-multiples/pre-work-mcp.md)
- [modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md](../modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md)
- [modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md](../modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md)
- [modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md](../modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md)
- [modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md](../modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md)
- [modulo-3-produccion/sesion-08-despliegue-hf-spaces/lab/README.md](../modulo-3-produccion/sesion-08-despliegue-hf-spaces/lab/README.md)
- [modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md](../modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md)
- [modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md](../modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md)
- [modulo-3-produccion/sesion-10-evaluacion-optimizacion/lab/README.md](../modulo-3-produccion/sesion-10-evaluacion-optimizacion/lab/README.md)
- [modulo-3-produccion/sesion-11-sustentacion-final/README.md](../modulo-3-produccion/sesion-11-sustentacion-final/README.md)
- [modulo-4-plus-foundry/README.md](../modulo-4-plus-foundry/README.md)
- [recursos/glosario.md](../recursos/glosario.md)
- [recursos/rubricas/rubrica-a1.md](../recursos/rubricas/rubrica-a1.md)
- [recursos/rubricas/rubrica-final.md](../recursos/rubricas/rubrica-final.md)
- [recursos/rubricas/rubrica-m2.md](../recursos/rubricas/rubrica-m2.md)

## Nuevos archivos

- [AGENTS.md](../AGENTS.md)
- [docente/validar_materiales.py](../docente/validar_materiales.py)
- [docs/CONTENT-GUIDELINES.md](../docs/CONTENT-GUIDELINES.md)
- [docs/COURSE-CONSISTENCY-REPORT.md](../docs/COURSE-CONSISTENCY-REPORT.md)
- [docs/COURSE-INVENTORY.md](../docs/COURSE-INVENTORY.md)
- [docs/COURSE-MAP.md](../docs/COURSE-MAP.md)
- [docs/DELIVERY-REPORT.md](../docs/DELIVERY-REPORT.md)
- [docs/GLOSSARY.md](../docs/GLOSSARY.md)
- [docs/PULL-REQUEST.md](../docs/PULL-REQUEST.md)
- [docs/VALIDATION-REPORT.md](../docs/VALIDATION-REPORT.md)
- [imagenes/00-preparacion/NOTAS-SLIDES.md](../imagenes/00-preparacion/NOTAS-SLIDES.md)
- [imagenes/CATALOGO-IMAGENES.md](../imagenes/CATALOGO-IMAGENES.md)
- [imagenes/DESIGN-SYSTEM.md](../imagenes/DESIGN-SYSTEM.md)
- [imagenes/GENERATION-LOG.json](../imagenes/GENERATION-LOG.json)
- [imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/01-agentic-loop.png](../imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/01-agentic-loop.png)
- [imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/NOTAS-SLIDES.md](../imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/NOTAS-SLIDES.md)
- [imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/PROMPTS-IMAGENES.md](../imagenes/modulo-1-fundamentos/sesion-01-fundamentos-agentes/PROMPTS-IMAGENES.md)
- [imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/01-structured-output.png](../imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/01-structured-output.png)
- [imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/NOTAS-SLIDES.md](../imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/NOTAS-SLIDES.md)
- [imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/PROMPTS-IMAGENES.md](../imagenes/modulo-1-fundamentos/sesion-02-ecosistema-langchain/PROMPTS-IMAGENES.md)
- [imagenes/modulo-1-fundamentos/sesion-03-tools-api-externa/NOTAS-SLIDES.md](../imagenes/modulo-1-fundamentos/sesion-03-tools-api-externa/NOTAS-SLIDES.md)
- [imagenes/modulo-1-fundamentos/sesion-03-tools-api-externa/PROMPTS-IMAGENES.md](../imagenes/modulo-1-fundamentos/sesion-03-tools-api-externa/PROMPTS-IMAGENES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-04-tools-multiples/NOTAS-SLIDES.md](../imagenes/modulo-2-agentes-avanzados/sesion-04-tools-multiples/NOTAS-SLIDES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-04-tools-multiples/PROMPTS-IMAGENES.md](../imagenes/modulo-2-agentes-avanzados/sesion-04-tools-multiples/PROMPTS-IMAGENES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/01-memoria-rag.png](../imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/01-memoria-rag.png)
- [imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/NOTAS-SLIDES.md](../imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/NOTAS-SLIDES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/PROMPTS-IMAGENES.md](../imagenes/modulo-2-agentes-avanzados/sesion-05-memoria-rag/PROMPTS-IMAGENES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/01-controles.png](../imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/01-controles.png)
- [imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/NOTAS-SLIDES.md](../imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/NOTAS-SLIDES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/PROMPTS-IMAGENES.md](../imagenes/modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/PROMPTS-IMAGENES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/NOTAS-SLIDES.md](../imagenes/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/NOTAS-SLIDES.md)
- [imagenes/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/PROMPTS-IMAGENES.md](../imagenes/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/PROMPTS-IMAGENES.md)
- [imagenes/modulo-3-produccion/seminario-internacional/NOTAS-SLIDES.md](../imagenes/modulo-3-produccion/seminario-internacional/NOTAS-SLIDES.md)
- [imagenes/modulo-3-produccion/seminario-internacional/PROMPTS-IMAGENES.md](../imagenes/modulo-3-produccion/seminario-internacional/PROMPTS-IMAGENES.md)
- [imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/01-despliegue.png](../imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/01-despliegue.png)
- [imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/NOTAS-SLIDES.md](../imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/NOTAS-SLIDES.md)
- [imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/PROMPTS-IMAGENES.md](../imagenes/modulo-3-produccion/sesion-08-despliegue-hf-spaces/PROMPTS-IMAGENES.md)
- [imagenes/modulo-3-produccion/sesion-09-observabilidad-langfuse/NOTAS-SLIDES.md](../imagenes/modulo-3-produccion/sesion-09-observabilidad-langfuse/NOTAS-SLIDES.md)
- [imagenes/modulo-3-produccion/sesion-09-observabilidad-langfuse/PROMPTS-IMAGENES.md](../imagenes/modulo-3-produccion/sesion-09-observabilidad-langfuse/PROMPTS-IMAGENES.md)
- [imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/01-evaluacion.png](../imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/01-evaluacion.png)
- [imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/NOTAS-SLIDES.md](../imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/NOTAS-SLIDES.md)
- [imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/PROMPTS-IMAGENES.md](../imagenes/modulo-3-produccion/sesion-10-evaluacion-optimizacion/PROMPTS-IMAGENES.md)
- [imagenes/modulo-3-produccion/sesion-11-sustentacion-final/NOTAS-SLIDES.md](../imagenes/modulo-3-produccion/sesion-11-sustentacion-final/NOTAS-SLIDES.md)
- [imagenes/modulo-3-produccion/sesion-11-sustentacion-final/PROMPTS-IMAGENES.md](../imagenes/modulo-3-produccion/sesion-11-sustentacion-final/PROMPTS-IMAGENES.md)
- [imagenes/modulo-4-plus-foundry/NOTAS-SLIDES.md](../imagenes/modulo-4-plus-foundry/NOTAS-SLIDES.md)
- [imagenes/modulo-4-plus-foundry/PROMPTS-IMAGENES.md](../imagenes/modulo-4-plus-foundry/PROMPTS-IMAGENES.md)

## Commits y revisión Git

El repositorio no tenía identidad Git configurada. Los commits de esta revisión usan
`Codex <codex@localhost>` mediante opciones por comando; no se cambió la configuración global
ni se atribuyeron los commits al usuario. La base `main` permanece en
`65c64a65d7fca83f0443cdbdd1dfdce1698f819f`.

Cinco commits de contenido/visuales y un sexto de validación/entrega, todos locales.
El sexto commit contiene este informe; su hash se consulta en `git log -1`.
[Borrador de PR](PULL-REQUEST.md).

| Commit | Propósito |
|---|---|
| `b61700f` | docs: add course governance and consistency audit |
| `f32d3fa` | docs: correct foundation contracts and assessments |
| `1822648` | docs: align advanced and production sessions with code |
| `4d2ce32` | docs: align course overview and instructor guidance |
| `e07f1ef` | visual: add reusable course diagrams and speaker notes |
| Commit de cierre | `chore: validate course materials and prepare draft PR` |
