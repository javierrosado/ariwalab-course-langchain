# Prompts de imágenes — sesion-10-evaluacion-optimizacion

## IMG-M03-S10-001 — Evaluation

- **Objetivo pedagógico:** Comparar versiones con evidencia y límites de medición.
- **Composición:** Golden dataset se bifurca a Agente v1 y Agente v2. Cada uno entrega Respuesta, Tools, Contexto a Evaluadores. Evaluadores → Tabla comparativa → Decisión documentada. Rama de Casos no aplicables separada del conteo de aciertos. Pie: proxy léxico requiere revisión de fuente. No cifras de mejora inventadas.
- **Elementos y texto visible:** Golden dataset, Agente v1, Agente v2, Respuesta, Tools, Contexto, Evaluadores, Tabla comparativa, Decisión documentada, Casos no aplicables, Revisar fuente.
- **Flujo:** las relaciones direccionales descritas en composición son obligatorias.
- **Jerarquía:** título, mecanismo central, nota breve.
- **Iconos:** persona, chip, runtime, llave, cilindro, historial, documentos, árbol de trazas y checklist según corresponda.
- **Paleta:** fondo #F4F6F8; texto #1E293B; tarjetas #FFFFFF; acento #FF5733.
- **Formato:** 16:9; objetivo 1536 × 864 o equivalente; PNG.
- **Restricciones:** distinguir propuesta/ejecución; evitar cruces de flechas y exceso de texto.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, credenciales, tecnologías ajenas o métricas inventadas.
- **Archivo:** `01-evaluacion.png`.
- **Uso:** Recurso disponible para las diapositivas.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, target 1536x864 or equivalent. Finished PNG bitmap, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Concept: Evaluation. Pedagogical goal: Comparar versiones con evidencia y límites de medición. Composition and exact directional relationships: Golden dataset se bifurca a Agente v1 y Agente v2. Cada uno entrega Respuesta, Tools, Contexto a Evaluadores. Evaluadores → Tabla comparativa → Decisión documentada. Rama de Casos no aplicables separada del conteo de aciertos. Pie: proxy léxico requiere revisión de fuente. No cifras de mejora inventadas. Visible labels verbatim in Spanish: Golden dataset, Agente v1, Agente v2, Respuesta, Tools, Contexto, Evaluadores, Tabla comparativa, Decisión documentada, Casos no aplicables, Revisar fuente. Title: Evaluation. Visual hierarchy: title then main flow then one short explanatory note. Consistent icons: user outline, LLM chip, runtime square, tool wrench, database cylinder, history stacked cards, documents pages, observability tree, evaluation checklist. Solid arrows for execution/data and dashed for telemetry; keep arrows unambiguous and non-crossing. No photographs, humanoid robots, 3D, heavy shadows, gradients, stock imagery, extra technologies, real company logos, fabricated metrics, API keys, or paragraphs. Do not add components not requested. Clearly distinguish the model proposing and the runtime executing actions. This is a precise teaching diagram, not decorative art.
```

### Criterios visuales

Fondo opaco; representar LLM con chip. Incluir solo los nodos del mecanismo, sin leyendas
de iconos adicionales. Las flechas de datos y ejecución son sólidas; telemetría solo en
el diagrama de despliegue.

```text
Keep this Evaluation diagram and all labels/relationships exactly. Change ALL dashed arrows to solid arrows: they represent observed data, NOT telemetry. Remove the bottom-left legend entirely. Replace both small brain icons inside Agente v1 and Agente v2 with microchip icons matching the course LLM symbol. Keep all six outputs Respuesta, Tools, Contexto. Change bottom note to exactly: Proxy léxico: revisar fuente y afirmación. Change the X icon for Casos no aplicables to an em dash symbol so it is not confused with a failure. Keep fully opaque background and 16:9 composition. No other changes.
```
