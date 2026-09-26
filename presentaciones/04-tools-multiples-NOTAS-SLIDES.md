# Catálogo de tools e integración — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. De una tool a cuatro

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: De una tool a cuatro
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer que ampliar el catálogo añade decisiones que deben medirse.

CONCEPTO PRINCIPAL
De una tool a cuatro

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Cada decisión adicional merece una prueba.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué falla si la tool ejecuta bien pero fue mal elegida?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Capacidades: Cada tool resuelve una necesidad definida del track.

Selección: El modelo decide cuál corresponde a la consulta.

Evidencia: Se compara la tool llamada con la esperada.

Cierre con la distinción: Cada decisión adicional merece una prueba.

ELEMENTOS QUE CONVIENE EXPLICAR
Capacidades; Selección; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El agente debe consultar stock y luego describir el producto.
Elegir: check_stock_by_store responde disponibilidad.
Continuar: get_product_details aporta características.
Comprobar: Una tool correcta no compensa la otra elección equivocada.
Resultado: La fiabilidad de una secuencia no se deduce del mejor paso aislado.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falla si la tool ejecuta bien pero fue mal elegida?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Cada decisión adicional merece una prueba.

ERRORES CONCEPTUALES FRECUENTES
Presentar 93 % como medición universal del modelo.

CONEXIÓN ANTERIOR
S3: primera tool con contrato.

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Responsabilidad única en el catálogo

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. La fiabilidad se compone

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: La fiabilidad se compone
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer que ampliar el catálogo añade decisiones que deben medirse.

CONCEPTO PRINCIPAL
De una tool a cuatro

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Cada decisión adicional merece una prueba.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Paso: Una elección puede fallar aunque la tool funcione.

Cadena: En un modelo ilustrativo, 0,93³ ≈ 0,804.

Supuesto: El producto requiere tasas condicionales apropiadas; no prueba independencia real.

Contraste la regla con este error: Presentar 93 % como medición universal del modelo. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Paso; Cadena; Supuesto. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El agente debe consultar stock y luego describir el producto.
Elegir: check_stock_by_store responde disponibilidad.
Continuar: get_product_details aporta características.
Comprobar: Una tool correcta no compensa la otra elección equivocada.
Resultado: La fiabilidad de una secuencia no se deduce del mejor paso aislado.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falla si la tool ejecuta bien pero fue mal elegida?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Cada decisión adicional merece una prueba.

ERRORES CONCEPTUALES FRECUENTES
Presentar 93 % como medición universal del modelo.

CONEXIÓN ANTERIOR
S3: primera tool con contrato.

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Responsabilidad única en el catálogo

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · De una tool a cuatro

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: MercaSur · De una tool a cuatro
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Reconocer que ampliar el catálogo añade decisiones que deben medirse.

CONCEPTO PRINCIPAL
De una tool a cuatro

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Cada decisión adicional merece una prueba.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El agente debe consultar stock y luego describir el producto. Pida una predicción.

Elegir: check_stock_by_store responde disponibilidad.

Continuar: get_product_details aporta características.

Comprobar: Una tool correcta no compensa la otra elección equivocada.

Resultado esperado: La fiabilidad de una secuencia no se deduce del mejor paso aislado. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Elegir; Continuar; Comprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El agente debe consultar stock y luego describir el producto.
Elegir: check_stock_by_store responde disponibilidad.
Continuar: get_product_details aporta características.
Comprobar: Una tool correcta no compensa la otra elección equivocada.
Resultado: La fiabilidad de una secuencia no se deduce del mejor paso aislado.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falla si la tool ejecuta bien pero fue mal elegida?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Cada decisión adicional merece una prueba.

ERRORES CONCEPTUALES FRECUENTES
Presentar 93 % como medición universal del modelo.

CONEXIÓN ANTERIOR
S3: primera tool con contrato.

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Responsabilidad única en el catálogo

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Responsabilidad única en el catálogo

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Responsabilidad única en el catálogo
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Diseñar fronteras claras entre las cuatro tools núcleo.

