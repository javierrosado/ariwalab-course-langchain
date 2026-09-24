# Roadmap de construcción del curso

> Checklist maestro. Marca cada casilla al completar el paso.
> Estado a **2026-09-10**. Actualizar este archivo es parte de cada entrega.
> Última actualización: Fase 2C — mitigación de los riesgos técnicos altos R10 y R11 —
> más `CLAUDE.md` para que una sesión de Claude Code arranque con todo el contexto.
>
> Leyenda: ✅ hecho · ⬜ pendiente · ⏸️ bloqueado por un tercero · 🔁 recurrente

---

## Resumen de avance

| Fase | Bloque | Estado | Entregables |
|------|--------|--------|-------------|
| 0 | Diseño curricular | ✅ **100 %** | 9 documentos |
| 1 | Cimientos técnicos | ✅ **100 %** | 6 módulos + 32 datasets + 24 tools |
| 2 | Nivelación (Sesión 0) | ✅ **100 %** | 11 archivos |
| 2B | **Simulador de industria** | ✅ **100 %** | 20 archivos |
| 2C | **Mitigación de riesgos técnicos** | ✅ **100 %** | 4 archivos |
| 3 | Módulo 1 · sesiones 1-3 | ✅ **100 %** | 27+ archivos (incluye `recursos/rubricas/rubrica-a1.md` y `docente/verificar_ejercicio_pydantic.py`) |
| 4 | Módulo 2 · sesiones 4-7 | ✅ **100 %** (S7 ampliada 2026-09-16 con `code/`+`solucion/`) | 129 archivos en `modulo-2-agentes-avanzados/` + `recursos/golden/` (4) + `recursos/ataques/` (4) + `recursos/rubricas/rubrica-m2.md` + `docente/verificar_guardrails.py` |
| 5 | Módulo 3 · sesiones 8-11 | ✅ **100 %** | 66 archivos en `modulo-3-produccion/` + `recursos/rubricas/rubrica-final.md` + `comun/evaluadores.py` + `docente/verificar_despliegue.py` + `docente/generar_trafico.py` |
| 6 | Seminario Internacional | ✅ **100 %** | 5 archivos en `modulo-3-produccion/seminario-internacional/` |
| 7 | Bonus Foundry | ✅ **100 %** | 6 archivos en `modulo-4-plus-foundry/` |
| 8 | Materiales del docente | ✅ **100 %** (7/9 archivos; 2 se consolidaron en `rubrica-final.md`, ver D29) | `guia-docente.md` + `banco-preguntas.md` + `checklist-pre-sesion.md` + `recursos/plantillas/` (2) + `docente/presentaciones/` (14) |
| — | Verificación del stack | ✅ | `Qwen3-32B` verificado 2026-09-10 |

> **Corrección de numeración (2026-09-16).** Esta tabla decía "Fase 6 · Bonus Foundry" y
> "Fase 7 · Materiales del docente", pero `docente/esqueletos/README.md` (el índice pactado)
> siempre mapeó `seminario.md` → Fase 6 y `bonus-foundry.md` → Fase 7. Contradicción entre este
> archivo y el esqueleto: **gana el esqueleto** (regla explícita del propio índice). Se corrige
> aquí insertando el Seminario como Fase 6 y recorriendo Bonus Foundry → 7 y Materiales del
> docente → 8.

```
    FASE 0 ✅   FASE 1 ✅   FASE 2 ✅   FASE 3 ✅   FASE 4 ✅   FASE 5 ✅   FASE 6 ✅    FASE 7 ✅
    ─────────  ─────────  ─────────  ─────────  ─────────  ─────────  ──────────  ─────────
    diseño     cimientos  Sesión 0   Mód. 1     Mód. 2     Mód. 3     Seminario   Foundry
    plan·ADR   comun/ ·   glosario   S1-S3      S4-S7      S8-S11     Internac.   bonus
    mapeo      datos/tools nivelac.  L1-L3      L4-L7      L8-L11                L12
                                        │          │          │          │          │
                                        └──────────┴────┬─────┴──────────┴──────────┘
                                                        │
                                        FASE 8 ✅ materiales del docente
                                        rúbricas · guía · presentaciones
```

**El curso completo (Fases 0-8) está construido.** Lo que queda pendiente son las tareas de
Javier señaladas a lo largo de este archivo (infraestructura desplegada, cuotas verificadas,
convocatorias) — no contenido por escribir.

---

## FASE 0 · Diseño curricular ✅

- [x] Analizar el repo `microsoft/langchain-for-beginners` y persistir el contexto
- [x] Mapear el syllabus del PDF contra el repo, con gaps y adiciones
- [x] Definir prerrequisitos técnicos por sesión
- [x] Diseñar la malla de 11 sesiones con balance 40/60 sobre 72 h
- [x] Definir los 4 casos de uso peruanos y sus tracks
- [x] Definir la cadena de laboratorios incrementales L1 → L12
- [x] Registrar 21 decisiones de diseño y 13 riesgos (ADR)
- [x] Evaluar el impacto de los LLM personalizados por industria
- [x] Especificar los 4 modelos para el profesor
- [x] Calibrar todo el diseño para un modelo de 7B (reglas A1-A6)

