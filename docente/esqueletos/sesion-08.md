# Esqueleto · Sesión 8 — Despliegue en producción con HF Spaces

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-3-produccion/sesion-08-despliegue-hf-spaces/` |
| Semana · día | Semana 4 · jueves |
| Horas | **2.5 h teoría · 3.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (90 T / 80 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L8 · Contenedor y despliegue en HF Spaces** |
| Hitos | **Avance 1 del M3**: arquitectura de despliegue |

---

## 2. Riesgo abierto

| Riesgo | Estado | Impacto en esta sesión |
|---|---|---|
| Límites del free tier de HF Spaces | **Sin verificar** | 15 Spaces simultáneos podrían no caber. Alternativa preparada: Render |
| Cuota de HF Inference | Sin verificar | Un endpoint público mal protegido la agota en horas — por eso la decisión de §6 |

> **Acción del docente antes de la semana 4:** crear un Space de prueba y confirmar límites de CPU,
> RAM, almacenamiento y tiempo de inactividad del tier gratuito.

---

## 3. Objetivos de aprendizaje

1. Explicar qué significa "producción" para un agente, y en qué se diferencia de un script que corre.
2. Escribir un `Dockerfile` **sin ejecutar Docker en local** (principio P2), y explicar cada línea.
3. Exponer el agente por **FastAPI** con `/chat` y `/health`, y saber por qué la plataforma exige el segundo.
4. Gestionar secretos **en la plataforma**, no en el repositorio.
5. Proteger un endpoint público y explicar qué se protege: no el secreto, **la cuota**.
6. Explicar el *cold start* y por qué el primer request de un tier gratuito tarda.

---

## 4. Con qué llega el alumno

**Pre-work de 1 h:**

| # | Concepto | Por qué |
|---|---|---|
| 1 | 12-Factor App: config por entorno | Marco mental de todo el despliegue |
| 2 | Contenedores: imagen, capa, `Dockerfile`, `EXPOSE`, `CMD` | Se escribe uno real; lo construye el Space |
| 3 | FastAPI: rutas, Pydantic como request/response, ASGI | API del proyecto |
| 4 | Health check: por qué una plataforma lo exige | `/health` es requisito del Space |
| 5 | *Space secrets* vs `.env` local | Invariante: nunca credenciales en el repo |
| 6 | `git push` a un remote que no es GitHub | Es el mecanismo de despliegue |

**Verificación de entrada:** cuenta de HF con un Space vacío ya creado, y `git remote -v` mostrándolo.

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | Qué es "producción" para un agente | 10 | T | No es que corra: es que otro lo invoque, sin ti delante |
| 1 | 12-Factor y config por entorno | 15 | T | El mismo código, tres entornos, cero cambios de código |
| 2 | El `Dockerfile`, línea por línea | 20 | T | Se escribe, **no se ejecuta en local** (P2). Lo construye la plataforma |
| 3 | FastAPI: `/chat` y `/health` | 20 | T | Qué va autenticado y qué no, y por qué |
| 4 | **Secretos en la nube** | 15 | T | Space secrets. Qué pasa cuando un token se filtra en un commit |
| 5 | *Cold start* y el free tier | 10 | T | El primer request tarda. Es una propiedad del tier, no un bug |
| — | **Pausa** | 10 | — | |
| 6 | Práctica: `api.py` + `Dockerfile` | 45 | P | La capa HTTP sobre el agente del L7 |
| 7 | Desplegar y **probar desde fuera** | 35 | P | `git push` y llamada desde otra máquina |

**Teoría 90 · práctica 80 · pausa 10** → con pre-work y lab: **2.5 h / 3.5 h** ✅

### Bloque 3 — qué va autenticado

```
   GET  /health   ──► SIN autenticación
                      La plataforma lo llama para saber si el Space vive.
                      Si pide credencial, el Space queda marcado como caído.

   POST /chat     ──► CON autenticación   (X-API-Key)
                      Cada llamada gasta cuota de HF Inference del equipo.
