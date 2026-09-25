# Observabilidad y trazabilidad con Langfuse — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Hacer visible la ejecución

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Hacer visible la ejecución
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Inspeccionar el recorrido del agente después de una solicitud real.

CONCEPTO PRINCIPAL
Hacer visible la ejecución

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La traza permite discutir una ejecución concreta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué diferencia hay entre sospechar lentitud y localizarla?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Solicitud: Una ejecución identificable del cliente.

Instrumentación: Registra operaciones relevantes con tiempos y relaciones.

Langfuse: Permite examinar el recorrido y formular hipótesis.

Cierre con la distinción: La traza permite discutir una ejecución concreta.

ELEMENTOS QUE CONVIENE EXPLICAR
Solicitud; Instrumentación; Langfuse. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Una consulta sencilla tarda más de lo esperado.
Abrir: Localizar su traza en Langfuse.
Recorrer: Identificar llamadas al modelo y tools.
Priorizar: Señalar el paso dominante con evidencia.
Resultado: El curso usa Langfuse para el objetivo de observabilidad del sílabo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre sospechar lentitud y localizarla?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La traza permite discutir una ejecución concreta.

ERRORES CONCEPTUALES FRECUENTES
Cambiar tecnología o prompt antes de observar el problema.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos.

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Logs, métricas y trazas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Observar antes de optimizar

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Observar antes de optimizar
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Inspeccionar el recorrido del agente después de una solicitud real.

CONCEPTO PRINCIPAL
Hacer visible la ejecución

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La traza permite discutir una ejecución concreta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Camino: Qué modelo, tools y retriever participaron.

Costo: Qué pasos consumieron tokens y tiempo.

Decisión: Dónde conviene investigar primero.

Contraste la regla con este error: Cambiar tecnología o prompt antes de observar el problema. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Camino; Costo; Decisión. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Una consulta sencilla tarda más de lo esperado.
Abrir: Localizar su traza en Langfuse.
Recorrer: Identificar llamadas al modelo y tools.
Priorizar: Señalar el paso dominante con evidencia.
Resultado: El curso usa Langfuse para el objetivo de observabilidad del sílabo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre sospechar lentitud y localizarla?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La traza permite discutir una ejecución concreta.

ERRORES CONCEPTUALES FRECUENTES
Cambiar tecnología o prompt antes de observar el problema.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos.

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Logs, métricas y trazas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Hacer visible la ejecución

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: AndesMóvil · Hacer visible la ejecución
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Inspeccionar el recorrido del agente después de una solicitud real.

CONCEPTO PRINCIPAL
Hacer visible la ejecución

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La traza permite discutir una ejecución concreta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una consulta sencilla tarda más de lo esperado. Pida una predicción.

Abrir: Localizar su traza en Langfuse.

Recorrer: Identificar llamadas al modelo y tools.

Priorizar: Señalar el paso dominante con evidencia.

Resultado esperado: El curso usa Langfuse para el objetivo de observabilidad del sílabo. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Abrir; Recorrer; Priorizar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Una consulta sencilla tarda más de lo esperado.
Abrir: Localizar su traza en Langfuse.
Recorrer: Identificar llamadas al modelo y tools.
Priorizar: Señalar el paso dominante con evidencia.
Resultado: El curso usa Langfuse para el objetivo de observabilidad del sílabo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre sospechar lentitud y localizarla?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La traza permite discutir una ejecución concreta.

ERRORES CONCEPTUALES FRECUENTES
Cambiar tecnología o prompt antes de observar el problema.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos.

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Logs, métricas y trazas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Logs, métricas y trazas

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Logs, métricas y trazas
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Elegir la señal adecuada para la pregunta de diagnóstico.

CONCEPTO PRINCIPAL
Logs, métricas y trazas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Ninguna señal aislada explica todos los niveles de un incidente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué usarías para seguir una consulta específica entre varios pasos?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Logs: Eventos y mensajes que describen qué pasó.

