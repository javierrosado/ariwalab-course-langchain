# Speaker notes — Sesión 11

## Slide 01 — Despliegue y observabilidad

**ID:** IMG-M03-S08-001.

**Archivo:** `../sesion-08-despliegue-hf-spaces/01-despliegue.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 11 — teoría y objetivos](../../../modulo-3-produccion/sesion-11-sustentacion-final/README.md).

**Objetivo pedagógico:** Situar fronteras de API, agente y servicios gestionados.

**Concepto principal:** Despliegue y observabilidad.

**Mensaje clave:** El endpoint del agente coordina servicios externos; las trazas son otra salida.

**Explicación sugerida:** Usar la arquitectura para sustentar alternativas, criterios y consecuencias. Explicar que SSE fragmenta la salida después de validar, sin generación token a token.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Cliente → caja HF Spaces que contiene FastAPI → Agente. GET /health público junto a FastAPI; POST /chat con X-API-Key hacia Agente. Agente se conecta por flechas separadas a Modelo remoto, Simulador API y Qdrant. Una flecha discontinua desde Agente pasa por Enmascarador y llega a Langfuse con etiqueta S9. No poner credenciales reales.

**Ejemplo:** Ante reinicio del Space, el historial por proceso desaparece; explicar ese límite y la evidencia de contingencia.

**Ejemplo de industria:** MercaSur: mostrar consulta de pedido, política recuperada y salida validada desde el cliente web.

**Pregunta al alumno:** ¿Qué decisión defenderías si te preguntan por memoria durable o aprobación humana?

**Error conceptual frecuente:** Presentar el checkpoint didáctico como despliegue industrial completo.

**Conexión con sesión anterior:** S10: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** Bonus opcional: portabilidad y límites.

**Duración sugerida:** 5 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
