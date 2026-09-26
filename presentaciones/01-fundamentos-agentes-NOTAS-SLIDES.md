# Fundamentos de los agentes inteligentes — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Objetivos de aprendizaje

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Objetivos de aprendizaje
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Relacionar las capacidades de la sesión con el proyecto que crecerá durante el curso.

CONCEPTO PRINCIPAL
Objetivos de aprendizaje

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El proyecto crece por capas; hoy se construye su base.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué parte del caso todavía no puede resolver el script de L1?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Comprender: Distinguir un LLM, un workflow y un agente.

Construir: Ejecutar el primer script con el proveedor común.

Orientar: Elegir un track y reconocer la arquitectura futura.

Cierre con la distinción: El proyecto crece por capas; hoy se construye su base.

ELEMENTOS QUE CONVIENE EXPLICAR
Comprender; Construir; Orientar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El equipo quiere un asistente que informe consumo y reciba reclamos.
Separar: Redactar una respuesta no consulta consumo.
Ubicar: Las tools se implementan desde S3.
Empezar: Hoy verifican proveedor y primer script.
Resultado: Cada capacidad se incorpora con evidencia en su sesión.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte del caso todavía no puede resolver el script de L1?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El proyecto crece por capas; hoy se construye su base.

ERRORES CONCEPTUALES FRECUENTES
Llamar agente completo a cualquier primer chat.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno.

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: LLM y fuente de verdad

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Tres evidencias del aprendizaje

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Tres evidencias del aprendizaje
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Relacionar las capacidades de la sesión con el proyecto que crecerá durante el curso.

CONCEPTO PRINCIPAL
Objetivos de aprendizaje

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El proyecto crece por capas; hoy se construye su base.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Explicación: Justificar cuándo hace falta consultar un sistema.

Ejecución: Obtener una respuesta del modelo desde el entorno del curso.

Decisión: Seleccionar un caso de industria con alcance definido.

Contraste la regla con este error: Llamar agente completo a cualquier primer chat. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Explicación; Ejecución; Decisión. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El equipo quiere un asistente que informe consumo y reciba reclamos.
Separar: Redactar una respuesta no consulta consumo.
Ubicar: Las tools se implementan desde S3.
Empezar: Hoy verifican proveedor y primer script.
Resultado: Cada capacidad se incorpora con evidencia en su sesión.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte del caso todavía no puede resolver el script de L1?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El proyecto crece por capas; hoy se construye su base.

ERRORES CONCEPTUALES FRECUENTES
Llamar agente completo a cualquier primer chat.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno.

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: LLM y fuente de verdad

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Objetivos de aprendizaje

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: AndesMóvil · Objetivos de aprendizaje
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Relacionar las capacidades de la sesión con el proyecto que crecerá durante el curso.

CONCEPTO PRINCIPAL
Objetivos de aprendizaje

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El proyecto crece por capas; hoy se construye su base.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El equipo quiere un asistente que informe consumo y reciba reclamos. Pida una predicción.

Separar: Redactar una respuesta no consulta consumo.

Ubicar: Las tools se implementan desde S3.

Empezar: Hoy verifican proveedor y primer script.

Resultado esperado: Cada capacidad se incorpora con evidencia en su sesión. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Separar; Ubicar; Empezar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El equipo quiere un asistente que informe consumo y reciba reclamos.
Separar: Redactar una respuesta no consulta consumo.
Ubicar: Las tools se implementan desde S3.
Empezar: Hoy verifican proveedor y primer script.
Resultado: Cada capacidad se incorpora con evidencia en su sesión.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte del caso todavía no puede resolver el script de L1?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El proyecto crece por capas; hoy se construye su base.

ERRORES CONCEPTUALES FRECUENTES
Llamar agente completo a cualquier primer chat.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno.

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: LLM y fuente de verdad

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. LLM y fuente de verdad

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: LLM y fuente de verdad
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Romper la expectativa de que el modelo conoce la tarifa actual del cliente.

CONCEPTO PRINCIPAL
LLM y fuente de verdad

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El LLM no sustituye el sistema que administra la tarifa.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué harías si ambas ejecuciones del LLM devolvieran la misma cifra falsa?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Pregunta: «¿Cuál es la tarifa de mi plan?»

LLM sin fuente: Puede producir una cifra plausible sin consultarla.

Sistema de negocio: Contiene el dato que permite comprobar la respuesta.

Cierre con la distinción: El LLM no sustituye el sistema que administra la tarifa.

ELEMENTOS QUE CONVIENE EXPLICAR
Pregunta; LLM sin fuente; Sistema de negocio. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. En una demostración ficticia, el modelo propone S/ 49.90 y la API devuelve S/ 59.90.
Comparar: Identificar los dos orígenes de información.
Elegir: Usar el valor verificado del sistema.
Limitar: Si la API falla, no inventar una tarifa alternativa.
Resultado: La respuesta debe depender del dato consultado, no de la cifra más plausible.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías si ambas ejecuciones del LLM devolvieran la misma cifra falsa?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El LLM no sustituye el sistema que administra la tarifa.

ERRORES CONCEPTUALES FRECUENTES
Usar variación como única prueba de falta de veracidad.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Objetivos de aprendizaje

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Un LLM solo no es un agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Cambiar el origen del dato

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Cambiar el origen del dato
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Romper la expectativa de que el modelo conoce la tarifa actual del cliente.

CONCEPTO PRINCIPAL
LLM y fuente de verdad

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El LLM no sustituye el sistema que administra la tarifa.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Detectar: La pregunta pide un hecho específico y vigente.

Consultar: La aplicación debe obtenerlo del sistema pertinente.

Explicar: El modelo puede redactar el resultado recibido.

Contraste la regla con este error: Usar variación como única prueba de falta de veracidad. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Detectar; Consultar; Explicar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. En una demostración ficticia, el modelo propone S/ 49.90 y la API devuelve S/ 59.90.
Comparar: Identificar los dos orígenes de información.
Elegir: Usar el valor verificado del sistema.
Limitar: Si la API falla, no inventar una tarifa alternativa.
Resultado: La respuesta debe depender del dato consultado, no de la cifra más plausible.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías si ambas ejecuciones del LLM devolvieran la misma cifra falsa?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El LLM no sustituye el sistema que administra la tarifa.

