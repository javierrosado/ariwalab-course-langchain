# Esqueleto · Sesión 7 — Hackathon, clínica y sustentación del Proyecto M2

> Contrato de la sesión 7. Insumo de la sesión de Claude Code que escribe los archivos
> (pasos 4.16–4.19 del `ROADMAP.md`). No es material de alumno.
>
> Decidido con Javier el 2026-09-16 · Fase 4 · Módulo 2

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta destino | la que ya exista bajo `modulo-2-agentes-avanzados/` para la sesión 7 |
| Semana · día | Semana 4 · martes |
| Horas | **1.5 h teoría · 4.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (30 T / 140 P / 10 pausa) + 2 h lab (P) |
| Laboratorio | **L7 · Pruebas de estrés** |
| Evaluación | **Proyecto M2 · 100 % del Módulo 2** |
| Estado en el mapeo | `AULA` — sin contraparte en el repo |

---

## 2. Qué hace distinta a esta sesión

**Decidido: clínica, sin ataque cruzado entre equipos.** Cada equipo prueba su propio agente.

Eso deja una pregunta abierta que hay que resolver por diseño: *si nadie ataca a nadie, ¿en qué se
diferencia el L7 del L6?* La respuesta es que **cambia el adversario**:

| | **L6 · Guardrails** | **L7 · Estrés** |
|---|---|---|
| Amenaza | Un adversario **deliberado** | El **mundo real sin malicia** |
| Ejemplos | Inyección, exfiltración de PII, acción prohibida | El servicio cae, el dato no existe, el usuario pregunta dos cosas a la vez, la respuesta llega malformada |
| Instrumento | Batería de 15 ataques | **`CHAOS_RATE=0.1` en el simulador** |
| Criterio | 0 filtraciones | ≥ 10 casos borde documentados **y resueltos** |
| Quién lo provoca | El alumno, a propósito | **El docente**, de forma aleatoria y anunciada |

> **El adversario de la S7 es el entorno, y lo activa el docente.** A `CHAOS_RATE=0.1`, una de
> cada diez llamadas al simulador falla sola: 503, timeout, respuesta lenta o JSON malformado. El
> agente tiene que sobrevivir a una conversación completa con esa tasa de fallo. Ningún equipo
> necesita atacar a otro para que la sesión sea dura.

⚠️ **Anunciarlo.** El cronograma ya lo dice: `CHAOS_RATE=0.1` **activado y anunciado**, y de vuelta
a `0.0` al terminar. Un fallo aleatorio no anunciado en la sesión que vale el 100 % del módulo
sería una trampa, no una lección.

---

## 3. Objetivos de aprendizaje

1. Explicar por qué **no se puede probar un agente con `assert respuesta == "esperado"`**.
2. Diseñar casos de prueba para un sistema no determinístico: invariantes, no igualdades.
3. Encontrar y **resolver** al menos 10 casos borde de su propio agente.
4. Demostrar el agente en vivo ante el aula y responder preguntas técnicas sobre sus decisiones.

---

## 4. Pre-work · 1 h — Testing no determinístico

| # | Concepto | Por qué |
|---|---|---|
| 1 | Por qué falla `assert respuesta == "esperado"` | Se anunció en la S0; aquí se resuelve |
| 2 | **Invariantes** en vez de igualdades | *"la respuesta cita una fuente"*, *"no aparece un DNI"*, *"llamó a ≤ 3 tools"* |
| 3 | Las 4 familias de caso borde | Entrada ambigua · dato ausente · servicio caído · respuesta del modelo fuera de formato |
| 4 | Los 6 fallos inyectables del simulador | `timeout` · `error500` · `error503` · `lento` · `vacio` · `malformado` |

### El concepto central, en una tabla

| No se prueba así | Se prueba así |
|---|---|
| `assert r == "Tu plan es Max 89"` | `assert "Max 89" in r` |
| `assert r == esperado` | `assert agente.llamo_tool("get_customer_plan")` |
| "la respuesta es correcta" | `assert r.cita_fuente()` y `assert not contiene_dni(r)` |
| Un solo intento | **5 intentos**, y se mide cuántos pasaron |

