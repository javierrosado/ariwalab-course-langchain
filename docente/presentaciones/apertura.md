# Bienvenida al curso — guion docente y prompts visuales

Apertura de 20 minutos antes de [S0](../../00-preparacion/README.md).
Once sesiones, 66 horas: 33 en vivo y 33 asíncronas. S0 y bonus quedan fuera de ese total.
Los mensajes sirven como guion oral; cada prompt puede copiarse por separado en ChatGPT Imágenes.

## 1. Propósito y audiencia · 2 min

### Qué comunicar

En este curso aprenderemos a construir aplicaciones que usan un modelo de lenguaje para consultar información, seleccionar herramientas y responder dentro de límites definidos. Por ejemplo, una consulta sobre un pedido exige identificar la información necesaria, consultar el sistema y explicar el resultado.

El curso está dirigido a desarrolladores con conocimientos de Python, REST, Git y línea de comandos. No necesitan experiencia previa con LLM: comenzaremos con una preparación específica. El objetivo es implementar un agente, explicar sus componentes y comprobar su comportamiento con evidencia.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “Construcción de agentes de IA con LangChain”.
Subtítulo: “Aprender a construir, controlar y evaluar”.
En el centro, tres tarjetas conectadas de izquierda a derecha: “Consultar información”, con documentos y base de datos; “Usar herramientas”, con llave inglesa y función; “Responder con evidencia”, con conversación y referencia documental.
Debajo, una franja con “Base requerida: Python · REST · Git” y “Sin experiencia previa con LLM”. El título domina la composición; las tres capacidades son el segundo foco. No representar al modelo como una persona ni sugerir autonomía ilimitada.
Pie discreto: “01 / 08”.
```

## 2. Resultado final · 3 min

### Qué comunicar

Cada equipo construirá un prototipo accesible mediante una aplicación web y una API. Un usuario podrá preguntar qué plan tiene y cuál es su tarifa: la aplicación consultará los datos del cliente con una herramienta y recuperará información del servicio desde documentos.

También podremos investigar qué herramientas se ejecutaron, cuánto tardaron las llamadas y qué resultados obtuvimos al evaluar distintos casos. Documentaremos los límites del prototipo: desplegarlo no demuestra que esté preparado para operar con clientes reales. Mostrar aquí una demo verificada, siguiendo una consulta de principio a fin.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “El resultado final: un agente que puedes explicar y evaluar”.
A la izquierda, una interfaz web con “¿Qué plan tengo y cuál es su tarifa?”. En el centro, un contenedor “Agente” con “Modelo” y “Ejecución de herramientas”. Debajo, fuera del contenedor, “Datos del cliente” y “Documentos del servicio”. Las conexiones a esos recursos parten de “Ejecución de herramientas”, nunca directamente del modelo; mostrar consultas y retornos.
A la derecha: “Información del plan con su fuente”. En la franja inferior: “Traza de ejecución”, con árbol de operaciones, y “Evaluación”, con tabla de casos. Conectar la traza mediante una línea discontinua “Telemetría”. Nota: “Prototipo didáctico con límites documentados”. No inventar datos de clientes ni resultados.
Pie discreto: “02 / 08”.
```

## 3. Alcance y límites · 3 min

### Qué comunicar

Aprenderemos a exponer funciones como herramientas, conservar contexto conversacional y recuperar documentos mediante RAG. Incorporaremos controles de entrada, ejecución y salida, y comprobaremos qué situaciones cubren. Después publicaremos una API, conectaremos una interfaz web e instrumentaremos el agente para observarlo y evaluarlo.

