# Despliegue con HF Spaces — notas del docente

Fuente: commit `27c24090f1662f9473b673d2020e7bffee04490b`. Tres diapositivas por capítulo.

## 1. Del script a un servicio invocable

DIAPOSITIVA 1 · CAPÍTULO 1 · CONCEPTO
Título: Del script a un servicio invocable
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Definir producción como una ejecución que otra persona puede invocar sin el autor presente.

CONCEPTO PRINCIPAL
Del script a un servicio invocable

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Desplegar añade responsabilidades operativas al agente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué dependencia local impediría que otro use el servicio?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Cliente: Envía una solicitud a una URL conocida.

Servicio: Arranca, carga configuración y atiende la API.

Dependencias: Modelo, simulador y Qdrant siguen fuera del proceso.

Cierre con la distinción: Desplegar añade responsabilidades operativas al agente.

ELEMENTOS QUE CONVIENE EXPLICAR
Cliente; Servicio; Dependencias. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un evaluador consulta un pedido desde su propia computadora.
Conectar: Usar la URL del Space y la key del equipo.
Invocar: Enviar el cuerpo esperado a /chat.
Comprobar: Recibir una respuesta vinculada al simulador.
Resultado: La URL permite acceso; el comportamiento completo todavía debe probarse.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dependencia local impediría que otro use el servicio?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Desplegar añade responsabilidades operativas al agente.

ERRORES CONCEPTUALES FRECUENTES
Equiparar archivo subido con servicio funcional.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado.

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Configuración por entorno

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 2. Qué cambia respecto a la laptop

DIAPOSITIVA 2 · CAPÍTULO 1 · DESARROLLO
Título: Qué cambia respecto a la laptop
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Definir producción como una ejecución que otra persona puede invocar sin el autor presente.

CONCEPTO PRINCIPAL
Del script a un servicio invocable

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Desplegar añade responsabilidades operativas al agente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Acceso: La invocación deja de depender de la terminal del autor.

Operación: El proceso debe arrancar con configuración disponible.

Evidencia: Otra persona comprueba una consulta completa desde fuera.

Contraste la regla con este error: Equiparar archivo subido con servicio funcional. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Acceso; Operación; Evidencia. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un evaluador consulta un pedido desde su propia computadora.
Conectar: Usar la URL del Space y la key del equipo.
Invocar: Enviar el cuerpo esperado a /chat.
Comprobar: Recibir una respuesta vinculada al simulador.
Resultado: La URL permite acceso; el comportamiento completo todavía debe probarse.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dependencia local impediría que otro use el servicio?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Desplegar añade responsabilidades operativas al agente.

ERRORES CONCEPTUALES FRECUENTES
Equiparar archivo subido con servicio funcional.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado.

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Configuración por entorno

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 3. Ejemplo · Del script a un servicio invocable

DIAPOSITIVA 3 · CAPÍTULO 1 · EJEMPLO
Título: MercaSur · Del script a un servicio invocable
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: Objetivos y §0
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Definir producción como una ejecución que otra persona puede invocar sin el autor presente.

CONCEPTO PRINCIPAL
Del script a un servicio invocable

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Desplegar añade responsabilidades operativas al agente.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Un evaluador consulta un pedido desde su propia computadora. Pida una predicción.

Conectar: Usar la URL del Space y la key del equipo.

Invocar: Enviar el cuerpo esperado a /chat.

Comprobar: Recibir una respuesta vinculada al simulador.

Resultado esperado: La URL permite acceso; el comportamiento completo todavía debe probarse. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Conectar; Invocar; Comprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Un evaluador consulta un pedido desde su propia computadora.
Conectar: Usar la URL del Space y la key del equipo.
Invocar: Enviar el cuerpo esperado a /chat.
Comprobar: Recibir una respuesta vinculada al simulador.
Resultado: La URL permite acceso; el comportamiento completo todavía debe probarse.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dependencia local impediría que otro use el servicio?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Desplegar añade responsabilidades operativas al agente.

ERRORES CONCEPTUALES FRECUENTES
Equiparar archivo subido con servicio funcional.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado.

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Configuración por entorno

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 4. Configuración por entorno

DIAPOSITIVA 4 · CAPÍTULO 2 · CONCEPTO
Título: Configuración por entorno
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §1 · 12-Factor
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mantener el código y cambiar los valores de configuración entre entornos.

CONCEPTO PRINCIPAL
Configuración por entorno

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Separar configuración permite mover el código entre entornos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué comprobarías si solo falla la versión desplegada?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Laptop: .env proporciona variables durante desarrollo.

