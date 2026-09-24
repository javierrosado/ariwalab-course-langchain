# Speaker notes — Sesión 02

## Slide 01 — Structured Output

**ID:** IMG-M01-S02-001.

**Archivo:** `01-structured-output.png`. Consultar estado en el catálogo antes de insertar en PPT.

**Sección fuente:** [Sesión 2 — teoría y objetivos](../../../modulo-1-fundamentos/sesion-02-ecosistema-langchain/README.md).

**Objetivo pedagógico:** Distinguir validación estructural y recuperación acotada.

**Concepto principal:** Structured Output.

**Mensaje clave:** El esquema valida la forma; el wrapper administra errores.

**Explicación sugerida:** Separar contrato estructural de clasificación correcta. Señalar que Pydantic valida y que el wrapper administra el presupuesto de reintentos.

**Elementos que debe señalar el docente:** recorrer los nodos y flechas del mecanismo en
orden; detenerse en la frontera que cambia en esta sesión. Flujo horizontal: Consulta → Modelo + esquema → Validación Pydantic. De validación, rama válida → Objeto tipado; rama error → Wrapper: un reintento → Modelo + esquema. Error después del reintento → ExtraccionFallida. Nota: no prueba veracidad.

**Ejemplo:** Una categoría fuera del Enum causa error; una categoría permitida pero equivocada pasa validación.

**Ejemplo de industria:** Banco Inti: una consulta de saldo puede tener esquema válido y una intención equivocada.

**Pregunta al alumno:** ¿Un objeto Pydantic válido demuestra que la intención fue bien clasificada?

**Error conceptual frecuente:** Atribuir al wrapper una validación que ya hace la integración Pydantic.

**Conexión con sesión anterior:** S1: retomar el incremento anterior del COURSE-MAP.

**Conexión con sesión posterior:** S3: ubicar el incremento siguiente del COURSE-MAP.

**Duración sugerida:** 5 min dentro del bloque existente; no agrega tiempo al guion.

**Notas adicionales:** Conservar el asset aprobado.
Usar el código y las limitaciones del reporte CONS como respaldo. Las cifras que muestre
el docente deben proceder de una ejecución identificada; esta imagen no aporta mediciones.
