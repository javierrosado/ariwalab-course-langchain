# Proyecto Integrador Final — 100 % del Módulo 3

> Enunciado que cita `docente/esqueletos/sesion-11.md`. Se sustenta en la sesión en vivo de la
> S11, ante panel.

---

## Qué se entrega

El proyecto acumulado desde el L1 — no hay nada nuevo que inventar, hay que **cerrarlo**:

```
   L1  entorno            L5  memoria + RAG         L9   trazabilidad
   L2  clasificador       L6  guardrails            L10  evaluación
   L3  primera tool       L7  endurecido            L11  cliente web + entrega
   L4  catálogo de 4      L8  desplegado             ▲
                                                     └── esto es lo único nuevo de la S11
```

| Entregable | De dónde viene |
|---|---|
| Agente desplegado con URL pública y API key | L8 |
| Trazas en Langfuse del Space real | L9 |
| Evaluación v1 vs v2 sobre 30 casos | L10 |
| Cliente HTML con streaming | L11 |
| Documento de diseño con diagrama de arquitectura | L11 |
| Demo end-to-end ante panel | día de la S11 |

---

## Entrega anticipada — 24 h antes de la sustentación

- [ ] URL pública del Space (L8)
- [ ] API key para el panel
- [ ] Captura de una traza en Langfuse (L9)
- [ ] Salida de `python docente/verificar_despliegue.py --url <url> --key <key>` en verde

Ver la regla de contingencia en el `README.md` de la sesión, §6: sin esta entrega, una caída del
Space el día de la demo sí penaliza.

---

## El día de la sustentación

| # | Movimiento | Min (sobre 10) |
|---|---|---|
| 1 | El caso de uso en una frase, y a quién sirve | 1 |
| 2 | La demo funcionando: una consulta completa, de principio a fin | 3 |
| 3 | La decisión de arquitectura de la que están más orgullosos, con su alternativa descartada | 3 |
| 4 | El número: qué midieron en el L10 y qué mejoró | 1 |
| — | Q&A del panel | 2 |

---

## Rúbrica

Ver [`recursos/rubricas/rubrica-final.md`](../../recursos/rubricas/rubrica-final.md) — los 5
criterios institucionales completos (Funcionalidad 25 %, Diseño de tools y prompts 20 %,
Guardrails y manejo de errores 20 %, Observabilidad y evaluación 20 %, Comunicación técnica
15 %).

---

## Calendario

| Cuándo | Qué |
|---|---|
| 24 h antes de la S11 | Entrega anticipada (ver arriba) |
| S11, bloque 1 (30 min) | Ensayo cronometrado por equipo |
| S11, bloque 2 (105 min) | Sustentaciones ante panel |
| S11, bloque 3 (5 min) | Cierre del módulo: se libera el bonus de Foundry |

La aritmética de la ronda (minutos por equipo según el número de equipos inscritos) se calcula
antes de la sesión — ver `docente/esqueletos/sesion-11.md` §5, y la tarea **ag** (Javier, con el
número real de inscritos).