Métricas: Agregados que muestran cantidades y tendencias.

Trazas: Recorrido de una ejecución con relaciones entre operaciones.

Cierre con la distinción: Ninguna señal aislada explica todos los niveles de un incidente.

ELEMENTOS QUE CONVIENE EXPLICAR
Logs; Métricas; Trazas. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Algunos clientes experimentan respuestas lentas.
Métrica: Identificar si crece la latencia de cola.
Traza: Abrir un caso lento y localizar sus spans.
Log: Leer el error o detalle asociado al paso problemático.
Resultado: Las señales se complementan porque responden preguntas distintas.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué usarías para seguir una consulta específica entre varios pasos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Ninguna señal aislada explica todos los niveles de un incidente.

ERRORES CONCEPTUALES FRECUENTES
Tratar una lista de prints como una traza completa.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Hacer visible la ejecución

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Anatomía de una traza

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Una pregunta por señal

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Una pregunta por señal
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Elegir la señal adecuada para la pregunta de diagnóstico.

CONCEPTO PRINCIPAL
Logs, métricas y trazas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Ninguna señal aislada explica todos los niveles de un incidente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Evento: ¿Qué error devolvió la herramienta?

Agregado: ¿Qué proporción de peticiones termina con error?

Recorrido: ¿En qué paso se consumió el tiempo de este caso?

Contraste la regla con este error: Tratar una lista de prints como una traza completa. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Evento; Agregado; Recorrido. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Algunos clientes experimentan respuestas lentas.
Métrica: Identificar si crece la latencia de cola.
Traza: Abrir un caso lento y localizar sus spans.
Log: Leer el error o detalle asociado al paso problemático.
Resultado: Las señales se complementan porque responden preguntas distintas.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué usarías para seguir una consulta específica entre varios pasos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Ninguna señal aislada explica todos los niveles de un incidente.

ERRORES CONCEPTUALES FRECUENTES
Tratar una lista de prints como una traza completa.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Hacer visible la ejecución

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Anatomía de una traza

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Logs, métricas y trazas

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: Banco Inti · Logs, métricas y trazas
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Elegir la señal adecuada para la pregunta de diagnóstico.

CONCEPTO PRINCIPAL
Logs, métricas y trazas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Ninguna señal aislada explica todos los niveles de un incidente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Algunos clientes experimentan respuestas lentas. Pida una predicción.

Métrica: Identificar si crece la latencia de cola.

Traza: Abrir un caso lento y localizar sus spans.

Log: Leer el error o detalle asociado al paso problemático.

Resultado esperado: Las señales se complementan porque responden preguntas distintas. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Métrica; Traza; Log. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Algunos clientes experimentan respuestas lentas.
Métrica: Identificar si crece la latencia de cola.
Traza: Abrir un caso lento y localizar sus spans.
Log: Leer el error o detalle asociado al paso problemático.
Resultado: Las señales se complementan porque responden preguntas distintas.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué usarías para seguir una consulta específica entre varios pasos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Ninguna señal aislada explica todos los niveles de un incidente.

ERRORES CONCEPTUALES FRECUENTES
Tratar una lista de prints como una traza completa.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Hacer visible la ejecución

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Anatomía de una traza

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Anatomía de una traza

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Anatomía de una traza
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Relacionar el tiempo total con las operaciones del ejemplo del repositorio.

CONCEPTO PRINCIPAL
Anatomía de una traza

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Optimiza el paso que la traza identifica, no el que parece complejo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Reducir 100 ms de la tool resolvería la mayor parte de la latencia?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Modelo: Tres llamadas: 1.180 + 980 + 410 = 2.570 ms.

Herramienta: get_customer_plan consume 240 ms.

Retriever: La recuperación consume 610 ms; total ilustrado: 3.420 ms.

Cierre con la distinción: Optimiza el paso que la traza identifica, no el que parece complejo.

