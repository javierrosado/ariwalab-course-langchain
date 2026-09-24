# Esqueleto · Sesión 4 — Tools e integración de herramientas

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-2-agentes-avanzados/sesion-04-tools-multiples/` |
| Semana · día | Semana 2 · jueves |
| Horas | **2.5 h teoría · 3.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (90 T / 80 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L4 · Catálogo de 4 tools** |
| Hitos | Sustentación del **A1** (4 equipos, 20 min) · **Avance 1 del proyecto** |

> **Ojo con el arranque.** Los primeros 20 min son la sustentación del A1 descrita en la S3. El
> guion de abajo empieza *después* de esos 20 min, así que el bloque de contenido son 160 min y no
> 180. Está descontado del bloque 5.

---

## 2. Objetivos de aprendizaje

1. Diseñar un catálogo de tools con **responsabilidad única**: una tool, una pregunta.
2. Explicar por qué la precisión de selección cae al pasar de 4 herramientas, y por qué eso se
   agrava a lo largo del bucle.
3. **Medir** el acierto de selección de su propio agente y leer una matriz de confusión.
4. Distinguir una tool **idempotente** de una que no lo es, y proteger la segunda.
5. Conectar el agente a un servidor **MCP** y explicar qué cambia y qué no.

---

## 3. Con qué llega el alumno

**Pre-work de 1 h — MCP: conectarse, no construir.**

| # | Contenido | Tiempo |
|---|---|---|
| 1 | Qué es MCP y qué problema resuelve: un protocolo, no una librería | 15 min lectura |
| 2 | `simulador-industria/docs/GUIA-MCP.md`: los dos transportes (stdio y HTTP) | 15 min lectura |
| 3 | **Conectar el agente al servidor MCP del simulador** con `langchain-mcp-adapters` | 30 min práctica |

> **Por qué conectarse y no construir.** El simulador ya expone 6 tools por MCP, con su guía
> escrita y los dos transportes funcionando. Construir un servidor propio no cabe en 1 h para
> alguien que escribió su primera tool hace dos días. Y la lección central de MCP se aprende
> igual conectándose: **el agente no nota la diferencia** — mismas tools, distinto transporte.
>
> Construir un servidor MCP con 2 tools propias queda como **reto del L4**, no como requisito.

---

## 4. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| — | **Sustentación del A1** | 20 | — | 4 equipos, uno por track, 5 min cada uno |
| 0 | De una tool a cuatro | 5 | T | Qué se rompe al añadir herramientas |
| 1 | Catálogo y **responsabilidad única** | 20 | T | Una tool, una pregunta. La tool que hace dos cosas nunca se elige bien |
| 2 | **Selección dinámica: cómo elige y por qué falla** | 25 | T | El modelo solo lee nombres y docstrings. Tipos de confusión |
| 3 | **Por qué 4 y no 6** (regla A1) | 20 | T | Fiabilidad compuesta: 93 % por llamada = 80 % en 3 pasos |
| 4 | **Idempotencia y tope de iteraciones** (regla A4) | 20 | T | Leer es reintentable; escribir no. El bucle que no termina |
| — | **Pausa** | 10 | — | |
| 5 | Laboratorio guiado: completar el catálogo | 45 | P | Las 4 tools núcleo del track |
| 6 | **Medir**: correr la matriz de selección propia | 25 | P | Leer la matriz de confusión y corregir una docstring |
| 7 | Avance 1 del proyecto | 10 | P | Caso de uso y herramientas necesarias, por escrito |

**Teoría 90 · práctica 80 · pausa 10 = 180 min de S4.** Los 20 min del A1 **no caben dentro**
de esos 180: sumarían 200.

> **Preparación del horario:** la sustentación A1 requiere 20 minutos además de los 180
> del guion S4. Confirmar con coordinación académica una franja compatible y comunicarla
> antes de clase; no anunciar que ambas actividades caben en tres horas.

### Bloque 2 — los tres tipos de confusión

```
   El modelo NO ve tu código. Ve esto:

      [ nombre de la tool ]  +  [ docstring ]  +  [ esquema de argumentos ]

   Y con eso decide. Cuando falla, falla de tres maneras:

   ┌─ SOLAPAMIENTO ── dos docstrings describen el mismo caso
   │                  → escribir en cada una "cuándo NO"
   ├─ VACÍO ───────── ninguna docstring describe la pregunta
   │                  → el modelo elige la menos mala, o no llama a nada
   └─ SOBRE-USO ───── llama a una tool cuando no debía llamar a ninguna
                      → falta el límite: tarifas y políticas van a RAG (S5)