La personalización se realizará mediante instrucciones, herramientas y documentos. No entrenaremos los pesos del modelo. Fine-tuning, coordinación multiagente y diseño avanzado de grafos quedan fuera del alcance práctico. Foundry es un bloque opcional. Así podremos dedicar tiempo a implementar, probar y comprender las capacidades principales.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “El alcance del curso”.
Bajo el encabezado “Capacidades que implementarás”, una cuadrícula de dos filas y cuatro columnas: “Herramientas”, “Memoria”, “RAG”, “Guardrails”, “API”, “Interfaz web”, “Observabilidad” y “Evaluación”. Iconos respectivos: llave inglesa, mensajes apilados, documentos con lupa, escudo abierto con condición, conexión, navegador, árbol de trazas y tabla de casos. No unir las tarjetas con flechas: son capacidades, no una secuencia.
En una franja separada: “Fuera del alcance práctico” y “Fine-tuning · Sistemas multiagente · Grafos avanzados”. Etiqueta independiente: “Foundry: bonus opcional”. No representar los guardrails como protección absoluta.
Pie discreto: “03 / 08”.
```

## 4. Recorrido de aprendizaje · 3 min

### Qué comunicar

Cada laboratorio añade una capacidad al proyecto. En M1 aprenderemos a interactuar con el modelo, estructurar respuestas y conectarlo con una herramienta. Cerraremos con un primer agente y evidencia de su funcionamiento.

En M2 ampliaremos herramientas, memoria y recuperación documental, y trabajaremos controles y pruebas ante errores. En M3 desplegaremos la aplicación, observaremos las ejecuciones y compararemos resultados para mejorarla. El curso culmina con la sustentación del proyecto integrador en S11.

Son once sesiones de seis horas: 66 horas lectivas. El bonus de Foundry queda fuera de ese total y permite explorar otro entorno comprobando qué componentes pueden reutilizarse y cuáles requieren adaptación.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “Un proyecto que crece durante el curso”.
Mostrar tres tarjetas grandes conectadas: “M1 · Fundamentos”, “Sesiones 1–3”, “Mensajes, prompts y herramientas”, resultado “Primer agente”; “M2 · Agentes avanzados”, “Sesiones 4–7”, “Memoria, RAG y guardrails”, resultado “Agente ampliado”; “M3 · Despliegue y evaluación”, “Sesiones 8–11”, “API, trazas y medición”, resultado “Proyecto integrador”.
Representar capacidades que se agregan al mismo prototipo. El recorrido principal termina en S11. Debajo, una tarjeta separada: “Bonus opcional · Microsoft Foundry”, con “Fuera de las 66 horas”. Franja de cierre: “11 sesiones × 6 horas = 66 horas”. No añadir ninguna sesión ni actividad intermedia adicional.
Pie discreto: “04 / 08”.
```

## 5. Casos de aplicación y equipos · 2 min

### Qué comunicar

Trabajaremos con telecomunicaciones, banca, retail y seguros. En telecomunicaciones atenderemos consultas de planes, consumo y reclamos; en banca, cuentas y operaciones sospechosas; en retail, pedidos, productos y solicitudes de devolución; en seguros, pólizas y reportes de siniestros.

La base técnica es compartida. Cambian datos, herramientas, vocabulario y límites. Formaremos equipos de dos: cada equipo propondrá un track y coordinaremos su distribución para representar las cuatro industrias. Las empresas son ficticias y los datos sintéticos. Cada equipo desarrollará su proyecto en su propio repositorio, laboratorio a laboratorio.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “Cuatro industrias, una base técnica compartida”.
Crear una cuadrícula 2 × 2 con igual jerarquía: “Telecomunicaciones”, “AndesMóvil”, “Planes · Consumo · Reclamos”, icono teléfono y antena; “Banca”, “Banco Inti”, “Cuentas · Operaciones sospechosas”, icono banco y lupa; “Retail”, “MercaSur”, “Pedidos · Productos · Devoluciones”, icono paquete y carrito; “Seguros”, “Andina Seguros”, “Pólizas · Reporte de siniestros”, icono vehículo y documento.
Pie: “Equipos de 2 personas · Un proyecto por equipo” y “Empresas ficticias y datos sintéticos”. No mostrar transferencias ejecutadas, devoluciones aprobadas, indemnizaciones autorizadas ni datos personales.
Pie discreto: “05 / 08”.
```

## 6. Metodología y dedicación · 3 min

### Qué comunicar

El curso ocupa seis semanas de calendario. Durante las primeras cinco tendremos dos encuentros en vivo por semana; en la sexta tendremos uno para cerrar con la sustentación final. La dedicación es de doce horas por semana en semanas 1–5 y seis horas en semana 6.

Cada sesión comprende una hora de preparación, tres horas en vivo con explicación, demos y práctica guiada, y dos horas posteriores de laboratorio. El total es de 66 horas: 33 en vivo y 33 asíncronas. Los laboratorios son incrementales y trabajaremos en parejas. La preparación S0 y el bonus de Foundry son adicionales y no forman parte de esas 66 horas.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “Cómo organizaremos el aprendizaje”.
Arriba, tres cifras: “6 semanas”, “11 sesiones” y “66 horas”.
En el centro, tres bloques conectados: “Antes de clase”, “1 hora”, “Conceptos y preparación”, icono libro; “En clase”, “3 horas”, “Explicación, demos y práctica”, icono pantalla; “Después de clase”, “2 horas”, “Laboratorio incremental”, icono terminal.
Debajo, dos franjas bien diferenciadas: “Semanas 1–5: 2 sesiones y 12 horas por semana” y “Semana 6: 1 sesión y 6 horas”. Cierre: “33 horas en vivo + 33 horas asíncronas”. Nota: “S0 y bonus: tiempo adicional”. No representar seis semanas idénticas ni indicar doce horas en la última semana. Las flechas expresan secuencia; los bloques no tienen que ocurrir el mismo día.
Pie discreto: “06 / 08”.
```