ELEMENTOS QUE CONVIENE EXPLICAR
Modelo; Herramienta; Retriever. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La traza incluye una consulta de plan y una recuperación documental.
Sumar: 2.570 + 240 + 610 = 3.420 ms.
Localizar: El modelo representa aproximadamente el 75 % del total.
Investigar: Revisar si todas las llamadas eran necesarias.
Resultado: Las cifras son el ejemplo del README; no mediciones del nuevo PPTX.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Reducir 100 ms de la tool resolvería la mayor parte de la latencia?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Optimiza el paso que la traza identifica, no el que parece complejo.

ERRORES CONCEPTUALES FRECUENTES
Sumar spans solapados como si siempre fueran secuenciales.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Logs, métricas y trazas

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: p50, p95 y promedio

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Leer jerarquía y secuencia

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Leer jerarquía y secuencia
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Relacionar el tiempo total con las operaciones del ejemplo del repositorio.

CONCEPTO PRINCIPAL
Anatomía de una traza

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Optimiza el paso que la traza identifica, no el que parece complejo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Trace: Agrupa la consulta completa.

Span: Describe una operación y su relación con la ejecución.

Interpretación: En el ejemplo secuencial, las llamadas al modelo dominan el tiempo.

Contraste la regla con este error: Sumar spans solapados como si siempre fueran secuenciales. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Trace; Span; Interpretación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La traza incluye una consulta de plan y una recuperación documental.
Sumar: 2.570 + 240 + 610 = 3.420 ms.
Localizar: El modelo representa aproximadamente el 75 % del total.
Investigar: Revisar si todas las llamadas eran necesarias.
Resultado: Las cifras son el ejemplo del README; no mediciones del nuevo PPTX.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Reducir 100 ms de la tool resolvería la mayor parte de la latencia?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Optimiza el paso que la traza identifica, no el que parece complejo.

ERRORES CONCEPTUALES FRECUENTES
Sumar spans solapados como si siempre fueran secuenciales.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Logs, métricas y trazas

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: p50, p95 y promedio

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Anatomía de una traza

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: AndesMóvil · Anatomía de una traza
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Relacionar el tiempo total con las operaciones del ejemplo del repositorio.

CONCEPTO PRINCIPAL
Anatomía de una traza

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Optimiza el paso que la traza identifica, no el que parece complejo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La traza incluye una consulta de plan y una recuperación documental. Pida una predicción.

Sumar: 2.570 + 240 + 610 = 3.420 ms.

Localizar: El modelo representa aproximadamente el 75 % del total.

Investigar: Revisar si todas las llamadas eran necesarias.

Resultado esperado: Las cifras son el ejemplo del README; no mediciones del nuevo PPTX. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Sumar; Localizar; Investigar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La traza incluye una consulta de plan y una recuperación documental.
Sumar: 2.570 + 240 + 610 = 3.420 ms.
Localizar: El modelo representa aproximadamente el 75 % del total.
Investigar: Revisar si todas las llamadas eran necesarias.
Resultado: Las cifras son el ejemplo del README; no mediciones del nuevo PPTX.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Reducir 100 ms de la tool resolvería la mayor parte de la latencia?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Optimiza el paso que la traza identifica, no el que parece complejo.

ERRORES CONCEPTUALES FRECUENTES
Sumar spans solapados como si siempre fueran secuenciales.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Logs, métricas y trazas

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: p50, p95 y promedio

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. p50, p95 y promedio

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: p50, p95 y promedio
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Describir la distribución y la cola de latencia con un método explícito.

CONCEPTO PRINCIPAL
p50, p95 y promedio

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Reporta distribución y condiciones, no solo una media.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Por qué dos herramientas pueden mostrar distinto p95 con diez datos?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Muestra: Nueve solicitudes de 800 ms y una de 21.000 ms.

Promedio: 28.200 / 10 = 2.820 ms.

Percentiles: p50 = 800 ms; p95 = 21.000 ms usando rango más próximo.

Cierre con la distinción: Reporta distribución y condiciones, no solo una media.

