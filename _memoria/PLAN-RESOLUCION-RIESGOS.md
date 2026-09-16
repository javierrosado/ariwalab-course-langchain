# Plan de resolución de riesgos · Curso IA Agent Building

**Estado a 2026-09-10** · Ariwa Labs
Proyecto: `C:\personal\microsoft\ariwalab-course-langchain`

---

## Decisiones que definen el curso

| # | Decisión | Efecto sobre el riesgo |
|---|---|---|
| **D21 · Camino A** | Sin fine-tuning. Un solo modelo; la personalización vive en el system prompt y en Qdrant | Disolvió o redujo **7 riesgos** |
| **D27 · Calendario** | 2 sesiones/semana de 3 h → **6 semanas**, 12 h semanales por alumno | Bajó **R15 y R16** de alto a medio |
| **D28 · Modelo** | **`Qwen/Qwen3-32B`**, modo non-thinking | **Cerró R1**, el único riesgo crítico bloqueante |

---

## Verificación del modelo · resultado real

Ejecutado el 2026-09-10 con `python -m comun.check_stack --candidatos` contra el endpoint real:

```
VEREDICTO: 1 de 4 candidatos sirven para el curso.
Recomendado por velocidad: Qwen/Qwen3-32B
```

| Candidato | Resultado |
|---|---|
| **`Qwen/Qwen3-32B`** | ✅ **Pasó** — modelo del curso |
| `Qwen/Qwen3-30B-A3B` | ❌ Falló |
| `Qwen/Qwen3-8B` | ❌ Falló |
| `meta-llama/Llama-3.3-70B-Instruct` | ❌ Falló |

**Lección:** la recomendación previa era el MoE `Qwen3-30B-A3B` por su bajo costo de inferencia.
La medición la descartó. El modelo se eligió por evidencia, no por catálogo — que es exactamente
la razón de verificar antes de construir 44 laboratorios.

**Repetir esta verificación 2 semanas antes de cada dictado:** la disponibilidad de un modelo en
los *inference providers* de Hugging Face puede cambiar entre ediciones.

---

## Riesgos vivos, por criticidad

### 🟠 Altos

| # | Riesgo | Estado de la mitigación |
|---|---|---|
| **R2** | Cuotas del free tier de Hugging Face con 15-30 alumnos | **Sin verificar**. Agravado por R18. *Acción de Javier* |
| **R18** | El modelo es un 32B denso, no el MoE barato | Consume más cuota por llamada. Verificar límites antes del dictado |
| **R5** | Límites del free tier de HF Spaces | **Sin verificar**. Alternativa Render preparada |
| **R14** | El simulador es punto único de fallo | Resuelto en código (modo degradado `DATA_SOURCE=csv`). Falta desplegarlo |

### 🟡 Medios

| # | Riesgo | Estado |
|---|---|---|
| **R11** | Bucle ReAct: la fiabilidad se compone a lo largo del agente | 🟡 **Medible** — `docente/matriz_seleccion.py` construido y probado. Falta correrlo contra el endpoint real (80 llamadas) |
| **R15** | Dedicación de 12 h semanales del alumno | Declarar antes de la inscripción |
| **R16** | Aprovisionamiento de cuentas | Qdrant en semana 3, Langfuse en semana 5. Cerrar todo en semana 0 |
| **R17** | Modo *thinking* de Qwen3 activo por default del proveedor | `HF_ENABLE_THINKING=false` fijado explícitamente en `provider.py` |
| **R6** | El PDF nombra LangSmith y el curso usa Langfuse | Documentar la equivalencia en el sílabo |
| **R9** | Dependencia de 5 servicios SaaS | Verificación antes de cada sesión con `check_stack` |

### 🟢 Resueltos o disueltos

`R1` tool calling ✅ · **`R10` structured output ✅ (nuevo)** · `R3` equipos de 2 · `R7` horas ·
`R12` el agente no recupera · ~~`R13`~~ contradicción modelo-datasets · `R4` free tier de Qdrant ·
`R8` preview de `langchain-azure-ai`

---

## Lo construido para cerrar R10 y R11 · 2026-09-10