---

## FASE 1 · Cimientos técnicos ✅

- [x] `comun/settings.py` — configuración central, un solo lugar que lee el `.env`
- [x] `comun/provider.py` — `get_chat_model()` conmutable HF ↔ Foundry, modelo por track
- [x] `comun/vectorstore.py` — Qdrant Cloud, backend único
- [x] `comun/observability.py` — callback de Langfuse, compatible v2 y v3
- [x] `comun/datos.py` — capa de acceso a los datasets
- [x] `comun/check_stack.py` — verificador de 8 comprobaciones
- [x] 32 archivos de datasets sintéticos en 4 tracks, con marcas ficticias
- [x] `recursos/datasets/generar_datasets.py` — regeneración con semilla fija
- [x] `recursos/datasets/verificar_datasets.py` — 22 comprobaciones, sale con código 1 si falla
- [x] 24 tools (4 núcleo + 2 opcionales × 4 tracks) con schemas Pydantic
- [x] `docente/verificar_tools.py` — 4 comprobaciones × 24 tools, sin credenciales
- [x] `docente/especificacion-tools.md` — generado por introspección del código

---

## FASE 2 · Nivelación · Sesión 0 ✅

> Asíncrona y obligatoria. Es la respuesta al punto 3 del encargo: ingenieros de
> software con poco conocimiento de LLMs. Sin esto, la sesión 1 no funciona.

- [x] **2.1** `recursos/glosario.md` — 40 términos en español, con analogía y ejemplo
- [x] **2.2** `00-preparacion/README.md` — guía de la sesión 0 y ruta de estudio
- [x] **2.3** `00-preparacion/conceptos-previos/fundamentos-llm.md` — token, contexto, temperatura, embedding, alucinación, costo
- [x] **2.4** `00-preparacion/conceptos-previos/alta-de-cuentas.md` — HF, Qdrant y Langfuse paso a paso, con capturas
- [x] **2.5** `00-preparacion/conceptos-previos/python-y-entorno.md` — venv, `.env`, secretos, Pydantic v2
- [x] **2.6** `00-preparacion/code/` — 4 demos ejecutables: tokenización, temperatura, embeddings, costo
- [x] **2.7** `00-preparacion/autoevaluacion.md` — 10 preguntas, umbral 80 % para entrar a la S1

---

## FASE 2B · Simulador de industria ✅

> Infraestructura del curso, no contenido del alumno. Simula cuatro empresas peruanas
> ficticias y expone el mismo dominio por REST, SQL y MCP. Es la base contra la cual
> corren los laboratorios desde el L3.

- [x] **2B.1** `simulador-industria/db.py` — carga los CSV en SQLite, aísla escrituras por equipo
- [x] **2B.2** `simulador-industria/auth.py` — `X-API-Key` por equipo, 401 explicativo
- [x] **2B.3** `simulador-industria/chaos.py` — 6 fallos provocables + `CHAOS_RATE`
- [x] **2B.4** `simulador-industria/routers.py` — 18 rutas REST de las 4 industrias
- [x] **2B.5** `simulador-industria/app.py` — FastAPI, monta routers y MCP HTTP
- [x] **2B.6** `simulador-industria/mcp_server.py` — 6 tools MCP, transportes stdio y HTTP
- [x] **2B.7** `simulador-industria/Dockerfile` — imagen para HF Spaces
- [x] **2B.8** `simulador-industria/equipos.json` — mapa de API keys
- [x] **2B.9** `simulador-industria/verificar_simulador.py` — 33 comprobaciones, sin credenciales
- [x] **2B.10** `simulador-industria/README.md` — documentación completa
- [x] **2B.11** `comun/api_client.py` — cliente HTTP y traducción de errores
- [x] **2B.12** `comun/datos.py` — conmutador `DATA_SOURCE=csv|api`
- [x] **2B.13** `comun/settings.py` — variables del simulador y de MCP
- [x] **2B.20** `comun/prompts_industria.py` — system prompt de 5 bloques por industria (D26)
- [x] **2B.14** `docs/REFERENCIA-API.md` — 18 rutas con peticiones y respuestas reales
- [x] **2B.15** `docs/GUIA-ALUMNO.md` — conectar el agente, manejo de errores, provocar fallos
- [x] **2B.16** `docs/GUIA-DOCENTE.md` — despliegue, API keys, operación en clase, diagnóstico
- [x] **2B.17** `docs/GUIA-MCP.md` — transportes stdio y HTTP con código de conexión
- [x] **2B.18** `generar_referencia_api.py` — regenera la referencia desde el código en ejecución
- [ ] **2B.19** ⏸️ Desplegar el Space y repartir las API keys — **lo hace Javier**. Vencimiento
      fijado en `docente/esqueletos/sesion-03.md` §2: **lunes de la semana 2**. Bloquea la S3
      (Assignment A1) y, con ella, la nota del Módulo 1

