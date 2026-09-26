# Notas para PowerPoint — modulo-04/bonus-foundry

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — El switch de proveedor
+
+- **Archivo:** `01-switch-proveedor.png`
+- **Sección fuente:** `La lección, en una línea`; fuente: `modulo-4-plus-foundry/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «el switch de proveedor» en el proyecto incremental.
+- **Concepto principal:** El switch de proveedor.
+- **Mensaje para el alumno:** La portabilidad del código no garantiza respuestas idénticas entre modelos.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La portabilidad del código no garantiza respuestas idénticas entre modelos.
+- **Elementos que explicar:** 1) Agente sin cambios, 2) AI_PROVIDER=huggingface, 3) AI_PROVIDER=foundry, 4) Comparar comportamiento. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Mismas cinco consultas del track en ambos proveedores.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «AI_PROVIDER=foundry»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** S1–S11: agente acumulado y provider.
+- **Conexión posterior:** Curso 2: despliegue y gobierno Azure.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Modelo de recursos Foundry
+
+- **Archivo:** `02-modelo-recursos-azure.png`
+- **Sección fuente:** `Objetivos + los 8 pasos`; fuente: `modulo-4-plus-foundry/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «modelo de recursos foundry» en el proyecto incremental.
+- **Concepto principal:** Modelo de recursos Foundry.
+- **Mensaje para el alumno:** La jerarquía ubica el deployment que consume el agente.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La jerarquía ubica el deployment que consume el agente.
+- **Elementos que explicar:** 1) Suscripción, 2) Grupo de recursos, 3) Recurso y proyecto, 4) Deployment del modelo. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Crear deployment para el bonus opcional.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Recurso y proyecto»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** S1–S11: agente acumulado y provider.
+- **Conexión posterior:** Curso 2: despliegue y gobierno Azure.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Hosted agent y Responses
+
+- **Archivo:** `03-hosted-agent-responses.png`
+- **Sección fuente:** `Pasos 5-7`; fuente: `modulo-4-plus-foundry/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «hosted agent y responses» en el proyecto incremental.
+- **Concepto principal:** Hosted agent y Responses.
+- **Mensaje para el alumno:** El host envuelve el grafo; revisar por separado la portabilidad de guardrails.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El host envuelve el grafo; revisar por separado la portabilidad de guardrails.
+- **Elementos que explicar:** 1) Grafo LangGraph, 2) ResponsesHostServer, 3) Endpoint /responses, 4) Cliente y streaming. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Exponer el mismo caso del track con endpoint gestionado.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Endpoint /responses»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** S1–S11: agente acumulado y provider.
+- **Conexión posterior:** Curso 2: despliegue y gobierno Azure.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Comparativa de despliegues
+
+- **Archivo:** `04-comparacion-evidencia.png`
+- **Sección fuente:** `El entregable: cuadro comparativo`; fuente: `modulo-4-plus-foundry/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «comparativa de despliegues» en el proyecto incremental.
+- **Concepto principal:** Comparativa de despliegues.
+- **Mensaje para el alumno:** La elección depende de evidencia y restricciones del escenario.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La elección depende de evidencia y restricciones del escenario.
+- **Elementos que explicar:** 1) HF Spaces: stack abierto, 2) Foundry: hosting gestionado, 3) 7 dimensiones medidas, 4) Decisión contextual. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Comparar latencia, costo, operación y gobernanza con mediciones propias.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «7 dimensiones medidas»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** S1–S11: agente acumulado y provider.
+- **Conexión posterior:** Curso 2: despliegue y gobierno Azure.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+