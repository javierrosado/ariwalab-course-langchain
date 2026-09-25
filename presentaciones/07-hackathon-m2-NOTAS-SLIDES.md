# Hackathon, clínica y Proyecto M2 — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Probar comportamiento no determinístico

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Probar comportamiento no determinístico
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Definir invariantes útiles en lugar de comparar frases completas.

CONCEPTO PRINCIPAL
Probar comportamiento no determinístico

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Prueba lo que debe mantenerse, no una redacción exacta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué invariante añadirías además del nombre del plan?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Dato: La respuesta conserva el hecho esperado.

Acción: La tool seleccionada corresponde a la consulta.

Límite: La salida cita cuando corresponde y no expone PII.

Cierre con la distinción: Prueba lo que debe mantenerse, no una redacción exacta.

ELEMENTOS QUE CONVIENE EXPLICAR
Dato; Acción; Límite. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Cinco respuestas usan redacciones distintas para el mismo plan.
Criterio: Deben contener el plan correcto consultado.
Observación: Cuatro cumplen y una omite el dato.
Resultado: Registrar 4/5 y analizar la ejecución fallida.
Resultado: El criterio puede ser estable aunque el texto cambie.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué invariante añadirías además del nombre del plan?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Prueba lo que debe mantenerse, no una redacción exacta.

ERRORES CONCEPTUALES FRECUENTES
Aceptar cualquier texto variable o exigir igualdad literal de toda la respuesta.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados.

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Guardrails y estrés: fallos diferentes

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Repetir para medir

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Repetir para medir
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Definir invariantes útiles en lugar de comparar frases completas.

CONCEPTO PRINCIPAL
Probar comportamiento no determinístico

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Prueba lo que debe mantenerse, no una redacción exacta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Caso: Mantener la consulta y el criterio de aceptación.

Cinco intentos: Registrar cuántas ejecuciones cumplen el criterio.

Lectura: Una tasa observada no equivale a garantía futura.

Contraste la regla con este error: Aceptar cualquier texto variable o exigir igualdad literal de toda la respuesta. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Caso; Cinco intentos; Lectura. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Cinco respuestas usan redacciones distintas para el mismo plan.
Criterio: Deben contener el plan correcto consultado.
Observación: Cuatro cumplen y una omite el dato.
Resultado: Registrar 4/5 y analizar la ejecución fallida.
Resultado: El criterio puede ser estable aunque el texto cambie.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué invariante añadirías además del nombre del plan?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Prueba lo que debe mantenerse, no una redacción exacta.

ERRORES CONCEPTUALES FRECUENTES
Aceptar cualquier texto variable o exigir igualdad literal de toda la respuesta.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados.

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Guardrails y estrés: fallos diferentes

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Probar comportamiento no determinístico

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: AndesMóvil · Probar comportamiento no determinístico
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Definir invariantes útiles en lugar de comparar frases completas.

CONCEPTO PRINCIPAL
Probar comportamiento no determinístico

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Prueba lo que debe mantenerse, no una redacción exacta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Cinco respuestas usan redacciones distintas para el mismo plan. Pida una predicción.

Criterio: Deben contener el plan correcto consultado.

Observación: Cuatro cumplen y una omite el dato.

Resultado: Registrar 4/5 y analizar la ejecución fallida.

Resultado esperado: El criterio puede ser estable aunque el texto cambie. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Criterio; Observación; Resultado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Cinco respuestas usan redacciones distintas para el mismo plan.
Criterio: Deben contener el plan correcto consultado.
Observación: Cuatro cumplen y una omite el dato.
Resultado: Registrar 4/5 y analizar la ejecución fallida.
Resultado: El criterio puede ser estable aunque el texto cambie.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué invariante añadirías además del nombre del plan?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Prueba lo que debe mantenerse, no una redacción exacta.

ERRORES CONCEPTUALES FRECUENTES
Aceptar cualquier texto variable o exigir igualdad literal de toda la respuesta.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados.

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Guardrails y estrés: fallos diferentes

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Guardrails y estrés: fallos diferentes

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Guardrails y estrés: fallos diferentes
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir un ataque deliberado de una falla operativa o entrada ambigua.

