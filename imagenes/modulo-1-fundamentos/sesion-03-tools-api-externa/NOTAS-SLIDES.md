# Speaker notes — Sesión 03

## Slide 01 — Agentic Loop

**ID:** IMG-M01-S01-001.

**Archivo:** `../sesion-01-fundamentos-agentes/01-agentic-loop.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 3 — teoría y objetivos](../../../modulo-1-fundamentos/sesion-03-tools-api-externa/README.md).

**Objetivo pedagógico:** Separar propuesta del modelo y ejecución por el runtime.

**Concepto principal:** Agentic Loop.

**Mensaje clave:** El modelo propone; la aplicación ejecuta.

**Explicación sugerida:** Volver al mismo bucle de S1 y nombrar AIMessage.tool_calls y ToolMessage. Mostrar la demo 3 manual y después create_agent.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Usuario → Agente; dentro del agente: LLM → Runtime → Tool; Tool → API; resultado vuelve a LLM; LLM entrega respuesta a Usuario. Mostrar límite de iteraciones como borde del bucle.

**Ejemplo:** Una tool de lectura consulta la API; la observación se incorpora como mensaje tool.

**Ejemplo de industria:** MercaSur: track_order consulta un pedido; todavía no se crean devoluciones.

**Pregunta al alumno:** ¿Qué pasa si la API no responde pero el modelo sigue proponiendo llamadas?

**Error conceptual frecuente:** Confundir el JSON propuesto con el resultado real de la API.

**Conexión con sesión anterior:** S2: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S4: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 5 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
