# Demos de la Sesión 7

Ejecuta siempre **desde la raíz del curso**. Las demos 1 y 3 usan el agente de referencia de la
Sesión 6 (telecomunicaciones, con guardrails ya enganchados); la demo 2 es lógica pura.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python .../code/01_por_que_falla_assert.py` | `HF_TOKEN` | La misma pregunta, dos respuestas distintas: por qué `assert ==` falla |
| 2 | `python .../code/02_invariantes.py` | No | Las funciones invariante en aislamiento, antes de usarlas contra un agente real |
| 3 | `python .../code/03_repetir_y_medir.py` | `HF_TOKEN` | 5 repeticiones de la misma pregunta: una prueba que no siempre pasa está midiendo |

## Qué deberías notar en cada una

**Demo 1.** Las dos respuestas casi seguro difieren en el texto exacto, pero ambas deberían
mencionar el dato correcto. Esa es la diferencia entre probar la forma y probar el contenido.

**Demo 2.** Cada invariante comprueba una sola propiedad (hay un DNI sin enmascarar, hay una
tarjeta completa, se menciona una palabra clave). Son las mismas funciones que vas a usar contra
tu agente real en `solucion/<track>/tests/invariantes.py`.

**Demo 3.** Si el resultado no es 5/5, no borres el intento fallido ni lo repitas hasta que
salga bien: **anótalo**. Ese es exactamente el tipo de dato que va en tu `INFORME-L7.md`.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `ModuleNotFoundError: agent` | No se encuentra el agente de la S6 | Verifica que `sesion-06-automatizacion-guardrails/solucion/telecomunicaciones/agent.py` exista |
| Las 5 repeticiones de la demo 3 tardan | Cola del *inference provider* | Normal; no gastes más cuota reintentando en bucle |
| `OpenAIInvalidRequestError` / el modelo no responde nada | Incidente del proveedor de HF, no de tu código | Reintenta más tarde; verifica con `python -m comun.check_stack --solo-modelo` |
