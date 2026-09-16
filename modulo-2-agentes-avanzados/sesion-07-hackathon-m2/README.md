# Sesión 7 — Hackathon, clínica y sustentación del Proyecto M2

> Semana 4 · martes · **1.5 h teoría + 4.5 h práctica = 6 h**. Cierra el Módulo 2: hoy se
> sustenta el **Proyecto M2**, 100 % de la nota del módulo.

---

## 1. Objetivos de aprendizaje

1. Explicar por qué **no se puede probar un agente con `assert respuesta == "esperado"`**.
2. Diseñar casos de prueba para un sistema no determinístico: invariantes, no igualdades.
3. Encontrar y **resolver** al menos 10 casos borde de tu propio agente.
4. Demostrar el agente en vivo ante el aula y responder preguntas técnicas sobre sus decisiones.

---

## 0. Cómo se prueba lo no determinístico

**El concepto central, en una tabla:**

| No se prueba así | Se prueba así |
|---|---|
| `assert r == "Tu plan es Max 89"` | `assert "Max 89" in r` |
| `assert r == esperado` | `assert agente.llamo_tool("get_customer_plan")` |
| "la respuesta es correcta" | `assert r.cita_fuente()` y `assert not contiene_dni(r)` |
| Un solo intento | **5 intentos**, y se mide cuántos pasaron |

> Lo último es lo que más cuesta aceptar a un ingeniero: **una prueba que pasa 4 de 5 veces no
> está rota, está midiendo.** Es la misma idea de la fiabilidad compuesta (D20) aplicada al
> testing: si tu agente pasa el 93 % de las veces por invariante, y tu prueba de estrés encadena
> 3 invariantes, el resultado esperado no es "siempre pasa", es "pasa la mayoría de las veces, y
> tú sabes cuánto".

**Invariantes útiles, en vez de igualdades exactas:**
- La respuesta contiene el dato correcto (`"Max 89" in r`), no es idéntica carácter por carácter.
- El agente llamó a la tool correcta (`agente.llamo_tool("get_customer_plan")`).
- La respuesta cita una fuente cuando afirma una tarifa (`r.cita_fuente()`).
- Ningún DNI sin enmascarar aparece en la respuesta (`not contiene_dni(r)`).

**Las 4 familias de caso borde:**

```
   1. ENTRADA AMBIGUA        "quiero cambiar mi plan y también reclamar por la factura"
                             → dos intenciones en un turno. ¿Qué hace el agente?

   2. DATO AUSENTE           un identificador que no existe, o un campo vacío en la respuesta
                             → ya lo viste en el A1; ahora dentro de una conversación larga

   3. SERVICIO CAÍDO         CHAOS_RATE=0.1: falla sin avisar, a mitad de conversación
                             → ¿pierde el hilo? ¿reintenta en bucle? ¿miente?

   4. SALIDA FUERA DE FORMATO  el modelo devuelve algo que no cumple el esquema
                             → aquí se cobra comun/structured.py de la Sesión 2
```

**Los 6 fallos inyectables del simulador:** `timeout` · `error500` · `error503` · `lento` ·
`vacio` · `malformado`. Fuérzalos con el parámetro `?_fallo=<nombre>` contra el simulador; al
azar, con `CHAOS_RATE>0` sin especificar `_fallo`, solo se inyectan `error503` o `lento`.

---

## 1. Qué hace distinta a esta sesión

**Decidido: clínica, sin ataque cruzado entre equipos.** Cada equipo prueba su propio agente. La
pregunta que esto deja abierta —si nadie ataca a nadie, ¿en qué se diferencia del L6?— se
responde así: **cambia el adversario**.

| | **L6 · Guardrails** | **L7 · Estrés** |
|---|---|---|
| Amenaza | Un adversario **deliberado** | El **mundo real sin malicia** |
| Ejemplos | Inyección, exfiltración de PII, acción prohibida | El servicio cae, el dato no existe, el usuario pregunta dos cosas a la vez, la respuesta llega malformada |
| Instrumento | Batería de 15 ataques | **`CHAOS_RATE=0.1`** en el simulador |
| Criterio | 0 filtraciones | ≥ 10 casos borde documentados **y resueltos** |
| Quién lo provoca | El alumno, a propósito | **El docente**, de forma aleatoria y anunciada |

> **El adversario de hoy es el entorno, y lo activa el docente.** `CHAOS_RATE=0.1` **activado y
> anunciado** al empezar la clínica, y de vuelta a `0.0` al terminar. Un fallo aleatorio no
> anunciado en la sesión que vale el 100 % del módulo sería una trampa, no una lección.

---

## 2. La clínica: 45 minutos, 4 familias

| Min | Qué pide el docente |
|---|---|
| 0-10 | *"Hazle dos preguntas en un solo turno"* — familia 1 |
| 10-20 | *"Pregúntale por algo que no existe, en el turno 4 de la conversación"* — familia 2 |
| 20-30 | *"Sigue conversando hasta que el caos te dé un 503"* — familia 3 |
| 30-40 | *"Fuérzale una salida estructurada con una entrada rarísima"* — familia 4 |
| 40-45 | *"Elige el peor caso que encontraste: ese va primero en tu demo"* |

El último punto es deliberado: **la demo abre con el fallo que el equipo encontró y resolvió**,
no con el camino feliz. Enseña que en un sistema no determinístico lo valioso es saber dónde se
rompe, no fingir que no se rompe.

---

## 3. La ronda de demos

| Equipos | Por equipo | Total |
|---|---|---|
| 8 | 8 min + 3 de preguntas | 88 min ✅ holgado |
| 12 | 5 min + 2 | 84 min ✅ justo |
| 15 | 4 min + 2 | 90 min ⚠️ al límite, sin margen |

Con 15 equipos hay que cronometrar de verdad; el docente entrega retroalimentación extensa por
escrito después, no en el momento. Si el aula supera los 15 equipos, la ronda se parte entre la
S7 y los primeros 20 min de la S8 — igual que se hizo con el Assignment A1.

---

## 4. El Proyecto M2

Ver [`proyecto-m2.md`](proyecto-m2.md) para el enunciado completo, la rúbrica y la regla del
piso. Ver [`lab/`](lab/) para el guion de la clínica y las plantillas del informe y del
documento de diseño.

---

## 5. Qué NO entra hoy

| No entra | Va en |
|---|---|
| Despliegue, Docker, FastAPI | Sesión 8 |
| Langfuse y trazas | Sesión 9 |
| Métricas formales y golden dataset de evaluación | Sesión 10 |
| Ataque entre equipos | Descartado por diseño: la S7 es clínica, no torneo |
