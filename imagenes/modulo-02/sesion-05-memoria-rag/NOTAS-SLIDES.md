# Notas para PowerPoint — modulo-02/sesion-05-memoria-rag

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Memoria por hilo
+
+- **Archivo:** `01-thread-id-estado.png`
+- **Sección fuente:** `1. Estado conversacional y thread_id`; fuente: `modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «memoria por hilo» en el proyecto incremental.
+- **Concepto principal:** Memoria por hilo.
+- **Mensaje para el alumno:** La memoria conversacional pertenece al estado de la aplicación y se aísla por hilo.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La memoria conversacional pertenece al estado de la aplicación y se aísla por hilo.
+- **Elementos que explicar:** 1) Mensaje y thread_id, 2) Checkpoint del hilo, 3) Historial recuperado, 4) Modelo recibe contexto. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Separar dos conversaciones de clientes de Banco Inti.
+- **Ejemplo de industria:** Banco Inti: Separar dos conversaciones de clientes de Banco Inti.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Historial recuperado»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Ingesta y chunking
+
+- **Archivo:** `02-ingesta-chunking-qdrant.png`
+- **Sección fuente:** `3. Chunking y su trade-off`; fuente: `modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «ingesta y chunking» en el proyecto incremental.
+- **Concepto principal:** Ingesta y chunking.
+- **Mensaje para el alumno:** Partir textos preserva fragmentos recuperables y su procedencia.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Partir textos preserva fragmentos recuperables y su procedencia.
+- **Elementos que explicar:** 1) Documento del dominio, 2) Chunks con metadatos, 3) Embeddings HF, 4) Colección Qdrant Cloud. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Condicionado SOAT dividido por cobertura y exclusión.
+- **Ejemplo de industria:** Andina Seguros: Condicionado SOAT dividido por cobertura y exclusión.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Embeddings HF»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — RAG fijo y agéntico
+
+- **Archivo:** `03-rag-tradicional-agentico.png`
+- **Sección fuente:** `5. RAG tradicional vs RAG agéntico`; fuente: `modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «rag fijo y agéntico» en el proyecto incremental.
+- **Concepto principal:** RAG fijo y agéntico.
+- **Mensaje para el alumno:** En RAG agéntico el agente decide si necesita recuperación y puede usar otras tools.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. En RAG agéntico el agente decide si necesita recuperación y puede usar otras tools.
+- **Elementos que explicar:** 1) RAG fijo: siempre buscar, 2) Recuperar → responder, 3) RAG agéntico: decidir, 4) Buscar solo cuando conviene. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Pregunta de política frente a consulta de estado de siniestro.
+- **Ejemplo de industria:** Andina Seguros: Pregunta de política frente a consulta de estado de siniestro.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «RAG agéntico: decidir»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Respuesta con cita
+
+- **Archivo:** `04-rag-fuentes-citas.png`
+- **Sección fuente:** `6. Salvaguarda A6 y fundamentación`; fuente: `modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «respuesta con cita» en el proyecto incremental.
+- **Concepto principal:** Respuesta con cita.
+- **Mensaje para el alumno:** La cita permite revisar la base documental de una afirmación.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La cita permite revisar la base documental de una afirmación.
+- **Elementos que explicar:** 1) Pregunta, 2) Recuperar pasaje, 3) Respuesta anclada, 4) Cita de fuente. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Explicar exclusión de póliza citando cláusula.
+- **Ejemplo de industria:** Andina Seguros: Explicar exclusión de póliza citando cláusula.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Respuesta anclada»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 05 — Conocimiento y personalización
+
+- **Archivo:** `05-rag-vs-finetuning.png`
+- **Sección fuente:** `La demo clave: conocimiento va al RAG`; fuente: `modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «conocimiento y personalización» en el proyecto incremental.
+- **Concepto principal:** Conocimiento y personalización.
+- **Mensaje para el alumno:** Los cuatro tracks comparten modelo; cambian prompt, datos y tools.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Los cuatro tracks comparten modelo; cambian prompt, datos y tools.
+- **Elementos que explicar:** 1) Un modelo base, 2) Prompt por industria, 3) Conocimiento en Qdrant, 4) Sin fine-tuning. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Tarifarios actualizables por colección, sin reentrenar Qwen3.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Conocimiento en Qdrant»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+