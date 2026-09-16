# Laboratorio L8 · Contenedor y despliegue en HF Spaces

**Objetivo:** sacar tu agente del entorno de desarrollo y darle una URL pública.

**Duración:** 2 h.

**Punto de partida:** el `agent.py` (v4, con guardrails) de tu Laboratorio 6 — con memoria y
RAG del L5 ya dentro. Hoy no le agregas ninguna capacidad nueva al agente: lo envuelves con
una capa HTTP y lo publicas.

---

## Parte 1 · `app/api.py` (30 min)

Escribe `/chat` y `/health`, y el guardia de `X-API-Key` (ver `code/01_api_local.py` como punto
de partida — es literalmente el mismo contrato, con tu propio `agent.py`):

```
   GET  /health   ──► SIN autenticación, responde {"status": "ok"}
   POST /chat     ──► CON X-API-Key, invoca tu responder(mensaje) y devuelve {"respuesta": ...}
```

Si `X-API-Key` no coincide con tu `AGENT_API_KEY`, responde `401` **antes** de llamar al agente
— nunca gastes cuota de HF Inference validando una key mala.

## Parte 2 · `Dockerfile` y `requirements.txt` (25 min)

Copia el `Dockerfile` de `code/02_dockerfile_comentado.md` (o `solucion/<tu-track>/Dockerfile`
como referencia) y ajusta el `CMD` al módulo real de tu `app/api.py`. Verifica que
`requirements.txt` en la raíz de tu repo tenga `fastapi` y `uvicorn[standard]`.

## Parte 3 · Crear el Space, cargar secretos, `git push` (35 min)

1. Crea el Space (SDK: Docker) si no lo hiciste en el pre-work.
2. Carga **todas** las variables que tu agente necesita como *Space secrets*: `HF_TOKEN`,
   `QDRANT_URL`, `QDRANT_API_KEY`, `AGENT_API_KEY`, y las que uses de tu track.
3. `git push space main` (o el nombre que le hayas dado a tu remote).
4. Espera a que el Space termine de construir (revisa los logs de build si falla).

## Parte 4 · Probar desde fuera y documentar el *cold start* (30 min)

```bash
python docente/verificar_despliegue.py --url https://<tu-space>.hf.space --key <tu-AGENT_API_KEY>
```

Debe pasar las 4 comprobaciones. Anota en `DESPLIEGUE.md` cuánto tardó el **primer** request
tras un periodo sin tráfico, contra el segundo inmediato — el script lo detecta y lo marca si la
diferencia es grande.

---

## Entregables

| Entregable | Ruta |
|---|---|
| `app/api.py` | tu repositorio de equipo |
| `Dockerfile` | raíz de tu repositorio |
| URL pública del Space + key para el evaluador | `lab/<tu-track>/DESPLIEGUE.md` |
| **Avance 1 del M3**: diagrama de arquitectura de despliegue | `lab/<tu-track>/avance-1-m3.md` |

Ver las plantillas de `DESPLIEGUE.md` y `avance-1-m3.md` en
[`solucion/telecomunicaciones/`](../solucion/telecomunicaciones/) — están vacías de datos reales
a propósito: son la estructura que debes llenar con la evidencia de **tu** Space.

## Criterio de aceptación

- El agente responde por HTTP **desde fuera de tu máquina**, con tu API key.
- `/health` responde **sin** credencial.
- **Cero credenciales en el repositorio**: ni `.env`, ni en el `Dockerfile`, ni en el historial
  de git. Se verifica con `git log -p | grep -i "hf_\|sk-lf\|api_key"` sobre tu repo — si aparece
  algo, revoca el token y regenera uno nuevo.
- El equipo documenta la latencia del primer request tras la inactividad (*cold start*).

## Cada track, sus 4 tools desplegadas

| Track | Enunciado |
|---|---|
| Telecomunicaciones · AndesMóvil | [`telecomunicaciones.md`](telecomunicaciones.md) |
| Banca · Banco Inti | [`banca.md`](banca.md) |
| Retail · MercaSur | [`retail.md`](retail.md) |
| Seguros · Andina Seguros | [`seguros.md`](seguros.md) |