---

## FASE 2C · Mitigación de riesgos técnicos ✅

> Cierra los dos riesgos altos que no dependían de credenciales ni de terceros.
> Ambos convierten una regla escrita en un archivo ejecutable: una regla que nadie puede
> comprobar no es una regla, es una intención.

- [x] **2C.1** `comun/structured.py` — la regla **A3** como código: valida contra el esquema,
      reintenta una vez con el error concreto y falla con `ExtraccionFallida` en vez de propagar
      un `None`. Expone `extraer()` y `extraer_con_detalle()` *(cierra **R10**)*
- [x] **2C.2** `docente/verificar_structured.py` — 36 comprobaciones con modelo simulado:
      camino feliz, reintento, presupuesto de reintentos, few-shot y fallo definitivo.
      Sin red ni credenciales
- [x] **2C.3** `docente/matriz_seleccion.py` — la regla **A1** como número: 20 consultas por
      track (12 directas, 4 confusables, 4 que **no** deben llamar a ninguna tool), matriz de
      confusión, umbral 85 %, y un diagnóstico que dice qué docstring corregir. Modo `--simular`
      para probar el arnés sin gastar cuota *(cierra **R11**)*
- [x] **2C.4** `CLAUDE.md` — contexto de arranque para sesiones de Claude Code: regla #0 de
      Javier, restricciones P1-P6, decisiones que no se renegocian, índice de `_memoria/` y
      comandos de verificación

---

## FASE 3 · Módulo 1 · sesiones 1-3 ✅

> Cada sesión sigue la misma estructura de 5 piezas. Multiplicar los labs por 4 tracks.

> **Flujo de trabajo de esta fase (2026-09-15):** el *esqueleto* de cada sesión se pacta en
> Cowork y se guarda en `docente/esqueletos/`; los archivos de la sesión se escriben y se
> ejecutan en Claude Code, tomando ese esqueleto como contrato.

- [x] **3.0** `docente/esqueletos/sesion-01.md` — contrato de la S1: guion de 180 min, alcance
      del L1 (entorno + primer script), 3 demos, Test 1, regla de elección de track y la lista
      de lo que **no** entra

### Sesión 1 — Fundamentos de los agentes inteligentes ✅
- [x] **3.1** `README.md` — teoría: agente vs LLM, percepción → razonamiento → acción, anatomía de LangChain
- [x] **3.2** `conceptos-previos.md` — 4 conceptos del pre-work + Test 1 (10 preguntas comentadas)
- [x] **3.3** `code/` — 3 demos: primer llamado, tipos de mensaje, **un modelo · cuatro industrias**
      (no "comparación de modelos": con D28 el curso usa un solo modelo, ver `docente/esqueletos/README.md` tarea e)
- [x] **3.4** `lab/` — enunciado L1 en los 4 tracks
- [x] **3.5** `solucion/` — checkpoint L1 (`primer_contacto.py`) en los 4 tracks

### Sesión 2 — Ecosistema LangChain: prompts, cadenas y modelos ✅
- [x] **3.6** `README.md` — mensajes y roles, Rol+Contexto+Tarea+Formato, few-shot (A5), la demo
      del fallo y `comun/structured.py` (A3)
- [x] **3.7** `conceptos-previos.md` — 5 conceptos del pre-work + pase de entrada de Pydantic + Test 2
- [x] **3.8** `code/` — 4 demos: plantilla de dominio, few-shot (0/2/4), structured crudo vs
      robusto, tokens y costo
- [x] **3.9** `lab/` — enunciado L2 (clasificador de intención, taxonomía 1:1 con el L4) en los 4 tracks
- [x] **3.10** `solucion/` — `schemas.py`, `prompts.py`, `clasificar.py` (usa `extraer()`,
      prohibido `with_structured_output()` directo), `medir_clasificador.py`, en los 4 tracks

**Trabajo previo de la S2 completado en el mismo tramo:** `recursos/golden/consultas-<track>.json`
ampliado con los campos `intencion` (taxonomía) y `tool_esperada` (tool del L4);
`docente/matriz_seleccion.py` y `.../sesion-04.../02_matriz_didactica.py` actualizados para leer
`tool_esperada`; `docente/verificar_ejercicio_pydantic.py` (nuevo, probado con un caso válido y
uno inválido); taxonomía de telco corregida en `docente/labs-incrementales.md`.

### Sesión 3 — Herramientas, integración externa y Assignment A1 ✅
- [x] **3.11** `README.md` — function calling, el LLM genera / tu código ejecuta, la docstring
      como prompt (A2), errores redactados para el modelo (A4), del bucle manual a `create_agent()`
- [x] **3.12** `conceptos-previos.md` — 6 conceptos del pre-work + verificación con `salud()`
- [x] **3.13** `code/` — 4 demos: tool simple, binding (la demo de la sesión), bucle ReAct
      manual, `create_agent()` — las 4 verificadas en vivo contra el modelo real
