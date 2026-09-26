# Prompts, mensajes y contratos — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Del primer llamado al primer contrato

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Del primer llamado al primer contrato
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Pasar de texto libre a una salida que la aplicación puede validar y consumir.

CONCEPTO PRINCIPAL
Del primer llamado al primer contrato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un contrato explícito hace visible el error antes de actuar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Por qué un párrafo bien redactado puede ser inútil para el consumidor?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Entrada: Consulta del cliente expresada en lenguaje natural.

Contrato: Campos, tipos y categorías esperados por la aplicación.

Resultado: Objeto validado o fallo explícito recuperable.

Cierre con la distinción: Un contrato explícito hace visible el error antes de actuar.

ELEMENTOS QUE CONVIENE EXPLICAR
Entrada; Contrato; Resultado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Dónde está mi pedido?» debe convertirse en una intención.
Definir: Elegir la categoría de seguimiento del track.
Extraer: Solicitar el objeto estructurado al modelo.
Validar: Aceptar el contrato o activar recuperación.
Resultado: El clasificador prepara una decisión; todavía no consulta el pedido.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué un párrafo bien redactado puede ser inútil para el consumidor?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un contrato explícito hace visible el error antes de actuar.

ERRORES CONCEPTUALES FRECUENTES
Considerar suficiente que la salida parezca JSON.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo.

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Mensajes, roles y statelessness

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Qué necesita el consumidor

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Qué necesita el consumidor
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Pasar de texto libre a una salida que la aplicación puede validar y consumir.

CONCEPTO PRINCIPAL
Del primer llamado al primer contrato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un contrato explícito hace visible el error antes de actuar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Forma: El dato debe cumplir el esquema.

Categoría: Solo se aceptan valores definidos para el track.

Fallo: La ausencia de un objeto válido no se disfraza de éxito.

Contraste la regla con este error: Considerar suficiente que la salida parezca JSON. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Forma; Categoría; Fallo. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Dónde está mi pedido?» debe convertirse en una intención.
Definir: Elegir la categoría de seguimiento del track.
Extraer: Solicitar el objeto estructurado al modelo.
Validar: Aceptar el contrato o activar recuperación.
Resultado: El clasificador prepara una decisión; todavía no consulta el pedido.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué un párrafo bien redactado puede ser inútil para el consumidor?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un contrato explícito hace visible el error antes de actuar.

ERRORES CONCEPTUALES FRECUENTES
Considerar suficiente que la salida parezca JSON.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo.

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Mensajes, roles y statelessness

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Del primer llamado al primer contrato

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: MercaSur · Del primer llamado al primer contrato
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Pasar de texto libre a una salida que la aplicación puede validar y consumir.

CONCEPTO PRINCIPAL
Del primer llamado al primer contrato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un contrato explícito hace visible el error antes de actuar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Dónde está mi pedido?» debe convertirse en una intención. Pida una predicción.

Definir: Elegir la categoría de seguimiento del track.

Extraer: Solicitar el objeto estructurado al modelo.

Validar: Aceptar el contrato o activar recuperación.

Resultado esperado: El clasificador prepara una decisión; todavía no consulta el pedido. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Definir; Extraer; Validar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Dónde está mi pedido?» debe convertirse en una intención.
Definir: Elegir la categoría de seguimiento del track.
Extraer: Solicitar el objeto estructurado al modelo.
Validar: Aceptar el contrato o activar recuperación.
Resultado: El clasificador prepara una decisión; todavía no consulta el pedido.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué un párrafo bien redactado puede ser inútil para el consumidor?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un contrato explícito hace visible el error antes de actuar.

ERRORES CONCEPTUALES FRECUENTES
Considerar suficiente que la salida parezca JSON.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo.

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Mensajes, roles y statelessness

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Mensajes, roles y statelessness

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Mensajes, roles y statelessness
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Construir la entrada conversacional con roles y contexto explícitos.

