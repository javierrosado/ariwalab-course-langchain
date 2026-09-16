# Conceptos previos · Sesión 4

> Pre-work asíncrono de 1 h. La parte de MCP está en su propio archivo:
> [`pre-work-mcp.md`](pre-work-mcp.md) (30 min de práctica). Esto de aquí es el resto.

---

## 1. Patrón ReAct: Thought → Action → Observation

Es lo que `create_agent()` hace por dentro, y lo que ya viste como "bucle manual" en la Sesión 3:

```
   Thought      el modelo razona qué necesita hacer
   Action       el modelo propone una tool_call (no la ejecuta: la propone)
   Observation  tu código ejecuta la tool y le devuelve el resultado
   (se repite hasta que el modelo tiene lo que necesita para responder)
```

Con 4 tools en vez de 1, cada vuelta del bucle es una nueva oportunidad para que el modelo elija
mal. Por eso hoy se mide la selección, no se asume.

## 2. Bucle de agente y límite de iteraciones

Un bucle sin límite es un riesgo operativo, no solo un detalle de estilo: si el modelo no logra
resolver la tarea, puede seguir llamando tools indefinidamente. Un límite explícito de
iteraciones (regla A4) convierte "el agente se cuelga" en "el agente avisa y deriva" — la
diferencia entre un incidente silencioso y uno manejado.

## 3. `async`/`await` en Python — lo mínimo para hoy

MCP usa clientes asíncronos (`await cliente.get_tools()`). No necesitas dominar `asyncio` a
fondo: para el pre-work de hoy basta con saber que una función `async def` se llama con `await`
dentro de otra función `async`, y que un script que solo usa `await` en su punto de entrada se
ejecuta con `asyncio.run(main())`. Se refuerza a fondo en la Sesión 5 y en el reto opcional del L4.

## 4. Diseño de interfaces / responsabilidad única (SRP)

El mismo principio que ya conoces de diseño de software aplicado a tools: una tool, una
responsabilidad. Si te cuesta nombrar una tool con un solo verbo y un solo sustantivo
(`get_data_usage`, no `handle_line_stuff`), probablemente está haciendo más de una cosa.

## 5. Idempotencia de operaciones

Una operación es idempotente si ejecutarla dos veces produce el mismo resultado que ejecutarla
una vez. Un agente puede invocar la misma tool más de una vez en una conversación (por ejemplo,
si el usuario repite la pregunta) — para las tools de **lectura** eso es inofensivo; para las de
**escritura**, no. Ver `README.md` sección 4.

---

## Verificación antes de la sesión

- [ ] Completaste `pre-work-mcp.md` y tu agente pudo listar las 6 tools del servidor MCP.
- [ ] Tienes tu Assignment A1 listo para sustentar (5 min, con el resto del equipo).
- [ ] Repasaste tu `domain_tools.py` del L3: es la base sobre la que hoy añades tres tools más.
