# Esqueleto · Sesión 10 — Optimización continua y evaluación

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-3-produccion/sesion-10-evaluacion-optimizacion/` |
| Semana · día | Semana 5 · jueves |
| Horas | **2.5 h teoría · 3.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (90 T / 80 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L10 · Evaluación y optimización** |
| Hitos | **Avance 3 del M3** |

---

## 2. La sesión donde se cierra la espina dorsal del curso

El golden set que se escribió para el L2 **es** el dataset de evaluación de esta sesión. No se
construye nada nuevo: se usa por cuarta vez, ahora completo.

```
   recursos/golden/consultas-<track>.json          30 casos por track
   │
   ├── 20 con tool esperada  ──► S2 · L2   clasificar intención
   │                         ──► S4 · L4   seleccionar herramienta
   ├── 10 de categoría OTRO  ──► S5 · L5   recuperar y citar
   └── los 30 juntos         ──► S10 · L10 evaluar v1 contra v2
```

> **Decirlo explícitamente en clase.** El alumno lleva nueve sesiones viendo las mismas consultas y
> hoy descubre que eran un *golden dataset* desde el primer día. Es la mejor manera de enseñar que
> un conjunto de evaluación no se improvisa al final: se construye mientras se construye el sistema.

⚠️ **Prerrequisito:** las 10 consultas `OTRO` por track y el
campo `respuesta_esperada` en los 30. Sin eso no hay evaluación automática.

---

## 3. Objetivos de aprendizaje

1. Explicar por qué `assert respuesta == "esperado"` no sirve, y qué lo reemplaza.
2. Construir evaluators **determinísticos** para exactitud, uso de tool y *groundedness*.
3. Explicar qué es **LLM-as-judge**, cuándo sirve y cuáles son sus sesgos.
4. Comparar dos versiones de prompt sobre el mismo dataset y decidir con el número.
5. Distinguir una mejora real de ruido de muestreo.

---

## 4. Con qué llega el alumno

**Pre-work de 1 h:**

| # | Concepto | Por qué |
|---|---|---|
| 1 | Conjunto de prueba / *golden dataset* | Base de todo lo demás |
| 2 | Precisión y recall, nociones | Métricas de tools y retriever |
| 3 | **Groundedness**: fidelidad a la fuente | Métrica central de un sistema RAG |
| 4 | LLM-as-judge y sus sesgos conocidos | Técnica de la sesión |
| 5 | Prueba A/B y qué significa "mejoró" | Comparar dos prompts |
| 6 | Regresión: por qué se re-evalúa al cambiar algo | Puente hacia CI |

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | Mejorar con evidencia, no con intuición | 5 | T | Retomar los 2 cuellos del Avance 2: hoy se atacan |
| 1 | El golden dataset era el de siempre | 15 | T | El diagrama de §2. Cómo se construye un dataset: en paralelo, no al final |
| 2 | **Los 3 evaluators determinísticos** | 25 | T | Exactitud · uso correcto de tool · groundedness por cita comprobable |
| 3 | **LLM-as-judge y sus sesgos** | 25 | T | Qué mide bien, qué mide mal, y la autoevaluación |
| 4 | A/B de prompts: cuándo una mejora es real | 20 | T | Ruido de muestreo. 30 casos no dan para presumir de 2 puntos |
| — | **Pausa** | 10 | — | |
| 5 | Práctica: los 30 casos en Langfuse Datasets | 35 | P | Cargar y correr la línea base v1 |
| 6 | Optimizar y medir v2 | 45 | P | Un cambio, una medición, una fila en la tabla |

**Teoría 90 · práctica 80 · pausa 10** → con pre-work y lab: **2.5 h / 3.5 h** ✅

### Bloque 2 — los tres evaluators que sí califican

| Evaluator | Qué mide | Cómo se calcula, sin modelo de por medio |
|---|---|---|
| **Uso correcto de tool** | ¿Llamó a la herramienta esperada? | Comparar el `tool_call` contra `tool_esperada` del dataset. **Es `matriz_seleccion.py`**, que existe desde el L4 |
| **Exactitud** | ¿La respuesta contiene el dato correcto? | ¿Aparece `respuesta_esperada` (o su valor clave) en el texto? |
| **Groundedness por cita** | ¿La cita existe y sostiene la afirmación? | El documento y la sección citados existen, y la cifra afirmada está en ese chunk |

> **Los tres son verificables sin juicio.** Se pueden correr mil veces y dan lo mismo. Eso es lo que
> los hace aptos para calificar, y lo que los distingue del juez del bloque 3.

### Bloque 3 — LLM-as-judge: se enseña, no califica

**El juez es demo. La nota la sostienen los tres evaluators determinísticos.**

Cómo se enseña el sesgo, en vivo y en 10 minutos:

```
   1.  Tomar 10 casos ya puntuados por los evaluators determinísticos
   2.  Pasarlos por el juez (el mismo Qwen3-32B)
   3.  Poner las dos columnas lado a lado y buscar los desacuerdos
