# Prompts de imágenes — sesion-02-ecosistema-langchain

## IMG-M01-S02-001 — Structured Output

- **Objetivo pedagógico:** Distinguir validación estructural y recuperación acotada.
- **Composición:** Flujo horizontal: Consulta → Modelo + esquema → Validación Pydantic. De validación, rama válida → Objeto tipado; rama error → Wrapper: un reintento → Modelo + esquema. Error después del reintento → ExtraccionFallida. Nota: no prueba veracidad.
- **Elementos y texto visible:** Consulta, Modelo + esquema, Validación Pydantic, Objeto tipado, Error, Un reintento, ExtraccionFallida, Validez no es veracidad.
- **Flujo:** las relaciones direccionales descritas en composición son obligatorias.
- **Jerarquía:** título, mecanismo central, nota breve.
- **Iconos:** persona, chip, runtime, llave, cilindro, historial, documentos, árbol de trazas y checklist según corresponda.
- **Paleta:** fondo #F4F6F8; texto #1E293B; tarjetas #FFFFFF; acento #FF5733.
- **Formato:** 16:9; objetivo 1536 × 864 o equivalente; PNG.
- **Restricciones:** distinguir propuesta/ejecución; evitar cruces de flechas y exceso de texto.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, credenciales, tecnologías ajenas o métricas inventadas.
- **Archivo previsto:** `01-structured-output.png`.
- **Estado:** GENERATED. Revisada visualmente el 2026-09-24.

### Prompt completo enviado a la herramienta

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, target 1536x864 or equivalent. Finished PNG bitmap, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Concept: Structured Output. Pedagogical goal: Distinguir validación estructural y recuperación acotada. Composition and exact directional relationships: Flujo horizontal: Consulta → Modelo + esquema → Validación Pydantic. De validación, rama válida → Objeto tipado; rama error → Wrapper: un reintento → Modelo + esquema. Error después del reintento → ExtraccionFallida. Nota: no prueba veracidad. Visible labels verbatim in Spanish: Consulta, Modelo + esquema, Validación Pydantic, Objeto tipado, Error, Un reintento, ExtraccionFallida, Validez no es veracidad. Title: Structured Output. Visual hierarchy: title then main flow then one short explanatory note. Consistent icons: user outline, LLM chip, runtime square, tool wrench, database cylinder, history stacked cards, documents pages, observability tree, evaluation checklist. Solid arrows for execution/data and dashed for telemetry; keep arrows unambiguous and non-crossing. No photographs, humanoid robots, 3D, heavy shadows, gradients, stock imagery, extra technologies, real company logos, fabricated metrics, API keys, or paragraphs. Do not add components not requested. Clearly distinguish the model proposing and the runtime executing actions. This is a precise teaching diagram, not decorative art.
```

### Ajustes de aceptación y regeneración

Fondo opaco; representar LLM con chip. Incluir solo los nodos del mecanismo, sin leyendas
de iconos adicionales. Las flechas de datos y ejecución son sólidas; telemetría solo en
el diagrama de despliegue.

```text
Make exactly ONE icon change: replace the brain icon representing the model/LLM with a simple orange MICROCHIP icon outlined in dark navy, matching the canonical course LLM symbol. Preserve every word, arrow, layout, color and card from the input. No other changes. Opaque background.
```

Usar un único Modelo + esquema y un único Validador: Primer error → Un reintento → Modelo + esquema; Segundo error → ExtraccionFallida. El retorno no salta directamente a validación.
