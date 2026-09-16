# Sesión 1 — Fundamentos de los agentes inteligentes

> Módulo 1 · Semana 1 · martes · **3.5 h teoría + 2.5 h práctica = 6 h**
> Reparto: 1 h pre-work + 3 h en vivo (2.5 h teoría / 0.5 h práctica) + 2 h de laboratorio.

Antes de esta sesión debiste completar la **Sesión 0** (`00-preparacion/`) y su autoevaluación
con 8 aciertos o más. Si no la hiciste, vuelve ahí: nada de lo que sigue tiene sentido sin esa
base.

---

## 1. Objetivos de aprendizaje

Al terminar esta sesión puedes:

1. Explicar por qué **un LLM solo no es un agente**, nombrando las cuatro piezas que le faltan.
2. Decidir, ante un problema dado, si necesitas un **workflow** o un **agente** — y justificarlo.
3. Situar cada objeto de LangChain 1.x (`model`, `message`, `tool`, `agent`, `middleware`) en el
   mapa de las 12 sesiones del curso.
4. Ejecutar un script que llama a un modelo de pesos abiertos **en línea**, sin instalar ningún
   motor de inferencia en tu laptop.
5. Explicar qué hace `comun/provider.py` y por qué ningún archivo del curso instancia el modelo
   directamente.

Los objetivos 1 y 2 se verifican con el **Test 1** (al final de esta sesión, ver
[`conceptos-previos.md`](conceptos-previos.md)); los objetivos 4 y 5, con el laboratorio **L1**.

---

## 2. El antipatrón que esta sesión tiene que romper

> **Llegas con 10 años de experiencia como ingeniero de software y asumes, sin pensarlo, que un
> LLM es una API determinística: mismos parámetros, misma respuesta.** Si esa expectativa no se
> rompe hoy, la arrastras hasta la sesión 10, cuando intentes evaluar tu agente con
> `assert respuesta == "esperado"` y el test falle siempre, incluso cuando el agente responde
> bien.

Se rompe con una demo en vivo, no con una diapositiva: el docente le pregunta al modelo una
tarifa de AndesMóvil dos veces seguidas, y el modelo responde con **total seguridad** dos cifras
distintas — ninguna real, porque el modelo nunca tuvo acceso al tarifario. El resto de esta
sesión explica **por qué** pasa esto, y las diez sesiones siguientes construyen las defensas
(tools, RAG, guardrails, evaluación).

---

## 3. Un LLM solo no es un agente

Un modelo de lenguaje, solo, hace una cosa: recibe texto y devuelve texto. No sabe si acertó, no
recuerda la conversación anterior salvo que se la reenvíes completa, y no puede tocar ningún
sistema tuyo. Le faltan cuatro piezas para convertirse en agente:

```
   LLM suelto                        Agente
   ──────────                        ──────
   texto → texto                     texto → [razonar → actuar → observar]* → texto
                                                    │
        ¿qué le falta?                              ├── HERRAMIENTAS  el dato sale de tu sistema      (S3, S4)
        ────────────────                            ├── MEMORIA       recuerda la conversación        (S5)
                                                    ├── OBJETIVO      sabe cuándo terminó             (S4)
                                                    └── CONTROL       límites de lo que puede hacer   (S6)
```

Cada pieza se etiqueta con la sesión que la construye. Este diagrama es el mapa del curso: se
repite en la apertura de las sesiones 3, 4, 5 y 6, así que vale la pena entenderlo hoy.

- **Herramientas** — sin ellas, el modelo solo puede *inventar* que consultó tu sistema. Con
  ellas, de verdad consulta el plan del cliente, el saldo de la cuenta o el estado del pedido.
- **Memoria** — el modelo es *stateless*: si no le reenvías la conversación, no sabe que ya te
  presentaste. "Recordar" es, en realidad, tu código reenviando el historial en cada llamada.
- **Objetivo** — un agente necesita un criterio para saber cuándo terminó la tarea. Sin eso, o se
  detiene demasiado pronto o repite pasos indefinidamente.
- **Control** — límites explícitos de lo que el agente puede y no puede hacer. Sin control, un
  agente de banca podría "decidir" que ejecutar una transferencia es el siguiente paso lógico.

---

## 4. Agente = percepción → razonamiento → acción → entorno

El marco que vas a usar todo el curso para describir cualquier agente, en cualquier industria:

```
        ┌────────────────────────────────────────────────────┐
        │                                                      │
        ▼                                                      │
   PERCEPCIÓN ──────► RAZONAMIENTO ──────► ACCIÓN ──────► ENTORNO
   lee el mensaje      el LLM decide       llama a una     el sistema real
   del usuario y        el próximo paso     tool, responde   responde: CRM,
   el estado actual     con el contexto     al usuario, o    base de datos,
   de la conversación   que tiene           pide más datos   API externa
                                                              │
        └─────────────────── observa el resultado ◄──────────┘
```

El bucle se repite mientras el agente lo considere necesario (por eso el `*` del diagrama de la
sección 3): cada vuelta es una oportunidad para razonar mejor con más información, y también una
oportunidad para acumular error si algo no está bien diseñado (retoma esta idea en la sección 6).

