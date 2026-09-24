# Sesión 4 — Tools e integración de herramientas

> Semana 2 · jueves · **2.5 h teoría + 3.5 h práctica = 6 h**.
> Primeros 20 min de la clase en vivo: sustentación del Assignment A1 (4 equipos, uno por track,
> 5 min cada uno). El guion de abajo empieza después de esa sustentación.

Antes de esta sesión: pre-work de 1 h sobre MCP ([`pre-work-mcp.md`](pre-work-mcp.md)) y haber
conectado tu agente al servidor MCP del simulador.

---

## 1. Objetivos de aprendizaje

1. Diseñar un catálogo de tools con **responsabilidad única**: una tool, una pregunta.
2. Explicar por qué el tamaño y la ambigüedad del catálogo deben medirse, y cómo los errores
   pueden acumularse a lo largo del bucle.
3. **Medir** el acierto de selección de tu propio agente y leer una matriz de confusión.
4. Distinguir una tool **idempotente** de una que no lo es, y proteger la segunda.
5. Conectar el agente a un servidor **MCP** y explicar qué cambia y qué no.

---

## 0. De una tool a cuatro — qué se rompe

Con una sola tool (tu L3), el modelo no elige nada: solo decide *si* la usa. Con cuatro, además
tiene que decidir *cuál*. Esa decisión la toma leyendo únicamente el nombre, la docstring y el
esquema de argumentos de cada tool — nunca tu código. Hoy construyes las otras tres y aprendes a
medir si esa elección funciona.

**`domain_tools.py` no empieza de cero.** Tu `tools/external_api.py` del L3
(`solucion/<track>/external_api.py` en la Sesión 3 es la referencia) tiene ya la primera tool del
catálogo — literalmente la misma función. Hoy la mueves a `domain_tools.py` junto con las 3
nuevas: `TOOLS_NUCLEO` de las 4 tracks abre exactamente con la tool que ya escribiste y probaste
con `prueba_tool.py`.

---

## 1. Catálogo y responsabilidad única

