# Speaker notes — Sesión 04

## Slide 01 — Agentic Loop

**ID:** IMG-M01-S01-001.

**Archivo:** `../../modulo-1-fundamentos/sesion-01-fundamentos-agentes/01-agentic-loop.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 4 — teoría y objetivos](../../../modulo-2-agentes-avanzados/sesion-04-tools-multiples/README.md).

**Objetivo pedagógico:** Separar propuesta del modelo y ejecución por el runtime.

**Concepto principal:** Agentic Loop.

**Mensaje clave:** El modelo propone; la aplicación ejecuta.

**Explicación sugerida:** La tarjeta Tool ahora representa una selección entre cuatro herramientas de negocio. El número de herramientas no determina las vueltas del bucle.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Usuario → Agente; dentro del agente: LLM → Runtime → Tool; Tool → API; resultado vuelve a LLM; LLM entrega respuesta a Usuario. Mostrar límite de iteraciones como borde del bucle.

**Ejemplo:** Dos docstrings ambiguas pueden causar confusión aunque ambas funciones sean correctas.

**Ejemplo de industria:** Andina Seguros: diferenciar consulta de póliza y apertura de expediente.

**Pregunta al alumno:** ¿Qué evidencia usarías para cambiar una docstring?

**Error conceptual frecuente:** Suponer que cuatro herramientas siempre superan a cinco en cualquier modelo.

**Conexión con sesión anterior:** S3: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S5: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 4 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
