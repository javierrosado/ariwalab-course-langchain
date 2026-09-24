# Esqueleto · Sesión 2 — Ecosistema LangChain: prompts, cadenas y modelos

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-1-fundamentos/sesion-02-ecosistema-langchain/` |
| Semana · día | Semana 1 · jueves |
| Horas | **3.0 h teoría · 3.0 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (120 T / 50 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L2 · Clasificador de intención** |
| Hitos | **Test 2** · **pase de entrada de Pydantic** |

> **Convención horaria:** tres horas en vivo = 170 minutos de contenido y diez de pausa.
> El reparto teoría/práctica de la malla se calcula sobre las seis horas completas.

---

## 2. Objetivos de aprendizaje

Al terminar, el alumno puede:

1. Explicar por qué el modelo es **stateless** y qué es realmente la "memoria" de un agente.
2. Escribir un prompt con la estructura **Rol + Contexto + Tarea + Formato** y justificar cada parte.
3. Decidir cuándo el **few-shot** rinde y cuándo solo gasta tokens (regla A5).
4. Definir un esquema Pydantic y obtener del modelo una **salida tipada y validada**.
5. Explicar por qué `with_structured_output()` **no basta** y qué añade `comun/structured.py`.
6. Medir el acierto de su clasificador contra un conjunto de prueba, en vez de opinar sobre él.

El 1, 2, 3 y 5 se verifican con el **Test 2**; el 4 y el 6 con el **L2**.

---

## 3. Con qué llega el alumno

**Pre-work de 1 h** (`conceptos-previos.md` de esta sesión):

| # | Concepto | Por qué antes de la clase |
|---|---|---|
| 1 | Roles de mensaje: `system`, `human`, `ai`, `tool` | Es el modelo mental de toda la librería |
| 2 | El historial es una **lista de mensajes** que tú reenvías | Sin esto no se entiende la memoria de la S5 |
| 3 | **Pydantic v2**: `BaseModel`, `Field`, `Enum`, validación | Prerrequisito **duro** de esta sesión y de la S3 |
| 4 | JSON Schema, lectura básica | Es lo que el modelo recibe de verdad, no la clase Python |
| 5 | f-strings y placeholders | Base de `PromptTemplate` |

### Pase de entrada · Pydantic

> **Regla: sin el ejercicio entregado, no se hace el L2.**

- El ejercicio es el `Reclamo` de `00-preparacion/conceptos-previos/python-y-entorno.md` §6.
- Se entrega **antes** de la S2: el archivo `.py` más la salida de `Reclamo.model_json_schema()`.
- Quien no lo entregó dedica las 2 h de laboratorio a resolverlo, no al L2, y retoma el L2 con el
  checkpoint de la solución.

**Por qué es duro y aun así correcto.** La S3 es el **Assignment A1** y ocurre 5 días después. Un
alumno que no sabe definir un `BaseModel` no puede escribir el `args_schema` de una tool: no es que
le cueste el A1, es que no puede empezarlo. Descubrirlo el jueves de la semana 1 deja margen;
descubrirlo el martes de la semana 2 no.

**Herramienta para el docente:** `docente/verificar_ejercicio_pydantic.py`, que
recibe el archivo del alumno y comprueba las 4 restricciones del enunciado (Enum de 3 valores,
longitud 10-200, exactamente 9 dígitos, booleano con default). Con 15 equipos, revisar a ojo no
escala.

---

## 4. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | De "primer llamado" a "primer contrato" | 5 | T | Qué cambia hoy: el modelo deja de devolver texto y empieza a devolver estructura |
| 1 | Mensajes, roles y **statelessness** | 25 | T | `system`/`human`/`ai`. El historial como lista. Por qué el turno 10 cuesta 8× el turno 1 |
| 2 | **Rol + Contexto + Tarea + Formato** | 25 | T | Las 4 partes, una a una, sobre el prompt real del track |
| 3 | **Few-shot** (regla A5) | 20 | T | Cuándo rinde: enums y campos ambiguos. Cuándo solo gasta tokens |
| 4 | **Structured output: la demo del fallo** | 25 | T | Comparar esquema válido, error de validación y wrapper; fallo simulado reproducible |
| 5 | `comun/structured.py` (regla A3) | 20 | T | Comprobar retorno · reintentar con instrucción correctiva · fallar con claridad |
| — | **Pausa** | 10 | — | |
| 6 | Práctica guiada: el esquema `Intencion` del track | 35 | P | Cada equipo escribe su Enum de 5 categorías y lo prueba |
| 7 | **Test 2** | 15 | P | 10 preguntas |

**Teoría 120 min · práctica 50 min · pausa 10** → con el pre-work y el lab: **3.0 h / 3.0 h** ✅

### Bloque 4 — la demo del fallo, en detalle

El bloque compara validación y recuperación de errores; no se exige que falle una llamada
real. `with_structured_output(Intencion)` valida mediante Pydantic. Si la demo devuelve un
objeto válido, discutir su exactitud semántica; para un fallo reproducible ejecutar el
verificador con modelo simulado.

```text
modelo + esquema → validación Pydantic → objeto válido
                              ↓ error
                     wrapper, un reintento
                              ↓ vuelve al modelo
                  segundo fallo → ExtraccionFallida
