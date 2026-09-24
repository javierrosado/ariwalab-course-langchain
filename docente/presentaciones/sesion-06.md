# Sesión 6 — Automatización, asistentes y guardrails

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-06.md`.

---

## Sesión 6 · Guardrails y límites
- Semana 3 · jueves · 6 h (2.5 T / 3.5 P)
- Controles de entrada, acción y salida; cobertura y límites de los guardrails
- Hito: Avance 3 del proyecto

---

## Lo que el agente NO debe hacer
- Hasta hoy: habilitar. Hoy: limitar
- Puente con la S5: citar no es lo mismo que estar autorizado; el corpus es superficie de ataque
  nueva; el filtro por metadatos ya era un guardrail sin saberlo

---

## Inyección de prompt
- "Ignora tus instrucciones..." — la defensa NO está en el prompt
- Es el mismo diagrama del bloque 1 de la S3, releído como seguridad: el modelo nunca ejecuta,
  solo propone; tu código decide

---

## PII y Ley 29733
- Qué cuenta como dato personal: DNI, tarjeta, teléfono, dirección
- Ley 29733 como contexto regulatorio, no asesoría legal
- Enmascarar en entrada Y en salida — son dos guardrails distintos

---

## Límites de actuación y escalamiento
- Lista de acciones prohibidas, propia de cada industria
- Cuándo el agente debe dejar de intentarlo y derivar a un humano

---

## Middleware: dónde se enganchan
- 3 puntos: antes del modelo · antes de ejecutar la tool · después de la respuesta
- Few-shot (A5) como primera capa, antes del código — no lo reemplaza
- Mención breve: cuándo hace falta LangGraph (ramificación condicional persistente) — Curso 2

*(Pausa · 10 min)*

---

## Laboratorio guiado: `guardrails.py`
- Entrada, acción, salida + lista de prohibidos del track

---

## Correr la batería de 15 ataques
- `docente/verificar_guardrails.py`
- Que un ataque pase en el primer intento es lo esperado, no un fracaso

---

## Avance 3 del proyecto
- Prototipo funcional declarado

---

## Qué NO entra hoy
- Pruebas de estrés del entorno (sin malicia) → S7
- Autenticación real de usuarios → fuera del curso
- Métricas de seguridad en producción → S9/S10
