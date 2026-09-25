# Evaluación y optimización continua — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Mejorar con evidencia

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Mejorar con evidencia
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Medir una línea base, cambiar una cosa y volver a medir.

CONCEPTO PRINCIPAL
Mejorar con evidencia

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una mejora defendible tiene línea base, cambio y evidencia.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué sabrías si v2 mejora después de cambiar modelo, prompt y corpus a la vez?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

v1: Resultados del sistema antes de la modificación.

Intervención: Un cambio dirigido a un cuello de botella de L9.

v2: Mismos casos y criterios para comparar el efecto.

Cierre con la distinción: Una mejora defendible tiene línea base, cambio y evidencia.

ELEMENTOS QUE CONVIENE EXPLICAR
v1; Intervención; v2. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El equipo reduce una instrucción redundante del prompt.
Medir: Ejecutar v1 sobre los treinta casos.
Cambiar: Editar solo la instrucción elegida.
Comparar: Revisar aciertos, tokens y latencia en v2.
Resultado: Si cambian varias piezas a la vez, atribuir el resultado se vuelve difícil.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué sabrías si v2 mejora después de cambiar modelo, prompt y corpus a la vez?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una mejora defendible tiene línea base, cambio y evidencia.

ERRORES CONCEPTUALES FRECUENTES
Optimizar por intuición o seleccionar solo casos favorables.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados.

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: El golden dataset del curso

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Controlar la comparación

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Controlar la comparación
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Medir una línea base, cambiar una cosa y volver a medir.

CONCEPTO PRINCIPAL
Mejorar con evidencia

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una mejora defendible tiene línea base, cambio y evidencia.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Constantes: Mantener dataset y condiciones relevantes.

Variable: Nombrar exactamente qué cambió.

Decisión: Conservar o revertir según calidad y costo operativo.

Contraste la regla con este error: Optimizar por intuición o seleccionar solo casos favorables. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Constantes; Variable; Decisión. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El equipo reduce una instrucción redundante del prompt.
Medir: Ejecutar v1 sobre los treinta casos.
Cambiar: Editar solo la instrucción elegida.
Comparar: Revisar aciertos, tokens y latencia en v2.
Resultado: Si cambian varias piezas a la vez, atribuir el resultado se vuelve difícil.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué sabrías si v2 mejora después de cambiar modelo, prompt y corpus a la vez?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una mejora defendible tiene línea base, cambio y evidencia.

ERRORES CONCEPTUALES FRECUENTES
Optimizar por intuición o seleccionar solo casos favorables.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados.

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: El golden dataset del curso

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Mejorar con evidencia

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: AndesMóvil · Mejorar con evidencia
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Medir una línea base, cambiar una cosa y volver a medir.

CONCEPTO PRINCIPAL
Mejorar con evidencia

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una mejora defendible tiene línea base, cambio y evidencia.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El equipo reduce una instrucción redundante del prompt. Pida una predicción.

Medir: Ejecutar v1 sobre los treinta casos.

Cambiar: Editar solo la instrucción elegida.

Comparar: Revisar aciertos, tokens y latencia en v2.

Resultado esperado: Si cambian varias piezas a la vez, atribuir el resultado se vuelve difícil. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Medir; Cambiar; Comparar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El equipo reduce una instrucción redundante del prompt.
Medir: Ejecutar v1 sobre los treinta casos.
Cambiar: Editar solo la instrucción elegida.
Comparar: Revisar aciertos, tokens y latencia en v2.
Resultado: Si cambian varias piezas a la vez, atribuir el resultado se vuelve difícil.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué sabrías si v2 mejora después de cambiar modelo, prompt y corpus a la vez?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una mejora defendible tiene línea base, cambio y evidencia.

ERRORES CONCEPTUALES FRECUENTES
Optimizar por intuición o seleccionar solo casos favorables.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados.

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: El golden dataset del curso

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. El golden dataset del curso

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: El golden dataset del curso
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer la continuidad de los treinta casos por track.

