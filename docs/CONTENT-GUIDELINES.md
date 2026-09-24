# Guía editorial y pedagógica

Audiencia: ingenieros de software/sistemas que empiezan con LLM y agentes. Explicar primero
el problema, después el mecanismo, sus límites y cómo observarlo en el código del curso.
Usar español claro, términos técnicos canónicos y ejemplos sintéticos de las cuatro industrias.

## Estructura de una sesión

Incluir prerrequisitos verificables, objetivos observables, conexión con el incremento anterior,
teoría, ejemplos, demos enlazadas, laboratorio, criterios de aceptación y siguiente paso.
Conservar las horas y pesos del plan. Las secciones usan encabezados únicos y enlaces a
títulos estables; evitar referencias numéricas que no correspondan al documento publicado.
Los guiones del docente, slides y quizzes deben corregirse junto con la teoría afectada.

## Exactitud y profundidad

Separar capacidades del modelo, decisiones de la aplicación y servicios externos. Un modelo
propone Tool Calls; el runtime valida y ejecuta. Una política escrita en un prompt no impone
una autorización. Una regex cubre patrones concretos, no todas las variantes de un ataque.
Una analogía debe declarar dónde deja de aplicar. No presentar parámetros, límites del plan
gratuito ni resultados de una medición anterior como garantías universales.

Cuando una API o un proveedor cambia, consultar documentación oficial y registrar fecha,
versión y alcance de la verificación. Las fórmulas de fiabilidad deben explicar sus supuestos.
Una salida válida según Pydantic puede ser semánticamente incorrecta.

## Código, tablas y ejemplos

Usar bloques con lenguaje (`python`, `bash`, `dotenv`) y marcar pseudocódigo o extractos.
Los ejemplos ejecutables deben indicar archivo, directorio de ejecución, dependencias y
servicios requeridos. No inventar métodos auxiliares como si fueran APIs existentes.
Las tablas sirven para comparar contratos, decisiones y trazabilidad; no sustituyen una
explicación causal. Los resultados de demo se registran como observados, nunca garantizados.
No ejecutar servicios externos para aparentar una validación offline.

## Laboratorios y evaluación

Cada lab consume el checkpoint anterior y entrega un incremento identificable. El alumno
construye en su repositorio; la solución se consulta después. Distinguir ejercicios, retos
opcionales y evaluaciones ponderadas. El banco de preguntas enlaza el instrumento original.
Las respuestas de opción múltiple se ocultan hasta la autocorrección.

Conservar pesos y umbrales aprobados. Medir sobre datos y ejecuciones identificables.
Separar casos no aplicables de aciertos, selección de tools de negocio de recuperación RAG,
y presencia de un dato de fundamentación semántica. Una prueba simulada valida el arnés;
no demuestra precisión del modelo. Reportar experimentos negativos con igual trazabilidad.

## Referencias y continuidad

Consultar [COURSE-MAP](COURSE-MAP.md) y [GLOSSARY](GLOSSARY.md) antes de editar.
Un enlace relativo parte del archivo que lo contiene. Comprobar archivos y anclas, excluyendo
plantillas dentro de bloques de código. Enlaces a fuentes externas deben ser portables en GitHub.
Las referencias a material futuro nombran sesión y alcance: introducción, implementación,
práctica o evaluación. No afirmar cobertura de Multi-agent si no existe actividad correspondiente.

## Visuales y mantenimiento

Usar una imagen solo si aclara una relación, flujo, arquitectura o decisión. Los prompts,
catálogo y speaker notes evolucionan con el contenido. Las notas explican el mensaje,
el ejemplo, la pregunta al alumno y el error frecuente, además de los elementos que señalar.

## Audiencia y contenido publicado

Publicar orientación para docentes y alumnos: conceptos, ejemplos, ejercicios, criterios de
evaluación y preparación de clase. Excluir historia de creación del repositorio, alternativas
editoriales descartadas, códigos de decisiones internas, conversaciones con asistentes e
informes de entrega o PR. Conservar atribuciones y límites técnicos relevantes para la práctica.
La historia de edición se consulta en Git; las decisiones de arquitectura que debe justificar
el alumno sí forman parte de las actividades.