- [x] **3.14** `lab/` — enunciado L3 (primera tool de lectura, con identificadores reales de los
      datasets) en los 4 tracks + plantilla de `EVIDENCIA-A1.md`
- [x] **3.15** `solucion/` — `external_api.py`, `agent.py` v1, `prueba_tool.py` en los 4 tracks,
      con los 3 escenarios verificados (el 3.º queda documentado como pendiente del simulador
      real, ver bloqueador 2B.19)
- [x] **3.16** `assignment-a1.md` — enunciado, entregables, rúbrica 4×5, regla del piso y calendario

**Trabajo previo de la S3 completado en el mismo tramo:** `recursos/rubricas/rubrica-a1.md`
(nuevo, con la nota de que observabilidad no aplica antes de la S9); fecha de **2B.19** fijada a
lunes de la semana 2 (ver bloqueador más abajo); `domain_tools.py` del L4 (Sesión 4) confirmado
como continuación literal de `external_api.py` de esta sesión, no un archivo nuevo.

---

## FASE 4 · Módulo 2 · sesiones 4-7 ✅

> Construida siguiendo `docente/esqueletos/sesion-04.md` a `sesion-07.md` (2026-09-16), que en
> varios puntos afinó o corrigió lo que este checklist proyectaba antes de pactarse el esqueleto
> — manda el esqueleto, y las descripciones de abajo ya reflejan lo que de verdad se construyó.
> Tareas previas **i-s** de `docente/esqueletos/README.md` ejecutadas en el mismo tramo de trabajo
> (`docente/matriz_seleccion.py --tools`, corrección del pre-work de MCP, `recursos/golden/`,
> `docente/verificar_guardrails.py`, `recursos/ataques/`, `recursos/rubricas/rubrica-m2.md`,
> plantillas de L7, nota de `CHAOS_RATE` en `docente/cronograma.md`).

### Sesión 4 — Tools e integración de herramientas ✅
- [x] **4.1** `README.md` — catálogo de tools, selección dinámica, **por qué 4 tools y no 6**
      (fiabilidad compuesta, D20), diagrama de los 3 tipos de confusión, tabla de idempotencia, y
      la aclaración de `proyecto-final/`
- [x] **4.2** `conceptos-previos.md` — ReAct, async, límite de iteraciones
- [x] **4.3** `code/` — 3 demos: multi-tool, matriz de selección (didáctica), tope de iteraciones
- [x] **4.4** `pre-work-mcp.md` — MCP: conectarse al servidor del simulador, no construir uno propio
- [x] **4.5** `lab/` + `solucion/` — L4 (4 tools del dominio, una de escritura con confirmación) en
      los 4 tracks, medido con `docente/matriz_seleccion.py --tools`

### Sesión 5 — Memoria contextual y RAG ✅
- [x] **4.6** `README.md` — embeddings, chunking, RAG tradicional vs agéntico, Qdrant, salvaguarda A6
- [x] **4.7** `conceptos-previos.md` — similitud coseno, chunking, vocabulario de Qdrant, pase de entrada
- [x] **4.8** `code/` — 4 demos: ingesta, similitud, RAG tradicional, RAG agéntico
- [x] **4.9** `code/demo-parametrico-vs-recuperable.py` — **la demo clave**, con guion para el docente
- [x] **4.10** `lab/` + `solucion/` — L5 (`knowledge/ingest.py`, `knowledge/retriever.py`,
      `memory.py`, `agent.py` v3) en los 4 tracks. ⏸️ **Indexación real de las 4 colecciones de
      respaldo `kb-<track>-respaldo` pendiente**: el `QDRANT_URL` del `.env` no resuelve por DNS
      (cluster probablemente borrado o recreado) — ver nota en `_memoria/DECISIONES.md` bajo D10

### Sesión 6 — Automatización, asistentes y guardrails ✅
- [x] **4.11** `README.md` — middleware, prompt injection, PII y Ley 29733, escalamiento, límites por industria
- [x] **4.12** `conceptos-previos.md` — inyección, PII, Ley 29733, entrada vs salida
- [x] **4.13** `code/` — 4 demos: guardrail de entrada, de acción, de salida, middleware
- [x] **4.14** `lab/` + `solucion/` — L6 (`guardrails.py`, `agent.py` v4) en los 4 tracks, con su
      lista de prohibidos. Verificado en vivo contra el modelo real: telecomunicaciones, 0/15 filtraciones
- [x] **4.15** `recursos/ataques/bateria-<track>.json` — los 15 ataques × 4 tracks (5 inyección +
      3 exfiltración PII + 3 acción prohibida + 2 fuera de dominio + 2 presión/urgencia)

### Sesión 7 — Hackathon y Proyecto M2 ✅
- [x] **4.16** `README.md` — cómo se prueba lo no determinístico: invariantes, familias de caso
      borde, la clínica y la aritmética de la ronda de demos
