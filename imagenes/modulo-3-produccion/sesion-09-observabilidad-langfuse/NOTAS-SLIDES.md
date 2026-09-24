# Speaker notes — Sesión 09

## Slide 01 — Despliegue y observabilidad

**ID:** IMG-M03-S08-001.

**Archivo:** `../sesion-08-despliegue-hf-spaces/01-despliegue.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 9 — teoría y objetivos](../../../modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md).

**Objetivo pedagógico:** Situar fronteras de API, agente y servicios gestionados.

**Concepto principal:** Despliegue y observabilidad.

**Mensaje clave:** El endpoint del agente coordina servicios externos; las trazas son otra salida.

**Explicación sugerida:** Reutilizar la arquitectura y recorrer la salida de telemetría por el enmascarador. Verificar la jerarquía real antes de asumir un único árbol por conversación.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Cliente → caja HF Spaces que contiene FastAPI → Agente. GET /health público junto a FastAPI; POST /chat con X-API-Key hacia Agente. Agente se conecta por flechas separadas a Modelo remoto, Simulador API y Qdrant. Una flecha discontinua desde Agente pasa por Enmascarador y llega a Langfuse con etiqueta S9. No poner credenciales reales.

**Ejemplo:** Comparar tiempo de llamadas al modelo y tiempo del retriever en la evidencia real.

**Ejemplo de industria:** AndesMóvil: enmascarar el número de teléfono antes de exportar la traza.

**Pregunta al alumno:** ¿Dónde podrían salir datos personales además de la respuesta visible?

**Error conceptual frecuente:** Confundir run_name compartido con una traza padre común y p95 con máximo universal.

**Conexión con sesión anterior:** S8: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S10: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 5 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Reutilización del mismo asset; no regenerar otra arquitectura.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
