# Speaker notes — Sesión 01

## Slide 01 — Agentic Loop

**ID:** IMG-M01-S01-001.

**Archivo:** `01-agentic-loop.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 1 — teoría y objetivos](../../../modulo-1-fundamentos/sesion-01-fundamentos-agentes/README.md).

**Objetivo pedagógico:** Separar propuesta del modelo y ejecución por el runtime.

**Concepto principal:** Agentic Loop.

**Mensaje clave:** El modelo propone; la aplicación ejecuta.

**Explicación sugerida:** Distinguir llamada al modelo de un sistema que ejecuta acciones. Recorrer solo el bucle; anunciar tools S3, historial S5 y controles S6.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Usuario → Agente; dentro del agente: LLM → Runtime → Tool; Tool → API; resultado vuelve a LLM; LLM entrega respuesta a Usuario. Mostrar límite de iteraciones como borde del bucle.

**Ejemplo:** Comparar una respuesta sin consultar sistemas con una consulta cuyo resultado vuelve al modelo.

**Ejemplo de industria:** AndesMóvil: preguntar por el plan de una línea; el dato debe salir del simulador.

**Pregunta al alumno:** ¿Qué componente puede ejecutar la consulta HTTP?

**Error conceptual frecuente:** Creer que generar una Tool Call significa haber ejecutado la herramienta.

**Conexión con sesión anterior:** S0: fundamentos de LLM y entorno.

**Conexión con sesión posterior:** S2: mensajes y contratos.

**Duración sugerida:** 4 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Conservar el asset aprobado.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