CONCEPTO PRINCIPAL
Guardrails y estrés: fallos diferentes

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La clínica trata el entorno como fuente de fallos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué parte de este caso no cubre un filtro de inyección?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

L6: Explora intentos de inyección, filtración y acciones prohibidas.

L7: Explora servicios caídos, datos ausentes y respuestas malformadas.

Complemento: Ambas pruebas buscan comportamientos manejados y observables.

Cierre con la distinción: La clínica trata el entorno como fuente de fallos.

ELEMENTOS QUE CONVIENE EXPLICAR
L6; L7; Complemento. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El servicio responde lentamente en mitad de una conversación legítima.
Distinguir: El usuario no está atacando al agente.
Manejar: Aplicar timeout y respuesta útil según el contrato.
Conservar: Mantener contexto sin inventar un estado de pedido.
Resultado: La resiliencia se prueba también cuando nadie actúa con malicia.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte de este caso no cubre un filtro de inyección?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La clínica trata el entorno como fuente de fallos.

ERRORES CONCEPTUALES FRECUENTES
Usar fallos ocultos o aleatorios como sorpresa evaluativa.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Probar comportamiento no determinístico

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Cuatro familias de casos borde

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Caos anunciado y controlado

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Caos anunciado y controlado
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir un ataque deliberado de una falla operativa o entrada ambigua.

CONCEPTO PRINCIPAL
Guardrails y estrés: fallos diferentes

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La clínica trata el entorno como fuente de fallos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Inicio: El docente anuncia CHAOS_RATE=0.1.

Clínica: Los equipos prueban su propio agente y documentan fallos.

Cierre: La configuración vuelve a 0.0 al terminar.

Contraste la regla con este error: Usar fallos ocultos o aleatorios como sorpresa evaluativa. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Inicio; Clínica; Cierre. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El servicio responde lentamente en mitad de una conversación legítima.
Distinguir: El usuario no está atacando al agente.
Manejar: Aplicar timeout y respuesta útil según el contrato.
Conservar: Mantener contexto sin inventar un estado de pedido.
Resultado: La resiliencia se prueba también cuando nadie actúa con malicia.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte de este caso no cubre un filtro de inyección?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La clínica trata el entorno como fuente de fallos.

ERRORES CONCEPTUALES FRECUENTES
Usar fallos ocultos o aleatorios como sorpresa evaluativa.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Probar comportamiento no determinístico

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Cuatro familias de casos borde

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Guardrails y estrés: fallos diferentes

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: MercaSur · Guardrails y estrés: fallos diferentes
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir un ataque deliberado de una falla operativa o entrada ambigua.

CONCEPTO PRINCIPAL
Guardrails y estrés: fallos diferentes

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La clínica trata el entorno como fuente de fallos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El servicio responde lentamente en mitad de una conversación legítima. Pida una predicción.

Distinguir: El usuario no está atacando al agente.

Manejar: Aplicar timeout y respuesta útil según el contrato.

Conservar: Mantener contexto sin inventar un estado de pedido.

Resultado esperado: La resiliencia se prueba también cuando nadie actúa con malicia. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Distinguir; Manejar; Conservar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El servicio responde lentamente en mitad de una conversación legítima.
Distinguir: El usuario no está atacando al agente.
Manejar: Aplicar timeout y respuesta útil según el contrato.
Conservar: Mantener contexto sin inventar un estado de pedido.
Resultado: La resiliencia se prueba también cuando nadie actúa con malicia.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte de este caso no cubre un filtro de inyección?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La clínica trata el entorno como fuente de fallos.

ERRORES CONCEPTUALES FRECUENTES
Usar fallos ocultos o aleatorios como sorpresa evaluativa.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Probar comportamiento no determinístico

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Cuatro familias de casos borde

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Cuatro familias de casos borde

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Cuatro familias de casos borde
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §0 y §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explorar ambigüedad, ausencia de datos, caída de servicio y contrato inválido.