ERRORES CONCEPTUALES FRECUENTES
Usar variación como única prueba de falta de veracidad.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Objetivos de aprendizaje

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Un LLM solo no es un agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · LLM y fuente de verdad

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: AndesMóvil · LLM y fuente de verdad
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Romper la expectativa de que el modelo conoce la tarifa actual del cliente.

CONCEPTO PRINCIPAL
LLM y fuente de verdad

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El LLM no sustituye el sistema que administra la tarifa.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: En una demostración ficticia, el modelo propone S/ 49.90 y la API devuelve S/ 59.90. Pida una predicción.

Comparar: Identificar los dos orígenes de información.

Elegir: Usar el valor verificado del sistema.

Limitar: Si la API falla, no inventar una tarifa alternativa.

Resultado esperado: La respuesta debe depender del dato consultado, no de la cifra más plausible. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Comparar; Elegir; Limitar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. En una demostración ficticia, el modelo propone S/ 49.90 y la API devuelve S/ 59.90.
Comparar: Identificar los dos orígenes de información.
Elegir: Usar el valor verificado del sistema.
Limitar: Si la API falla, no inventar una tarifa alternativa.
Resultado: La respuesta debe depender del dato consultado, no de la cifra más plausible.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías si ambas ejecuciones del LLM devolvieran la misma cifra falsa?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El LLM no sustituye el sistema que administra la tarifa.

ERRORES CONCEPTUALES FRECUENTES
Usar variación como única prueba de falta de veracidad.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Objetivos de aprendizaje

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Un LLM solo no es un agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Un LLM solo no es un agente

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Un LLM solo no es un agente
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Identificar los componentes que convierten generación de texto en actuación controlada.

CONCEPTO PRINCIPAL
Un LLM solo no es un agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El modelo propone; el sistema ejecuta y gobierna las capacidades.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Un agente necesita siempre memoria persistente?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

LLM: Interpreta mensajes y propone respuestas o acciones.

Tools y contexto: Aportan capacidades externas e información pertinente.

Objetivo y control: Definen qué resolver, cuándo actuar y cuándo terminar.

Cierre con la distinción: El modelo propone; el sistema ejecuta y gobierna las capacidades.

ELEMENTOS QUE CONVIENE EXPLICAR
LLM; Tools y contexto; Objetivo y control. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El usuario quiere saber dónde está el pedido PED-2026-00123.
Interpretar: Reconocer que pregunta por un pedido concreto.
Actuar: Consultar track_order desde la aplicación.
Responder: Explicar el estado obtenido sin inventar movimientos.
Resultado: La acción externa y su control completan el circuito.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un agente necesita siempre memoria persistente?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El modelo propone; el sistema ejecuta y gobierna las capacidades.

ERRORES CONCEPTUALES FRECUENTES
Presentar memoria como requisito universal o atribuir ejecución directa al modelo.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: LLM y fuente de verdad

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: El ciclo del agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Responsabilidades de la aplicación

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Responsabilidades de la aplicación
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Identificar los componentes que convierten generación de texto en actuación controlada.

CONCEPTO PRINCIPAL
Un LLM solo no es un agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El modelo propone; el sistema ejecuta y gobierna las capacidades.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Exponer: Dar al modelo un catálogo explícito de capacidades.

Ejecutar: Validar y realizar la acción seleccionada.

Controlar: Conservar estado cuando haga falta y aplicar límites.

Contraste la regla con este error: Presentar memoria como requisito universal o atribuir ejecución directa al modelo. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Exponer; Ejecutar; Controlar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El usuario quiere saber dónde está el pedido PED-2026-00123.
Interpretar: Reconocer que pregunta por un pedido concreto.
Actuar: Consultar track_order desde la aplicación.
Responder: Explicar el estado obtenido sin inventar movimientos.
Resultado: La acción externa y su control completan el circuito.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un agente necesita siempre memoria persistente?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El modelo propone; el sistema ejecuta y gobierna las capacidades.

ERRORES CONCEPTUALES FRECUENTES
Presentar memoria como requisito universal o atribuir ejecución directa al modelo.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: LLM y fuente de verdad

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: El ciclo del agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Un LLM solo no es un agente

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: MercaSur · Un LLM solo no es un agente
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Identificar los componentes que convierten generación de texto en actuación controlada.

CONCEPTO PRINCIPAL
Un LLM solo no es un agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El modelo propone; el sistema ejecuta y gobierna las capacidades.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El usuario quiere saber dónde está el pedido PED-2026-00123. Pida una predicción.

Interpretar: Reconocer que pregunta por un pedido concreto.

Actuar: Consultar track_order desde la aplicación.

Responder: Explicar el estado obtenido sin inventar movimientos.

Resultado esperado: La acción externa y su control completan el circuito. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Interpretar; Actuar; Responder. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El usuario quiere saber dónde está el pedido PED-2026-00123.
Interpretar: Reconocer que pregunta por un pedido concreto.
Actuar: Consultar track_order desde la aplicación.
Responder: Explicar el estado obtenido sin inventar movimientos.
Resultado: La acción externa y su control completan el circuito.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un agente necesita siempre memoria persistente?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El modelo propone; el sistema ejecuta y gobierna las capacidades.

ERRORES CONCEPTUALES FRECUENTES
Presentar memoria como requisito universal o atribuir ejecución directa al modelo.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: LLM y fuente de verdad

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: El ciclo del agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. El ciclo del agente

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: El ciclo del agente
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Recorrer percepción, decisión, acción y observación hasta una condición de parada.

CONCEPTO PRINCIPAL
El ciclo del agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El ciclo usa observaciones; no implica actualizar los pesos del modelo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué observación justificaría repetir una consulta?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Percibir y decidir: Leer la solicitud y el estado disponible.

Actuar: Proponer una tool; la aplicación la ejecuta.