ELEMENTOS QUE CONVIENE EXPLICAR
Muestra; Promedio; Percentiles. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un cold start afecta una de diez consultas del mismo escenario.
Ordenar: Separar las nueve rápidas de la lenta.
Resumir: Informar p50, p95 y método, junto al tamaño de muestra.
Contextualizar: Marcar que la lenta ocurrió tras inactividad.
Resultado: El percentil cambia con la muestra y el método; no elimina la variación.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué dos herramientas pueden mostrar distinto p95 con diez datos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Reporta distribución y condiciones, no solo una media.

ERRORES CONCEPTUALES FRECUENTES
Llamar peor caso al p95 en cualquier conjunto.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Anatomía de una traza

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: PII en la telemetría

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Interpretar con cuidado

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Interpretar con cuidado
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Describir la distribución y la cola de latencia con un método explícito.

CONCEPTO PRINCIPAL
p50, p95 y promedio

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Reporta distribución y condiciones, no solo una media.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

p50: Describe el punto central de la muestra ordenada.

p95: Describe un percentil alto; no es sinónimo universal de máximo.

Método: Con pocas observaciones, la interpolación puede dar otro valor.

Contraste la regla con este error: Llamar peor caso al p95 en cualquier conjunto. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
p50; p95; Método. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un cold start afecta una de diez consultas del mismo escenario.
Ordenar: Separar las nueve rápidas de la lenta.
Resumir: Informar p50, p95 y método, junto al tamaño de muestra.
Contextualizar: Marcar que la lenta ocurrió tras inactividad.
Resultado: El percentil cambia con la muestra y el método; no elimina la variación.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué dos herramientas pueden mostrar distinto p95 con diez datos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Reporta distribución y condiciones, no solo una media.

ERRORES CONCEPTUALES FRECUENTES
Llamar peor caso al p95 en cualquier conjunto.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Anatomía de una traza

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: PII en la telemetría

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · p50, p95 y promedio

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: MercaSur · p50, p95 y promedio
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Describir la distribución y la cola de latencia con un método explícito.

CONCEPTO PRINCIPAL
p50, p95 y promedio

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Reporta distribución y condiciones, no solo una media.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Un cold start afecta una de diez consultas del mismo escenario. Pida una predicción.

Ordenar: Separar las nueve rápidas de la lenta.

Resumir: Informar p50, p95 y método, junto al tamaño de muestra.

Contextualizar: Marcar que la lenta ocurrió tras inactividad.

Resultado esperado: El percentil cambia con la muestra y el método; no elimina la variación. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Ordenar; Resumir; Contextualizar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un cold start afecta una de diez consultas del mismo escenario.
Ordenar: Separar las nueve rápidas de la lenta.
Resumir: Informar p50, p95 y método, junto al tamaño de muestra.
Contextualizar: Marcar que la lenta ocurrió tras inactividad.
Resultado: El percentil cambia con la muestra y el método; no elimina la variación.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué dos herramientas pueden mostrar distinto p95 con diez datos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Reporta distribución y condiciones, no solo una media.

ERRORES CONCEPTUALES FRECUENTES
Llamar peor caso al p95 en cualquier conjunto.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Anatomía de una traza

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: PII en la telemetría

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. PII en la telemetría

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: PII en la telemetría
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §4 y comun/observability.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Aplicar protección antes de que el contenido salga hacia la plataforma de trazas.

CONCEPTO PRINCIPAL
PII en la telemetría

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Proteger la respuesta visible no protege automáticamente las trazas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿En qué punto ya sería tarde para evitar que el SaaS reciba el dato?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Ejecución: Mensajes y argumentos pueden contener identificadores.

Enmascarador: Transforma los datos en la frontera de exportación.

Langfuse: Recibe contenido protegido y estructura útil de la traza.

Cierre con la distinción: Proteger la respuesta visible no protege automáticamente las trazas.