CONCEPTO PRINCIPAL
El golden dataset del curso

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La evaluación depende tanto de los casos como del criterio.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué significa que un evaluator apruebe por definición un campo None?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

S2 y S4: Veinte casos con tool esperada ayudan a clasificar y seleccionar.

S5: Los casos OTRO amplían el trabajo con conocimiento del dominio.

S10: Los treinta casos permiten comparar versiones con el mismo conjunto.

Cierre con la distinción: La evaluación depende tanto de los casos como del criterio.

ELEMENTOS QUE CONVIENE EXPLICAR
S2 y S4; S5; S10. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una fila pide un dato y otra corresponde a una interacción sin dato verificable.
Distinguir: No todas las filas exigen una tool o una cifra.
Configurar: Interpretar los campos esperados del dataset.
Reportar: No atribuir exactitud semántica a un criterio marcado como no aplicable.
Resultado: Conocer el contrato del dataset evita interpretar mal sus porcentajes.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué significa que un evaluator apruebe por definición un campo None?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La evaluación depende tanto de los casos como del criterio.

ERRORES CONCEPTUALES FRECUENTES
Contar una no aplicabilidad como evidencia de un hecho correcto.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Mejorar con evidencia

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Tres evaluadores determinísticos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Leer una fila antes de evaluar

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Leer una fila antes de evaluar
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer la continuidad de los treinta casos por track.

CONCEPTO PRINCIPAL
El golden dataset del curso

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La evaluación depende tanto de los casos como del criterio.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Consulta: Entrada exacta del caso.

Esperado: tool_esperada y respuesta_esperada definen comprobaciones.

Aplicabilidad: Un campo None puede indicar que ese criterio no aplica.

Contraste la regla con este error: Contar una no aplicabilidad como evidencia de un hecho correcto. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Consulta; Esperado; Aplicabilidad. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una fila pide un dato y otra corresponde a una interacción sin dato verificable.
Distinguir: No todas las filas exigen una tool o una cifra.
Configurar: Interpretar los campos esperados del dataset.
Reportar: No atribuir exactitud semántica a un criterio marcado como no aplicable.
Resultado: Conocer el contrato del dataset evita interpretar mal sus porcentajes.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué significa que un evaluator apruebe por definición un campo None?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La evaluación depende tanto de los casos como del criterio.

ERRORES CONCEPTUALES FRECUENTES
Contar una no aplicabilidad como evidencia de un hecho correcto.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Mejorar con evidencia

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Tres evaluadores determinísticos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · El golden dataset del curso

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: Banco Inti · El golden dataset del curso
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer la continuidad de los treinta casos por track.

CONCEPTO PRINCIPAL
El golden dataset del curso

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La evaluación depende tanto de los casos como del criterio.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una fila pide un dato y otra corresponde a una interacción sin dato verificable. Pida una predicción.

Distinguir: No todas las filas exigen una tool o una cifra.

Configurar: Interpretar los campos esperados del dataset.

Reportar: No atribuir exactitud semántica a un criterio marcado como no aplicable.

Resultado esperado: Conocer el contrato del dataset evita interpretar mal sus porcentajes. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Distinguir; Configurar; Reportar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una fila pide un dato y otra corresponde a una interacción sin dato verificable.
Distinguir: No todas las filas exigen una tool o una cifra.
Configurar: Interpretar los campos esperados del dataset.
Reportar: No atribuir exactitud semántica a un criterio marcado como no aplicable.
Resultado: Conocer el contrato del dataset evita interpretar mal sus porcentajes.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué significa que un evaluator apruebe por definición un campo None?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La evaluación depende tanto de los casos como del criterio.

ERRORES CONCEPTUALES FRECUENTES
Contar una no aplicabilidad como evidencia de un hecho correcto.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Mejorar con evidencia

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Tres evaluadores determinísticos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Tres evaluadores determinísticos

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Tres evaluadores determinísticos
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §2 y comun/evaluadores.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar qué comprueba realmente cada función del repositorio.