Observar: Incorporar el resultado y decidir si continuar o responder.

Cierre con la distinción: El ciclo usa observaciones; no implica actualizar los pesos del modelo.

ELEMENTOS QUE CONVIENE EXPLICAR
Percibir y decidir; Actuar; Observar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El cliente pregunta cuántos datos le quedan.
Percibir: Identificar la línea y la consulta de consumo.
Consultar: get_data_usage obtiene el resultado del simulador.
Observar: La respuesta recibida permite explicar el consumo.
Resultado: Si falta identificar la línea, el siguiente paso útil es preguntar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué observación justificaría repetir una consulta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El ciclo usa observaciones; no implica actualizar los pesos del modelo.

ERRORES CONCEPTUALES FRECUENTES
Describir el ciclo como aprendizaje permanente automático.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Un LLM solo no es un agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Workflow frente a agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Cómo cierra el ciclo

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Cómo cierra el ciclo
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Recorrer percepción, decisión, acción y observación hasta una condición de parada.

CONCEPTO PRINCIPAL
El ciclo del agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El ciclo usa observaciones; no implica actualizar los pesos del modelo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Resultado útil: Responder cuando hay evidencia suficiente.

Dato faltante: Pedir información necesaria al usuario.

Límite alcanzado: Detener o derivar en vez de repetir indefinidamente.

Contraste la regla con este error: Describir el ciclo como aprendizaje permanente automático. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Resultado útil; Dato faltante; Límite alcanzado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El cliente pregunta cuántos datos le quedan.
Percibir: Identificar la línea y la consulta de consumo.
Consultar: get_data_usage obtiene el resultado del simulador.
Observar: La respuesta recibida permite explicar el consumo.
Resultado: Si falta identificar la línea, el siguiente paso útil es preguntar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué observación justificaría repetir una consulta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El ciclo usa observaciones; no implica actualizar los pesos del modelo.

ERRORES CONCEPTUALES FRECUENTES
Describir el ciclo como aprendizaje permanente automático.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Un LLM solo no es un agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Workflow frente a agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · El ciclo del agente

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: AndesMóvil · El ciclo del agente
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Recorrer percepción, decisión, acción y observación hasta una condición de parada.

CONCEPTO PRINCIPAL
El ciclo del agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El ciclo usa observaciones; no implica actualizar los pesos del modelo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El cliente pregunta cuántos datos le quedan. Pida una predicción.

Percibir: Identificar la línea y la consulta de consumo.

Consultar: get_data_usage obtiene el resultado del simulador.

Observar: La respuesta recibida permite explicar el consumo.

Resultado esperado: Si falta identificar la línea, el siguiente paso útil es preguntar. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Percibir; Consultar; Observar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El cliente pregunta cuántos datos le quedan.
Percibir: Identificar la línea y la consulta de consumo.
Consultar: get_data_usage obtiene el resultado del simulador.
Observar: La respuesta recibida permite explicar el consumo.
Resultado: Si falta identificar la línea, el siguiente paso útil es preguntar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué observación justificaría repetir una consulta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El ciclo usa observaciones; no implica actualizar los pesos del modelo.

ERRORES CONCEPTUALES FRECUENTES
Describir el ciclo como aprendizaje permanente automático.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Un LLM solo no es un agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Workflow frente a agente

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Workflow frente a agente

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Workflow frente a agente
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Elegir el control del proceso según si la ruta debe fijarse o decidirse durante la ejecución.

CONCEPTO PRINCIPAL
Workflow frente a agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Elige agentes cuando la decisión dinámica justifica su complejidad.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Un workflow con condiciones deja de ser workflow?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Workflow: La aplicación define pasos y ramas permitidas.

Agente: El modelo puede elegir el siguiente paso dentro de límites.

Sistema combinado: Un flujo puede contener decisiones agénticas acotadas.

Cierre con la distinción: Elige agentes cuando la decisión dinámica justifica su complejidad.

ELEMENTOS QUE CONVIENE EXPLICAR
Workflow; Agente; Sistema combinado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una consulta requiere verificar datos antes de explicar una comisión.
Fijar: La verificación obligatoria pertenece al flujo.
Consultar: El agente puede elegir qué información adicional necesita.
Restringir: No se habilita una transferencia por decisión del modelo.
Resultado: Las obligaciones no se vuelven opcionales por usar un agente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un workflow con condiciones deja de ser workflow?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Elige agentes cuando la decisión dinámica justifica su complejidad.

ERRORES CONCEPTUALES FRECUENTES
Equiparar cualquier bifurcación o resultado variable con autonomía.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: El ciclo del agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Anatomía de LangChain 1.x

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Criterio para decidir

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Criterio para decidir
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Elegir el control del proceso según si la ruta debe fijarse o decidirse durante la ejecución.

CONCEPTO PRINCIPAL
Workflow frente a agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Elige agentes cuando la decisión dinámica justifica su complejidad.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Ruta obligatoria: Codificar el orden y las verificaciones necesarias.

Ruta variable: Permitir selección de herramientas cuando aporte valor.

Consecuencia: Conservar controles de negocio fuera de decisiones libres.

Contraste la regla con este error: Equiparar cualquier bifurcación o resultado variable con autonomía. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Ruta obligatoria; Ruta variable; Consecuencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una consulta requiere verificar datos antes de explicar una comisión.
Fijar: La verificación obligatoria pertenece al flujo.
Consultar: El agente puede elegir qué información adicional necesita.
Restringir: No se habilita una transferencia por decisión del modelo.
Resultado: Las obligaciones no se vuelven opcionales por usar un agente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un workflow con condiciones deja de ser workflow?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Elige agentes cuando la decisión dinámica justifica su complejidad.

ERRORES CONCEPTUALES FRECUENTES
Equiparar cualquier bifurcación o resultado variable con autonomía.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: El ciclo del agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Anatomía de LangChain 1.x

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Workflow frente a agente

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: Banco Inti · Workflow frente a agente
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Elegir el control del proceso según si la ruta debe fijarse o decidirse durante la ejecución.