> Lo último es lo que más cuesta aceptar a un ingeniero: **una prueba que pasa 4 de 5 veces no está
> rota, está midiendo.** Es la misma idea de la fiabilidad compuesta, aplicada al testing.

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | **Cómo se prueba lo no determinístico** | 30 | T | Invariantes, familias de caso borde, cuántas veces repetir |
| — | **Pausa** | 10 | — | |
| 1 | **Clínica con el caos activado** | 45 | P | `CHAOS_RATE=0.1`. Cada equipo rompe su agente y lo arregla |
| 2 | **Ronda de demos** | 90 | P | Demo + preguntas, equipo por equipo |
| 3 | Cierre y entrega | 5 | P | Qué se entrega y hasta cuándo |

**Teoría 30 · práctica 140 · pausa 10** → con pre-work y lab: **1.5 h / 4.5 h** ✅

### Aritmética de la ronda de demos

| Equipos | Por equipo | Total | ¿Cabe en 90 min? |
|---|---|---|---|
| 8 | 8 min demo + 3 de preguntas | 88 min | ✅ holgado |
| 12 | 5 min + 2 | 84 min | ✅ justo |
| **15** | **4 min + 2** | **90 min** | ⚠️ **al límite, sin margen** |

Con 15 equipos hay que cronometrar de verdad y el docente no puede dar retroalimentación extensa
en el momento: se entrega por escrito después. **Si el aula supera los 15 equipos, la ronda no
cabe** y hay que partirla entre la S7 y los primeros 20 min de la S8 — igual que se hizo con el A1.

---

## 6. Laboratorio L7 · Pruebas de estrés

### Las 4 familias de caso borde

```
   1. ENTRADA AMBIGUA        "quiero cambiar mi plan y también reclamar por la factura"
                             → dos intenciones en un turno. ¿Qué hace el agente?

   2. DATO AUSENTE           un identificador que no existe, o un campo vacío en la respuesta
                             → ya se vio en el A1; ahora dentro de una conversación larga

   3. SERVICIO CAÍDO         CHAOS_RATE=0.1: falla sin avisar, a mitad de conversación
                             → ¿pierde el hilo? ¿reintenta en bucle? ¿miente?

   4. SALIDA FUERA DE FORMATO  el modelo devuelve algo que no cumple el esquema
                             → aquí se cobra comun/structured.py de la S2
```

### Entregables · Proyecto M2

| Entregable | Qué contiene |
|---|---|
| **Demo en vivo** | 4-8 min según el tamaño del aula, con el caos activado |
| `INFORME-L7.md` | **≥ 10 casos borde**: qué se probó, qué pasó, qué se cambió |
| `tests/` | Las pruebas escritas con invariantes, repetibles |
| **Documento de diseño** | 2-3 páginas: arquitectura, las 4 tools y por qué, decisiones de RAG y de guardrails |

> El **documento de diseño** es lo que distingue el Proyecto M2 del A1. El A1 pedía una tool que
> funcionara; el M2 pide que el equipo **defienda sus decisiones de arquitectura**. Es también el
> insumo del Proyecto Integrador de la S11.

### Rúbrica · 4 niveles × 5 criterios

| Criterio | Peso | Qué se mira |
|---|---|---|
| **Funcionalidad** | 25 % | El agente resuelve el caso de uso con tools + RAG + memoria, con el caos activo |
| **Diseño de tools y prompts** | 20 % | Las 4 tools, el retriever, el system prompt del track |
| **Guardrails y manejo de errores** | 25 % | 0 filtraciones se sostiene, y los 4 tipos de caso borde están cubiertos |
| **Evidencia de pruebas** | 20 % | `INFORME-L7.md` con ≥ 10 casos reales, no descritos. Las pruebas corren |
| **Comunicación técnica** | 10 % | La demo y la defensa del documento de diseño |

> **Corrección VALIDACION-INTEGRAL H2 (2026-09-16).** La regla A4 (tope de iteraciones) se
> enseña en la S3 y la S4 y hasta ahora no se medía en ningún sitio. El criterio
> **"Guardrails y manejo de errores"** de arriba incluye, explícitamente, esta comprobación de
> la familia 3 (servicio caído): *ante `?_fallo=error503` sostenido durante toda la conversación
> (o, en `tests/`, con la tool parcheada para fallar siempre), el agente debe terminar en
> **como máximo `MAX_ITERATIONS`** llamadas al modelo y emitir un mensaje explícito al usuario
> — nunca colgarse, nunca reintentar en silencio hasta agotar la cuota.* Es una línea de código
> en el enunciado del L7, no un capítulo nuevo: `docente/esqueletos/README.md` §"Trabajo previo"
> ya lo trae como tarea, y `solucion/<track>/tests/test_casos_borde.py` de esta sesión lo
> implementa como parte de la familia 3.

