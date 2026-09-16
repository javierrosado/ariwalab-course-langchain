# L1 · Telecomunicaciones — AndesMóvil

Construyes el primer script de tu proyecto: `primer_contacto.py`. Endereza tu entorno primero
(parte 1 del `README.md` del laboratorio) y vuelve aquí para la parte 2.

## Tus 3 preguntas de dominio

Tu script debe hacerle al modelo estas 3 preguntas reales de un cliente de AndesMóvil,
imprimiendo pregunta y respuesta:

1. "¿Cuáles son los planes postpago disponibles y cuánto cuesta cada uno?"
2. "Si supero mi bono de datos contratado, ¿qué pasa con mi velocidad y me cobran algo extra?"
3. "¿Cuál es el procedimiento para portar mi número a otro operador?"

## Cómo estructurarlo

- Usa `comun.provider.get_chat_model()` — nunca instancies `ChatOpenAI` directamente.
- Usa `comun.prompts_industria.get_system_prompt()` para que el modelo responda con el
  vocabulario y los límites de AndesMóvil (viste este patrón en las demos 2 y 3 de `code/`).
- Guarda el archivo en `lab/telecomunicaciones/primer_contacto.py`.

## Qué deberías notar

Ninguna de las 3 respuestas viene de un tarifario real: el modelo no tiene ninguna herramienta
todavía. Van a sonar convincentes igual — ese es justo el problema que rompe la demo del
antipatrón (`README.md` de la sesión, sección 2).

## Reto opcional · no evaluado

Hazle al modelo una cuarta pregunta:

> "¿Cuántos GB ha consumido este mes la línea 987654321?"

Esa cifra solo existe en el sistema de facturación de AndesMóvil — el modelo no puede saberla.
Anota en 5 líneas qué número inventó y con qué seguridad lo presentó. Guarda la nota: la
retomas en la Sesión 5 como el "antes" del RAG.
