# Prompts de imágenes — sesion-08-despliegue-hf-spaces

## IMG-M03-S08-001 — Despliegue y observabilidad

- **Objetivo pedagógico:** Situar fronteras de API, agente y servicios gestionados.
- **Composición:** Cliente → caja HF Spaces que contiene FastAPI → Agente. GET /health público junto a FastAPI; POST /chat con X-API-Key hacia Agente. Agente se conecta por flechas separadas a Modelo remoto, Simulador API y Qdrant. Una flecha discontinua desde Agente pasa por Enmascarador y llega a Langfuse con etiqueta S9. No poner credenciales reales.
- **Elementos y texto visible:** Cliente, HF Spaces, FastAPI, Agente, GET /health, POST /chat, X-API-Key, Modelo remoto, Simulador API, Qdrant, Enmascarador, Langfuse, S9.
- **Flujo:** las relaciones direccionales descritas en composición son obligatorias.
- **Jerarquía:** título, mecanismo central, nota breve.
- **Iconos:** persona, chip, runtime, llave, cilindro, historial, documentos, árbol de trazas y checklist según corresponda.
- **Paleta:** fondo #F4F6F8; texto #1E293B; tarjetas #FFFFFF; acento #FF5733.
- **Formato:** 16:9; objetivo 1536 × 864 o equivalente; PNG.
- **Restricciones:** distinguir propuesta/ejecución; evitar cruces de flechas y exceso de texto.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, credenciales, tecnologías ajenas o métricas inventadas.
- **Archivo previsto:** `01-despliegue.png`.
- **Estado:** GENERATED. Revisada visualmente el 2026-09-24.

### Prompt completo enviado a la herramienta

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, target 1536x864 or equivalent. Finished PNG bitmap, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Concept: Despliegue y observabilidad. Pedagogical goal: Situar fronteras de API, agente y servicios gestionados. Composition and exact directional relationships: Cliente → caja HF Spaces que contiene FastAPI → Agente. GET /health público junto a FastAPI; POST /chat con X-API-Key hacia Agente. Agente se conecta por flechas separadas a Modelo remoto, Simulador API y Qdrant. Una flecha discontinua desde Agente pasa por Enmascarador y llega a Langfuse con etiqueta S9. No poner credenciales reales. Visible labels verbatim in Spanish: Cliente, HF Spaces, FastAPI, Agente, GET /health, POST /chat, X-API-Key, Modelo remoto, Simulador API, Qdrant, Enmascarador, Langfuse, S9. Title: Despliegue y observabilidad. Visual hierarchy: title then main flow then one short explanatory note. Consistent icons: user outline, LLM chip, runtime square, tool wrench, database cylinder, history stacked cards, documents pages, observability tree, evaluation checklist. Solid arrows for execution/data and dashed for telemetry; keep arrows unambiguous and non-crossing. No photographs, humanoid robots, 3D, heavy shadows, gradients, stock imagery, extra technologies, real company logos, fabricated metrics, API keys, or paragraphs. Do not add components not requested. Clearly distinguish the model proposing and the runtime executing actions. This is a precise teaching diagram, not decorative art.
```

### Ajustes de aceptación y regeneración

Fondo opaco; representar LLM con chip. Incluir solo los nodos del mecanismo, sin leyendas
de iconos adicionales. Las flechas de datos y ejecución son sólidas; telemetría solo en
el diagrama de despliegue.

```text
Critical architecture correction: extend the rounded HF Spaces boundary so it contains FastAPI AND Agente AND Enmascarador. The three cards are all in the same Space process. Leave Cliente, Modelo remoto, Simulador API, Qdrant and Langfuse OUTSIDE that boundary. Keep existing arrows and labels. Replace Qdrant wrench icon with database cylinder containing vector dots. Replace Simulador API wrench icon with endpoint connection icon. Replace Langfuse gear icon with tree of spans. Add small Público label to GET /health. Keep POST /chat and X-API-Key. Keep diagram fully opaque 16:9, same colors and flat style. No extra components. Reduce title font if needed for margins.
```
