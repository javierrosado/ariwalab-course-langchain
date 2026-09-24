# Informe de consistencia del curso

Fecha de revisión: 2026-09-24. Rama: `feature/curso-final`; base: `main`.
El inventario inicial contiene 425 archivos, 201 Markdown y 183 Python. Los cambios previos
de archivos versionados eran finales de línea (diff vacío con `--ignore-space-at-eol`).
`prompt.txt` no está versionado y se conserva como instrucción del usuario.

## Alcance y criterio de cierre

La revisión conecta sesiones, código, labs y evaluaciones como una unidad. `FIXED` indica
corrección comprobada del hallazgo descrito, no certificación de todos los servicios.
`OPEN` conserva trabajo pendiente; `DECISION REQUIRED` necesita decisión del autor;
`ACCEPTED` registra una limitación explícita aceptada, nunca una aprobación inferida.
No declarar el curso final ni el PR listo para integración con problemas críticos pendientes.

## Hallazgos

### CONS-001 — Se describen carpetas vacías y entregables por construir.

- **Tipo:** Estado
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** —
- **Archivo:** README.md; PLAN-CURRICULAR.md
- **Descripción:** Se describen carpetas vacías y entregables por construir.
- **Evidencia inicial:** README: «aún vacías»; PLAN §9: «Por construir».
- **Impacto:** El lector desconoce el material disponible.
- **Corrección propuesta:** Actualizar estado según inventario, conservando aprobación académica pendiente.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-002 — Se afirma que Pydantic no valida y que el fallo debe ocurrir en vivo.

- **Tipo:** Técnico/pedagógico
- **Severidad:** HIGH
- **Módulo:** M1
- **Sesión:** S2
- **Archivo:** README; conceptos-previos; code/03_structured_crudo_vs_robusto.py
- **Descripción:** Se afirma que Pydantic no valida y que el fallo debe ocurrir en vivo.
- **Evidencia inicial:** comun/structured.py captura ValidationError; with_structured_output recibe una clase Pydantic.
- **Impacto:** Enseña un contrato falso y evalúa esa falsedad en Test 2.
- **Corrección propuesta:** Corregir teoría, preguntas, demo y slides: validación existente, reintento acotado y error explícito.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-003 — Se presenta 0.93^n como tasa universal y número de tools como número de pasos.

- **Tipo:** Técnico
- **Severidad:** HIGH
- **Módulo:** M1/M2
- **Sesión:** S1/S4/S7
- **Archivo:** README S4; PLAN-CURRICULAR; glosario
- **Descripción:** Se presenta 0.93^n como tasa universal y número de tools como número de pasos.
- **Evidencia inicial:** S4 §3 declara caída a partir de 4–5 herramientas sin medición general.
- **Impacto:** Confunde un modelo simplificado con una ley de arquitectura.
- **Corrección propuesta:** Declarar supuestos de independencia/tasa condicional y separar catálogo de iteraciones.
- **Estado:** OPEN
- **Avance y pendiente:** Se corrigieron los supuestos en el plan y S4; quedan formulaciones históricas por revisar y no existe medición universal del límite del catálogo.

### CONS-004 — Máximo cuatro tools contradice cuatro núcleo + retriever.

- **Tipo:** Coherencia
- **Severidad:** HIGH
- **Módulo:** M2
- **Sesión:** S4/S5
- **Archivo:** CLAUDE.md; pre-work-mcp.md; agent.py L5
- **Descripción:** Máximo cuatro tools contradice cuatro núcleo + retriever.
- **Evidencia inicial:** ALL_TOOLS = TOOLS_NUCLEO + [retrieve_knowledge_base].
- **Impacto:** La gobernanza prohíbe el checkpoint que pide el lab.
- **Corrección propuesta:** Describir cuatro de negocio en L4, cinco con retriever desde L5; no agregar opcionales sin medir.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-005 — Afirma que cada track dispone de dos tools MCP.

- **Tipo:** MCP
- **Severidad:** MEDIUM
- **Módulo:** M2
- **Sesión:** S4
- **Archivo:** pre-work-mcp.md
- **Descripción:** Afirma que cada track dispone de dos tools MCP.
- **Evidencia inicial:** mcp_server.py: telco 2, banca 1, retail 1, seguros 2.
- **Impacto:** El checklist exige descubrir herramientas que no existen.
- **Corrección propuesta:** Corregir reparto real y la recomendación de enlazar seis tools.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-006 — El booleano confirmado_por_cliente procede de argumentos del modelo.

