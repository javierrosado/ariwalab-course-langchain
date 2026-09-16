# Demos de la Sesión 8

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python modulo-3-produccion/sesion-08-despliegue-hf-spaces/code/01_api_local.py` | `HF_TOKEN` | El agente detrás de `/chat` y `/health`, con `uvicorn`, corriendo localmente |
| 2 | [`02_dockerfile_comentado.md`](02_dockerfile_comentado.md) | No (es lectura) | El `Dockerfile` del curso explicado línea por línea |
| 3 | `python modulo-3-produccion/sesion-08-despliegue-hf-spaces/code/03_secretos.py` | No | El mismo código leyendo un secreto de `.env` y de una variable del Space |
| 4 | `python modulo-3-produccion/sesion-08-despliegue-hf-spaces/code/04_llamar_desde_fuera.py --url <space-docente> --key <key>` | No (llama por HTTP) | La URL pública con key correcta, sin key y con key mala |

La demo 1 usa el agente de referencia de la Sesión 6
(`modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/solucion/telecomunicaciones/agent.py`)
a propósito — es una demo del docente, no tu Laboratorio 8. La demo 4 corre contra el Space del
docente ya desplegado; si aún no está desplegado en el momento de la clase, corre en modo
`--simular` (sin `--url`/`--key`) contra una app en memoria, para no bloquear la sesión.

## Qué deberías notar en cada una

**Demo 1 — API local.** Que `/health` no exige credencial y `/chat` sí — antes incluso de
hablar de despliegue, ya puedes probar el contrato completo en tu máquina.

**Demo 2 — Dockerfile comentado.** Por qué `COPY requirements.txt .` va ANTES de `COPY . .`:
es caché de capas, no una preferencia estética.

**Demo 3 — Secretos.** Que el código que lee `AGENT_API_KEY` no sabe ni le importa si el valor
vino de tu `.env` o de un *Space secret* — es la prueba en vivo del principio 12-Factor.

**Demo 4 — Llamar desde fuera.** Que solo el primer caso llega a invocar el modelo; los otros
dos se rechazan ANTES de gastar cuota.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| La demo 1 no responde en `/chat` | Falta `HF_TOKEN` en el `.env` | Revisa `.env.example` |
| La demo 4 da error de conexión | El Space del docente no está desplegado todavía | Corre sin `--url`/`--key` (modo `--simular`) |
| `401` en la demo 1 con curl | La key del `curl` no coincide con `AGENT_API_KEY` impresa al arrancar | Copia la key exacta que imprime la consola |
