# Speaker notes — Sesión 05

## Slide 01 — Memory y RAG

**ID:** IMG-M02-S05-001.

**Archivo:** `01-memoria-rag.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 5 — teoría y objetivos](../../../modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md).

**Objetivo pedagógico:** Separar historial conversacional de recuperación documental.

**Concepto principal:** Memory y RAG.

**Mensaje clave:** Recordar la conversación y consultar documentos son mecanismos diferentes.

**Explicación sugerida:** Recorrer por separado conversación e ingesta documental. La consulta también se representa en el mismo espacio de embeddings de los documentos.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Dos carriles hacia el mismo LLM. Arriba: Usuario → Historial por thread_id → LLM, etiquetar memoria del proceso. Abajo: Corpus → Chunks → Embeddings → Qdrant; Consulta → Retriever → Qdrant; Qdrant → Contexto y fuente → LLM. LLM → Respuesta.

**Ejemplo:** Un turno dice «¿y ese plan?»; el historial resuelve la referencia y RAG aporta la tarifa documentada.

**Ejemplo de industria:** AndesMóvil: historial conserva el plan mencionado y Qdrant aporta el tarifario vigente.

**Pregunta al alumno:** ¿Qué se pierde al reiniciar el proceso y qué permanece en Qdrant?

**Error conceptual frecuente:** Tratar el corpus recuperado como memoria de conversación o reentrenamiento.

**Conexión con sesión anterior:** S4: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S6: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 6 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