Space: La plataforma proporciona secretos y variables.

Aplicación: comun/settings.py lee la configuración al ejecutarse.

Cierre con la distinción: Separar configuración permite mover el código entre entornos.

ELEMENTOS QUE CONVIENE EXPLICAR
Laptop; Space; Aplicación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El agente local encuentra Qdrant, pero el Space no.
Comparar: Revisar presencia de QDRANT_URL y credenciales en el destino.
Corregir: Configurar el entorno del Space.
Reiniciar: Volver a verificar la conexión desde el servicio desplegado.
Resultado: El .env de la laptop no se copia mágicamente al contenedor.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué comprobarías si solo falla la versión desplegada?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Separar configuración permite mover el código entre entornos.

ERRORES CONCEPTUALES FRECUENTES
Editar el agente para pegar claves o URLs de cada entorno.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Del script a un servicio invocable

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Dockerfile: describir el arranque

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 5. Revisar la configuración de destino

DIAPOSITIVA 5 · CAPÍTULO 2 · DESARROLLO
Título: Revisar la configuración de destino
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §1 · 12-Factor
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mantener el código y cambiar los valores de configuración entre entornos.

CONCEPTO PRINCIPAL
Configuración por entorno

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Separar configuración permite mover el código entre entornos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Inventario: Identificar variables realmente utilizadas por el checkpoint.

Destino: Cargar endpoint y credenciales correctos en el Space.

Validación: Comprobar el arranque sin imprimir secretos.

Contraste la regla con este error: Editar el agente para pegar claves o URLs de cada entorno. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Inventario; Destino; Validación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El agente local encuentra Qdrant, pero el Space no.
Comparar: Revisar presencia de QDRANT_URL y credenciales en el destino.
Corregir: Configurar el entorno del Space.
Reiniciar: Volver a verificar la conexión desde el servicio desplegado.
Resultado: El .env de la laptop no se copia mágicamente al contenedor.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué comprobarías si solo falla la versión desplegada?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Separar configuración permite mover el código entre entornos.

ERRORES CONCEPTUALES FRECUENTES
Editar el agente para pegar claves o URLs de cada entorno.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Del script a un servicio invocable

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Dockerfile: describir el arranque

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 6. Ejemplo · Configuración por entorno

DIAPOSITIVA 6 · CAPÍTULO 2 · EJEMPLO
Título: Banco Inti · Configuración por entorno
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §1 · 12-Factor
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Mantener el código y cambiar los valores de configuración entre entornos.

CONCEPTO PRINCIPAL
Configuración por entorno

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Separar configuración permite mover el código entre entornos.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El agente local encuentra Qdrant, pero el Space no. Pida una predicción.

Comparar: Revisar presencia de QDRANT_URL y credenciales en el destino.

Corregir: Configurar el entorno del Space.

Reiniciar: Volver a verificar la conexión desde el servicio desplegado.

Resultado esperado: El .env de la laptop no se copia mágicamente al contenedor. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Comparar; Corregir; Reiniciar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El agente local encuentra Qdrant, pero el Space no.
Comparar: Revisar presencia de QDRANT_URL y credenciales en el destino.
Corregir: Configurar el entorno del Space.
Reiniciar: Volver a verificar la conexión desde el servicio desplegado.
Resultado: El .env de la laptop no se copia mágicamente al contenedor.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué comprobarías si solo falla la versión desplegada?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Separar configuración permite mover el código entre entornos.

ERRORES CONCEPTUALES FRECUENTES
Editar el agente para pegar claves o URLs de cada entorno.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Del script a un servicio invocable

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Dockerfile: describir el arranque

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 7. Dockerfile: describir el arranque

DIAPOSITIVA 7 · CAPÍTULO 3 · CONCEPTO
Título: Dockerfile: describir el arranque
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §2 y solucion/*/Dockerfile
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar las etapas que convierten el repositorio en un servicio ejecutable.

CONCEPTO PRINCIPAL
Dockerfile: describir el arranque

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un contenedor útil incluye un arranque verificable.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué diferencia hay entre un fallo de build y uno al iniciar la API?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Base y dependencias: Elegir entorno Python e instalar requirements.

Código y proceso: Copiar archivos y definir directorio de trabajo.

Arranque: Iniciar la API con interfaz y puerto requeridos por la plataforma.

Cierre con la distinción: Un contenedor útil incluye un arranque verificable.

ELEMENTOS QUE CONVIENE EXPLICAR
Base y dependencias; Código y proceso; Arranque. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El build termina, pero la URL no acepta conexiones.
Aislar: Construcción correcta no demuestra escucha correcta.
Revisar: Comando de arranque, interfaz y puerto del Dockerfile.
Verificar: Comprobar /health desde fuera después del redespliegue.
Resultado: HF Spaces construye el contenedor; el curso no exige ejecutar Docker localmente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre un fallo de build y uno al iniciar la API?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un contenedor útil incluye un arranque verificable.

ERRORES CONCEPTUALES FRECUENTES
Confundir EXPOSE con abrir automáticamente cualquier servicio.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Configuración por entorno

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: FastAPI: health y chat

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 8. Leer cada instrucción por su efecto

DIAPOSITIVA 8 · CAPÍTULO 3 · DESARROLLO
Título: Leer cada instrucción por su efecto
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §2 y solucion/*/Dockerfile
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar las etapas que convierten el repositorio en un servicio ejecutable.

