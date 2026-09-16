# Demos de la Sesión 6

Ninguna de las 4 demos requiere `HF_TOKEN`: los guardrails son código (regex y reglas), no
llamadas al modelo — es justo el punto central de la sesión (`README.md`, bloque 1). Ejecuta
siempre **desde la raíz del curso**.

| Demo | Comando | Qué demuestra |
|------|---------|----------------|
| 1 | `python .../code/01_guardrail_entrada.py` | Detección de inyección y enmascarado de PII antes del modelo |
| 2 | `python .../code/02_guardrail_accion.py` | Bloqueo de una tool de escritura no autorizada o sin confirmar |
| 3 | `python .../code/03_guardrail_salida.py` | Un DNI que se coló en la respuesta se enmascara; una promesa prohibida se reemplaza |
| 4 | `python .../code/04_middleware.py` | Los tres enganchados alrededor de un agente simulado, sin tocar su lógica |

## Qué deberías notar en cada una

**Demo 1.** Un mensaje legítimo con PII (el cliente dando su propio DNI) pasa al modelo, pero se
enmascara en lo que queda en logs — enmascarar para auditoría no es lo mismo que bloquear.

**Demo 2.** El guardrail de acción no confía en que el modelo "elija bien": evalúa la acción
propuesta sin importar qué la originó.

**Demo 3.** El guardrail de salida reemplaza, no solo avisa. Compáralo con un guardrail que
"solo registra la filtración": ese no protege al usuario final.

**Demo 4.** `fake_agent()` no cambia entre el segundo y el tercer mensaje — lo que cambia es qué
guardrail actúa. Eso es exactamente lo que significa "middleware": interceptar sin reescribir.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` en la demo 4 | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| Un ataque nuevo no se detecta | El patrón no está en `INJECTION_PATTERNS` | Amplía la lista — es exactamente el trabajo del laboratorio |
