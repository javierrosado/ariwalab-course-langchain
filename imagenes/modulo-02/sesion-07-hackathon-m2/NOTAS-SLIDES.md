# Notas para PowerPoint — modulo-02/sesion-07-hackathon-m2

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Pruebas por invariantes
+
+- **Archivo:** `01-invariantes-no-igualdad.png`
+- **Sección fuente:** `0. Cómo se prueba lo no determinístico`; fuente: `modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «pruebas por invariantes» en el proyecto incremental.
+- **Concepto principal:** Pruebas por invariantes.
+- **Mensaje para el alumno:** Se prueba comportamiento observable y condiciones obligatorias, no redacción exacta.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Se prueba comportamiento observable y condiciones obligatorias, no redacción exacta.
+- **Elementos que explicar:** 1) Texto exacto: frágil, 2) Tool correcta, 3) Fuente citada, 4) PII ausente. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Respuesta sobre póliza con cita y sin DNI completo.
+- **Ejemplo de industria:** Andina Seguros: Respuesta sobre póliza con cita y sin DNI completo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Fuente citada»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Casos borde y repeticiones
+
+- **Archivo:** `02-casos-borde-repeticion.png`
+- **Sección fuente:** `2. La clínica: 45 minutos`; fuente: `modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «casos borde y repeticiones» en el proyecto incremental.
+- **Concepto principal:** Casos borde y repeticiones.
+- **Mensaje para el alumno:** Una tasa sobre varias ejecuciones revela fallas intermitentes.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Una tasa sobre varias ejecuciones revela fallas intermitentes.
+- **Elementos que explicar:** 1) Casos normales y borde, 2) Repetir ejecuciones, 3) Contar aprobaciones, 4) Corregir fallos reales. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Servicio externo caído durante una consulta de pedido.
+- **Ejemplo de industria:** MercaSur: Servicio externo caído durante una consulta de pedido.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Contar aprobaciones»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** Módulo 1: modelo, prompts y herramientas.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+