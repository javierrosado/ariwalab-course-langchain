# Demos de la Sesión 3

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado. Usan
`DATA_SOURCE=csv` (el valor por defecto), así que no necesitas el simulador desplegado para
correrlas — el Laboratorio 3 sí lo necesita, con `DATA_SOURCE=api`.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python .../code/01_tool_simple.py` | No | `@tool` + `args_schema`, invocada directamente desde Python |
| 2 | `python .../code/02_binding.py` | `HF_TOKEN` | **La demo de la sesión**: `bind_tools()` y el `tool_call` sin ejecutarlo |
| 3 | `python .../code/03_bucle_react_manual.py` | `HF_TOKEN` | El bucle ReAct en ~20 líneas, con tope de iteraciones |
| 4 | `python .../code/04_create_agent.py` | `HF_TOKEN` | Lo mismo en 3 líneas, con `create_agent()` |

## Qué deberías notar en cada una

**Demo 1.** Que una tool decorada con `@tool` sigue siendo una función normal. El modelo no le
agrega ninguna capacidad nueva: solo decide cuándo llamarla.

**Demo 2 — la demo de la sesión.** El `RuntimeError` dentro de la tool nunca se dispara. Eso
demuestra, sin ambigüedad, que el modelo solo propuso la llamada — nadie la ejecutó.

**Demo 3.** El "razonamiento" del agente es un `while` común, con un tope explícito. No hay
ninguna magia adicional: es exactamente el código que tú controlas.

**Demo 4.** La traza de mensajes es idéntica a la de la demo 3 (Human → AIMessage con
tool_calls → ToolMessage → AIMessage final). `create_agent()` no razona distinto: te ahorra
escribir el bucle.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `401 Unauthorized` | Token sin permiso de inferencia | Regenera el token de Hugging Face |
| El modelo no llama a la tool en la demo 2 | Puede pasar: reformula la pregunta o vuelve a correr | Es varianza normal del modelo, no un error de tu código |
| `ModuleNotFoundError: langchain.agents` | Versión de `langchain` desactualizada | `pip install -r requirements.txt` de nuevo |