| Artefacto | Riesgo | Qué hace | Verificación |
|---|---|---|---|
| `comun/structured.py` | **R10** | La regla A3 como código: valida contra el esquema Pydantic, reintenta una vez devolviéndole al modelo **el error concreto** que cometió, y lanza `ExtraccionFallida` en vez de propagar un `None` que revienta tres líneas más abajo | `docente/verificar_structured.py` — **36/36 en verde**, con modelo simulado, sin credenciales |
| `docente/matriz_seleccion.py` | **R11** | La regla A1 como número: **20 consultas por track** (12 directas, 4 confusables, 4 que **no** deben llamar a ninguna tool) → matriz de confusión, umbral 85 % y un diagnóstico que dice **qué docstring corregir** | Modo `--simular` probado: pasa con 90 %, y falla con salida `1` cuando se le inyectan más errores |
| `CLAUDE.md` | — | Contexto de arranque para sesiones de Claude Code: regla #0 de Javier, restricciones P1-P6, decisiones que no se renegocian, índice de `_memoria/` y comandos de verificación | — |

> **Por qué la matriz importa más que el porcentaje.** "El modelo elige mal" no se puede
> corregir. *"Eligió `get_data_usage` 3 veces donde esperábamos `get_customer_plan`"* sí: se
> separan esas dos docstrings diciendo en cada una cuándo NO usarla. El script imprime esa
> recomendación por ti.

---

## Reparto de responsabilidades

### Acciones de Javier

| # | Acción | Resuelve | Tiempo | Estado |
|---|---|---|---|---|
| 1 | Ejecutar `check_stack --candidatos` | **R1** | 15 min | ✅ **Hecho** |
| 2 | Ejecutar `matriz_seleccion.py` contra el endpoint real | **R11** | 10 min · 80 llamadas | Pendiente |
| 3 | Verificar límites del free tier de HF Inference y Spaces | R2, R5, R18 | 20 min | Pendiente |
| 4 | Desplegar el simulador en HF Spaces y repartir API keys | R14 | 1 h | Pendiente |
| 5 | Declarar las 12 h semanales antes de la inscripción | R15 | — | Pendiente |

### Construcción pendiente

Ninguna de los riesgos altos. Lo siguiente es contenido: **Fase 3 · Módulo 1 · sesiones 1-3**
(27 archivos: READMEs, conceptos previos, demos, laboratorios L1-L3 en los 4 tracks, soluciones
y el enunciado del Assignment A1).

---

## Calendario vigente

**6 semanas · 12 sesiones · 72 horas · 2 sesiones semanales de 3 h · 12 h/semana por alumno**

| Semana | Sesiones | Hito |
|---|---|---|
| 0 | Nivelación asíncrona | Cuentas, entorno y equipos listos |
| 1 | S1, S2 | Test 1 y 2 · elección de track |
| 2 | S3, S4 | **Assignment A1** · 100 % del Módulo 1 |
| 3 | S5, S6 | Qdrant operativo · guardrails |
| 4 | S7, S8 | **Proyecto M2** · 100 % del Módulo 2 |
| 5 | S9, S10 | Langfuse operativo · evaluación |
| 6 | S11, Seminario | **Proyecto Integrador** · 100 % del Módulo 3 |

Bonus de Foundry: asíncrono, opcional, no ponderado.

---

## Estado de construcción

| Fase | Bloque | Estado |
|---|---|---|
| 0 | Diseño curricular | ✅ |
| 1 | Cimientos técnicos | ✅ |
| 2 | Nivelación · Sesión 0 | ✅ |
| 2B | Simulador de industria | ✅ |
| **2C** | **Mitigación de riesgos técnicos (R10, R11)** | ✅ **nuevo** |
| **3** | **Módulo 1 · sesiones 1-3** | ⬜ **siguiente** |
| 4 | Módulo 2 · sesiones 4-7 | ⬜ |
| 5 | Módulo 3 · sesiones 8-11 | ⬜ |
| 6 | Bonus Foundry | ⬜ |
| 7 | Materiales del docente | ⬜ |
