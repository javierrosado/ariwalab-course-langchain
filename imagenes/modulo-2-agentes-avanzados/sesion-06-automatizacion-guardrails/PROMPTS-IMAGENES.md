# Prompts de imágenes — sesion-06-automatizacion-guardrails

## IMG-M02-S06-001 — Guardrails

- **Objetivo pedagógico:** Ubicar controles y explicar su cobertura acotada.
- **Composición:** Flujo: Entrada → Control de entrada → LLM. LLM propone Tool Call → Control de acción → Runtime ejecuta Tool → Resultado vuelve al LLM. Respuesta del LLM → Control de salida → Usuario. Nota inferior: cobertura limitada a condiciones implementadas. No mostrar autenticación ni aprobación humana como funcionalidad implementada.
- **Elementos y texto visible:** Entrada, Control de entrada, LLM, Tool Call, Control de acción, Runtime, Tool, Resultado, Control de salida, Usuario, Cobertura limitada.
- **Flujo:** las relaciones direccionales descritas en composición son obligatorias.
- **Jerarquía:** título, mecanismo central, nota breve.
- **Iconos:** persona, chip, runtime, llave, cilindro, historial, documentos, árbol de trazas y checklist según corresponda.
- **Paleta:** fondo #F4F6F8; texto #1E293B; tarjetas #FFFFFF; acento #FF5733.
- **Formato:** 16:9; objetivo 1536 × 864 o equivalente; PNG.
- **Restricciones:** distinguir propuesta/ejecución; evitar cruces de flechas y exceso de texto.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, credenciales, tecnologías ajenas o métricas inventadas.
- **Archivo:** `01-controles.png`.
- **Uso:** Recurso disponible para las diapositivas.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, target 1536x864 or equivalent. Finished PNG bitmap, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Concept: Guardrails. Pedagogical goal: Ubicar controles y explicar su cobertura acotada. Composition and exact directional relationships: Flujo: Entrada → Control de entrada → LLM. LLM propone Tool Call → Control de acción → Runtime ejecuta Tool → Resultado vuelve al LLM. Respuesta del LLM → Control de salida → Usuario. Nota inferior: cobertura limitada a condiciones implementadas. No mostrar autenticación ni aprobación humana como funcionalidad implementada. Visible labels verbatim in Spanish: Entrada, Control de entrada, LLM, Tool Call, Control de acción, Runtime, Tool, Resultado, Control de salida, Usuario, Cobertura limitada. Title: Guardrails. Visual hierarchy: title then main flow then one short explanatory note. Consistent icons: user outline, LLM chip, runtime square, tool wrench, database cylinder, history stacked cards, documents pages, observability tree, evaluation checklist. Solid arrows for execution/data and dashed for telemetry; keep arrows unambiguous and non-crossing. No photographs, humanoid robots, 3D, heavy shadows, gradients, stock imagery, extra technologies, real company logos, fabricated metrics, API keys, or paragraphs. Do not add components not requested. Clearly distinguish the model proposing and the runtime executing actions. This is a precise teaching diagram, not decorative art.
```

### Criterios visuales

Fondo opaco; representar LLM con chip. Incluir solo los nodos del mecanismo, sin leyendas
de iconos adicionales. Las flechas de datos y ejecución son sólidas; telemetría solo en
el diagrama de despliegue.

```text
Keep this diagram's main orange execution flow exactly. REMOVE ALL dark dashed arrows and remove the two-item arrow legend at bottom left. This diagram has NO telemetry; do not add any telemetry. Replace the icon in Usuario with the outline of a PERSON (head and shoulders); keep label Usuario. Keep coverage-limited note. Solid opaque pale grey background. Only requested edits.
```
