# Notas para PowerPoint — modulo-02/sesion-06-automatizacion-guardrails

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Inyección y frontera de confianza
+
+- **Archivo:** `01-prompt-injection-frontera.png`
+- **Sección fuente:** `1. Inyección de prompt`; fuente: `modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «inyección y frontera de confianza» en el proyecto incremental.
+- **Concepto principal:** Inyección y frontera de confianza.
+- **Mensaje para el alumno:** Un prompt de defensa no reemplaza controles ejecutables en código.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Un prompt de defensa no reemplaza controles ejecutables en código.
+- **Elementos que explicar:** 1) Entrada no confiable, 2) Modelo puede ser inducido, 3) Código valida permisos, 4) Tool bloquea acción prohibida. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Un mensaje malicioso no habilita transferencias en Banco Inti.
+- **Ejemplo de industria:** Banco Inti: Un mensaje malicioso no habilita transferencias en Banco Inti.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Código valida permisos»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — PII de entrada y salida
+
+- **Archivo:** `02-pii-entrada-salida.png`
+- **Sección fuente:** `2. PII y Ley 29733`; fuente: `modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «pii de entrada y salida» en el proyecto incremental.
+- **Concepto principal:** PII de entrada y salida.
+- **Mensaje para el alumno:** La protección de datos debe cubrir entrada, respuesta y observabilidad.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La protección de datos debe cubrir entrada, respuesta y observabilidad.
+- **Elementos que explicar:** 1) Entrada con PII, 2) Enmascarar antes de LLM, 3) Procesar solicitud, 4) Filtrar salida y traza. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Mostrar solo los cuatro últimos dígitos de tarjeta.
+- **Ejemplo de industria:** Banco Inti: Mostrar solo los cuatro últimos dígitos de tarjeta.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Procesar solicitud»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Escalamiento humano
+
+- **Archivo:** `03-escalamiento-humano.png`
+- **Sección fuente:** `3. Límites de actuación y escalamiento`; fuente: `modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «escalamiento humano» en el proyecto incremental.
+- **Concepto principal:** Escalamiento humano.
+- **Mensaje para el alumno:** El humano interviene donde la política impide que el agente decida o actúe solo.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El humano interviene donde la política impide que el agente decida o actúe solo.
+- **Elementos que explicar:** 1) Detectar riesgo o límite, 2) Detener acción automática, 3) Solicitar revisión humana, 4) Registrar resolución. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Derivar lesiones personales en un siniestro SOAT.
+- **Ejemplo de industria:** Andina Seguros: Derivar lesiones personales en un siniestro SOAT.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Solicitar revisión humana»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 04 — Arquitectura evolutiva: guardrails
+
+- **Archivo:** `04-middleware-evolucion.png`
+- **Sección fuente:** `4. Middleware`; fuente: `modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «arquitectura evolutiva: guardrails» en el proyecto incremental.
+- **Concepto principal:** Arquitectura evolutiva: guardrails.
+- **Mensaje para el alumno:** Middleware aplica controles alrededor del agente sin redefinir sus tools.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Middleware aplica controles alrededor del agente sin redefinir sus tools.
+- **Elementos que explicar:** 1) Usuario y entrada, 2) Middleware: PII / política, 3) Agente + tools + RAG, 4) Middleware: salida y traza. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Bloquear respuestas con datos de terceros.
+- **Ejemplo de industria:** Banco Inti: Bloquear respuestas con datos de terceros.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Agente + tools + RAG»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+