ELEMENTOS QUE CONVIENE EXPLICAR
Ejecución; Enmascarador; Langfuse. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El argumento de consulta incluye una placa o un identificador del caso.
Revisar: Identificar qué campos llegan a la instrumentación.
Proteger: Aplicar el saneamiento previsto antes de exportar.
Verificar: Inspeccionar la traza recibida y sus campos reales.
Resultado: El patrón debe comprobarse campo por campo; no todos los identificadores tienen el mismo formato.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿En qué punto ya sería tarde para evitar que el SaaS reciba el dato?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Proteger la respuesta visible no protege automáticamente las trazas.

ERRORES CONCEPTUALES FRECUENTES
Suponer que cualquier campo queda cubierto por el patrón de DNI.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: p50, p95 y promedio

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Laboratorio L9: dos cuellos de botella

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Equilibrio entre diagnóstico y exposición

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Equilibrio entre diagnóstico y exposición
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §4 y comun/observability.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Aplicar protección antes de que el contenido salga hacia la plataforma de trazas.

CONCEPTO PRINCIPAL
PII en la telemetría

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Proteger la respuesta visible no protege automáticamente las trazas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Conservar: Nombres de tools, estructura, tiempos y uso.

Reducir: Identificadores sensibles que no deben exportarse íntegros.

Aceptar: Una traza enmascarada puede no permitir reproducir exactamente el dato.

Contraste la regla con este error: Suponer que cualquier campo queda cubierto por el patrón de DNI. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Conservar; Reducir; Aceptar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El argumento de consulta incluye una placa o un identificador del caso.
Revisar: Identificar qué campos llegan a la instrumentación.
Proteger: Aplicar el saneamiento previsto antes de exportar.
Verificar: Inspeccionar la traza recibida y sus campos reales.
Resultado: El patrón debe comprobarse campo por campo; no todos los identificadores tienen el mismo formato.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿En qué punto ya sería tarde para evitar que el SaaS reciba el dato?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Proteger la respuesta visible no protege automáticamente las trazas.

ERRORES CONCEPTUALES FRECUENTES
Suponer que cualquier campo queda cubierto por el patrón de DNI.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: p50, p95 y promedio

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Laboratorio L9: dos cuellos de botella

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · PII en la telemetría

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: Andina Seguros · PII en la telemetría
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §4 y comun/observability.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Aplicar protección antes de que el contenido salga hacia la plataforma de trazas.

CONCEPTO PRINCIPAL
PII en la telemetría

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Proteger la respuesta visible no protege automáticamente las trazas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El argumento de consulta incluye una placa o un identificador del caso. Pida una predicción.

Revisar: Identificar qué campos llegan a la instrumentación.

Proteger: Aplicar el saneamiento previsto antes de exportar.

Verificar: Inspeccionar la traza recibida y sus campos reales.

Resultado esperado: El patrón debe comprobarse campo por campo; no todos los identificadores tienen el mismo formato. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Revisar; Proteger; Verificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El argumento de consulta incluye una placa o un identificador del caso.
Revisar: Identificar qué campos llegan a la instrumentación.
Proteger: Aplicar el saneamiento previsto antes de exportar.
Verificar: Inspeccionar la traza recibida y sus campos reales.
Resultado: El patrón debe comprobarse campo por campo; no todos los identificadores tienen el mismo formato.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿En qué punto ya sería tarde para evitar que el SaaS reciba el dato?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Proteger la respuesta visible no protege automáticamente las trazas.

ERRORES CONCEPTUALES FRECUENTES
Suponer que cualquier campo queda cubierto por el patrón de DNI.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: p50, p95 y promedio

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: Laboratorio L9: dos cuellos de botella

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Laboratorio L9: dos cuellos de botella

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Laboratorio L9: dos cuellos de botella
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Instrumentar el Space y extraer dos hallazgos respaldados por trazas reales.

CONCEPTO PRINCIPAL
Laboratorio L9: dos cuellos de botella

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un hallazgo útil conecta observación, causa posible y próxima prueba.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué traza adicional buscarías para comprobar que el patrón se repite?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Integrar: Añadir observability.py y la configuración de Langfuse.