```

El wrapper comprueba también `None` y tipo inesperado. Un reintento es el presupuesto
predeterminado para limitar costo y latencia, no una prueba de que el segundo fallo sea
necesariamente culpa del prompt. Conservar guion, horas y Test 2 corregido.

---

## 5. Las 4 demos · `code/`

| Archivo | Qué demuestra | Qué debe notar el alumno |
|---|---|---|
| `01_plantilla_dominio.py` | Rol + Contexto + Tarea + Formato sobre el prompt del track | Comparar el efecto observado de instrucciones y esquema |
| `02_few_shot.py` | El mismo clasificador con 0, 2 y 4 ejemplos | Medir si más ejemplos mejoran el acierto y cuánto cuestan |
| `03_structured_crudo_vs_robusto.py` | La misma extracción por los dos caminos, lado a lado | Cuántos intentos hizo falta en cada uno. Usa `extraer_con_detalle()` |
| `04_tokens_y_costo.py` | Conteo de tokens de un prompt con y sin few-shot y con historial | Que el few-shot **se paga en cada llamada**, no una sola vez |

---

## 6. Laboratorio L2 · Clasificador de intención

**Objetivo:** convertir texto libre del cliente en estructura tipada y **medir** el acierto.

### Taxonomía — alineada 1:1 con las tools del L4

| Track | Categorías del Enum | Tool del L4 que predice |
|---|---|---|
| **telecomunicaciones** | `CONSULTA_PLAN` | `get_customer_plan` |
| | `CONSULTA_CONSUMO` | `get_data_usage` |
| | `AVERIA` | `run_line_diagnostics` |
| | `RECLAMO` | `create_complaint_ticket` |
| | `OTRO` | ninguna → va a RAG en la S5 |
| **banca** | `CONSULTA_SALDO` · `CONSULTA_MOVIMIENTOS` · `CONSULTA_TARJETA` · `SOSPECHA_FRAUDE` · `OTRO` | `get_account_balance` · `list_transactions` · `get_card_info` · `score_transaction_risk` · — |
| **retail** | `SEGUIMIENTO_PEDIDO` · `CONSULTA_PRODUCTO` · `CONSULTA_STOCK` · `DEVOLUCION` · `OTRO` | `track_order` · `get_product_details` · `check_stock_by_store` · `start_return_request` · — |
| **seguros** | `CONSULTA_POLIZA` · `COTIZACION` · `ESTADO_SINIESTRO` · `REPORTE_SINIESTRO` · `OTRO` | `get_policy_by_plate` · `quote_soat` · `get_claim_status` · `open_claim` · — |

**Por qué 1:1.** En el L4 el alumno no reclasifica nada: la categoría que ya sabe producir *es* la
herramienta que debe elegir. La progresión L2 → L4 deja de ser temática y pasa a ser mecánica.

**`OTRO` no es un cajón de sastre.** Es la categoría de las preguntas sobre tarifas, coberturas y
políticas — exactamente las que en la S5 se responden con RAG. El alumno construye en el L2 la
etiqueta que en la S5 dispara el recuperador.

### El conjunto de prueba — una sola fuente para el L2 y el L4

Usar el subconjunto de 20 consultas por track de `recursos/golden/consultas-<track>.json`
que comparten el clasificador L2 y la matriz de selección L4. Comparar las tareas con
las mismas entradas permite interpretar sus resultados:

```
recursos/golden/consultas-<track>.json
[
  {"consulta": "¿Qué plan tengo contratado en la línea 987654321?",
   "intencion": "CONSULTA_PLAN",
   "tool_esperada": "get_customer_plan"},
  ...
]
                    │                          │
                    ▼                          ▼
             L2 · acierto de             L4 · matriz de
             clasificación               selección de tools