CONCEPTO PRINCIPAL
Workflow frente a agente

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Elige agentes cuando la decisión dinámica justifica su complejidad.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una consulta requiere verificar datos antes de explicar una comisión. Pida una predicción.

Fijar: La verificación obligatoria pertenece al flujo.

Consultar: El agente puede elegir qué información adicional necesita.

Restringir: No se habilita una transferencia por decisión del modelo.

Resultado esperado: Las obligaciones no se vuelven opcionales por usar un agente. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Fijar; Consultar; Restringir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una consulta requiere verificar datos antes de explicar una comisión.
Fijar: La verificación obligatoria pertenece al flujo.
Consultar: El agente puede elegir qué información adicional necesita.
Restringir: No se habilita una transferencia por decisión del modelo.
Resultado: Las obligaciones no se vuelven opcionales por usar un agente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un workflow con condiciones deja de ser workflow?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Elige agentes cuando la decisión dinámica justifica su complejidad.

ERRORES CONCEPTUALES FRECUENTES
Equiparar cualquier bifurcación o resultado variable con autonomía.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: El ciclo del agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Anatomía de LangChain 1.x

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Anatomía de LangChain 1.x

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Anatomía de LangChain 1.x
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §6
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ubicar modelos, mensajes, herramientas, agente y controles en el mapa del curso.

CONCEPTO PRINCIPAL
Anatomía de LangChain 1.x

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La arquitectura se reconoce ahora y se construye progresivamente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Dónde ubicarías un filtro de salida que evita exponer PII?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Mensajes y modelo: La interfaz recibe contexto y genera salidas.

Agente y tools: El control coordina decisiones y ejecución externa.

Estado y middleware: Conservan conversación y aplican controles alrededor del flujo.

Cierre con la distinción: La arquitectura se reconoce ahora y se construye progresivamente.

ELEMENTOS QUE CONVIENE EXPLICAR
Mensajes y modelo; Agente y tools; Estado y middleware. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una consulta de póliza necesita dato del sistema y una regla documental.
Datos: Una tool consulta la póliza.
Conocimiento: El retriever recupera una cláusula del corpus.
Control: La aplicación limita promesas y deriva lo que no puede resolver.
Resultado: Cada componente tiene una responsabilidad y un laboratorio donde se implementa.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde ubicarías un filtro de salida que evita exponer PII?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La arquitectura se reconoce ahora y se construye progresivamente.

ERRORES CONCEPTUALES FRECUENTES
Confundir todo LangChain con el LLM o adelantar APIs no usadas.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Workflow frente a agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Modelos abiertos y cerrados

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Cuándo aparece cada pieza

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Cuándo aparece cada pieza
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §6
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ubicar modelos, mensajes, herramientas, agente y controles en el mapa del curso.

CONCEPTO PRINCIPAL
Anatomía de LangChain 1.x

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La arquitectura se reconoce ahora y se construye progresivamente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

S1–S2: Proveedor común, mensajes, prompts y salida estructurada.

S3–S5: Tools, selección, memoria y recuperación de conocimiento.

S6–S10: Límites, despliegue, trazas y evaluación.

Contraste la regla con este error: Confundir todo LangChain con el LLM o adelantar APIs no usadas. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
S1–S2; S3–S5; S6–S10. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una consulta de póliza necesita dato del sistema y una regla documental.
Datos: Una tool consulta la póliza.
Conocimiento: El retriever recupera una cláusula del corpus.
Control: La aplicación limita promesas y deriva lo que no puede resolver.
Resultado: Cada componente tiene una responsabilidad y un laboratorio donde se implementa.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde ubicarías un filtro de salida que evita exponer PII?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La arquitectura se reconoce ahora y se construye progresivamente.

ERRORES CONCEPTUALES FRECUENTES
Confundir todo LangChain con el LLM o adelantar APIs no usadas.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Workflow frente a agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Modelos abiertos y cerrados

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Anatomía de LangChain 1.x

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: Andina Seguros · Anatomía de LangChain 1.x
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §6
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ubicar modelos, mensajes, herramientas, agente y controles en el mapa del curso.

CONCEPTO PRINCIPAL
Anatomía de LangChain 1.x

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La arquitectura se reconoce ahora y se construye progresivamente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una consulta de póliza necesita dato del sistema y una regla documental. Pida una predicción.

Datos: Una tool consulta la póliza.

Conocimiento: El retriever recupera una cláusula del corpus.

Control: La aplicación limita promesas y deriva lo que no puede resolver.

Resultado esperado: Cada componente tiene una responsabilidad y un laboratorio donde se implementa. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Datos; Conocimiento; Control. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una consulta de póliza necesita dato del sistema y una regla documental.
Datos: Una tool consulta la póliza.
Conocimiento: El retriever recupera una cláusula del corpus.
Control: La aplicación limita promesas y deriva lo que no puede resolver.
Resultado: Cada componente tiene una responsabilidad y un laboratorio donde se implementa.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde ubicarías un filtro de salida que evita exponer PII?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La arquitectura se reconoce ahora y se construye progresivamente.

ERRORES CONCEPTUALES FRECUENTES
Confundir todo LangChain con el LLM o adelantar APIs no usadas.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Workflow frente a agente

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Modelos abiertos y cerrados

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. Modelos abiertos y cerrados

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: Modelos abiertos y cerrados
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §7
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar acceso, operación y evidencia de adecuación para el curso.

CONCEPTO PRINCIPAL
Modelos abiertos y cerrados

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El modelo se elige por evidencia sobre la tarea.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Podemos trasladar el resultado a cualquier versión o endpoint sin probar?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Pesos abiertos: Permiten acceso bajo la licencia concreta del modelo.

Modelos cerrados: Se consumen normalmente mediante el servicio de su proveedor.

Selección del curso: Qwen3-32B cumplió las pruebas documentadas para este material.

Cierre con la distinción: El modelo se elige por evidencia sobre la tarea.