CONCEPTO PRINCIPAL
Responsabilidad única en el catálogo

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una tool, una responsabilidad reconocible.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Cómo detectarías una tool que hace demasiadas cosas?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Consulta específica: Cada nombre comunica la capacidad que ofrece.

Contrato acotado: Argumentos y errores pertenecen a esa responsabilidad.

Frontera explícita: La docstring distingue capacidades vecinas.

Cierre con la distinción: Una tool, una responsabilidad reconocible.

ELEMENTOS QUE CONVIENE EXPLICAR
Consulta específica; Contrato acotado; Frontera explícita. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Queda talla M?» no pregunta dónde está un pedido.
Identificar: Es una consulta de disponibilidad.
Seleccionar: Usar check_stock_by_store con los datos requeridos.
Excluir: track_order exige una compra ya identificada.
Resultado: Las capacidades se distinguen por la tarea, no solo por palabras compartidas.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Cómo detectarías una tool que hace demasiadas cosas?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una tool, una responsabilidad reconocible.

ERRORES CONCEPTUALES FRECUENTES
Crear una función genérica que resuelve todo y dificulta la selección.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: De una tool a cuatro

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Selección dinámica y confusiones

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Catálogo núcleo de retail

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Catálogo núcleo de retail
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Diseñar fronteras claras entre las cuatro tools núcleo.

CONCEPTO PRINCIPAL
Responsabilidad única en el catálogo

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una tool, una responsabilidad reconocible.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Pedidos y stock: track_order y check_stock_by_store.

Devolución: start_return_request inicia la solicitud prevista por el simulador.

Producto: get_product_details informa características.

Contraste la regla con este error: Crear una función genérica que resuelve todo y dificulta la selección. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Pedidos y stock; Devolución; Producto. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Queda talla M?» no pregunta dónde está un pedido.
Identificar: Es una consulta de disponibilidad.
Seleccionar: Usar check_stock_by_store con los datos requeridos.
Excluir: track_order exige una compra ya identificada.
Resultado: Las capacidades se distinguen por la tarea, no solo por palabras compartidas.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Cómo detectarías una tool que hace demasiadas cosas?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una tool, una responsabilidad reconocible.

ERRORES CONCEPTUALES FRECUENTES
Crear una función genérica que resuelve todo y dificulta la selección.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: De una tool a cuatro

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Selección dinámica y confusiones

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Responsabilidad única en el catálogo

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: MercaSur · Responsabilidad única en el catálogo
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Diseñar fronteras claras entre las cuatro tools núcleo.

CONCEPTO PRINCIPAL
Responsabilidad única en el catálogo

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Una tool, una responsabilidad reconocible.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Queda talla M?» no pregunta dónde está un pedido. Pida una predicción.

Identificar: Es una consulta de disponibilidad.

Seleccionar: Usar check_stock_by_store con los datos requeridos.

Excluir: track_order exige una compra ya identificada.

Resultado esperado: Las capacidades se distinguen por la tarea, no solo por palabras compartidas. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Identificar; Seleccionar; Excluir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Queda talla M?» no pregunta dónde está un pedido.
Identificar: Es una consulta de disponibilidad.
Seleccionar: Usar check_stock_by_store con los datos requeridos.
Excluir: track_order exige una compra ya identificada.
Resultado: Las capacidades se distinguen por la tarea, no solo por palabras compartidas.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Cómo detectarías una tool que hace demasiadas cosas?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Una tool, una responsabilidad reconocible.

ERRORES CONCEPTUALES FRECUENTES
Crear una función genérica que resuelve todo y dificulta la selección.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: De una tool a cuatro

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Selección dinámica y confusiones

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Selección dinámica y confusiones

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Selección dinámica y confusiones
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Analizar errores de selección antes de modificar el catálogo.

CONCEPTO PRINCIPAL
Selección dinámica y confusiones

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Corregir selección exige identificar qué capacidades se confunden.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Siempre es un error no llamar ninguna tool?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Consulta real: Incluye sinónimos, ambigüedades y datos incompletos.

Descripción de tools: Orienta qué capacidad debe usar el modelo.

Matriz de selección: Muestra tool esperada frente a tool llamada.

