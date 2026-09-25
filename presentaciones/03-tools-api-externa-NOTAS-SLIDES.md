# Herramientas e integración externa — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Del conocimiento a la consulta

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Del conocimiento a la consulta
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Responder hechos del negocio a partir de la fuente externa pertinente.

CONCEPTO PRINCIPAL
Del conocimiento a la consulta

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Las tools conectan el lenguaje con capacidades verificables.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué parte aporta el estado real del pedido?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Solicitud: El usuario pide un dato específico del dominio.

Herramienta: Expone una capacidad limitada de consulta.

Respuesta: El modelo redacta a partir del resultado recibido.

Cierre con la distinción: Las tools conectan el lenguaje con capacidades verificables.

ELEMENTOS QUE CONVIENE EXPLICAR
Solicitud; Herramienta; Respuesta. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Dónde está el pedido PED-2026-00123?»
Identificar: La tarea requiere el sistema de pedidos.
Consultar: track_order recibe el identificador validado.
Explicar: El agente usa el estado real devuelto por el simulador.
Resultado: La respuesta puede vincularse con una consulta concreta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte aporta el estado real del pedido?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Las tools conectan el lenguaje con capacidades verificables.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que el LLM conoce el dato porque mencionó una tool.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores.

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Function calling: proponer y ejecutar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Separar tres responsabilidades

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Separar tres responsabilidades
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Responder hechos del negocio a partir de la fuente externa pertinente.

CONCEPTO PRINCIPAL
Del conocimiento a la consulta

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Las tools conectan el lenguaje con capacidades verificables.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Modelo: Propone qué capacidad y argumentos necesita.

Aplicación: Valida y ejecuta la llamada.

Sistema externo: Devuelve el dato o el error del negocio.

Contraste la regla con este error: Afirmar que el LLM conoce el dato porque mencionó una tool. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Modelo; Aplicación; Sistema externo. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Dónde está el pedido PED-2026-00123?»
Identificar: La tarea requiere el sistema de pedidos.
Consultar: track_order recibe el identificador validado.
Explicar: El agente usa el estado real devuelto por el simulador.
Resultado: La respuesta puede vincularse con una consulta concreta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte aporta el estado real del pedido?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Las tools conectan el lenguaje con capacidades verificables.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que el LLM conoce el dato porque mencionó una tool.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores.

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Function calling: proponer y ejecutar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Del conocimiento a la consulta

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: MercaSur · Del conocimiento a la consulta
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Responder hechos del negocio a partir de la fuente externa pertinente.

CONCEPTO PRINCIPAL
Del conocimiento a la consulta

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Las tools conectan el lenguaje con capacidades verificables.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Dónde está el pedido PED-2026-00123?» Pida una predicción.

Identificar: La tarea requiere el sistema de pedidos.

Consultar: track_order recibe el identificador validado.

Explicar: El agente usa el estado real devuelto por el simulador.

Resultado esperado: La respuesta puede vincularse con una consulta concreta. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Identificar; Consultar; Explicar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Dónde está el pedido PED-2026-00123?»
Identificar: La tarea requiere el sistema de pedidos.
Consultar: track_order recibe el identificador validado.
Explicar: El agente usa el estado real devuelto por el simulador.
Resultado: La respuesta puede vincularse con una consulta concreta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte aporta el estado real del pedido?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Las tools conectan el lenguaje con capacidades verificables.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que el LLM conoce el dato porque mencionó una tool.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores.

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Function calling: proponer y ejecutar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Function calling: proponer y ejecutar

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Function calling: proponer y ejecutar
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Seguir la llamada desde la salida del modelo hasta ToolMessage.

CONCEPTO PRINCIPAL
Function calling: proponer y ejecutar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El LLM genera la petición; la aplicación produce el efecto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Quién realiza realmente la conexión HTTP?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Modelo: Produce nombre de tool, argumentos y un identificador de llamada.