Redesplegar: Enviar tráfico a la URL real del Space.

Analizar: Documentar dos cuellos de botella y su evidencia.

Cierre con la distinción: Un hallazgo útil conecta observación, causa posible y próxima prueba.

ELEMENTOS QUE CONVIENE EXPLICAR
Integrar; Redesplegar; Analizar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una pregunta de comisión genera recuperación repetida y varias llamadas al modelo.
Evidencia: Guardar referencias de las ejecuciones representativas.
Hipótesis: La descripción del retriever induce llamadas redundantes.
Siguiente: Proponer una modificación medible para L10.
Resultado: La hipótesis es una explicación por verificar, no un hecho demostrado por una sola traza.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué traza adicional buscarías para comprobar que el patrón se repite?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un hallazgo útil conecta observación, causa posible y próxima prueba.

ERRORES CONCEPTUALES FRECUENTES
Presentar una sospecha como causa confirmada.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: PII en la telemetría

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: De trazas a evaluación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Redactar un hallazgo útil

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Redactar un hallazgo útil
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Instrumentar el Space y extraer dos hallazgos respaldados por trazas reales.

CONCEPTO PRINCIPAL
Laboratorio L9: dos cuellos de botella

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un hallazgo útil conecta observación, causa posible y próxima prueba.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Hecho: Qué span o secuencia domina en los casos observados.

Hipótesis: Qué causa podría explicar ese comportamiento.

Prueba futura: Qué cambio o medición permitiría comprobarla en S10.

Contraste la regla con este error: Presentar una sospecha como causa confirmada. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Hecho; Hipótesis; Prueba futura. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una pregunta de comisión genera recuperación repetida y varias llamadas al modelo.
Evidencia: Guardar referencias de las ejecuciones representativas.
Hipótesis: La descripción del retriever induce llamadas redundantes.
Siguiente: Proponer una modificación medible para L10.
Resultado: La hipótesis es una explicación por verificar, no un hecho demostrado por una sola traza.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué traza adicional buscarías para comprobar que el patrón se repite?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un hallazgo útil conecta observación, causa posible y próxima prueba.

ERRORES CONCEPTUALES FRECUENTES
Presentar una sospecha como causa confirmada.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: PII en la telemetría

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: De trazas a evaluación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Laboratorio L9: dos cuellos de botella

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: Banco Inti · Laboratorio L9: dos cuellos de botella
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Instrumentar el Space y extraer dos hallazgos respaldados por trazas reales.

CONCEPTO PRINCIPAL
Laboratorio L9: dos cuellos de botella

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un hallazgo útil conecta observación, causa posible y próxima prueba.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una pregunta de comisión genera recuperación repetida y varias llamadas al modelo. Pida una predicción.

Evidencia: Guardar referencias de las ejecuciones representativas.

Hipótesis: La descripción del retriever induce llamadas redundantes.

Siguiente: Proponer una modificación medible para L10.

Resultado esperado: La hipótesis es una explicación por verificar, no un hecho demostrado por una sola traza. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Evidencia; Hipótesis; Siguiente. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una pregunta de comisión genera recuperación repetida y varias llamadas al modelo.
Evidencia: Guardar referencias de las ejecuciones representativas.
Hipótesis: La descripción del retriever induce llamadas redundantes.
Siguiente: Proponer una modificación medible para L10.
Resultado: La hipótesis es una explicación por verificar, no un hecho demostrado por una sola traza.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué traza adicional buscarías para comprobar que el patrón se repite?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un hallazgo útil conecta observación, causa posible y próxima prueba.

ERRORES CONCEPTUALES FRECUENTES
Presentar una sospecha como causa confirmada.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: PII en la telemetría

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia · Sigue: De trazas a evaluación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. De trazas a evaluación

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: De trazas a evaluación
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §6 y conexión S10
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir observar el recorrido y decidir si una versión es mejor.