- [x] **4.17** `conceptos-previos.md` — testing no determinístico + los 6 fallos del simulador
- [x] **4.18** `lab/` — guion de la clínica por track + plantillas de `INFORME-L7.md` y del
      documento de diseño
- [x] **4.19** `proyecto-m2.md` — enunciado, entregables, rúbrica 4×5 (`recursos/rubricas/rubrica-m2.md`),
      regla del piso y calendario
- [x] **4.20** `code/` — 3 demos añadidas el 2026-09-16 (no estaban en `sesion-07.md` original,
      se completó la sesión a pedido): por qué falla `assert ==`, invariantes en aislamiento,
      repetir y medir + `README.md`
- [x] **4.21** `solucion/` — añadido el 2026-09-16: `tests/invariantes.py` +
      `tests/test_casos_borde.py` en los 4 tracks, con las 4 familias del bloque 0 medidas por
      repetición e invariantes (no `assert ==`). Verificado por import y por lógica aislada
      (parcheo de `comun.datos.buscar_uno`); la corrida en vivo de punta a punta quedó bloqueada
      por un incidente del proveedor de HF (ver nota más abajo)
- [x] **4.22** Hallazgos H1-H5 de `docente/esqueletos/VALIDACION-INTEGRAL.md`, corregidos el
      2026-09-16 sin reabrir el guion de 180 min (verificado con `validar_coherencia.py`):
      - **H1** (few-shot de A5 sin aplicar) — añadida la sección 2.1 al `README.md` de S4 y un
        párrafo al bloque 1 del `README.md` de S6
      - **H2** (A4 sin medir) — nota de corrección en `sesion-07.md` + docstrings de
        `tests/test_casos_borde.py` explicando cómo esos tests miden el tope de iteraciones
      - **H3** (streaming prometido, nunca enseñado) — se resuelve en la S11 con
        `code/web/index.html` (streaming real), no antes
      - **H4** (LangGraph desaparece) — añadido el párrafo "¿Y LangGraph?" al bloque 4 del
        `README.md` de S6
      - **H5** (S4 no nombra el archivo golden) — añadido el párrafo "de dónde salen las 30
        consultas" a la sección 2 del `README.md` de S4
      - **H6** (descuadre de 20 min en S4) queda **fuera de esta lista a propósito**: es
        DECISION-PENDIENTE de Javier, no un hallazgo para que Code corrija solo
- [x] **4.23** `recursos/golden/consultas-<track>.json` ampliado de 26 a **30 consultas/track**
      (20 con tool + 10 otro, según exige `sesion-10.md`) y con el campo `respuesta_esperada`
      añadido a las 30 filas de los 4 tracks. Referencias cruzadas a "26"/"104" corregidas en
      10 archivos. Verificado: `matriz_seleccion.py --simular` → 100 % global
- [x] **4.24** Hallazgo H7 de `VALIDACION-INTEGRAL.md` (2026-09-17): `comun/structured.py`
      (regla A3) se usaba solo en el L2. Cerrado:
      - `sesion-10-evaluacion-optimizacion/code/03_llm_as_judge.py` — el juez ahora responde con
        un esquema `Veredicto` (`aprueba: bool`, `motivo: str`, `confianza: Enum`) extraído con
        `extraer()`, en vez de texto libre parseado a mano
      - `domain_tools.py` de telecomunicaciones, retail y seguros (L4) — la tool de escritura de
        cada track normaliza su enum con `extraer()` antes de pedir confirmación
      - `domain_tools.py` de banca — nota explícita de por qué no aplica (el track no tiene tool
        de escritura en su núcleo)
      - Verificado con pruebas funcionales (modelo simulado) para los 3 tracks afectados y
        `docente/matriz_seleccion.py --simular` (100 % global, sin regresión)

---

## FASE 5 · Módulo 3 · sesiones 8-11 ✅

### Sesión 8 — Despliegue en HF Spaces ✅
- [x] **5.1** `README.md` — 12-Factor, contenedores, protocolo de despliegue, diagrama de qué
      va autenticado
- [x] **5.2** `conceptos-previos.md` — Dockerfile, FastAPI, secretos en la nube
- [x] **5.3** `code/` — 4 demos (api local, Dockerfile comentado, secretos, llamar desde
      fuera) + `README.md`. `docente/verificar_despliegue.py` y `docente/generar_trafico.py`
      añadidos como infraestructura compartida (tareas v/y de `sesion-08.md`/`sesion-09.md`)
- [x] **5.4** `lab/` + `solucion/` — L8 en los 4 tracks (`api.py`, `Dockerfile`,
      `DESPLIEGUE.md` y `avance-1-m3.md` como plantillas — sin datos reales porque no hay un
      Space desplegado desde esta sesión de Code; ver bloqueador abajo)
- [ ] **5.5** ⏸️ Despliegue real del Space de referencia del docente (tarea u de
      `sesion-08.md`) y verificación de los límites del free tier de HF Spaces (tarea t,
      riesgo R5) — **son tareas de Javier**, no de Code (P2: nada corre ni se despliega
      desde aquí sin credenciales de infraestructura que Code no tiene)