## 7. Evaluación y evidencias · 2 min

### Qué comunicar

La evaluación tiene tres hitos. A1 presenta un primer agente conectado con una API y evidencia de tres escenarios. El proyecto M2 integra herramientas, memoria, RAG y controles. El integrador presenta la aplicación desplegada, las trazas y los resultados de evaluación, con una sustentación ante evaluadores.

Cada hito representa el cien por ciento de la nota de su módulo; no son porcentajes que deban sumarse sobre una única nota global. Las rúbricas consideran funcionamiento, diseño, controles, evidencia y comunicación según lo enseñado en cada etapa. Mostrarán qué funciona, qué falla y cómo lo comprobaron. Las autoevaluaciones son habilitantes; el bonus no es ponderado.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “Evaluaremos lo que construyes y cómo lo demuestras”.
Mostrar tres columnas: “A1”, “Primer agente”, “API externa + tres escenarios”, “100 % del Módulo 1”; “Proyecto M2”, “Agente ampliado”, “Herramientas + memoria + RAG + controles”, “100 % del Módulo 2”; “Proyecto integrador”, “Aplicación desplegada”, “Trazas + evaluación + sustentación”, “100 % del Módulo 3”.
Debajo: “Criterios según la rúbrica de cada etapa” y “Funcionamiento · Diseño · Controles · Evidencia · Comunicación”. Pie: “Autoevaluaciones: habilitantes” y “Bonus: no ponderado”. No usar gráfico circular ni sumar los porcentajes de módulos distintos. Representar evidencia con pruebas y documentos, no con trofeos ni resultados inventados.
Pie discreto: “07 / 08”.
```

## 8. Próximos pasos: preparación S0 · 2 min

### Qué comunicar

El siguiente paso es completar S0 antes de la primera sesión en vivo. Reserven entre cuatro y cinco horas que pueden distribuir en varios días. Revisarán fundamentos de modelos de lenguaje y consultarán el glosario; después prepararán Python, el entorno y las cuentas necesarias.

Ejecutarán cuatro demos sobre tokens, variación de respuestas, embeddings y costo. Finalmente resolverán la autoevaluación con un mínimo de ochenta por ciento. La preparación es obligatoria, asíncrona y está fuera de las 66 horas lectivas. Si aparece un problema de acceso o configuración, comuníquenlo con anticipación para resolverlo antes de los laboratorios.

### Prompt para la imagen

```text
Crea una diapositiva educativa completa en español, horizontal 16:9, resolución 1536 × 864 o equivalente, legible al proyectarse en un aula.
Estilo técnico plano de aspecto vectorial. Fondo #F4F6F8, texto #1E293B, tarjetas blancas y acento #FF5733. Tipografía sans serif grande, iconos lineales consistentes, bordes redondeados, amplio espacio libre y márgenes seguros del 5 %. Sin fotografías, robots humanoides, 3D, sombras pesadas, logotipos comerciales ni métricas inventadas. No añadir textos distintos de los solicitados.

Título exacto: “Tu siguiente paso: completar la preparación S0”. Subtítulo: “Antes de la primera sesión en vivo”.
Diseñar una ruta numerada: “1 · Fundamentos de LLM”, icono libro; “2 · Python y entorno”, icono terminal; “3 · Cuentas y accesos”, texto “Hugging Face · Qdrant · Langfuse”, icono conexiones; “4 · Cuatro demos”, texto “Tokens · Temperatura · Embeddings · Costo”, icono ejecución; “5 · Autoevaluación”, icono checklist.
Destacar “Reserva 4–5 horas” y “Mínimo 80 %”. Pie: “Preparación obligatoria y asíncrona” y “Fuera de las 66 horas lectivas”. Mostrar tareas por completar, sin marcas de aprobación ni resultados obtenidos. Mantener una ruta visual fácil de seguir, con una acción inmediata al terminar la bienvenida.
Pie discreto: “08 / 08”.
```