CONCEPTO PRINCIPAL
Tres evaluadores determinísticos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué falso positivo puede pasar si solo buscas una subcadena?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Tool: Compara nombre llamado y nombre esperado, incluyendo ausencia de llamada.

Exactitud: Busca respuesta_esperada como subcadena sin distinguir mayúsculas.

Groundedness: Exige ese dato tanto en la respuesta como en el contexto recuperado.

Cierre con la distinción: Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

ELEMENTOS QUE CONVIENE EXPLICAR
Tool; Exactitud; Groundedness. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Dato esperado didáctico: «30 días»; respuesta: «no son 30 días».
Evaluar: La subcadena «30 días» está presente.
Detectar límite: La comprobación lexical puede aprobar una negación incorrecta.
Revisar: Interpretar el resultado con el texto y la fuente.
Resultado: Este caso ilustra un límite del código; no cambia los criterios de calificación del curso.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falso positivo puede pasar si solo buscas una subcadena?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que la función valida semánticamente una cita completa.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: El golden dataset del curso

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: LLM-as-judge: uso y sesgos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Límites de estas comprobaciones

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Límites de estas comprobaciones
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §2 y comun/evaluadores.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar qué comprueba realmente cada función del repositorio.

CONCEPTO PRINCIPAL
Tres evaluadores determinísticos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Repetibilidad: Misma entrada produce el mismo resultado del evaluator.

Cobertura: Una coincidencia textual no interpreta todas las negaciones o relaciones.

Complemento: Revisar casos dudosos y distinguir métrica del concepto completo.

Contraste la regla con este error: Afirmar que la función valida semánticamente una cita completa. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Repetibilidad; Cobertura; Complemento. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Dato esperado didáctico: «30 días»; respuesta: «no son 30 días».
Evaluar: La subcadena «30 días» está presente.
Detectar límite: La comprobación lexical puede aprobar una negación incorrecta.
Revisar: Interpretar el resultado con el texto y la fuente.
Resultado: Este caso ilustra un límite del código; no cambia los criterios de calificación del curso.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falso positivo puede pasar si solo buscas una subcadena?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que la función valida semánticamente una cita completa.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: El golden dataset del curso

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: LLM-as-judge: uso y sesgos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Tres evaluadores determinísticos

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: Andina Seguros · Tres evaluadores determinísticos
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §2 y comun/evaluadores.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar qué comprueba realmente cada función del repositorio.

CONCEPTO PRINCIPAL
Tres evaluadores determinísticos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Dato esperado didáctico: «30 días»; respuesta: «no son 30 días». Pida una predicción.

Evaluar: La subcadena «30 días» está presente.

Detectar límite: La comprobación lexical puede aprobar una negación incorrecta.

Revisar: Interpretar el resultado con el texto y la fuente.

Resultado esperado: Este caso ilustra un límite del código; no cambia los criterios de calificación del curso. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Evaluar; Detectar límite; Revisar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Dato esperado didáctico: «30 días»; respuesta: «no son 30 días».
Evaluar: La subcadena «30 días» está presente.
Detectar límite: La comprobación lexical puede aprobar una negación incorrecta.
Revisar: Interpretar el resultado con el texto y la fuente.
Resultado: Este caso ilustra un límite del código; no cambia los criterios de calificación del curso.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falso positivo puede pasar si solo buscas una subcadena?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un evaluator es exacto respecto a su regla, no respecto a todo el significado.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que la función valida semánticamente una cita completa.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: El golden dataset del curso

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: LLM-as-judge: uso y sesgos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. LLM-as-judge: uso y sesgos

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: LLM-as-judge: uso y sesgos
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Contrastar un juicio del modelo con los criterios determinísticos del curso.

CONCEPTO PRINCIPAL
LLM-as-judge: uso y sesgos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
No confundas una evaluación del modelo con una verdad independiente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué cambiarías para explorar un sesgo de posición en A/B?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Juez: Un modelo puntúa o compara respuestas según instrucciones.

