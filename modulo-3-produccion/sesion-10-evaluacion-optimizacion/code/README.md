# Demos de la Sesión 10

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/01_dataset_langfuse.py` | Langfuse | Subir los 30 casos del track a Langfuse Datasets |
| 2 | `python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/02_evaluators.py` | No | Los 3 evaluators determinísticos corriendo sobre una respuesta |
| 3 | `python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/03_llm_as_judge.py` | `HF_TOKEN` | El juez sobre 10 casos ya puntuados, con las dos columnas lado a lado |
| 4 | `python modulo-3-produccion/sesion-10-evaluacion-optimizacion/code/04_ab_prompts.py` | `HF_TOKEN` | El mismo dataset contra dos versiones del prompt, con la tabla de salida |

## Qué deberías notar en cada una

**Demo 1 — Dataset en Langfuse.** Que las 30 filas ya existían desde la S2: hoy solo se suben a
un lugar donde se pueden correr experimentos repetibles sobre ellas.

**Demo 2 — Evaluators.** Que los 3 son verificables sin juicio: corre el script dos veces y
compara — el resultado es idéntico.

**Demo 3 — LLM-as-judge.** Cuántos desacuerdos hay entre el juez y el evaluator determinístico,
y en cuáles casos el juez se equivocó por verbosidad o autocomplacencia.

**Demo 4 — A/B de prompts.** La tabla comparativa v1 vs v2. Antes de celebrar una mejora, aplica
la regla del bloque 4 del README: ¿se sostiene en dos corridas? ¿se sabe qué la causó?

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `RuntimeError: Falta la variable LANGFUSE_PUBLIC_KEY` | Falta configurar Langfuse en `.env` | Revisa `.env.example` |
| Las demos 3 y 4 tardan o fallan | Cola o cuota del *inference provider* | Reduce el número de casos si necesitas una corrida rápida |
| Demo 4: v1 y v2 dan exactamente igual | El cambio de prompt no tocó ninguna de las consultas OTRO de la muestra | Normal con pocos casos; es parte de la lección del bloque 4 |
