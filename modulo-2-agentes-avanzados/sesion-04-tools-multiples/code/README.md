# Demos de la Sesión 4

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python modulo-2-agentes-avanzados/sesion-04-tools-multiples/code/01_multi_tool.py` | `HF_TOKEN` | Un agente con las 4 tools del track elige distinto según la pregunta |
| 2 | `python modulo-2-agentes-avanzados/sesion-04-tools-multiples/code/02_matriz_didactica.py` | `HF_TOKEN` | 5 consultas y su matriz, en 30 segundos — la lectura antes del instrumento completo |
| 3 | `python modulo-2-agentes-avanzados/sesion-04-tools-multiples/code/03_tope_iteraciones.py` | No | El mismo agente con y sin tope de iteraciones ante fallos repetidos |

Las demos 1 y 2 usan la implementación de referencia del docente
(`proyecto-final/telecomunicaciones/`) a propósito — son demos del docente, no tu Laboratorio 4.
La demo 3 no llama a ningún modelo real: simula el mecanismo con un "modelo terco" determinista,
para enseñar el tope de iteraciones sin depender de la latencia del simulador ni gastar cuota.

## Qué deberías notar en cada una

**Demo 1 — Multi-tool.** Que la última pregunta (una de tarifas) no debería disparar ninguna
tool. Si el agente inventó un precio, es la prueba en vivo de por qué existe la salvaguarda A6
(Sesión 5).

**Demo 2 — Matriz didáctica.** Que con solo 5 consultas ya se ve un acierto directo, una
confusión y un "sin tool" correcto — la versión completa (30 consultas, matriz de confusión) es
`docente/matriz_seleccion.py`, que corres sobre tu propio catálogo en el laboratorio.

**Demo 3 — Tope de iteraciones.** Que "sin tope" no significa "no funciona": significa que
**cuando** falla, falla mal (gasta cuota indefinidamente). "Con tope" convierte ese fallo en un
mensaje claro de derivación.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `FileNotFoundError` en `proyecto-final/...` | No estás en la raíz del curso | Igual que arriba |
| `401 Unauthorized` | Token sin permiso de inferencia | Regenera el token de Hugging Face |
| La demo 1 o 2 tardan | Cola del *inference provider* | Normal, no es un error de tu código |
