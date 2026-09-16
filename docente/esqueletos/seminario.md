# Esqueleto · Seminario Internacional — Panel de casos reales

> Contrato del Seminario. Insumo de la sesión de Claude Code que escribe sus archivos.
> No es material de alumno.
>
> Decidido con Javier el 2026-09-16 · Semana 6

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta destino | `modulo-3-produccion/seminario-internacional/` |
| Semana · día | Semana 6 · jueves *(después de la sustentación final del martes)* |
| Horas | **1.5 h teoría · 4.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (T) + 3 h en vivo (30 T / 140 P / 10 pausa) + 2 h de contraste (P) |
| Laboratorio | Ninguno. El entregable es un **documento de contraste** |
| Evaluación | **Formativa, no ponderada** |
| Estado en el mapeo | Sin contraparte en el repo ni en el PDF: se diseña entero |

**Formato decidido: panel de casos reales de la industria.** Dos o tres profesionales cuentan
implantaciones de agentes en sus empresas, y cada equipo contrasta su propio diseño contra esos casos.

---

## 2. Objetivos de aprendizaje

Al terminar, el alumno puede:

1. **Extraer una decisión de arquitectura** de un relato de industria, separándola del adorno.
2. Formular una pregunta que compare una decisión propia contra la de un tercero.
3. Contrastar su diseño con implantaciones reales y nombrar **dos puntos donde difiere**.
4. Anticipar un modo de fallo de su propio agente a partir del fallo que sufrió otro.

El objetivo 1 se trabaja en el bloque 0; los demás, en el documento de contraste.

---

## 3. El problema de diseño, dicho de frente

Un panel es **contenido impredecible**. El docente no controla qué dirán los invitados, y un
seminario mal estructurado degenera en tres presentaciones de producto y media hora de silencio
incómodo cuando se abre el turno de preguntas.

La sesión se diseña asumiendo eso. **La estructura la pone el curso; el panel solo aporta materia
prima.** Tres mecanismos:

| # | Mecanismo | Qué evita |
|---|---|---|
| 1 | **Brief escrito a los panelistas** con 4 preguntas fijas que deben responder | Que la charla sea una presentación comercial |
| 2 | **Preguntas preparadas por escrito** y entregadas 48 h antes, curadas por el docente | El silencio, y las 15 versiones de la misma pregunta |
| 3 | **Documento de contraste** posterior, con plantilla | Que la sesión se disuelva en anécdotas |

> Si solo se implanta uno de los tres, que sea el primero. Un panelista sin brief habla de su
> producto; un panelista con brief habla de sus decisiones.

---

## 4. El brief a los panelistas · 1 página

Se envía con 3 semanas de anticipación. Pide **20 minutos** estructurados así:

| # | Pregunta que cada panelista debe responder | Min |
|---|---|---|
| 1 | ¿Qué construyeron, para quién, y qué problema de negocio resolvía? | 4 |
| 2 | **¿Qué decisión de arquitectura cambiarían hoy, y por qué?** | 6 |
| 3 | **¿Qué falló en producción que no esperaban?** | 6 |
| 4 | ¿Qué midieron para saber que funcionaba? | 4 |

Las preguntas 2 y 3 son las que sostienen la sesión. Un caso de éxito sin fallos no enseña nada, y
todo el mundo que ha puesto un agente en producción tiene esa historia.

> **Qué se le pide explícitamente al panelista que NO haga:** demo de producto, cifras de ventas,
> nombres de clientes. El curso no necesita un caso de marketing: necesita una decisión discutible.

---

## 5. Con qué llega el alumno

**Pre-work de 1 h:**

| # | Tarea | Entrega |
|---|---|---|
| 1 | Leer los perfiles y el sector de los 3 panelistas | — |
| 2 | Releer su propio documento de diseño de la S11 | — |
| 3 | **Escribir 3 preguntas**, una por panelista, siguiendo la plantilla | 48 h antes |

### La plantilla de pregunta

Una pregunta útil nombra una decisión propia. El formato obligatorio:

```
   "Nosotros decidimos [X] porque [criterio].
    En su caso, ¿cómo resolvieron [ese mismo punto] y qué los llevó a decidirlo así?"
```

Ejemplo real del track de seguros:

> *"Nosotros obligamos al agente a citar el condicionado antes de afirmar una cobertura, porque una
> respuesta sin fuente no es auditable. ¿Ustedes impusieron una regla parecida, o confiaron en el
> modelo y lo controlaron después?"*

**El docente cura las preguntas**: agrupa las repetidas, descarta las que se responden con un sí o
un no, y ordena las 12-15 que sobrevivan por tema. Sin esa curaduría, el turno de preguntas lo
monopolizan dos equipos.

---

