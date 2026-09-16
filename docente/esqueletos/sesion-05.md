# Esqueleto · Sesión 5 — Memoria contextual y RAG con Qdrant Cloud

> Contrato de la sesión 5. Insumo de la sesión de Claude Code que escribe los archivos
> (pasos 4.6–4.10 del `ROADMAP.md`). No es material de alumno.
>
> Decidido con Javier el 2026-09-16 · Fase 4 · Módulo 2

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta destino | la que ya exista bajo `modulo-2-agentes-avanzados/` para la sesión 5 |
| Semana · día | Semana 3 · martes |
| Horas | **3.0 h teoría · 3.0 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (120 T / 50 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L5 · Memoria + RAG del dominio** |
| Hitos | **Avance 2** · **Qdrant operativo en todos los equipos** |
| Estado en el mapeo | `COMPLETA`, con sustitución de vector store |

> **Es la sesión con más teoría del Módulo 2 y la más frágil operativamente.** Depende de un
> servicio externo que cada equipo aprovisionó en la semana 0 y que hasta hoy no ha usado.

---

## 2. Bloqueante con fecha

| Qué | Quién | Para cuándo | Si falta |
|---|---|---|---|
| Cluster de Qdrant **Healthy** en cada equipo | Cada equipo | Lunes semana 3 | Sin L5. Y el L6 y el L7 se construyen sobre el agente con RAG: el daño se propaga 3 sesiones |
| **Colecciones de respaldo** `kb-<track>-respaldo` indexadas y en solo lectura | **Javier** | Lunes semana 3 | Un fallo de ingesta deja al equipo sin laboratorio |
| Embeddings de HF respondiendo (`check_stack` nº 6) | Cada equipo | Lunes semana 3 | No hay ingesta posible |

**Pase de entrada**, mismo patrón que Pydantic en la S2:

```powershell
python -m comun.check_stack
```

Comprobaciones **6 y 7 en verde** (embeddings y Qdrant) antes del martes. Quien falle, avisa el
lunes — no el martes a las 19:05.

### La colección de respaldo · decidido

> **El alumno indexa, pero hay red.** Indexar es la lección: chunking, embeddings, payload. Si la
> ingesta de un equipo falla, apunta `QDRANT_COLLECTION` a la colección de respaldo del docente y
> sigue el laboratorio; la parte de ingesta la recupera después con el checkpoint.

- Cuatro colecciones, una por track, en el cluster de Javier: `kb-telecomunicaciones-respaldo`,
  `kb-banca-respaldo`, `kb-retail-respaldo`, `kb-seguros-respaldo`.
- **Solo lectura** para los alumnos (API key de lectura del cluster).
- Se indexan con el **mismo** `ingest.py` que usarán los alumnos: si el respaldo se construye con
  otro código, deja de ser una red y pasa a ser una segunda versión que puede contradecir.

> Esto matiza D10 (Qdrant sin fallback) sin romperlo: **no hay fallback de tecnología** — sigue
> siendo Qdrant y solo Qdrant. Lo que hay es una colección alternativa dentro del mismo servicio.
> Anotarlo en `_memoria/DECISIONES.md` para que no se lea como una contradicción.

---

## 3. Objetivos de aprendizaje

1. Explicar qué es la memoria de un agente y cómo la implementa un `thread_id`.
2. **Defender** el tamaño de chunk de su track: qué se gana y qué se pierde al partir un documento.
3. Indexar un corpus en Qdrant Cloud: colección, vector, payload.
4. Distinguir **RAG tradicional** de **RAG agéntico** y decir cuándo conviene cada uno.
5. Hacer que el agente **cite la fuente**, y explicar por qué eso es un requisito de auditoría y
   no un adorno.

---

## 4. Pre-work · 1 h

| # | Concepto | Por qué |
|---|---|---|
| 1 | Similitud coseno, leída de nuevo con el ejemplo del track | Ya se vio en la S0; aquí se aplica |
| 2 | Chunking: por qué partir y qué se pierde al partir | Es la decisión que más afecta la calidad |
| 3 | Colección, punto, vector, **payload**, filtro por metadatos | Vocabulario de Qdrant |
| 4 | Verificación: `check_stack` nº 6 y 7 en verde | Pase de entrada |

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | El agente que no recuerda y el que no sabe | 5 | T | Dos carencias distintas, dos soluciones distintas |
| 1 | Estado conversacional y `thread_id` | 20 | T | El modelo es stateless: la memoria la implementa tu código |
| 2 | Embeddings aplicados al dominio | 15 | T | Dos preguntas del track sin palabras en común, cerca en el espacio |
| 3 | **Chunking y su trade-off** | 20 | T | Chunk grande: contexto sobrante. Chunk chico: contexto amputado |
| 4 | Qdrant: colección, punto, payload, filtros | 20 | T | El payload es lo que permite **citar** |
| 5 | **RAG tradicional vs RAG agéntico** | 25 | T | Buscar siempre vs decidir si buscar |
| 6 | **Salvaguarda A6 y la fundamentación** | 15 | T | Una respuesta sin fuente no es verificable |
| — | **Pausa** | 10 | — | |
| 7 | Laboratorio guiado: ingesta del corpus del track | 35 | P | De 3 `.md` a una colección consultable |
| 8 | Avance 2 del proyecto | 15 | P | Qué preguntas resuelve el RAG y cuáles las tools |

**Teoría 120 · práctica 50 · pausa 10** → con pre-work y lab: **3.0 h / 3.0 h** ✅

### Bloque 3 — chunking: parámetros **fijos**, decidido

El curso fija el tamaño y el solapamiento por track. El alumno entiende el compromiso y sabe
defenderlo, pero **no experimenta con él en el L5**.

| Track | `chunk_size` | `overlap` | Por qué ese valor |
|---|---|---|---|
| telecomunicaciones | 400 | 60 | Tarifario: entradas cortas, tabulares, autocontenidas |
| banca | 400 | 60 | Comisiones y límites: párrafos breves e independientes |
| retail | 350 | 50 | Fichas de producto y política de devoluciones: muy breves |
| seguros | **600** | **100** | Condicionado legal: una cláusula partida por la mitad pierde su sentido |

| Si el chunk es… | Ventaja | Problema |
|---|---|---|
| Muy pequeño (~150) | Recuperación muy precisa | La cláusula queda amputada: el modelo lee media condición |
| Equilibrado (350-600) | — | — |
| Muy grande (~1500) | Nunca parte una idea | Cada resultado arrastra ruido, y se paga en tokens **en cada llamada** |

> **Por qué se fijan y no se experimentan.** Re-indexar consume cuota de embeddings, y los riesgos
> **R2 y R18 siguen sin verificar**. Con 15 equipos, un experimento de dos configuraciones duplica
> el consumo en la semana más cargada del curso. Quien quiera optimizar el chunking lo hace en el
> **proyecto M2 (S7)**, donde hay tiempo de clínica y el equipo decide dónde invertir.

⚠️ Estos valores son una **propuesta razonada, no medida**. Tarea previa: indexar una vez cada
corpus, anotar cuántos chunks produce y ajustar si alguno queda absurdo.

### Bloque 5 — el cuadro que estructura la sesión

```
   RAG TRADICIONAL                      RAG AGÉNTICO
   ──────────────                       ────────────
   pregunta                             pregunta
      │                                    │
      ▼                                    ▼
   SIEMPRE busca                     ¿necesito buscar?  ── no ──► responde
      │                                    │ sí
      ▼                                    ▼
   pega los fragmentos                 llama al retriever como TOOL
      │                                    │
      ▼                                    ▼
   responde                            responde CITANDO
```

| | Tradicional | Agéntico |
|---|---|---|
| Latencia | Fija, siempre paga la búsqueda | Variable: no busca si no hace falta |
| "Hola, buenos días" | Busca igual: gasta y ensucia el contexto | No busca |
| Control | Total: siempre hay contexto | El agente **puede** decidir mal |
| Defensa cuando decide mal | — | **La salvaguarda A6** |

### Bloque 6 — A6 no es paranoia, es auditoría

El system prompt de las 4 industrias ya lleva el bloque *recuperación obligatoria*
(`comun/prompts_industria.py`). La regla:

> Ante cualquier afirmación sobre **tarifas, coberturas, plazos o políticas**, el agente debe
> recuperar y citar. Si no encuentra fuente, dice que no lo sabe.

Y el motivo, que es el que hay que enseñar: **una respuesta sin fuente no se puede auditar.** En
telco el regulador pregunta de dónde salió esa tarifa; en seguros, de dónde salió esa cobertura.
"El modelo lo dijo" no es una respuesta admisible.

---

## 6. Las demos · `code/`

| Archivo | Qué demuestra |
|---|---|
| `01_ingesta.py` | Cargar los 3 `.md` del track, partirlos, embeberlos e indexarlos |
| `02_similitud.py` | Las mismas preguntas del track contra la colección, con su puntaje |
| `03_rag_tradicional.py` | Buscar siempre y pegar el contexto |
| `04_rag_agentico.py` | El retriever como **tool**: el agente decide |
| **`demo-parametrico-vs-recuperable.py`** | **La demo clave del curso** (paso 4.9) |

### La demo clave, paso a paso

```
   1.  Preguntar: "¿cuánto cuesta el plan Max 89?"      → responde citando el tarifario
   2.  EDITAR el documento en Qdrant: el plan sube a 99
   3.  Preguntar lo mismo                               → responde 99, citando el mismo documento
   4.  La pregunta al aula: ¿qué habría hecho falta para cambiar eso
       si el precio estuviera en los pesos del modelo?
```

Es la demostración física de por qué el conocimiento va al RAG y no al fine-tuning (D21). Dura
5 minutos y sostiene una decisión de arquitectura del curso entero. **No la recortes.**

---

## 7. Laboratorio L5 · Memoria + RAG del dominio

### Incremento sobre el L4

| Archivo nuevo | Qué hace |
|---|---|
| `knowledge/ingest.py` | Carga, chunking, embeddings e indexación en Qdrant |
| `knowledge/retriever.py` | El retriever expuesto como **tool** (RAG agéntico) |
| `memory.py` | Estado conversacional por `thread_id` |
| `agent.py` v3 | Las 4 tools + el retriever + memoria |

### El corpus por track

Los 3 `.md` que ya existen en `recursos/datasets/<track>/`. No se escriben corpus nuevos.

### Criterio de aceptación

- El agente **decide** cuándo buscar: una pregunta de saludo no dispara el retriever.
- **10 preguntas con cita verificable**: la respuesta nombra el documento del que salió.
- La memoria funciona: el turno 3 entiende "¿y el mes pasado?" sin repetir el número de línea.

### De dónde salen las 10 preguntas

Del mismo `recursos/golden/consultas-<track>.json` del L2 y el L4: las consultas etiquetadas
**`OTRO`** son exactamente las de tarifas, coberturas y políticas — las que van a RAG.

```
   golden/consultas-<track>.json
         │
         ├── categorías de tool  ──►  L2 clasifica · L4 selecciona
         └── categoría OTRO      ──►  L5 recupera y cita
```

> ⚠️ Hoy hay **4 consultas `OTRO` por track** y el criterio pide 10. Tarea previa: subirlas a 10
> por track en el mismo archivo. Son preguntas sobre el corpus que ya existe, así que se escriben
> leyendo los 3 `.md` del track.

**Reto opcional:** filtro por metadatos en el payload (por ejemplo, recuperar solo del tarifario
vigente y no del histórico).

---

## 8. Qué **no** entra

| No entra | Va en |
|---|---|
| Guardrails, PII, prompt injection | S6 |
| Pruebas de estrés y casos borde | S7 |
| Métricas de groundedness | S10 |
| Reindexación automática y pipelines de ingesta | fuera del curso |

> La S5 hace que el agente **cite**. Medir si la cita realmente sostiene la respuesta —
> *groundedness*— es la S10. Decirlo evita que el alumno intente evaluar hoy lo que aún no sabe medir.

---

## 9. Los archivos a producir

| # | Archivo | Contenido pactado |
|---|---|---|
| **4.6** | `README.md` | Bloques 0 a 6, con el cuadro tradicional vs agéntico |
| **4.7** | `conceptos-previos.md` | Coseno, chunking, vocabulario de Qdrant, pase de entrada |
| **4.8** | `code/` | Las 4 demos + `README.md` |
| **4.9** | `demo-parametrico-vs-recuperable.py` | La demo clave, con guion para el docente |
| **4.10** | `lab/` + `solucion/` | L5 × 4 tracks |

### Trabajo previo

| # | Tarea | Por qué |
|---|---|---|
| a | Subir a **10** las consultas `OTRO` por track en `recursos/golden/` | El criterio pide 10 y hoy hay 4 |
| b | Indexar las 4 colecciones de respaldo con el mismo `ingest.py` | Es la red de seguridad decidida |
| c | Anotar en `_memoria/DECISIONES.md` que la colección de respaldo **no** contradice D10 | Mismo servicio, otra colección |

---

## 10. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| La ingesta falla a mitad | Cuota de embeddings de HF agotada | Colección de respaldo, y retomar la ingesta después |
| El agente busca ante "hola" | El retriever no tiene "cuándo NO" en su docstring | A2 aplicada al retriever |
| El agente nunca busca | El system prompt no lleva el bloque A6 | Usar `get_system_prompt(track)`, no un prompt propio |
| Cita el documento equivocado | Chunks demasiado grandes | Es el trade-off del bloque 3: reducir y volver a medir |
| Responde sin citar | Falta la instrucción de formato en el prompt | Rol + Contexto + Tarea + **Formato**, de la S2 |
| El turno 3 no recuerda | Falta `thread_id` o se genera uno nuevo por turno | Revisar `memory.py` |
