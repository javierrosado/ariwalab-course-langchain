# Memoria contextual y RAG con Qdrant — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. No recuerda y no sabe

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: No recuerda y no sabe
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar contexto conversacional y conocimiento documental del dominio.

CONCEPTO PRINCIPAL
No recuerda y no sabe

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Memoria, RAG y tools resuelven necesidades diferentes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué mecanismo falta si recuerda el producto pero inventa el plazo?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Memoria: Recupera mensajes de esa conversación.

RAG: Recupera fragmentos de un corpus externo.

Tools de negocio: Obtienen estados y datos del simulador.

Cierre con la distinción: Memoria, RAG y tools resuelven necesidades diferentes.

ELEMENTOS QUE CONVIENE EXPLICAR
Memoria; RAG; Tools de negocio. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Puedo devolverlo?» llega después de identificar un producto dañado.
Memoria: Conservar a qué producto se refiere «lo».
RAG: Recuperar la política aplicable.
Respuesta: Explicar la regla y citar el documento.
Resultado: Añadir historial no reemplaza una política ausente del contexto.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué mecanismo falta si recuerda el producto pero inventa el plazo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Memoria, RAG y tools resuelven necesidades diferentes.

ERRORES CONCEPTUALES FRECUENTES
Resolver falta de conocimiento con más mensajes de conversación.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools.

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Estado por thread_id

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Elegir el mecanismo adecuado

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Elegir el mecanismo adecuado
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar contexto conversacional y conocimiento documental del dominio.

CONCEPTO PRINCIPAL
No recuerda y no sabe

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Memoria, RAG y tools resuelven necesidades diferentes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Referencia previa: «¿Y el mes pasado?» necesita historial pertinente.

Política: Una regla de devolución necesita su documento fuente.

Estado actual: Un pedido concreto requiere la tool de pedidos.

Contraste la regla con este error: Resolver falta de conocimiento con más mensajes de conversación. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Referencia previa; Política; Estado actual. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Puedo devolverlo?» llega después de identificar un producto dañado.
Memoria: Conservar a qué producto se refiere «lo».
RAG: Recuperar la política aplicable.
Respuesta: Explicar la regla y citar el documento.
Resultado: Añadir historial no reemplaza una política ausente del contexto.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué mecanismo falta si recuerda el producto pero inventa el plazo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Memoria, RAG y tools resuelven necesidades diferentes.

ERRORES CONCEPTUALES FRECUENTES
Resolver falta de conocimiento con más mensajes de conversación.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools.

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Estado por thread_id

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · No recuerda y no sabe

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: MercaSur · No recuerda y no sabe
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar contexto conversacional y conocimiento documental del dominio.

CONCEPTO PRINCIPAL
No recuerda y no sabe

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Memoria, RAG y tools resuelven necesidades diferentes.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Puedo devolverlo?» llega después de identificar un producto dañado. Pida una predicción.

Memoria: Conservar a qué producto se refiere «lo».

RAG: Recuperar la política aplicable.

Respuesta: Explicar la regla y citar el documento.

Resultado esperado: Añadir historial no reemplaza una política ausente del contexto. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Memoria; RAG; Respuesta. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. «¿Puedo devolverlo?» llega después de identificar un producto dañado.
Memoria: Conservar a qué producto se refiere «lo».
RAG: Recuperar la política aplicable.
Respuesta: Explicar la regla y citar el documento.
Resultado: Añadir historial no reemplaza una política ausente del contexto.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué mecanismo falta si recuerda el producto pero inventa el plazo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Memoria, RAG y tools resuelven necesidades diferentes.

ERRORES CONCEPTUALES FRECUENTES
Resolver falta de conocimiento con más mensajes de conversación.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools.

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Estado por thread_id

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Estado por thread_id

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Estado por thread_id
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §1 y solucion/*/memory.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Aislar conversaciones y entender los límites de la memoria del checkpoint.

CONCEPTO PRINCIPAL
Estado por thread_id

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La memoria de L5 vive en el proceso y no es persistencia duradera.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué ocurre con el historial cuando se reinicia el Space?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Identificador: thread_id selecciona una conversación.

Historial: Un diccionario del proceso conserva la lista de mensajes.

Nueva llamada: La aplicación reenvía ese historial al modelo.

Cierre con la distinción: La memoria de L5 vive en el proceso y no es persistencia duradera.

ELEMENTOS QUE CONVIENE EXPLICAR
Identificador; Historial; Nueva llamada. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Dos clientes hacen preguntas consecutivas sobre sus cuentas.
Separar: Asignar una conversación diferente a cada cliente.
Reutilizar: Cada cliente continúa con su propio thread_id.
Verificar: El contexto de uno no aparece en la respuesta del otro.
Resultado: El identificador organiza estado; no autentica por sí mismo al usuario.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué ocurre con el historial cuando se reinicia el Space?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La memoria de L5 vive en el proceso y no es persistencia duradera.

ERRORES CONCEPTUALES FRECUENTES
Dibujar un checkpointer duradero que el código no implementa.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: No recuerda y no sabe

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Embeddings del dominio

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Qué garantiza esta implementación

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Qué garantiza esta implementación
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §1 y solucion/*/memory.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Aislar conversaciones y entender los límites de la memoria del checkpoint.

