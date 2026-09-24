# Sesión 11 — Aplicación final y sustentación

> Semana 6 · martes · **1.5 h teoría + 4.5 h práctica = 6 h**.

Antes de esta sesión: pre-work de 1 h ([`conceptos-previos.md`](conceptos-previos.md)) y la
**entrega anticipada, 24 h antes** (ver §6): URL pública, API key para el panel, captura de una
traza en Langfuse, y salida de `docente/verificar_despliegue.py` en verde.

---

## 1. Objetivos de aprendizaje

1. Consumir la propia API desde un cliente web, con **streaming**.
2. Documentar una arquitectura de agente de forma que otro ingeniero pueda operarla.
3. **Argumentar** una decisión de arquitectura: qué se eligió, qué se descartó y por qué.
4. Sostener un Q&A técnico sobre decisiones propias.

---

## Alcance del checkpoint web

`responder_streaming()` espera la respuesta completa y aplica el guardrail antes de enviarla
por fragmentos SSE. Permite una interfaz progresiva, pero no reduce el tiempo hasta completar
la generación del modelo. El historial heredado de L5 vive en memoria del proceso y se pierde
al reiniciar el Space; el despliegue del curso no incorpora persistencia durable.

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

## 0. Cómo se argumenta ante un panel

Una decisión de arquitectura tiene 3 partes: **alternativa descartada → criterio → consecuencia**.

```
   "Usamos Qdrant"                              ──► dato, no es una decisión

   "Usamos Qdrant y no un índice en memoria
    porque el corpus tiene que sobrevivir al
    reinicio del Space y necesitábamos filtrar
    por metadatos para citar"                   ──► decisión + criterio + consecuencia  ✓
```

### El guion de la demo, en 4 movimientos

| # | Movimiento | Min (sobre 10) |
|---|---|---|
| 1 | El caso de uso en una frase, y a quién sirve | 1 |
| 2 | **La demo funcionando**: una consulta completa, de principio a fin | 3 |
| 3 | **La decisión de arquitectura de la que están más orgullosos**, con su alternativa descartada | 3 |
| 4 | El número: qué midieron en el L10 y qué mejoró | 1 |
| — | Q&A del panel | 2 |

**El movimiento 3 es el que separa una buena sustentación de una narración de código.**

---

## 6. Decisión: contingencia si el Space está caído

| Momento | Qué |
|---|---|
| **24 h antes** | El equipo entrega la evidencia: URL pública, API key para el panel, captura de una traza en Langfuse y salida de `docente/verificar_despliegue.py` en verde |
| El día de la demo, si el Space responde | Se sustenta contra la URL pública |
| El día de la demo, si el Space duerme o falla | Se sustenta **en local, sin penalización** |

La nota evalúa el diseño, la evidencia y la argumentación — no la disponibilidad de un tier
gratuito que el equipo no controla. Si un equipo **no** entregó la evidencia de las 24 h y
además el Space falla, ahí sí hay penalización.

---

## 7. El documento de diseño — 4 páginas, no más

| Sección | Contenido |
|---|---|
| 1 · Caso de uso | Qué resuelve, para quién, y qué **no** resuelve |
| 2 · Arquitectura | Diagrama: cliente → API → agente → tools · retriever · guardrails → simulador · Qdrant · modelo |
| 3 · Decisiones | 5 decisiones con su alternativa descartada y el criterio |
| 4 · Evidencia | Métricas del L10, cuellos del L9, y qué se haría con una semana más |

Plantilla: [`plantilla-documento-diseno.md`](../../recursos/plantillas/plantilla-documento-diseno.md).

---

## 8. Rúbrica del Proyecto Integrador

Ver [`recursos/rubricas/rubrica-final.md`](../../recursos/rubricas/rubrica-final.md). Es la
**única evaluación del curso donde los 5 criterios institucionales aplican completos** — hasta
la S9 no existía observabilidad que calificar.

---

## 9. El laboratorio

Ver [`lab/README.md`](lab/README.md) para el Laboratorio 11 completo (cliente con streaming,
documento de diseño, evidencia y ensayo) y [`proyecto-integrador.md`](proyecto-integrador.md)
para el enunciado completo.

---

## 10. Qué NO entra hoy

| No entra | Va en |
|---|---|
| Foundry | bonus asíncrono, liberado al cerrar hoy |
| Contenido nuevo de agentes | ninguno: hoy se cierra |
