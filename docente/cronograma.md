# Cronograma de dictado

**6 semanas · 12 sesiones · 72 horas lectivas**
**2 sesiones por semana de 3 horas síncronas** (ejemplo: martes y jueves)
**+ módulo bonus asíncrono de Foundry**, liberado al cerrar la sesión 11
**Equipos de 2 personas**

---

## Estructura de cada sesión

```
   ANTES de la sesión        SESIÓN EN VIVO         DESPUÉS de la sesión
   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
   │ Conceptos previos│   │  Teoría + demo   │   │   Laboratorio    │
   │      1 hora      │──►│  Lab guiado      │──►│  incremental     │
   │   asíncrono      │   │     3 horas      │   │  2 h asíncrono   │
   │  BLOQUEANTE      │   │    síncrono      │   │                  │
   └──────────────────┘   └──────────────────┘   └──────────────────┘
        TEORÍA                   MIXTO                 PRÁCTICA
```

**6 horas por sesión × 12 sesiones = 72 horas.**
Con 2 sesiones por semana, el alumno dedica **12 horas semanales** durante 6 semanas.

> Este ritmo es exigente pero compatible con una jornada laboral: entre sesiones hay 3 o 4 días
> para resolver 1 h de pre-work y 2 h de laboratorio. Ver §"Efectos del ritmo".

---

## Calendario

### Semana 0 · Preparación (antes de la primera sesión)

| Qué | Tiempo | Estado |
|-----|--------|--------|
| Sesión 0 completa: nivelación de LLMs | 4-5 h | **Bloqueante** |
| Alta de las 3 cuentas: HF, Qdrant, Langfuse | 40 min | **Bloqueante** |
| Entorno Python y `.env` funcionando | 45 min | **Bloqueante** |
| Las 4 demos ejecutadas | 60 min | Bloqueante |
| Autoevaluación ≥ 80 % | 30 min | **Bloqueante** |
| Equipos de 2 personas formados | — | **Bloqueante** |
| Elección preliminar de industria | — | Se formaliza en el L1 |

> Con el ritmo comprimido, **la semana 0 deja de ser una recomendación**. La sesión 5 ocurre
> el día 5 del curso: no hay margen para aprovisionar Qdrant sobre la marcha.

---

### Semana 1 · Módulo 1 · Fundamentos

| Día | Sesión | Pre-work (1 h) | Sesión en vivo (3 h) | Laboratorio (2 h) | Hito |
|-----|--------|----------------|----------------------|-------------------|------|
| Mar | **S1** | Agente vs LLM · secretos · `.env` | Fundamentos + primer modelo en línea | **L1** primer agente-cero | Test 1 · **elección de track** |
| Jue | **S2** | Roles de mensaje · **Pydantic v2** | Prompts, plantillas, structured output | **L2** clasificador de intención | Test 2 |

---

### Semana 2 · Cierre del M1 y arranque del M2

| Día | Sesión | Pre-work (1 h) | Sesión en vivo (3 h) | Laboratorio (2 h) | Hito |
|-----|--------|----------------|----------------------|-------------------|------|
| Mar | **S3** | Docstrings · decoradores · REST | Tools + API externa + ReAct manual | **L3** primera tool contra el simulador | **Assignment A1 · 100 % del M1** |
| Jue | **S4** | **MCP** · async | Catálogo de tools y selección dinámica | **L4** 4 tools + MCP | Avance 1 del proyecto |

---

### Semana 3 · Módulo 2 · Memoria, RAG y guardrails

| Día | Sesión | Pre-work (1 h) | Sesión en vivo (3 h) | Laboratorio (2 h) | Hito |
|-----|--------|----------------|----------------------|-------------------|------|
| Mar | **S5** | Embeddings · coseno · chunking | Memoria + RAG agéntico en Qdrant | **L5** RAG del dominio | Avance 2 · **Qdrant operativo** |
| Jue | **S6** | Prompt injection · PII · Ley 29733 | Guardrails y límites de actuación | **L6** 15 ataques bloqueados | Avance 3 |

---

### Semana 4 · Cierre del M2 y arranque del M3

| Día | Sesión | Pre-work (1 h) | Sesión en vivo (3 h) | Laboratorio (2 h) | Hito |
|-----|--------|----------------|----------------------|-------------------|------|
| Mar | **S7** | Testing no determinístico | Hackathon + clínica + demo (**`CHAOS_RATE=0.1` activado y anunciado, vuelve a `0.0` al terminar**) | **L7** pruebas de estrés | **Proyecto M2 · 100 % del M2** |
| Jue | **S8** | 12-Factor · Docker · FastAPI | Contenedor y despliegue en HF Spaces | **L8** URL pública viva | Avance 1 del M3 |

---

### Semana 5 · Módulo 3 · Observabilidad y evaluación

| Día | Sesión | Pre-work (1 h) | Sesión en vivo (3 h) | Laboratorio (2 h) | Hito |
|-----|--------|----------------|----------------------|-------------------|------|
| Mar | **S9** | Trazas · spans · percentiles | Observabilidad con Langfuse | **L9** 2 cuellos de botella | Avance 2 · **Langfuse operativo** |
| Jue | **S10** | Golden dataset · groundedness | Evaluación y optimización | **L10** v1 vs v2 medido | Avance 3 del M3 |

---

### Semana 6 · Cierre

