# Assignment A1 · 100 % del Módulo 1

> El Laboratorio 3 **es** el Assignment A1: no hay un enunciado separado del laboratorio, este
> documento es la envoltura formal — entregables, rúbrica, calendario y regla del piso.

---

## Qué resuelve

Tu primera tool contra el simulador real, con los 3 escenarios de una integración real: éxito,
dato inexistente y servicio caído. Es la primera vez que tu agente consulta un dato real en vez
de inventarlo — la alucinación de la Sesión 1 termina aquí.

Ver [`lab/README.md`](lab/README.md) para el enunciado técnico completo (tu tool según tu
track, los 3 escenarios, cómo provocarlos).

---

## Qué se entrega

| Entregable | Ruta | Para qué |
|---|---|---|
| `tools/external_api.py` | tu proyecto | La tool, con docstring A2 y `args_schema` |
| `agent.py` v1 | tu proyecto | `create_agent()` con esa tool y el prompt de tu track |
| `prueba_tool.py` | tu proyecto | Los 3 escenarios llamando la tool directamente, sin modelo |
| `EVIDENCIA-A1.md` | tu proyecto | Las 3 trazas reales pegadas + qué se decidió (plantilla: [`lab/plantilla-evidencia-a1.md`](lab/plantilla-evidencia-a1.md)) |

---

## Rúbrica · 4 niveles × 5 criterios

Ver el detalle completo con los 4 niveles por criterio en
[`recursos/rubricas/rubrica-a1.md`](../../../recursos/rubricas/rubrica-a1.md). Resumen de pesos:

| Criterio | Peso |
|---|---|
| Funcionalidad | 30 % |
| Diseño de tool y prompt | 25 % |
| Manejo de errores | 25 % |
| Evidencia | 10 % |
| Comunicación técnica | 10 % |

> ⚠️ **El criterio "observabilidad" de la rúbrica institucional no aplica todavía** — Langfuse
> entra en la Sesión 9. Aquí su lugar lo ocupa **Evidencia**.

---

## La regla del piso

> Si `prueba_tool.py` pasa los 3 escenarios y la docstring cumple la regla A2 (verbo · cuándo
> usarla · cuándo NO), tu equipo **no baja de Competente** en Funcionalidad, aunque en la
> sustentación en vivo el modelo no haya elegido la tool.

**Por qué existe esta regla.** Con 93 % de acierto por llamada (la cifra medida en D20), una
tarea de tres pasos sale bien el 80 % de las veces. Penalizar a tu equipo por la varianza del
modelo enseñaría exactamente lo contrario de lo que este curso quiere enseñar. Lo que sí se
evalúa es si diseñaste el sistema para que esa varianza no se convierta en un fallo silencioso —
y `prueba_tool.py` es justamente la prueba de que lo hiciste.

---

## Calendario de entrega y sustentación

| Momento | Qué |
|---|---|
| **Martes** (Sesión 3), 2 h de laboratorio | Se construye la tool y se corren los 3 escenarios |
| **Miércoles 23:59** | Entrega del paquete completo (código + `EVIDENCIA-A1.md`) |
| **Jueves** (Sesión 4), primeros 20 min | Sustentación de **4 equipos, uno por track**, 5 min cada uno |

> **Por qué solo 4 equipos sustentan, no todos.** Con 8-15 equipos a 5 min cada uno, la
> sustentación tomaría 40-75 min y se comería la sesión del catálogo de tools. Por eso sustentan
> 4 equipos —uno por track— en rotación: los demás entregan el paquete y el docente califica de
> forma asíncrona. A lo largo del curso (A1 · Proyecto M2 · Proyecto Integrador) cada equipo
> sustenta al menos una vez, y el aula ve las 4 industrias en cada hito.

---

## Reto opcional · no evaluado

`?_fallo=malformado` — un `200` con un JSON que no cumple el contrato esperado. Es el más
difícil porque no hay código de error: solo se detecta validando la forma de la respuesta. Es el
puente natural hacia los guardrails de la Sesión 6.
