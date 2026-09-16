# L1 · Seguros — Andina Seguros

Construyes el primer script de tu proyecto: `primer_contacto.py`. Endereza tu entorno primero
(parte 1 del `README.md` del laboratorio) y vuelve aquí para la parte 2.

## Tus 3 preguntas de dominio

Tu script debe hacerle al modelo estas 3 preguntas reales de un cliente de Andina Seguros,
imprimiendo pregunta y respuesta:

1. "¿Qué cubre el SOAT en caso de un accidente de tránsito?"
2. "¿Cuáles son los pasos para reportar un siniestro vehicular?"
3. "¿Hasta cuántas UIT cubre el SOAT por gastos de sepelio?"

## Cómo estructurarlo

- Usa `comun.provider.get_chat_model()` — nunca instancies `ChatOpenAI` directamente.
- Usa `comun.prompts_industria.get_system_prompt()` para que el modelo responda con el
  vocabulario y los límites de Andina Seguros (viste este patrón en las demos 2 y 3 de `code/`).
- Guarda el archivo en `lab/seguros/primer_contacto.py`.

## Qué deberías notar

Presta especial atención a la pregunta 3: es el mismo caso de la pregunta 4 de la autoevaluación
de la Sesión 0, donde el SOAT cubre **1 UIT** por sepelio, no 2. Compara la cifra que da tu
modelo con la real — sin RAG todavía, es una moneda al aire. Ninguna de las 3 respuestas viene
del condicionado real: el modelo no tiene ninguna herramienta todavía.

## Reto opcional · no evaluado

Hazle al modelo una cuarta pregunta:

> "¿En qué estado está el siniestro SIN-2026-0341?"

Ese estado solo existe en el sistema de siniestros de Andina Seguros — el modelo no puede
saberlo. Anota en 5 líneas qué estado inventó y con qué seguridad lo presentó. Guarda la nota:
la retomas en la Sesión 5 como el "antes" del RAG.
