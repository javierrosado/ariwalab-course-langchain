# Seminario Internacional — Panel de casos reales

> Semana 6 · jueves (después de la sustentación final del martes) ·
> **1.5 h teoría + 4.5 h práctica = 6 h**. Evaluación **formativa, no ponderada**.

**Formato: panel de casos reales de la industria.** Dos o tres profesionales cuentan
implantaciones de agentes en sus empresas, y cada equipo contrasta su propio diseño contra esos
casos.

---

## 1. Objetivos de aprendizaje

Al terminar, puedes:

1. **Extraer una decisión de arquitectura** de un relato de industria, separándola del adorno.
2. Formular una pregunta que compare una decisión propia contra la de un tercero.
3. Contrastar tu diseño con implantaciones reales y nombrar **dos puntos donde difiere**.
4. Anticipar un modo de fallo de tu propio agente a partir del fallo que sufrió otro.

---

## 0. Cómo se escucha un caso de industria

Un panel es contenido impredecible: el docente no controla qué dirán los invitados. Por eso la
sesión se diseña asumiendo eso — **la estructura la pone el curso; el panel solo aporta materia
prima.** Tu trabajo en el bloque 0 es aprender a separar la decisión del adorno:

| Anotar | Ignorar |
|---|---|
| Una decisión y su criterio | El nombre del producto |
| Un fallo de producción y su causa | Las cifras de adopción |
| Una métrica y por qué esa | La lista de tecnologías |
| Un límite que pusieron al agente | El roadmap de la empresa |

```
   "Usamos RAG"                    ──► dato, no enseña nada

   "Usamos RAG y no fine-tuning
    porque el tarifario cambia
    cada mes y el regulador nos
    pide la fuente"                ──► decisión + criterio + consecuencia  ✓
```

Es el mismo marco que se te exigió en la S11 para argumentar tus propias decisiones. **Hoy lo
aplicas para escuchar, no para hablar** — y eso es lo que hace que el seminario cierre el curso.

---

## 2. Los tres mecanismos contra el silencio y el discurso comercial

| # | Mecanismo | Qué evita |
|---|---|---|
| 1 | **Brief escrito a los panelistas** con 4 preguntas fijas que deben responder | Que la charla sea una presentación comercial |
| 2 | **Preguntas preparadas por escrito** y entregadas 48 h antes, curadas por el docente | El silencio, y las 15 versiones de la misma pregunta |
| 3 | **Documento de contraste** posterior, con plantilla | Que la sesión se disuelva en anécdotas |

---

## 3. Guion de la sesión en vivo

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | Cómo se escucha un caso de industria | 30 | T | Separar la decisión del adorno |
| — | Pausa | 10 | — | |
| 1 | Panel: 3 casos × 20 min | 60 | P | Cada panelista responde las 4 preguntas del brief |
| 2 | Preguntas curadas de los equipos | 45 | P | El docente conduce con la lista preparada |
| 3 | Contraste en vivo | 35 | P | Cada equipo nombra, en 90 s, una decisión propia que cambiaría y por qué |

### Bloque 3 — el contraste en vivo

90 segundos por equipo, cronometrados:

1. Una decisión de tu proyecto que hoy tomarías distinto.
2. Qué del panel te lo hizo ver.

Es el cierre real del curso: descubres que tu diseño era una hipótesis, no una verdad.

---

## 4. Tu pre-work: 3 preguntas, 48 h antes

Ver [`preparacion.md`](preparacion.md) para la plantilla de pregunta y ejemplos por track.

---

## 5. Tu entregable: documento de contraste

Ver [`plantilla-contraste.md`](plantilla-contraste.md). Dos páginas, formativo, no ponderado —
la nota del Módulo 3 ya se cerró el martes con el Proyecto Integrador.

---

## 6. Qué NO entra hoy

| No entra | Por qué |
|---|---|
| Contenido técnico nuevo | El curso cerró el martes. Hoy se integra, no se añade |
| Evaluación ponderada | Es formativo — ver §5 |
| Demos de producto de los panelistas | Se prohíbe en el brief |
| El bonus de Foundry | Es asíncrono y se libera aparte |