CONCEPTO PRINCIPAL
Mensajes, roles y statelessness

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La conversación existe porque la aplicación la administra.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué cambia si solo envías el último mensaje?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

System: Instrucciones de tarea y límites de la aplicación.

Human: Consulta actual y mensajes del usuario.

AI y Tool: Respuesta del modelo y, más adelante, resultados de herramientas.

Cierre con la distinción: La conversación existe porque la aplicación la administra.

ELEMENTOS QUE CONVIENE EXPLICAR
System; Human; AI y Tool. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El usuario dice «mi línea termina en 321» y luego «¿cuánto consumí?».
Separar: El segundo mensaje no contiene toda la identificación.
Preparar: La aplicación aporta el contexto permitido.
Limitar: Los datos reales se consultarán mediante tools en S3.
Resultado: Los roles organizan el contexto; no crean almacenamiento automático.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué cambia si solo envías el último mensaje?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La conversación existe porque la aplicación la administra.

ERRORES CONCEPTUALES FRECUENTES
Suponer que los roles guardan memoria por sí mismos.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Del primer llamado al primer contrato

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Rol, contexto, tarea y formato

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Quién conserva cada parte

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Quién conserva cada parte
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Construir la entrada conversacional con roles y contexto explícitos.

CONCEPTO PRINCIPAL
Mensajes, roles y statelessness

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La conversación existe porque la aplicación la administra.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Aplicación: Construye la lista de mensajes de la llamada.

Modelo: Responde a lo que recibe en esa invocación.

Historial: Debe reenviarse cuando la tarea depende del turno anterior.

Contraste la regla con este error: Suponer que los roles guardan memoria por sí mismos. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Aplicación; Modelo; Historial. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El usuario dice «mi línea termina en 321» y luego «¿cuánto consumí?».
Separar: El segundo mensaje no contiene toda la identificación.
Preparar: La aplicación aporta el contexto permitido.
Limitar: Los datos reales se consultarán mediante tools en S3.
Resultado: Los roles organizan el contexto; no crean almacenamiento automático.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué cambia si solo envías el último mensaje?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La conversación existe porque la aplicación la administra.

ERRORES CONCEPTUALES FRECUENTES
Suponer que los roles guardan memoria por sí mismos.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Del primer llamado al primer contrato

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Rol, contexto, tarea y formato

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Mensajes, roles y statelessness

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: AndesMóvil · Mensajes, roles y statelessness
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Construir la entrada conversacional con roles y contexto explícitos.

CONCEPTO PRINCIPAL
Mensajes, roles y statelessness

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La conversación existe porque la aplicación la administra.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El usuario dice «mi línea termina en 321» y luego «¿cuánto consumí?». Pida una predicción.

Separar: El segundo mensaje no contiene toda la identificación.

Preparar: La aplicación aporta el contexto permitido.

Limitar: Los datos reales se consultarán mediante tools en S3.

Resultado esperado: Los roles organizan el contexto; no crean almacenamiento automático. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Separar; Preparar; Limitar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El usuario dice «mi línea termina en 321» y luego «¿cuánto consumí?».
Separar: El segundo mensaje no contiene toda la identificación.
Preparar: La aplicación aporta el contexto permitido.
Limitar: Los datos reales se consultarán mediante tools en S3.
Resultado: Los roles organizan el contexto; no crean almacenamiento automático.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué cambia si solo envías el último mensaje?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La conversación existe porque la aplicación la administra.

ERRORES CONCEPTUALES FRECUENTES
Suponer que los roles guardan memoria por sí mismos.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Del primer llamado al primer contrato

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Rol, contexto, tarea y formato

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Rol, contexto, tarea y formato

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Rol, contexto, tarea y formato
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Redactar un prompt con responsabilidades identificables y comprobables.