CONCEPTO PRINCIPAL
Cuatro familias de casos borde

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La prueba de estrés debe localizar un comportamiento concreto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Por qué conviene forzar el fallo después de encontrarlo al azar?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Intención y datos: Dos tareas en un turno o un identificador inexistente.

Servicio: Timeout, error500, error503 o lentitud.

Formato: Respuesta vacía, malformada o fuera del esquema.

Cierre con la distinción: La prueba de estrés debe localizar un comportamiento concreto.

ELEMENTOS QUE CONVIENE EXPLICAR
Intención y datos; Servicio; Formato. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. En el cuarto turno, la consulta de movimientos recibe un 503.
Reproducir: Forzar error503 para aislar la situación.
Observar: Comprobar si conserva el hilo y evita repetir sin límite.
Resolver: Responder que la consulta no pudo completarse y aplicar la política prevista.
Resultado: Un caso reproducible permite comprobar que la corrección aborda la causa.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué conviene forzar el fallo después de encontrarlo al azar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La prueba de estrés debe localizar un comportamiento concreto.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que el modo aleatorio usa indistintamente los seis fallos.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Guardrails y estrés: fallos diferentes

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Clínica de 45 minutos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Forzar y documentar el fallo

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Forzar y documentar el fallo
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §0 y §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explorar ambigüedad, ausencia de datos, caída de servicio y contrato inválido.

CONCEPTO PRINCIPAL
Cuatro familias de casos borde

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La prueba de estrés debe localizar un comportamiento concreto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Dirigido: ?_fallo=<nombre> permite solicitar uno de los seis fallos del simulador.

Aleatorio: CHAOS_RATE sin _fallo inyecta error503 o lento.

Evidencia: Registrar entrada, turno, fallo, resultado y solución.

Contraste la regla con este error: Afirmar que el modo aleatorio usa indistintamente los seis fallos. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Dirigido; Aleatorio; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. En el cuarto turno, la consulta de movimientos recibe un 503.
Reproducir: Forzar error503 para aislar la situación.
Observar: Comprobar si conserva el hilo y evita repetir sin límite.
Resolver: Responder que la consulta no pudo completarse y aplicar la política prevista.
Resultado: Un caso reproducible permite comprobar que la corrección aborda la causa.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué conviene forzar el fallo después de encontrarlo al azar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La prueba de estrés debe localizar un comportamiento concreto.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que el modo aleatorio usa indistintamente los seis fallos.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Guardrails y estrés: fallos diferentes

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Clínica de 45 minutos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Cuatro familias de casos borde

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: Banco Inti · Cuatro familias de casos borde
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §0 y §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explorar ambigüedad, ausencia de datos, caída de servicio y contrato inválido.

CONCEPTO PRINCIPAL
Cuatro familias de casos borde

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La prueba de estrés debe localizar un comportamiento concreto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: En el cuarto turno, la consulta de movimientos recibe un 503. Pida una predicción.

Reproducir: Forzar error503 para aislar la situación.

Observar: Comprobar si conserva el hilo y evita repetir sin límite.

Resolver: Responder que la consulta no pudo completarse y aplicar la política prevista.

Resultado esperado: Un caso reproducible permite comprobar que la corrección aborda la causa. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Reproducir; Observar; Resolver. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. En el cuarto turno, la consulta de movimientos recibe un 503.
Reproducir: Forzar error503 para aislar la situación.
Observar: Comprobar si conserva el hilo y evita repetir sin límite.
Resolver: Responder que la consulta no pudo completarse y aplicar la política prevista.
Resultado: Un caso reproducible permite comprobar que la corrección aborda la causa.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué conviene forzar el fallo después de encontrarlo al azar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La prueba de estrés debe localizar un comportamiento concreto.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que el modo aleatorio usa indistintamente los seis fallos.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Guardrails y estrés: fallos diferentes

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Clínica de 45 minutos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. Clínica de 45 minutos

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: Clínica de 45 minutos
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Organizar la exploración para terminar con casos resueltos y evidencia.

