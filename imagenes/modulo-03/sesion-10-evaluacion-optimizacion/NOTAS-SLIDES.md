# Notas para PowerPoint — modulo-03/sesion-10-evaluacion-optimizacion

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Golden dataset a lo largo del curso
+
+- **Archivo:** `01-golden-dataset-evolutivo.png`
+- **Sección fuente:** `1. El golden dataset era el de siempre`; fuente: `modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «golden dataset a lo largo del curso» en el proyecto incremental.
+- **Concepto principal:** Golden dataset a lo largo del curso.
+- **Mensaje para el alumno:** El mismo conjunto de casos sirve para medir capacidades nuevas.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El mismo conjunto de casos sirve para medir capacidades nuevas.
+- **Elementos que explicar:** 1) S2: clasificar, 2) S4: elegir tool, 3) S5: recuperar/citar, 4) S10: comparar versiones. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** 30 consultas por track con resultados esperados.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «S5: recuperar/citar»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Tres evaluadores
+
+- **Archivo:** `02-evaluadores-deterministas.png`
+- **Sección fuente:** `2. Los 3 evaluators determinísticos`; fuente: `modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «tres evaluadores» en el proyecto incremental.
+- **Concepto principal:** Tres evaluadores.
+- **Mensaje para el alumno:** Las reglas verificables permiten comparar versiones de forma reproducible.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Las reglas verificables permiten comparar versiones de forma reproducible.
+- **Elementos que explicar:** 1) Exactitud de resultado, 2) Uso de tool esperado, 3) Groundedness, 4) Puntaje por caso. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Comprobar que la cobertura cite el texto fuente.
+- **Ejemplo de industria:** Andina Seguros: Comprobar que la cobertura cite el texto fuente.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Groundedness»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Experimento v1 y v2
+
+- **Archivo:** `03-experimento-v1-v2.png`
+- **Sección fuente:** `4. Cuándo una mejora es real`; fuente: `modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «experimento v1 y v2» en el proyecto incremental.
+- **Concepto principal:** Experimento v1 y v2.
+- **Mensaje para el alumno:** Comparar con los mismos casos y considerar el ruido de muestreo.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Comparar con los mismos casos y considerar el ruido de muestreo.
+- **Elementos que explicar:** 1) Fijar dataset, 2) Medir baseline v1, 3) Cambiar una variable, 4) Medir v2 y variación. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Cambiar la docstring de la tool de devoluciones.
+- **Ejemplo de industria:** MercaSur: Cambiar la docstring de la tool de devoluciones.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Cambiar una variable»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+