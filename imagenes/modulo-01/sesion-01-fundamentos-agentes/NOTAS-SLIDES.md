# Notas para PowerPoint — modulo-01/sesion-01-fundamentos-agentes

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — LLM y agente
+
+- **Archivo:** `01-llm-vs-agente.png`
+- **Sección fuente:** `3. Un LLM solo no es un agente`; fuente: `modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «llm y agente» en el proyecto incremental.
+- **Concepto principal:** LLM y agente.
+- **Mensaje para el alumno:** El agente combina modelo, objetivo, herramientas, estado y control.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El agente combina modelo, objetivo, herramientas, estado y control.
+- **Elementos que explicar:** 1) LLM: genera texto, 2) Meta y contexto, 3) Tools y memoria, 4) Control del bucle. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Consultar el plan exige una tool; el LLM aislado no conoce el plan real.
+- **Ejemplo de industria:** AndesMóvil: Consultar el plan exige una tool; el LLM aislado no conoce el plan real.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Tools y memoria»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Bucle de agente: versión base
+
+- **Archivo:** `02-agentic-loop-base.png`
+- **Sección fuente:** `4. Agente = percepción → razonamiento → acción → entorno`; fuente: `modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «bucle de agente: versión base» en el proyecto incremental.
+- **Concepto principal:** Bucle de agente: versión base.
+- **Mensaje para el alumno:** La aplicación ejecuta la tool y devuelve la observación; el ciclo puede repetirse.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La aplicación ejecuta la tool y devuelve la observación; el ciclo puede repetirse.
+- **Elementos que explicar:** 1) Percibir petición, 2) Razonar / elegir, 3) Actuar con tool, 4) Observar resultado. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Consultar consumo y explicar el saldo disponible.
+- **Ejemplo de industria:** AndesMóvil: Consultar consumo y explicar el saldo disponible.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Actuar con tool»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Workflow o agente
+
+- **Archivo:** `03-workflow-vs-agente.png`
+- **Sección fuente:** `5. Workflow vs agente`; fuente: `modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «workflow o agente» en el proyecto incremental.
+- **Concepto principal:** Workflow o agente.
+- **Mensaje para el alumno:** Elegir agencia solo cuando la ruta de ejecución necesita decisiones dinámicas.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Elegir agencia solo cuando la ruta de ejecución necesita decisiones dinámicas.
+- **Elementos que explicar:** 1) Ruta conocida y estable, 2) Workflow: pasos fijados, 3) Ruta variable por contexto, 4) Agente: decide siguiente paso. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Consulta fija de estado frente a diagnóstico variable de avería.
+- **Ejemplo de industria:** AndesMóvil: Consulta fija de estado frente a diagnóstico variable de avería.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Ruta variable por contexto»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Indirección del proveedor
+
+- **Archivo:** `04-provider-portabilidad.png`
+- **Sección fuente:** `8. comun/provider.py`; fuente: `modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «indirección del proveedor» en el proyecto incremental.
+- **Concepto principal:** Indirección del proveedor.
+- **Mensaje para el alumno:** El mismo código del agente solicita el modelo mediante una interfaz común.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El mismo código del agente solicita el modelo mediante una interfaz común.
+- **Elementos que explicar:** 1) Código del agente, 2) comun/provider.py, 3) HF: curso principal, 4) Foundry: bonus. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Cambiar AI_PROVIDER sin reescribir el agente.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «HF: curso principal»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Sesión 0: límites del LLM.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+