**La regla del piso del A1 sigue vigente**, adaptada: si las pruebas de `tests/` pasan con el
agente llamado directamente y el informe documenta los 10 casos, el equipo no baja de *Competente*
aunque en la demo en vivo el caos le arruine un turno. **Es exactamente lo que la sesión enseña:**
un sistema no determinístico se juzga por su diseño y su evidencia, no por una sola ejecución.

---

## 7. Guion de la clínica · para el docente

45 minutos, con el caos ya activado. El docente rota por los equipos con esta secuencia:

| Min | Qué pide el docente |
|---|---|
| 0-10 | *"Hazle dos preguntas en un solo turno"* — familia 1 |
| 10-20 | *"Pregúntale por algo que no existe, en el turno 4 de la conversación"* — familia 2 |
| 20-30 | *"Sigue conversando hasta que el caos te dé un 503"* — familia 3 |
| 30-40 | *"Fuérzale una salida estructurada con una entrada rarísima"* — familia 4 |
| 40-45 | *"Elige el peor caso que encontraste: ese va primero en tu demo"* |

> El último punto es deliberado: **la demo abre con el fallo que el equipo encontró y resolvió**,
> no con el camino feliz. Enseña que en un sistema no determinístico lo valioso es saber dónde se
> rompe, no fingir que no se rompe.

---

## 8. Qué **no** entra

| No entra | Va en |
|---|---|
| Despliegue, Docker, FastAPI | S8 |
| Langfuse y trazas | S9 |
| Métricas formales y golden dataset de evaluación | S10 |
| Ataque entre equipos | descartado por decisión: esta sesión es clínica |

---

## 9. Los archivos a producir

| # | Archivo | Contenido pactado |
|---|---|---|
| **4.16** | `README.md` | El bloque 0 completo: invariantes, familias, cuántas repeticiones |
| **4.17** | `conceptos-previos.md` | Testing no determinístico + los 6 fallos del simulador |
| **4.18** | `lab/` | L7 × 4 tracks: guion de la clínica y plantilla de `INFORME-L7.md` |
| **4.19** | `proyecto-m2.md` | Enunciado, entregables, rúbrica 4×5, regla del piso y calendario |

> ⚠️ **Ampliación 2026-09-16.** El pacto original de esta sesión no incluía `code/` ni
> `solucion/` (bloque 2 de §5 dice que la "ronda de demos" es de los propios equipos, no de
> Code). Por pedido explícito se añadieron los pasos **4.20** y **4.21** para que el bloque 0
> (invariantes, familias, repetición) tenga demos ejecutables y para que el criterio de
> `tests/` del §7 tenga un checkpoint de referencia, igual que las demás sesiones del módulo.

| **4.20** | `code/` | 3 demos: por qué falla `assert ==`, invariantes en aislamiento, repetir y medir + `README.md` |
| **4.21** | `solucion/` | `tests/invariantes.py` + `tests/test_casos_borde.py` × 4 tracks, con las 4 familias del bloque 0 medidas por repetición e invariantes |

### Trabajo previo

| # | Tarea | Por qué |
|---|---|---|
| a | `recursos/rubricas/rubrica-m2.md` | La cita el enunciado y la usa el docente |
| b | Plantilla de `INFORME-L7.md` y de documento de diseño | Sin plantilla, 15 informes con 15 estructuras distintas |
| c | Añadir al `docente/cronograma.md` el recordatorio de `CHAOS_RATE=0.1` → `0.0` | Ya está en la lista de verificación; conviene que también esté en la sesión |

---

## 10. Errores esperables

| Síntoma | Causa | Respuesta |
|---|---|---|
| El informe describe casos en vez de mostrarlos | No se pegaron las trazas | Traza real o no cuenta, igual que en el A1 |
| Los 10 casos son todos de la familia 2 | Es la más fácil de provocar | Exigir al menos 2 de cada familia |
| El agente pierde el hilo tras un 503 | El error borró el historial | Revisar `memory.py`: el fallo de una tool no debe tumbar el hilo |
| El equipo culpa al caos de todo | No distingue fallo del entorno de fallo propio | Es la lección: el entorno **va** a fallar; el diseño es lo que se evalúa |
| La demo se pasa de tiempo | No se ensayó | Cronometrar de verdad; con 15 equipos no hay margen |
