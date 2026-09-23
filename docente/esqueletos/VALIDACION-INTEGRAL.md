# Validación integral del curso

> **Qué es.** La revisión de coherencia entre las 13 piezas del curso: 11 sesiones, el Seminario
> Internacional y el bonus de Foundry. Comprueba que formen **un curso**, y no trece diseños
> independientes que coinciden en la misma carpeta.
>
> Ejecutada el 2026-09-16, después de pactar el último esqueleto.

---

## 1. Cómo se valida

La validación tiene dos mitades, y la división importa:

| Mitad | Instrumento | Qué comprueba |
|---|---|---|
| **Mecánica** | `python docente/validar_coherencia.py` | Horas, guiones, referencias, laboratorios, tareas, herramientas, bloqueantes. 10 familias de comprobación, determinista, sin credenciales |
| **Pedagógica** | Este documento | Si un concepto se enseña antes de usarse, si la narrativa se sostiene, si hay huecos o duplicados. **No se puede automatizar: se revisa leyendo** |

**Resultado de la mitad mecánica, hoy:**

```
   COHERENCIA VERIFICADA · 1 aviso
   13 de 13 esqueletos · 72.0 h · 40.3 % teoría / 59.7 % práctica
```

El único aviso es el descuadre de 20 min de la S4, marcado como `DECISION-PENDIENTE` a la espera
de Javier. **Re-ejecutar el script tras cualquier cambio en un esqueleto**: es barato y detecta en
segundos lo que a ojo se pasa.

---

## 2. Los seis arcos que atraviesan el curso

Un curso es coherente cuando lo que se construye en una sesión se consume en la siguiente. Estos
son los hilos que hay que poder seguir de principio a fin.

### 2.1 · La cadena de laboratorios

```
   L1  entorno ─► L2  clasificador ─► L3  primera tool ─► L4  catálogo de 4
        │                                                       │
        └───────────────── mismo repositorio ───────────────────┤
                                                                ▼
   L8  desplegado ◄─ L7  endurecido ◄─ L6  guardrails ◄─ L5  memoria + RAG
        │
        ▼
   L9  trazado ─► L10  evaluado ─► L11  entregado ─► L12  en Foundry (bonus)
```

✅ **Verificado.** Cada laboratorio consume la salida del anterior y ninguno parte de cero. El
único que podría hacerlo —el L1— está diseñado a propósito como entorno, no como código.

### 2.2 · El golden set

El hilo más fuerte del curso, y el que más tarde se revela:

| Sesión | Uso de `recursos/golden/consultas-<track>.json` |
|---|---|
| S2 · L2 | Clasificar intención · 20 consultas |
| S4 · L4 | Seleccionar herramienta · las mismas 20 |
| S5 · L5 | Recuperar y citar · las 10 de categoría `OTRO` |
| S9 · L9 | Generar tráfico real contra el Space desplegado |
| S10 · L10 | **Dataset de evaluación en Langfuse: los 30 juntos** |

✅ **Verificado, con una corrección pendiente** (ver §3, hallazgo H5).

### 2.3 · Las reglas A1–A6

| Regla | Se nombra | Se aplica | Se **mide** |
|---|---|---|---|
| A1 · máximo 4 tools | S1 | S4 | `matriz_seleccion.py` (S4, S10) |
| A2 · docstring con "cuándo NO" | S1 | S3 | `matriz_seleccion.py` |
| A3 · structured output validado | S1 | S2, **S4, S10** | `verificar_structured.py` |
| A4 · tope de iteraciones y errores legibles | S1 | S3, S4 | — |
| A5 · few-shot | S1 | S2 | — |
| A6 · recuperación obligatoria | S1 | S5 | groundedness (S10) |

⚠️ **Dos reglas se enuncian y luego desaparecen** (ver §3, hallazgos H1 y H2). **Una tercera se
enuncia y se queda en un solo uso** (ver §3, hallazgo H7 — ya corregido).