Aplicación: Busca la tool, valida argumentos y ejecuta el código.

ToolMessage: Devuelve el resultado asociado a tool_call_id.

Cierre con la distinción: El LLM genera la petición; la aplicación produce el efecto.

ELEMENTOS QUE CONVIENE EXPLICAR
Modelo; Aplicación; ToolMessage. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El modelo propone consultar consumo de una línea.
Propuesta: tool_calls identifica la herramienta y su argumento.
Ejecución: Python realiza la petición HTTP al simulador.
Observación: El resultado vuelve al modelo antes de la respuesta final.
Resultado: Nombrar una herramienta en texto no es ejecutarla.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Quién realiza realmente la conexión HTTP?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El LLM genera la petición; la aplicación produce el efecto.

ERRORES CONCEPTUALES FRECUENTES
Dibujar una flecha directa del modelo a la base como si ejecutara código.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Del conocimiento a la consulta

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Docstring y esquema de argumentos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Completar el intercambio

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Completar el intercambio
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Seguir la llamada desde la salida del modelo hasta ToolMessage.

CONCEPTO PRINCIPAL
Function calling: proponer y ejecutar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El LLM genera la petición; la aplicación produce el efecto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Registrar: Conservar el mensaje del modelo que contiene tool_calls.

Ejecutar: Invocar la capacidad seleccionada con los argumentos.

Continuar: Enviar ToolMessage para que el modelo use la observación.

Contraste la regla con este error: Dibujar una flecha directa del modelo a la base como si ejecutara código. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Registrar; Ejecutar; Continuar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El modelo propone consultar consumo de una línea.
Propuesta: tool_calls identifica la herramienta y su argumento.
Ejecución: Python realiza la petición HTTP al simulador.
Observación: El resultado vuelve al modelo antes de la respuesta final.
Resultado: Nombrar una herramienta en texto no es ejecutarla.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Quién realiza realmente la conexión HTTP?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El LLM genera la petición; la aplicación produce el efecto.

ERRORES CONCEPTUALES FRECUENTES
Dibujar una flecha directa del modelo a la base como si ejecutara código.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Del conocimiento a la consulta

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Docstring y esquema de argumentos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Function calling: proponer y ejecutar

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: AndesMóvil · Function calling: proponer y ejecutar
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Seguir la llamada desde la salida del modelo hasta ToolMessage.

CONCEPTO PRINCIPAL
Function calling: proponer y ejecutar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El LLM genera la petición; la aplicación produce el efecto.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El modelo propone consultar consumo de una línea. Pida una predicción.

Propuesta: tool_calls identifica la herramienta y su argumento.

Ejecución: Python realiza la petición HTTP al simulador.

Observación: El resultado vuelve al modelo antes de la respuesta final.

Resultado esperado: Nombrar una herramienta en texto no es ejecutarla. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Propuesta; Ejecución; Observación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El modelo propone consultar consumo de una línea.
Propuesta: tool_calls identifica la herramienta y su argumento.
Ejecución: Python realiza la petición HTTP al simulador.
Observación: El resultado vuelve al modelo antes de la respuesta final.
Resultado: Nombrar una herramienta en texto no es ejecutarla.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Quién realiza realmente la conexión HTTP?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El LLM genera la petición; la aplicación produce el efecto.

ERRORES CONCEPTUALES FRECUENTES
Dibujar una flecha directa del modelo a la base como si ejecutara código.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Del conocimiento a la consulta

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Docstring y esquema de argumentos

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Docstring y esquema de argumentos

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Docstring y esquema de argumentos
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §2 · regla A2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Diseñar una tool que el modelo pueda seleccionar y usar correctamente.

CONCEPTO PRINCIPAL
Docstring y esquema de argumentos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una tool bien descrita reduce decisiones ambiguas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué frase añadirías para explicar cuándo NO usar tu tool?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Propósito: Describir qué consulta o acción resuelve.

