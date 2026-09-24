# Prompts de imágenes — sesion-05-memoria-rag

## IMG-M02-S05-001 — Memory y RAG

- **Objetivo pedagógico:** Separar historial conversacional de recuperación documental.
- **Composición:** Dos carriles hacia el mismo LLM. Arriba: Usuario → Historial por thread_id → LLM, etiquetar memoria del proceso. Abajo: Corpus → Chunks → Embeddings → Qdrant; Consulta → Retriever → Qdrant; Qdrant → Contexto y fuente → LLM. LLM → Respuesta.
- **Elementos y texto visible:** Memory, RAG, Usuario, Historial, thread_id, Memoria del proceso, LLM, Corpus, Chunks, Embeddings, Qdrant, Consulta, Retriever, Contexto y fuente, Respuesta.
- **Flujo:** las relaciones direccionales descritas en composición son obligatorias.
- **Jerarquía:** título, mecanismo central, nota breve.
- **Iconos:** persona, chip, runtime, llave, cilindro, historial, documentos, árbol de trazas y checklist según corresponda.
- **Paleta:** fondo #F4F6F8; texto #1E293B; tarjetas #FFFFFF; acento #FF5733.
- **Formato:** 16:9; objetivo 1536 × 864 o equivalente; PNG.
- **Restricciones:** distinguir propuesta/ejecución; evitar cruces de flechas y exceso de texto.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, credenciales, tecnologías ajenas o métricas inventadas.
- **Archivo:** `01-memoria-rag.png`.
- **Uso:** Recurso disponible para las diapositivas.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, target 1536x864 or equivalent. Finished PNG bitmap, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Concept: Memory y RAG. Pedagogical goal: Separar historial conversacional de recuperación documental. Composition and exact directional relationships: Dos carriles hacia el mismo LLM. Arriba: Usuario → Historial por thread_id → LLM, etiquetar memoria del proceso. Abajo: Corpus → Chunks → Embeddings → Qdrant; Consulta → Retriever → Qdrant; Qdrant → Contexto y fuente → LLM. LLM → Respuesta. Visible labels verbatim in Spanish: Memory, RAG, Usuario, Historial, thread_id, Memoria del proceso, LLM, Corpus, Chunks, Embeddings, Qdrant, Consulta, Retriever, Contexto y fuente, Respuesta. Title: Memory y RAG. Visual hierarchy: title then main flow then one short explanatory note. Consistent icons: user outline, LLM chip, runtime square, tool wrench, database cylinder, history stacked cards, documents pages, observability tree, evaluation checklist. Solid arrows for execution/data and dashed for telemetry; keep arrows unambiguous and non-crossing. No photographs, humanoid robots, 3D, heavy shadows, gradients, stock imagery, extra technologies, real company logos, fabricated metrics, API keys, or paragraphs. Do not add components not requested. Clearly distinguish the model proposing and the runtime executing actions. This is a precise teaching diagram, not decorative art.
```

### Criterios visuales

Fondo opaco; representar LLM con chip. Incluir solo los nodos del mecanismo, sin leyendas
de iconos adicionales. Las flechas de datos y ejecución son sólidas; telemetría solo en
el diagrama de despliegue.

```text
Make exactly ONE icon change: replace the brain icon representing the model/LLM with a simple orange MICROCHIP icon outlined in dark navy, matching the canonical course LLM symbol. Preserve every word, arrow, layout, color and card from the input. No other changes. Opaque background.
```