## 6. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | **Cómo se escucha un caso de industria** | 30 | T | Separar la decisión del adorno. Qué anotar y qué ignorar |
| — | **Pausa** | 10 | — | |
| 1 | Panel: 3 casos × 20 min | 60 | P | Cada panelista responde las 4 preguntas del brief |
| 2 | Preguntas curadas de los equipos | 45 | P | El docente conduce con la lista preparada |
| 3 | **Contraste en vivo** | 35 | P | Cada equipo nombra, en 90 segundos, una decisión propia que cambiaría y por qué |

**Teoría 30 · práctica 140 · pausa 10** → con pre-work y contraste: **1.5 h / 4.5 h** ✅

### Bloque 0 — qué anotar

Es la parte lectiva, y es lo que convierte un panel en formación:

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

Es el mismo marco que se les exigió a ellos en la S11. **Hoy lo aplican para escuchar, no para
hablar** — y eso es lo que hace que el seminario cierre el curso.

### Bloque 3 — el contraste en vivo

90 segundos por equipo, cronometrados:

1. Una decisión de su proyecto que hoy tomarían distinto.
2. Qué del panel se lo hizo ver.

Con 10 equipos son 15 minutos de contenido y 20 de discusión. Es el cierre real del curso: el
alumno descubre que su diseño era una hipótesis, no una verdad.

---

## 7. Entregable · documento de contraste

Las 2 h asíncronas posteriores. **Dos páginas**, formativo, no ponderado:

| Sección | Contenido |
|---|---|
| 1 | Los 3 casos en una frase cada uno: qué construyeron y para qué |
| 2 | **Tres decisiones del panel que coinciden** con las suyas, y por qué creen que coinciden |
| 3 | **Dos decisiones que difieren**, y cuál de las dos defenderían ante un cliente |
| 4 | Un fallo de producción que oyeron y que **su agente también tendría** |

La sección 4 es la que más rinde. Un equipo que sale del curso sabiendo cómo va a fallar su propio
sistema aprendió más que uno que sale creyendo que no fallará.

> **Por qué no se pondera.** La nota del Módulo 3 ya se cerró el martes con el Proyecto Integrador.
> Este documento es retroalimentación, y se lee y se comenta — pero calificar la capacidad de un
> alumno para contrastar contra un panel cuyo contenido nadie controló sería injusto.

---

## 8. Qué **no** entra

| No entra | Por qué |
|---|---|
| Contenido técnico nuevo | El curso cerró el martes. Hoy se integra, no se añade |
| Evaluación ponderada | Ver §6 |
| Demos de producto de los panelistas | Se prohíbe en el brief |
| El bonus de Foundry | Es asíncrono y se libera aparte |

---

## 9. Archivos a producir

| Archivo | Contenido |
|---|---|
| `README.md` | El bloque 0 completo: cómo se escucha un caso, con el cuadro de qué anotar |
| `preparacion.md` | El pre-work: plantilla de pregunta, ejemplos por track, plazo de 48 h |
| `plantilla-contraste.md` | Las 4 secciones del entregable |
| `brief-panelistas.md` | **Documento del docente**, no del alumno: el brief de 1 página |
| `guion-docente.md` | Cómo conducir: tiempos, curaduría de preguntas, qué hacer si un panelista se extiende |

---

## 10. Tareas de Javier, con fecha

| # | Tarea | Para cuándo | Si falta |
|---|---|---|---|
| ai | **Convocar 3 panelistas** de sectores distintos a los 4 tracks, o de los mismos | 3 semanas antes | Con 2 el panel funciona; con 1 no es un panel |
| aj | Enviar el brief de 1 página a cada uno | Al confirmar | El panelista improvisa una presentación comercial |
| ak | Confirmar asistencia y probar la conexión si alguno es remoto | 48 h antes | Es un seminario "internacional": hay husos horarios |
| al | Curar las preguntas de los equipos | 24 h antes | El turno de preguntas lo monopolizan dos equipos |

> **Plan B, escrito de antemano:** si el día del seminario solo llega un panelista, la sesión se
> reconvierte en el formato alternativo — el docente presenta 2 casos públicos documentados y el
> bloque 2 se alarga. Tener ese plan escrito evita improvisar delante del aula.

---

## 11. Riesgos propios de esta sesión

| Riesgo | Mitigación |
|---|---|
| Un panelista cancela a última hora | Convocar 3 para que el piso sean 2 · Plan B escrito |
| El panel deriva en presentación de producto | El brief, y el docente interrumpiendo con la pregunta 2 |
| Nadie pregunta | Las preguntas ya están escritas y curadas: el docente las lee |
| Un panelista se extiende 40 min | Cronómetro visible y aviso previo en el brief |
| El contenido no conecta con ningún track | Es aceptable: el contraste de §6 funciona igual entre industrias distintas |