Frontera: Decir cuándo usarla y cuándo no usarla.

Argumentos: Definir campos, tipos y restricciones con args_schema.

Cierre con la distinción: Una tool bien descrita reduce decisiones ambiguas.

ELEMENTOS QUE CONVIENE EXPLICAR
Propósito; Frontera; Argumentos. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una tool consulta saldo; otra, en S4, explicará comisiones.
Aclarar: get_account_balance consulta saldo de una cuenta.
Excluir: No usarla para explicar un cobro o transferir dinero.
Validar: Pedir el identificador exigido por su contrato.
Resultado: La descripción guía la selección y el esquema controla la forma de entrada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué frase añadirías para explicar cuándo NO usar tu tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una tool bien descrita reduce decisiones ambiguas.

ERRORES CONCEPTUALES FRECUENTES
Describir solo la implementación HTTP y omitir el propósito.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Function calling: proponer y ejecutar

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Errores que el modelo puede usar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Revisar el contrato de la tool

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Revisar el contrato de la tool
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §2 · regla A2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Diseñar una tool que el modelo pueda seleccionar y usar correctamente.

CONCEPTO PRINCIPAL
Docstring y esquema de argumentos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una tool bien descrita reduce decisiones ambiguas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Nombre: Debe expresar la capacidad sin ambigüedad.

Docstring: Incluir límites y significado de los parámetros.

Esquema: Rechazar entradas incompletas o incompatibles antes de llamar.

Contraste la regla con este error: Describir solo la implementación HTTP y omitir el propósito. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Nombre; Docstring; Esquema. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una tool consulta saldo; otra, en S4, explicará comisiones.
Aclarar: get_account_balance consulta saldo de una cuenta.
Excluir: No usarla para explicar un cobro o transferir dinero.
Validar: Pedir el identificador exigido por su contrato.
Resultado: La descripción guía la selección y el esquema controla la forma de entrada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué frase añadirías para explicar cuándo NO usar tu tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una tool bien descrita reduce decisiones ambiguas.

ERRORES CONCEPTUALES FRECUENTES
Describir solo la implementación HTTP y omitir el propósito.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Function calling: proponer y ejecutar

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Errores que el modelo puede usar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Docstring y esquema de argumentos

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: Banco Inti · Docstring y esquema de argumentos
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §2 · regla A2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Diseñar una tool que el modelo pueda seleccionar y usar correctamente.

CONCEPTO PRINCIPAL
Docstring y esquema de argumentos

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una tool bien descrita reduce decisiones ambiguas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una tool consulta saldo; otra, en S4, explicará comisiones. Pida una predicción.

Aclarar: get_account_balance consulta saldo de una cuenta.

Excluir: No usarla para explicar un cobro o transferir dinero.

Validar: Pedir el identificador exigido por su contrato.

Resultado esperado: La descripción guía la selección y el esquema controla la forma de entrada. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Aclarar; Excluir; Validar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Una tool consulta saldo; otra, en S4, explicará comisiones.
Aclarar: get_account_balance consulta saldo de una cuenta.
Excluir: No usarla para explicar un cobro o transferir dinero.
Validar: Pedir el identificador exigido por su contrato.
Resultado: La descripción guía la selección y el esquema controla la forma de entrada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué frase añadirías para explicar cuándo NO usar tu tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una tool bien descrita reduce decisiones ambiguas.

ERRORES CONCEPTUALES FRECUENTES
Describir solo la implementación HTTP y omitir el propósito.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Function calling: proponer y ejecutar

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Errores que el modelo puede usar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. Errores que el modelo puede usar

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: Errores que el modelo puede usar
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §3 · regla A4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Convertir fallos técnicos en observaciones útiles sin ocultarlos.

CONCEPTO PRINCIPAL
Errores que el modelo puede usar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El error forma parte del contrato de la herramienta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué diferencia hay entre no encontrado y servicio no disponible?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Éxito: Dato consultado con contexto suficiente.