Cierre con la distinción: Corregir selección exige identificar qué capacidades se confunden.

ELEMENTOS QUE CONVIENE EXPLICAR
Consulta real; Descripción de tools; Matriz de selección. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. «¿Por qué me cobraron mantenimiento?» se envía por error a saldo.
Detectar: La esperada es explain_fee, no get_account_balance.
Diagnosticar: Revisar fronteras y ejemplos de ambas descripciones.
Repetir: Volver a medir los mismos casos tras el ajuste.
Resultado: La matriz localiza una confusión que el promedio oculta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Siempre es un error no llamar ninguna tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Corregir selección exige identificar qué capacidades se confunden.

ERRORES CONCEPTUALES FRECUENTES
Contar cualquier llamada como un acierto.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Responsabilidad única en el catálogo

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Few-shot para elegir herramientas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Leer la matriz para actuar

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Leer la matriz para actuar
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Analizar errores de selección antes de modificar el catálogo.

CONCEPTO PRINCIPAL
Selección dinámica y confusiones

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Corregir selección exige identificar qué capacidades se confunden.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Diagonal: Casos en que la selección coincide con lo esperado.

Fuera de diagonal: Pares de tools confundidas que requieren revisión.

Sin llamada: Puede ser correcto para OTRO o un error en una consulta de negocio.

Contraste la regla con este error: Contar cualquier llamada como un acierto. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Diagonal; Fuera de diagonal; Sin llamada. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. «¿Por qué me cobraron mantenimiento?» se envía por error a saldo.
Detectar: La esperada es explain_fee, no get_account_balance.
Diagnosticar: Revisar fronteras y ejemplos de ambas descripciones.
Repetir: Volver a medir los mismos casos tras el ajuste.
Resultado: La matriz localiza una confusión que el promedio oculta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Siempre es un error no llamar ninguna tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Corregir selección exige identificar qué capacidades se confunden.

ERRORES CONCEPTUALES FRECUENTES
Contar cualquier llamada como un acierto.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Responsabilidad única en el catálogo

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Few-shot para elegir herramientas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Selección dinámica y confusiones

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: Banco Inti · Selección dinámica y confusiones
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §2
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Analizar errores de selección antes de modificar el catálogo.

CONCEPTO PRINCIPAL
Selección dinámica y confusiones

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Corregir selección exige identificar qué capacidades se confunden.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Por qué me cobraron mantenimiento?» se envía por error a saldo. Pida una predicción.

Detectar: La esperada es explain_fee, no get_account_balance.

Diagnosticar: Revisar fronteras y ejemplos de ambas descripciones.

Repetir: Volver a medir los mismos casos tras el ajuste.

Resultado esperado: La matriz localiza una confusión que el promedio oculta. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Detectar; Diagnosticar; Repetir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. «¿Por qué me cobraron mantenimiento?» se envía por error a saldo.
Detectar: La esperada es explain_fee, no get_account_balance.
Diagnosticar: Revisar fronteras y ejemplos de ambas descripciones.
Repetir: Volver a medir los mismos casos tras el ajuste.
Resultado: La matriz localiza una confusión que el promedio oculta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Siempre es un error no llamar ninguna tool?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Corregir selección exige identificar qué capacidades se confunden.

ERRORES CONCEPTUALES FRECUENTES
Contar cualquier llamada como un acierto.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Responsabilidad única en el catálogo

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Few-shot para elegir herramientas

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. Few-shot para elegir herramientas

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: Few-shot para elegir herramientas
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §2.1 · regla A5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Usar contrastes que aclaren la frontera entre capacidades cercanas.

CONCEPTO PRINCIPAL
Few-shot para elegir herramientas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los ejemplos deben enseñar una distinción transferible.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué reformulación usarías para comprobar que no memorizó la frase?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Consulta A: Pide información de la cuenta.

Consulta B: Pregunta por movimientos o por una comisión.

Criterio: Seleccionar según la necesidad, no por mencionar dinero.

Cierre con la distinción: Los ejemplos deben enseñar una distinción transferible.

