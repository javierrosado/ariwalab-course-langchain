# Sesión 7 — Hackathon, clínica y sustentación del Proyecto M2

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-07.md`.
> ⚠️ Anunciar `CHAOS_RATE=0.1` antes de activarlo — nunca sorpresa en la sesión que vale el 100 %
> del Módulo 2.

---

## Sesión 7 · Hackathon M2
- Semana 4 · martes · 6 h (1.5 T / 4.5 P)
- Hito: **Proyecto M2 — 100 % del Módulo 2**
- Adversario de hoy: el mundo real sin malicia (no un atacante, eso fue la S6)

---

## Cómo se prueba lo no determinístico
- `assert r == "esperado"` no sirve
- Invariantes: "cita una fuente", "no aparece un DNI", "llamó a ≤ 3 tools"
- Una prueba que pasa 4 de 5 veces no está rota, está midiendo
- Las 4 familias: entrada ambigua · dato ausente · servicio caído · salida fuera de formato

*(Pausa · 10 min)*

---

## Clínica con el caos activado
- `CHAOS_RATE=0.1`: cada equipo rompe su agente y lo arregla
- Secuencia guiada por el docente: una familia cada 10 min

---

## Ronda de demos
- Demo + preguntas, equipo por equipo
- La demo abre con el peor fallo encontrado y resuelto, no con el camino feliz
- Aritmética: con 15 equipos, 4 min demo + 2 de preguntas — al límite, sin margen

---

## Entregables del Proyecto M2
- Demo en vivo · `INFORME-L7.md` (≥10 casos borde) · `tests/` con invariantes · documento de
  diseño (2-3 páginas)
- Rúbrica: Funcionalidad 25 % · Diseño 20 % · Guardrails y errores 25 % · Evidencia 20 % ·
  Comunicación 10 %
- Regla del piso: si `tests/` pasa y el informe documenta los 10 casos, no baja de Competente
  aunque el caos arruine un turno en vivo

---

## Cierre y entrega
- Qué se entrega y hasta cuándo
- `CHAOS_RATE` vuelve a `0.0`

---

## Qué NO entra hoy
- Despliegue, Docker, FastAPI → S8
- Langfuse y trazas → S9
- Golden dataset de evaluación → S10