ELEMENTOS QUE CONVIENE EXPLICAR
Pesos abiertos; Modelos cerrados; Selección del curso. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Se evalúan candidatos para elegir tools de pedidos y stock.
Definir: La prueba requiere llamadas de herramientas correctas.
Ejecutar: Aplicar la misma batería a cada candidato.
Decidir: Elegir el que cumpla los requisitos en ese contexto.
Resultado: El resultado del repositorio no es un ranking universal de modelos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Podemos trasladar el resultado a cualquier versión o endpoint sin probar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El modelo se elige por evidencia sobre la tarea.

ERRORES CONCEPTUALES FRECUENTES
Tratar una comparación del curso como verdad permanente.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Anatomía de LangChain 1.x

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: La capa comun/provider.py

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. Elegir con pruebas del caso

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: Elegir con pruebas del caso
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §7
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar acceso, operación y evidencia de adecuación para el curso.

CONCEPTO PRINCIPAL
Modelos abiertos y cerrados

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El modelo se elige por evidencia sobre la tarea.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Compatibilidad: Comprobar tool calling y el patrón de interacción requerido.

Operación: Valorar acceso, capacidad y esfuerzo de mantenimiento.

Evidencia: Conservar resultados de la batería, no una preferencia de marca.

Contraste la regla con este error: Tratar una comparación del curso como verdad permanente. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Compatibilidad; Operación; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Se evalúan candidatos para elegir tools de pedidos y stock.
Definir: La prueba requiere llamadas de herramientas correctas.
Ejecutar: Aplicar la misma batería a cada candidato.
Decidir: Elegir el que cumpla los requisitos en ese contexto.
Resultado: El resultado del repositorio no es un ranking universal de modelos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Podemos trasladar el resultado a cualquier versión o endpoint sin probar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El modelo se elige por evidencia sobre la tarea.

ERRORES CONCEPTUALES FRECUENTES
Tratar una comparación del curso como verdad permanente.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Anatomía de LangChain 1.x

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: La capa comun/provider.py

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · Modelos abiertos y cerrados

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: MercaSur · Modelos abiertos y cerrados
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §7
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar acceso, operación y evidencia de adecuación para el curso.

CONCEPTO PRINCIPAL
Modelos abiertos y cerrados

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El modelo se elige por evidencia sobre la tarea.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Se evalúan candidatos para elegir tools de pedidos y stock. Pida una predicción.

Definir: La prueba requiere llamadas de herramientas correctas.

Ejecutar: Aplicar la misma batería a cada candidato.

Decidir: Elegir el que cumpla los requisitos en ese contexto.

Resultado esperado: El resultado del repositorio no es un ranking universal de modelos. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Definir; Ejecutar; Decidir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Se evalúan candidatos para elegir tools de pedidos y stock.
Definir: La prueba requiere llamadas de herramientas correctas.
Ejecutar: Aplicar la misma batería a cada candidato.
Decidir: Elegir el que cumpla los requisitos en ese contexto.
Resultado: El resultado del repositorio no es un ranking universal de modelos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Podemos trasladar el resultado a cualquier versión o endpoint sin probar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El modelo se elige por evidencia sobre la tarea.

ERRORES CONCEPTUALES FRECUENTES
Tratar una comparación del curso como verdad permanente.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Anatomía de LangChain 1.x

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: La capa comun/provider.py

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 22. La capa comun/provider.py

DIAPOSITIVA 22 · CAPÍTULO 8 · CONCEPTO
Título: La capa comun/provider.py
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §8
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar cómo una interfaz común evita dispersar la configuración del proveedor.

CONCEPTO PRINCIPAL
La capa comun/provider.py

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué tendrías que modificar si cada archivo creara su propio cliente?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Aplicación: Solicita get_chat_model() o get_embeddings().

Adaptador común: Lee AI_PROVIDER y la configuración correspondiente.

Proveedor: Devuelve el cliente con la interfaz usada por el curso.

Cierre con la distinción: Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

ELEMENTOS QUE CONVIENE EXPLICAR
Aplicación; Adaptador común; Proveedor. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El mismo agente pasa de Hugging Face a Foundry en el bonus.
Preparar: Completar las variables del destino.
Cambiar: Seleccionar AI_PROVIDER=foundry.
Medir: Ejecutar las mismas consultas y comparar resultados.
Resultado: La interfaz puede mantenerse; las respuestas del modelo pueden cambiar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué tendrías que modificar si cada archivo creara su propio cliente?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

ERRORES CONCEPTUALES FRECUENTES
Prometer resultados idénticos después del cambio.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Modelos abiertos y cerrados

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: De la apertura al laboratorio L1

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 23. Portabilidad y sus límites

DIAPOSITIVA 23 · CAPÍTULO 8 · DESARROLLO
Título: Portabilidad y sus límites
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §8
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar cómo una interfaz común evita dispersar la configuración del proveedor.

CONCEPTO PRINCIPAL
La capa comun/provider.py

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Código: Centralizar la selección en el módulo común.

Configuración: Proporcionar endpoint, modelo y credenciales requeridas.

Comportamiento: Repetir pruebas al cambiar de modelo o servicio.

Contraste la regla con este error: Prometer resultados idénticos después del cambio. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Código; Configuración; Comportamiento. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El mismo agente pasa de Hugging Face a Foundry en el bonus.
Preparar: Completar las variables del destino.
Cambiar: Seleccionar AI_PROVIDER=foundry.
Medir: Ejecutar las mismas consultas y comparar resultados.
Resultado: La interfaz puede mantenerse; las respuestas del modelo pueden cambiar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué tendrías que modificar si cada archivo creara su propio cliente?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

ERRORES CONCEPTUALES FRECUENTES
Prometer resultados idénticos después del cambio.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Modelos abiertos y cerrados

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: De la apertura al laboratorio L1

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 24. Ejemplo · La capa comun/provider.py

DIAPOSITIVA 24 · CAPÍTULO 8 · EJEMPLO
Título: AndesMóvil · La capa comun/provider.py
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §8
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar cómo una interfaz común evita dispersar la configuración del proveedor.

CONCEPTO PRINCIPAL
La capa comun/provider.py

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El mismo agente pasa de Hugging Face a Foundry en el bonus. Pida una predicción.