ELEMENTOS QUE CONVIENE EXPLICAR
Consulta A; Consulta B; Criterio. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. «¿Cuánto tengo?» frente a «¿Qué cargos hubo ayer?»
Saldo: get_account_balance responde disponibilidad en la cuenta.
Movimientos: list_transactions recupera la actividad.
Transferir: No añadir una operación de transferencia al catálogo.
Resultado: El catálogo y sus límites definen qué decisiones son posibles.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué reformulación usarías para comprobar que no memorizó la frase?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los ejemplos deben enseñar una distinción transferible.

ERRORES CONCEPTUALES FRECUENTES
Usar ejemplos idénticos a la prueba y presentarlo como generalización.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Selección dinámica y confusiones

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Cuatro tools núcleo y alcance

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Construir el par de ejemplos

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Construir el par de ejemplos
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §2.1 · regla A5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Usar contrastes que aclaren la frontera entre capacidades cercanas.

CONCEPTO PRINCIPAL
Few-shot para elegir herramientas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los ejemplos deben enseñar una distinción transferible.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Aislar: Mantener vocabulario parecido y cambiar la intención.

Etiquetar: Indicar la tool esperada y por qué corresponde.

Comprobar: Probar reformulaciones no incluidas en el prompt.

Contraste la regla con este error: Usar ejemplos idénticos a la prueba y presentarlo como generalización. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Aislar; Etiquetar; Comprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. «¿Cuánto tengo?» frente a «¿Qué cargos hubo ayer?»
Saldo: get_account_balance responde disponibilidad en la cuenta.
Movimientos: list_transactions recupera la actividad.
Transferir: No añadir una operación de transferencia al catálogo.
Resultado: El catálogo y sus límites definen qué decisiones son posibles.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué reformulación usarías para comprobar que no memorizó la frase?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los ejemplos deben enseñar una distinción transferible.

ERRORES CONCEPTUALES FRECUENTES
Usar ejemplos idénticos a la prueba y presentarlo como generalización.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Selección dinámica y confusiones

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Cuatro tools núcleo y alcance

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · Few-shot para elegir herramientas

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: Banco Inti · Few-shot para elegir herramientas
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §2.1 · regla A5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Usar contrastes que aclaren la frontera entre capacidades cercanas.

CONCEPTO PRINCIPAL
Few-shot para elegir herramientas

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los ejemplos deben enseñar una distinción transferible.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Cuánto tengo?» frente a «¿Qué cargos hubo ayer?» Pida una predicción.

Saldo: get_account_balance responde disponibilidad en la cuenta.

Movimientos: list_transactions recupera la actividad.

Transferir: No añadir una operación de transferencia al catálogo.

Resultado esperado: El catálogo y sus límites definen qué decisiones son posibles. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Saldo; Movimientos; Transferir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. «¿Cuánto tengo?» frente a «¿Qué cargos hubo ayer?»
Saldo: get_account_balance responde disponibilidad en la cuenta.
Movimientos: list_transactions recupera la actividad.
Transferir: No añadir una operación de transferencia al catálogo.
Resultado: El catálogo y sus límites definen qué decisiones son posibles.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué reformulación usarías para comprobar que no memorizó la frase?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los ejemplos deben enseñar una distinción transferible.

ERRORES CONCEPTUALES FRECUENTES
Usar ejemplos idénticos a la prueba y presentarlo como generalización.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Selección dinámica y confusiones

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Cuatro tools núcleo y alcance

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Cuatro tools núcleo y alcance

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Cuatro tools núcleo y alcance
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §3 · regla A1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comprender la reducción del catálogo como decisión pedagógica medible.

CONCEPTO PRINCIPAL
Cuatro tools núcleo y alcance

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un catálogo pequeño y claro facilita aprender a medir la selección.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué evidencia justificaría incorporar una quinta capacidad?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Núcleo: Cuatro capacidades obligatorias por industria.

Opcionales: Otras capacidades del simulador quedan como ampliación.

Comparación: Se puede medir cómo cambia la selección al ampliar opciones.

Cierre con la distinción: Un catálogo pequeño y claro facilita aprender a medir la selección.