**El mismo marco en las 4 industrias del curso:**

| Industria | Percepción | Razonamiento | Acción | Entorno |
|---|---|---|---|---|
| **AndesMóvil** (telco) | "Se me acabaron mis gigas y no sé por qué" | Decide que necesita el consumo real antes de responder | Llama a `get_data_usage` | El sistema de facturación devuelve el consumo del ciclo actual |
| **Banco Inti** (banca) | "Hay un cargo que no reconozco" | Decide evaluar el riesgo antes de tranquilizar o alertar | Llama a `score_transaction_risk` | El motor de riesgo devuelve un puntaje y una recomendación |
| **MercaSur** (retail) | "Mi pedido no ha llegado" | Decide que necesita el estado real del envío | Llama a `track_order` | El courier devuelve el último evento de tracking |
| **Andina Seguros** (seguros) | "Choqué y no sé qué hacer" | Decide que debe guiar el reporte, no improvisar coberturas | Llama a `open_claim` y consulta el condicionado | El sistema registra el expediente y el RAG devuelve la cláusula aplicable |

> Fíjate en que en los cuatro casos el modelo **no responde de memoria**: percibe, decide que le
> falta un dato real, actúa para conseguirlo, y recién entonces responde. Ese es el patrón que
> vas a construir de la sesión 3 en adelante.

---

## 5. Workflow vs agente — cuándo NO necesitas un agente

Esta es, para un ingeniero de software, la distinción más práctica de la sesión: **construir un
agente cuando un workflow te alcanza es más caro, más lento y menos predecible sin ninguna
ganancia a cambio.** La mitad de los casos reales de un curso de agentes... no necesitan agente.

| Si… | Necesitas | Por qué |
|---|---|---|
| Los pasos son siempre los mismos | **Workflow** | Más barato, más rápido, depurable con un debugger normal |
| El orden depende de lo que responda el usuario | **Agente** | El modelo decide la ruta en cada turno |
| Hay que garantizar que un paso ocurra siempre (p. ej. registrar el reclamo) | **Workflow** | Un agente *puede* saltárselo si "decide" que no hace falta |
| El número de pasos no se conoce de antemano | **Agente** | El bucle termina cuando el objetivo se cumple, no en un paso fijo |

> **Mensaje que te tienes que llevar hoy:** un agente es más caro, más lento y menos predecible
> que un workflow. Solo se justifica cuando la ruta no se puede escribir de antemano con un
> `if/else`. Si puedes dibujar el diagrama de flujo completo antes de escribir código, no
> necesitas un agente — necesitas un workflow, y probablemente te vaya mejor con uno.

---

## 6. Anatomía de LangChain 1.x — dónde estás parado en el mapa del curso

LangChain 1.x organiza todo alrededor de cinco objetos. Esta tabla es tu mapa de las 12
sesiones: cuando en la sesión 5 aparezca "middleware" por primera vez en código, vuelve aquí.

| Objeto | Qué es | Cuándo lo usas por primera vez |
|---|---|---|
| `model` | La abstracción de "un LLM que responde", sin importar el proveedor | **Hoy**, vía `comun/provider.py` |
| `message` | `system` / `human` / `ai` / `tool`: el modelo mental de toda conversación | **Hoy** (demo 2) y a fondo en la S2 |
| `tool` | Una función de tu código que el modelo puede pedir que se ejecute | S3 |
| `agent` | El bucle que encadena `model` + `tool` + `message` hasta cumplir un objetivo | S3 (`create_agent()`) |
| `middleware` | Interceptores que se ejecutan antes/después de cada paso del agente (guardrails, logging) | S6 |

No memorices esta tabla: vuelve a ella cada vez que empieces una sesión nueva del módulo 1 y 2.

---

## 7. Modelos abiertos vs cerrados — y cómo se eligió el de este curso

El curso usa **modelos de pesos abiertos** ("open-weights"): los parámetros del modelo son
descargables y auditables, a diferencia de un modelo cerrado (GPT, Claude, Gemini) donde solo
consumes una API. Esto no es una preferencia ideológica: es la restricción **P1** del curso
(100 % open source), y tiene una consecuencia técnica directa que vas a comprobar tú mismo en el
laboratorio de hoy.

**Cómo se eligió `Qwen/Qwen3-32B`: midiendo, no por catálogo.** Se probaron 4 candidatos contra
el endpoint real de Hugging Face con `check_stack --candidatos`, verificando dos cosas críticas
para un curso de agentes: que el modelo soporte **tool calling** de forma confiable y que
sostenga el **bucle ReAct** (razonar → actuar → observar, la sección 4 de hoy) sin romperse.

| Candidato | ¿Pasó tool calling + ReAct? |
|---|---|
| `Qwen/Qwen3-32B` | ✅ **Sí — el único de los 4** |
| `Qwen/Qwen3-30B-A3B` | ❌ No |
| `Qwen/Qwen3-8B` | ❌ No |
| `meta-llama/Llama-3.3-70B-Instruct` | ❌ No |