```

Lo que aparece, y es el contenido:

| Sesgo | Cómo se manifiesta |
|---|---|
| **Autoevaluación** | El modelo puntúa mejor sus propias salidas que las de otro modelo |
| **Verbosidad** | Una respuesta larga y segura puntúa alto aunque sea falsa — es la alucinación de la S1, otra vez |
| **Posición** | En comparaciones A/B, la primera opción tiende a ganar |
| **Autocomplacencia** | Ante la duda, aprueba |

> **Por qué igual se enseña.** Es la técnica que el alumno va a encontrar en toda la industria, y
> para lo que sirve de verdad —criterios subjetivos como tono o utilidad, donde no hay evaluator
> determinístico posible— es insustituible. Lo que no puede es sostener una nota, ni un informe a
> un cliente, sin decir su margen de error.

### Bloque 4 — cuándo una mejora es real

```
   v1: 24/30 = 80.0 %
   v2: 26/30 = 86.7 %        ¿mejoró?   ── depende ──►  ¿se corrió dos veces?
                                                        ¿los 2 casos ganados son
                                                        siempre los mismos?
```

Con 30 casos, **dos aciertos de diferencia pueden ser ruido.** La regla del curso: una mejora se
reporta cuando se sostiene en dos corridas y se puede señalar **qué cambio la produjo**. Si no se
sabe qué la causó, no es una mejora: es una casualidad que todavía no falla.

---

## 6. Las 4 demos · `code/`

| Archivo | Qué demuestra |
|---|---|
| `01_dataset_langfuse.py` | Subir los 30 casos del track a Langfuse Datasets |
| `02_evaluators.py` | Los 3 evaluators determinísticos corriendo sobre una respuesta |
| `03_llm_as_judge.py` | El juez sobre 10 casos ya puntuados, con las dos columnas lado a lado |
| `04_ab_prompts.py` | El mismo dataset contra dos versiones del prompt, con la tabla de salida |

---

## 7. Laboratorio L10

| Parte | Min | Qué hace el alumno |
|---|---|---|
| 1 | 25 | Cargar sus 30 casos en Langfuse Datasets |
| 2 | 25 | Correr la línea base **v1** y registrar las 3 métricas |
| 3 | 40 | Aplicar **un** cambio dirigido a uno de los cuellos del L9 |
| 4 | 30 | Correr **v2**, comparar y decidir si se conserva |

### El cambio de la parte 3

Debe ser **uno solo y trazable a un cuello del Avance 2**. Ejemplos por cuello:

| Cuello hallado en el L9 | Cambio típico en el L10 |
|---|---|
| El retriever se llama siempre | Escribir el "cuándo NO" en su docstring |
| Dos tools se confunden | Separar ambas docstrings (es lo que dice la matriz) |
| El historial dispara el costo | Recortar o resumir el historial |
| Reintentos frecuentes de extracción | Partir el esquema en dos, o añadir few-shot |

> **Un cambio por medición.** Si el equipo cambia tres cosas a la vez y mejora, no sabe cuál sirvió
> — y en la siguiente iteración no sabrá qué conservar. Es la disciplina que se está enseñando, más
> que el resultado.

### Entregables

| Entregable | Ruta |
|---|---|
| `evals/dataset.py` y `evals/evaluadores.py` | repo del equipo |
| Dataset de 30 casos visible en Langfuse | proyecto del equipo |
| `INFORME-L10.md` con la tabla v1 vs v2 | `lab/<track>/` |
| **Avance 3 del M3** | `lab/<track>/avance-3-m3.md` |

### Criterio de aceptación

- Los **30 casos** corriendo en Langfuse Datasets con los 3 evaluators.
- **Mejora medible de v1 a v2**, con tabla comparativa por métrica.
- El informe **nombra el cambio** que produjo la mejora y el cuello del L9 que atacaba.
- Si v2 **no** mejoró: también se acepta, documentando la hipótesis y por qué se descartó. Un
  experimento negativo bien documentado vale lo mismo que uno positivo — y es más honesto que
  retocar el dataset hasta que salga bonito.

---

## 8. Qué **no** entra

| No entra | Va en |
|---|---|
| El cliente web y la demo final | S11 |
| RAGAS en profundidad | mención y enlace; complemento opcional |
| Evaluación en CI / pipeline automatizado | se menciona como cierre, no se implementa |
| Fine-tuning como vía de mejora | fuera del alcance; se trabaja con prompts y RAG |

---

## 10. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| v2 mejora 2 puntos y el equipo lo celebra | Ruido de muestreo con 30 casos | Correr otra vez. Es el bloque 4 |
| El juez aprueba todo | Autocomplacencia | Es el sesgo del bloque 3, visto en vivo |
| Groundedness = 100 % siempre | El evaluator comprueba que hay cita, no que la sostenga | Revisar el evaluator: es el error más común |
| Se cambiaron 3 cosas y mejoró | No se sabe cuál sirvió | Revertir dos y volver a medir |
| Se agotaron las unidades de Langfuse | La S9 consumió más de lo previsto | Reducir a 15 casos por corrida y documentarlo |
