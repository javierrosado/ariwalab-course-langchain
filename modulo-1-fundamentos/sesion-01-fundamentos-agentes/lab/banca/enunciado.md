# L1 · Banca — Banco Inti

Construyes el primer script de tu proyecto: `primer_contacto.py`. Endereza tu entorno primero
(parte 1 del `README.md` del laboratorio) y vuelve aquí para la parte 2.

## Tus 3 preguntas de dominio

Tu script debe hacerle al modelo estas 3 preguntas reales de un cliente de Banco Inti,
imprimiendo pregunta y respuesta:

1. "¿Cuánto cobra el banco por mantenimiento de cuenta de ahorros y por una transferencia
   interbancaria?"
2. "¿Qué pasos sigue el banco si detecta una operación sospechosa en mi tarjeta?"
3. "¿Qué cubre exactamente el seguro de protección de mi tarjeta de crédito?"

## Cómo estructurarlo

- Usa `comun.provider.get_chat_model()` — nunca instancies `ChatOpenAI` directamente.
- Usa `comun.prompts_industria.get_system_prompt()` para que el modelo responda con el
  vocabulario y los límites de Banco Inti (viste este patrón en las demos 2 y 3 de `code/`).
- Guarda el archivo en `lab/banca/primer_contacto.py`.

## Qué deberías notar

Ninguna de las 3 respuestas viene de un tarifario ni de una política real: el modelo no tiene
ninguna herramienta todavía. En banca, un número mal dicho no es una imprecisión — es un
problema. Es justo la razón por la que este track exige guardrails desde el diseño.

## Reto opcional · no evaluado

Hazle al modelo una cuarta pregunta:

> "¿Cuál es el saldo disponible de la cuenta 191-2233445-0-11?"

Ese dato solo existe en el core bancario de Banco Inti — el modelo no puede saberlo. Anota en
5 líneas qué cifra inventó y con qué seguridad la presentó. Guarda la nota: la retomas en la
Sesión 5 como el "antes" del RAG.