CONCEPTO PRINCIPAL
De trazas a evaluación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Observar permite formular cambios; evaluar permite defenderlos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué perderías si midieras solo milisegundos?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

S9: Describe cómo ocurrió cada ejecución.

S10: Aplica criterios de calidad a casos comparables.

Decisión: Combina calidad, latencia y costo para aceptar o revertir un cambio.

Cierre con la distinción: Observar permite formular cambios; evaluar permite defenderlos.

ELEMENTOS QUE CONVIENE EXPLICAR
S9; S10; Decisión. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una propuesta elimina una llamada para reducir tiempo.
Observar: La traza confirma menos operaciones.
Evaluar: Comprobar que no empeoran datos ni fundamentación.
Decidir: Aceptar solo con evidencia suficiente sobre los criterios elegidos.
Resultado: Una respuesta más rápida puede ser peor si perdió la fuente necesaria.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué perderías si midieras solo milisegundos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Observar permite formular cambios; evaluar permite defenderlos.

ERRORES CONCEPTUALES FRECUENTES
Usar una traza rápida como prueba de mejora global.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Laboratorio L9: dos cuellos de botella

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. Preparar la línea base

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: Preparar la línea base
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §6 y conexión S10
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir observar el recorrido y decidir si una versión es mejor.

CONCEPTO PRINCIPAL
De trazas a evaluación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Observar permite formular cambios; evaluar permite defenderlos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Conjunto: Usar el dataset del track y conservar sus casos.

Versión: Identificar código, prompt y configuración de la corrida.

Evidencia: Relacionar resultados con trazas y condiciones de ejecución.

Contraste la regla con este error: Usar una traza rápida como prueba de mejora global. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Conjunto; Versión; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una propuesta elimina una llamada para reducir tiempo.
Observar: La traza confirma menos operaciones.
Evaluar: Comprobar que no empeoran datos ni fundamentación.
Decidir: Aceptar solo con evidencia suficiente sobre los criterios elegidos.
Resultado: Una respuesta más rápida puede ser peor si perdió la fuente necesaria.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué perderías si midieras solo milisegundos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Observar permite formular cambios; evaluar permite defenderlos.

ERRORES CONCEPTUALES FRECUENTES
Usar una traza rápida como prueba de mejora global.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Laboratorio L9: dos cuellos de botella

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · De trazas a evaluación

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: MercaSur · De trazas a evaluación
Sesión: Observabilidad y trazabilidad con Langfuse
Archivo: 09-observabilidad-langfuse-editable.pptx
Sección que soporta: §6 y conexión S10
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-09-observabilidad-langfuse; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir observar el recorrido y decidir si una versión es mejor.

CONCEPTO PRINCIPAL
De trazas a evaluación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Observar permite formular cambios; evaluar permite defenderlos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una propuesta elimina una llamada para reducir tiempo. Pida una predicción.

Observar: La traza confirma menos operaciones.

Evaluar: Comprobar que no empeoran datos ni fundamentación.

Decidir: Aceptar solo con evidencia suficiente sobre los criterios elegidos.

Resultado esperado: Una respuesta más rápida puede ser peor si perdió la fuente necesaria. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Observar; Evaluar; Decidir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una propuesta elimina una llamada para reducir tiempo.
Observar: La traza confirma menos operaciones.
Evaluar: Comprobar que no empeoran datos ni fundamentación.
Decidir: Aceptar solo con evidencia suficiente sobre los criterios elegidos.
Resultado: Una respuesta más rápida puede ser peor si perdió la fuente necesaria.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué perderías si midieras solo milisegundos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Observar permite formular cambios; evaluar permite defenderlos.

ERRORES CONCEPTUALES FRECUENTES
Usar una traza rápida como prueba de mejora global.

CONEXIÓN ANTERIOR
S8: API desplegada; S6: protección de datos · Capítulo previo: Laboratorio L9: dos cuellos de botella

CONEXIÓN POSTERIOR
S10: cambiar y medir sobre evidencia.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

