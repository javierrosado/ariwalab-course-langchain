# Sesión 9 — Monitoreo y trazabilidad con Langfuse

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-09.md`.

---

## Sesión 9 · Observabilidad con Langfuse
- Semana 5 · martes · 6 h (2.5 T / 3.5 P)
- Hito: Avance 2 del Módulo 3
- Desviación documentada del PDF: LangSmith (propietario) → Langfuse (open source, P1)

---

## El agente ya está desplegado. ¿Y ahora qué hace?
- Hoy deja de ser una caja negra

---

## Logs vs métricas vs trazas
- ¿Qué pasó? · ¿Cuánto? · ¿Por dónde pasó?

---

## Anatomía de una traza de agente
- Arquitectura de traza → spans: modelo, tool, retriever; verificar contexto padre en la implementación
- 3 llamadas al modelo para 1 pregunta: la fiabilidad se compone
- El modelo suele ser el cuello, no las tools ni Qdrant

---

## Latencia p50/p95 y costo por ejecución
- Un solo *cold start* distorsiona el promedio
- p50 = mediana · p95 = percentil de cola; declarar método y muestra

---

## PII dentro de una traza
- Enmascarador de comun/observability.py, aplicado antes de exportar a Langfuse
- Si el DNI no sale hacia el cliente, tampoco sale hacia un SaaS de terceros
- Costo real: se pierde capacidad de depuración — se firma a propósito

*(Pausa · 10 min)*

---

## Práctica: instrumentar y redesplegar
- El callback, el enmascarador, `git push`

---

## Leer trazas reales y hallar 2 cuellos de botella
- Del Space, no de la laptop
- Candidatos típicos: retriever que se llama siempre, historial que crece, reintentos de
  extracción, *cold start*

---

## Qué NO entra hoy
- Datasets, evaluators, LLM-as-judge → S10
- Optimizar de verdad (solo se identifica) → S10
- Azure Monitor / OTel exporters → Curso 2