No encontrado: El identificador no corresponde a un registro disponible.

Servicio caído: La consulta no pudo completarse; no hay dato verificado.

Cierre con la distinción: El error forma parte del contrato de la herramienta.

ELEMENTOS QUE CONVIENE EXPLICAR
Éxito; No encontrado; Servicio caído. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. La consulta de póliza no encuentra el identificador enviado.
Leer: La tool informa que no se encontró la póliza.
Preguntar: Solicitar comprobar el dato aportado.
Evitar: No afirmar que el cliente carece de toda cobertura.
Resultado: No encontrar un registro no demuestra una conclusión más amplia.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre no encontrado y servicio no disponible?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El error forma parte del contrato de la herramienta.

ERRORES CONCEPTUALES FRECUENTES
Devolver una excepción cruda o transformar todo fallo en una respuesta inventada.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Docstring y esquema de argumentos

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Bucle manual y create_agent

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Recuperar según la causa

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Recuperar según la causa
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §3 · regla A4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Convertir fallos técnicos en observaciones útiles sin ocultarlos.

CONCEPTO PRINCIPAL
Errores que el modelo puede usar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El error forma parte del contrato de la herramienta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Entrada incorrecta: Solicitar o corregir el identificador necesario.

Fallo temporal: Reintentar solo si la política y la operación lo permiten.

Sin respuesta: Explicar el límite sin inventar un resultado.

Contraste la regla con este error: Devolver una excepción cruda o transformar todo fallo en una respuesta inventada. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Entrada incorrecta; Fallo temporal; Sin respuesta. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. La consulta de póliza no encuentra el identificador enviado.
Leer: La tool informa que no se encontró la póliza.
Preguntar: Solicitar comprobar el dato aportado.
Evitar: No afirmar que el cliente carece de toda cobertura.
Resultado: No encontrar un registro no demuestra una conclusión más amplia.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre no encontrado y servicio no disponible?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El error forma parte del contrato de la herramienta.

ERRORES CONCEPTUALES FRECUENTES
Devolver una excepción cruda o transformar todo fallo en una respuesta inventada.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Docstring y esquema de argumentos

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Bucle manual y create_agent

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · Errores que el modelo puede usar

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: Andina Seguros · Errores que el modelo puede usar
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §3 · regla A4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Convertir fallos técnicos en observaciones útiles sin ocultarlos.

CONCEPTO PRINCIPAL
Errores que el modelo puede usar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El error forma parte del contrato de la herramienta.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La consulta de póliza no encuentra el identificador enviado. Pida una predicción.

Leer: La tool informa que no se encontró la póliza.

Preguntar: Solicitar comprobar el dato aportado.

Evitar: No afirmar que el cliente carece de toda cobertura.

Resultado esperado: No encontrar un registro no demuestra una conclusión más amplia. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Leer; Preguntar; Evitar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. La consulta de póliza no encuentra el identificador enviado.
Leer: La tool informa que no se encontró la póliza.
Preguntar: Solicitar comprobar el dato aportado.
Evitar: No afirmar que el cliente carece de toda cobertura.
Resultado: No encontrar un registro no demuestra una conclusión más amplia.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre no encontrado y servicio no disponible?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El error forma parte del contrato de la herramienta.

ERRORES CONCEPTUALES FRECUENTES
Devolver una excepción cruda o transformar todo fallo en una respuesta inventada.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Docstring y esquema de argumentos

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Bucle manual y create_agent

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Bucle manual y create_agent

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Bucle manual y create_agent
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer el mismo intercambio de mensajes en dos formas de orquestación.

CONCEPTO PRINCIPAL
Bucle manual y create_agent

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Comprender el bucle permite depurar la abstracción.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué responsabilidad conserva tu función de herramienta?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Manual: La aplicación inspecciona tool_calls y ejecuta explícitamente.