Utilidad: Puede aportar juicios sobre tono y utilidad.

Sesgos: Posición, verbosidad y autoevaluación pueden influir.

Cierre con la distinción: No confundas una evaluación del modelo con una verdad independiente.

ELEMENTOS QUE CONVIENE EXPLICAR
Juez; Utilidad; Sesgos. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una respuesta larga suena convincente, pero contiene un estado de pedido falso.
Juez: Puede valorar claridad o detalle de forma favorable.
Dato: La comprobación del estado revela la discrepancia.
Discusión: Separar estilo útil y contenido correcto.
Resultado: El desacuerdo sirve para analizar el criterio y los límites del juez.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué cambiarías para explorar un sesgo de posición en A/B?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: No confundas una evaluación del modelo con una verdad independiente.

ERRORES CONCEPTUALES FRECUENTES
Presentar el juez como árbitro infalible o como sustituto automático del dataset.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Tres evaluadores determinísticos

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Mejora, variación y repetición

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Diseñar la demostración

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Diseñar la demostración
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Contrastar un juicio del modelo con los criterios determinísticos del curso.

CONCEPTO PRINCIPAL
LLM-as-judge: uso y sesgos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
No confundas una evaluación del modelo con una verdad independiente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Base: Tomar diez casos ya puntuados por los evaluators.

Comparación: Presentar las dos columnas y localizar desacuerdos.

Límite: La calificación del curso se sostiene en los criterios determinísticos.

Contraste la regla con este error: Presentar el juez como árbitro infalible o como sustituto automático del dataset. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Base; Comparación; Límite. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una respuesta larga suena convincente, pero contiene un estado de pedido falso.
Juez: Puede valorar claridad o detalle de forma favorable.
Dato: La comprobación del estado revela la discrepancia.
Discusión: Separar estilo útil y contenido correcto.
Resultado: El desacuerdo sirve para analizar el criterio y los límites del juez.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué cambiarías para explorar un sesgo de posición en A/B?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: No confundas una evaluación del modelo con una verdad independiente.

ERRORES CONCEPTUALES FRECUENTES
Presentar el juez como árbitro infalible o como sustituto automático del dataset.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Tres evaluadores determinísticos

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Mejora, variación y repetición

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · LLM-as-judge: uso y sesgos

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: MercaSur · LLM-as-judge: uso y sesgos
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Contrastar un juicio del modelo con los criterios determinísticos del curso.

CONCEPTO PRINCIPAL
LLM-as-judge: uso y sesgos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
No confundas una evaluación del modelo con una verdad independiente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una respuesta larga suena convincente, pero contiene un estado de pedido falso. Pida una predicción.

Juez: Puede valorar claridad o detalle de forma favorable.

Dato: La comprobación del estado revela la discrepancia.

Discusión: Separar estilo útil y contenido correcto.

Resultado esperado: El desacuerdo sirve para analizar el criterio y los límites del juez. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Juez; Dato; Discusión. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una respuesta larga suena convincente, pero contiene un estado de pedido falso.
Juez: Puede valorar claridad o detalle de forma favorable.
Dato: La comprobación del estado revela la discrepancia.
Discusión: Separar estilo útil y contenido correcto.
Resultado: El desacuerdo sirve para analizar el criterio y los límites del juez.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué cambiarías para explorar un sesgo de posición en A/B?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: No confundas una evaluación del modelo con una verdad independiente.

ERRORES CONCEPTUALES FRECUENTES
Presentar el juez como árbitro infalible o como sustituto automático del dataset.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Tres evaluadores determinísticos

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Mejora, variación y repetición

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Mejora, variación y repetición

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Mejora, variación y repetición
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Interpretar una diferencia pequeña sin convertirla en certeza estadística.

CONCEPTO PRINCIPAL
Mejora, variación y repetición

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Reportar incertidumbre forma parte de medir bien.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué harías si mejora la media pero empeoran siempre los mismos casos críticos?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