```

> **Es la misma asimetría que el alumno ya consumió.** El simulador expone `/health` abierto y
> todo lo demás con `X-API-Key`. En la S3 fue cliente de ese patrón; hoy lo publica. Cierra el
> círculo, y conviene decirlo en voz alta.

---

## 6. Decisión: el `/chat` lleva API key propia del equipo

| | Decidido |
|---|---|
| `/health` | Público, sin credencial |
| `/chat` | Exige cabecera `X-API-Key` |
| Dónde vive la key | `AGENT_API_KEY` como **Space secret**, nunca en el repo |
| Cómo se evalúa "cualquiera puede invocarlo" | El equipo entrega la key al evaluador junto con la URL |

**Qué se protege: la cuota, no el secreto.** Los datos son sintéticos y las marcas ficticias; no
hay nada confidencial detrás. Lo que hay detrás es el token de HF Inference del equipo: un `/chat`
abierto que alguien descubra agota en horas un free tier que, además, todavía no está medido.

> Para evaluar L8, pedir la URL y la API key del agente al equipo. La invocación debe
> estar autenticada y las credenciales del proveedor no deben estar en el código.

---

## 7. Las 4 demos · `code/`

| Archivo | Qué demuestra |
|---|---|
| `01_api_local.py` | El agente detrás de `/chat` y `/health`, con `uvicorn` |
| `02_dockerfile_comentado` | El `Dockerfile` del curso explicado línea por línea |
| `03_secretos.py` | El mismo código leyendo un secreto de `.env` y de una variable del Space |
| `04_llamar_desde_fuera.py` | La URL pública con key correcta, sin key y con key mala |

La demo 4 se corre **contra el Space del docente**, ya desplegado, para que el alumno vea el
resultado antes de desplegar el suyo.

---

## 8. Laboratorio L8

| Parte | Min | Qué hace el alumno |
|---|---|---|
| 1 | 30 | `app/api.py`: `/chat`, `/health` y el guardia de `X-API-Key` |
| 2 | 25 | `Dockerfile` y `requirements.txt` del Space |
| 3 | 35 | Crear el Space, cargar los secretos, `git push` |
| 4 | 30 | Probar **desde otra máquina** y documentar la latencia del primer request |

### Entregables

| Entregable | Ruta |
|---|---|
| `app/api.py` | repo del equipo |
| `Dockerfile` | raíz del repo del equipo |
| URL pública del Space + key para el evaluador | `lab/<track>/DESPLIEGUE.md` |
| **Avance 1 del M3**: diagrama de arquitectura de despliegue | `lab/<track>/avance-1-m3.md` |

### Criterio de aceptación

- El agente responde por HTTP **desde fuera de la máquina del alumno**, con su API key.
- `/health` responde **sin** credencial.
- **Cero credenciales en el repositorio**: ni `.env`, ni en el `Dockerfile`, ni en el historial de git.
- El equipo documenta la latencia del primer request tras la inactividad (*cold start*).

> La verificación de las credenciales no es a ojo: `git log -p | grep -i "hf_\|sk-lf\|api_key"` sobre
> el repo del equipo. Si aparece algo, el token se revoca y se regenera — y esa es la lección
> completa sobre secretos, aprendida donde no cuesta nada.

---

## 9. Qué **no** entra

| No entra | Va en |
|---|---|
| Trazabilidad y Langfuse | S9 |
| Evaluación y datasets | S10 |
| Cliente web con streaming | S11 |
| Foundry | bonus asíncrono |
| Docker en local, Kubernetes, CI/CD | fuera de alcance (P2) |

---

## 11. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| El Space queda en *Build error* | Falta una dependencia en `requirements.txt` | Leer el log de build del Space: es donde vive el error |
| El Space arranca y muere | `/health` pide credencial, o el puerto no es el que espera la plataforma | Es el bloque 3 |
| `401` desde fuera | La key no se cargó como Space secret | Los secrets no se leen del repo |
| El primer request tarda 40 s | *Cold start* del tier gratuito | No es un bug: documentarlo es parte del entregable |
| Un token aparece en el historial de git | Se commiteó el `.env` antes de añadirlo al `.gitignore` | Revocar, regenerar, y explicar por qué borrar el commit no basta |