Preparar: Completar las variables del destino.

Cambiar: Seleccionar AI_PROVIDER=foundry.

Medir: Ejecutar las mismas consultas y comparar resultados.

Resultado esperado: La interfaz puede mantenerse; las respuestas del modelo pueden cambiar. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Preparar; Cambiar; Medir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El mismo agente pasa de Hugging Face a Foundry en el bonus.
Preparar: Completar las variables del destino.
Cambiar: Seleccionar AI_PROVIDER=foundry.
Medir: Ejecutar las mismas consultas y comparar resultados.
Resultado: La interfaz puede mantenerse; las respuestas del modelo pueden cambiar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué tendrías que modificar si cada archivo creara su propio cliente?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Abstraer el proveedor reduce cambios de código, no elimina la evaluación.

ERRORES CONCEPTUALES FRECUENTES
Prometer resultados idénticos después del cambio.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Modelos abiertos y cerrados

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: De la apertura al laboratorio L1

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 25. De la apertura al laboratorio L1

DIAPOSITIVA 25 · CAPÍTULO 9 · CONCEPTO
Título: De la apertura al laboratorio L1
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §9 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Conectar explicación, demostración y ejecución individual en la sesión.

CONCEPTO PRINCIPAL
De la apertura al laboratorio L1

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
L1 valida entorno y conexión; las tools llegan en S3.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué evidencia adicional convertiría esto en una consulta real de saldo?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Observar: La apertura y el antipatrón cuestionan la expectativa de API determinista.

Practicar: El live coding muestra el primer acceso al modelo.

Consolidar: Test, elección de track y laboratorio producen evidencias.

Cierre con la distinción: L1 valida entorno y conexión; las tools llegan en S3.

ELEMENTOS QUE CONVIENE EXPLICAR
Observar; Practicar; Consolidar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El alumno obtiene una respuesta textual a una consulta bancaria.
Ejecutar: Su primer script llama al modelo.
Evaluar: No hay consulta de saldo ni transacción externa.
Documentar: Anotar el resultado y el límite de esa demostración.
Resultado: El primer éxito técnico no demuestra que los datos de negocio sean verdaderos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia adicional convertiría esto en una consulta real de saldo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: L1 valida entorno y conexión; las tools llegan en S3.

ERRORES CONCEPTUALES FRECUENTES
Dar por implementado el agente final al recibir texto.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: La capa comun/provider.py

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Elección del track

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 26. Comprobar el primer script

DIAPOSITIVA 26 · CAPÍTULO 9 · DESARROLLO
Título: Comprobar el primer script
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §9 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Conectar explicación, demostración y ejecución individual en la sesión.

CONCEPTO PRINCIPAL
De la apertura al laboratorio L1

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
L1 valida entorno y conexión; las tools llegan en S3.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Preparación: Entorno y variables configurados antes de invocar.

Llamada: Usar la capa común del proveedor.

Lectura: Distinguir respuesta de texto y ejecución de una tool.

Contraste la regla con este error: Dar por implementado el agente final al recibir texto. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Preparación; Llamada; Lectura. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El alumno obtiene una respuesta textual a una consulta bancaria.
Ejecutar: Su primer script llama al modelo.
Evaluar: No hay consulta de saldo ni transacción externa.
Documentar: Anotar el resultado y el límite de esa demostración.
Resultado: El primer éxito técnico no demuestra que los datos de negocio sean verdaderos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia adicional convertiría esto en una consulta real de saldo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: L1 valida entorno y conexión; las tools llegan en S3.

ERRORES CONCEPTUALES FRECUENTES
Dar por implementado el agente final al recibir texto.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: La capa comun/provider.py

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Elección del track

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 27. Ejemplo · De la apertura al laboratorio L1

DIAPOSITIVA 27 · CAPÍTULO 9 · EJEMPLO
Título: Banco Inti · De la apertura al laboratorio L1
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §9 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Conectar explicación, demostración y ejecución individual en la sesión.

CONCEPTO PRINCIPAL
De la apertura al laboratorio L1

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
L1 valida entorno y conexión; las tools llegan en S3.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El alumno obtiene una respuesta textual a una consulta bancaria. Pida una predicción.

Ejecutar: Su primer script llama al modelo.

Evaluar: No hay consulta de saldo ni transacción externa.

Documentar: Anotar el resultado y el límite de esa demostración.

Resultado esperado: El primer éxito técnico no demuestra que los datos de negocio sean verdaderos. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Ejecutar; Evaluar; Documentar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El alumno obtiene una respuesta textual a una consulta bancaria.
Ejecutar: Su primer script llama al modelo.
Evaluar: No hay consulta de saldo ni transacción externa.
Documentar: Anotar el resultado y el límite de esa demostración.
Resultado: El primer éxito técnico no demuestra que los datos de negocio sean verdaderos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia adicional convertiría esto en una consulta real de saldo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: L1 valida entorno y conexión; las tools llegan en S3.

ERRORES CONCEPTUALES FRECUENTES
Dar por implementado el agente final al recibir texto.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: La capa comun/provider.py

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Elección del track

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 28. Elección del track

DIAPOSITIVA 28 · CAPÍTULO 10 · CONCEPTO
Título: Elección del track
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §10
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer cuatro dominios sobre un mismo patrón de arquitectura.

CONCEPTO PRINCIPAL
Elección del track

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Elegir industria significa concretar datos, tareas y límites.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué límite deberías explicar en la primera frase de tu caso?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Telco y banca: AndesMóvil y Banco Inti trabajan datos y operaciones del dominio.

Retail y seguros: MercaSur y Andina Seguros aportan otros catálogos y corpus.

Núcleo compartido: Modelo, tools, contexto y control siguen el mismo patrón.

Cierre con la distinción: Elegir industria significa concretar datos, tareas y límites.

