# Notas para PowerPoint — modulo-01/sesion-02-ecosistema-langchain

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Mensajes y estado
+
+- **Archivo:** `01-mensajes-stateless.png`
+- **Sección fuente:** `1. Mensajes, roles y statelessness`; fuente: `modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «mensajes y estado» en el proyecto incremental.
+- **Concepto principal:** Mensajes y estado.
+- **Mensaje para el alumno:** El modelo no conserva conversaciones entre llamadas: la aplicación reenvía contexto.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El modelo no conserva conversaciones entre llamadas: la aplicación reenvía contexto.
+- **Elementos que explicar:** 1) Usuario envía turno, 2) Aplicación reúne historial, 3) Modelo recibe mensajes, 4) Aplicación conserva estado. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Mantener el hilo de atención del cliente de Banco Inti.
+- **Ejemplo de industria:** Banco Inti: Mantener el hilo de atención del cliente de Banco Inti.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Modelo recibe mensajes»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Estructura del prompt
+
+- **Archivo:** `02-estructura-prompt.png`
+- **Sección fuente:** `2. Rol + Contexto + Tarea + Formato`; fuente: `modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «estructura del prompt» en el proyecto incremental.
+- **Concepto principal:** Estructura del prompt.
+- **Mensaje para el alumno:** Cada parte reduce ambigüedad en una tarea evaluable.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Cada parte reduce ambigüedad en una tarea evaluable.
+- **Elementos que explicar:** 1) Rol, 2) Contexto del dominio, 3) Tarea concreta, 4) Formato de salida. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Clasificar una consulta de devolución en MercaSur.
+- **Ejemplo de industria:** MercaSur: Clasificar una consulta de devolución en MercaSur.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Tarea concreta»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Few-shot selectivo
+
+- **Archivo:** `03-few-shot-selectivo.png`
+- **Sección fuente:** `3. Few-shot (regla A5)`; fuente: `modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «few-shot selectivo» en el proyecto incremental.
+- **Concepto principal:** Few-shot selectivo.
+- **Mensaje para el alumno:** Agregar ejemplos cuando mejoran casos ambiguos; medir el efecto.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Agregar ejemplos cuando mejoran casos ambiguos; medir el efecto.
+- **Elementos que explicar:** 1) Sin ejemplos: tarea clara, 2) Con ejemplos: ambigüedad, 3) Costo adicional de tokens, 4) Medir acierto. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Diferenciar reclamo de consulta en atención posventa.
+- **Ejemplo de industria:** MercaSur: Diferenciar reclamo de consulta en atención posventa.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Costo adicional de tokens»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Salida estructurada robusta
+
+- **Archivo:** `04-structured-output-robusto.png`
+- **Sección fuente:** `4. Structured output: la demo del fallo`; fuente: `modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «salida estructurada robusta» en el proyecto incremental.
+- **Concepto principal:** Salida estructurada robusta.
+- **Mensaje para el alumno:** Pedir JSON no basta; validar y tratar fallos en código.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Pedir JSON no basta; validar y tratar fallos en código.
+- **Elementos que explicar:** 1) Respuesta del modelo, 2) Esquema Pydantic, 3) Validación y reintento, 4) Objeto tipado o error. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Clasificación de operación sospechosa con campos tipados.
+- **Ejemplo de industria:** Banco Inti: Clasificación de operación sospechosa con campos tipados.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Validación y reintento»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+