Observación: El resultado vuelve como mensaje de herramienta.

create_agent: La abstracción coordina ese patrón de interacción.

Cierre con la distinción: Comprender el bucle permite depurar la abstracción.

ELEMENTOS QUE CONVIENE EXPLICAR
Manual; Observación; create_agent. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. La primera consulta devuelve un estado de entrega.
Manual: Seguir paso a paso la llamada y ToolMessage.
Abstracción: Repetir con create_agent y las mismas tools.
Comparar: Identificar qué parte coordina ahora el framework.
Resultado: La abstracción reduce código de coordinación, no cambia la fuente del dato.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué responsabilidad conserva tu función de herramienta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Comprender el bucle permite depurar la abstracción.

ERRORES CONCEPTUALES FRECUENTES
Suponer que create_agent arregla automáticamente una tool defectuosa.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Errores que el modelo puede usar

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Laboratorio L3 y Assignment A1

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Qué debe seguir siendo visible

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Qué debe seguir siendo visible
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer el mismo intercambio de mensajes en dos formas de orquestación.

CONCEPTO PRINCIPAL
Bucle manual y create_agent

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Comprender el bucle permite depurar la abstracción.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Catálogo: Las capacidades disponibles permanecen explícitas.

Errores: Las tools siguen siendo responsables de devolver resultados útiles.

Control: La ejecución necesita condiciones de parada y límites.

Contraste la regla con este error: Suponer que create_agent arregla automáticamente una tool defectuosa. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Catálogo; Errores; Control. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. La primera consulta devuelve un estado de entrega.
Manual: Seguir paso a paso la llamada y ToolMessage.
Abstracción: Repetir con create_agent y las mismas tools.
Comparar: Identificar qué parte coordina ahora el framework.
Resultado: La abstracción reduce código de coordinación, no cambia la fuente del dato.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué responsabilidad conserva tu función de herramienta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Comprender el bucle permite depurar la abstracción.

ERRORES CONCEPTUALES FRECUENTES
Suponer que create_agent arregla automáticamente una tool defectuosa.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Errores que el modelo puede usar

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Laboratorio L3 y Assignment A1

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Bucle manual y create_agent

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: MercaSur · Bucle manual y create_agent
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer el mismo intercambio de mensajes en dos formas de orquestación.

CONCEPTO PRINCIPAL
Bucle manual y create_agent

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Comprender el bucle permite depurar la abstracción.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La primera consulta devuelve un estado de entrega. Pida una predicción.

Manual: Seguir paso a paso la llamada y ToolMessage.

Abstracción: Repetir con create_agent y las mismas tools.

Comparar: Identificar qué parte coordina ahora el framework.

Resultado esperado: La abstracción reduce código de coordinación, no cambia la fuente del dato. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Manual; Abstracción; Comparar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. La primera consulta devuelve un estado de entrega.
Manual: Seguir paso a paso la llamada y ToolMessage.
Abstracción: Repetir con create_agent y las mismas tools.
Comparar: Identificar qué parte coordina ahora el framework.
Resultado: La abstracción reduce código de coordinación, no cambia la fuente del dato.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué responsabilidad conserva tu función de herramienta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Comprender el bucle permite depurar la abstracción.

ERRORES CONCEPTUALES FRECUENTES
Suponer que create_agent arregla automáticamente una tool defectuosa.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Errores que el modelo puede usar

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Laboratorio L3 y Assignment A1

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Laboratorio L3 y Assignment A1

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Laboratorio L3 y Assignment A1
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Demostrar una tool de lectura contra el simulador y sus tres escenarios.

CONCEPTO PRINCIPAL
Laboratorio L3 y Assignment A1

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La tool no está terminada hasta que sus errores también son comprensibles.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué evidencia distingue un dato inventado de una consulta real?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Una tool: Implementar la consulta de lectura asignada al track.

Tres escenarios: Éxito, no encontrado y servicio caído.

