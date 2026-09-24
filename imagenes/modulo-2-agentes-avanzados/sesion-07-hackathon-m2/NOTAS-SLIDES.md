# Speaker notes — Sesión 07

## Slide 01 — Agentic Loop

**ID:** IMG-M01-S01-001.

**Archivo:** `../../modulo-1-fundamentos/sesion-01-fundamentos-agentes/01-agentic-loop.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 7 — teoría y objetivos](../../../modulo-2-agentes-avanzados/sesion-07-hackathon-m2/README.md).

**Objetivo pedagógico:** Separar propuesta del modelo y ejecución por el runtime.

**Concepto principal:** Agentic Loop.

**Mensaje clave:** El modelo propone; la aplicación ejecuta.

**Explicación sugerida:** Reutilizar el bucle para localizar dónde se inyectan fallos: entrada ambigua, tool sin dato, servicio caído y salida fuera de formato.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Usuario → Agente; dentro del agente: LLM → Runtime → Tool; Tool → API; resultado vuelve a LLM; LLM entrega respuesta a Usuario. Mostrar límite de iteraciones como borde del bucle.

**Ejemplo:** Con la tool fallando continuamente, contar llamadas y verificar el límite sin depender del texto exacto.

**Ejemplo de industria:** MercaSur: el servicio de pedidos cae y el agente debe informar el fallo sin inventar un envío.

**Pregunta al alumno:** ¿Qué invariante comprobarías aunque la redacción cambie?

**Error conceptual frecuente:** Confundir cinco repeticiones con una certificación de fiabilidad o las invariantes de pseudocódigo con métodos existentes.

**Conexión con sesión anterior:** S6: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S8: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 5 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