ELEMENTOS QUE CONVIENE EXPLICAR
Telco y banca; Retail y seguros; Núcleo compartido. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El equipo elige asistencia sobre pólizas y registro de siniestros.
Delimitar: Consultar póliza, revisar condiciones y registrar información.
Restringir: No aprobar indemnizaciones por decisión del agente.
Conectar: Usar prompts, tools y documentos del track de seguros.
Resultado: El track cambia el dominio; no reemplaza el método del curso.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué límite deberías explicar en la primera frase de tu caso?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Elegir industria significa concretar datos, tareas y límites.

ERRORES CONCEPTUALES FRECUENTES
Elegir un caso que exige sistemas o permisos inexistentes.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: De la apertura al laboratorio L1

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Alcance de S1 y evolución posterior

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 29. Definir un caso viable

DIAPOSITIVA 29 · CAPÍTULO 10 · DESARROLLO
Título: Definir un caso viable
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §10
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer cuatro dominios sobre un mismo patrón de arquitectura.

CONCEPTO PRINCIPAL
Elección del track

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Elegir industria significa concretar datos, tareas y límites.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Usuario: Nombrar quién pide ayuda y qué necesita.

Alcance: Elegir las consultas cubiertas por el simulador y el corpus.

Límite: Explicitar qué acciones no puede realizar el asistente.

Contraste la regla con este error: Elegir un caso que exige sistemas o permisos inexistentes. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Usuario; Alcance; Límite. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El equipo elige asistencia sobre pólizas y registro de siniestros.
Delimitar: Consultar póliza, revisar condiciones y registrar información.
Restringir: No aprobar indemnizaciones por decisión del agente.
Conectar: Usar prompts, tools y documentos del track de seguros.
Resultado: El track cambia el dominio; no reemplaza el método del curso.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué límite deberías explicar en la primera frase de tu caso?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Elegir industria significa concretar datos, tareas y límites.

ERRORES CONCEPTUALES FRECUENTES
Elegir un caso que exige sistemas o permisos inexistentes.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: De la apertura al laboratorio L1

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Alcance de S1 y evolución posterior

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 30. Ejemplo · Elección del track

DIAPOSITIVA 30 · CAPÍTULO 10 · EJEMPLO
Título: Andina Seguros · Elección del track
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §10
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer cuatro dominios sobre un mismo patrón de arquitectura.

CONCEPTO PRINCIPAL
Elección del track

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Elegir industria significa concretar datos, tareas y límites.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El equipo elige asistencia sobre pólizas y registro de siniestros. Pida una predicción.

Delimitar: Consultar póliza, revisar condiciones y registrar información.

Restringir: No aprobar indemnizaciones por decisión del agente.

Conectar: Usar prompts, tools y documentos del track de seguros.

Resultado esperado: El track cambia el dominio; no reemplaza el método del curso. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Delimitar; Restringir; Conectar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El equipo elige asistencia sobre pólizas y registro de siniestros.
Delimitar: Consultar póliza, revisar condiciones y registrar información.
Restringir: No aprobar indemnizaciones por decisión del agente.
Conectar: Usar prompts, tools y documentos del track de seguros.
Resultado: El track cambia el dominio; no reemplaza el método del curso.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué límite deberías explicar en la primera frase de tu caso?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Elegir industria significa concretar datos, tareas y límites.

ERRORES CONCEPTUALES FRECUENTES
Elegir un caso que exige sistemas o permisos inexistentes.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: De la apertura al laboratorio L1

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Alcance de S1 y evolución posterior

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 31. Alcance de S1 y evolución posterior

DIAPOSITIVA 31 · CAPÍTULO 11 · CONCEPTO
Título: Alcance de S1 y evolución posterior
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §11
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ubicar las capacidades que se construirán después sin adelantarlas como terminadas.

CONCEPTO PRINCIPAL
Alcance de S1 y evolución posterior

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Distingue siempre arquitectura objetivo y checkpoint implementado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Dónde se implementa el aislamiento de conversaciones?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Ahora: Fundamentos, proveedor y primer script.

S2–S5: Contratos, tools, selección, memoria y RAG.

S6 en adelante: Guardrails, pruebas, operación y evidencia de calidad.

Cierre con la distinción: Distingue siempre arquitectura objetivo y checkpoint implementado.

ELEMENTOS QUE CONVIENE EXPLICAR
Ahora; S2–S5; S6 en adelante. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El equipo quiere que su primer script recuerde todos los pedidos.
Ubicar: L1 no incluye el estado conversacional de L5.
Separar: El historial y el sistema de pedidos cumplen funciones distintas.
Planificar: Esperar la implementación y prueba de cada pieza.
Resultado: El mapa del curso orienta; no certifica capacidades del código actual.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde se implementa el aislamiento de conversaciones?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Distingue siempre arquitectura objetivo y checkpoint implementado.

ERRORES CONCEPTUALES FRECUENTES
Mostrar memoria duradera o despliegue como si ya existieran.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Elección del track

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Siguiente paso: del texto al contrato

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 32. Cómo leer la arquitectura futura

DIAPOSITIVA 32 · CAPÍTULO 11 · DESARROLLO
Título: Cómo leer la arquitectura futura
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §11
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ubicar las capacidades que se construirán después sin adelantarlas como terminadas.

CONCEPTO PRINCIPAL
Alcance de S1 y evolución posterior

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Distingue siempre arquitectura objetivo y checkpoint implementado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Reconocer: Identificar el nombre y propósito de cada componente.

Posponer: No depender de una capacidad todavía no implementada.

Verificar: En cada laboratorio, demostrar la nueva responsabilidad.

Contraste la regla con este error: Mostrar memoria duradera o despliegue como si ya existieran. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Reconocer; Posponer; Verificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El equipo quiere que su primer script recuerde todos los pedidos.
Ubicar: L1 no incluye el estado conversacional de L5.
Separar: El historial y el sistema de pedidos cumplen funciones distintas.
Planificar: Esperar la implementación y prueba de cada pieza.
Resultado: El mapa del curso orienta; no certifica capacidades del código actual.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde se implementa el aislamiento de conversaciones?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Distingue siempre arquitectura objetivo y checkpoint implementado.