```

`matriz_seleccion.py` lee las consultas del archivo compartido.

**Efecto pedagógico:** el alumno ve las **mismas 20 consultas** dos veces — en el L2 clasificándolas
y en el L4 resolviéndolas — y entiende que el clasificador y el agente resuelven el mismo problema
con distinta profundidad.

### Entregables

| Entregable | Ruta | Qué contiene |
|---|---|---|
| `schemas.py` | `proyecto-final/<track>/app/` | `Intencion`: `categoria` (Enum de 5), `urgencia`, entidades del track |
| `prompts.py` | `proyecto-final/<track>/app/` | Plantilla Rol+Contexto+Tarea+Formato + 2 ejemplos few-shot |
| `clasificar.py` | `lab/<track>/` | Usa `extraer()` de `comun/structured.py`. **Prohibido** `with_structured_output()` directo |
| `medir_clasificador.py` | `lab/<track>/` | Corre las 20 consultas del golden set e imprime acierto + matriz de confusión |

### Criterio de aceptación

- **≥ 90 % de acierto** sobre las 20 consultas del golden set del curso.
- El alumno añade **5 consultas propias** de su track y reporta el acierto sobre las 25.
- Se reporta también **cuántas extracciones necesitaron reintento** (`al_primer_intento`): es el
  primer dato de fiabilidad que el alumno mide con sus manos, y se retoma en la S10.

> ⚠️ **El umbral del 90 % está sin verificar.** Con 5 clases, un modelo genérico y few-shot es
> plausible, pero nadie lo ha medido contra el endpoint real. **Acción para el docente:** correr el
> `medir_clasificador.py` de un track antes del dictado, junto con `check_stack`. Si
> sale 80 %, se baja el umbral o se mejora el few-shot — pero se decide con el número delante,
> no el día de la clase.

---

## 7. Test 2 · 10 preguntas

| # | Evalúa |
|---|---|
| 1-2 | Roles de mensaje y qué hace cada uno |
| 3 | Por qué el modelo es stateless y qué es la "memoria" |
| 4-5 | Rol + Contexto + Tarea + Formato: identificar la parte que falta en un prompt dado |
| 6 | Cuándo el few-shot **no** conviene |
| 7 | Qué recibe el modelo: la clase Pydantic o el JSON Schema |
| 8 | Por qué `with_structured_output()` no basta |
| 9 | Por qué un solo reintento y no cinco |
| 10 | Qué componente domina el costo en una conversación de 10 turnos |

---

## 8. Qué **no** entra en esta sesión

| No entra | Va en |
|---|---|
| `@tool`, function calling, `args_schema` | S3 |
| `create_agent()` y el bucle ReAct | S3 |
| Llamadas a APIs externas y al simulador | S3 |
| RAG, embeddings, Qdrant | S5 |
| Memoria conversacional real (`thread_id`) | S5 |
| Guardrails y PII | S6 |
| Streaming y manejo de errores de red | material asíncrono opcional, enlazado desde el README |

> El L2 **no llama a ninguna API ni al simulador**: entra texto, sale estructura. Es la única
> sesión del curso en la que el modelo trabaja solo, y conviene decirlo para que el alumno note el
> contraste cuando la S3 conecte el primer dato real.

---

## 10. Errores esperables y cómo atenderlos

| Síntoma | Causa | Respuesta del docente |
|---|---|---|
| El modelo inventa un valor de Enum | Faltan ejemplos few-shot o el `description` del campo es vago | Es la lección del bloque 3: añadir 2 ejemplos y volver a medir |
| Acierto alto en las 20 del curso, bajo en las 5 propias | Las consultas propias son ambiguas incluso para un humano | Buena señal: si un humano duda, la etiqueta está mal definida |
| `ExtraccionFallida` repetida | El esquema pide demasiado en una sola llamada | Partir en dos extracciones, o simplificar el esquema |
| Todo se clasifica como `OTRO` | El `description` de las 4 categorías reales no distingue | Escribir en cada `description` **cuándo NO** aplica — es A2 aplicada a un enum |
| El lab termina en 40 min | Equipo que ya dominaba Pydantic | Reto: añadir el campo `entidades` con extracción de número de línea, cuenta, SKU o placa |
