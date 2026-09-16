# Sesión 4 — Tools e integración de herramientas

> Semana 2 · jueves · **2.5 h teoría + 3.5 h práctica = 6 h**.
> Primeros 20 min de la clase en vivo: sustentación del Assignment A1 (4 equipos, uno por track,
> 5 min cada uno). El guion de abajo empieza después de esa sustentación.

Antes de esta sesión: pre-work de 1 h sobre MCP ([`pre-work-mcp.md`](pre-work-mcp.md)) y haber
conectado tu agente al servidor MCP del simulador.

---

## 1. Objetivos de aprendizaje

1. Diseñar un catálogo de tools con **responsabilidad única**: una tool, una pregunta.
2. Explicar por qué la precisión de selección cae al pasar de 4 herramientas, y por qué eso se
   agrava a lo largo del bucle del agente.
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

---

## 3. Por qué 4 y no 6 (regla A1)

La fiabilidad se compone (decisión D20): si el modelo acierta el 93 % de las veces en una sola
llamada, una tarea de 3 pasos sale bien el 80 % de las veces, y una de 5 pasos, el 70 %. Cuantas
más tools enlazadas, más pasos potenciales, y más se multiplica el error. La precisión de
selección cae de forma notoria al pasar de 4-5 herramientas — por eso el curso fija **4 tools
núcleo** por track y dos más quedan como reto opcional, nunca enlazadas junto a las cuatro.

---

## 4. Idempotencia y tope de iteraciones (regla A4)

| Tool | ¿Idempotente? | Qué pasa si se reintenta | Protección |
|---|---|---|---|
| `get_customer_plan` (telco) | Sí | Nada: misma respuesta | Ninguna |
| `get_account_balance` (banca) | Sí | Nada | Ninguna |
| `create_complaint_ticket` (telco) | **No** | **Dos reclamos duplicados** | Confirmación explícita antes de llamar |
| `open_claim` (seguros) | **No** | Dos expedientes del mismo siniestro | Confirmación explícita |
| `start_return_request` (retail) | **No** | Dos solicitudes de devolución | Confirmación explícita |

> **Nota de honestidad sobre banca.** Sus 4 tools núcleo (`get_account_balance`,
> `list_transactions`, `get_card_info`, `score_transaction_risk`) son las cuatro de **solo
> lectura** — no hay ninguna tool de escritura en el núcleo de este track. Su única acción de
> escritura (`request_card_block`, bloqueo de tarjeta) queda como **tool opcional**, precisamente
> porque es irreversible: el curso prefiere introducir la escritura donde el costo de un error es
> menor (un reclamo o una devolución duplicados se pueden anular; una tarjeta bloqueada, no). El
> guardrail de banca sobre `request_card_block` se retoma en la Sesión 6.

Es la primera vez que escribes una tool que **modifica algo**. La regla, para toda tool de
escritura: exige confirmación explícita del usuario antes de ejecutarse. Se implementa **hoy**,
no se pospone a los guardrails de la Sesión 6.

El mismo bloque cubre el **tope de iteraciones**: sin un límite, un agente que no logra resolver
la tarea (por ejemplo, ante un `503` del simulador) puede reintentar indefinidamente hasta agotar
tu cuota de HF. Cada llamada al agente debe tener un máximo de vueltas del bucle, y al alcanzarlo,
avisar y derivar — nunca fallar en silencio ni repetir para siempre. Ver `code/03_tope_iteraciones.py`.

---

## `proyecto-final/`: qué es y qué no es

**Aclaración que debió estar desde el Laboratorio 1.** `proyecto-final/<track>/` en **este**
repositorio (el del curso) es la **implementación de referencia del docente** — el aspecto final
que debería tener tu proyecto, ya escrita y verificada (`docente/verificar_tools.py`,
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