> **Nota de numeración:** este bloque ya no tiene una entrega `guia-hf-spaces.md` separada
> —el paso a paso de despliegue quedó integrado en `lab/README.md` parte 3, siguiendo el
> guion de `sesion-08.md` §8, que no pide un archivo aparte.

### Sesión 9 — Observabilidad con Langfuse ✅
- [x] **5.6** `README.md` — logs vs métricas vs trazas, span, latencia p50/p95, costo,
      decisión de enmascarar PII antes de exportar
- [x] **5.7** `conceptos-previos.md` — traza distribuida, OpenTelemetry, PII en trazas
- [x] **5.8** `code/` — 3 demos (traza mínima, anatomía de spans, PII con y sin
      enmascarar) + `README.md`
- [x] **5.9** `lab/` + `solucion/` — L9 en los 4 tracks (`observability.py`, `agent.py` v5
      con `config={"callbacks": ...}` en cada invoke, `INFORME-L9.md` como plantilla).
      La corrida en vivo contra un Space real y la lectura del dashboard de Langfuse quedan
      pendientes de infraestructura desplegada (depende de la S8, ⏸️ arriba)

### Sesión 10 — Evaluación y optimización ✅
- [x] **5.10** `README.md` — golden dataset (espina dorsal del curso), evaluators,
      groundedness, LLM-as-judge y sus 4 sesgos
- [x] **5.11** `conceptos-previos.md` — precisión/recall, prueba A/B, regresión
- [x] **5.12** El golden dataset **ya vive** en `recursos/golden/consultas-<track>.json`
      (30 casos/track, ampliado en la tarea 4.23) — no se duplica en un `.jsonl` aparte,
      siguiendo la decisión explícita de `sesion-10.md` §2 ("no se construye nada nuevo")
- [x] **5.13** `code/` — 4 demos (dataset en Langfuse, evaluators, LLM-as-judge, A/B de
      prompts) + `README.md`. `comun/evaluadores.py` añadido como infraestructura
      compartida (tarea ab)
- [x] **5.14** `lab/` + `solucion/` — L10 en los 4 tracks (`evals/dataset.py`,
      `evals/evaluadores.py`, `INFORME-L10.md` y `avance-3-m3.md` como plantillas)

### Sesión 11 — Aplicación final y sustentación ✅
- [x] **5.15** `README.md` — cierre e integración, cómo se argumenta ante un panel, regla de
      contingencia si el Space cae
- [x] **5.16** `code/index.html` — cliente HTML de referencia con streaming (SSE vía `fetch()` +
      `ReadableStream`, no `EventSource`) + `code/README.md`
- [x] **5.17** `lab/plantilla-documento-diseno.md` — las 4 secciones (caso de uso, arquitectura,
      decisiones, evidencia)
- [x] **5.18** `proyecto-integrador.md` — enunciado, entregables, calendario, y
      `recursos/rubricas/rubrica-final.md` (tarea ad) con los 5 criterios institucionales
      completos. `checklist-panel.md` (tarea af) añadido para uso del panel el día de la demo.
      `lab/` + `solucion/` — L11 en los 4 tracks (`agent.py` v6 con `responder_streaming()`,
      `api.py` con `/chat/stream`, `web/index.html`)

> **Nota de diseño (streaming vs. guardrails):** `responder_streaming()` no transmite tokens en
> vivo del modelo — resuelve el bucle completo, corre `guardrails.check_output()` sobre el texto
> íntegro, y solo transmite el resultado ya validado, palabra por palabra. Se documenta como
> decisión deliberada en el docstring de `agent.py` de cada track: un guardrail de salida que
> evalúa texto completo y un streaming de tokens en vivo no son compatibles sin un rediseño más
> profundo (guardrails incrementales por fragmento), fuera de alcance de este curso.

---

## FASE 6 · Seminario Internacional ✅

> Panel de casos reales, formativo, no ponderado. `docente/esqueletos/seminario.md`. Carpeta:
> `modulo-3-produccion/seminario-internacional/`. Las tareas de convocatoria, brief a
> panelistas, confirmación de asistencia y curaduría de preguntas (**ai-aj-ak-al**) son de
> Javier, con fecha — ver `guion-docente.md`; aquí solo van los documentos que Code produce.

- [x] **6.1** `README.md` — formato del panel, objetivos, cuadro "anotar vs. ignorar", los 3
      mecanismos contra el silencio y el discurso comercial
- [x] **6.2** `preparacion.md` — la plantilla de pregunta + un ejemplo real por track
- [x] **6.3** `plantilla-contraste.md` — las 4 secciones del documento de contraste
- [x] **6.4** `brief-panelistas.md` — el brief de 1 página que Javier envía a los panelistas
- [x] **6.5** `guion-docente.md` — guion del moderador, tiempos, curaduría de preguntas, riesgos
      y el Plan B si solo llega 1 panelista

