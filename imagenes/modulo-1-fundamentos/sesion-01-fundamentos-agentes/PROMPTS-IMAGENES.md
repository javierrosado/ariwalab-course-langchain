# Prompts de imágenes — sesion-01-fundamentos-agentes

## IMG-M01-S01-001 — Agentic Loop

- **Objetivo pedagógico:** Separar propuesta del modelo y ejecución por el runtime.
- **Composición:** Usuario → Agente; dentro del agente: LLM → Runtime → Tool; Tool → API; resultado vuelve a LLM; LLM entrega respuesta a Usuario. Mostrar límite de iteraciones como borde del bucle.
- **Elementos y texto visible:** Usuario, Agente, LLM, Runtime, Tool, API, Resultado, Respuesta, Límite de iteraciones.
- **Flujo:** las relaciones direccionales descritas en composición son obligatorias.
- **Jerarquía:** título, mecanismo central, nota breve.
- **Iconos:** persona, chip, runtime, llave, cilindro, historial, documentos, árbol de trazas y checklist según corresponda.
- **Paleta:** fondo #F4F6F8; texto #1E293B; tarjetas #FFFFFF; acento #FF5733.
- **Formato:** 16:9; objetivo 1536 × 864 o equivalente; PNG.
- **Restricciones:** distinguir propuesta/ejecución; evitar cruces de flechas y exceso de texto.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, credenciales, tecnologías ajenas o métricas inventadas.
- **Archivo previsto:** `01-agentic-loop.png`.
- **Estado:** GENERATED. Revisada visualmente el 2026-09-24.

### Prompt completo enviado a la herramienta

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, target 1536x864 or equivalent. Finished PNG bitmap, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Concept: Agentic Loop. Pedagogical goal: Separar propuesta del modelo y ejecución por el runtime. Composition and exact directional relationships: Usuario → Agente; dentro del agente: LLM → Runtime → Tool; Tool → API; resultado vuelve a LLM; LLM entrega respuesta a Usuario. Mostrar límite de iteraciones como borde del bucle. Visible labels verbatim in Spanish: Usuario, Agente, LLM, Runtime, Tool, API, Resultado, Respuesta, Límite de iteraciones. Title: Agentic Loop. Visual hierarchy: title then main flow then one short explanatory note. Consistent icons: user outline, LLM chip, runtime square, tool wrench, database cylinder, history stacked cards, documents pages, observability tree, evaluation checklist. Solid arrows for execution/data and dashed for telemetry; keep arrows unambiguous and non-crossing. No photographs, humanoid robots, 3D, heavy shadows, gradients, stock imagery, extra technologies, real company logos, fabricated metrics, API keys, or paragraphs. Do not add components not requested. Clearly distinguish the model proposing and the runtime executing actions. This is a precise teaching diagram, not decorative art.
```

### Ajustes de aceptación y regeneración

Fondo opaco; representar LLM con chip. Incluir solo los nodos del mecanismo, sin leyendas
de iconos adicionales. Las flechas de datos y ejecución son sólidas; telemetría solo en
el diagrama de despliegue.

El contenedor Agente incluye LLM, Runtime y Tool; API queda fuera. Omitir historial, documentos, observabilidad y evaluación de esta vista inicial.
