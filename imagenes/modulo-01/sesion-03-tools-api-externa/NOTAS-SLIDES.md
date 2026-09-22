# Notas para PowerPoint — modulo-01/sesion-03-tools-api-externa

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Quién decide y quién ejecuta
+
+- **Archivo:** `01-tool-call-separacion.png`
+- **Sección fuente:** `1. Function calling: quién genera y quién ejecuta`; fuente: `modulo-1-fundamentos/sesion-03-tools-api-externa/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «quién decide y quién ejecuta» en el proyecto incremental.
+- **Concepto principal:** Quién decide y quién ejecuta.
+- **Mensaje para el alumno:** El modelo solicita; la aplicación controla ejecución, argumentos y permisos.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El modelo solicita; la aplicación controla ejecución, argumentos y permisos.
+- **Elementos que explicar:** 1) LLM solicita tool, 2) Aplicación valida llamada, 3) Tool consulta API, 4) Resultado vuelve al LLM. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Consultar el estado de una línea sin dar al modelo acceso directo a la API.
+- **Ejemplo de industria:** AndesMóvil: Consultar el estado de una línea sin dar al modelo acceso directo a la API.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Tool consulta API»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Contrato de herramienta
+
+- **Archivo:** `02-tool-schema-docstring.png`
+- **Sección fuente:** `2. La docstring es el prompt`; fuente: `modulo-1-fundamentos/sesion-03-tools-api-externa/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «contrato de herramienta» en el proyecto incremental.
+- **Concepto principal:** Contrato de herramienta.
+- **Mensaje para el alumno:** La descripción y el esquema orientan la selección; el código implementa el efecto.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La descripción y el esquema orientan la selección; el código implementa el efecto.
+- **Elementos que explicar:** 1) Nombre preciso, 2) Cuándo usar / no usar, 3) Args Pydantic, 4) Resultado o error legible. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Tool de consulta de estado del pedido.
+- **Ejemplo de industria:** MercaSur: Tool de consulta de estado del pedido.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Args Pydantic»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Tres resultados de API externa
+
+- **Archivo:** `03-integracion-tres-resultados.png`
+- **Sección fuente:** `3. Errores redactados para el modelo`; fuente: `modulo-1-fundamentos/sesion-03-tools-api-externa/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «tres resultados de api externa» en el proyecto incremental.
+- **Concepto principal:** Tres resultados de API externa.
+- **Mensaje para el alumno:** No confundir ausencia de dato con caída del servicio.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. No confundir ausencia de dato con caída del servicio.
+- **Elementos que explicar:** 1) Solicitud a servicio, 2) Dato encontrado, 3) Dato inexistente, 4) Servicio no disponible. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Un número de póliza inexistente difiere de una API de seguros caída.
+- **Ejemplo de industria:** Andina Seguros: Un número de póliza inexistente difiere de una API de seguros caída.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Dato inexistente»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Bucle manual y create_agent
+
+- **Archivo:** `04-bucle-manual-create-agent.png`
+- **Sección fuente:** `4. Del bucle manual a create_agent()`; fuente: `modulo-1-fundamentos/sesion-03-tools-api-externa/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «bucle manual y create_agent» en el proyecto incremental.
+- **Concepto principal:** Bucle manual y create_agent.
+- **Mensaje para el alumno:** La abstracción automatiza el bucle que se estudió explícitamente.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La abstracción automatiza el bucle que se estudió explícitamente.
+- **Elementos que explicar:** 1) Bucle ReAct manual, 2) Tool call / tool result, 3) create_agent(), 4) Mismo control observable. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Diagnóstico de línea con una consulta externa.
+- **Ejemplo de industria:** AndesMóvil: Diagnóstico de línea con una consulta externa.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «create_agent()»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+