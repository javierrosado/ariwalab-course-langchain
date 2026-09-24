# Sesión 1 — Fundamentos de los agentes inteligentes

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-01.md`.

---

## Sesión 1 · Fundamentos de los agentes inteligentes
- Semana 1 · martes · 6 h (3.5 T / 2.5 P)
- Hitos: Test 1 · elección de track
- Hoy: por qué un LLM solo no es un agente

---

## Apertura y mapa del curso
- Qué construirán en 6 semanas
- Mostrar la app final funcionando (demo del docente)

---

## Un LLM solo no es un agente
- Demo en vivo: preguntar dos veces una tarifa de AndesMóvil → dos cifras distintas, ninguna real
- Las 4 piezas que le faltan: herramientas, memoria, objetivo, control
- Cada pieza se etiqueta con la sesión que la construye (S3-S6)

---

## Agente = percepción → razonamiento → acción → entorno
- El bucle que se repite en cada turno
- Ejemplo en las 4 industrias del curso

---

## Workflow vs agente
- Pasos siempre iguales → workflow (más barato, más rápido, depurable)
- Orden depende del usuario → agente
- Un agente es más caro, más lento y menos predecible: solo se justifica cuando la ruta no se
  puede escribir de antemano

*(Pausa · 10 min)*

---

## Anatomía de LangChain 1.x
- `model` · `message` · `tool` · `agent` · `middleware`
- En qué sesión se ve cada uno

---

## Modelos abiertos vs cerrados
- Pesos abiertos: parámetros públicos y auditables
- `Qwen/Qwen3-32B`: verificar disponibilidad y Tool Calling antes de las prácticas

---

## `comun/provider.py` en vivo
- `describe_provider()` y el primer llamado
- Por qué ningún archivo instancia el modelo directamente
- La indirección es lo que hace posible el bonus de Foundry sin reescribir código

---

## Test 1 + elección de track
- 10 preguntas, en clase
- Cada equipo declara su track — el docente balancea para que los 4 estén representados

---

## Qué NO entra hoy
- `@tool`, function calling → S3
- Pydantic y structured output → S2
- `create_agent()` → S3
- El simulador de industria → S3
- MCP → S4