Esta es la decisión **D28** del curso, y la razón de que el `.env` traiga
`HF_ENABLE_THINKING=false`: Qwen3 alterna entre modo "pensando en voz alta" y modo directo, y el
modo directo es el que no interfiere con el parseo de las llamadas a herramientas. Si algún día
te preguntas por qué el curso no usa "el modelo más grande" o "el más nuevo", la respuesta está
aquí: se usa el que **demostradamente funciona** para lo que este curso necesita.

> Nota importante para las próximas 10 sesiones: **las 4 industrias comparten este mismo
> modelo** (decisión D21). Nada de fine-tuning por sector. Lo que hace que el agente "suene a"
> AndesMóvil o a Banco Inti es el *system prompt* de `comun/prompts_industria.py`, no los pesos
> del modelo — lo vas a comprobar tú mismo con la demo 3 de hoy.

---

## 8. `comun/provider.py` — la indirección que hace posible todo lo demás

Ningún archivo de este curso escribe `ChatOpenAI(...)` directamente ni llama a `os.getenv(...)`.
Todo pasa por dos funciones:

```python
from comun.provider import get_chat_model, describe_provider

print(describe_provider())          # una línea legible: proveedor, track, modelo, URL
modelo = get_chat_model()           # devuelve un ChatOpenAI ya configurado
respuesta = modelo.invoke("¿Qué es un agente de IA?")
print(respuesta.content)
```

`get_chat_model()` decide, según `AI_PROVIDER` en tu `.env`, si construye el cliente contra el
router de Hugging Face o contra un endpoint de Microsoft Foundry — pero desde afuera es
exactamente el mismo objeto `ChatOpenAI`. Esta indirección es la decisión **D13**, y es la razón
de que el bonus asíncrono de Foundry (módulo 4, opcional) no requiera reescribir ni una línea de
tu agente: solo cambia una variable de entorno.

**Por qué te importa esto desde el día 1 y no solo en el bonus:** si en tu laboratorio de hoy
escribes `ChatOpenAI(model=...)` en vez de `get_chat_model()`, tu script funciona igual — hasta
que en el módulo 4 tengas que cambiar de proveedor y descubras que el cambio no es "una
variable", sino "buscar y reemplazar en cada archivo". El criterio de aceptación de tu
laboratorio lo revisa explícitamente.

---

## 9. Qué vas a hacer hoy, en orden

| Bloque | Contenido |
|---|---|
| Apertura | Ver la app final funcionando y el mapa de las 6 semanas |
| Demo del antipatrón | La tarifa inventada dos veces (sección 2) |
| Teoría | Secciones 3 a 8 de este documento |
| Práctica en vivo | `describe_provider()` y tu primer llamado al modelo, con el docente |
| **Test 1** | 10 preguntas — ver [`conceptos-previos.md`](conceptos-previos.md) |
| **Elección de track** | Tu equipo propone, el docente balancea — ver abajo |
| Laboratorio **L1** | Entorno verde + tu propio `primer_contacto.py` — ver [`lab/`](lab/) |

---

## 10. Elección de track — el equipo propone, el docente balancea

Al cerrar esta sesión, cada equipo de 2 personas declara el track sobre el que va a construir
**todos** los laboratorios, del L2 al L11: telecomunicaciones (AndesMóvil), banca (Banco Inti),
retail (MercaSur) o seguros (Andina Seguros). El docente ajusta la propuesta solo si hace falta,
para que los 4 tracks queden representados en la sustentación final y para que Banca —el más
exigente en guardrails y structured output— no caiga en el equipo con menos experiencia. El
track es **irrevocable** una vez asignado.

Si quieres ver el detalle de los 4 casos de uso antes de proponer uno, revisa
`docente/casos-de-uso-industrias.md`.

---

## 11. Qué NO entra en esta sesión

Para que sepas qué esperar (y qué no) del laboratorio de hoy:

| No entra hoy | Cuándo se ve |
|---|---|
| `@tool`, function calling | Sesión 3 |
| Pydantic y structured output | Sesión 2 |
| `create_agent()` | Sesión 3 |
| Plantillas de prompt, few-shot | Sesión 2 |
| El simulador de industria | Sesión 3 |
| Qdrant y Langfuse (más allá de tener la cuenta creada) | Sesión 5 y Sesión 9 |
| MCP | Sesión 4 |

La palabra "agente" se explicó en las secciones 3 y 4, pero **no vas a construir uno hoy**. Hoy
construyes el cimiento: un script que llama al modelo correctamente, sin instalar nada en tu
laptop. El primer agente real es el de la Sesión 3.

---

## 12. Siguiente paso

1. Si no lo hiciste, completa el pre-work de 1 h: [`conceptos-previos.md`](conceptos-previos.md).
2. Después de la sesión en vivo, ve al laboratorio: [`lab/`](lab/).
3. Si te bloqueas, revisa primero la tabla de errores esperables en `conceptos-previos.md` y en
   el `README.md` de `code/`.