Evidencia: Mostrar argumentos, resultado y respuesta del agente.

Cierre con la distinción: La tool no está terminada hasta que sus errores también son comprensibles.

ELEMENTOS QUE CONVIENE EXPLICAR
Una tool; Tres escenarios; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El mismo cliente se consulta con los modos de fallo del simulador.
Éxito: El agente explica el dato obtenido.
No encontrado: Pide verificar el identificador.
Caído: Reconoce que no pudo consultar en ese momento.
Resultado: La prueba cubre comportamiento útil y manejo explícito de fallos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia distingue un dato inventado de una consulta real?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La tool no está terminada hasta que sus errores también son comprensibles.

ERRORES CONCEPTUALES FRECUENTES
Probar solo el caso feliz o ejecutar sin registrar la observación.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Bucle manual y create_agent

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Del primer conector al catálogo

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Preparar una prueba reproducible

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Preparar una prueba reproducible
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Demostrar una tool de lectura contra el simulador y sus tres escenarios.

CONCEPTO PRINCIPAL
Laboratorio L3 y Assignment A1

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La tool no está terminada hasta que sus errores también son comprensibles.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Caso: Usar la entrada y el modo de fallo indicados por el laboratorio.

Observación: Conservar el resultado de la tool antes de la redacción.

Criterio: Comprobar que la respuesta refleja ese resultado.

Contraste la regla con este error: Probar solo el caso feliz o ejecutar sin registrar la observación. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Caso; Observación; Criterio. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El mismo cliente se consulta con los modos de fallo del simulador.
Éxito: El agente explica el dato obtenido.
No encontrado: Pide verificar el identificador.
Caído: Reconoce que no pudo consultar en ese momento.
Resultado: La prueba cubre comportamiento útil y manejo explícito de fallos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia distingue un dato inventado de una consulta real?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La tool no está terminada hasta que sus errores también son comprensibles.

ERRORES CONCEPTUALES FRECUENTES
Probar solo el caso feliz o ejecutar sin registrar la observación.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Bucle manual y create_agent

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Del primer conector al catálogo

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Laboratorio L3 y Assignment A1

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: AndesMóvil · Laboratorio L3 y Assignment A1
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Demostrar una tool de lectura contra el simulador y sus tres escenarios.

CONCEPTO PRINCIPAL
Laboratorio L3 y Assignment A1

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La tool no está terminada hasta que sus errores también son comprensibles.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El mismo cliente se consulta con los modos de fallo del simulador. Pida una predicción.

Éxito: El agente explica el dato obtenido.

No encontrado: Pide verificar el identificador.

Caído: Reconoce que no pudo consultar en ese momento.

Resultado esperado: La prueba cubre comportamiento útil y manejo explícito de fallos. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Éxito; No encontrado; Caído. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El mismo cliente se consulta con los modos de fallo del simulador.
Éxito: El agente explica el dato obtenido.
No encontrado: Pide verificar el identificador.
Caído: Reconoce que no pudo consultar en ese momento.
Resultado: La prueba cubre comportamiento útil y manejo explícito de fallos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia distingue un dato inventado de una consulta real?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La tool no está terminada hasta que sus errores también son comprensibles.

ERRORES CONCEPTUALES FRECUENTES
Probar solo el caso feliz o ejecutar sin registrar la observación.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Bucle manual y create_agent

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica · Sigue: Del primer conector al catálogo

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. Del primer conector al catálogo

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: Del primer conector al catálogo
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: proyecto-final y Qué NO entra hoy
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Situar la primera tool como base de las decisiones entre varias capacidades.

CONCEPTO PRINCIPAL
Del primer conector al catálogo

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El catálogo crece sobre contratos claros, no sobre funciones indistintas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué debe quedar estable al incorporar la segunda tool?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Checkpoint L3: Una herramienta de lectura con contrato y errores.

S4: Cuatro tools núcleo con responsabilidades diferenciadas.

