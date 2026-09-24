# Curso "IA Agent Building" — Construcción de agentes con LangChain

Curso en español para **ingenieros de software con poco conocimiento de LLMs**.
Basado en la malla `IA Agent Building` y en el repo [`microsoft/langchain-for-beginners`](https://github.com/microsoft/langchain-for-beginners).

> **Recorrido:** preparación S0, once sesiones, seminario y bonus opcional.
> Consulta el [mapa pedagógico](docs/COURSE-MAP.md) y el [glosario](recursos/glosario.md).

---

## Los dos principios del curso

| | |
|---|---|
| **Open source** | Modelo, framework, embeddings, vector store, observabilidad y evaluación son de código abierto |
| **Todo en línea** | La inferencia y los servicios se consumen en línea; Python, clientes y demos pueden correr en la laptop. Verificar cuotas de los planes antes del dictado |
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
| Plus | Cliente de chat conmutable y adaptación de hosting a Microsoft Foundry (bonus no ponderado) |

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
| **Docente** | [Plan curricular](PLAN-CURRICULAR.md) → [Guía docente](docente/guia-docente.md) → [Verificación del entorno](VERIFICACION.md) |
| **Docente que va a dictar** | [`docente/prerrequisitos-por-sesion.md`](docente/prerrequisitos-por-sesion.md) → [`docente/labs-incrementales.md`](docente/labs-incrementales.md) → [`docente/casos-de-uso-industrias.md`](docente/casos-de-uso-industrias.md) |
| **Alumno** | `00-preparacion/` (obligatorio antes de la Sesión 1) |

---

## Documentos del plan

| Documento | Responde a |
|---|---|
| [`PLAN-CURRICULAR.md`](PLAN-CURRICULAR.md) | Malla, horas, balance 40/60, stack y evaluación |
| [Personalización por industria](docente/modelos-por-industria.md) | Modelo compartido, prompts, herramientas y RAG por track |
| [`VERIFICACION.md`](VERIFICACION.md) | Cómo verificar el stack antes de las clases |
| [`docente/prerrequisitos-por-sesion.md`](docente/prerrequisitos-por-sesion.md) | audiencia y conceptos previos |
| [`docente/labs-incrementales.md`](docente/labs-incrementales.md) | labs incrementales y proyecto acumulativo |
| [`docente/casos-de-uso-industrias.md`](docente/casos-de-uso-industrias.md) | los 4 casos peruanos |
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

`proyecto-final/<track>/` contiene el **catálogo base de tools del docente**. No contiene una aplicación final completa.
Los checkpoints de cada sesión están en `solucion/<track>/`; S11 aporta el agente, API y web.
El catálogo base tiene verificadores (`docente/verificar_tools.py`, `docente/matriz_seleccion.py`,
`docente/verificar_guardrails.py`).

| Qué | Rol |
|---|---|
| `proyecto-final/<track>/` **en este repo** | Catálogo base de tools usado por verificadores; no aplicación final |
| El repositorio de **cada equipo** | Donde el alumno construye el suyo, del L1 al L11, siguiendo cada enunciado |

**No es tu repositorio.** Si eres alumno: no copies `proyecto-final/` como punto de partida —
constrúyelo tú, laboratorio a laboratorio, y usa la referencia solo para comparar **después** de
intentarlo. Para evaluar tu trabajo, pasa tu archivo con `--tools` o `--agente`. Algunos verificadores
usan el catálogo de referencia por defecto; ese resultado no valida tu implementación.

---

## Cuentas que necesita cada equipo

| Servicio | Para qué | Preparación |
|---|---|---|
| Hugging Face | Modelo de chat, embeddings y despliegue en Spaces | Configurar token y comprobar disponibilidad y cuota |
| Qdrant Cloud | Base vectorial del RAG | Crear cluster y comprobar límites del plan |
| Langfuse Cloud | Trazabilidad y evaluación | Crear proyecto del equipo y comprobar límites del plan |
| GitHub | Repositorio del proyecto | Crear repositorio del equipo |
| Azure (solo bonus) | Bloque plus de Foundry — **opcional** | Revisar acceso y presupuesto antes del bonus |

---

## Referencias y atribución

Material adaptado de [Microsoft LangChain for Beginners](https://github.com/microsoft/langchain-for-beginners), con licencia MIT.
