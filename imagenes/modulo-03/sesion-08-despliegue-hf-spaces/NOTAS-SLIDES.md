# Notas para PowerPoint — modulo-03/sesion-08-despliegue-hf-spaces

Las notas indican un orden sugerido; adaptar al tiempo de la clase y demostrar el código real.

+## Slide 01 — Del script al servicio
+
+- **Archivo:** `01-fastapi-hf-spaces.png`
+- **Sección fuente:** `3. FastAPI`; fuente: `modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «del script al servicio» en el proyecto incremental.
+- **Concepto principal:** Del script al servicio.
+- **Mensaje para el alumno:** Producción permite invocación remota sin el desarrollador delante.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. Producción permite invocación remota sin el desarrollador delante.
+- **Elementos que explicar:** 1) Cliente externo, 2) API key → /chat, 3) FastAPI en HF Spaces, 4) Agente + proveedores SaaS. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Consulta web del estado de un pedido.
+- **Ejemplo de industria:** MercaSur: Consulta web del estado de un pedido.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «FastAPI en HF Spaces»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 02 — Rutas y secretos
+
+- **Archivo:** `02-health-chat-secretos.png`
+- **Sección fuente:** `3. FastAPI + 4. Secretos en la nube`; fuente: `modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «rutas y secretos» en el proyecto incremental.
+- **Concepto principal:** Rutas y secretos.
+- **Mensaje para el alumno:** El endpoint de chat protege la cuota y las credenciales viven en la plataforma.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. El endpoint de chat protege la cuota y las credenciales viven en la plataforma.
+- **Elementos que explicar:** 1) /health: estado, 2) /chat: autenticado, 3) Secrets del Space, 4) Cuota protegida. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Panel externo usa API key del equipo.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Secrets del Space»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+
+## Slide 03 — Arranque en frío
+
+- **Archivo:** `03-cold-start.png`
+- **Sección fuente:** `5. Cold start y free tier`; fuente: `modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md`.
+- **Objetivo pedagógico:** Explicar y aplicar «arranque en frío» en el proyecto incremental.
+- **Concepto principal:** Arranque en frío.
+- **Mensaje para el alumno:** La primera petición puede incluir el tiempo de activación del servicio.
+- **Guion del docente:** Parta de un caso del track y pregunte qué dato o decisión falta. Recorra los elementos numerados, haga que el alumnado explique quién controla cada transición y cierre contrastando el resultado con el mensaje central. La primera petición puede incluir el tiempo de activación del servicio.
+- **Elementos que explicar:** 1) Space inactivo, 2) Primera solicitud, 3) Arranque del contenedor, 4) Solicitudes siguientes. El elemento coral señala el control o resultado crítico, no una nueva tecnología.
+- **Ejemplo práctico:** Evaluador invoca un Space que llevaba horas inactivo.
+- **Ejemplo de industria:** El mismo patrón puede aplicarse a los cuatro tracks; usar el track asignado al equipo.
+- **Pregunta al aula:** ¿Qué fallaría en este caso si se omitiera «Arranque del contenedor»? ¿Cómo se comprobaría con una prueba o una traza?
+- **Errores frecuentes:** Confundir propuesta del modelo con ejecución confirmada; asumir que la caja final garantiza corrección sin validación. Aclarar los límites concretos del caso antes de avanzar.
+- **Conexión anterior:** M.
+- **Conexión posterior:** Sesiones siguientes: integrar y verificar esta capacidad en el agente.
+- **Notas PPTX:** Imagen 16:9 a pantalla completa; conservar margen superior y banda de conclusión. Mostrar cada paso de izquierda a derecha (o por filas en comparaciones); las explicaciones y advertencias van en speaker notes, no sobre la imagen.
+