CONCEPTO PRINCIPAL
Clínica de 45 minutos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La clínica termina con evidencia de corrección, no con una lista de síntomas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué variación usarías para verificar que la solución se generaliza?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Minutos 0–20: Entrada ambigua y dato ausente en conversación.

Minutos 20–40: Servicio caído y salida fuera de formato.

Minutos 40–45: Elegir el peor fallo resuelto para abrir la demo.

Cierre con la distinción: La clínica termina con evidencia de corrección, no con una lista de síntomas.

ELEMENTOS QUE CONVIENE EXPLICAR
Minutos 0–20; Minutos 20–40; Minutos 40–45. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El agente responde solo una de dos preguntas sobre póliza y siniestro.
Hallazgo: La segunda intención queda sin atender.
Solución: Hacer explícito qué resolvió y qué falta consultar.
Prueba: Repetir con el orden de preguntas invertido.
Resultado: Documentar diez fallos sin resolverlos no completa el objetivo del laboratorio.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué variación usarías para verificar que la solución se generaliza?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La clínica termina con evidencia de corrección, no con una lista de síntomas.

ERRORES CONCEPTUALES FRECUENTES
Confundir incidente encontrado con caso resuelto.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Cuatro familias de casos borde

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Demo y argumentación del Proyecto M2

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. De hallazgo a caso resuelto

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: De hallazgo a caso resuelto
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Organizar la exploración para terminar con casos resueltos y evidencia.

CONCEPTO PRINCIPAL
Clínica de 45 minutos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La clínica termina con evidencia de corrección, no con una lista de síntomas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Reproducir: Conservar la entrada y el estado que disparan el fallo.

Corregir: Aplicar un cambio relacionado con la causa.

Verificar: Repetir el caso y revisar efectos sobre consultas cercanas.

Contraste la regla con este error: Confundir incidente encontrado con caso resuelto. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Reproducir; Corregir; Verificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El agente responde solo una de dos preguntas sobre póliza y siniestro.
Hallazgo: La segunda intención queda sin atender.
Solución: Hacer explícito qué resolvió y qué falta consultar.
Prueba: Repetir con el orden de preguntas invertido.
Resultado: Documentar diez fallos sin resolverlos no completa el objetivo del laboratorio.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué variación usarías para verificar que la solución se generaliza?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La clínica termina con evidencia de corrección, no con una lista de síntomas.

ERRORES CONCEPTUALES FRECUENTES
Confundir incidente encontrado con caso resuelto.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Cuatro familias de casos borde

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Demo y argumentación del Proyecto M2

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · Clínica de 45 minutos

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: Andina Seguros · Clínica de 45 minutos
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Organizar la exploración para terminar con casos resueltos y evidencia.

CONCEPTO PRINCIPAL
Clínica de 45 minutos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La clínica termina con evidencia de corrección, no con una lista de síntomas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El agente responde solo una de dos preguntas sobre póliza y siniestro. Pida una predicción.

Hallazgo: La segunda intención queda sin atender.

Solución: Hacer explícito qué resolvió y qué falta consultar.

Prueba: Repetir con el orden de preguntas invertido.

Resultado esperado: Documentar diez fallos sin resolverlos no completa el objetivo del laboratorio. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Hallazgo; Solución; Prueba. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El agente responde solo una de dos preguntas sobre póliza y siniestro.
Hallazgo: La segunda intención queda sin atender.
Solución: Hacer explícito qué resolvió y qué falta consultar.
Prueba: Repetir con el orden de preguntas invertido.
Resultado: Documentar diez fallos sin resolverlos no completa el objetivo del laboratorio.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué variación usarías para verificar que la solución se generaliza?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La clínica termina con evidencia de corrección, no con una lista de síntomas.

ERRORES CONCEPTUALES FRECUENTES
Confundir incidente encontrado con caso resuelto.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Cuatro familias de casos borde

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Demo y argumentación del Proyecto M2

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Demo y argumentación del Proyecto M2

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Demo y argumentación del Proyecto M2
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §3 y §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mostrar el peor fallo resuelto y justificar la decisión que lo corrigió.