CONCEPTO PRINCIPAL
Rol, contexto, tarea y formato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un buen prompt puede explicarse y probarse por partes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué sección modificarías si la categoría es correcta pero el formato falla?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Rol y contexto: Definir para quién trabaja y con qué información.

Tarea: Especificar la transformación que debe realizar.

Formato: Describir la salida requerida por el consumidor.

Cierre con la distinción: Un buen prompt puede explicarse y probarse por partes.

ELEMENTOS QUE CONVIENE EXPLICAR
Rol y contexto; Tarea; Formato. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Clasifica «No entiendo este cobro» dentro de la taxonomía bancaria.
Rol: Clasificador de consultas del track banca.
Tarea: Elegir una intención permitida sin inventar saldos.
Formato: Devolver el objeto que exige el esquema del laboratorio.
Resultado: Cada parte del prompt contribuye a una responsabilidad concreta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué sección modificarías si la categoría es correcta pero el formato falla?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un buen prompt puede explicarse y probarse por partes.

ERRORES CONCEPTUALES FRECUENTES
Añadir instrucciones largas sin resolver la ambigüedad.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Mensajes, roles y statelessness

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Few-shot para desambiguar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Diagnosticar un prompt incompleto

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Diagnosticar un prompt incompleto
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Redactar un prompt con responsabilidades identificables y comprobables.

CONCEPTO PRINCIPAL
Rol, contexto, tarea y formato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un buen prompt puede explicarse y probarse por partes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Ambigüedad: ¿Falta indicar qué debe decidir?

Información: ¿Tiene datos suficientes o debe reconocer un límite?

Contrato: ¿La salida esperada puede verificarse con un esquema?

Contraste la regla con este error: Añadir instrucciones largas sin resolver la ambigüedad. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Ambigüedad; Información; Contrato. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Clasifica «No entiendo este cobro» dentro de la taxonomía bancaria.
Rol: Clasificador de consultas del track banca.
Tarea: Elegir una intención permitida sin inventar saldos.
Formato: Devolver el objeto que exige el esquema del laboratorio.
Resultado: Cada parte del prompt contribuye a una responsabilidad concreta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué sección modificarías si la categoría es correcta pero el formato falla?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un buen prompt puede explicarse y probarse por partes.

ERRORES CONCEPTUALES FRECUENTES
Añadir instrucciones largas sin resolver la ambigüedad.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Mensajes, roles y statelessness

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Few-shot para desambiguar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Rol, contexto, tarea y formato

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: Banco Inti · Rol, contexto, tarea y formato
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Redactar un prompt con responsabilidades identificables y comprobables.

CONCEPTO PRINCIPAL
Rol, contexto, tarea y formato

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un buen prompt puede explicarse y probarse por partes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Clasifica «No entiendo este cobro» dentro de la taxonomía bancaria. Pida una predicción.

Rol: Clasificador de consultas del track banca.

Tarea: Elegir una intención permitida sin inventar saldos.

Formato: Devolver el objeto que exige el esquema del laboratorio.

Resultado esperado: Cada parte del prompt contribuye a una responsabilidad concreta. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Rol; Tarea; Formato. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Clasifica «No entiendo este cobro» dentro de la taxonomía bancaria.
Rol: Clasificador de consultas del track banca.
Tarea: Elegir una intención permitida sin inventar saldos.
Formato: Devolver el objeto que exige el esquema del laboratorio.
Resultado: Cada parte del prompt contribuye a una responsabilidad concreta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué sección modificarías si la categoría es correcta pero el formato falla?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un buen prompt puede explicarse y probarse por partes.

ERRORES CONCEPTUALES FRECUENTES
Añadir instrucciones largas sin resolver la ambigüedad.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Mensajes, roles y statelessness

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Few-shot para desambiguar

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. Few-shot para desambiguar

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: Few-shot para desambiguar
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §3 · regla A5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Usar ejemplos contrastivos para aclarar decisiones difíciles del dominio.

