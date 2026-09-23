# Sesión 8 — Despliegue en producción con HF Spaces

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-08.md`.

---

## Sesión 8 · Despliegue en HF Spaces
- Semana 4 · jueves · 6 h (2.5 T / 3.5 P)
- Hito: Avance 1 del Módulo 3
- Hoy el agente deja de vivir en tu terminal

---

## Qué es "producción" para un agente
- No es que corra: es que otro lo invoque, sin ti delante

---

## 12-Factor y config por entorno
- El mismo código, tres entornos, cero cambios de código
- `comun/settings.py` ya lo hace desde el L1

---

## El Dockerfile, línea por línea
- Se escribe hoy, no se ejecuta en local (P2) — lo construye la plataforma

---

## FastAPI: `/chat` y `/health` — qué va autenticado
- `/health` sin credencial (la plataforma lo necesita)
- `/chat` con `X-API-Key` — se protege la cuota, no un secreto de negocio

---

## Secretos en la nube
- *Space secrets*, nunca `.env` en el repo
- Un token filtrado se revoca y se regenera; borrar el commit no basta

---

## *Cold start* y el free tier
- El primer request tras inactividad tarda — propiedad del tier, no un bug

*(Pausa · 10 min)*

---

## Práctica: `api.py` + `Dockerfile`
- La capa HTTP sobre el agente del L7

---

## Desplegar y probar desde fuera
- `git push` al remote del Space
- `docente/verificar_despliegue.py` — 4 comprobaciones automáticas
- Documentar la latencia del primer request vs el segundo

---

## Qué NO entra hoy
- Trazabilidad y Langfuse → S9
- Evaluación y datasets → S10
- Cliente web con streaming → S11
- Docker en local, Kubernetes, CI/CD → fuera de alcance
