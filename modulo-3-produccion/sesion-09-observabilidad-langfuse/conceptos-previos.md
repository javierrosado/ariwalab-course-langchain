# Conceptos previos — Sesión 9

> Pre-work de 1 h. Tráelo resuelto: la sesión en vivo lo asume leído.

---

## 1. Observabilidad: logs vs métricas vs trazas

Ver README.md §1. La mayoría de quien llega a esta sesión solo ha usado logs (`print`,
`logging`). Hoy conoces el tercer pilar: trazas distribuidas.

## 2. Traza distribuida: *span*, *trace id*, jerarquía

Un *trace* agrupa todo lo que pasó al atender una petición; cada *span* es una unidad de
trabajo dentro de ese trace (una llamada al modelo, una tool, una consulta a Qdrant), con
relación padre-hijo. Un run de tu agente **es exactamente eso**: un trace con varios spans
anidados.

## 3. OpenTelemetry, nociones

Langfuse habla el protocolo **OTel** (OpenTelemetry), el estándar de facto de trazabilidad en
la industria — es el puente conceptual hacia el Curso 2 (Azure Monitor y Application Insights
también hablan OTel). Hoy no configuras OTel a mano: el SDK de Langfuse lo hace por ti.

## 4. Percentiles: p50 y p95, y por qué no el promedio

- **p50** (mediana): la mitad de las peticiones fue más rápida que este valor.
- **p95**: el 95 % de las peticiones fue más rápida que este valor — lo que vive el peor caso
  frecuente (no el peor caso absoluto, que sería p100/máximo).

El promedio se distorsiona con un solo valor extremo (un *cold start*); los percentiles, no.
Ver README.md §3.

## 5. *Callback handler* de LangChain

LangChain expone un mecanismo de *callbacks*: objetos que se "enganchan" a la ejecución de un
`Runnable` (un modelo, una tool, una cadena) y reciben eventos (`on_llm_start`, `on_tool_end`,
etc.) sin que el código del Runnable sepa que están ahí. Es exactamente cómo se instrumenta hoy:
**sin tocar la lógica del agente**, solo pasando `config={"callbacks": [...]}` en cada
`.invoke()`.

## 6. Qué es PII dentro de una traza

Una traza de agente guarda, por defecto, **los mensajes completos**: el prompt del sistema, lo
que escribió el cliente, y lo que respondió el modelo. Si el cliente escribió su DNI o su
número de tarjeta en la conversación, ese dato queda en la traza tal cual — a menos que se
enmascare antes de exportar. Es el contenido del bloque 4 del README.

---

## Verificación de entrada

```bash
python -m comun.check_stack
```

Debe pasar en verde la comprobación de Langfuse (nº 8). La cuenta se creó en la Sesión 0; el
plan Hobby admite 2 usuarios por proyecto (los equipos del curso son de dos personas).
