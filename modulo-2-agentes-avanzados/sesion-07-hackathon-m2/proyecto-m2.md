# Proyecto M2 · 100 % del Módulo 2

> Se sustenta en la Sesión 7. La rúbrica completa vive en `recursos/rubricas/rubrica-m2.md` —
> este documento la resume y da el contexto de entrega.

---

## Qué se entrega

| Entregable | Qué contiene |
|---|---|
| **Demo en vivo** | 4-8 min según el tamaño del aula, con `CHAOS_RATE=0.1` activo. Abre con el peor caso encontrado y resuelto |
| `INFORME-L7.md` | **≥ 10 casos borde**, al menos 2 por familia, con traza real (entrada, salida, qué se cambió). Plantilla: `lab/plantilla-informe-l7.md` |
| `tests/` | Pruebas escritas con invariantes (no `assert ==`), repetibles |
| **Documento de diseño** | 2-3 páginas: arquitectura, las 4 tools y por qué, decisiones de RAG y de guardrails. Plantilla: `lab/plantilla-documento-diseno.md` |

El **documento de diseño** es lo que distingue el Proyecto M2 del Assignment A1. El A1 pedía una
tool que funcionara; el M2 pide que el equipo **defienda sus decisiones de arquitectura**. Es
también el insumo directo del Proyecto Integrador de la Sesión 11.

---

## Rúbrica · 4 niveles × 5 criterios

| Criterio | Peso | Qué se mira |
|---|---|---|
| **Funcionalidad** | 25 % | El agente resuelve el caso de uso con tools + RAG + memoria, con el caos activo |
| **Diseño de tools y prompts** | 20 % | Las 4 tools, el retriever, el system prompt del track |
| **Guardrails y manejo de errores** | 25 % | 0 filtraciones se sostiene, y los 4 tipos de caso borde están cubiertos |
| **Evidencia de pruebas** | 20 % | `INFORME-L7.md` con ≥ 10 casos reales, no descritos. Las pruebas corren |
| **Comunicación técnica** | 10 % | La demo y la defensa del documento de diseño |

Descriptores completos de los 4 niveles (Insuficiente / Básico / Competente / Sobresaliente) por
criterio: `recursos/rubricas/rubrica-m2.md`.

---

## La regla del piso

**Heredada del Assignment A1, adaptada a un sistema no determinístico:** si tu carpeta `tests/`
pasa invocando el agente directamente (sin depender del caos del simulador) y tu `INFORME-L7.md`
documenta los 10 casos con evidencia real, tu equipo **no baja de Competente** en el criterio de
Funcionalidad, aunque el caos te arruine un turno en la demo en vivo.

> **Por qué existe esta regla.** Es exactamente lo que la sesión enseña: un sistema no
> determinístico se juzga por su diseño y su evidencia, no por el resultado de una sola
> ejecución. Sin esta regla, un `CHAOS_RATE=0.1` desafortunado en el minuto exacto de tu demo
> penalizaría la mala suerte, no el mal diseño.

---

## Calendario

| Cuándo | Qué pasa |
|---|---|
| Antes de la S7 | Pre-work de 1 h (testing no determinístico) + agente de las Sesiones 4-6 funcionando |
| Sesión 7, primeros 45 min | Clínica con `CHAOS_RATE=0.1` |
| Sesión 7, siguientes 90 min | Ronda de demos (ver `README.md`, sección 3, para la aritmética según el tamaño del aula) |
| Al cerrar la S7 | Entrega de `INFORME-L7.md`, `tests/` y el documento de diseño |

Si el aula supera los 15 equipos, la ronda de demos se parte entre la S7 y los primeros 20 min de
la S8 — el mismo ajuste que se hizo con el Assignment A1 en la S4.
