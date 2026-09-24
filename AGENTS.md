# Instrucciones para mantener el curso

## Propósito y estructura

Curso en español de Agentic AI y LangChain para ingenieros de software: nivelación S0,
M1 (S1–S3), M2 (S4–S7), M3 (S8–S11), M4 (bonus Foundry).
Son 11 sesiones numeradas: 66 horas; el bonus no computa.
`comun/` concentra infraestructura; `simulador-industria/` implementa servicios sintéticos;
`recursos/` contiene datos, rúbricas y plantillas; `docente/` contiene guiones y verificadores.
Las soluciones de cada sesión son checkpoints incrementales. Inspeccionar el contenido de
`proyecto-final/` antes de describirlo como una aplicación completa.

## Fuentes de verdad

Leer [mapa](docs/COURSE-MAP.md), [glosario](docs/GLOSSARY.md),
[guía editorial](docs/CONTENT-GUIDELINES.md).
El código y sus pruebas determinan el comportamiento implementado; `docente/esqueletos/`
documenta el contrato pedagógico; `PLAN-CURRICULAR.md` fija horas y evaluaciones;
La guía docente y los checklists describen la preparación operativa de cada sesión.
Si estas fuentes contradicen entre sí, registrar evidencia, sin declarar una validación inexistente.
El contenido publicado se dirige al docente y al alumno. No incluir historia de creación,
bitácoras, códigos de decisiones internas, tareas para asistentes de IA ni informes de entrega.
La trazabilidad de los cambios permanece en Git. Conservar las atribuciones de autoría.

## Revisión pedagógica obligatoria

> Nunca modificar una sesión considerando únicamente ese archivo.

Antes de editar: revisar COURSE-MAP, GLOSSARY, sesión anterior, sesión actual, sesión
posterior, código, laboratorio y evaluación asociados. Para S0 y bonus usar las sesiones
adyacentes que existan. Mantener la cadena objetivo → teoría → ejemplo → lab → evaluación.
Un concepto futuro se anuncia con su sesión; una mención no equivale a una implementación.
No exigir en una rúbrica una capacidad todavía no enseñada. Conservar contenido técnico útil.

## Reglas técnicas y terminología

Usar `comun.provider` y `comun.settings`; no dispersar clientes ni secretos por los labs.
Conservar el stack y las versiones declaradas salvo necesidad demostrada. No introducir
tecnologías ni refactorizaciones ajenas al hallazgo. Distinguir demostración, pseudocódigo,
checkpoint ejecutable y resultado medido. No prometer un fallo o una mejora de un LLM en vivo.
LangChain 1.x tiene APIs propias de middleware: un wrapper Python no equivale a usarlas.
Confirmación propuesta por el modelo no demuestra aprobación humana autenticada.
Conservar Tool Calling, Structured Output, Middleware, Guardrail, Agentic Loop y
Human-in-the-loop cuando mejoran la precisión; consultar el glosario antes de crear sinónimos.

Las cuatro marcas son AndesMóvil (Telecomunicaciones/Telco), Banco Inti (Banca), MercaSur
(Retail) y Andina Seguros (Seguros). Datos sintéticos; no renombrar marcas ni forzar ejemplos.
El catálogo real del L4 tiene cuatro tools núcleo; L5 añade un retriever. No confundir
número de tools disponibles con número de iteraciones del agente.

No editar a mano `docente/especificacion-tools.md`, `simulador-industria/docs/REFERENCIA-API.md`
ni datos generados: modificar la fuente y regenerar con su script si corresponde.
Ejecutar verificadores pertinentes; diferenciar simulación de medición con servicios reales.
No publicar secretos, salidas con credenciales, ni resultados inventados.

## Git, trazabilidad y aprobación humana

Trabajar únicamente en `feature/curso-final` para esta revisión. Comprobar rama y estado
antes de editar. Conservar cambios previos del usuario y sus finales de línea; no incluirlos
accidentalmente en commits. Commits pequeños y semánticos.
Revisar diff contra `main`; no modificar ni fusionar `main`, borrar historial, hacer force
push ni squash automático. Preparar o crear PR hacia `main` sin aprobarlo ni hacer merge.

Consultar al autor sobre cambios pedagógicos o arquitectónicos importantes; no introducir
debates internos en el material de clase. Expresar límites técnicos como instrucciones verificables. La revisión y aprobación
humana del PR es necesaria para integrar. Esto no impide las correcciones y validaciones
ya autorizadas por el encargo. Despliegues y comunicaciones a terceros requieren alcance explícito.

## Gobernanza visual

Seguir `imagenes/DESIGN-SYSTEM.md` y `imagenes/CATALOGO-IMAGENES.md` cuando existan.
Cada imagen tiene ID, propósito, fuente, prompt reproducible, estado y notas para PPT.
Reutilizar arquitectura e iconografía. Evitar decoración. Validar texto, flechas, legibilidad
y correspondencia con el código antes de marcar GENERATED. Los pendientes se marcan
PENDING_GENERATION; no enlazar archivos inexistentes como si fueran imágenes finales.