ELEMENTOS QUE CONVIENE EXPLICAR
Núcleo; Opcionales; Comparación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El núcleo incluye cotización SOAT, póliza, cobertura y apertura de siniestro.
Definir: quote_soat y get_policy_by_plate cubren dos tareas distintas.
Completar: check_coverage y open_claim completan el núcleo.
Limitar: Abrir un siniestro no significa aprobar su pago.
Resultado: Cuatro es una decisión del curso; no un límite universal de los agentes.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia justificaría incorporar una quinta capacidad?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un catálogo pequeño y claro facilita aprender a medir la selección.

ERRORES CONCEPTUALES FRECUENTES
Convertir la regla didáctica de cuatro en una ley técnica.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Few-shot para elegir herramientas

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Idempotencia y límite de iteraciones

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Aplicar la restricción con criterio

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Aplicar la restricción con criterio
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §3 · regla A1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comprender la reducción del catálogo como decisión pedagógica medible.

CONCEPTO PRINCIPAL
Cuatro tools núcleo y alcance

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un catálogo pequeño y claro facilita aprender a medir la selección.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Relevancia: Incluir lo necesario para el caso principal.

Claridad: Evitar capacidades redundantes sin una frontera útil.

Evidencia: Ampliar solo cuando las nuevas capacidades aporten y se prueben.

Contraste la regla con este error: Convertir la regla didáctica de cuatro en una ley técnica. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Relevancia; Claridad; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El núcleo incluye cotización SOAT, póliza, cobertura y apertura de siniestro.
Definir: quote_soat y get_policy_by_plate cubren dos tareas distintas.
Completar: check_coverage y open_claim completan el núcleo.
Limitar: Abrir un siniestro no significa aprobar su pago.
Resultado: Cuatro es una decisión del curso; no un límite universal de los agentes.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia justificaría incorporar una quinta capacidad?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un catálogo pequeño y claro facilita aprender a medir la selección.

ERRORES CONCEPTUALES FRECUENTES
Convertir la regla didáctica de cuatro en una ley técnica.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Few-shot para elegir herramientas

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Idempotencia y límite de iteraciones

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Cuatro tools núcleo y alcance

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: Andina Seguros · Cuatro tools núcleo y alcance
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §3 · regla A1
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comprender la reducción del catálogo como decisión pedagógica medible.

CONCEPTO PRINCIPAL
Cuatro tools núcleo y alcance

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un catálogo pequeño y claro facilita aprender a medir la selección.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El núcleo incluye cotización SOAT, póliza, cobertura y apertura de siniestro. Pida una predicción.

Definir: quote_soat y get_policy_by_plate cubren dos tareas distintas.

Completar: check_coverage y open_claim completan el núcleo.

Limitar: Abrir un siniestro no significa aprobar su pago.

Resultado esperado: Cuatro es una decisión del curso; no un límite universal de los agentes. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Definir; Completar; Limitar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El núcleo incluye cotización SOAT, póliza, cobertura y apertura de siniestro.
Definir: quote_soat y get_policy_by_plate cubren dos tareas distintas.
Completar: check_coverage y open_claim completan el núcleo.
Limitar: Abrir un siniestro no significa aprobar su pago.
Resultado: Cuatro es una decisión del curso; no un límite universal de los agentes.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué evidencia justificaría incorporar una quinta capacidad?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un catálogo pequeño y claro facilita aprender a medir la selección.

ERRORES CONCEPTUALES FRECUENTES
Convertir la regla didáctica de cuatro en una ley técnica.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Few-shot para elegir herramientas

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Idempotencia y límite de iteraciones

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Idempotencia y límite de iteraciones

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Idempotencia y límite de iteraciones
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §4 · regla A4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Evitar efectos duplicados y ejecuciones sin una salida controlada.

CONCEPTO PRINCIPAL
Idempotencia y límite de iteraciones

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los reintentos deben considerar el efecto de la operación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué podría ocurrir al reintentar una creación tras un timeout?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Repetición: Un usuario o un fallo puede provocar llamadas repetidas.

Escritura: Repetir una creación puede duplicar el efecto.

Control: Identificar operaciones, limitar iteraciones y definir derivación.

