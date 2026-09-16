# Esqueleto · Sesión 3 — Herramientas, integración externa y Assignment A1

> **Qué es este documento.** El contrato de la sesión 3: qué enseña, en qué orden, qué produce
> el alumno y qué **no** entra. Es el insumo de la sesión de Claude Code que escribe los archivos
> (pasos 3.11–3.16 del `ROADMAP.md`). No es material de alumno.
>
> Decidido con Javier el 2026-09-15 · Fase 3 · Módulo 1

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta destino | `modulo-1-fundamentos/sesion-03-tools-api-externa/` |
| Semana · día | Semana 2 · martes |
| Horas | **2.5 h teoría · 3.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (90 T / 80 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L3 · Primera tool contra el simulador** = **Assignment A1** |
| Evaluación | **Assignment A1 · 100 % del Módulo 1** |
| Estado en el mapeo | `COMPLETA` — repo `04-function-calling-tools` + `05-agents` |

> **Es la sesión más cara del módulo.** Es la primera que toca el simulador, la primera que
> ejerce tool calling de verdad, y su laboratorio **es** la nota del Módulo 1. Todo lo que pueda
> fallar debe estar resuelto antes del martes, no durante.

---

## 2. Bloqueante con fecha

| Qué | Quién | Para cuándo | Si falta |
|---|---|---|---|
| Simulador desplegado en HF Spaces y respondiendo `/health` | **Javier** | Lunes semana 2 | Se dicta con `DATA_SOURCE=csv`: el L3 pierde la API real y el escenario "API caída" deja de ser demostrable |
| **API key por equipo** repartida | **Javier** | Lunes semana 2 | Sin ella no hay L3, y sin L3 no hay A1 |
| `CHAOS_RATE=0.0` confirmado | Javier | Martes, antes de clase | Fallos aleatorios durante la evaluación del módulo |

Es la tarea **2B.19** del `ROADMAP.md`, que hoy está en ⏸️. Deja de ser "pendiente" y pasa a tener
fecha: el martes de la semana 2 es su vencimiento real.

---

## 3. Objetivos de aprendizaje

Al terminar, el alumno puede:

1. Explicar quién **genera** la llamada a la herramienta y quién la **ejecuta** — y por qué esa
   separación es toda la seguridad del sistema.
2. Escribir una docstring que haga que el modelo elija bien: verbo, cuándo usarla, **cuándo NO**.
3. Definir el `args_schema` de una tool con Pydantic.
4. Manejar los 3 escenarios de una integración real: éxito, dato inexistente y servicio caído.
5. Redactar un error **para que lo lea el modelo**, no para que lo lea un humano en un log.
6. Explicar qué hace `create_agent()` por dentro, habiendo visto el bucle escrito a mano.

---

## 4. Con qué llega el alumno

**Pre-work de 1 h** (`conceptos-previos.md`):

| # | Concepto | Por qué antes de la clase |
|---|---|---|
| 1 | **Docstrings** de Python | La docstring de la tool **es el prompt** que lee el modelo |
| 2 | Decoradores | `@tool` es un decorador; sin eso parece magia |
| 3 | REST con `httpx`: GET, headers, códigos de estado | La tool llama a una API real |
| 4 | Parsing de JSON, `KeyError`, timeouts | El PDF lo pide explícitamente |
| 5 | `try/except` con mensajes útiles **al modelo** | Un error mal devuelto rompe el bucle ReAct |
| 6 | La guía del simulador y **su API key de equipo** | Debe llegar con `salud()` respondiendo |

**Verificación de entrada** — 2 minutos, en el pre-work:

```powershell
python -c "from comun.api_client import salud; print(salud())"
```

Quien no obtenga respuesta avisa **antes** del martes. Es el mismo principio del pase de entrada
de Pydantic de la S2: los bloqueos se descubren con margen, no en la sesión que vale la nota.

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | Hoy el modelo deja de saber y empieza a consultar | 5 | T | Recuperar la alucinación de la S1 y anunciar que hoy se acaba |
| 1 | **Function calling: quién genera y quién ejecuta** | 25 | T | El modelo **propone** una llamada en JSON. **Tu código decide** si la ejecuta |
| 2 | **La docstring es el prompt** (regla A2) | 25 | T | Verbo + cuándo usarla + cuándo NO. Reescribir en vivo una docstring mala |
| 3 | **Errores redactados para el modelo** (regla A4) | 20 | T | 404 → `None`; 401 → "reintentar no lo soluciona"; 5xx → "el servicio no responde" |
| 4 | Demo: bucle ReAct manual → `create_agent()` | 15 | T | Las ~20 líneas del bucle, y después las 3 de la abstracción |
| — | **Pausa** | 10 | — | |
| 5 | Práctica guiada: el primer `@tool` contra el simulador | 40 | P | Todos escriben la misma tool del track, en clase, con el docente mirando |
| 6 | Los 3 escenarios con `?_fallo=` | 25 | P | Provocar el 503 y ver qué hace el agente |
| 7 | Rúbrica del A1 y reparto de trabajo | 15 | P | Qué se entrega, cómo se califica, cuándo se sustenta |

**Teoría 90 min · práctica 80 min · pausa 10** → con pre-work y lab: **2.5 h / 3.5 h** ✅

### Bloque 1 — el diagrama central de la sesión

```
   ┌──────────┐   1. pregunta          ┌──────────┐
   │ Usuario  │ ─────────────────────► │  MODELO  │
   └──────────┘                        └────┬─────┘
                                            │ 2. NO ejecuta nada.
                                            │    Propone: {"name": "get_customer_plan",
                                            │               "args": {"numero_linea": "987654321"}}
                                            ▼
                                     ┌─────────────┐
                                     │  TU CÓDIGO  │ 3. decide si la ejecuta,
                                     │             │    valida los argumentos,
                                     └──────┬──────┘    aplica permisos
                                            │ 4. HTTP GET
                                            ▼
                                     ┌─────────────┐
                                     │  SIMULADOR  │
                                     └──────┬──────┘
                                            │ 5. el resultado vuelve como mensaje `tool`
                                            ▼
                                        MODELO redacta la respuesta final
```

> **El paso 3 es toda la seguridad del sistema.** El modelo nunca toca la red, la base de datos
> ni el disco: solo escribe una intención en JSON. Si un atacante lo convence de pedir algo
> indebido, quien decide sigue siendo tu código. Esta idea se retoma entera en la S6 (guardrails).

### Bloque 2 — la docstring mala, reescrita en vivo

```python
# ANTES — el modelo no sabe cuándo usarla
@tool
def get_customer_plan(numero_linea: str) -> str:
    """Obtiene información del cliente."""

# DESPUÉS — regla A2
@tool
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene, si su línea está activa
    o en qué distrito está registrada.

    NO la uses para consultar consumo de datos (usa get_data_usage) ni para
    registrar un reclamo (usa create_complaint_ticket). No sirve para
    preguntas sobre tarifas o precios: eso está en la base de conocimiento.
    """
```

Cerrar el bloque mostrando la salida de `docente/matriz_seleccion.py`: **la calidad de esa
docstring es un número medible**, no una opinión.

### Bloque 3 — cómo se redacta un error para el modelo

| Situación | ❌ Para un humano | ✅ Para el modelo |
|---|---|---|
| 404 | `raise KeyError("not found")` | `"No existe una línea con el número 999999999 en AndesMóvil. Verifica el número con el cliente."` |
| 401 | `raise HTTPError(401)` | `"Credencial rechazada (401). Reintentar no soluciona un 401."` |
| 503 | traceback completo | `"El servicio de AndesMóvil no responde en este momento. Informa al cliente y ofrece reintentar más tarde."` |

`comun/api_client.py` ya lo hace así. En el lab el alumno escribe el `try/except` de **su** tool
con ese mismo criterio — no lo copia, lo reproduce.

---

## 6. Las 4 demos · `code/`

| Archivo | Qué demuestra | Qué debe notar el alumno |
|---|---|---|
| `01_tool_simple.py` | `@tool` + `args_schema`, invocada **directamente desde Python** | Que una tool es una función normal: sin modelo de por medio funciona igual |
| `02_binding.py` | `bind_tools()` e imprimir el `tool_call` **sin ejecutarlo** | Que el modelo solo produjo un JSON. Nada pasó todavía |
| `03_bucle_react_manual.py` | El bucle escrito a mano en ~20 líneas, con el tope de iteraciones (A4) | Que el "razonamiento" del agente es un `while` que tú controlas |
| `04_create_agent.py` | Lo mismo en 3 líneas | Que la abstracción no añade inteligencia: quita código repetido |

**La demo 2 es la de la sesión.** Es la que convierte el diagrama del bloque 1 en algo que el
alumno ve con sus ojos: el modelo generó la llamada y no ocurrió nada.

---

## 7. Laboratorio L3 = Assignment A1

### La tool por track

Una sola tool, la primera de las cuatro que el L4 completará. Las cuatro son **de lectura**, sin
efectos secundarios: el alumno puede reintentar cuantas veces quiera sin ensuciar datos.

| Track | Tool | Ruta del simulador | Categoría del L2 que resuelve |
|---|---|---|---|
| telecomunicaciones | `get_customer_plan` | `GET /telco/clientes/{numero_linea}` | `CONSULTA_PLAN` |
| banca | `get_account_balance` | `GET /banca/cuentas/{numero_cuenta}` | `CONSULTA_SALDO` |
| retail | `track_order` | `GET /retail/pedidos/{pedido_id}` | `SEGUIMIENTO_PEDIDO` |
| seguros | `get_policy_by_plate` | `GET /seguros/polizas/{placa}` | `CONSULTA_POLIZA` |

```
   L2   clasifica  CONSULTA_PLAN
   L3   construye  get_customer_plan            ← la tool de esa categoría
   L4   completa   + get_data_usage
                   + run_line_diagnostics
                   + create_complaint_ticket    ← las 4 del catálogo
```

### Los 3 escenarios obligatorios

| # | Escenario | Cómo se provoca | Qué debe hacer el agente |
|---|---|---|---|
| 1 | **Éxito** | Un identificador real del dataset del track | Llamar la tool y responder citando el dato |
| 2 | **Dato inexistente** | Un identificador que no existe → 404 | La tool devuelve "no existe"; el agente **no inventa** ni reintenta |
| 3 | **Servicio caído** | `?_fallo=error503` | El agente avisa al cliente y **no entra en bucle** de reintentos |

**Reto opcional:** `?_fallo=malformado` — 200 con un JSON que no cumple el contrato. Es el más
difícil porque **no hay código de error**: el fallo solo se detecta validando la respuesta. Es el
puente natural hacia los guardrails de la S6.

### Entregables

| Entregable | Ruta | Para qué |
|---|---|---|
| `tools/external_api.py` | `proyecto-final/<track>/app/` | La tool, con docstring A2 y `args_schema` |
| `agent.py` v1 | `proyecto-final/<track>/app/` | `create_agent()` con esa única tool y el prompt del track |
| **`prueba_tool.py`** | `lab/<track>/` | Llama la tool **directamente**, sin modelo, en los 3 escenarios |
| `EVIDENCIA-A1.md` | `lab/<track>/` | Las 3 trazas pegadas + qué se decidió en cada caso |

> **`prueba_tool.py` es la pieza que sostiene la regla de calificación.** Separa la calidad de la
> herramienta de la varianza del modelo: si la tool se comporta bien cuando se la llama
> directamente, el diseño está probado, aunque en la demo el modelo no la haya elegido.

### Rúbrica · 4 niveles × 5 criterios

| Criterio | Peso | Qué se mira |
|---|---|---|
| **Funcionalidad** | 30 % | Los 3 escenarios corren end-to-end con el agente |
| **Diseño de tool y prompt** | 25 % | Docstring A2 (verbo · cuándo · cuándo NO), `args_schema` correcto, nombre claro |
| **Manejo de errores** | 25 % | Los errores están redactados para el modelo. Hay tope de iteraciones (A4) |
| **Evidencia** | 10 % | `EVIDENCIA-A1.md` con las 3 trazas reales, no descritas |
| **Comunicación técnica** | 10 % | La sustentación de 5 min: explica la decisión, no narra el código |

**Regla del piso (decidida):**

> Si `prueba_tool.py` pasa los 3 escenarios y la docstring cumple A2, el equipo **no baja de
> Competente**, aunque en la sustentación el modelo no haya elegido la tool.

El motivo se explica en clase, porque es contenido: con 93 % de acierto por llamada, una tarea de
tres pasos sale bien el 80 % de las veces. **Penalizar al alumno por la varianza del modelo sería
enseñarle exactamente lo contrario de lo que el curso quiere enseñar.** Lo que sí se evalúa es si
diseñó el sistema para que esa varianza no se convierta en un fallo silencioso.

> ⚠️ **El criterio "observabilidad" de la rúbrica institucional no aplica todavía** — Langfuse
> entra en la S9. En el A1 su lugar lo ocupa "Evidencia": las 3 trazas impresas a mano son el
> precursor de lo que en la S9 se leerá en Langfuse. Anotarlo en `recursos/rubricas/`.

### Entrega y sustentación

| Momento | Qué |
|---|---|
| **Martes** (S3), 2 h de lab | Se construye la tool y se corren los 3 escenarios |
| **Miércoles 23:59** | Entrega del paquete completo (código + `EVIDENCIA-A1.md`) |
| **Jueves** (S4), primeros 20 min | Sustentación de **4 equipos, uno por track**, 5 min cada uno |

> ⚠️ **Corrección de la aritmética.** Al plantear esta opción calculé "~25 min de la S4", pero con
> 8-15 equipos a 5 min serían 40-75 min: se comería la sesión del catálogo de tools. Por eso
> **sustentan 4 equipos, uno por track, en rotación**: los demás entregan el paquete y el docente
> califica de forma asíncrona. A lo largo del curso (A1 · Proyecto M2 · Integrador) cada equipo
> sustenta al menos una vez, y el aula ve las 4 industrias en cada hito.

---

## 8. Qué **no** entra en esta sesión

| No entra | Va en |
|---|---|
| Catálogo de varias tools y selección dinámica | S4 |
| MCP | S4 (pre-work asíncrono) |
| Tools de **escritura** (crear reclamo, abrir siniestro) | S4 |
| Memoria conversacional y RAG | S5 |
| Guardrails, PII, prompt injection | S6 |
| Langfuse y trazabilidad | S9 |

> El L3 usa **una sola tool y de lectura**. La primera tool que escribe algo llega en el L4, ya
> con el hábito de manejar errores adquirido.

---

## 9. Los archivos a producir

| # | Archivo | Contenido pactado |
|---|---|---|
| **3.11** | `sesion-03-tools-api-externa/README.md` | Bloques 0 a 4 del guion, con el diagrama del bloque 1 y el antes/después de la docstring |
| **3.12** | `sesion-03-tools-api-externa/conceptos-previos.md` | Los 6 conceptos del pre-work + la verificación de entrada con `salud()` |
| **3.13** | `sesion-03-tools-api-externa/code/` | Las 4 demos + `README.md` de la carpeta |
| **3.14** | `sesion-03-tools-api-externa/lab/` | Enunciado del L3 **× 4 tracks**, con su tool, sus identificadores reales y los 3 escenarios |
| **3.15** | `sesion-03-tools-api-externa/solucion/` | `external_api.py`, `agent.py` v1, `prueba_tool.py` × 4 tracks |
| **3.16** | `sesion-03-tools-api-externa/assignment-a1.md` | Enunciado, entregables, rúbrica de 4×5, regla del piso y calendario de entrega |

### Trabajo previo

| # | Tarea | Por qué |
|---|---|---|
| **a** | `recursos/rubricas/rubrica-a1.md` — la rúbrica como archivo propio | La cita el assignment y la usará el docente al calificar |
| **b** | Anotar en `recursos/rubricas/` que el criterio de observabilidad no aplica antes de la S9 | Evita que se califique algo que aún no se enseñó |
| **c** | Fijar fecha a la tarea **2B.19** del ROADMAP: lunes semana 2 | Hoy está en ⏸️ sin vencimiento, y bloquea la nota del módulo |

---

## 10. Errores esperables y cómo atenderlos

| Síntoma | Causa | Respuesta del docente |
|---|---|---|
| `401` del simulador | API key del equipo mal copiada en `SIM_API_KEY` | Reintentar no sirve: es credencial. Reemitir la key |
| El modelo no llama a la tool | Docstring vaga, o la pregunta no correspondía | Reescribir la docstring con "cuándo NO" y volver a probar |
| El agente reintenta sin parar ante el 503 | Falta el tope de iteraciones (A4) | Es justo lo que el bloque 3 anticipó: fijar el tope |
| El agente inventa el dato tras un 404 | El mensaje de error no le dijo qué hacer | Reescribir el mensaje para el modelo, no para el log |
| Todo funciona con `DATA_SOURCE=csv` pero no contra la API | El Space está caído o la key no se repartió | Modo degradado para seguir; el escenario 3 se documenta con el CSV |
| El equipo termina en 50 min | Ya dominaba REST | Reto: `?_fallo=malformado`, que no da código de error |
