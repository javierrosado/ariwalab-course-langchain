# Speaker notes — Bonus

## Slide 01 — Arquitectura como evidencia de una decisión

**ID:** IMG-M03-S08-001.

**Archivo:** `../modulo-3-produccion/sesion-08-despliegue-hf-spaces/01-despliegue.png`; reutilización.

**Sección fuente:** [Contenido](../../modulo-4-plus-foundry/README.md).

**Objetivo pedagógico:** contrastar decisiones de arquitectura con sus requisitos.

**Concepto principal:** límites del sistema y portabilidad.

**Mensaje clave:** conservar una interfaz no demuestra conservar el comportamiento.

**Explicación sugerida:** Usar el diagrama como línea base HF que se compara con Foundry, no como arquitectura del host. Señalar las piezas que deben adaptarse: memoria, guardrails y compatibilidad de embeddings. La política de embeddings sigue en CONS-010.

**Elementos que debe señalar el docente:** límite HF Spaces, API y agente, servicios externos y telemetría.

**Ejemplo:** comparar un cambio de cliente de chat con un cambio de hosting del agente.

**Ejemplo de industria:** Andina Seguros necesita conservar recuperación de fuentes y límites de actuación al cambiar de plataforma.

**Pregunta al alumno:** ¿qué prueba necesitarías para afirmar que el nuevo despliegue conserva los controles?

**Error conceptual frecuente:** concluir equivalencia técnica por usar el mismo nombre de tool.

**Conexión con sesión anterior:** S11, defensa de decisiones y evidencia.

**Conexión con sesión posterior:** reflexión final y Curso 2 como alcance futuro, sin evaluación nueva en la troncal.

**Duración sugerida:** 5 min dentro del bloque previsto.

**Notas adicionales:** la imagen muestra HF como referencia, no certifica disponibilidad ni despliegue Foundry.