Cierre con la distinción: Los reintentos deben considerar el efecto de la operación.

ELEMENTOS QUE CONVIENE EXPLICAR
Repetición; Escritura; Control. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El cliente repite la solicitud de crear un reclamo.
Reconocer: Puede tratarse de la misma operación de negocio.
Proteger: Usar el mecanismo de idempotencia del contrato cuando corresponda.
Comprobar: No presentar dos tickets como si fueran una sola gestión.
Resultado: Limitar vueltas no vuelve idempotente una escritura.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué podría ocurrir al reintentar una creación tras un timeout?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los reintentos deben considerar el efecto de la operación.

ERRORES CONCEPTUALES FRECUENTES
Suponer que toda lectura o escritura repetida es inocua.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Cuatro tools núcleo y alcance

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: MCP: exponer y descubrir tools

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Dos protecciones distintas

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Dos protecciones distintas
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §4 · regla A4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Evitar efectos duplicados y ejecuciones sin una salida controlada.

CONCEPTO PRINCIPAL
Idempotencia y límite de iteraciones

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los reintentos deben considerar el efecto de la operación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Idempotencia: La repetición del mismo pedido no debe crear efectos nuevos.

Tope: El bucle se detiene al alcanzar el máximo configurado.

Respuesta: Informar qué ocurrió y cuándo se necesita ayuda humana.

Contraste la regla con este error: Suponer que toda lectura o escritura repetida es inocua. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Idempotencia; Tope; Respuesta. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El cliente repite la solicitud de crear un reclamo.
Reconocer: Puede tratarse de la misma operación de negocio.
Proteger: Usar el mecanismo de idempotencia del contrato cuando corresponda.
Comprobar: No presentar dos tickets como si fueran una sola gestión.
Resultado: Limitar vueltas no vuelve idempotente una escritura.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué podría ocurrir al reintentar una creación tras un timeout?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los reintentos deben considerar el efecto de la operación.

ERRORES CONCEPTUALES FRECUENTES
Suponer que toda lectura o escritura repetida es inocua.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Cuatro tools núcleo y alcance

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: MCP: exponer y descubrir tools

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Idempotencia y límite de iteraciones

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: AndesMóvil · Idempotencia y límite de iteraciones
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §4 · regla A4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Evitar efectos duplicados y ejecuciones sin una salida controlada.

CONCEPTO PRINCIPAL
Idempotencia y límite de iteraciones

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los reintentos deben considerar el efecto de la operación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El cliente repite la solicitud de crear un reclamo. Pida una predicción.

Reconocer: Puede tratarse de la misma operación de negocio.

Proteger: Usar el mecanismo de idempotencia del contrato cuando corresponda.

Comprobar: No presentar dos tickets como si fueran una sola gestión.

Resultado esperado: Limitar vueltas no vuelve idempotente una escritura. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Reconocer; Proteger; Comprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El cliente repite la solicitud de crear un reclamo.
Reconocer: Puede tratarse de la misma operación de negocio.
Proteger: Usar el mecanismo de idempotencia del contrato cuando corresponda.
Comprobar: No presentar dos tickets como si fueran una sola gestión.
Resultado: Limitar vueltas no vuelve idempotente una escritura.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué podría ocurrir al reintentar una creación tras un timeout?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los reintentos deben considerar el efecto de la operación.

ERRORES CONCEPTUALES FRECUENTES
Suponer que toda lectura o escritura repetida es inocua.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Cuatro tools núcleo y alcance

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: MCP: exponer y descubrir tools

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. MCP: exponer y descubrir tools

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: MCP: exponer y descubrir tools
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: Pre-work MCP y conceptos-previos
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar el protocolo de herramientas, su transporte y el sistema de negocio.

CONCEPTO PRINCIPAL
MCP: exponer y descubrir tools

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
MCP estandariza una interfaz; no decide la política del catálogo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Dónde sigue viviendo la lógica de consulta al simulador?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Cliente MCP: Descubre e incorpora herramientas publicadas.

Servidor MCP: Expone contratos de capacidades al cliente.