---

## FASE 7 · Bonus Foundry ✅

> Asíncrono, opcional, no ponderado. Se libera al cerrar la S11. Carpeta:
> `modulo-4-plus-foundry/`. Las tareas am/an/ao/ap (re-verificar `langchain-azure-ai[hosting]`
> contra un proyecto real, desplegar el proyecto compartido de la vía B, capturas del portal,
> fecha de cierre del bonus) son de Javier — ver la nota ⏸️ en `acceso-azure.md`.

- [x] **7.1** `README.md` — hosted agent, protocolo Responses, modelo de recursos de Azure, los
      8 pasos, advertencia de la tarjeta en la primera línea
- [x] **7.2** `acceso-azure.md` — las dos vías (A: suscripción propia, B: proyecto del docente),
      paso a paso. ⏸️ Capturas del portal pendientes (tarea ao, Javier)
- [x] **7.3** `host/main.py` — wrapper `ResponsesHostServer` sobre `comun.provider.get_chat_model()`
      + las tools del L4/L5, con nota explícita de qué NO porta sin cambios (guardrails del L6).
      Verificado por import y compilación; **no verificado en vivo contra un proyecto Foundry
      real** — `langchain-azure-ai[hosting]` está en preview (riesgo R8) y esa verificación es
      la tarea am, de Javier
- [x] **7.4** `host/azure.yaml` — configuración de despliegue, adaptada del ejemplo oficial de
      `langchain-azure` (`samples/hosting/langgraph-hosted-agents/responses/10_resilient`)
- [x] **7.5** `puente-curso-2.md` — qué mueve este bonus vs. qué mueve el Curso 2, y por qué
- [x] **7.6** `plantilla-comparativa.md` — las 7 dimensiones, con cómo medir cada una (sin
      cifras de precio fijas, que caducan)

> **Nota de numeración:** el `ROADMAP.md` original preveía `code/main.py`/`code/azure.yaml` y
> una `guia-despliegue-azd.md` separada; el esqueleto pactado (`bonus-foundry.md` §10) los
> agrupa como `host/main.py` + `host/azure.yaml`, con la guía de despliegue integrada en el
> `README.md` §"Pasos 5-7" en vez de un archivo aparte — se siguió el esqueleto por ser la
> fuente pactada más reciente.

---

## FASE 8 · Materiales del docente ✅

- [x] **8.1** `recursos/rubricas/rubrica-a1.md` — 5 criterios × 4 niveles (construida en Fase 3, S3)
- [x] **8.2** `recursos/rubricas/rubrica-m2.md` (construida en Fase 4, S7)
- [x] **8.3** ~~`recursos/rubricas/rubrica-m3.md`~~ — **consolidada en `rubrica-final.md`**
      (Fase 5, S11): el proyecto de cierre del M3 y la sustentación ante panel son el mismo
      evento (S11 §2 y §8), así que no hay un "proyecto M3" que calificar aparte de la demo. Ver
      decisión **D29** en `_memoria/DECISIONES.md`
- [x] **8.4** ~~`recursos/rubricas/rubrica-demo.md`~~ — **consolidada en `rubrica-final.md`**,
      cuyo criterio "Comunicación técnica" (15 %) ya cubre la sustentación ante panel. Misma
      decisión D29
- [x] **8.5** `docente/guia-docente.md` — resumen operativo de las 11 sesiones + seminario +
      bonus (ficha, guion condensado, errores esperables), derivado de `docente/esqueletos/`
      sin reinventar contenido; incluye las decisiones pendientes de Javier (descuadre de 20 min
      de la S4, etc.)
- [x] **8.6** `docente/banco-preguntas.md` — índice de los 3 instrumentos que ya existían
      (autoevaluación de la S0, Test 1, Test 2), sin duplicar sus preguntas
- [x] **8.7** `docente/checklist-pre-sesion.md` — deriva de `docente/cronograma.md` §"Puntos de
      control" y de `comun/check_stack.py`; añade los bloqueantes con fecha por sesión y los
      modos degradados por servicio
- [x] **8.8** `recursos/plantillas/` — `plantilla-proyecto-final.md` (nueva: estructura y
      `README.md` inicial para el repositorio de cada equipo) + `plantilla-documento-diseno.md`
      (movida desde `modulo-3-produccion/sesion-11-.../lab/`, que la citaba como archivo propio
      de esa sesión sin serlo — ahora vive junto a las demás plantillas compartidas)
- [x] **8.9** `docente/presentaciones/` — esqueleto de diapositivas en Markdown, una por sesión
      (13 archivos + índice), decidido con el usuario: sin herramienta específica, listo para
      pegar en Google Slides, PowerPoint, Marp o reveal.js

---

## Verificaciones transversales 🔁

Ejecutar antes de cerrar cada fase:

