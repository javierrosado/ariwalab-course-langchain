# Puente al Curso 2

> Qué sigue, y por qué se dejó fuera de aquí.

---

## Lo que este bonus movió

Una sola pieza: **el modelo**. `AI_PROVIDER=foundry` y un *hosted agent* envolviendo el mismo
grafo. Todo lo demás —Qdrant, Langfuse, el simulador de industria, tu código de tools y
guardrails— se quedó exactamente donde estaba.

## Lo que el Curso 2 mueve

El Curso 2 es **100 % Foundry**: no solo el modelo, sino la arquitectura completa alrededor de
él.

| Pieza de este curso | Qué le pasa en el Curso 2 |
|---|---|
| Qdrant Cloud | Migra a **Azure AI Search** (o se integra con Foundry directamente) |
| Langfuse Cloud | Migra a **Azure Monitor / Application Insights** (mismo protocolo OTel que ya viste en la S9 — no es un concepto nuevo, es el mismo con otro backend) |
| El simulador de industria (REST propio) | Se integra vía **Azure Functions / APIM** en vez de un servidor Flask/FastAPI aparte |
| Identidad y permisos | Se profundiza: managed identity, políticas de Azure, redes — nada de esto entró aquí a propósito |
| Guardrails escritos a mano | Se exploran alternativas gestionadas de la plataforma, sin abandonar lo aprendido en el L6 |

## Por qué se dejó así, y no se adelantó nada

Tres razones, ya conocidas del resto del curso:

1. **P1/P3**: la troncal del curso es 100 % open source; Foundry es un bonus asíncrono
   deliberadamente acotado (decisión D17).
2. **D21**: sin fine-tuning por industria, el switch de modelo es honesto y simple — adelantar
   más piezas de Azure aquí habría complicado esa demostración sin necesidad.
3. Este curso te deja con un **agente completo, portable y medido**. El Curso 2 parte de esa
   base y construye la versión "todo en Azure" — no tiene sentido construirla dos veces.

## Qué te llevas de aquí, literalmente

- Un agente que ya sabes que corre en dos proveedores distintos con un cambio de variable.
- Un vocabulario de recursos de Azure (suscripción, grupo, proyecto, deployment) que el Curso 2
  da por sabido.
- La noción de *hosted agent* y el protocolo Responses, que reaparece ahí con más profundidad
  (sesiones, interrupts, checkpointers durables).
- Un cuadro comparativo con datos propios — no una opinión prestada — sobre cuándo cada stack
  tiene sentido.