| Día | Sesión | Pre-work (1 h) | Sesión en vivo (3 h) | Laboratorio (2 h) | Hito |
|-----|--------|----------------|----------------------|-------------------|------|
| Mar | **S11** | Diagramas de arquitectura | Sustentación ante panel | **L11** app final | **Proyecto Integrador · 100 % del M3** |
| Jue | **Sem** | — | Seminario Internacional | — | Cierre del certificado |

---

### Después del curso · Bonus asíncrono

| Bloque | Pre-work | Contenido | Entregable | Peso |
|--------|----------|-----------|------------|------|
| **Bonus** | Modelo de recursos de Azure · `azd` | Guía autoguiada de despliegue en Foundry | **L12** agente en Foundry + cuadro comparativo | **No ponderado** |

Se libera al cerrar la S11. Opcional. Se ofrece una asesoría de 1 h para quien tenga suscripción
de Azure.

---

## Efectos del ritmo

Dos sesiones semanales es el punto de equilibrio: sostiene la continuidad sin exigir dedicación
completa. Aun así, hay efectos que conviene gestionar.

| # | Efecto | Por qué importa | Cómo se gestiona |
|---|--------|-----------------|------------------|
| **1** | **12 horas semanales de dedicación** | Es compatible con una jornada laboral, pero no es poco | Declararlo con claridad **antes de la inscripción**. Nadie debe descubrirlo en la semana 2 |
| **2** | **Margen de recuperación de 3-4 días** | Un equipo que se atrasa el martes tiene hasta el jueves | Suficiente para retomar con el **checkpoint de recuperación** (`solucion/` de cada lab), que el docente reparte proactivamente |
| **3** | **Los módulos no cierran en frontera de semana** | El M1 cierra el martes de la semana 2 y el M2 el martes de la semana 4 | No es un problema pedagógico, pero conviene anunciarlo: el alumno espera que "módulo" y "semana" coincidan |
| **4** | **El pre-work compite con el laboratorio** | 1 h de pre-work + 2 h de lab en 3-4 días | El pre-work debe ser **estrictamente de 1 hora**. Si no cabe, se recorta contenido, no se estira el tiempo |
| **5** | **Aprovisionamiento con margen acotado** | La S5 usa Qdrant en la **semana 3** y la S9 usa Langfuse en la **semana 5** | Se cierra todo en la semana 0. Hay margen para rescatar a un rezagado, pero no para empezar de cero |
| **6** | **Un fallo de servicio arruina 2 sesiones** | Si el simulador cae un martes, afecta martes y jueves | Verificación de los 4 servicios **antes de cada sesión** y modo degradado `DATA_SOURCE=csv` documentado |

---

## Puntos de control

### Antes de que empiece el curso

| Cuándo | Qué verificar | Si falla |
|--------|---------------|----------|
| **2 semanas antes** | **Tool calling del modelo**, probado contra el endpoint real | Bloqueante del curso completo: cambiar de modelo |
| **2 semanas antes** | Simulador desplegado en HF Spaces y respondiendo | Se dicta con `uvicorn` local, perdiendo el realismo |
| **1 semana antes** | Límites vigentes del free tier de HF Inference y HF Spaces | Cuenta PRO del docente para las demos |
| **1 semana antes** | API keys de equipo generadas y repartidas | Sin ellas no hay L3 |
| **Semana 0** | Las 3 cuentas activas en **todos** los equipos | Sesión de soporte antes de la S1 |
| **Semana 0** | Equipos de 2 formados, con su proyecto Langfuse creado | Reestructurar antes de la S1, nunca en la S9 |
| **Semana 0** | **Ejercicio de Pydantic resuelto** | Sin esto se cae la S3, que es el día 3 |

### Durante el curso

| Cuándo | Qué verificar | Si falla |
|--------|---------------|----------|
| **Antes de cada sesión** | `/health` del simulador + HF + Qdrant + Langfuse responden | Modo degradado `DATA_SOURCE=csv` |
| Sem 2 · S3 | Todos los equipos con el L3 funcionando | Repartir el checkpoint del L2 antes de la S4 |
| Sem 3 · S5 | Cluster de Qdrant operativo por equipo | Bloqueante del L5 y de todo lo que sigue |
| Sem 4 · S7 | Los 4 tracks con prototipo funcional | Repartir el checkpoint del L6 antes del hackathon |
| Sem 4 · S7 | `CHAOS_RATE=0.1` activado y anunciado | Bajarlo a `0.0` al terminar |
| Sem 4 · S8 | Space de cada equipo creado y `git push` funcionando | Alternativa preparada: Render |
| Sem 5 · S9 | Proyecto de Langfuse operativo por equipo | Bloqueante del L9 y del L10 |
| Sem 6 · S11 | App final desplegada por cada equipo | Se sustenta con el agente del L9 |

---

## Otras modalidades posibles

La misma malla admite otros repartos sin cambiar el contenido ni las horas:

| Modalidad | Semanas | Sesiones/semana | Horas/semana | Perfil de alumno |
|-----------|---------|-----------------|--------------|------------------|
| Intensiva | 4 | 3 | 18 h | Dedicación completa o bootcamp |
| **Equilibrada** *(actual)* | **6** | **2** | **12 h** | **Profesional con jornada laboral** |
| Extendida | 12 | 1 | 6 h | Profesional con poca disponibilidad |

Las tres suman 72 horas y respetan el balance 40/60. Solo cambia el calendario.