### 2.4 · El simulador de industria

| Sesión | Uso |
|---|---|
| S3 | Primera tool contra `/telco/clientes/...`. Los 3 escenarios con `?_fallo=` |
| S4 | Las 4 tools núcleo, incluida la primera de escritura. MCP sobre el mismo servicio |
| S5 | Sigue sirviendo datos mientras el RAG sirve documentos |
| S7 | **`CHAOS_RATE=0.1`**: el simulador se vuelve el adversario del hackathon |
| S8-S11 | El agente desplegado lo sigue consumiendo desde el Space |

✅ **Verificado.** El simulador aparece en la S3 y no desaparece nunca. La decisión de que sea un
solo servicio con tres superficies (REST, SQL, MCP) se paga sola en la S4.

### 2.5 · Los verificadores

Cada criterio que dice "≥ X %" tiene un script detrás. Es lo que impide que un criterio sea una opinión:

| Criterio | Script | Sesión |
|---|---|---|
| Las 24 tools corren | `verificar_tools.py` | interno |
| Structured output con reintento | `verificar_structured.py` | S2 |
| ≥ 90 % de clasificación | `medir_clasificador.py` | S2 |
| ≥ 85 % de selección de tool | `matriz_seleccion.py` | S4 |
| 0 filtraciones en 15 ataques | `verificar_guardrails.py` | S6 |
| Despliegue accesible y autenticado | `verificar_despliegue.py` | S8 |
| Coherencia entre sesiones | `validar_coherencia.py` | interno |

✅ **Verificado.** Siete instrumentos para siete criterios. Ninguno depende de credenciales salvo
los tres que necesariamente las requieren.

### 2.6 · La evaluación

| Instrumento | Sesión | Peso | Criterios de la rúbrica que aplican |
|---|---|---|---|
| Test 1 | S1 | formativo | — |
| Test 2 | S2 | formativo | — |
| **Assignment A1** | S3 → sustenta en S4 | 100 % M1 | 4 de 5 (observabilidad no aplica) |
| **Proyecto M2** | S7 | 100 % M2 | 4 de 5 (observabilidad no aplica) |
| **Proyecto Integrador** | S11 | 100 % M3 | **los 5** |
| Contraste del seminario | seminario | formativo | — |
| Bonus Foundry | asíncrono | no ponderado | — |

✅ **Verificado.** El criterio de observabilidad solo aplica cuando ya se enseñó (S9), y está
anotado como tarea previa *g*.

---

## 3. Hallazgos

Ordenados por lo que cuesta arreglarlos después.

### H1 · La regla A5 (few-shot) se enuncia y nunca vuelve — **alto**

El plan curricular declara que A5 aplica en **L2, L4 y L6**. En los esqueletos aparece solo en la
S2. Las sesiones 4 y 6 no mencionan few-shot ni una vez.

| Dónde falta | Qué debería decir |
|---|---|
| S4 | Los ejemplos few-shot en el system prompt mejoran la **selección** entre tools parecidas. Es una palanca más, junto a la docstring |
| S6 | Los ejemplos de ataques bloqueados en el prompt son la primera capa del guardrail, antes del código |

**Corrección:** añadir un párrafo a cada esqueleto, o quitar A5 de la lista de reglas del plan. Lo
que no puede quedar es una regla enunciada en la S1 que el alumno nunca ve aplicada.

### H2 · La regla A4 no se mide en ningún sitio — **medio**

A1, A2, A3 y A6 tienen instrumento. A4 —tope de iteraciones y errores redactados para el modelo—
se enseña en la S3 y la S4 y **no se comprueba nunca**. El L7 lo roza al probar con caos, pero sin
criterio explícito.

**Corrección:** añadir al criterio del L7 una comprobación concreta: *el agente, ante `?_fallo=error503`
sostenido, termina en ≤ N iteraciones y emite un mensaje al usuario*. Es una línea en el enunciado.

### H3 · El streaming se exige sin haberse enseñado — **medio**

