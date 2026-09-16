# Curso "IA Agent Building" — Construcción de agentes con LangChain

Curso en español para **ingenieros de software con poco conocimiento de LLMs**.
Basado en la malla `IA Agent Building` y en el repo [`microsoft/langchain-for-beginners`](../langchain-for-beginners).

> **Estado: PLAN CURRICULAR v2.0 — pendiente de aprobación.**
> Las carpetas de sesiones están creadas pero aún vacías de contenido.

---

## Los dos principios del curso

| | |
|---|---|
| **Open source** | Modelo, framework, embeddings, vector store, observabilidad y evaluación son de código abierto |
| **Todo en línea** | Nada corre en la laptop del alumno: se usan las nubes gestionadas de esos productos, en planes gratuitos |
| **Excepción** | El **módulo bonus asíncrono** es el *plus*: el mismo agente desplegado en Microsoft Foundry, como puerta de entrada al Curso 2 |

---

## Datos del curso

| | |
|---|---|
| Duración | 12 sesiones de 6 h · **2 por semana → 6 semanas** + bonus asíncrono |
| Horas lectivas | **72 h** · 36 síncronas / 36 asíncronas · **12 h semanales** por alumno |
| Balance | 40 % teoría / 60 % práctica |
| Laboratorios | 4 tracks en paralelo, incrementales (L1 → L11 + L12 bonus) · **equipos de 2 personas** |
| Proyecto final | Agente open source desplegado en HF Spaces, monitoreado con Langfuse, con app FastAPI |
| Plus | El mismo agente en Microsoft Foundry sin cambiar una línea de código de negocio (bonus, no ponderado) |

---

## Stack

```
        LangChain 1.x  (MIT)
              │
   ┌──────────┼───────────┬───────────────┬────────────────┐
   ▼          ▼           ▼               ▼                ▼
 modelo   embeddings  vector store   observabilidad    despliegue
   │          │           │               │                │
 HF Inf.   HF Inf.   Qdrant Cloud   Langfuse Cloud     HF Spaces
  Qwen3     e5-large   Apache 2.0        MIT          Docker+FastAPI
   32B
   └──────────┴───────────┴───────────────┴────────────────┘
                          │
                    [  BONUS · PLUS  ]
                          ▼
                  Microsoft Foundry
                  (hosted agent + azd)
                          │
                          ▼
                      CURSO 2
                   100 % Foundry
```

---

## Por dónde empezar

| Si eres… | Lee esto |
|---|---|
| **Javier / diseñador del curso** | [`PLAN-CURRICULAR.md`](PLAN-CURRICULAR.md) → [`_memoria/DECISIONES.md`](_memoria/DECISIONES.md) |
| **Docente que va a dictar** | [`docente/prerrequisitos-por-sesion.md`](docente/prerrequisitos-por-sesion.md) → [`docente/labs-incrementales.md`](docente/labs-incrementales.md) → [`docente/casos-de-uso-industrias.md`](docente/casos-de-uso-industrias.md) |
| **Quien retome esto en otra sesión** | [`_memoria/CONTEXTO-REPO.md`](_memoria/CONTEXTO-REPO.md) — evita reanalizar el repo base |
| **Alumno** | `00-preparacion/` (obligatorio antes de la Sesión 1) |

---

## Documentos del plan