v1 ilustrativa: 24/30 = 80,0 % de aciertos.

v2 ilustrativa: 26/30 ≈ 86,7 % de aciertos.

Pregunta: ¿Se sostiene la diferencia y qué casos cambiaron?

Cierre con la distinción: Reportar incertidumbre forma parte de medir bien.

ELEMENTOS QUE CONVIENE EXPLICAR
v1 ilustrativa; v2 ilustrativa; Pregunta. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. v2 gana dos casos en una corrida y los pierde en la siguiente.
Observar: La diferencia no se mantiene.
Investigar: Revisar variación de selección y de condiciones.
Reportar: Explicar que la evidencia aún no sostiene la mejora.
Resultado: Las cifras son ilustrativas; el informe debe usar mediciones del equipo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías si mejora la media pero empeoran siempre los mismos casos críticos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Reportar incertidumbre forma parte de medir bien.

ERRORES CONCEPTUALES FRECUENTES
Llamar mejora real a cualquier aumento en una sola ejecución.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: LLM-as-judge: uso y sesgos

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Laboratorio L10: un cambio dirigido

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Regla operativa del curso

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Regla operativa del curso
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Interpretar una diferencia pequeña sin convertirla en certeza estadística.

CONCEPTO PRINCIPAL
Mejora, variación y repetición

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Reportar incertidumbre forma parte de medir bien.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Repetir: Comprobar la mejora en dos corridas.

Identificar: Señalar el cambio aplicado y los casos ganados o perdidos.

Limitar: La regla es pedagógica; no demuestra significancia estadística.

Contraste la regla con este error: Llamar mejora real a cualquier aumento en una sola ejecución. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Repetir; Identificar; Limitar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. v2 gana dos casos en una corrida y los pierde en la siguiente.
Observar: La diferencia no se mantiene.
Investigar: Revisar variación de selección y de condiciones.
Reportar: Explicar que la evidencia aún no sostiene la mejora.
Resultado: Las cifras son ilustrativas; el informe debe usar mediciones del equipo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías si mejora la media pero empeoran siempre los mismos casos críticos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Reportar incertidumbre forma parte de medir bien.

ERRORES CONCEPTUALES FRECUENTES
Llamar mejora real a cualquier aumento en una sola ejecución.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: LLM-as-judge: uso y sesgos

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Laboratorio L10: un cambio dirigido

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Mejora, variación y repetición

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: Banco Inti · Mejora, variación y repetición
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Interpretar una diferencia pequeña sin convertirla en certeza estadística.

CONCEPTO PRINCIPAL
Mejora, variación y repetición

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Reportar incertidumbre forma parte de medir bien.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: v2 gana dos casos en una corrida y los pierde en la siguiente. Pida una predicción.

Observar: La diferencia no se mantiene.

Investigar: Revisar variación de selección y de condiciones.

Reportar: Explicar que la evidencia aún no sostiene la mejora.

Resultado esperado: Las cifras son ilustrativas; el informe debe usar mediciones del equipo. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Observar; Investigar; Reportar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. v2 gana dos casos en una corrida y los pierde en la siguiente.
Observar: La diferencia no se mantiene.
Investigar: Revisar variación de selección y de condiciones.
Reportar: Explicar que la evidencia aún no sostiene la mejora.
Resultado: Las cifras son ilustrativas; el informe debe usar mediciones del equipo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías si mejora la media pero empeoran siempre los mismos casos críticos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Reportar incertidumbre forma parte de medir bien.

ERRORES CONCEPTUALES FRECUENTES
Llamar mejora real a cualquier aumento en una sola ejecución.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: LLM-as-judge: uso y sesgos

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Laboratorio L10: un cambio dirigido

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Laboratorio L10: un cambio dirigido

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Laboratorio L10: un cambio dirigido
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar v1 y v2 en Langfuse Datasets con una intervención trazable.