CONCEPTO PRINCIPAL
Few-shot para desambiguar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué par de ejemplos ayudaría a separar tus dos categorías más confundidas?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Caso de entrada: Una formulación que suele generar confusión.

Salida esperada: La etiqueta y campos definidos por el contrato.

Contraste: Otro caso parecido que debe recibir una categoría distinta.

Cierre con la distinción: Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

ELEMENTOS QUE CONVIENE EXPLICAR
Caso de entrada; Salida esperada; Contraste. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Hay stock?» y «¿Dónde está mi pedido?» hablan de productos, pero piden cosas distintas.
Ejemplo 1: Existencia del producto → intención de stock.
Ejemplo 2: Pedido ya creado → intención de seguimiento.
Prueba nueva: «¿Llegó mi compra?» debe reconocer seguimiento.
Resultado: El ejemplo enseña el criterio de distinción, no una palabra mágica.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué par de ejemplos ayudaría a separar tus dos categorías más confundidas?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

ERRORES CONCEPTUALES FRECUENTES
Confundir ejemplos en el prompt con fine-tuning.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Rol, contexto, tarea y formato

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Salida estructurada y validación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Elegir ejemplos útiles

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Elegir ejemplos útiles
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §3 · regla A5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Usar ejemplos contrastivos para aclarar decisiones difíciles del dominio.

CONCEPTO PRINCIPAL
Few-shot para desambiguar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Representativos: Incluir lenguaje realista del track.

Diferenciadores: Aclarar fronteras entre categorías cercanas.

Separados: No usar las respuestas del test como demostración de generalización.

Contraste la regla con este error: Confundir ejemplos en el prompt con fine-tuning. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Representativos; Diferenciadores; Separados. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Hay stock?» y «¿Dónde está mi pedido?» hablan de productos, pero piden cosas distintas.
Ejemplo 1: Existencia del producto → intención de stock.
Ejemplo 2: Pedido ya creado → intención de seguimiento.
Prueba nueva: «¿Llegó mi compra?» debe reconocer seguimiento.
Resultado: El ejemplo enseña el criterio de distinción, no una palabra mágica.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué par de ejemplos ayudaría a separar tus dos categorías más confundidas?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

ERRORES CONCEPTUALES FRECUENTES
Confundir ejemplos en el prompt con fine-tuning.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Rol, contexto, tarea y formato

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Salida estructurada y validación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · Few-shot para desambiguar

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: MercaSur · Few-shot para desambiguar
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §3 · regla A5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Usar ejemplos contrastivos para aclarar decisiones difíciles del dominio.

CONCEPTO PRINCIPAL
Few-shot para desambiguar

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Hay stock?» y «¿Dónde está mi pedido?» hablan de productos, pero piden cosas distintas. Pida una predicción.

Ejemplo 1: Existencia del producto → intención de stock.

Ejemplo 2: Pedido ya creado → intención de seguimiento.

Prueba nueva: «¿Llegó mi compra?» debe reconocer seguimiento.

Resultado esperado: El ejemplo enseña el criterio de distinción, no una palabra mágica. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Ejemplo 1; Ejemplo 2; Prueba nueva. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Hay stock?» y «¿Dónde está mi pedido?» hablan de productos, pero piden cosas distintas.
Ejemplo 1: Existencia del producto → intención de stock.
Ejemplo 2: Pedido ya creado → intención de seguimiento.
Prueba nueva: «¿Llegó mi compra?» debe reconocer seguimiento.
Resultado: El ejemplo enseña el criterio de distinción, no una palabra mágica.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué par de ejemplos ayudaría a separar tus dos categorías más confundidas?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Few-shot aporta demostraciones dentro del contexto; no entrena pesos.

ERRORES CONCEPTUALES FRECUENTES
Confundir ejemplos en el prompt con fine-tuning.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Rol, contexto, tarea y formato

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Salida estructurada y validación

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Salida estructurada y validación

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Salida estructurada y validación
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §4 y comun/structured.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Tratar una salida mal formada como un fallo esperable del contrato.