CONCEPTO PRINCIPAL
Demo y argumentación del Proyecto M2

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una buena sustentación conecta el diseño con evidencia observable.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué pregunta técnica harías al equipo sobre su corrección?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Problema: Qué ocurrió y por qué importa para el usuario.

Cambio: Qué decisión de diseño se aplicó.

Evidencia: Cómo se comprobó la mejora y qué límite permanece.

Cierre con la distinción: Una buena sustentación conecta el diseño con evidencia observable.

ELEMENTOS QUE CONVIENE EXPLICAR
Problema; Cambio; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un timeout podía provocar una devolución duplicada.
Mostrar: Describir la secuencia que repetía la operación.
Corregir: Separar reintento técnico y efecto de negocio.
Probar: Verificar que repetir la solicitud no duplica el efecto previsto.
Resultado: La demo muestra conocimiento de los fallos y de sus consecuencias.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué pregunta técnica harías al equipo sobre su corrección?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una buena sustentación conecta el diseño con evidencia observable.

ERRORES CONCEPTUALES FRECUENTES
Abrir únicamente con el caso feliz y ocultar los límites.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Clínica de 45 minutos

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Cerrar M2 y preparar producción

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Preparar una exposición breve

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Preparar una exposición breve
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §3 y §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mostrar el peor fallo resuelto y justificar la decisión que lo corrigió.

CONCEPTO PRINCIPAL
Demo y argumentación del Proyecto M2

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una buena sustentación conecta el diseño con evidencia observable.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Abrir: Mostrar el caso que antes fallaba.

Demostrar: Ejecutar el comportamiento corregido.

Argumentar: Explicar criterio, alternativa y resultado sin narrar todo el código.

Contraste la regla con este error: Abrir únicamente con el caso feliz y ocultar los límites. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Abrir; Demostrar; Argumentar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un timeout podía provocar una devolución duplicada.
Mostrar: Describir la secuencia que repetía la operación.
Corregir: Separar reintento técnico y efecto de negocio.
Probar: Verificar que repetir la solicitud no duplica el efecto previsto.
Resultado: La demo muestra conocimiento de los fallos y de sus consecuencias.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué pregunta técnica harías al equipo sobre su corrección?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una buena sustentación conecta el diseño con evidencia observable.

ERRORES CONCEPTUALES FRECUENTES
Abrir únicamente con el caso feliz y ocultar los límites.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Clínica de 45 minutos

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Cerrar M2 y preparar producción

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Demo y argumentación del Proyecto M2

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: MercaSur · Demo y argumentación del Proyecto M2
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §3 y §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mostrar el peor fallo resuelto y justificar la decisión que lo corrigió.

CONCEPTO PRINCIPAL
Demo y argumentación del Proyecto M2

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una buena sustentación conecta el diseño con evidencia observable.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Un timeout podía provocar una devolución duplicada. Pida una predicción.

Mostrar: Describir la secuencia que repetía la operación.

Corregir: Separar reintento técnico y efecto de negocio.

Probar: Verificar que repetir la solicitud no duplica el efecto previsto.

Resultado esperado: La demo muestra conocimiento de los fallos y de sus consecuencias. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Mostrar; Corregir; Probar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un timeout podía provocar una devolución duplicada.
Mostrar: Describir la secuencia que repetía la operación.
Corregir: Separar reintento técnico y efecto de negocio.
Probar: Verificar que repetir la solicitud no duplica el efecto previsto.
Resultado: La demo muestra conocimiento de los fallos y de sus consecuencias.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué pregunta técnica harías al equipo sobre su corrección?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una buena sustentación conecta el diseño con evidencia observable.

ERRORES CONCEPTUALES FRECUENTES
Abrir únicamente con el caso feliz y ocultar los límites.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Clínica de 45 minutos

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal · Sigue: Cerrar M2 y preparar producción

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Cerrar M2 y preparar producción

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Cerrar M2 y preparar producción
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §4–§5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Consolidar un checkpoint probado antes de desplegarlo.