CONCEPTO PRINCIPAL
Laboratorio L10: un cambio dirigido

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La optimización debe conservar el propósito del agente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué resultado te haría revertir una versión más barata?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Preparar: Cargar los treinta casos del track.

Ejecutar: Medir v1 y aplicar una modificación ligada a L9.

Decidir: Medir v2 y justificar conservar o revertir.

Cierre con la distinción: La optimización debe conservar el propósito del agente.

ELEMENTOS QUE CONVIENE EXPLICAR
Preparar; Ejecutar; Decidir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El retriever devuelve contexto redundante que incrementa tokens.
Hipótesis: Reducir redundancia puede bajar costo.
Prueba: Comparar el mismo dataset con la modificación.
Decisión: Revertir si la reducción deja cláusulas sin respaldo.
Resultado: Ahorrar tokens no justifica perder el contexto decisivo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué resultado te haría revertir una versión más barata?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La optimización debe conservar el propósito del agente.

ERRORES CONCEPTUALES FRECUENTES
Reportar solo la métrica que mejoró y omitir regresiones.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Mejora, variación y repetición

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Preparar evidencia para la sustentación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Qué debe contener el informe

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Qué debe contener el informe
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar v1 y v2 en Langfuse Datasets con una intervención trazable.

CONCEPTO PRINCIPAL
Laboratorio L10: un cambio dirigido

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La optimización debe conservar el propósito del agente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Cambio: Descripción concreta de la pieza modificada.

Resultados: Métricas comparables y casos que explican las diferencias.

Consecuencia: Beneficio, regresión o límite que afecta la decisión.

Contraste la regla con este error: Reportar solo la métrica que mejoró y omitir regresiones. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Cambio; Resultados; Consecuencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El retriever devuelve contexto redundante que incrementa tokens.
Hipótesis: Reducir redundancia puede bajar costo.
Prueba: Comparar el mismo dataset con la modificación.
Decisión: Revertir si la reducción deja cláusulas sin respaldo.
Resultado: Ahorrar tokens no justifica perder el contexto decisivo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué resultado te haría revertir una versión más barata?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La optimización debe conservar el propósito del agente.

ERRORES CONCEPTUALES FRECUENTES
Reportar solo la métrica que mejoró y omitir regresiones.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Mejora, variación y repetición

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Preparar evidencia para la sustentación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Laboratorio L10: un cambio dirigido

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: Andina Seguros · Laboratorio L10: un cambio dirigido
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar v1 y v2 en Langfuse Datasets con una intervención trazable.

CONCEPTO PRINCIPAL
Laboratorio L10: un cambio dirigido

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La optimización debe conservar el propósito del agente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El retriever devuelve contexto redundante que incrementa tokens. Pida una predicción.

Hipótesis: Reducir redundancia puede bajar costo.

Prueba: Comparar el mismo dataset con la modificación.

Decisión: Revertir si la reducción deja cláusulas sin respaldo.

Resultado esperado: Ahorrar tokens no justifica perder el contexto decisivo. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Hipótesis; Prueba; Decisión. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El retriever devuelve contexto redundante que incrementa tokens.
Hipótesis: Reducir redundancia puede bajar costo.
Prueba: Comparar el mismo dataset con la modificación.
Decisión: Revertir si la reducción deja cláusulas sin respaldo.
Resultado: Ahorrar tokens no justifica perder el contexto decisivo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué resultado te haría revertir una versión más barata?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La optimización debe conservar el propósito del agente.

ERRORES CONCEPTUALES FRECUENTES
Reportar solo la métrica que mejoró y omitir regresiones.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Mejora, variación y repetición

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel · Sigue: Preparar evidencia para la sustentación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. Preparar evidencia para la sustentación

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: Preparar evidencia para la sustentación
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §6 y conexión S11
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Convertir la comparación técnica en una explicación que el panel pueda revisar.

CONCEPTO PRINCIPAL
Preparar evidencia para la sustentación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La evidencia sirve para decidir, no solo para mostrar porcentajes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué pregunta del panel pondría a prueba tu interpretación de los datos?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Problema: Un cuello de botella medido en L9.

