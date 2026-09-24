# Esqueleto · Sesión 11 — Sustentación final integradora

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-3-produccion/sesion-11-sustentacion-final/` |
| Semana · día | Semana 6 · martes |
| Horas | **1.5 h teoría · 4.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (30 T / 140 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L11 · Aplicación final** |
| Evaluación | **Proyecto Integrador Final · 100 % del Módulo 3** |

---

## 2. Qué se entrega

El proyecto acumulado desde el L1. No hay nada nuevo que inventar: hay que **cerrarlo**.

```
   L1  entorno            L5  memoria + RAG         L9   trazabilidad
   L2  clasificador       L6  guardrails            L10  evaluación
   L3  primera tool       L7  endurecido            L11  cliente web + entrega
   L4  catálogo de 4      L8  desplegado             ▲
                                                     └── esto es lo único nuevo de hoy
```

| Entregable | De dónde viene |
|---|---|
| Agente desplegado con URL pública y API key | L8 |
| Trazas en Langfuse del Space real | L9 |
| Evaluación v1 vs v2 sobre 30 casos | L10 |
| **Cliente HTML con streaming** | **nuevo, L11** |
| **Documento de diseño con diagrama de arquitectura** | **nuevo, L11** |
| Demo end-to-end ante panel | hoy |

---

## 3. Objetivos de aprendizaje

1. Consumir la propia API desde un cliente web, con **streaming**.
2. Documentar una arquitectura de agente de forma que otro ingeniero pueda operarla.
3. **Argumentar** una decisión de arquitectura: qué se eligió, qué se descartó y por qué.
4. Sostener un Q&A técnico sobre decisiones propias.

---

## 4. Con qué llega el alumno

**Pre-work de 1 h:**

| # | Concepto | Por qué |
|---|---|---|
| 1 | Diagramas de arquitectura (C4 nivel 1 y 2, o equivalente) | Se exige en el documento de diseño |
| 2 | OpenAPI / Swagger, que FastAPI ya genera | Parte del entregable |
| 3 | Server-Sent Events y streaming en el navegador | El cliente del L11 |
| 4 | Cómo se argumenta una decisión: alternativas, criterio, consecuencia | Es lo que el panel evalúa |

**Entrega anticipada, 24 h antes** — ver §6.

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | **Cómo se argumenta ante un panel** | 30 | T | Decisión → alternativas → criterio → consecuencia. Qué preguntará el panel y por qué |
| — | **Pausa** | 10 | — | |
| 1 | Ensayo cronometrado por equipo | 30 | P | Cada equipo corre su demo una vez, con reloj |
| 2 | **Sustentaciones ante panel** | 105 | P | Demo end-to-end + Q&A |
| 3 | Cierre del módulo | 5 | P | Qué queda: el bonus de Foundry |

**Teoría 30 · práctica 140 · pausa 10** → con pre-work y lab: **1.5 h / 4.5 h** ✅

### Aritmética de la ronda — hay que hacerla antes, no el día

```
   105 min disponibles ÷ nº de equipos

     8 equipos  ──► 13 min    cómodo
    10 equipos  ──► 10 min    cómodo
    13 equipos  ──►  8 min    mínimo aceptable
    15 equipos  ──►  7 min    ajustado: usar 30 min del laboratorio
   >16 equipos  ──► dos paneles en paralelo
