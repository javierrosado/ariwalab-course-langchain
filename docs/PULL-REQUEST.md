# Borrador de PR: coherencia técnica, gobernanza y material visual del curso

Destino: `feature/curso-final` → `main`. Estado: **borrador preparado localmente**.
No aprobar ni fusionar: existen decisiones y verificaciones pendientes.

## Objetivo

El curso construido conserva afirmaciones del plan inicial y promesas que no corresponden a
sus checkpoints. Esta revisión hace explícito el recorrido real y corrige contratos técnicos,
referencias y material docente; incorpora gobernanza y diagramas reutilizables.

## Alcance

Documentación, quizzes, comentarios de código, mensajes de demo, validador de materiales,
imágenes y notas. Se conserva arquitectura, datos, dependencias, horas y pesos de evaluación.
Los cambios previos de finales de línea permanecen en el árbol de trabajo y se excluyen de
los commits de esta revisión.

## Módulos procesados

M1 Fundamentos; M2 Agentes avanzados; M3 Producción y seminario; M4 bonus Foundry;
nivelación, infraestructura compartida, recursos y documentación del docente.

## Sesiones procesadas

S0, S1–S11, seminario y bonus. [Mapa y trazabilidad](COURSE-MAP.md).

## Archivos modificados

Ver [informe de entrega](DELIVERY-REPORT.md) y el diff de los commits. El inventario inicial
completo está en [COURSE-INVENTORY](COURSE-INVENTORY.md).

## Cambios pedagógicos

- Separación entre introducción, implementación, práctica y evaluación.
- Corrección de Structured Output y Test 2; opciones sin marcado de respuesta anticipada.
- Distinción de catálogo de tools, iteraciones, memoria por proceso y RAG.
- Límites explícitos de controles, métricas, trazas, streaming y portabilidad.

## Cambios técnicos

Se corrigen explicaciones y mensajes de la demo de extracción, docstrings de helpers y rutas.
`docente/validar_materiales.py` añade validación sin red de AST Python y enlaces Markdown
inline locales, incluyendo anclas. No implementa aprobación humana real ni migra embeddings.

## Inconsistencias encontradas

27, con severidad, evidencia, impacto y propuesta en [el reporte](COURSE-CONSISTENCY-REPORT.md).

## Inconsistencias corregidas

17 cerradas como FIXED; cinco OPEN conservan trabajo pendiente. El cierre de una afirmación
documental no certifica una capacidad de producción que el checkpoint no implementa.

## DECISION REQUIRED

CONS-006: aprobación humana verificable; CONS-010: política de embeddings del bonus;
CONS-014: contrato de evaluación y aplicabilidad; CONS-019: 20 minutos adicionales en S4;
CONS-020: nomenclatura institucional de las rúbricas. Alternativas e impactos en el reporte.

## Gobernanza creada

AGENTS, mapa, glosario canónico, guía editorial, inventario y reporte de consistencia.

## Assets visuales

Design System, catálogo y registro de generación. Seis diagramas generados con imagegen,
copiados al repositorio y revisados visualmente. [Catálogo](../imagenes/CATALOGO-IMAGENES.md).

## Imágenes identificadas

Seis: Agentic Loop, Structured Output, Memory/RAG, Guardrails, despliegue/observabilidad,
evaluación. Se prioriza reutilización sobre una imagen por sección.

## Imágenes generadas

Seis PNG finales, aproximadamente 16:9. Variantes descartadas no se incluyen en Git.

## Imágenes pendientes

Cero entre las seis seleccionadas. No se han creado capturas de portales ni evidencia ficticia.

## Speaker Notes

14 archivos: S0, S1–S11, seminario y bonus. S0 explica por qué se usan demos existentes;
las otras notas incluyen mensaje, ejemplo, pregunta, error frecuente y conexiones entre sesiones.

## Tests ejecutados

Datasets, 24 tools, Structured Output, selección simulada, guardrails simulados con y sin
fallos inyectados, simulador mediante TestClient y validador de materiales. Detalle y límites
en [VALIDATION-REPORT](VALIDATION-REPORT.md).

## Validaciones realizadas

Rutas/anclas locales, sintaxis Python, correspondencia teoría/checkpoints, contratos de labs,
rúbricas, prompts, archivos visuales y diff contra `main`. La revisión global no sustituye una
auditoría exhaustiva de todos los caminos de ejecución ni una prueba de servicios reales.

## Riesgos

Persisten cinco hallazgos abiertos y cinco decisiones. No se validaron inferencia ni servicios
cloud; las cuotas y despliegues del ROADMAP siguen pendientes. El bonus no está certificado
como migración equivalente del agente completo. Los proxies de evaluación tienen límites.

## Observaciones

No se hizo push, merge, squash ni force push. `prompt.txt` permanece sin versionar.
Este documento prepara una revisión local; no representa un PR publicado en GitHub.

## Checklist de revisión humana

- [ ] Resolver o aceptar explícitamente los hallazgos OPEN y DECISION REQUIRED.
- [ ] Confirmar tiempos, nomenclatura de rúbricas y aprobación académica.
- [ ] Verificar inferencia, Qdrant, Langfuse, Spaces y Foundry con evidencia real.
- [ ] Revisar las limitaciones de seguridad, persistencia y evaluación antes del dictado.
- [ ] Revisar legibilidad de PNG en el proyector y las notas por sesión.
- [ ] Revisar diff final contra `main` antes de aprobar; no merge automático.