- **Tipo:** Seguridad
- **Severidad:** HIGH
- **Módulo:** M2/M3
- **Sesión:** S4–S11
- **Archivo:** guardrails.py; domain_tools.py
- **Descripción:** El booleano confirmado_por_cliente procede de argumentos del modelo.
- **Evidencia inicial:** check_action comprueba args.get(...); no consulta aprobación autenticada.
- **Impacto:** El modelo puede proponer true sin una aprobación verificable.
- **Corrección propuesta:** Documentar límite; decidir alcance de un estado de aprobación externo antes de producción.
- **Estado:** DECISION REQUIRED
- **Avance y pendiente:** Se documentó la limitación del booleano. Implementar aprobación autenticada cambia el alcance; decisión del autor pendiente.

### CONS-007 — Regex y API key de equipo se presentan como garantía y autorización por cliente.

- **Tipo:** Seguridad
- **Severidad:** HIGH
- **Módulo:** M2
- **Sesión:** S6
- **Archivo:** README; guardrails.py; simulador-industria/auth.py
- **Descripción:** Regex y API key de equipo se presentan como garantía y autorización por cliente.
- **Evidencia inicial:** auth.py identifica equipo; check_action no comprueba titularidad de cuenta.
- **Impacto:** Puede confundirse un ejercicio sintético con control de acceso completo.
- **Corrección propuesta:** Corregir alcance didáctico, cobertura acotada y ausencia de identidad de cliente.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-008 — El wrapper manual se confunde con la API Middleware de LangChain 1.x.

- **Tipo:** API/terminología
- **Severidad:** MEDIUM
- **Módulo:** M2
- **Sesión:** S6
- **Archivo:** README; code/04_middleware.py
- **Descripción:** El wrapper manual se confunde con la API Middleware de LangChain 1.x.
- **Evidencia inicial:** Demo usa funciones de entrada/acción/salida; no AgentMiddleware.
- **Impacto:** El alumno no distingue patrón arquitectónico e interfaz de librería.
- **Corrección propuesta:** Explicitar diferencia y enlazar documentación oficial, sin migrar el checkpoint.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-009 — Promesa de migración completa sin cambios contradice el host.

- **Tipo:** Portabilidad
- **Severidad:** HIGH
- **Módulo:** M4
- **Sesión:** Bonus
- **Archivo:** README; host/main.py; comun/provider.py
- **Descripción:** Promesa de migración completa sin cambios contradice el host.
- **Evidencia inicial:** Host construye create_agent sin memoria L5 ni guardrails L6.
- **Impacto:** El alumno cree que el hosting conserva controles que no incorpora.
- **Corrección propuesta:** Separar cambio de cliente de chat de adaptación al hosting; señalar faltantes.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-010 — AI_PROVIDER cambia también los embeddings; reutilizar colección HF no es válido automáticamente.

- **Tipo:** Portabilidad/RAG
- **Severidad:** CRITICAL
- **Módulo:** M4
- **Sesión:** Bonus
- **Archivo:** comun/provider.py; comun/vectorstore.py
- **Descripción:** AI_PROVIDER cambia también los embeddings; reutilizar colección HF no es válido automáticamente.
- **Evidencia inicial:** get_embeddings elige OpenAIEmbeddings para foundry; colección por defecto 1024.
- **Impacto:** Dimensión o espacio vectorial incompatible; respuestas recuperadas incorrectas.
- **Corrección propuesta:** Elegir embeddings HF independientes o reindexación separada; no cambiar arquitectura sin decisión.
- **Estado:** DECISION REQUIRED
- **Avance y pendiente:** Promesa corregida en bonus; código de proveedores conservado hasta elegir política de embeddings.

### CONS-011 — Cinco enlaces internos a archivos inexistentes.

- **Tipo:** Links
- **Severidad:** MEDIUM
- **Módulo:** M1/M3
- **Sesión:** S3/S8
- **Archivo:** assignment-a1.md; S8/lab/README.md
- **Descripción:** Cinco enlaces internos a archivos inexistentes.
- **Evidencia inicial:** A1 sube tres niveles; L8 enlaza telecomunicaciones.md y otros tres nombres inexistentes.
- **Impacto:** No se accede a rúbrica o enunciados.
- **Corrección propuesta:** Corregir profundidad y rutas <track>/enunciado.md.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-012 — proyecto-final se describe como aplicación final completa.