```

Cada tipo tiene su celda en la matriz de confusión y su corrección distinta. Es el contenido que
el bloque 6 pone en práctica.

### Bloque 4 — idempotencia, en una tabla

| Tool | ¿Idempotente? | Qué pasa si se reintenta | Protección |
|---|---|---|---|
| `get_customer_plan` | Sí | Nada: misma respuesta | Ninguna |
| `get_account_balance` | Sí | Nada | Ninguna |
| `create_complaint_ticket` | **No** | **Dos reclamos duplicados** | Confirmación explícita antes de llamar |
| `open_claim` | **No** | Dos expedientes del mismo siniestro | Confirmación explícita |

> Es la primera vez que el alumno escribe una tool que **modifica algo**. La regla: toda tool de
> escritura exige confirmación del usuario antes de ejecutarse, y eso se implementa en el L4, no
> se posterga a los guardrails de la S6.

---

## 5. Las 3 demos · `code/`

| Archivo | Qué demuestra | Qué debe notar el alumno |
|---|---|---|
| `01_multi_tool.py` | Un agente con las 4 tools del track | Que el agente elige distinto según cómo se formule la pregunta |
| `02_matriz_didactica.py` | 5 consultas y su matriz, en 30 segundos | La versión corta de `docente/matriz_seleccion.py`, para entender la lectura |
| `03_tope_iteraciones.py` | El mismo agente con y sin tope, ante un `?_fallo=error503` | Sin tope, el agente reintenta hasta agotar la cuota. Con tope, avisa y para |

Más `pre-work-mcp.md` como material asíncrono.

---

## 6. Laboratorio L4 · Catálogo de 4 tools

**Objetivo:** que el agente elija bien entre cuatro herramientas, y que el alumno lo **mida**.

| Track | Las 4 tools núcleo |
|---|---|
| telecomunicaciones | `get_customer_plan` · `get_data_usage` · `run_line_diagnostics` · `create_complaint_ticket` |
| banca | `get_account_balance` · `list_transactions` · `get_card_info` · `score_transaction_risk` |
| retail | `track_order` · `get_product_details` · `check_stock_by_store` · `start_return_request` |
| seguros | `get_policy_by_plate` · `quote_soat` · `get_claim_status` · `open_claim` |

La primera ya está escrita: es la del L3. El L4 añade las otras tres, **una de ellas de escritura**.

### Criterio de aceptación

- **≥ 85 % de selección correcta** en `docente/matriz_seleccion.py` sobre su propio catálogo.
- La tool de escritura **no se ejecuta sin confirmación**.
- Hay tope de iteraciones y los errores están redactados para el modelo (A4, heredado del L3).

### Medir el catálogo del equipo

```
   docente/matriz_seleccion.py --track <suyo> --tools lab/<track>/domain_tools.py

        20 consultas ──► matriz de confusión ──► "corrige la docstring de X"
```

> Usar `--tools <ruta>` para medir el catálogo del equipo. La ruta por defecto mide el
> catálogo de referencia del curso y no acredita el trabajo del alumno.

### Catálogo de referencia y proyecto del equipo

`proyecto-final/<track>/` contiene las tools de referencia que usan los verificadores.
Cada equipo implementa su agente en su propio repositorio, del L1 al L11. Los checkpoints
en `solucion/<track>/` permiten comparar el trabajo después de intentar cada práctica.

**Reto opcional:** las 2 tools opcionales del track, y exponer 2 de las propias como servidor MCP.

---

## 7. Avance 1 del proyecto

Media página por equipo, entregada al cerrar la sesión:

1. El caso de uso concreto que resuelve su agente, en una frase.
2. Las 4 tools y **por qué esas cuatro y no otras**.
3. Qué preguntas del cliente **no** resuelve ninguna tool — y qué se hará con ellas (respuesta:
   RAG, en la S5).

El punto 3 es el que prepara la S5: el alumno descubre el hueco antes de que se lo llenen.

---

## 8. Qué **no** entra

| No entra | Va en |
|---|---|
| RAG, embeddings, Qdrant | S5 |
| Memoria conversacional | S5 |
| Guardrails, PII, prompt injection | S6 |
| Construir un servidor MCP propio | reto opcional |
| Langfuse | S9 |

---

## 10. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| Acierto < 85 % concentrado en dos tools | Docstrings que se solapan | Escribir "cuándo NO" en ambas. Es la lección |
| El agente llama a una tool ante una pregunta de tarifas | Falta el límite | Anticipa la S5: eso va a RAG. Añadirlo a la docstring |
| Dos reclamos duplicados | La tool de escritura se ejecutó sin confirmación | Es el bloque 4: implementar la confirmación |
| El agente agota la cuota de HF | Bucle sin tope ante un 5xx | Tope de iteraciones (A4) |
| MCP no conecta | Transporte mal elegido o URL del Space | `GUIA-MCP.md` §transportes |