CONCEPTO PRINCIPAL
Salida estructurada y validación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Solicitar estructura y validar estructura son responsabilidades distintas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Cuántos intentos hay si reintentos=1?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Esquema: Pydantic define campos y valores válidos.

Modelo: with_structured_output solicita esa estructura.

Validación: El wrapper detecta errores, None o tipos inesperados.

Cierre con la distinción: Solicitar estructura y validar estructura son responsabilidades distintas.

ELEMENTOS QUE CONVIENE EXPLICAR
Esquema; Modelo; Validación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El clasificador devuelve una categoría fuera del enum.
Detectar: El contrato rechaza el valor.
Corregir: El segundo intento recibe la restricción incumplida.
Cerrar: Si vuelve a fallar, solicitar reformulación sin propagar None.
Resultado: La recuperación tiene un límite y un resultado de error definido.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Cuántos intentos hay si reintentos=1?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Solicitar estructura y validar estructura son responsabilidades distintas.

ERRORES CONCEPTUALES FRECUENTES
Interpretar un reintento como intentos ilimitados o garantía de éxito.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Few-shot para desambiguar

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Medir el clasificador en L2

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Recuperación acotada

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Recuperación acotada
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §4 y comun/structured.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Tratar una salida mal formada como un fallo esperable del contrato.

CONCEPTO PRINCIPAL
Salida estructurada y validación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Solicitar estructura y validar estructura son responsabilidades distintas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Intento inicial: Solicitar la salida estructurada.

Corrección: Devolver el error y los campos obligatorios; reintentar una vez por defecto.

Fallo explícito: Lanzar ExtraccionFallida si ambos intentos fallan.

Contraste la regla con este error: Interpretar un reintento como intentos ilimitados o garantía de éxito. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Intento inicial; Corrección; Fallo explícito. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El clasificador devuelve una categoría fuera del enum.
Detectar: El contrato rechaza el valor.
Corregir: El segundo intento recibe la restricción incumplida.
Cerrar: Si vuelve a fallar, solicitar reformulación sin propagar None.
Resultado: La recuperación tiene un límite y un resultado de error definido.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Cuántos intentos hay si reintentos=1?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Solicitar estructura y validar estructura son responsabilidades distintas.

ERRORES CONCEPTUALES FRECUENTES
Interpretar un reintento como intentos ilimitados o garantía de éxito.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Few-shot para desambiguar

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Medir el clasificador en L2

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Salida estructurada y validación

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: Andina Seguros · Salida estructurada y validación
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §4 y comun/structured.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Tratar una salida mal formada como un fallo esperable del contrato.

CONCEPTO PRINCIPAL
Salida estructurada y validación

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Solicitar estructura y validar estructura son responsabilidades distintas.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El clasificador devuelve una categoría fuera del enum. Pida una predicción.

Detectar: El contrato rechaza el valor.

Corregir: El segundo intento recibe la restricción incumplida.

Cerrar: Si vuelve a fallar, solicitar reformulación sin propagar None.

Resultado esperado: La recuperación tiene un límite y un resultado de error definido. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Detectar; Corregir; Cerrar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El clasificador devuelve una categoría fuera del enum.
Detectar: El contrato rechaza el valor.
Corregir: El segundo intento recibe la restricción incumplida.
Cerrar: Si vuelve a fallar, solicitar reformulación sin propagar None.
Resultado: La recuperación tiene un límite y un resultado de error definido.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Cuántos intentos hay si reintentos=1?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Solicitar estructura y validar estructura son responsabilidades distintas.

ERRORES CONCEPTUALES FRECUENTES
Interpretar un reintento como intentos ilimitados o garantía de éxito.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Few-shot para desambiguar

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Medir el clasificador en L2

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Medir el clasificador en L2

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Medir el clasificador en L2
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Evaluar las decisiones sobre casos conocidos y consultas propias.