Sistema externo: La implementación puede consultar el simulador por HTTP.

Cierre con la distinción: MCP estandariza una interfaz; no decide la política del catálogo.

ELEMENTOS QUE CONVIENE EXPLICAR
Cliente MCP; Servidor MCP; Sistema externo. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El pre-work lista las seis tools disponibles en el servidor.
Conectar: Inicializar el cliente según el ejercicio MCP.
Descubrir: Revisar nombres, descripciones y esquemas recibidos.
Seleccionar: El catálogo núcleo del laboratorio sigue siendo de cuatro.
Resultado: Descubrir seis capacidades no obliga a habilitarlas todas en el agente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde sigue viviendo la lógica de consulta al simulador?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: MCP estandariza una interfaz; no decide la política del catálogo.

ERRORES CONCEPTUALES FRECUENTES
Confundir MCP con una base de datos o con el transporte HTTP del negocio.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Idempotencia y límite de iteraciones

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Laboratorio L4: integrar y medir

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. Leer las fronteras de integración

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: Leer las fronteras de integración
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: Pre-work MCP y conceptos-previos
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar el protocolo de herramientas, su transporte y el sistema de negocio.

CONCEPTO PRINCIPAL
MCP: exponer y descubrir tools

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
MCP estandariza una interfaz; no decide la política del catálogo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Descubrimiento: El cliente obtiene el catálogo del servidor.

Transporte: stdio comunica procesos; HTTP es otra frontera del sistema.

Ejecución: La tool sigue teniendo argumentos, errores y límites de negocio.

Contraste la regla con este error: Confundir MCP con una base de datos o con el transporte HTTP del negocio. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Descubrimiento; Transporte; Ejecución. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El pre-work lista las seis tools disponibles en el servidor.
Conectar: Inicializar el cliente según el ejercicio MCP.
Descubrir: Revisar nombres, descripciones y esquemas recibidos.
Seleccionar: El catálogo núcleo del laboratorio sigue siendo de cuatro.
Resultado: Descubrir seis capacidades no obliga a habilitarlas todas en el agente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde sigue viviendo la lógica de consulta al simulador?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: MCP estandariza una interfaz; no decide la política del catálogo.

ERRORES CONCEPTUALES FRECUENTES
Confundir MCP con una base de datos o con el transporte HTTP del negocio.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Idempotencia y límite de iteraciones

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Laboratorio L4: integrar y medir

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · MCP: exponer y descubrir tools

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: MercaSur · MCP: exponer y descubrir tools
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: Pre-work MCP y conceptos-previos
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar el protocolo de herramientas, su transporte y el sistema de negocio.

CONCEPTO PRINCIPAL
MCP: exponer y descubrir tools

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
MCP estandariza una interfaz; no decide la política del catálogo.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El pre-work lista las seis tools disponibles en el servidor. Pida una predicción.

Conectar: Inicializar el cliente según el ejercicio MCP.

Descubrir: Revisar nombres, descripciones y esquemas recibidos.

Seleccionar: El catálogo núcleo del laboratorio sigue siendo de cuatro.

Resultado esperado: Descubrir seis capacidades no obliga a habilitarlas todas en el agente. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Conectar; Descubrir; Seleccionar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El pre-work lista las seis tools disponibles en el servidor.
Conectar: Inicializar el cliente según el ejercicio MCP.
Descubrir: Revisar nombres, descripciones y esquemas recibidos.
Seleccionar: El catálogo núcleo del laboratorio sigue siendo de cuatro.
Resultado: Descubrir seis capacidades no obliga a habilitarlas todas en el agente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Dónde sigue viviendo la lógica de consulta al simulador?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: MCP estandariza una interfaz; no decide la política del catálogo.

ERRORES CONCEPTUALES FRECUENTES
Confundir MCP con una base de datos o con el transporte HTTP del negocio.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: Idempotencia y límite de iteraciones

CONEXIÓN POSTERIOR
S5: retriever y memoria · Sigue: Laboratorio L4: integrar y medir

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 22. Laboratorio L4: integrar y medir

