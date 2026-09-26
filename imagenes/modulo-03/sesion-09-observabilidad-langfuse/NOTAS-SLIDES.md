# Notas para PowerPoint — modulo-03/sesion-09-observabilidad-langfuse

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Tres señales de observabilidad
+
+- **Archivo:** `01-logs-metricas-trazas.png`
+- **Sección fuente:** `1. Logs vs métricas vs trazas`; fuente: `modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «tres señales de observabilidad» en el proyecto incremental.
+- **Concepto principal:** Tres señales de observabilidad.
+- **Mensaje para el alumno:** Las trazas muestran la cadena causal y los spans de una ejecución.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Las trazas muestran la cadena causal y los spans de una ejecución.
+- **Elementos que explicar:** 1) Logs: qué ocurrió, 2) Métricas: cuánto, 3) Trazas: dónde ocurrió, 4) Diagnóstico concreto. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Detectar lentitud en tool de tipo de cambio.
+- **Ejemplo de industria:** Banco Inti: Detectar lentitud en tool de tipo de cambio.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Trazas: dónde ocurrió»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Traza de agente en Langfuse
+
+- **Archivo:** `02-trace-span-langfuse.png`
+- **Sección fuente:** `2. Anatomía de una traza`; fuente: `modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «traza de agente en langfuse» en el proyecto incremental.
+- **Concepto principal:** Traza de agente en Langfuse.
+- **Mensaje para el alumno:** Cada paso del agente debe poder localizarse en su ejecución.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Cada paso del agente debe poder localizarse en su ejecución.
+- **Elementos que explicar:** 1) Trace de /chat, 2) Span del modelo, 3) Span de herramienta, 4) Latencia y costo. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Consultar balance y luego política de comisiones.
+- **Ejemplo de industria:** Banco Inti: Consultar balance y luego política de comisiones.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Span de herramienta»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Latencia p50 y p95
+
+- **Archivo:** `03-p50-p95-colas.png`
+- **Sección fuente:** `3. Latencia p50/p95`; fuente: `modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «latencia p50 y p95» en el proyecto incremental.
+- **Concepto principal:** Latencia p50 y p95.
+- **Mensaje para el alumno:** El promedio puede ocultar respuestas lentas del extremo de distribución.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El promedio puede ocultar respuestas lentas del extremo de distribución.
+- **Elementos que explicar:** 1) p50: experiencia típica, 2) p95: cola lenta, 3) Costo por ejecución, 4) Optimizar cuello medido. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Una tool externa lenta afecta el p95.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Costo por ejecución»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Trazabilidad sin fuga de PII
+
+- **Archivo:** `04-traza-sin-pii.png`
+- **Sección fuente:** `4. PII dentro de una traza`; fuente: `modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «trazabilidad sin fuga de pii» en el proyecto incremental.
+- **Concepto principal:** Trazabilidad sin fuga de PII.
+- **Mensaje para el alumno:** Una traza también almacena datos: se sanitiza antes de enviarla.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Una traza también almacena datos: se sanitiza antes de enviarla.
+- **Elementos que explicar:** 1) Petición original, 2) Sanitización, 3) Traza enviada, 4) Revisión segura. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** DNI enmascarado en observabilidad de aseguradora.
+- **Ejemplo de industria:** Andina Seguros: DNI enmascarado en observabilidad de aseguradora.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Traza enviada»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+