```

**Regla:** 8 minutos por equipo es el piso. Por debajo de eso no hay Q&A, y el Q&A es donde se ve
si el equipo entendió lo que construyó. Si los números no dan, se amplía con parte de las 2 h de
laboratorio — nunca se recorta el Q&A.

### Bloque 0 — el guion de la demo, en 4 movimientos

| # | Movimiento | Min (sobre 10) |
|---|---|---|
| 1 | El caso de uso en una frase, y a quién sirve | 1 |
| 2 | **La demo funcionando**: una consulta completa, de principio a fin | 3 |
| 3 | **La decisión de arquitectura de la que están más orgullosos**, con su alternativa descartada | 3 |
| 4 | El número: qué midieron en el L10 y qué mejoró | 1 |
| — | Q&A del panel | 2 |

> **El movimiento 3 es el que separa una buena sustentación de una narración de código.** "Usamos
> Qdrant" no es una decisión: es un hecho. "Usamos Qdrant y no un índice en memoria porque el
> corpus tiene que sobrevivir al reinicio del Space y porque necesitábamos filtrar por metadatos
> para citar" sí lo es.

---

## 6. Decisión: contingencia si el Space está caído

| Momento | Qué |
|---|---|
| **24 h antes** | El equipo entrega la evidencia: URL pública, API key para el panel, captura de una traza en Langfuse y salida de `docente/verificar_despliegue.py` en verde |
| **El día de la demo, si el Space responde** | Se sustenta contra la URL pública |
| **El día de la demo, si el Space duerme o falla** | Se sustenta **en local, sin penalización** |

**El fundamento es el mismo que la regla del piso del A1:** la nota evalúa el diseño, la evidencia y
la argumentación — no la disponibilidad de un tier gratuito que el equipo no controla. Lo que sí se
califica es haber dejado evidencia con anticipación, que es exactamente lo que se hace en una
entrega real.

> Si un equipo **no** entregó la evidencia de las 24 h y además el Space falla, ahí sí hay
> penalización: el fallo no es del free tier, es de no haber previsto que podía fallar. Es la
> lección de todo el módulo, aplicada a ellos mismos.

---

## 7. Laboratorio L11 · 2 h antes de la sesión

| Parte | Min | Qué hace el alumno |
|---|---|---|
| 1 | 50 | `app/web/index.html`: cliente con streaming contra su `/chat` |
| 2 | 40 | Documento de diseño: diagrama de arquitectura + decisiones |
| 3 | 20 | Correr `verificar_despliegue.py` y capturar la evidencia |
| 4 | 10 | Ensayo y cronómetro |

### El documento de diseño — 4 páginas, no más

| Sección | Contenido |
|---|---|
| 1 · Caso de uso | Qué resuelve, para quién, y qué **no** resuelve |
| 2 · Arquitectura | Diagrama: cliente → API → agente → tools · retriever · guardrails → simulador · Qdrant · modelo |
| 3 · Decisiones | 5 decisiones con su alternativa descartada y el criterio |
| 4 · Evidencia | Métricas del L10, cuellos del L9, y qué se haría con una semana más |

La sección 4 importa más de lo que parece: **decir qué falta es señal de que se entendió el sistema.**

---

## 8. Rúbrica del Proyecto Integrador

Es la **única evaluación del curso donde los 5 criterios institucionales aplican completos** — hasta
la S9 no existía observabilidad que calificar.

| Criterio | Peso | Qué se mira |
|---|---|---|
| **Funcionalidad** | 25 % | La demo end-to-end corre: consulta → tool o RAG → respuesta citada |
| **Diseño de tools y prompts** | 20 % | Las 4 tools con docstrings A2, el system prompt del track, el retriever acotado |
| **Guardrails y manejo de errores** | 20 % | PII enmascarada, acciones prohibidas, degradación limpia ante fallo |
| **Observabilidad y evaluación** | 20 % | Trazas reales del Space, 30 casos evaluados, mejora v1→v2 argumentada |
| **Comunicación técnica** | 15 % | Los 4 movimientos de la demo y el Q&A |

Cuatro niveles: Insuficiente · En desarrollo · Competente · Destacado.

> **Qué distingue a un Destacado.** No es que todo funcione: es que el equipo sepa **dónde no
> funciona y por qué**. Un equipo que muestra su peor caso, explica su causa y dice qué haría, ha
> entendido más que uno cuya demo salió perfecta.

---

## 9. Qué **no** entra

| No entra | Va en |
|---|---|
| Foundry | bonus asíncrono, liberado al cerrar hoy |
| Contenido nuevo de agentes | ninguno: hoy se cierra |

---

## 11. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| La demo narra el código | No se preparó el movimiento 3 | Es lo que el bloque 0 enseña; el ensayo lo corrige |
| El Space duerme justo al empezar | *Cold start* | Despertarlo 5 min antes: va en el checklist del panel |
| El equipo no sabe qué mejoró en el L10 | Se cambiaron varias cosas a la vez | Se arrastra desde la S10; el informe debería haberlo evitado |
| La demo se pasa de tiempo | No se cronometró | El ensayo del bloque 1 existe para esto |
| El cliente web no hace streaming, solo espera | Se implementó con un `fetch` normal | Funciona igual, pero se pierde el objetivo 1: se anota |
