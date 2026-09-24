# Sesión 3 — Herramientas, integración externa y Assignment A1

> Semana 2 · martes · **2.5 h teoría + 3.5 h práctica = 6 h**. Es la sesión más cara del módulo:
> la primera que toca el simulador de verdad, la primera con tool calling real, y su laboratorio
> **es** la nota del Módulo 1.

**Bloqueante con fecha (responsabilidad del docente):** simulador desplegado y respondiendo
`/health`, API key de tu equipo repartida, `CHAOS_RATE=0.0` confirmado — los tres, antes de esta
sesión. Sin ellos no hay L3, y sin L3 no hay Assignment A1.

---

## 1. Objetivos de aprendizaje

1. Explicar quién **genera** la llamada a la herramienta y quién la **ejecuta** — y por qué esa
   separación es toda la seguridad del sistema.
2. Escribir una docstring que haga que el modelo elija bien: verbo, cuándo usarla, **cuándo NO**.
3. Definir el `args_schema` de una tool con Pydantic.
4. Manejar los 3 escenarios de una integración real: éxito, dato inexistente y servicio caído.
5. Redactar un error **para que lo lea el modelo**, no para que lo lea un humano en un log.
6. Explicar qué hace `create_agent()` por dentro, habiendo visto el bucle escrito a mano.

---

## 0. Hoy el modelo deja de saber y empieza a consultar

En la Sesión 1 viste al modelo alucinar una tarifa con total seguridad. Hoy eso se acaba: tu
agente va a consultar un dato real, de un sistema real, en vez de inventarlo.

---

## 1. Function calling: quién genera y quién ejecuta

```
   ┌──────────┐   1. pregunta          ┌──────────┐
   │ Usuario  │ ─────────────────────► │  MODELO  │
   └──────────┘                        └────┬─────┘
                                            │ 2. NO ejecuta nada.
                                            │    Propone: {"name": "get_customer_plan",
                                            │               "args": {"numero_linea": "987654321"}}
                                            ▼
                                     ┌─────────────┐
                                     │  TU CÓDIGO  │ 3. decide si la ejecuta,
                                     │             │    valida los argumentos,
                                     └──────┬──────┘    aplica permisos
                                            │ 4. HTTP GET
                                            ▼
                                     ┌─────────────┐
                                     │  SIMULADOR  │
                                     └──────┬──────┘
                                            │ 5. el resultado vuelve como mensaje `tool`
                                            ▼
                                        MODELO redacta la respuesta final
```

> **El paso 3 es toda la seguridad del sistema.** El modelo nunca toca la red, la base de datos
> ni el disco: solo escribe una intención en JSON. Si alguien lo convence de pedir algo
> indebido, quien decide sigue siendo tu código. Esta idea se retoma entera en la Sesión 6
> (guardrails) — vas a volver a ver este mismo diagrama, leído como defensa de seguridad.

---

## 2. La docstring es el prompt (regla A2)

```python
# ANTES — el modelo no sabe cuándo usarla
@tool
def get_customer_plan(numero_linea: str) -> str:
    """Obtiene información del cliente."""

# DESPUÉS — regla A2
@tool
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene, si su línea está activa
    o en qué distrito está registrada.

    NO la uses para consultar consumo de datos (usa get_data_usage) ni para
    registrar un reclamo (usa create_complaint_ticket). No sirve para
    preguntas sobre tarifas o precios: eso está en la base de conocimiento.
    """
```

La docstring **es** lo que el modelo lee dentro del esquema de la tool — no es documentación
para otro programador, es el prompt que decide si el modelo la elige bien. Y la calidad de esa
docstring es un número medible: `docente/matriz_seleccion.py` te lo muestra desde el L4, pero el
hábito se construye hoy, con una sola tool.

---

## 3. Errores redactados para el modelo (regla A4)

| Situación | ❌ Para un humano | ✅ Para el modelo |
|---|---|---|
| 404 | `raise KeyError("not found")` | `"No existe una línea con el número 999999999 en AndesMóvil. Verifica el número con el cliente."` |
| 401 | `raise HTTPError(401)` | `"Credencial rechazada (401). Reintentar no soluciona un 401."` |
| 503 | traceback completo | `"El servicio de AndesMóvil no responde en este momento. Informa al cliente y ofrece reintentar más tarde."` |

`comun/api_client.py` traduce errores HTTP para la capa de datos. Se introduce al conectar el
simulador en esta sesión; el L1 solo consumía el modelo. Hoy escribes el `try/except` de **tu propia** tool con el mismo criterio — no lo
copias, lo reproduces.

---

## 4. Del bucle manual a `create_agent()`

Un agente no es magia: es un `while` que tú podrías escribir. La demo 3 de `code/` te lo muestra
en ~20 líneas — invoca al modelo, si propuso una tool_call la ejecuta, le devuelve el resultado,
repite hasta que el modelo responde texto o se agota el tope de iteraciones. `create_agent()`
hace exactamente eso en 3 líneas. **La abstracción no añade inteligencia: quita código
repetido.** Vas a necesitar haber visto el bucle a mano para poder diagnosticar un agente que se
cuelga en la Sesión 4.

---

## 5. Las 4 demos y el laboratorio

Ver [`code/README.md`](code/README.md) para las demos y [`lab/README.md`](lab/README.md) para
el Laboratorio 3, que **es** el [Assignment A1](assignment-a1.md).

---

## `proyecto-final/`: recordatorio

`proyecto-final/<track>/` en este repositorio es la referencia del docente. Tu tool de hoy va en
tu propio proyecto — y es, literalmente, la primera pieza de `domain_tools.py`, el catálogo que
vas a completar en el Laboratorio 4. No es un ejercicio aislado: es el primer cuarto del trabajo
de la Sesión 4.

---

## Qué NO entra hoy

| No entra | Va en |
|---|---|
| Catálogo de varias tools y selección dinámica | Sesión 4 |
| MCP | Sesión 4 (pre-work asíncrono) |
| Tools de **escritura** (crear reclamo, abrir siniestro) | Sesión 4 |
| Memoria conversacional y RAG | Sesión 5 |
| Guardrails, PII, prompt injection | Sesión 6 |
| Langfuse y trazabilidad | Sesión 9 |

> El L3 usa **una sola tool y de lectura**. La primera tool que escribe algo llega en el L4, ya
> con el hábito de manejar errores que construyes hoy.