**Una tool, una pregunta.** La tool que hace dos cosas a la vez ("consulta el plan y también
regístrame un reclamo") nunca se elige bien: el modelo no puede anticipar cuál de las dos cosas
vas a necesitar solo por su nombre. Cada una de tus 4 tools núcleo debe responder exactamente un
tipo de pregunta del cliente, con un nombre que empiece con un verbo y describa el dato que
devuelve (`get_data_usage`, no `manage_line`).

---

## 2. Selección dinámica: cómo elige el modelo y por qué falla

El modelo **no ve tu código**. Ve esto:

```
   [ nombre de la tool ]  +  [ docstring ]  +  [ esquema de argumentos ]
```

Y con eso decide. Cuando falla, falla de tres maneras:

```
   ┌─ SOLAPAMIENTO ── dos docstrings describen el mismo caso
   │                  → escribir en cada una "cuándo NO" usarla
   ├─ VACÍO ───────── ninguna docstring describe la pregunta
   │                  → el modelo elige la menos mala, o no llama a nada
   └─ SOBRE-USO ───── llama a una tool cuando no debía llamar a ninguna
                      → falta el límite: tarifas y políticas van a RAG (Sesión 5)
```

Cada tipo tiene su celda propia en la matriz de confusión de `docente/matriz_seleccion.py`, y una
corrección distinta. Es lo que vas a practicar en el bloque 6 de hoy, sobre tu propio catálogo.

**De dónde salen las 30 consultas que arma la matriz:** `recursos/golden/consultas-<tu-track>.json`
— el mismo archivo que ya usaste en la Sesión 2 para medir tu clasificador (`medir_clasificador.py`,
campo `intencion`). Aquí el script lee el campo `tool_esperada` de esas mismas 30 filas. No es
casualidad que coincidan: es la razón de que el archivo exista en un solo lugar (ver Sesión 2,
sección "El conjunto de prueba").

### 2.1 Few-shot para desambiguar tools (regla A5)

La docstring no es la única palanca contra el solapamiento. Cuando dos tools quedan cerca en el
espacio de decisión del modelo, **un par de ejemplos en el system prompt** (el mismo mecanismo
de la Sesión 2, aplicado aquí a selección de herramientas en vez de a clasificación) suele
resolver la confusión más rápido que seguir puliendo la docstring:

```
system prompt del track
  + identidad, jerga, límites (ya lo conoces de comun/prompts_industria.py)
  + 2 ejemplos: "cuando el cliente dice X, la tool correcta es Y — y NO Z porque..."
```

**Cuándo usarlo:** solo si, después de corregir las docstrings (bloque 2), la matriz sigue
mostrando confusión concentrada entre las mismas dos tools. Añadir few-shot sin haber corregido
antes la docstring es tratar el síntoma, no la causa — y cada ejemplo se paga en tokens en cada
llamada del agente, no solo en el momento de medir (recuerda `code/04_tokens_y_costo.py` de la
Sesión 2).

---

## 3. Por qué 4 y no 6 (regla A1)

La fiabilidad puede acumularse a lo largo de una tarea. Bajo el supuesto simplificado
de pasos independientes con probabilidad de éxito 0.93, todos aciertan con probabilidad
0.93³ ≈ 80 % en tres pasos y 0.93⁵ ≈ 70 % en cinco. No es una tasa medida del agente ni una
ley universal: los fallos reales pueden estar correlacionados.

El curso usa **cuatro tools núcleo de negocio en L4** por alcance didáctico. Desde L5 añade
un retriever: cinco tools enlazadas. Tamaño del catálogo y cantidad de iteraciones son
variables distintas. No existe aquí evidencia de un umbral universal de cuatro herramientas;
la matriz mide el catálogo concreto. Las opcionales se prueban con una selección explícita.

---

## 4. Idempotencia y tope de iteraciones (regla A4)

| Tool | ¿Idempotente? | Qué pasa si se reintenta | Protección |
|---|---|---|---|
| `get_customer_plan` (telco) | Sí | No modifica estado; la respuesta puede cambiar si cambian los datos | No necesita deduplicación de escrituras |
| `get_account_balance` (banca) | Sí | Nada | Ninguna |
| `create_complaint_ticket` (telco) | **No** | **Puede duplicar reclamos** | Confirmación; en producción, deduplicación/idempotency key |
| `open_claim` (seguros) | **No** | Dos expedientes del mismo siniestro | Confirmación explícita |
| `start_return_request` (retail) | **No** | Dos solicitudes de devolución | Confirmación explícita |

> **Nota de honestidad sobre banca.** Sus 4 tools núcleo (`get_account_balance`,
> `list_transactions`, `get_card_info`, `score_transaction_risk`) son las cuatro de **solo
> lectura** — no hay ninguna tool de escritura en el núcleo de este track. Su única acción de
> escritura (`request_card_block`, bloqueo de tarjeta) queda como **tool opcional**, precisamente
> porque es irreversible: el curso prefiere introducir la escritura donde el costo de un error es
> menor (un reclamo o una devolución duplicados se pueden anular; una tarjeta bloqueada, no). El
> guardrail de banca sobre `request_card_block` se retoma en la Sesión 6.

En los tracks con escritura, es la primera vez que escribes una tool que **modifica algo**.
La confirmación del checkpoint es un booleano en los argumentos del modelo: ilustra el
contrato, pero no demuestra aprobación humana autenticada. Tampoco evita por sí
sola duplicados ante reintentos. La regla, para toda tool de
escritura: exige confirmación explícita del usuario antes de ejecutarse. Se implementa **hoy**,
no se pospone a los guardrails de la Sesión 6.

El mismo bloque cubre el **tope de iteraciones**: sin un límite, un agente que no logra resolver
la tarea (por ejemplo, ante un `503` del simulador) puede reintentar indefinidamente hasta agotar
tu cuota de HF. Cada llamada al agente debe tener un máximo de vueltas del bucle, y al alcanzarlo,
avisar y derivar — nunca fallar en silencio ni repetir para siempre. Ver `code/03_tope_iteraciones.py`.

---

## `proyecto-final/`: qué es y qué no es

**Aclaración que debió estar desde el Laboratorio 1.** `proyecto-final/<track>/` en **este**
repositorio (el del curso) es la **catálogo base de referencia del docente**, no una aplicación final completa. Las
soluciones de cada sesión muestran su checkpoint; los verificadores comprueban el catálogo (`docente/verificar_tools.py`,
`docente/matriz_seleccion.py`). **No es tu repositorio.** Tu propio proyecto vive en el
repositorio de tu equipo, y lo construyes del L1 al L11 siguiendo cada enunciado — no copiando
`proyecto-final/`.

Por eso, cuando midas tu catálogo del L4, usas `--tools lab/<track>/domain_tools.py` (**tu**
archivo), nunca `--tools proyecto-final/<track>/app/tools/domain_tools.py` (**la referencia**):
medir la referencia contra sí misma no te dice nada sobre tu trabajo.

---

## 5. Las 3 demos y el laboratorio

Ver [`code/README.md`](code/README.md) para las demos y [`lab/README.md`](lab/README.md) para el
Laboratorio 4 completo (catálogo de 4 tools, medición y Avance 1 del proyecto).

---

## 6. Qué NO entra hoy

| No entra | Va en |
|---|---|
| RAG, embeddings, Qdrant | Sesión 5 |
| Memoria conversacional | Sesión 5 |
| Guardrails, PII, prompt injection | Sesión 6 |
| Construir un servidor MCP propio | Reto opcional del L4 |
| Langfuse | Sesión 9 |