- [ ] 🔁 `python recursos/datasets/verificar_datasets.py` — integridad y marcas
- [ ] 🔁 `python docente/verificar_tools.py` — 24 tools contra datos reales
- [ ] 🔁 `python docente/generar_especificacion_tools.py` — regenerar la spec si cambian tools
- [ ] 🔁 Revisar que ningún lab supere 4 tools núcleo (regla A1)
- [ ] 🔁 Revisar que toda docstring nueva diga "cuándo NO" (regla A2)

---

## Bloqueadores externos ⏸️

| # | Bloqueador | Responsable | Bloquea | Alternativa mientras tanto |
|---|-----------|-------------|---------|---------------------------|
| ~~B1~~ | ~~Ejecutar `check_stack` contra endpoints reales~~ | — | ✅ **Resuelto 2026-09-10** | `Qwen3-32B` verificado: 1 de 4 candidatos pasó (D28) |
| ~~B2~~ | ~~Decisión camino A o B~~ | — | **Resuelto** | Camino A decidido el 2026-09-10 (D21) |
| ~~B3~~ | ~~Endpoints de los 4 modelos por industria~~ | — | **Disuelto** | Con camino A hay un solo modelo base, sin endpoints custom |
| B4 | Aprobación de rúbricas por la universidad | **Universidad** | Fase 7 | Se usa el esquema del PDF |
| B5 | Desplegar el simulador en HF Spaces y repartir API keys | **Javier** | Los labs L3+ en clase | El simulador corre en local con `uvicorn` |
| B6 | **`QDRANT_URL` del `.env` no resuelve por DNS** (cluster probablemente borrado o recreado con otro id) | **Javier** | Indexar las 4 colecciones de respaldo `kb-<track>-respaldo` (tarea l) y correr en vivo `code/01_ingesta.py` y siguientes de la S5 | `knowledge/ingest.py` ya está escrito (S5, los 4 tracks) y probado en su lógica; falta un cluster real para correr la indexación |
| B7 | Cuota mensual de HF Inference agotada a mitad de una corrida de `check_stack` (`402`) | **Javier** | Verificaciones en vivo extensas (matriz de selección o guardrails sobre los 4 tracks completos) | Usar `--simular` en `matriz_seleccion.py` y `verificar_guardrails.py` mientras se repone la cuota; ya se verificó en vivo 1 track de cada instrumento antes de que se agotara |

> **Nota 2026-09-16:** al verificar el stack para la Fase 4, `.env` tenía `HF_CHAT_MODEL` y
> `HF_EMBEDDING_MODEL` invertidos (`Qwen/Qwen3-30B-A3B` —un candidato que D28 dice que falló— como
> modelo de chat, y `Qwen/Qwen3-32B` como embedding). Se corrigió a los valores documentados
> (D28/D15); `check_stack --solo-modelo` pasa las 6 comprobaciones desde entonces.

**Ninguno bloquea la generación de contenido.** Esa fue la razón de la decisión D13: el código
del agente no conoce a su proveedor, así que el material se escribe sin depender del modelo final.

---

## Orden de ejecución recomendado

```
  1. FASE 2  ──►  glosario y nivelación         ✅ COMPLETADA
  2. FASE 3  ──►  Módulo 1 completo              ✅ COMPLETADA (Sesiones 1-3, cerrada 2026-09-16)
        │
        └──► PUNTO DE REVISIÓN: Javier valida tono, profundidad y formato    ⬜ PENDIENTE
                    │
  3. FASE 4  ──►  Módulo 2                       ✅ COMPLETADA (Sesiones 4-7)
  4. FASE 5  ──►  Módulo 3                       ✅ COMPLETADA (Sesiones 8-11)
  5. FASE 6  ──►  Seminario Internacional        ✅ COMPLETADA
  6. FASE 7  ──►  Bonus Foundry                  ✅ COMPLETADA
  7. FASE 8  ──►  Materiales del docente         ✅ COMPLETADA
```

> **Nota de secuencia (2026-09-16):** la Fase 4 se construyó antes de que la Fase 3 estuviera
> completa (por encargo directo), así que el **punto de revisión** que este documento pedía tras
> cerrar la Fase 3 quedó atrasado. Con la Fase 3 ya cerrada, **este es el momento de hacer esa
> revisión** — de las 7 sesiones ya escritas (114 archivos entre ambas fases), no solo de la
> Sesión 1 — antes de seguir a la Fase 5. Corregir un problema de tono o formato ahora, con 2
> módulos completos, cuesta más que si se hubiera revisado al cierre de cada fase.

El punto de revisión tras la Fase 3 es deliberado: corregir el formato con 27 archivos escritos
cuesta poco; corregirlo con 114 escritos cuesta mucho.

## Revisión de consistencia — 2026-09-24

La construcción de contenido no equivale a validación final para dictado. Consultar
[mapa pedagógico](docs/COURSE-MAP.md), [inventario](docs/COURSE-INVENTORY.md) e
[informe de consistencia](docs/COURSE-CONSISTENCY-REPORT.md). La revisión conserva
los bloqueadores externos y decisiones del autor; no los marca resueltos por ejecutar pruebas offline.