Decisión: Una modificación concreta aplicada en L10.

Resultado: Qué mejoró, qué no y con qué evidencia.

Cierre con la distinción: La evidencia sirve para decidir, no solo para mostrar porcentajes.

ELEMENTOS QUE CONVIENE EXPLICAR
Problema; Decisión; Resultado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. La nueva versión responde más rápido, pero falla una consulta de devolución.
Explicar: Mostrar tanto latencia como el caso perdido.
Valorar: La devolución puede tener mayor consecuencia que un saludo.
Defender: Justificar si se revierte o se investiga antes de entregar.
Resultado: Una conclusión útil explica la decisión de producto y su costo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué pregunta del panel pondría a prueba tu interpretación de los datos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La evidencia sirve para decidir, no solo para mostrar porcentajes.

ERRORES CONCEPTUALES FRECUENTES
Presentar un número sin dataset, versión o criterio.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Laboratorio L10: un cambio dirigido

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. De números a argumento

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: De números a argumento
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §6 y conexión S11
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Convertir la comparación técnica en una explicación que el panel pueda revisar.

CONCEPTO PRINCIPAL
Preparar evidencia para la sustentación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La evidencia sirve para decidir, no solo para mostrar porcentajes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Contexto: Nombrar dataset y versión comparada.

Criterio: Decir qué umbral o compensación importaba al caso.

Límite: Reconocer tamaño de muestra y casos todavía problemáticos.

Contraste la regla con este error: Presentar un número sin dataset, versión o criterio. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Contexto; Criterio; Límite. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. La nueva versión responde más rápido, pero falla una consulta de devolución.
Explicar: Mostrar tanto latencia como el caso perdido.
Valorar: La devolución puede tener mayor consecuencia que un saludo.
Defender: Justificar si se revierte o se investiga antes de entregar.
Resultado: Una conclusión útil explica la decisión de producto y su costo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué pregunta del panel pondría a prueba tu interpretación de los datos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La evidencia sirve para decidir, no solo para mostrar porcentajes.

ERRORES CONCEPTUALES FRECUENTES
Presentar un número sin dataset, versión o criterio.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Laboratorio L10: un cambio dirigido

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · Preparar evidencia para la sustentación

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: MercaSur · Preparar evidencia para la sustentación
Sesión: Evaluación y optimización continua
Archivo: 10-evaluacion-optimizacion-editable.pptx
Sección que soporta: §6 y conexión S11
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-10-evaluacion-optimizacion; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Convertir la comparación técnica en una explicación que el panel pueda revisar.

CONCEPTO PRINCIPAL
Preparar evidencia para la sustentación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La evidencia sirve para decidir, no solo para mostrar porcentajes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La nueva versión responde más rápido, pero falla una consulta de devolución. Pida una predicción.

Explicar: Mostrar tanto latencia como el caso perdido.

Valorar: La devolución puede tener mayor consecuencia que un saludo.

Defender: Justificar si se revierte o se investiga antes de entregar.

Resultado esperado: Una conclusión útil explica la decisión de producto y su costo. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Explicar; Valorar; Defender. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. La nueva versión responde más rápido, pero falla una consulta de devolución.
Explicar: Mostrar tanto latencia como el caso perdido.
Valorar: La devolución puede tener mayor consecuencia que un saludo.
Defender: Justificar si se revierte o se investiga antes de entregar.
Resultado: Una conclusión útil explica la decisión de producto y su costo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué pregunta del panel pondría a prueba tu interpretación de los datos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La evidencia sirve para decidir, no solo para mostrar porcentajes.

ERRORES CONCEPTUALES FRECUENTES
Presentar un número sin dataset, versión o criterio.

CONEXIÓN ANTERIOR
S9: dos cuellos de botella documentados · Capítulo previo: Laboratorio L10: un cambio dirigido

CONEXIÓN POSTERIOR
S11: defender la mejora ante el panel.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