CONCEPTO PRINCIPAL
Medir el clasificador en L2

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Mide el contrato y la decisión por separado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Un objeto válido cuenta como clasificación correcta?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Taxonomía: Las categorías se alinean con las tools del L4.

Dataset: Casos del track permiten medir aciertos y confusiones.

Casos nuevos: Cinco consultas propias exploran límites del clasificador.

Cierre con la distinción: Mide el contrato y la decisión por separado.

ELEMENTOS QUE CONVIENE EXPLICAR
Taxonomía; Dataset; Casos nuevos. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El clasificador confunde consulta de plan y consulta de consumo.
Revisar: Separar esas filas en el resultado.
Modificar: Agregar ejemplos que distingan plan contratado y datos usados.
Repetir: Medir sobre el mismo conjunto y conservar evidencia.
Resultado: La mejora debe verse en casos comparables, no en una única pregunta favorable.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un objeto válido cuenta como clasificación correcta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Mide el contrato y la decisión por separado.

ERRORES CONCEPTUALES FRECUENTES
Ocultar errores de validación dentro de un único porcentaje.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Salida estructurada y validación

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Puente hacia herramientas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Leer más que un porcentaje

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Leer más que un porcentaje
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Evaluar las decisiones sobre casos conocidos y consultas propias.

CONCEPTO PRINCIPAL
Medir el clasificador en L2

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Mide el contrato y la decisión por separado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Error de contrato: La salida no pudo validarse.

Error de categoría: El objeto es válido, pero la intención es incorrecta.

Análisis: Agrupar confusiones antes de cambiar prompt o ejemplos.

Contraste la regla con este error: Ocultar errores de validación dentro de un único porcentaje. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Error de contrato; Error de categoría; Análisis. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El clasificador confunde consulta de plan y consulta de consumo.
Revisar: Separar esas filas en el resultado.
Modificar: Agregar ejemplos que distingan plan contratado y datos usados.
Repetir: Medir sobre el mismo conjunto y conservar evidencia.
Resultado: La mejora debe verse en casos comparables, no en una única pregunta favorable.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un objeto válido cuenta como clasificación correcta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Mide el contrato y la decisión por separado.

ERRORES CONCEPTUALES FRECUENTES
Ocultar errores de validación dentro de un único porcentaje.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Salida estructurada y validación

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Puente hacia herramientas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Medir el clasificador en L2

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: AndesMóvil · Medir el clasificador en L2
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: §5 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Evaluar las decisiones sobre casos conocidos y consultas propias.

CONCEPTO PRINCIPAL
Medir el clasificador en L2

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Mide el contrato y la decisión por separado.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El clasificador confunde consulta de plan y consulta de consumo. Pida una predicción.

Revisar: Separar esas filas en el resultado.

Modificar: Agregar ejemplos que distingan plan contratado y datos usados.

Repetir: Medir sobre el mismo conjunto y conservar evidencia.

Resultado esperado: La mejora debe verse en casos comparables, no en una única pregunta favorable. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Revisar; Modificar; Repetir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El clasificador confunde consulta de plan y consulta de consumo.
Revisar: Separar esas filas en el resultado.
Modificar: Agregar ejemplos que distingan plan contratado y datos usados.
Repetir: Medir sobre el mismo conjunto y conservar evidencia.
Resultado: La mejora debe verse en casos comparables, no en una única pregunta favorable.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Un objeto válido cuenta como clasificación correcta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Mide el contrato y la decisión por separado.

ERRORES CONCEPTUALES FRECUENTES
Ocultar errores de validación dentro de un único porcentaje.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Salida estructurada y validación

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo · Sigue: Puente hacia herramientas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. Puente hacia herramientas

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: Puente hacia herramientas
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: Qué NO entra hoy y conexión L3/L4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar qué reutiliza la próxima sesión y qué capacidad todavía falta.

