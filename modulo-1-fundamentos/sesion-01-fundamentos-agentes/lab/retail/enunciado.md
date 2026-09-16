# L1 · Retail — MercaSur

Construyes el primer script de tu proyecto: `primer_contacto.py`. Endereza tu entorno primero
(parte 1 del `README.md` del laboratorio) y vuelve aquí para la parte 2.

## Tus 3 preguntas de dominio

Tu script debe hacerle al modelo estas 3 preguntas reales de un cliente de MercaSur,
imprimiendo pregunta y respuesta:

1. "¿Cuál es la política de cambios y devoluciones si mi producto llegó dañado?"
2. "¿Cuánto tiempo de garantía tienen los electrodomésticos que venden?"
3. "¿Qué hago si mi pedido no llega en la fecha que me estimaron?"

## Cómo estructurarlo

- Usa `comun.provider.get_chat_model()` — nunca instancies `ChatOpenAI` directamente.
- Usa `comun.prompts_industria.get_system_prompt()` para que el modelo responda con el
  vocabulario y los límites de MercaSur (viste este patrón en las demos 2 y 3 de `code/`).
- Guarda el archivo en `lab/retail/primer_contacto.py`.

## Qué deberías notar

Ninguna de las 3 respuestas viene de una política de devoluciones real: el modelo no tiene
ninguna herramienta todavía. Compáralas después, en la Sesión 5, con lo que responde tu agente
cuando por fin puede citar el documento real.

## Reto opcional · no evaluado

Hazle al modelo una cuarta pregunta:

> "¿En qué estado está mi pedido PED-00842?"

Ese estado solo existe en el sistema de pedidos de MercaSur — el modelo no puede saberlo. Anota
en 5 líneas qué estado inventó y con qué seguridad lo presentó. Guarda la nota: la retomas en la
Sesión 5 como el "antes" del RAG.
