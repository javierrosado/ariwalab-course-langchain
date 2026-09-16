# Sesión 2 — Ecosistema LangChain: prompts, cadenas y modelos

> Semana 1 · jueves · **3.0 h teoría + 3.0 h práctica = 6 h**.

Antes de esta sesión: pre-work de 1 h ([`conceptos-previos.md`](conceptos-previos.md)) y el
**pase de entrada de Pydantic** entregado — sin él no se hace el L2 hoy.

---

## 1. Objetivos de aprendizaje

1. Explicar por qué el modelo es **stateless** y qué es realmente la "memoria" de un agente.
2. Escribir un prompt con la estructura **Rol + Contexto + Tarea + Formato** y justificar cada parte.
3. Decidir cuándo el **few-shot** rinde y cuándo solo gasta tokens (regla A5).
4. Definir un esquema Pydantic y obtener del modelo una **salida tipada y validada**.
5. Explicar por qué `with_structured_output()` **no basta** y qué añade `comun/structured.py`.
6. Medir el acierto de tu clasificador contra un conjunto de prueba, en vez de opinar sobre él.

---

## 0. De "primer llamado" a "primer contrato"

En la Sesión 1 el modelo devolvía texto. Hoy deja de ser suficiente: vas a pedirle una
**estructura** —un objeto con campos y tipos— y vas a tratar cualquier desviación de esa
estructura como un error, no como una curiosidad. Ese cambio de expectativa es el tema del día.

---

## 1. Mensajes, roles y *statelessness*

El modelo no tiene memoria entre llamadas. Lo que ves como "recordar" es tu código reenviando
el **historial completo como una lista de mensajes** (`system`, `human`, `ai`, y luego `tool`
desde la Sesión 3) en cada nueva llamada. Por eso el turno 10 de una conversación cuesta más
tokens que el turno 1: no es que la pregunta sea más larga, es que arrastra los 9 turnos
anteriores. Esto ya lo mediste en la demo 4 de la Sesión 0 — hoy lo vuelves a ver en
`code/04_tokens_y_costo.py`, aplicado a tu propio prompt.

---

## 2. Rol + Contexto + Tarea + Formato

La estructura de cualquier prompt de producción, en cuatro partes:

| Parte | Qué responde | Ejemplo (telco) |
|---|---|---|
| **Rol** | ¿Quién eres? | "Eres el asistente de AndesMóvil" |
| **Contexto** | ¿Qué sabes ya? | El vocabulario del sector, los límites de tu industria |
| **Tarea** | ¿Qué tienes que hacer con esta entrada? | "Clasifica la consulta del cliente en una categoría" |
| **Formato** | ¿Cómo debe verse la salida? | "Devuelve un objeto `Intencion` con categoría, urgencia y entidades" |

`comun/prompts_industria.py`, que ya usaste en la Sesión 1, es Rol + Contexto + los límites de
tu industria. Hoy le agregas la Tarea y el Formato para construir el prompt de clasificación.

---

## 3. Few-shot (regla A5)

Un ejemplo dentro del prompt ("clasifica esto → así") ayuda al modelo a entender un patrón
ambiguo mejor que cualquier descripción en prosa. Pero cada ejemplo se paga **en tokens, en
cada llamada** — no es gratis.

| Cuándo rinde | Cuándo solo gasta tokens |
|---|---|
| Enums con categorías parecidas entre sí | Categorías ya obvias por el vocabulario |
| Campos con un formato específico que hay que replicar | Texto libre sin restricción de forma |
| El primer y segundo ejemplo | El tercer y cuarto ejemplo (rendimiento decreciente) |

**Dónde se ve esto hoy:** `code/02_few_shot.py` compara el mismo clasificador con 0, 2 y 4
ejemplos. La mejora del segundo ejemplo es notoria; la del cuarto, casi nula.

---

## 4. Structured output: la demo del fallo

Este es el bloque que decide la sesión, y **tiene que fallar en vivo**:

```
   1.  Esquema Intencion con Enum de 5 categorías, sin few-shot
   2.  Consulta ambigua del track
   3.  El modelo devuelve  categoria="CONSULTA_DE_PLAN"   ← inventó el valor
                           urgencia=None                   ← campo obligatorio vacío
   4.  El código revienta tres líneas más abajo, no en la llamada
```

**El mensaje: el fallo no aparece donde se produce.** Por eso la validación va pegada a la
extracción, no al final del flujo. `with_structured_output()` de LangChain, usado solo, no te
protege de esto — funciona la mayoría de las veces, y la minoría es exactamente lo que rompe un
agente en producción.

Y entonces entra `comun/structured.py` (regla A3):

```
   extraer(modelo, Intencion, consulta)
        │
        ├── valida contra el esquema          ¿enum permitido? ¿campos obligatorios?
        ├── si falla, reintenta UNA vez       devolviéndole al modelo el error concreto
        └── si vuelve a fallar, ExtraccionFallida     nunca un None que revienta después
```

> **Por qué un solo reintento.** Si el segundo intento también falla, el problema es el esquema
> o el prompt, no la suerte. Reintentar cinco veces esconde un defecto de diseño y multiplica
> el costo — es la misma lógica de "un solo reintento" que verás en `comun/api_client.py` en
> la Sesión 3.

A partir de hoy, **ninguna extracción estructurada del curso usa `with_structured_output()`
directo**: todas pasan por `extraer()` o `extraer_con_detalle()`.

---

## 5. Las 4 demos y el laboratorio

Ver [`code/README.md`](code/README.md) para las demos y [`lab/README.md`](lab/README.md) para
el Laboratorio 2 completo (clasificador de intención, medido contra el golden set).

---

## Qué NO entra hoy

| No entra | Va en |
|---|---|
| `@tool`, function calling, `args_schema` | Sesión 3 |
| `create_agent()` y el bucle ReAct | Sesión 3 |
| Llamadas a APIs externas y al simulador | Sesión 3 |
| RAG, embeddings, Qdrant | Sesión 5 |
| Memoria conversacional real (`thread_id`) | Sesión 5 |
| Guardrails y PII | Sesión 6 |
| Streaming y manejo de errores de red | Material asíncrono opcional |

> El L2 **no llama a ninguna API ni al simulador**: entra texto, sale estructura. Es la única
> sesión del curso en la que el modelo trabaja solo — nótalo, porque la Sesión 3 rompe ese
> aislamiento con el primer dato real.