CONCEPTO PRINCIPAL
Puente hacia herramientas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Clasificar, consultar y autorizar son decisiones diferentes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué dos comprobaciones faltan entre una intención y una operación externa?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

S2: Comprende intención y valida estructura.

S3: Usa esquemas como argumentos de una herramienta externa.

S4: Decide entre varias herramientas del catálogo.

Cierre con la distinción: Clasificar, consultar y autorizar son decisiones diferentes.

ELEMENTOS QUE CONVIENE EXPLICAR
S2; S3; S4. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El clasificador reconoce una consulta de saldo.
Ahora: Devuelve la categoría permitida.
Después: Una tool consultará get_account_balance.
Límite: Reconocer saldo no autoriza una transferencia.
Resultado: El contrato prepara la acción, pero no la ejecuta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dos comprobaciones faltan entre una intención y una operación externa?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Clasificar, consultar y autorizar son decisiones diferentes.

ERRORES CONCEPTUALES FRECUENTES
Presentar el clasificador como agente con tools ya implementadas.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Medir el clasificador en L2

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. De categoría a acción controlada

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: De categoría a acción controlada
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: Qué NO entra hoy y conexión L3/L4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar qué reutiliza la próxima sesión y qué capacidad todavía falta.

CONCEPTO PRINCIPAL
Puente hacia herramientas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Clasificar, consultar y autorizar son decisiones diferentes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Interpretación: Identificar la tarea y sus datos necesarios.

Contrato: Validar argumentos de entrada a la capacidad.

Ejecución: La aplicación realizará la llamada y manejará sus errores.

Contraste la regla con este error: Presentar el clasificador como agente con tools ya implementadas. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Interpretación; Contrato; Ejecución. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El clasificador reconoce una consulta de saldo.
Ahora: Devuelve la categoría permitida.
Después: Una tool consultará get_account_balance.
Límite: Reconocer saldo no autoriza una transferencia.
Resultado: El contrato prepara la acción, pero no la ejecuta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dos comprobaciones faltan entre una intención y una operación externa?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Clasificar, consultar y autorizar son decisiones diferentes.

ERRORES CONCEPTUALES FRECUENTES
Presentar el clasificador como agente con tools ya implementadas.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Medir el clasificador en L2

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · Puente hacia herramientas

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: Banco Inti · Puente hacia herramientas
Sesión: Prompts, mensajes y contratos
Archivo: 02-ecosistema-langchain-editable.pptx
Sección que soporta: Qué NO entra hoy y conexión L3/L4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-1-fundamentos/sesion-02-ecosistema-langchain; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar qué reutiliza la próxima sesión y qué capacidad todavía falta.

CONCEPTO PRINCIPAL
Puente hacia herramientas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Clasificar, consultar y autorizar son decisiones diferentes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El clasificador reconoce una consulta de saldo. Pida una predicción.

Ahora: Devuelve la categoría permitida.

Después: Una tool consultará get_account_balance.

Límite: Reconocer saldo no autoriza una transferencia.

Resultado esperado: El contrato prepara la acción, pero no la ejecuta. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Ahora; Después; Límite. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El clasificador reconoce una consulta de saldo.
Ahora: Devuelve la categoría permitida.
Después: Una tool consultará get_account_balance.
Límite: Reconocer saldo no autoriza una transferencia.
Resultado: El contrato prepara la acción, pero no la ejecuta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dos comprobaciones faltan entre una intención y una operación externa?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Clasificar, consultar y autorizar son decisiones diferentes.

ERRORES CONCEPTUALES FRECUENTES
Presentar el clasificador como agente con tools ya implementadas.

CONEXIÓN ANTERIOR
S1: primera llamada al modelo · Capítulo previo: Medir el clasificador en L2

CONEXIÓN POSTERIOR
S3: argumentos de herramientas; S4: selección de catálogo.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

