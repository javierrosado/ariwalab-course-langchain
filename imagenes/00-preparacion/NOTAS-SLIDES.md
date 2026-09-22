# Notas para PowerPoint — 00-preparacion

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Tokens y ventana de contexto
+
+- **Archivo:** `01-token-contexto-costo.png`
+- **Sección fuente:** `Las 4 demos`; fuente: `00-preparacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «tokens y ventana de contexto» en el proyecto incremental.
+- **Concepto principal:** Tokens y ventana de contexto.
+- **Mensaje para el alumno:** Cada llamada consume presupuesto de contexto y costo.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Cada llamada consume presupuesto de contexto y costo.
+- **Elementos que explicar:** 1) Texto de entrada, 2) Tokens consumidos, 3) Ventana de contexto, 4) Tokens de salida y costo. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Una consulta extensa a una póliza ocupa más contexto que una pregunta breve.
+- **Ejemplo de industria:** Andina Seguros: Una consulta extensa a una póliza ocupa más contexto que una pregunta breve.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Ventana de contexto»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Python, HTTP y conceptos básicos de software.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Variación de respuestas
+
+- **Archivo:** `02-temperatura-no-determinismo.png`
+- **Sección fuente:** `Las 4 demos`; fuente: `00-preparacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «variación de respuestas» en el proyecto incremental.
+- **Concepto principal:** Variación de respuestas.
+- **Mensaje para el alumno:** La salida puede variar; el contrato y las pruebas deben tolerar formulaciones distintas.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La salida puede variar; el contrato y las pruebas deben tolerar formulaciones distintas.
+- **Elementos que explicar:** 1) Mismo prompt, 2) Muestreo A → respuesta A, 3) Muestreo B → respuesta B. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Dos respuestas válidas sobre un plan pueden usar palabras diferentes.
+- **Ejemplo de industria:** AndesMóvil: Dos respuestas válidas sobre un plan pueden usar palabras diferentes.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Muestreo B → respuesta B»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Python, HTTP y conceptos básicos de software.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Embeddings y proximidad semántica
+
+- **Archivo:** `03-embeddings-semantica.png`
+- **Sección fuente:** `Las 4 demos`; fuente: `00-preparacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «embeddings y proximidad semántica» en el proyecto incremental.
+- **Concepto principal:** Embeddings y proximidad semántica.
+- **Mensaje para el alumno:** La similitud vectorial ayuda a recuperar contenido aunque las palabras difieran.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La similitud vectorial ayuda a recuperar contenido aunque las palabras difieran.
+- **Elementos que explicar:** 1) Consulta en español, 2) Vector de la consulta, 3) Vectores de documentos, 4) Vecinos por significado. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** «No tengo señal» puede acercarse a «falla de cobertura».
+- **Ejemplo de industria:** AndesMóvil: «No tengo señal» puede acercarse a «falla de cobertura».
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Vectores de documentos»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Python, HTTP y conceptos básicos de software.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Alucinación y verificación
+
+- **Archivo:** `04-alucinacion-verificacion.png`
+- **Sección fuente:** `Errores frecuentes en esta sesión`; fuente: `00-preparacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «alucinación y verificación» en el proyecto incremental.
+- **Concepto principal:** Alucinación y verificación.
+- **Mensaje para el alumno:** Una respuesta convincente no equivale a un dato confirmado.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Una respuesta convincente no equivale a un dato confirmado.
+- **Elementos que explicar:** 1) Pregunta sin fuente, 2) LLM propone respuesta, 3) Verificar con fuente o tool, 4) Responder con evidencia. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** La cobertura de un SOAT debe contrastarse con el condicionado.
+- **Ejemplo de industria:** Andina Seguros: La cobertura de un SOAT debe contrastarse con el condicionado.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Verificar con fuente o tool»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Python, HTTP y conceptos básicos de software.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+