CONCEPTO PRINCIPAL
Dockerfile: describir el arranque

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un contenedor útil incluye un arranque verificable.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Construcción: Qué se instala o copia durante el build.

Ejecución: Qué comando se inicia al arrancar el contenedor.

Configuración: Qué valores se reciben como variables en runtime.

Contraste la regla con este error: Confundir EXPOSE con abrir automáticamente cualquier servicio. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Construcción; Ejecución; Configuración. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El build termina, pero la URL no acepta conexiones.
Aislar: Construcción correcta no demuestra escucha correcta.
Revisar: Comando de arranque, interfaz y puerto del Dockerfile.
Verificar: Comprobar /health desde fuera después del redespliegue.
Resultado: HF Spaces construye el contenedor; el curso no exige ejecutar Docker localmente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre un fallo de build y uno al iniciar la API?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un contenedor útil incluye un arranque verificable.

ERRORES CONCEPTUALES FRECUENTES
Confundir EXPOSE con abrir automáticamente cualquier servicio.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Configuración por entorno

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: FastAPI: health y chat

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 9. Ejemplo · Dockerfile: describir el arranque

DIAPOSITIVA 9 · CAPÍTULO 3 · EJEMPLO
Título: AndesMóvil · Dockerfile: describir el arranque
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §2 y solucion/*/Dockerfile
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Explicar las etapas que convierten el repositorio en un servicio ejecutable.

CONCEPTO PRINCIPAL
Dockerfile: describir el arranque

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Un contenedor útil incluye un arranque verificable.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El build termina, pero la URL no acepta conexiones. Pida una predicción.

Aislar: Construcción correcta no demuestra escucha correcta.

Revisar: Comando de arranque, interfaz y puerto del Dockerfile.

Verificar: Comprobar /health desde fuera después del redespliegue.

Resultado esperado: HF Spaces construye el contenedor; el curso no exige ejecutar Docker localmente. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Aislar; Revisar; Verificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. El build termina, pero la URL no acepta conexiones.
Aislar: Construcción correcta no demuestra escucha correcta.
Revisar: Comando de arranque, interfaz y puerto del Dockerfile.
Verificar: Comprobar /health desde fuera después del redespliegue.
Resultado: HF Spaces construye el contenedor; el curso no exige ejecutar Docker localmente.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué diferencia hay entre un fallo de build y uno al iniciar la API?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Un contenedor útil incluye un arranque verificable.

ERRORES CONCEPTUALES FRECUENTES
Confundir EXPOSE con abrir automáticamente cualquier servicio.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Configuración por entorno

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: FastAPI: health y chat

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 10. FastAPI: health y chat

DIAPOSITIVA 10 · CAPÍTULO 4 · CONCEPTO
Título: FastAPI: health y chat
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar comprobación de vida y ejecución que consume recursos.

CONCEPTO PRINCIPAL
FastAPI: health y chat

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Cada endpoint tiene una responsabilidad y un nivel de acceso.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Por qué no proteger /health con la misma key?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

GET /health: Permite a la plataforma comprobar que el servicio vive.

POST /chat: Recibe la consulta y ejecuta el agente.

X-API-Key: Protege /chat con la clave propia del equipo.

Cierre con la distinción: Cada endpoint tiene una responsabilidad y un nivel de acceso.

ELEMENTOS QUE CONVIENE EXPLICAR
GET /health; POST /chat; X-API-Key. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una persona conoce la URL pública pero no la clave del equipo.
Health: Puede comprobar si la API está viva.
Chat: No debe gastar cuota mediante una llamada sin autorización.
Evaluador: Recibe URL y key por el canal previsto para probar.
Resultado: Un health exitoso no demuestra que modelo, tools y RAG funcionen de extremo a extremo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué no proteger /health con la misma key?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Cada endpoint tiene una responsabilidad y un nivel de acceso.

ERRORES CONCEPTUALES FRECUENTES
Publicar /chat sin control o confundir la key del agente con HF_TOKEN.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Dockerfile: describir el arranque

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Secretos en el Space

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 11. Probar las dos rutas

DIAPOSITIVA 11 · CAPÍTULO 4 · DESARROLLO
Título: Probar las dos rutas
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar comprobación de vida y ejecución que consume recursos.

CONCEPTO PRINCIPAL
FastAPI: health y chat

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Cada endpoint tiene una responsabilidad y un nivel de acceso.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Health: Debe responder sin una credencial del cliente.

Sin key: La ruta de chat debe rechazar la invocación.

Con key: La solicitud válida puede ejecutar el agente.

Contraste la regla con este error: Publicar /chat sin control o confundir la key del agente con HF_TOKEN. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Health; Sin key; Con key. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una persona conoce la URL pública pero no la clave del equipo.
Health: Puede comprobar si la API está viva.
Chat: No debe gastar cuota mediante una llamada sin autorización.
Evaluador: Recibe URL y key por el canal previsto para probar.
Resultado: Un health exitoso no demuestra que modelo, tools y RAG funcionen de extremo a extremo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué no proteger /health con la misma key?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Cada endpoint tiene una responsabilidad y un nivel de acceso.

ERRORES CONCEPTUALES FRECUENTES
Publicar /chat sin control o confundir la key del agente con HF_TOKEN.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Dockerfile: describir el arranque

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Secretos en el Space

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 12. Ejemplo · FastAPI: health y chat

DIAPOSITIVA 12 · CAPÍTULO 4 · EJEMPLO
Título: MercaSur · FastAPI: health y chat
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §3
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Separar comprobación de vida y ejecución que consume recursos.

CONCEPTO PRINCIPAL
FastAPI: health y chat

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Cada endpoint tiene una responsabilidad y un nivel de acceso.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Una persona conoce la URL pública pero no la clave del equipo. Pida una predicción.

Health: Puede comprobar si la API está viva.

Chat: No debe gastar cuota mediante una llamada sin autorización.

Evaluador: Recibe URL y key por el canal previsto para probar.

Resultado esperado: Un health exitoso no demuestra que modelo, tools y RAG funcionen de extremo a extremo. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Health; Chat; Evaluador. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Una persona conoce la URL pública pero no la clave del equipo.
Health: Puede comprobar si la API está viva.
Chat: No debe gastar cuota mediante una llamada sin autorización.
Evaluador: Recibe URL y key por el canal previsto para probar.
Resultado: Un health exitoso no demuestra que modelo, tools y RAG funcionen de extremo a extremo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Por qué no proteger /health con la misma key?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Cada endpoint tiene una responsabilidad y un nivel de acceso.

ERRORES CONCEPTUALES FRECUENTES
Publicar /chat sin control o confundir la key del agente con HF_TOKEN.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Dockerfile: describir el arranque

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Secretos en el Space

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 13. Secretos en el Space

DIAPOSITIVA 13 · CAPÍTULO 5 · CONCEPTO
Título: Secretos en el Space
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Cargar credenciales en la plataforma y responder correctamente ante una exposición.

CONCEPTO PRINCIPAL
Secretos en el Space

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los secretos se administran fuera del código y con capacidad de revocación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué acción hace inútil el token que alguien pudo haber copiado?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Repositorio: Contiene código y nombres de variables, no sus valores secretos.

Plataforma: Entrega credenciales al proceso desde Space secrets.

Incidente: Una credencial publicada requiere revocación y reemplazo.

Cierre con la distinción: Los secretos se administran fuera del código y con capacidad de revocación.

ELEMENTOS QUE CONVIENE EXPLICAR
Repositorio; Plataforma; Incidente. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El equipo detecta que un token de prueba apareció en un commit.
Revocar: Invalidar el token comprometido.
Reemplazar: Configurar uno nuevo en el entorno correspondiente.
Revisar: Corregir el manejo del archivo y las evidencias que lo expusieron.
Resultado: Eliminar el archivo no invalida una credencial ya publicada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué acción hace inútil el token que alguien pudo haber copiado?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los secretos se administran fuera del código y con capacidad de revocación.

ERRORES CONCEPTUALES FRECUENTES
Creer que borrar el último commit equivale a revocar el acceso.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: FastAPI: health y chat

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Cold start y latencia percibida

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 14. Recorrido de una clave

DIAPOSITIVA 14 · CAPÍTULO 5 · DESARROLLO
Título: Recorrido de una clave
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Cargar credenciales en la plataforma y responder correctamente ante una exposición.

CONCEPTO PRINCIPAL
Secretos en el Space

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los secretos se administran fuera del código y con capacidad de revocación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Crear: Obtener la credencial con permisos adecuados al servicio.

Configurar: Guardarla en el destino que ejecutará el agente.

Rotar: Invalidar la anterior si se expuso, sin confiar en borrar el texto.

Contraste la regla con este error: Creer que borrar el último commit equivale a revocar el acceso. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Crear; Configurar; Rotar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El equipo detecta que un token de prueba apareció en un commit.
Revocar: Invalidar el token comprometido.
Reemplazar: Configurar uno nuevo en el entorno correspondiente.
Revisar: Corregir el manejo del archivo y las evidencias que lo expusieron.
Resultado: Eliminar el archivo no invalida una credencial ya publicada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué acción hace inútil el token que alguien pudo haber copiado?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los secretos se administran fuera del código y con capacidad de revocación.

ERRORES CONCEPTUALES FRECUENTES
Creer que borrar el último commit equivale a revocar el acceso.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: FastAPI: health y chat

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Cold start y latencia percibida

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 15. Ejemplo · Secretos en el Space

DIAPOSITIVA 15 · CAPÍTULO 5 · EJEMPLO
Título: Banco Inti · Secretos en el Space
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §4
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Cargar credenciales en la plataforma y responder correctamente ante una exposición.

CONCEPTO PRINCIPAL
Secretos en el Space

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Los secretos se administran fuera del código y con capacidad de revocación.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: El equipo detecta que un token de prueba apareció en un commit. Pida una predicción.

Revocar: Invalidar el token comprometido.

Reemplazar: Configurar uno nuevo en el entorno correspondiente.

Revisar: Corregir el manejo del archivo y las evidencias que lo expusieron.

Resultado esperado: Eliminar el archivo no invalida una credencial ya publicada. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Revocar; Reemplazar; Revisar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Banco Inti. El equipo detecta que un token de prueba apareció en un commit.
Revocar: Invalidar el token comprometido.
Reemplazar: Configurar uno nuevo en el entorno correspondiente.
Revisar: Corregir el manejo del archivo y las evidencias que lo expusieron.
Resultado: Eliminar el archivo no invalida una credencial ya publicada.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué acción hace inútil el token que alguien pudo haber copiado?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Los secretos se administran fuera del código y con capacidad de revocación.

ERRORES CONCEPTUALES FRECUENTES
Creer que borrar el último commit equivale a revocar el acceso.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: FastAPI: health y chat

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Cold start y latencia percibida

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 16. Cold start y latencia percibida

DIAPOSITIVA 16 · CAPÍTULO 6 · CONCEPTO
Título: Cold start y latencia percibida
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir la primera solicitud tras inactividad de una ejecución con el servicio activo.

CONCEPTO PRINCIPAL
Cold start y latencia percibida

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El contexto operativo forma parte de la medición de latencia.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué dato guardarías junto al tiempo de la primera llamada?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Inactividad: El servicio puede necesitar reactivarse.

Primera solicitud: Incluye costos de arranque y carga.

Solicitudes siguientes: Permiten observar el servicio ya activo.

Cierre con la distinción: El contexto operativo forma parte de la medición de latencia.

ELEMENTOS QUE CONVIENE EXPLICAR
Inactividad; Primera solicitud; Solicitudes siguientes. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La primera respuesta tarda más que la segunda tras inactividad.
Medir: Cronometrar ambas solicitudes con el mismo contenido.
Anotar: Identificar cuál activó el Space.
Explicar: No atribuir toda la diferencia al prompt sin observación adicional.
Resultado: Los tiempos deben medirse en el entorno real; no se prometen cifras del tier.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dato guardarías junto al tiempo de la primera llamada?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El contexto operativo forma parte de la medición de latencia.

ERRORES CONCEPTUALES FRECUENTES
Generalizar dos mediciones como una latencia garantizada.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Secretos en el Space

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Laboratorio L8: despliegue verificable

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 17. Medir sin confundir causas

DIAPOSITIVA 17 · CAPÍTULO 6 · DESARROLLO
Título: Medir sin confundir causas
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir la primera solicitud tras inactividad de una ejecución con el servicio activo.

CONCEPTO PRINCIPAL
Cold start y latencia percibida

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El contexto operativo forma parte de la medición de latencia.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Registrar: Anotar condición de arranque y tiempo de cada solicitud.

Comparar: Usar la misma consulta al repetir.

Interpretar: Separar arranque, red, modelo y herramientas cuando haya evidencia.

Contraste la regla con este error: Generalizar dos mediciones como una latencia garantizada. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Registrar; Comparar; Interpretar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La primera respuesta tarda más que la segunda tras inactividad.
Medir: Cronometrar ambas solicitudes con el mismo contenido.
Anotar: Identificar cuál activó el Space.
Explicar: No atribuir toda la diferencia al prompt sin observación adicional.
Resultado: Los tiempos deben medirse en el entorno real; no se prometen cifras del tier.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dato guardarías junto al tiempo de la primera llamada?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El contexto operativo forma parte de la medición de latencia.

ERRORES CONCEPTUALES FRECUENTES
Generalizar dos mediciones como una latencia garantizada.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Secretos en el Space

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Laboratorio L8: despliegue verificable

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 18. Ejemplo · Cold start y latencia percibida

DIAPOSITIVA 18 · CAPÍTULO 6 · EJEMPLO
Título: AndesMóvil · Cold start y latencia percibida
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §5
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Distinguir la primera solicitud tras inactividad de una ejecución con el servicio activo.

CONCEPTO PRINCIPAL
Cold start y latencia percibida

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
El contexto operativo forma parte de la medición de latencia.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La primera respuesta tarda más que la segunda tras inactividad. Pida una predicción.

Medir: Cronometrar ambas solicitudes con el mismo contenido.

Anotar: Identificar cuál activó el Space.

Explicar: No atribuir toda la diferencia al prompt sin observación adicional.

Resultado esperado: Los tiempos deben medirse en el entorno real; no se prometen cifras del tier. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Medir; Anotar; Explicar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
AndesMóvil. La primera respuesta tarda más que la segunda tras inactividad.
Medir: Cronometrar ambas solicitudes con el mismo contenido.
Anotar: Identificar cuál activó el Space.
Explicar: No atribuir toda la diferencia al prompt sin observación adicional.
Resultado: Los tiempos deben medirse en el entorno real; no se prometen cifras del tier.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué dato guardarías junto al tiempo de la primera llamada?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: El contexto operativo forma parte de la medición de latencia.

ERRORES CONCEPTUALES FRECUENTES
Generalizar dos mediciones como una latencia garantizada.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Secretos en el Space

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: Laboratorio L8: despliegue verificable

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 19. Laboratorio L8: despliegue verificable

DIAPOSITIVA 19 · CAPÍTULO 7 · CONCEPTO
Título: Laboratorio L8: despliegue verificable
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §6 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Entregar una API pública que otro integrante pueda probar.

CONCEPTO PRINCIPAL
Laboratorio L8: despliegue verificable

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Verificar desde fuera revela dependencias que la laptop puede ocultar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué caso usarías para comprobar también Qdrant?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Construir: API, Dockerfile y dependencias del checkpoint.

Publicar: Crear el Space, configurar secretos y enviar el código.

Verificar: Probar health, autenticación y una consulta real desde fuera.

Cierre con la distinción: Verificar desde fuera revela dependencias que la laptop puede ocultar.

ELEMENTOS QUE CONVIENE EXPLICAR
Construir; Publicar; Verificar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. La API responde health, pero falla una consulta de póliza.
Distinguir: El proceso vive; una dependencia del flujo está fallando.
Localizar: Revisar configuración y respuesta de la tool.
Reprobar: Ejecutar el caso de extremo a extremo desde el cliente externo.
Resultado: Una evidencia de despliegue incluye el flujo real, no solo una página accesible.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué caso usarías para comprobar también Qdrant?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Verificar desde fuera revela dependencias que la laptop puede ocultar.

ERRORES CONCEPTUALES FRECUENTES
Dar por concluido el laboratorio con una captura del build.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Cold start y latencia percibida

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: De disponibilidad a observabilidad

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 20. Evidencia del avance M3

DIAPOSITIVA 20 · CAPÍTULO 7 · DESARROLLO
Título: Evidencia del avance M3
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §6 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Entregar una API pública que otro integrante pueda probar.

CONCEPTO PRINCIPAL
Laboratorio L8: despliegue verificable

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Verificar desde fuera revela dependencias que la laptop puede ocultar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Acceso: URL y procedimiento de autenticación para el evaluador.

Funcionamiento: Consulta de cada capacidad núcleo del track.

Operación: Observaciones del arranque y sus tiempos.

Contraste la regla con este error: Dar por concluido el laboratorio con una captura del build. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Acceso; Funcionamiento; Operación. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. La API responde health, pero falla una consulta de póliza.
Distinguir: El proceso vive; una dependencia del flujo está fallando.
Localizar: Revisar configuración y respuesta de la tool.
Reprobar: Ejecutar el caso de extremo a extremo desde el cliente externo.
Resultado: Una evidencia de despliegue incluye el flujo real, no solo una página accesible.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué caso usarías para comprobar también Qdrant?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Verificar desde fuera revela dependencias que la laptop puede ocultar.

ERRORES CONCEPTUALES FRECUENTES
Dar por concluido el laboratorio con una captura del build.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Cold start y latencia percibida

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: De disponibilidad a observabilidad

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 21. Ejemplo · Laboratorio L8: despliegue verificable

DIAPOSITIVA 21 · CAPÍTULO 7 · EJEMPLO
Título: Andina Seguros · Laboratorio L8: despliegue verificable
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §6 y lab/README.md
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Entregar una API pública que otro integrante pueda probar.

CONCEPTO PRINCIPAL
Laboratorio L8: despliegue verificable

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
Verificar desde fuera revela dependencias que la laptop puede ocultar.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: La API responde health, pero falla una consulta de póliza. Pida una predicción.

Distinguir: El proceso vive; una dependencia del flujo está fallando.

Localizar: Revisar configuración y respuesta de la tool.

Reprobar: Ejecutar el caso de extremo a extremo desde el cliente externo.

Resultado esperado: Una evidencia de despliegue incluye el flujo real, no solo una página accesible. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Distinguir; Localizar; Reprobar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
Andina Seguros. La API responde health, pero falla una consulta de póliza.
Distinguir: El proceso vive; una dependencia del flujo está fallando.
Localizar: Revisar configuración y respuesta de la tool.
Reprobar: Ejecutar el caso de extremo a extremo desde el cliente externo.
Resultado: Una evidencia de despliegue incluye el flujo real, no solo una página accesible.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué caso usarías para comprobar también Qdrant?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: Verificar desde fuera revela dependencias que la laptop puede ocultar.

ERRORES CONCEPTUALES FRECUENTES
Dar por concluido el laboratorio con una captura del build.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Cold start y latencia percibida

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado · Sigue: De disponibilidad a observabilidad

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 22. De disponibilidad a observabilidad

DIAPOSITIVA 22 · CAPÍTULO 8 · CONCEPTO
Título: De disponibilidad a observabilidad
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §7 y conexión S9
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Identificar qué sigue siendo invisible después de publicar la API.

CONCEPTO PRINCIPAL
De disponibilidad a observabilidad

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La siguiente capa convierte ejecuciones en evidencia diagnóstica.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Abra con la pregunta «¿Qué no puedes concluir mirando solo el tiempo total?». Escuche una respuesta antes de revelar la conclusión. Explique las tres responsabilidades y pida al grupo que señale cuál aporta la evidencia y cuál solo transforma o presenta información.

Ahora: Se puede invocar y medir el tiempo total.

Pregunta pendiente: ¿Dónde se consume tiempo y qué camino se ejecutó?

S9: Las trazas permitirán inspeccionar modelo, tools y recuperación.

Cierre con la distinción: La siguiente capa convierte ejecuciones en evidencia diagnóstica.

ELEMENTOS QUE CONVIENE EXPLICAR
Ahora; Pregunta pendiente; S9. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Dos consultas terminan bien, pero una tarda mucho más.
Observar: El tiempo total muestra una diferencia.
Preguntar: Puede haber llamadas extra, lentitud externa o recuperación.
Investigar: S9 separará los pasos mediante spans.
Resultado: Saber que el agente respondió no explica cómo lo hizo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué no puedes concluir mirando solo el tiempo total?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La siguiente capa convierte ejecuciones en evidencia diagnóstica.

ERRORES CONCEPTUALES FRECUENTES
Adivinar un cuello de botella sin ver los pasos.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Laboratorio L8: despliegue verificable

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 23. Preparar la instrumentación

DIAPOSITIVA 23 · CAPÍTULO 8 · DESARROLLO
Título: Preparar la instrumentación
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §7 y conexión S9
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Identificar qué sigue siendo invisible después de publicar la API.

CONCEPTO PRINCIPAL
De disponibilidad a observabilidad

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La siguiente capa convierte ejecuciones en evidencia diagnóstica.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Recupere la idea de la diapositiva anterior y aplíquela a estas comprobaciones. Recorra cada fila y pregunte qué evidencia necesitarían para darla por cumplida.

Caso completo: Conservar una consulta representativa del track.

Identificación: Poder relacionar solicitud y ejecución.

Protección: Evitar datos sensibles en las evidencias compartidas.

Contraste la regla con este error: Adivinar un cuello de botella sin ver los pasos. Pida que expliquen la consecuencia concreta en su propio track.

ELEMENTOS QUE CONVIENE EXPLICAR
Caso completo; Identificación; Protección. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Dos consultas terminan bien, pero una tarda mucho más.
Observar: El tiempo total muestra una diferencia.
Preguntar: Puede haber llamadas extra, lentitud externa o recuperación.
Investigar: S9 separará los pasos mediante spans.
Resultado: Saber que el agente respondió no explica cómo lo hizo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué no puedes concluir mirando solo el tiempo total?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La siguiente capa convierte ejecuciones en evidencia diagnóstica.

ERRORES CONCEPTUALES FRECUENTES
Adivinar un cuello de botella sin ver los pasos.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Laboratorio L8: despliegue verificable

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 2–4 minutos según conocimientos previos; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

## 24. Ejemplo · De disponibilidad a observabilidad

DIAPOSITIVA 24 · CAPÍTULO 8 · EJEMPLO
Título: MercaSur · De disponibilidad a observabilidad
Sesión: Despliegue con HF Spaces
Archivo: 08-despliegue-hf-spaces-editable-v2.pptx
Sección que soporta: §7 y conexión S9
Fuente principal: https://github.com/javierrosado/ariwalab-course-langchain/blob/27c24090f1662f9473b673d2020e7bffee04490b/modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md
Contexto adicional: laboratorios, demos y soluciones de modulo-3-produccion/sesion-08-despliegue-hf-spaces; módulos comunes del repositorio.
Revisión de fuente: 27c24090f1662f9473b673d2020e7bffee04490b

OBJETIVO PEDAGÓGICO
Identificar qué sigue siendo invisible después de publicar la API.

CONCEPTO PRINCIPAL
De disponibilidad a observabilidad

MENSAJE QUE DEBE LLEVARSE EL ALUMNO
La siguiente capa convierte ejecuciones en evidencia diagnóstica.

EXPLICACIÓN SUGERIDA PARA EL DOCENTE
Plantee el caso antes de mostrar los pasos: Dos consultas terminan bien, pero una tarda mucho más. Pida una predicción.

Observar: El tiempo total muestra una diferencia.

Preguntar: Puede haber llamadas extra, lentitud externa o recuperación.

Investigar: S9 separará los pasos mediante spans.

Resultado esperado: Saber que el agente respondió no explica cómo lo hizo. Discuta qué parte se observó, qué parte debe comprobarse y qué conclusión sería excesiva. No presente este caso didáctico como una ejecución real medida. Proponga cambiar un dato de entrada y preguntar si se mantiene el razonamiento.

ELEMENTOS QUE CONVIENE EXPLICAR
Observar; Preguntar; Investigar. Las flechas indican progresión o relación según el rótulo; las comparaciones no implican una secuencia de ejecución.

EJEMPLO PRÁCTICO / APLICACIÓN A INDUSTRIA
MercaSur. Dos consultas terminan bien, pero una tarda mucho más.
Observar: El tiempo total muestra una diferencia.
Preguntar: Puede haber llamadas extra, lentitud externa o recuperación.
Investigar: S9 separará los pasos mediante spans.
Resultado: Saber que el agente respondió no explica cómo lo hizo.
Los casos y datos son didácticos o sintéticos. Las cifras copiadas de una demostración se identifican como tales; no son mediciones producidas al construir la presentación.

PREGUNTA SUGERIDA
¿Qué no puedes concluir mirando solo el tiempo total?
Orientación para el docente: contraste la respuesta con los criterios del desarrollo y pida evidencia. La conclusión debe respetar: La siguiente capa convierte ejecuciones en evidencia diagnóstica.

ERRORES CONCEPTUALES FRECUENTES
Adivinar un cuello de botella sin ver los pasos.

CONEXIÓN ANTERIOR
S7: checkpoint integrado y probado · Capítulo previo: Laboratorio L8: despliegue verificable

CONEXIÓN POSTERIOR
S9: observar el servicio desplegado.

NOTAS PARA EDITAR Y PRESENTAR
Textos, contenedores, tablas y conectores son objetos nativos editables. Formato 16:9. El bloque de tres láminas puede revelarse progresivamente. Duración sugerida: 3–5 minutos con discusión; el conjunto es un banco docente y no prescribe ampliar las horas del curso. Mantenga visibles los límites y no convierta ejemplos en resultados medidos. Fuente tipográfica: DejaVu Sans; si PowerPoint la sustituye, revise los saltos de línea.


---