- **Tipo:** Referencia
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** S1–S11
- **Archivo:** README; S4/README; CLAUDE.md
- **Descripción:** proyecto-final se describe como aplicación final completa.
- **Evidencia inicial:** Solo contiene app/__init__.py y tools en cada track; solución L11 contiene API y agente.
- **Impacto:** Un alumno busca componentes inexistentes o usa tools sin confirmación del L4.
- **Corrección propuesta:** Distinguir catálogo base para verificadores de checkpoints por sesión.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-013 — Groundedness se describe como prueba de cita y respaldo semántico.

- **Tipo:** Evaluación
- **Severidad:** HIGH
- **Módulo:** M3
- **Sesión:** S10
- **Archivo:** comun/evaluadores.py; README S10
- **Descripción:** Groundedness se describe como prueba de cita y respaldo semántico.
- **Evidencia inicial:** evaluar_groundedness solo busca la misma subcadena en respuesta y contexto.
- **Impacto:** Una coincidencia o una negación puede contarse como fundamentación.
- **Corrección propuesta:** Describir proxy léxico y complementar revisión de cita; decidir métricas más fuertes aparte.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-014 — Casos no aplicables se cuentan como aprobados y tool=None puede chocar con RAG.

- **Tipo:** Evaluación
- **Severidad:** HIGH
- **Módulo:** M3
- **Sesión:** S10
- **Archivo:** comun/evaluadores.py; recursos/golden/
- **Descripción:** Casos no aplicables se cuentan como aprobados y tool=None puede chocar con RAG.
- **Evidencia inicial:** respuesta_esperada None devuelve True; evaluar_tool compara un solo nombre.
- **Impacto:** Las tasas no reflejan cobertura; el runner debe separar tools de negocio y retriever.
- **Corrección propuesta:** Definir reporte de aplicabilidad y llamadas; registrar decisión de contrato antes de cambiar notas.
- **Estado:** DECISION REQUIRED
- **Avance y pendiente:** Lab y glosario explican aplicabilidad y separación del retriever; no se cambió el contrato de evaluación que alimenta la nota.

### CONS-015 — La jerarquía única de traza y los reintentos de extracción no están garantizados.

- **Tipo:** Teoría/código
- **Severidad:** HIGH
- **Módulo:** M3
- **Sesión:** S9
- **Archivo:** agent.py v5; code/02_anatomia_spans.py; README
- **Descripción:** La jerarquía única de traza y los reintentos de extracción no están garantizados.
- **Evidencia inicial:** Callbacks por invoke sin span padre explícito; bucle no invoca extraer_con_detalle.
- **Impacto:** La guía promete evidencia que puede no aparecer en Langfuse.
- **Corrección propuesta:** Aclarar instrumentación disponible y dejar agrupación como validación pendiente.
- **Estado:** OPEN
- **Avance y pendiente:** La teoría ya declara límites. La agrupación real de spans sigue pendiente de instrumentación/verificación con Langfuse.

### CONS-016 — p95 se equipara a peor caso; dos corridas se presentan como prueba concluyente.

- **Tipo:** Estadística
- **Severidad:** MEDIUM
- **Módulo:** M3
- **Sesión:** S9/S10
- **Archivo:** README S9; README S10
- **Descripción:** p95 se equipara a peor caso; dos corridas se presentan como prueba concluyente.
- **Evidencia inicial:** Ejemplo de diez peticiones; S10 regla de dos corridas.
- **Impacto:** Confunde convención de percentil y exploración con significancia.
- **Corrección propuesta:** Explicar nearest rank y alcance exploratorio, variabilidad y ausencia de prueba causal completa.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-017 — No hay runner completo; demo A/B no recupera contexto.