ERRORES CONCEPTUALES FRECUENTES
Mostrar memoria duradera o despliegue como si ya existieran.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Elección del track

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Siguiente paso: del texto al contrato

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 33. Ejemplo · Alcance de S1 y evolución posterior

DIAPOSITIVA 33 · CAPÍTULO 11 · EJEMPLO
Título: MercaSur · Alcance de S1 y evolución posterior
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §11
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ubicar las capacidades que se construirán después sin adelantarlas como terminadas.

CONCEPTO PRINCIPAL
Alcance de S1 y evolución posterior

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Distingue siempre arquitectura objetivo y checkpoint implementado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El equipo quiere que su primer script recuerde todos los pedidos. Pida una predicción.

Ubicar: L1 no incluye el estado conversacional de L5.

Separar: El historial y el sistema de pedidos cumplen funciones distintas.

Planificar: Esperar la implementación y prueba de cada pieza.

Resultado esperado: El mapa del curso orienta; no certifica capacidades del código actual. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Ubicar; Separar; Planificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El equipo quiere que su primer script recuerde todos los pedidos.
Ubicar: L1 no incluye el estado conversacional de L5.
Separar: El historial y el sistema de pedidos cumplen funciones distintas.
Planificar: Esperar la implementación y prueba de cada pieza.
Resultado: El mapa del curso orienta; no certifica capacidades del código actual.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde se implementa el aislamiento de conversaciones?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Distingue siempre arquitectura objetivo y checkpoint implementado.

ERRORES CONCEPTUALES FRECUENTES
Mostrar memoria duradera o despliegue como si ya existieran.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Elección del track

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool · Sigue: Siguiente paso: del texto al contrato

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 34. Siguiente paso: del texto al contrato

DIAPOSITIVA 34 · CAPÍTULO 12 · CONCEPTO
Título: Siguiente paso: del texto al contrato
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §12
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Preparar la transición hacia prompts claros y salida validada.

CONCEPTO PRINCIPAL
Siguiente paso: del texto al contrato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El próximo paso añade contrato, no confianza ciega en el texto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué harías con una categoría que tu aplicación no reconoce?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Base S1: El modelo ya recibe y devuelve mensajes.

Problema siguiente: Una aplicación necesita categorías y campos predecibles.

S2: Prompts, ejemplos y Pydantic convierten el resultado en un contrato.

Cierre con la distinción: El próximo paso añade contrato, no confianza ciega en el texto.

ELEMENTOS QUE CONVIENE EXPLICAR
Base S1; Problema siguiente; S2. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una consulta sobre una comisión debe clasificarse antes de actuar.
Entrada: El usuario pregunta por un cobro.
Contrato: El clasificador devolverá una categoría permitida.
Validación: La aplicación comprobará que pertenece a la taxonomía.
Resultado: La respuesta se prepara para que otro componente pueda usarla.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías con una categoría que tu aplicación no reconoce?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El próximo paso añade contrato, no confianza ciega en el texto.

ERRORES CONCEPTUALES FRECUENTES
Confundir exigir JSON con garantizar un objeto válido.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Alcance de S1 y evolución posterior

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 35. Preparar una consulta para S2

DIAPOSITIVA 35 · CAPÍTULO 12 · DESARROLLO
Título: Preparar una consulta para S2
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §12
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Preparar la transición hacia prompts claros y salida validada.

CONCEPTO PRINCIPAL
Siguiente paso: del texto al contrato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El próximo paso añade contrato, no confianza ciega en el texto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Elegir: Tomar una consulta concreta del track.

Definir: Nombrar qué campos necesita la aplicación consumidora.

Anticipar: Pensar qué ocurrirá si el modelo omite o inventa un campo.

Contraste la regla con este error: Confundir exigir JSON con garantizar un objeto válido. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Elegir; Definir; Anticipar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una consulta sobre una comisión debe clasificarse antes de actuar.
Entrada: El usuario pregunta por un cobro.
Contrato: El clasificador devolverá una categoría permitida.
Validación: La aplicación comprobará que pertenece a la taxonomía.
Resultado: La respuesta se prepara para que otro componente pueda usarla.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías con una categoría que tu aplicación no reconoce?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El próximo paso añade contrato, no confianza ciega en el texto.

ERRORES CONCEPTUALES FRECUENTES
Confundir exigir JSON con garantizar un objeto válido.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Alcance de S1 y evolución posterior

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 36. Ejemplo · Siguiente paso: del texto al contrato

DIAPOSITIVA 36 · CAPÍTULO 12 · EJEMPLO
Título: Banco Inti · Siguiente paso: del texto al contrato
Sesión: Fundamentos de los agentes inteligentes
Archivo: 01-fundamentos-agentes-editable-v2.pptx
Sección que soporta: §12
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-01-fundamentos-agentes; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Preparar la transición hacia prompts claros y salida validada.

CONCEPTO PRINCIPAL
Siguiente paso: del texto al contrato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El próximo paso añade contrato, no confianza ciega en el texto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una consulta sobre una comisión debe clasificarse antes de actuar. Pida una predicción.

Entrada: El usuario pregunta por un cobro.

Contrato: El clasificador devolverá una categoría permitida.

Validación: La aplicación comprobará que pertenece a la taxonomía.

Resultado esperado: La respuesta se prepara para que otro componente pueda usarla. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Entrada; Contrato; Validación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una consulta sobre una comisión debe clasificarse antes de actuar.
Entrada: El usuario pregunta por un cobro.
Contrato: El clasificador devolverá una categoría permitida.
Validación: La aplicación comprobará que pertenece a la taxonomía.
Resultado: La respuesta se prepara para que otro componente pueda usarla.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué harías con una categoría que tu aplicación no reconoce?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El próximo paso añade contrato, no confianza ciega en el texto.

ERRORES CONCEPTUALES FRECUENTES
Confundir exigir JSON con garantizar un objeto válido.

CONEXIÓN ANTERIOR
S0: modelos, contexto y entorno · Capítulo previo: Alcance de S1 y evolución posterior

CONEXIÓN POSTERIOR
S2: prompts y contratos; S3: primera tool.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