CONCEPTO PRINCIPAL
Estado por thread_id

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La memoria de L5 vive en el proceso y no es persistencia duradera.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Aislamiento lógico: Usar identificadores distintos evita compartir la misma lista.

Continuidad: Reutilizar el identificador conserva el contexto en ese proceso.

Límite: Reiniciar el proceso pierde este almacenamiento en memoria.

Contraste la regla con este error: Dibujar un checkpointer duradero que el código no implementa. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Aislamiento lógico; Continuidad; Límite. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Dos clientes hacen preguntas consecutivas sobre sus cuentas.
Separar: Asignar una conversación diferente a cada cliente.
Reutilizar: Cada cliente continúa con su propio thread_id.
Verificar: El contexto de uno no aparece en la respuesta del otro.
Resultado: El identificador organiza estado; no autentica por sí mismo al usuario.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué ocurre con el historial cuando se reinicia el Space?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La memoria de L5 vive en el proceso y no es persistencia duradera.

ERRORES CONCEPTUALES FRECUENTES
Dibujar un checkpointer duradero que el código no implementa.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: No recuerda y no sabe

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Embeddings del dominio

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Estado por thread_id

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: Banco Inti · Estado por thread_id
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §1 y solucion/*/memory.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Aislar conversaciones y entender los límites de la memoria del checkpoint.

CONCEPTO PRINCIPAL
Estado por thread_id

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La memoria de L5 vive en el proceso y no es persistencia duradera.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Dos clientes hacen preguntas consecutivas sobre sus cuentas. Pida una predicción.

Separar: Asignar una conversación diferente a cada cliente.

Reutilizar: Cada cliente continúa con su propio thread_id.

Verificar: El contexto de uno no aparece en la respuesta del otro.

Resultado esperado: El identificador organiza estado; no autentica por sí mismo al usuario. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Separar; Reutilizar; Verificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Dos clientes hacen preguntas consecutivas sobre sus cuentas.
Separar: Asignar una conversación diferente a cada cliente.
Reutilizar: Cada cliente continúa con su propio thread_id.
Verificar: El contexto de uno no aparece en la respuesta del otro.
Resultado: El identificador organiza estado; no autentica por sí mismo al usuario.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué ocurre con el historial cuando se reinicia el Space?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La memoria de L5 vive en el proceso y no es persistencia duradera.

ERRORES CONCEPTUALES FRECUENTES
Dibujar un checkpointer duradero que el código no implementa.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: No recuerda y no sabe

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Embeddings del dominio

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Embeddings del dominio

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Embeddings del dominio
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §2 y comun/provider.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Representar consulta y documentos en un espacio compatible para recuperar candidatos.

CONCEPTO PRINCIPAL
Embeddings del dominio

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La representación ayuda con sinónimos sin convertir similitud en verdad.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué falla si cambias el modelo de consulta sin reindexar?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Corpus: Documentos del track divididos en fragmentos.

Representación: El mismo modelo de embeddings representa corpus y consultas.

Comparación: La similitud ordena candidatos pertinentes.

Cierre con la distinción: La representación ayuda con sinónimos sin convertir similitud en verdad.

ELEMENTOS QUE CONVIENE EXPLICAR
Corpus; Representación; Comparación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. «¿Cuántos gigas incluye el plan?» usa vocabulario distinto al tarifario.
Representar: Convertir pregunta y fragmentos en vectores.
Recuperar: Encontrar la entrada semánticamente relacionada.
Contrastar: Comprobar plan, vigencia y cifra antes de responder.
Resultado: La similitud encuentra candidatos; el texto recuperado sostiene la afirmación.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falla si cambias el modelo de consulta sin reindexar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La representación ayuda con sinónimos sin convertir similitud en verdad.

ERRORES CONCEPTUALES FRECUENTES
Comparar vectores de espacios incompatibles.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Estado por thread_id

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Chunking y contexto de la cláusula

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Tres comprobaciones de compatibilidad

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Tres comprobaciones de compatibilidad
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §2 y comun/provider.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Representar consulta y documentos en un espacio compatible para recuperar candidatos.

CONCEPTO PRINCIPAL
Embeddings del dominio

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La representación ayuda con sinónimos sin convertir similitud en verdad.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Modelo: Mantener la misma configuración en ingesta y consulta.

Dimensión: La colección debe aceptar la dimensión del vector.

Dominio: Revisar que los candidatos pertenezcan al corpus esperado.

Contraste la regla con este error: Comparar vectores de espacios incompatibles. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Modelo; Dimensión; Dominio. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. «¿Cuántos gigas incluye el plan?» usa vocabulario distinto al tarifario.
Representar: Convertir pregunta y fragmentos en vectores.
Recuperar: Encontrar la entrada semánticamente relacionada.
Contrastar: Comprobar plan, vigencia y cifra antes de responder.
Resultado: La similitud encuentra candidatos; el texto recuperado sostiene la afirmación.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falla si cambias el modelo de consulta sin reindexar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La representación ayuda con sinónimos sin convertir similitud en verdad.

ERRORES CONCEPTUALES FRECUENTES
Comparar vectores de espacios incompatibles.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Estado por thread_id

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Chunking y contexto de la cláusula

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Embeddings del dominio

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: AndesMóvil · Embeddings del dominio
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §2 y comun/provider.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Representar consulta y documentos en un espacio compatible para recuperar candidatos.

CONCEPTO PRINCIPAL
Embeddings del dominio

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La representación ayuda con sinónimos sin convertir similitud en verdad.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: «¿Cuántos gigas incluye el plan?» usa vocabulario distinto al tarifario. Pida una predicción.

Representar: Convertir pregunta y fragmentos en vectores.

Recuperar: Encontrar la entrada semánticamente relacionada.

Contrastar: Comprobar plan, vigencia y cifra antes de responder.

Resultado esperado: La similitud encuentra candidatos; el texto recuperado sostiene la afirmación. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Representar; Recuperar; Contrastar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. «¿Cuántos gigas incluye el plan?» usa vocabulario distinto al tarifario.
Representar: Convertir pregunta y fragmentos en vectores.
Recuperar: Encontrar la entrada semánticamente relacionada.
Contrastar: Comprobar plan, vigencia y cifra antes de responder.
Resultado: La similitud encuentra candidatos; el texto recuperado sostiene la afirmación.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué falla si cambias el modelo de consulta sin reindexar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La representación ayuda con sinónimos sin convertir similitud en verdad.

ERRORES CONCEPTUALES FRECUENTES
Comparar vectores de espacios incompatibles.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Estado por thread_id

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Chunking y contexto de la cláusula

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. Chunking y contexto de la cláusula

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: Chunking y contexto de la cláusula
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Defender el tamaño de fragmento por equilibrio entre información y ruido.

CONCEPTO PRINCIPAL
Chunking y contexto de la cláusula

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El tamaño se justifica por el documento y se valida con preguntas reales.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué error de respuesta causaría recuperar solo la primera mitad?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Fragmento pequeño: Puede aislar con precisión, pero separar una condición de su excepción.

Fragmento grande: Puede conservar más contexto y añadir información irrelevante.

Overlap: Repite contenido cercano para reducir cortes problemáticos.

Cierre con la distinción: El tamaño se justifica por el documento y se valida con preguntas reales.

ELEMENTOS QUE CONVIENE EXPLICAR
Fragmento pequeño; Fragmento grande; Overlap. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una cláusula describe cobertura y a continuación una exclusión.
Cortar: Un fragmento demasiado pequeño separa la excepción.
Recuperar: El modelo solo recibe la mitad favorable.
Revisar: Verificar cortes y preservar el sentido completo de la condición.
Resultado: Un chunk grande tampoco garantiza que jamás parta una idea.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué error de respuesta causaría recuperar solo la primera mitad?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El tamaño se justifica por el documento y se valida con preguntas reales.

ERRORES CONCEPTUALES FRECUENTES
Llamar tokens a unidades del splitter sin comprobar su configuración.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Embeddings del dominio

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Colección, punto y payload

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Parámetros fijados por el curso

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Parámetros fijados por el curso
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Defender el tamaño de fragmento por equilibrio entre información y ruido.

CONCEPTO PRINCIPAL
Chunking y contexto de la cláusula

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El tamaño se justifica por el documento y se valida con preguntas reales.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Telco y banca: chunk_size 400; overlap 60.

Retail: chunk_size 350; overlap 50.

Seguros: chunk_size 600; overlap 100 para conservar contexto de cláusulas.

Contraste la regla con este error: Llamar tokens a unidades del splitter sin comprobar su configuración. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Telco y banca; Retail; Seguros. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una cláusula describe cobertura y a continuación una exclusión.
Cortar: Un fragmento demasiado pequeño separa la excepción.
Recuperar: El modelo solo recibe la mitad favorable.
Revisar: Verificar cortes y preservar el sentido completo de la condición.
Resultado: Un chunk grande tampoco garantiza que jamás parta una idea.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué error de respuesta causaría recuperar solo la primera mitad?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El tamaño se justifica por el documento y se valida con preguntas reales.

ERRORES CONCEPTUALES FRECUENTES
Llamar tokens a unidades del splitter sin comprobar su configuración.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Embeddings del dominio

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Colección, punto y payload

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · Chunking y contexto de la cláusula

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: Andina Seguros · Chunking y contexto de la cláusula
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Defender el tamaño de fragmento por equilibrio entre información y ruido.

CONCEPTO PRINCIPAL
Chunking y contexto de la cláusula

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El tamaño se justifica por el documento y se valida con preguntas reales.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una cláusula describe cobertura y a continuación una exclusión. Pida una predicción.

Cortar: Un fragmento demasiado pequeño separa la excepción.

Recuperar: El modelo solo recibe la mitad favorable.

Revisar: Verificar cortes y preservar el sentido completo de la condición.

Resultado esperado: Un chunk grande tampoco garantiza que jamás parta una idea. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Cortar; Recuperar; Revisar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. Una cláusula describe cobertura y a continuación una exclusión.
Cortar: Un fragmento demasiado pequeño separa la excepción.
Recuperar: El modelo solo recibe la mitad favorable.
Revisar: Verificar cortes y preservar el sentido completo de la condición.
Resultado: Un chunk grande tampoco garantiza que jamás parta una idea.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué error de respuesta causaría recuperar solo la primera mitad?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El tamaño se justifica por el documento y se valida con preguntas reales.

ERRORES CONCEPTUALES FRECUENTES
Llamar tokens a unidades del splitter sin comprobar su configuración.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Embeddings del dominio

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Colección, punto y payload

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Colección, punto y payload

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Colección, punto y payload
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Vincular búsqueda vectorial y trazabilidad del texto recuperado.

CONCEPTO PRINCIPAL
Colección, punto y payload

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El payload conecta el vector con una fuente que el docente puede revisar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué información perderías guardando solo vectores?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Colección: Agrupa vectores con una configuración compatible.

Punto: Contiene un vector y su payload.

Payload: Conserva texto, fuente y metadatos útiles para filtrar y citar.

Cierre con la distinción: El payload conecta el vector con una fuente que el docente puede revisar.

ELEMENTOS QUE CONVIENE EXPLICAR
Colección; Punto; Payload. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Dos versiones de una política contienen plazos distintos.
Indexar: Guardar texto y procedencia como metadatos.
Seleccionar: Recuperar la versión aplicable al caso.
Citar: Identificar el documento que respalda el plazo.
Resultado: Sin procedencia, un fragmento correcto puede quedar sin una cita verificable.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué información perderías guardando solo vectores?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El payload conecta el vector con una fuente que el docente puede revisar.

ERRORES CONCEPTUALES FRECUENTES
Confundir el vector con el texto que el modelo debe leer.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Chunking y contexto de la cláusula

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: RAG tradicional y RAG agéntico

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Recuperar con procedencia

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Recuperar con procedencia
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Vincular búsqueda vectorial y trazabilidad del texto recuperado.

CONCEPTO PRINCIPAL
Colección, punto y payload

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El payload conecta el vector con una fuente que el docente puede revisar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Texto: El resultado debe incluir el fragmento utilizable.

Fuente: Conservar el documento de origen junto al fragmento.

Filtro: Restringir por metadatos cuando la consulta exige un ámbito.

Contraste la regla con este error: Confundir el vector con el texto que el modelo debe leer. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Texto; Fuente; Filtro. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Dos versiones de una política contienen plazos distintos.
Indexar: Guardar texto y procedencia como metadatos.
Seleccionar: Recuperar la versión aplicable al caso.
Citar: Identificar el documento que respalda el plazo.
Resultado: Sin procedencia, un fragmento correcto puede quedar sin una cita verificable.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué información perderías guardando solo vectores?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El payload conecta el vector con una fuente que el docente puede revisar.

ERRORES CONCEPTUALES FRECUENTES
Confundir el vector con el texto que el modelo debe leer.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Chunking y contexto de la cláusula

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: RAG tradicional y RAG agéntico

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Colección, punto y payload

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: MercaSur · Colección, punto y payload
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Vincular búsqueda vectorial y trazabilidad del texto recuperado.

CONCEPTO PRINCIPAL
Colección, punto y payload

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El payload conecta el vector con una fuente que el docente puede revisar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Dos versiones de una política contienen plazos distintos. Pida una predicción.

Indexar: Guardar texto y procedencia como metadatos.

Seleccionar: Recuperar la versión aplicable al caso.

Citar: Identificar el documento que respalda el plazo.

Resultado esperado: Sin procedencia, un fragmento correcto puede quedar sin una cita verificable. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Indexar; Seleccionar; Citar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Dos versiones de una política contienen plazos distintos.
Indexar: Guardar texto y procedencia como metadatos.
Seleccionar: Recuperar la versión aplicable al caso.
Citar: Identificar el documento que respalda el plazo.
Resultado: Sin procedencia, un fragmento correcto puede quedar sin una cita verificable.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué información perderías guardando solo vectores?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El payload conecta el vector con una fuente que el docente puede revisar.

ERRORES CONCEPTUALES FRECUENTES
Confundir el vector con el texto que el modelo debe leer.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Chunking y contexto de la cláusula

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: RAG tradicional y RAG agéntico

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. RAG tradicional y RAG agéntico

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: RAG tradicional y RAG agéntico
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar una recuperación fijada en el flujo con una elegida como herramienta.

CONCEPTO PRINCIPAL
RAG tradicional y RAG agéntico

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
No toda consulta necesita RAG, pero una política sí necesita su fuente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué riesgo nuevo aparece al permitir que el agente elija buscar?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Tradicional: El flujo incluye la búsqueda antes de generar.

Agéntico: El retriever es una tool que el agente puede seleccionar.

Compensación: Evitar búsquedas innecesarias añade riesgo de omitir una necesaria.

Cierre con la distinción: No toda consulta necesita RAG, pero una política sí necesita su fuente.

ELEMENTOS QUE CONVIENE EXPLICAR
Tradicional; Agéntico; Compensación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Compara «Hola» con «¿Cuál es la comisión de mantenimiento?».
Saludo: Responder sin cargar fragmentos irrelevantes.
Comisión: Seleccionar retrieve_knowledge_base.
Resultado: Explicar lo que respalda el texto recuperado.
Resultado: El patrón agéntico aporta selección; esa selección también debe comprobarse.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué riesgo nuevo aparece al permitir que el agente elija buscar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: No toda consulta necesita RAG, pero una política sí necesita su fuente.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que la latencia del RAG tradicional es siempre constante.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Colección, punto y payload

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Recuperar y citar: salvaguarda A6

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Decidir cuándo recuperar

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Decidir cuándo recuperar
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar una recuperación fijada en el flujo con una elegida como herramienta.

CONCEPTO PRINCIPAL
RAG tradicional y RAG agéntico

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
No toda consulta necesita RAG, pero una política sí necesita su fuente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Saludo: No requiere consultar el corpus del negocio.

Dato operativo: Usar la tool de negocio que ya resuelve la consulta.

Política o tarifa: Recuperar la fuente correspondiente y citarla.

Contraste la regla con este error: Afirmar que la latencia del RAG tradicional es siempre constante. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Saludo; Dato operativo; Política o tarifa. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Compara «Hola» con «¿Cuál es la comisión de mantenimiento?».
Saludo: Responder sin cargar fragmentos irrelevantes.
Comisión: Seleccionar retrieve_knowledge_base.
Resultado: Explicar lo que respalda el texto recuperado.
Resultado: El patrón agéntico aporta selección; esa selección también debe comprobarse.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué riesgo nuevo aparece al permitir que el agente elija buscar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: No toda consulta necesita RAG, pero una política sí necesita su fuente.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que la latencia del RAG tradicional es siempre constante.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Colección, punto y payload

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Recuperar y citar: salvaguarda A6

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · RAG tradicional y RAG agéntico

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: Banco Inti · RAG tradicional y RAG agéntico
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Comparar una recuperación fijada en el flujo con una elegida como herramienta.

CONCEPTO PRINCIPAL
RAG tradicional y RAG agéntico

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
No toda consulta necesita RAG, pero una política sí necesita su fuente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Compara «Hola» con «¿Cuál es la comisión de mantenimiento?». Pida una predicción.

Saludo: Responder sin cargar fragmentos irrelevantes.

Comisión: Seleccionar retrieve_knowledge_base.

Resultado: Explicar lo que respalda el texto recuperado.

Resultado esperado: El patrón agéntico aporta selección; esa selección también debe comprobarse. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Saludo; Comisión; Resultado. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. Compara «Hola» con «¿Cuál es la comisión de mantenimiento?».
Saludo: Responder sin cargar fragmentos irrelevantes.
Comisión: Seleccionar retrieve_knowledge_base.
Resultado: Explicar lo que respalda el texto recuperado.
Resultado: El patrón agéntico aporta selección; esa selección también debe comprobarse.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué riesgo nuevo aparece al permitir que el agente elija buscar?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: No toda consulta necesita RAG, pero una política sí necesita su fuente.

ERRORES CONCEPTUALES FRECUENTES
Afirmar que la latencia del RAG tradicional es siempre constante.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Colección, punto y payload

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Recuperar y citar: salvaguarda A6

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. Recuperar y citar: salvaguarda A6

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: Recuperar y citar: salvaguarda A6
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §6 y comun/prompts_industria.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Exigir fuente ante afirmaciones sobre tarifas, coberturas, plazos o políticas.

CONCEPTO PRINCIPAL
Recuperar y citar: salvaguarda A6

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
A6 define una obligación; hay que observar si el agente la cumple.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Basta con que aparezca el nombre de un documento en la respuesta?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Afirmación sensible: El usuario pide una regla concreta del dominio.

Recuperación: El agente debe buscar el documento pertinente.

Fundamentación: La respuesta cita la fuente y reconoce cuando no la encuentra.

Cierre con la distinción: A6 define una obligación; hay que observar si el agente la cumple.

ELEMENTOS QUE CONVIENE EXPLICAR
Afirmación sensible; Recuperación; Fundamentación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El cliente pregunta si una situación específica está cubierta.
Buscar: Recuperar el condicionado aplicable.
Comprobar: La cláusula recibida debe sostener la respuesta.
Limitar: Si no hay respaldo, decir que no se puede confirmar.
Resultado: Incluir una cita decorativa no convierte una afirmación en fundamentada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Basta con que aparezca el nombre de un documento en la respuesta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: A6 define una obligación; hay que observar si el agente la cumple.

ERRORES CONCEPTUALES FRECUENTES
Presentar una instrucción del prompt como garantía técnica absoluta.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: RAG tradicional y RAG agéntico

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Conocimiento recuperable y actualización

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. Tres preguntas antes de afirmar

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: Tres preguntas antes de afirmar
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §6 y comun/prompts_industria.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Exigir fuente ante afirmaciones sobre tarifas, coberturas, plazos o políticas.

CONCEPTO PRINCIPAL
Recuperar y citar: salvaguarda A6

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
A6 define una obligación; hay que observar si el agente la cumple.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Existencia: ¿Se recuperó realmente algún fragmento?

Pertinencia: ¿Ese texto corresponde a la pregunta y al ámbito?

Respaldo: ¿Contiene la información que se va a afirmar?

Contraste la regla con este error: Presentar una instrucción del prompt como garantía técnica absoluta. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Existencia; Pertinencia; Respaldo. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El cliente pregunta si una situación específica está cubierta.
Buscar: Recuperar el condicionado aplicable.
Comprobar: La cláusula recibida debe sostener la respuesta.
Limitar: Si no hay respaldo, decir que no se puede confirmar.
Resultado: Incluir una cita decorativa no convierte una afirmación en fundamentada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Basta con que aparezca el nombre de un documento en la respuesta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: A6 define una obligación; hay que observar si el agente la cumple.

ERRORES CONCEPTUALES FRECUENTES
Presentar una instrucción del prompt como garantía técnica absoluta.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: RAG tradicional y RAG agéntico

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Conocimiento recuperable y actualización

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · Recuperar y citar: salvaguarda A6

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: Andina Seguros · Recuperar y citar: salvaguarda A6
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: §6 y comun/prompts_industria.py
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Exigir fuente ante afirmaciones sobre tarifas, coberturas, plazos o políticas.

CONCEPTO PRINCIPAL
Recuperar y citar: salvaguarda A6

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
A6 define una obligación; hay que observar si el agente la cumple.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El cliente pregunta si una situación específica está cubierta. Pida una predicción.

Buscar: Recuperar el condicionado aplicable.

Comprobar: La cláusula recibida debe sostener la respuesta.

Limitar: Si no hay respaldo, decir que no se puede confirmar.

Resultado esperado: Incluir una cita decorativa no convierte una afirmación en fundamentada. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Buscar; Comprobar; Limitar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. El cliente pregunta si una situación específica está cubierta.
Buscar: Recuperar el condicionado aplicable.
Comprobar: La cláusula recibida debe sostener la respuesta.
Limitar: Si no hay respaldo, decir que no se puede confirmar.
Resultado: Incluir una cita decorativa no convierte una afirmación en fundamentada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Basta con que aparezca el nombre de un documento en la respuesta?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: A6 define una obligación; hay que observar si el agente la cumple.

ERRORES CONCEPTUALES FRECUENTES
Presentar una instrucción del prompt como garantía técnica absoluta.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: RAG tradicional y RAG agéntico

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Conocimiento recuperable y actualización

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 22. Conocimiento recuperable y actualización

DIAPOSITIVA 22 · CAPÍTULO 8 · CONCEPTO
Título: Conocimiento recuperable y actualización
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: Demo paramétrico vs recuperable
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mostrar por qué el curso conserva reglas cambiantes fuera de los pesos del modelo.

CONCEPTO PRINCIPAL
Conocimiento recuperable y actualización

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El conocimiento externo puede renovarse sin modificar los pesos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué paso falta entre editar un archivo y esperar resultados nuevos?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Documento: Contiene el dato y su versión vigente.

Índice: Representa los fragmentos disponibles para recuperación.

Modelo: Usa el contexto recuperado sin reentrenar sus parámetros.

Cierre con la distinción: El conocimiento externo puede renovarse sin modificar los pesos.

ELEMENTOS QUE CONVIENE EXPLICAR
Documento; Índice; Modelo. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Un tarifario didáctico cambia una condición del plan.
Antes: La consulta recupera la versión previa.
Actualizar: Incorporar la nueva fuente al índice según la demo.
Después: Verificar que la respuesta usa el nuevo dato con su fuente.
Resultado: Actualizar el documento sin actualizar el índice puede dejar resultados antiguos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué paso falta entre editar un archivo y esperar resultados nuevos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El conocimiento externo puede renovarse sin modificar los pesos.

ERRORES CONCEPTUALES FRECUENTES
Suponer que Qdrant vigila y reindexa archivos automáticamente.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Recuperar y citar: salvaguarda A6

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Laboratorio L5: integrar memoria y RAG

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 23. Actualizar de forma verificable

DIAPOSITIVA 23 · CAPÍTULO 8 · DESARROLLO
Título: Actualizar de forma verificable
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: Demo paramétrico vs recuperable
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mostrar por qué el curso conserva reglas cambiantes fuera de los pesos del modelo.

CONCEPTO PRINCIPAL
Conocimiento recuperable y actualización

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El conocimiento externo puede renovarse sin modificar los pesos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Cambiar: Modificar la fuente de conocimiento que corresponde.

Indexar: Actualizar los puntos afectados mediante el proceso de ingesta.

Probar: Repetir la consulta y comprobar dato y procedencia.

Contraste la regla con este error: Suponer que Qdrant vigila y reindexa archivos automáticamente. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Cambiar; Indexar; Probar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Un tarifario didáctico cambia una condición del plan.
Antes: La consulta recupera la versión previa.
Actualizar: Incorporar la nueva fuente al índice según la demo.
Después: Verificar que la respuesta usa el nuevo dato con su fuente.
Resultado: Actualizar el documento sin actualizar el índice puede dejar resultados antiguos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué paso falta entre editar un archivo y esperar resultados nuevos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El conocimiento externo puede renovarse sin modificar los pesos.

ERRORES CONCEPTUALES FRECUENTES
Suponer que Qdrant vigila y reindexa archivos automáticamente.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Recuperar y citar: salvaguarda A6

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Laboratorio L5: integrar memoria y RAG

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 24. Ejemplo · Conocimiento recuperable y actualización

DIAPOSITIVA 24 · CAPÍTULO 8 · EJEMPLO
Título: AndesMóvil · Conocimiento recuperable y actualización
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: Demo paramétrico vs recuperable
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mostrar por qué el curso conserva reglas cambiantes fuera de los pesos del modelo.

CONCEPTO PRINCIPAL
Conocimiento recuperable y actualización

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El conocimiento externo puede renovarse sin modificar los pesos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Un tarifario didáctico cambia una condición del plan. Pida una predicción.

Antes: La consulta recupera la versión previa.

Actualizar: Incorporar la nueva fuente al índice según la demo.

Después: Verificar que la respuesta usa el nuevo dato con su fuente.

Resultado esperado: Actualizar el documento sin actualizar el índice puede dejar resultados antiguos. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Antes; Actualizar; Después. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. Un tarifario didáctico cambia una condición del plan.
Antes: La consulta recupera la versión previa.
Actualizar: Incorporar la nueva fuente al índice según la demo.
Después: Verificar que la respuesta usa el nuevo dato con su fuente.
Resultado: Actualizar el documento sin actualizar el índice puede dejar resultados antiguos.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué paso falta entre editar un archivo y esperar resultados nuevos?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El conocimiento externo puede renovarse sin modificar los pesos.

ERRORES CONCEPTUALES FRECUENTES
Suponer que Qdrant vigila y reindexa archivos automáticamente.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Recuperar y citar: salvaguarda A6

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación · Sigue: Laboratorio L5: integrar memoria y RAG

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 25. Laboratorio L5: integrar memoria y RAG

DIAPOSITIVA 25 · CAPÍTULO 9 · CONCEPTO
Título: Laboratorio L5: integrar memoria y RAG
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: lab/README.md y requisitos de entrada
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Construir y verificar la nueva capacidad sobre el catálogo de L4.

CONCEPTO PRINCIPAL
Laboratorio L5: integrar memoria y RAG

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué parte debes recuperar después si solo usaste el índice de respaldo?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Ingesta: Dividir corpus, generar vectores y cargar puntos.

Retriever: Exponer recuperación como tool con una docstring clara.

Conversación: Integrar historial y probar preguntas con cita.

Cierre con la distinción: Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

ELEMENTOS QUE CONVIENE EXPLICAR
Ingesta; Retriever; Conversación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El cluster propio falla antes de empezar la ingesta.
Diagnosticar: Revisar las comprobaciones 6 y 7.
Continuar: Coordinar uso de la colección de respaldo del mismo stack.
Recuperar: Completar después la ingesta pendiente con el checkpoint.
Resultado: Usar respaldo no elimina el objetivo de aprender la ingesta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte debes recuperar después si solo usaste el índice de respaldo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

ERRORES CONCEPTUALES FRECUENTES
Sustituir silenciosamente Qdrant por otra arquitectura.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Conocimiento recuperable y actualización

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 26. Pase de entrada y evidencias

DIAPOSITIVA 26 · CAPÍTULO 9 · DESARROLLO
Título: Pase de entrada y evidencias
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: lab/README.md y requisitos de entrada
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Construir y verificar la nueva capacidad sobre el catálogo de L4.

CONCEPTO PRINCIPAL
Laboratorio L5: integrar memoria y RAG

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Servicios: check_stack comprueba embeddings y Qdrant.

Respaldo: La colección kb-<track>-respaldo permite continuar si hay bloqueo.

Verificación: Revisar las diez preguntas de cita verificable del laboratorio.

Contraste la regla con este error: Sustituir silenciosamente Qdrant por otra arquitectura. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Servicios; Respaldo; Verificación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El cluster propio falla antes de empezar la ingesta.
Diagnosticar: Revisar las comprobaciones 6 y 7.
Continuar: Coordinar uso de la colección de respaldo del mismo stack.
Recuperar: Completar después la ingesta pendiente con el checkpoint.
Resultado: Usar respaldo no elimina el objetivo de aprender la ingesta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte debes recuperar después si solo usaste el índice de respaldo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

ERRORES CONCEPTUALES FRECUENTES
Sustituir silenciosamente Qdrant por otra arquitectura.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Conocimiento recuperable y actualización

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 27. Ejemplo · Laboratorio L5: integrar memoria y RAG

DIAPOSITIVA 27 · CAPÍTULO 9 · EJEMPLO
Título: MercaSur · Laboratorio L5: integrar memoria y RAG
Sesión: Memoria contextual y RAG con Qdrant
Archivo: 05-memoria-rag-editable-v2.pptx
Sección que soporta: lab/README.md y requisitos de entrada
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-2-agentes-avanzados/sesion-05-memoria-rag; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Construir y verificar la nueva capacidad sobre el catálogo de L4.

CONCEPTO PRINCIPAL
Laboratorio L5: integrar memoria y RAG

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El cluster propio falla antes de empezar la ingesta. Pida una predicción.

Diagnosticar: Revisar las comprobaciones 6 y 7.

Continuar: Coordinar uso de la colección de respaldo del mismo stack.

Recuperar: Completar después la ingesta pendiente con el checkpoint.

Resultado esperado: Usar respaldo no elimina el objetivo de aprender la ingesta. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Diagnosticar; Continuar; Recuperar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. El cluster propio falla antes de empezar la ingesta.
Diagnosticar: Revisar las comprobaciones 6 y 7.
Continuar: Coordinar uso de la colección de respaldo del mismo stack.
Recuperar: Completar después la ingesta pendiente con el checkpoint.
Resultado: Usar respaldo no elimina el objetivo de aprender la ingesta.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué parte debes recuperar después si solo usaste el índice de respaldo?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Separar preparación operativa y aprendizaje evita bloquear el laboratorio.

ERRORES CONCEPTUALES FRECUENTES
Sustituir silenciosamente Qdrant por otra arquitectura.

CONEXIÓN ANTERIOR
S4: catálogo de cuatro tools · Capítulo previo: Conocimiento recuperable y actualización

CONEXIÓN POSTERIOR
S6: límites; S10: evaluación de fundamentación.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