- **Tipo:** Contrato de laboratorio
- **Severidad:** HIGH
- **Módulo:** M3
- **Sesión:** S10
- **Archivo:** lab/README; solucion/*/evals/evaluadores.py; code/04_ab_prompts.py
- **Descripción:** No hay runner completo; demo A/B no recupera contexto.
- **Evidencia inicial:** Checkpoint reexporta funciones; demo solo model.invoke sobre consultas OTRO.
- **Impacto:** La tabla A/B no demuestra mejora del RAG end-to-end.
- **Corrección propuesta:** Documentar observaciones que debe recoger el alumno y alcance limitado de la demo.
- **Estado:** OPEN
- **Avance y pendiente:** Se documentó cómo recoger observaciones y el alcance de la demo; sigue faltando un runner end-to-end de referencia.

### CONS-018 — Nada corre en laptop contradice Python, venv, API local y MCP stdio.

- **Tipo:** Progresión
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** S1–Bonus
- **Archivo:** CLAUDE.md; PLAN-CURRICULAR; S8
- **Descripción:** Nada corre en laptop contradice Python, venv, API local y MCP stdio.
- **Evidencia inicial:** S0 instruye venv; S8 demo local; pre-work MCP subproceso.
- **Impacto:** Prerrequisitos imposibles de reconciliar literalmente.
- **Corrección propuesta:** Aclarar servicios gestionados e inferencia remota, con clientes/scripts locales.
- **Estado:** OPEN
- **Avance y pendiente:** Se aclaró ejecución local de clientes en README, plan y CLAUDE; otros textos históricos requieren armonización completa.

### CONS-019 — 180 minutos más 20 minutos de sustentación A1.

- **Tipo:** Calendario
- **Severidad:** MEDIUM
- **Módulo:** M2
- **Sesión:** S4
- **Archivo:** docente/esqueletos/sesion-04.md; guia-docente.md
- **Descripción:** 180 minutos más 20 minutos de sustentación A1.
- **Evidencia inicial:** VALIDACION-INTEGRAL H6 declara decisión pendiente de Javier.
- **Impacto:** El guion excede la duración lectiva.
- **Corrección propuesta:** Elegir A1 asíncrono, recorte del guion o tiempo adicional; conservar pendiente hasta respuesta.
- **Estado:** DECISION REQUIRED
- **Avance y pendiente:** Pregunta enviada al autor; no se modificaron horas ni modalidad por ausencia de respuesta.

### CONS-020 — Niveles Básico/Sobresaliente y En desarrollo/Destacado se presentan ambos como comunes.

- **Tipo:** Terminología
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** S3/S7/S11
- **Archivo:** recursos/rubricas/
- **Descripción:** Niveles Básico/Sobresaliente y En desarrollo/Destacado se presentan ambos como comunes.
- **Evidencia inicial:** A1/M2 usan los primeros; final los segundos.
- **Impacto:** Puede confundirse equivalencia entre niveles institucionales.
- **Corrección propuesta:** Documentar equivalencia ordinal; confirmar nomenclatura institucional sin cambiar pesos.
- **Estado:** DECISION REQUIRED
- **Avance y pendiente:** Se añadió equivalencia ordinal a las tres rúbricas; nombres institucionales pendientes de confirmación.

### CONS-021 — Las opciones correctas aparecen en negrita antes de abrir autocorrección.

- **Tipo:** Quizzes
- **Severidad:** LOW
- **Módulo:** M1
- **Sesión:** S0/S1/S2
- **Archivo:** autoevaluacion.md; conceptos-previos.md
- **Descripción:** Las opciones correctas aparecen en negrita antes de abrir autocorrección.
- **Evidencia inicial:** El banco promete respuestas ocultas en details.
- **Impacto:** El instrumento revela la solución antes del intento.
- **Corrección propuesta:** Quitar marcado revelador de opciones, conservar tabla de autocorrección.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-022 — Se afirma verificación con un script no versionado.

- **Tipo:** Links/scripts
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** —
- **Archivo:** docente/esqueletos/README.md; VALIDACION-INTEGRAL.md
- **Descripción:** Se afirma verificación con un script no versionado.
- **Evidencia inicial:** docente/validar_coherencia.py no existe.
- **Impacto:** No se puede reproducir la validación histórica.
- **Corrección propuesta:** Identificar resultado histórico no reproducible y aportar validador actual de rutas/sintaxis.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-023 — Middleware primera aparición S5 contradice tabla S6; bucle manual se llama demo 2.

- **Tipo:** Continuidad
- **Severidad:** LOW
- **Módulo:** M1
- **Sesión:** S1/S3
- **Archivo:** README S1; README S3
- **Descripción:** Middleware primera aparición S5 contradice tabla S6; bucle manual se llama demo 2.
- **Evidencia inicial:** S3/code/03_bucle_manual.py implementa bucle; demo 2 es binding.
- **Impacto:** Referencias cruzadas erróneas.
- **Corrección propuesta:** Corregir S6 y demo 3 y la afirmación de uso API en L1.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-024 — Memoria por proceso y SSE posterior a validación requieren explicación visible.

- **Tipo:** Persistencia/streaming
- **Severidad:** MEDIUM
- **Módulo:** M2/M3
- **Sesión:** S5/S8/S11
- **Archivo:** memory.py; README S11
- **Descripción:** Memoria por proceso y SSE posterior a validación requieren explicación visible.
- **Evidencia inicial:** _HISTORIES dict; responder_streaming llama responder antes de fragmentar.
- **Impacto:** Despliegue puede confundirse con persistencia y generación token a token.
- **Corrección propuesta:** Aclarar límites y pérdida al reiniciar; enlazar checkpoint real.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-025 — Faltan mapa, términos canónicos, auditoría y gobernanza visual.

- **Tipo:** Gobernanza
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** Todas
- **Archivo:** docs/; AGENTS.md; imagenes/
- **Descripción:** Faltan mapa, términos canónicos, auditoría y gobernanza visual.
- **Evidencia inicial:** No existen esos archivos en la base de la revisión.
- **Impacto:** Futuros cambios pueden desincronizar materiales.
- **Corrección propuesta:** Crear gobernanza, catálogo, prompts y notas con trazabilidad.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

### CONS-026 — Disponibilidad de servicios, cuotas, despliegues y aprobación académica pendientes.

- **Tipo:** Validación externa
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** S3/S5/S8/S9/Bonus
- **Archivo:** ROADMAP.md; acceso-azure.md
- **Descripción:** Disponibilidad de servicios, cuotas, despliegues y aprobación académica pendientes.
- **Evidencia inicial:** ROADMAP enumera B4–B7 y tareas am–ap.
- **Impacto:** No puede certificarse curso listo para dictado con pruebas offline.
- **Corrección propuesta:** Conservar bloqueos; registrar verificaciones locales sin afirmar resultados cloud.
- **Estado:** OPEN
- **Avance y pendiente:** Las pruebas locales se registran por separado; servicios reales, cuotas, despliegues y aprobación académica no verificados en esta revisión.

### CONS-027 — No se identifica implementación ni evaluación Multi-agent.

- **Tipo:** Cobertura
- **Severidad:** MEDIUM
- **Módulo:** Global
- **Sesión:** Multi-agent
- **Archivo:** COURSE-MAP; sesiones
- **Descripción:** No se identifica implementación ni evaluación Multi-agent.
- **Evidencia inicial:** Búsqueda de multi-agent/multiagente sin unidad lectiva.
- **Impacto:** No debe inventarse cobertura por estar nombrada en el prompt.
- **Corrección propuesta:** Registrar ausencia; no ampliar currículo sin decisión.
- **Estado:** FIXED
- **Resultado:** contenido o gobernanza corregidos en esta revisión; ver el diff asociado y la validación local. La evidencia inicial se conserva arriba.

## Decisiones pendientes: alternativas e impacto

| ID | Alternativas | Recomendación | Archivos afectados |
|---|---|---|---|
| CONS-006 | Mantener ejercicio sintético explícito; implementar aprobación autenticada fuera del modelo | No tratar el booleano como autorización real; diseñar estado de aprobación antes de producción | L4/L6, tools y API L8/L11 |
| CONS-010 | Mantener embeddings HF al cambiar chat; migrar embeddings y reindexar otra colección | Separar proveedor de chat y embeddings conserva el propósito del bonus | comun/provider.py, settings.py, vectorstore.py y bonus |
| CONS-014 | Conservar proxy con reporte de aplicabilidad; cambiar contrato a estados no aplicables y secuencias de tools | Definir contrato y rúbrica antes de alterar métricas que califican | comun/evaluadores.py, L10 y rúbrica final |
| CONS-019 | Sustentación A1 asíncrona; recortar 20 min; ampliar jornada | Asíncrona mantiene 180 min; requiere decisión del autor | S3/S4, cronograma y guiones |
| CONS-020 | Unificar niveles; mantener equivalencia ordinal documentada | Confirmar vocabulario institucional; conservar pesos | Tres rúbricas y plan curricular |

## Fuentes técnicas contrastadas

- [LangChain: modelos y Structured Output](https://docs.langchain.com/oss/python/langchain/models).
- [LangChain: Middleware](https://docs.langchain.com/oss/python/langchain/middleware/overview).
- [LangChain: Human-in-the-loop](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop).
- [Hugging Face: Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker).

La fuente principal para límites implementados es el código local citado en cada hallazgo.