Proyecto: Reutilizar el trabajo en una arquitectura acumulativa.

Cierre con la distinción: El catálogo crece sobre contratos claros, no sobre funciones indistintas.

ELEMENTOS QUE CONVIENE EXPLICAR
Checkpoint L3; S4; Proyecto. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Un equipo quiere añadir saldo, movimientos, comisiones y riesgo.
Partir: La primera consulta ya maneja errores.
Diseñar: Separar responsabilidades de las nuevas tools.
Anticipar: S4 medirá confusiones entre ellas.
Resultado: Sumar tools aumenta opciones y también posibilidades de selección incorrecta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué debe quedar estable al incorporar la segunda tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El catálogo crece sobre contratos claros, no sobre funciones indistintas.

ERRORES CONCEPTUALES FRECUENTES
Ampliar capacidades sin probar selección ni límites.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Laboratorio L3 y Assignment A1

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. Preparar la ampliación

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: Preparar la ampliación
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: proyecto-final y Qué NO entra hoy
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Situar la primera tool como base de las decisiones entre varias capacidades.

CONCEPTO PRINCIPAL
Del primer conector al catálogo

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El catálogo crece sobre contratos claros, no sobre funciones indistintas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Conservar: Mantener las garantías de la primera tool.

Diferenciar: Definir fronteras antes de sumar capacidades.

Medir: Comprobar selección correcta cuando exista más de una opción.

Contraste la regla con este error: Ampliar capacidades sin probar selección ni límites. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Conservar; Diferenciar; Medir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Un equipo quiere añadir saldo, movimientos, comisiones y riesgo.
Partir: La primera consulta ya maneja errores.
Diseñar: Separar responsabilidades de las nuevas tools.
Anticipar: S4 medirá confusiones entre ellas.
Resultado: Sumar tools aumenta opciones y también posibilidades de selección incorrecta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué debe quedar estable al incorporar la segunda tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El catálogo crece sobre contratos claros, no sobre funciones indistintas.

ERRORES CONCEPTUALES FRECUENTES
Ampliar capacidades sin probar selección ni límites.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Laboratorio L3 y Assignment A1

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · Del primer conector al catálogo

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: Banco Inti · Del primer conector al catálogo
Sesión: Herramientas e integración externa
Archivo: 03-tools-api-externa-editable-v2.pptx
Sección que soporta: proyecto-final y Qué NO entra hoy
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-03-tools-api-externa/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-03-tools-api-externa; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Situar la primera tool como base de las decisiones entre varias capacidades.

CONCEPTO PRINCIPAL
Del primer conector al catálogo

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El catálogo crece sobre contratos claros, no sobre funciones indistintas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Un equipo quiere añadir saldo, movimientos, comisiones y riesgo. Pida una predicción.

Partir: La primera consulta ya maneja errores.

Diseñar: Separar responsabilidades de las nuevas tools.

Anticipar: S4 medirá confusiones entre ellas.

Resultado esperado: Sumar tools aumenta opciones y también posibilidades de selección incorrecta. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Partir; Diseñar; Anticipar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Un equipo quiere añadir saldo, movimientos, comisiones y riesgo.
Partir: La primera consulta ya maneja errores.
Diseñar: Separar responsabilidades de las nuevas tools.
Anticipar: S4 medirá confusiones entre ellas.
Resultado: Sumar tools aumenta opciones y también posibilidades de selección incorrecta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué debe quedar estable al incorporar la segunda tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El catálogo crece sobre contratos claros, no sobre funciones indistintas.

ERRORES CONCEPTUALES FRECUENTES
Ampliar capacidades sin probar selección ni límites.

CONEXIÓN ANTERIOR
S2: esquemas y recuperación de errores · Capítulo previo: Laboratorio L3 y Assignment A1

CONEXIÓN POSTERIOR
S4: catálogo de tools y selección dinámica.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