`streaming` aparece en la S8 y en la S11 —donde el L11 **exige** un cliente web con streaming— pero
no se enseña en ninguna sesión. El mapeo lo listaba como "adición del repo" para la S2, y ahí quedó
como material asíncrono opcional.

**Corrección, tres opciones:** (a) incluirlo en el pre-work de la S11, que hoy ya lo menciona como
concepto previo pero sin material propio; (b) convertirlo en reto opcional del L11 y aceptar un
cliente sin streaming; (c) subirlo a demo de la S8, donde ya hay una capa HTTP.
**Recomendada: la (a)**, con un ejemplo funcional en el pre-work.

### H4 · LangGraph se promete en el plan y desaparece — **medio**

`prerrequisitos-por-sesion.md` y el plan curricular incluyen *"cuándo pasar a LangGraph"* como
contenido de la S6. El esqueleto de la S6 no lo menciona, y el Seminario —que era el otro lugar
natural— quedó como panel de industria.

**Corrección:** o se añade un bloque de 10 min al final de la S6 (*"esto ya no cabe en un agente:
cuándo pasar a un grafo"*), o se elimina la promesa del plan y de los prerrequisitos. **Recomendada:
el bloque de 10 min**, porque la pregunta la va a hacer alguien del aula igual, y responderla mal
en el momento es peor que tener la diapositiva.

### H5 · La S4 no nombra el archivo del golden set — **bajo**

La S4 habla de "las 20 consultas" y del script que las lee, pero no menciona
`recursos/golden/consultas-<track>.json`. Como el archivo se crea en la tarea previa *a*, conviene
que la S4 lo nombre para que la cadena sea visible también ahí.

### H6 · El descuadre de 20 min de la S4 — **pendiente de decisión**

La sustentación del A1 ocupa 20 min y el guion de la S4 ya suma 180. Están las tres salidas en
`sesion-04.md` §5, marcadas con `DECISION-PENDIENTE`. **Lo decide Javier.**

### H7 · `comun/structured.py` (regla A3) se usa solo en el L2 — **medio · corregido 2026-09-17**

La regla A3 se enuncia en la S1, se aplica en la S2 (`extraer()` para clasificar intención) y no
vuelve a aparecer en ningún otro laboratorio ni demo — ni siquiera en el L10, cuya sesión entera
trata sobre por qué `assert respuesta == "esperado"` no sirve y cómo medir con criterio, lo que
la hace el lugar más contradictorio posible para saltarse la validación estructurada. El L4
tampoco la usa: sus 3 tools de escritura (`create_complaint_ticket`, `start_return_request`,
`open_claim`) validaban su campo de enum con un `if valor not in {...}` escrito a mano, en vez de
con el módulo que el curso ya enseña para exactamente ese problema.

**Corrección aplicada:**

| Dónde | Qué cambió |
|---|---|
| `modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/03_llm_as_judge.py` | El juez ya no devuelve `"SI"`/`"NO"` en texto libre parseado a mano: responde con un esquema `Veredicto` (`aprueba: bool`, `motivo: str`, `confianza: Enum`) extraído con `extraer()`. Un juez sin validar habría contradicho la lección de la propia sesión |
| `domain_tools.py` de telecomunicaciones, retail y seguros (L4) | La tool de escritura de cada track normaliza su enum (`tipo`, `tipo_solucion`) con `extraer()` **antes** de pedir confirmación — no tiene sentido confirmarle al cliente una acción cuyo tipo todavía no se sabe si es válido |
| `domain_tools.py` de banca (L4) | Nota explícita: no aplica, porque el track no tiene ninguna tool de escritura en su núcleo (decisión ya documentada en el `README.md` de la S4) |

**Por qué no se corrigió también añadiendo A3 a más lugares.** El objetivo no es maximizar cuántas
veces aparece `extraer()`, es cerrar los dos huecos que contradicen contenido que el curso mismo
enseña: un juez de la S10 sin validar, y una tool de escritura del L4 que ya tenía el problema
exacto que `comun/structured.py` resuelve (un enum que el modelo puede inventar) sin usar la
solución que el curso ya construyó para eso.

---

## 4. El calendario de bloqueantes

Todos los bloqueantes son de Javier, y hay uno por semana. Vistos juntos, es la lista más
accionable de todo este documento:

| Vence | Qué | Bloquea | Riesgo |
|---|---|---|---|
| Antes de construir | `matriz_seleccion.py` contra el endpoint real | El criterio del L4 | R11 |
| **Lunes semana 2** | Simulador en HF Spaces + API keys por equipo | **S3, y la nota del M1** | R14 |
| **Lunes semana 3** | Cluster de Qdrant por equipo | **S5, y todo lo que sigue** | R4 · sin fallback (D10) |
| Semana 3 | Convocar 3 panelistas | Seminario | — |
| **Antes de semana 4** | Límites del free tier de HF Spaces | S8 | **R5, sin verificar** |
| **Lunes semana 5** | Proyecto de Langfuse por equipo | S9 y S10 | — |
| Antes del bonus | Re-verificar `langchain-azure-ai[hosting]` | Bonus pasos 6-7 | **R8, es preview** |

> **Los tres en negrita son los que no tienen plan B.** Qdrant no tiene fallback por decisión D10;
> el simulador lo tiene (`DATA_SOURCE=csv`) pero degradado; y el free tier de Spaces no se ha
> medido nunca.

---

## 5. Lo que queda fuera, a propósito

No es un hueco si está decidido. Se lista para que nadie lo "arregle" por error:

| Fuera | Por qué |
|---|---|
| Docker en local, Kubernetes, CI/CD | Principio P2: nada corre en local |
| Fine-tuning | Decisión D21 · camino A. Se explica por qué, no se hace |
| Escribir un servidor MCP | Reto opcional: no cabe en 1 h de pre-work |
| Re-ranking, búsqueda híbrida | Fuera del alcance de una primera edición |
| Azure más allá del modelo | Curso 2 |
| Experimentar con el chunking | Cuota de embeddings. Se traslada al proyecto M2 |

---

## 6. Veredicto

| Dimensión | Estado |
|---|---|
| Horas, balance y malla | ✅ 72 h · 40.3 / 59.7 · sin cambios académicos |
| Cadena de laboratorios | ✅ Incremental de L1 a L12 |
| Hilos transversales | ✅ Golden set, simulador y verificadores atraviesan el curso |
| Reglas de diseño A1–A6 | ✅ **H1, H2 y H7 corregidos** — A5 aplicado en S4/S6, A4 medido en el L7, A3 usado más allá del L2 |
| Contenido prometido | ✅ **H3 y H4 corregidos** — streaming en la S11, mención de LangGraph en la S6 |
| Referencias entre sesiones | ✅ Ninguna apunta hacia atrás |
| Evaluación | ✅ Cubierta, con la observabilidad acotada a partir de la S9 |
| Bloqueantes | ⚠️ Siete, todos de Javier, tres sin plan B |

**El curso es coherente.** Los siete hallazgos son de contenido, no de arquitectura: ninguno
obligó a rediseñar una sesión. De los siete, seis (H1 a H5 y H7) ya están corregidos; **H6 sigue
pendiente de decisión de Javier**, como corresponde a un `DECISION-PENDIENTE` que no le toca
resolver a quien escribe el contenido.

**Orden recomendado (histórico):** corregir H1 y H2 antes de construir el Módulo 2 —porque
afectan a los enunciados de los laboratorios L4 y L6—, y H3 y H4 antes del Módulo 3. **Cumplido**:
H1-H4 se corrigieron durante la construcción del Módulo 2 y el Módulo 3; H5 durante el cierre del
hueco de la S2-S3; H7 se detectó y corrigió después, con el curso ya completo. Solo H6 permanece
abierto, sin afectar la construcción de ninguna sesión.