| Documento | Responde a |
|---|---|
| [`PLAN-CURRICULAR.md`](PLAN-CURRICULAR.md) | Malla, horas, balance 40/60, stack, evaluación, alternativas de 72 h |
| [`_memoria/CONTEXTO-REPO.md`](_memoria/CONTEXTO-REPO.md) | **Punto 1** — entendimiento del repo, persistido |
| [`_memoria/MAPEO-SYLLABUS-REPO.md`](_memoria/MAPEO-SYLLABUS-REPO.md) | **Punto 2** — qué cubre el repo y qué agregar |
| [`_memoria/DECISIONES.md`](_memoria/DECISIONES.md) | 21 decisiones vigentes, 4 derogadas, 13 riesgos (2 resueltos) |
| [`_memoria/ESPEC-MODELOS-INDUSTRIA.md`](_memoria/ESPEC-MODELOS-INDUSTRIA.md) | El modelo del curso y cómo se personaliza cada industria |
| [`_memoria/IMPACTO-LLM-PERSONALIZADOS.md`](_memoria/IMPACTO-LLM-PERSONALIZADOS.md) | Por qué NO se afinan modelos por industria (decisión D21) |
| [`VERIFICACION.md`](VERIFICACION.md) | Cómo verificar el stack antes de construir laboratorios |
| [`docente/prerrequisitos-por-sesion.md`](docente/prerrequisitos-por-sesion.md) | **Puntos 3 y 4** — audiencia y conceptos previos |
| [`docente/labs-incrementales.md`](docente/labs-incrementales.md) | **Puntos 6 y 9** — labs incrementales y proyecto acumulativo |
| [`docente/casos-de-uso-industrias.md`](docente/casos-de-uso-industrias.md) | **Punto 6** — los 4 casos peruanos |
| [`docente/cronograma.md`](docente/cronograma.md) | Semana a semana + puntos de control de riesgo |

---

## Los 4 tracks de industria

| Track | Empresa ficticia | Caso de uso |
|---|---|---|
| Telecomunicaciones | AndesMóvil | Atención al cliente móvil postpago: plan, avería, reclamo, portabilidad |
| Banca | Banco Inti | Banca personal + detección de operación sospechosa |
| Retail | MercaSur | Post-venta e-commerce: pedido, cambio, devolución |
| Seguros | Andina Seguros | Asesor SOAT y pre-liquidación de siniestro vehicular |

Todas las marcas son ficticias y todos los datos sintéticos.

---

## `proyecto-final/`: qué es y qué no es

**Aclaración que debió estar desde el Laboratorio 1** (añadida al construir la Sesión 4, cuando
se hizo evidente el malentendido). `proyecto-final/<track>/` en **este** repositorio es la
**implementación de referencia del docente**: el aspecto final que debería tener el proyecto de
un equipo, ya escrita y verificada (`docente/verificar_tools.py`, `docente/matriz_seleccion.py`,
`docente/verificar_guardrails.py`).

| Qué | Rol |
|---|---|
| `proyecto-final/<track>/` **en este repo** | Implementación de referencia del docente — lo que leen los verificadores |
| El repositorio de **cada equipo** | Donde el alumno construye el suyo, del L1 al L11, siguiendo cada enunciado |

**No es tu repositorio.** Si eres alumno: no copies `proyecto-final/` como punto de partida —
constrúyelo tú, laboratorio a laboratorio, y usa la referencia solo para comparar **después** de
intentarlo. Los scripts de verificación (`--tools`, `--agente`) siempre apuntan a tu propia
carpeta de laboratorio, nunca a `proyecto-final/`, por diseño.

---

## Cuentas que necesita cada equipo

| Servicio | Para qué | Plan | Verificado |
|---|---|---|---|
| Hugging Face | Modelo de chat, embeddings y despliegue en Spaces | Gratuito | ⚠️ pendiente |
| Qdrant Cloud | Base vectorial del RAG | 1 GB RAM / 4 GB disco · gratis para siempre, sin tarjeta | ✔ 2026-09-05 |
| Langfuse Cloud | Trazabilidad y evaluación | 50k unidades/mes · sin tarjeta · 2 usuarios | ✔ 2026-09-05 |
| GitHub | Repositorio del proyecto | Gratuito | — |
| Azure (solo bonus) | Bloque plus de Foundry — **opcional** | Requiere suscripción | — |

---

## Relación con el repo base

Este curso **no modifica** `../langchain-for-beginners`. El repo de Microsoft queda intacto
para poder actualizarlo con `git pull`. Todo el material derivado vive aquí.

Licencia del repo base: MIT — se reconoce la autoría de Microsoft en los materiales adaptados.