DIAPOSITIVA 22 · CAPÍTULO 8 · CONCEPTO
Título: Laboratorio L4: integrar y medir
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §5, proyecto-final y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ensamblar el catálogo y demostrar selección y manejo de errores.

CONCEPTO PRINCIPAL
Laboratorio L4: integrar y medir

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué captura probaría la selección, además de la respuesta final?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Construir: Completar las cuatro tools núcleo con contratos coherentes.

Integrar: Ensamblar el agente y limitar su ejecución.

Medir: Evaluar selección y documentar el avance del proyecto.

Cierre con la distinción: Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

ELEMENTOS QUE CONVIENE EXPLICAR
Construir; Integrar; Medir. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una consulta de cobertura termina abriendo un siniestro por error.
Registrar: La llamada no coincide con la intención.
Corregir: Revisar la frontera entre consultar y registrar.
Reprobar: La misma consulta debe usar check_coverage.
Resultado: El avance es verificable cuando la selección se puede inspeccionar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué captura probaría la selección, además de la respuesta final?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

ERRORES CONCEPTUALES FRECUENTES
Mostrar solo texto final sin evidencia de la herramienta usada.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: MCP: exponer y descubrir tools

CONEXIÓN POSTERIOR
S5: retriever y memoria.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 23. Evidencia que debe conservarse

DIAPOSITIVA 23 · CAPÍTULO 8 · DESARROLLO
Título: Evidencia que debe conservarse
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §5, proyecto-final y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ensamblar el catálogo y demostrar selección y manejo de errores.

CONCEPTO PRINCIPAL
Laboratorio L4: integrar y medir

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Consulta: Entrada exacta que permite repetir el caso.

Llamada: Tool seleccionada y argumentos relevantes.

Resultado: Respuesta, error y comparación con lo esperado.

Contraste la regla con este error: Mostrar solo texto final sin evidencia de la herramienta usada. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Consulta; Llamada; Resultado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una consulta de cobertura termina abriendo un siniestro por error.
Registrar: La llamada no coincide con la intención.
Corregir: Revisar la frontera entre consultar y registrar.
Reprobar: La misma consulta debe usar check_coverage.
Resultado: El avance es verificable cuando la selección se puede inspeccionar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué captura probaría la selección, además de la respuesta final?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

ERRORES CONCEPTUALES FRECUENTES
Mostrar solo texto final sin evidencia de la herramienta usada.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: MCP: exponer y descubrir tools

CONEXIÓN POSTERIOR
S5: retriever y memoria.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 24. Ejemplo · Laboratorio L4: integrar y medir

DIAPOSITIVA 24 · CAPÍTULO 8 · EJEMPLO
Título: Andina Seguros · Laboratorio L4: integrar y medir
Sesión: Catálogo de tools e integración
Archivo: 04-tools-multiples-editable-v2.pptx
Sección que soporta: §5, proyecto-final y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-04-tools-multiples; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Ensamblar el catálogo y demostrar selección y manejo de errores.

CONCEPTO PRINCIPAL
Laboratorio L4: integrar y medir

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una consulta de cobertura termina abriendo un siniestro por error. Pida una predicción.

Registrar: La llamada no coincide con la intención.

Corregir: Revisar la frontera entre consultar y registrar.

Reprobar: La misma consulta debe usar check_coverage.

Resultado esperado: El avance es verificable cuando la selección se puede inspeccionar. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Registrar; Corregir; Reprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una consulta de cobertura termina abriendo un siniestro por error.
Registrar: La llamada no coincide con la intención.
Corregir: Revisar la frontera entre consultar y registrar.
Reprobar: La misma consulta debe usar check_coverage.
Resultado: El avance es verificable cuando la selección se puede inspeccionar.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué captura probaría la selección, además de la respuesta final?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un catálogo funciona cuando el agente elige bien y maneja sus fallos.

ERRORES CONCEPTUALES FRECUENTES
Mostrar solo texto final sin evidencia de la herramienta usada.

CONEXIÓN ANTERIOR
S3: primera tool con contrato · Capítulo previo: MCP: exponer y descubrir tools

CONEXIÓN POSTERIOR
S5: retriever y memoria.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