CONCEPTO PRINCIPAL
Cerrar M2 y preparar producción

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La calidad del despliegue empieza antes de subir el código.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué dependencia oculta podría romper el arranque en la nube?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Agente integrado: Tools, RAG, memoria y guardrails.

Casos borde: Al menos diez documentados y resueltos.

Diseño: Explicación de decisiones y alcance del sistema.

Cierre con la distinción: La calidad del despliegue empieza antes de subir el código.

ELEMENTOS QUE CONVIENE EXPLICAR
Agente integrado; Casos borde; Diseño. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La demo funciona solo en la laptop de una persona.
Detectar: Faltan dependencias o variables documentadas.
Completar: Revisar el entorno y los pasos de arranque.
Comprobar: Otro integrante ejecuta el mismo caso y sus pruebas.
Resultado: Un checkpoint reproducible es una mejor base para el contenedor de S8.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dependencia oculta podría romper el arranque en la nube?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La calidad del despliegue empieza antes de subir el código.

ERRORES CONCEPTUALES FRECUENTES
Confundir una demo local exitosa con disponibilidad en producción.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Demo y argumentación del Proyecto M2

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Preparar el salto a S8

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Preparar el salto a S8
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §4–§5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Consolidar un checkpoint probado antes de desplegarlo.

CONCEPTO PRINCIPAL
Cerrar M2 y preparar producción

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La calidad del despliegue empieza antes de subir el código.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Reproducibilidad: Otro integrante puede ejecutar el checkpoint.

Configuración: Separar secretos y valores por entorno.

Límites: Registrar qué depende de memoria del proceso o servicios externos.

Contraste la regla con este error: Confundir una demo local exitosa con disponibilidad en producción. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Reproducibilidad; Configuración; Límites. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La demo funciona solo en la laptop de una persona.
Detectar: Faltan dependencias o variables documentadas.
Completar: Revisar el entorno y los pasos de arranque.
Comprobar: Otro integrante ejecuta el mismo caso y sus pruebas.
Resultado: Un checkpoint reproducible es una mejor base para el contenedor de S8.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dependencia oculta podría romper el arranque en la nube?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La calidad del despliegue empieza antes de subir el código.

ERRORES CONCEPTUALES FRECUENTES
Confundir una demo local exitosa con disponibilidad en producción.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Demo y argumentación del Proyecto M2

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Cerrar M2 y preparar producción

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: AndesMóvil · Cerrar M2 y preparar producción
Sesión: Hackathon, clínica y Proyecto M2
Archivo: 07-hackathon-m2-editable.pptx
Sección que soporta: §4–§5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-07-hackathon-m2; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Consolidar un checkpoint probado antes de desplegarlo.

CONCEPTO PRINCIPAL
Cerrar M2 y preparar producción

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La calidad del despliegue empieza antes de subir el código.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La demo funciona solo en la laptop de una persona. Pida una predicción.

Detectar: Faltan dependencias o variables documentadas.

Completar: Revisar el entorno y los pasos de arranque.

Comprobar: Otro integrante ejecuta el mismo caso y sus pruebas.

Resultado esperado: Un checkpoint reproducible es una mejor base para el contenedor de S8. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Detectar; Completar; Comprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La demo funciona solo en la laptop de una persona.
Detectar: Faltan dependencias o variables documentadas.
Completar: Revisar el entorno y los pasos de arranque.
Comprobar: Otro integrante ejecuta el mismo caso y sus pruebas.
Resultado: Un checkpoint reproducible es una mejor base para el contenedor de S8.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dependencia oculta podría romper el arranque en la nube?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La calidad del despliegue empieza antes de subir el código.

ERRORES CONCEPTUALES FRECUENTES
Confundir una demo local exitosa con disponibilidad en producción.

CONEXIÓN ANTERIOR
S6: controles ante ataques deliberados · Capítulo previo: Demo y argumentación del Proyecto M2

CONEXIÓN POSTERIOR
S8: despliegue; S10: evaluación formal.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

