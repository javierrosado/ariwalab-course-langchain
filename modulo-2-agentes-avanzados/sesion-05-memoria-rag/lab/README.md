# Laboratorio L5 · Memoria + RAG del dominio

**Objetivo:** que tu agente responda con la documentación real de tu industria y recuerde la
conversación. Incremento sobre el L4:

| Archivo nuevo | Qué hace |
|---|---|
| `knowledge/ingest.py` | Carga, chunking, embeddings e indexación en Qdrant Cloud |
| `knowledge/retriever.py` | El retriever expuesto como **tool** (RAG agéntico) |
| `memory.py` | Estado conversacional por `thread_id` |
| `agent.py` (v3) | Tus 4 tools del L4 + el retriever + memoria |

**Duración:** 2 h.

---

## Parte 1 · Ingesta (35 min guiados)

1. Copia `solucion/<tu-track>/knowledge/ingest.py` como punto de partida a
   `lab/<tu-track>/knowledge/ingest.py` — **léelo primero**, no lo ejecutes a ciegas: entiende
   qué hace cada paso (cargar, trocear, indexar).
2. Ejecútalo una sola vez:
   ```bash
   python lab/<tu-track>/knowledge/ingest.py
   ```
3. Si tu ingesta falla (cuota de embeddings, Qdrant caído), apunta `QDRANT_COLLECTION` en tu
   `.env` a la colección de respaldo del docente (`kb-<tu-track>-respaldo`, solo lectura) y sigue
   el resto del laboratorio. Retoma tu propia ingesta después con el checkpoint.

## Parte 2 · El retriever como tool

Escribe `knowledge/retriever.py`: una función decorada con `@tool` que busca en tu colección y
devuelve los fragmentos con su fuente. La docstring debe decir, como toda tool (regla A2):
**cuándo** usarla (tarifas, coberturas, plazos, políticas) y **cuándo NO** (cualquier pregunta
que ya resuelve una de tus 4 tools del L4).

## Parte 3 · Memoria

Escribe `memory.py`: un almacén de historial por `thread_id` (en memoria de proceso alcanza para
el curso). Tu `agent.py` debe usar el mismo `thread_id` durante toda una conversación y uno nuevo
por cada conversación distinta.

## Parte 4 · Ensambla `agent.py` v3

Une tus 4 tools del L4 + el retriever + la memoria, con el mismo bucle de tope de iteraciones que
ya conoces. El system prompt sigue siendo `get_system_prompt(tu_track)` — no escribas uno propio:
ahí vive la salvaguarda A6 (recuperación obligatoria).

## Parte 5 · Avance 2 del proyecto (15 min, en la sesión en vivo)

Media página: qué preguntas resuelve tu RAG y cuáles siguen resolviendo tus tools — la línea
divisoria debe quedar clara para cualquiera que lea tu proyecto.

---

## Las 10 preguntas de cita verificable

Salen de `recursos/golden/consultas-<tu-track>.json`, categoría `"otro"` (son exactamente las
que en el L2 y el L4 el modelo NO debía resolver con ninguna tool — hoy sí las resuelve, con RAG).

## Criterio de aceptación

- El agente **decide** cuándo buscar: una pregunta de saludo no dispara el retriever.
- **10 preguntas con cita verificable**: la respuesta nombra el documento del que salió.
- La memoria funciona: el turno 3 entiende "¿y el mes pasado?" sin que repitas el identificador.

## Reto opcional · no evaluado

Filtro por metadatos en el payload (por ejemplo, recuperar solo del documento vigente y no de uno
histórico, si tu track llegara a tener ambos).

---

## Si te atoras

- [`../solucion/<tu-track>/`](../solucion/) — checkpoint de referencia.
- Tabla de errores esperables en el `README.md` de la sesión.
