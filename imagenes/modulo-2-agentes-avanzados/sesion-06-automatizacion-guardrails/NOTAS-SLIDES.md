# Speaker notes — Sesión 06

## Slide 01 — Guardrails

**ID:** IMG-M02-S06-001.

**Archivo:** `01-controles.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 6 — teoría y objetivos](../../../modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/README.md).

**Objetivo pedagógico:** Ubicar controles y explicar su cobertura acotada.

**Concepto principal:** Guardrails.

**Mensaje clave:** El control debe ejecutarse fuera del modelo y probarse.

**Explicación sugerida:** Ubicar controles antes de entrada, antes de ejecutar acciones y antes de salida. Distinguir patrón middleware de API nativa y declarar cobertura limitada.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Flujo: Entrada → Control de entrada → LLM. LLM propone Tool Call → Control de acción → Runtime ejecuta Tool → Resultado vuelve al LLM. Respuesta del LLM → Control de salida → Usuario. Nota inferior: cobertura limitada a condiciones implementadas. No mostrar autenticación ni aprobación humana como funcionalidad implementada.

**Ejemplo:** Una regex de DNI no detecta todas las formas de información personal.

**Ejemplo de industria:** Banco Inti: la API key del equipo no demuestra titularidad de una cuenta bancaria.

**Pregunta al alumno:** ¿Por qué confirmado_por_cliente=true propuesto por el LLM no demuestra aprobación humana?

**Error conceptual frecuente:** Confundir un control determinístico acotado con seguridad universal.

**Conexión con sesión anterior:** S5: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S7: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 6 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
