# Bonus — El mismo agente en Microsoft Foundry

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/bonus-foundry.md`. Uso opcional: el
> bloque es asíncrono y autoguiado, sin clase en vivo — estas diapositivas sirven para la
> asesoría de 1 h opcional que menciona `docente/cronograma.md`, no para un guion de aula.

---

## Bonus · El mismo agente en Foundry
- Asíncrono, liberado al cerrar la S11 · no ponderado
- ⚠️ Primera y única vez que el curso menciona una tarjeta de crédito (Vía A) — Vía B disponible

---

## La lección, en una línea
- `.env`: `AI_PROVIDER=huggingface` → `AI_PROVIDER=foundry`
- El cliente de chat conserva su interfaz; el host requiere un grafo compatible
- Revisar comportamiento, embeddings, memoria y guardrails (CONS-009/010)

---

## El modelo de recursos de Azure
- Suscripción → grupo de recursos → proyecto de Foundry → deployment del modelo

---

## El momento del bloque — el switch
- Batería de 5 consultas contra HF → anotar
- Configurar cliente Foundry y resolver compatibilidad de embeddings antes del RAG
- Misma batería contra Foundry → anotar y comparar
- ¿Qué habría hecho falta cambiar si el agente hubiera instanciado `ChatOpenAI` en cada archivo?

---

## *Hosted agent* y el protocolo Responses
- `ResponsesHostServer` envuelve un grafo de LangGraph
- Qué SÍ porta sin cambios (tools, retriever, prompts) y qué NO (guardrails escritos a mano)

---

## El cuadro comparativo — 7 dimensiones
- Latencia · costo · calidad de respuesta · soberanía del dato · portabilidad · curva de puesta
  en marcha · dependencia del proveedor
- Sin ganador predeterminado: el objetivo es saber en qué contexto elegir cada una
