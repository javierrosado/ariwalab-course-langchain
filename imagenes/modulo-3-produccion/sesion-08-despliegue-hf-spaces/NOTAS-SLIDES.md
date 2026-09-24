# Speaker notes — Sesión 08

## Slide 01 — Despliegue y observabilidad

**ID:** IMG-M03-S08-001.

**Archivo:** `01-despliegue.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 8 — teoría y objetivos](../../../modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md).

**Objetivo pedagógico:** Situar fronteras de API, agente y servicios gestionados.

**Concepto principal:** Despliegue y observabilidad.

**Mensaje clave:** El endpoint del agente coordina servicios externos; las trazas son otra salida.

**Explicación sugerida:** Señalar el límite HF Spaces que contiene API y agente. /health comprueba disponibilidad del proceso según el contrato del curso; /chat exige clave. Langfuse se anticipa para S9.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Cliente → caja HF Spaces que contiene FastAPI → Agente. GET /health público junto a FastAPI; POST /chat con X-API-Key hacia Agente. Agente se conecta por flechas separadas a Modelo remoto, Simulador API y Qdrant. Una flecha discontinua desde Agente pasa por Enmascarador y llega a Langfuse con etiqueta S9. No poner credenciales reales.

**Ejemplo:** Cliente invoca el mismo agente que antes corría en terminal, ahora por una API pública.

**Ejemplo de industria:** Andina Seguros: el endpoint envuelve herramientas de pólizas y recuperación de documentos.

**Pregunta al alumno:** ¿Qué servicios pueden fallar aunque /health responda?

**Error conceptual frecuente:** Creer que publicar FastAPI vuelve persistente la memoria o autentica a cada cliente final.

**Conexión con sesión anterior:** S7: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S9: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 5 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
