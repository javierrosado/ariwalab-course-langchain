# Conceptos previos · Sesión 1

> **Pre-work asíncrono, 1 hora.** Hazlo antes de la sesión en vivo. No repite la Sesión 0: la da
> por sabida. Si no completaste `00-preparacion/` con 8 aciertos o más en su autoevaluación,
> detente y hazlo primero — nada de esto va a tener sentido sin esa base.

---

## 0. Lo que ya deberías saber (Sesión 0, no se repite)

| Ya sabes | Dónde lo aprendiste |
|---|---|
| Token, ventana de contexto, temperatura, alucinación, embedding, costo | [`00-preparacion/conceptos-previos/fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md) |
| `venv`, `.env`, higiene de secretos, Pydantic básico | [`00-preparacion/conceptos-previos/python-y-entorno.md`](../../00-preparacion/conceptos-previos/python-y-entorno.md) |
| Las 3 cuentas creadas (Hugging Face, Qdrant Cloud, Langfuse Cloud) y el `.env` completo | [`00-preparacion/conceptos-previos/alta-de-cuentas.md`](../../00-preparacion/conceptos-previos/alta-de-cuentas.md) |
| Las 4 demos ejecutadas (tokens, temperatura, embeddings, costo) | [`00-preparacion/code/`](../../00-preparacion/code/) |

Si a alguno de estos le falta algo, resuélvelo ahora. La Sesión 1 asume que el entorno ya está
verde.

---

## 1. Los 4 conceptos nuevos de hoy

### 1.1 *Chat completion* vs **agente**

Un *chat completion* es una sola llamada: mandas mensajes, el modelo devuelve texto, se acabó.
Un **agente** es un *chat completion* dentro de un bucle: el modelo puede decidir llamar a una
herramienta, observar el resultado, y volver a razonar antes de responderte a ti. La distinción
importa porque **todo lo que ves como "inteligencia" del agente en realidad es ese bucle**, no
una capacidad especial del modelo. Es la distinción que estructura toda la Sesión 1 (ver
[`README.md`](README.md), secciones 3 y 4).

### 1.2 El bucle percepción → razonamiento → acción

Cuatro pasos que se repiten: el agente **percibe** el mensaje y el estado actual, **razona** cuál
es el siguiente paso, **actúa** (llama a una herramienta o responde), y observa cómo reaccionó el
**entorno** a esa acción. Este esquema se usa desde el minuto 10 de la sesión en vivo — tenlo
fresco. Detalle completo en `README.md` sección 4.

### 1.3 Por qué un LLM no es una API REST

Una API REST bien diseñada es determinística: mismos parámetros, misma respuesta, y si falla,
falla con un código de error explícito (`404`, `500`, timeout). Un LLM no cumple ninguna de las
dos cosas: la misma pregunta puede dar respuestas distintas incluso a `temperature=0` (ya lo
viste en la demo 2 de la Sesión 0), y cuando "falla" —alucina un dato— no hay ningún código de
error que te avise. Este es el antipatrón que la sesión de hoy tiene que romper explícitamente
(`README.md` sección 2): si asumes que el modelo es una API REST, vas a intentar testearlo con
`assert respuesta == "esperado"`, y ese test va a fallar incluso cuando el agente responde bien.

### 1.4 Qué es un modelo de **pesos abiertos**

Un modelo de pesos abiertos ("open-weights") publica sus parámetros: se puede descargar, auditar
y, en teoría, correr en tu propia infraestructura. Un modelo cerrado (GPT, Claude, Gemini) solo
te da una API. El curso usa pesos abiertos por la restricción **P1** (100 % open source), pero
consumidos **en línea** vía Hugging Face — no instalas ningún motor de inferencia en tu laptop
(restricción **P2**). Esto justifica todo el stack que vas a usar hoy: `comun/provider.py`
apuntando al router de Hugging Face, con `Qwen/Qwen3-32B` como modelo elegido **por medición**
(decisión D28, detalle en `README.md` sección 7).

---

## 2. Antes de la sesión en vivo, verifica

- [ ] Repasé los 4 conceptos de arriba y puedo explicarlos con mis palabras.
- [ ] Mi `.env` tiene `HF_TOKEN` válido (lo usé en la Sesión 0, demos 2 y 3).
- [ ] Puedo activar mi `venv` y el prompt muestra `(.venv)`.
- [ ] Tengo en mente, sin comprometerme todavía, qué industria me interesa más: telecomunicaciones
  (AndesMóvil), banca (Banco Inti), retail (MercaSur) o seguros (Andina Seguros). La declaración
  formal es al cerrar la sesión en vivo (ver `README.md` sección 10).

---

## Test 1 · 10 preguntas

> **Se responde en clase, al cierre del bloque teórico** (bloque 7 del guion, 15 minutos), no
> como parte del pre-work — para entonces ya viste la teoría completa de la sesión. Este archivo
> es donde vive el banco de preguntas; tu docente te dirá el formato exacto de entrega
> (papel, formulario, o el que use el curso).
>
> Formato igual al de `00-preparacion/autoevaluacion.md`: opción múltiple con las respuestas
> comentadas al final, no solo la letra correcta. No hay umbral de aprobación: es una
> verificación de los objetivos 1 y 2 de la sesión (`README.md` sección 1), no un filtro de
> entrada como la autoevaluación de la Sesión 0.

---

### Parte A · Un LLM no es un agente (preguntas 1-2)

**1.** Un compañero dice: *"Mi script ya es un agente: le paso un system prompt y responde muy
bien."* ¿Qué le falta para que sea, en rigor, un agente?

- a) Nada: si responde bien, ya es un agente
- b) Un modelo más grande
- c) Un bucle de decisión y ejecución de acciones con resultados observables
- d) Un `temperature` más bajo

**2.** ¿Cuál de estas NO es una de las cuatro capacidades que el proyecto del curso añade
alrededor del modelo?

- a) Herramientas
- b) Memoria
- c) Un vocabulario más grande
- d) Control

---

### Parte B · Percepción → razonamiento → acción → entorno (preguntas 3-4)

**3.** Un cliente de AndesMóvil escribe *"se me acabaron mis gigas y no sé por qué"*. El agente
decide que necesita el consumo real del ciclo antes de responder, y llama a `get_data_usage`.
¿Qué paso del bucle es "decide que necesita el consumo real"?

- a) Percepción
- b) Razonamiento
- c) Acción
- d) Entorno

**4.** En el mismo ejemplo, el sistema de facturación devuelve el consumo del ciclo actual.
¿Qué parte del bucle representa esa respuesta?

- a) Percepción
- b) Razonamiento
- c) Acción
- d) Entorno

---

### Parte C · Workflow vs agente (preguntas 5-6)

**5.** Un proceso de reclamos siempre debe: (1) pedir el número de línea, (2) verificar
identidad, (3) registrar el reclamo. El orden nunca cambia. ¿Qué construyes?

- a) Un agente, porque hay una tarea que cumplir
- b) Un workflow: los pasos son siempre los mismos, y necesitas garantizar que el paso 3
  ocurra siempre — un agente podría "decidir" saltárselo
- c) Un agente con `temperature=0` para que sea determinístico
- d) Ninguno de los dos: esto no se puede automatizar

**6.** Un cliente puede preguntar por su saldo, reportar fraude, pedir un límite más alto o
simplemente saludar, en cualquier orden y sin avisar qué va a pedir. ¿Qué construyes?

- a) Un agente: el orden depende de lo que responda el usuario y no se puede escribir de
  antemano con un `if/else`
- b) Un workflow con muchos `if`
- c) Un menú de opciones numeradas
- d) Un formulario web

---

### Parte D · El antipatrón (pregunta 7)

**7.** Le preguntas al modelo dos veces seguidas cuánto cuesta el plan de 20 GB de AndesMóvil, y
responde con total seguridad dos cifras distintas, ninguna real. ¿Por qué pasó esto?

- a) Hubo un error de red la segunda vez
- b) El modelo necesita un `temperature` más alto para ser preciso
- c) El modelo nunca tuvo acceso al tarifario real: respondió con la cifra estadísticamente más
  probable según su entrenamiento, no con un dato verificado. Por eso el curso obliga a
  recuperar antes de afirmar tarifas (regla A6, desde la Sesión 5)
- d) El modelo está mal configurado y hay que reiniciarlo

---

### Parte E · Modelos abiertos (pregunta 8)

**8.** ¿Qué significa que `Qwen/Qwen3-32B` sea un modelo de "pesos abiertos"?

- a) Que es gratis usarlo sin límite
- b) Que sus parámetros son públicos y auditables, a diferencia de un modelo cerrado del que
  solo consumes una API
- c) Que corre más rápido que un modelo cerrado
- d) Que fue entrenado solo con datos de código abierto

---

### Parte F · `comun/provider.py` (pregunta 9)

**9.** ¿Por qué ningún archivo del curso escribe `ChatOpenAI(...)` directamente, sino que llama a
`get_chat_model()`?

- a) Por una convención de estilo sin efecto real
- b) Porque `ChatOpenAI` no funciona con Hugging Face
- c) Porque esa indirección (decisión D13) es lo que permite, en el bonus de Foundry, cambiar
  de proveedor con una variable de entorno en vez de reescribir cada archivo del agente
- d) Porque `get_chat_model()` es más rápido

---

### Parte G · Cuándo NO conviene un agente (pregunta 10)

**10.** ¿Cuál de estas es una buena razón para **no** usar un agente?

- a) El agente es más lento y más caro que un workflow, y el problema que tienes se puede
  resolver con una secuencia de pasos fija — si puedes dibujar el diagrama de flujo completo
  antes de escribir código, no necesitas un agente
- b) Los agentes son un tema muy nuevo y da miedo usarlos
- c) Un agente nunca puede llamar a una API externa
- d) Los agentes solo sirven para chatbots de atención al cliente

---

## Autocorrección

<details>
<summary><b>Ver respuestas y explicaciones</b></summary>

| # | Respuesta | Por qué |
|---|-----------|---------|
| 1 | **c** | Una respuesta aislada no demuestra un bucle de acciones; memoria persistente no es requisito definitorio de todo agente |
| 2 | **c** | El tamaño del vocabulario no es una de las cuatro piezas (herramientas, memoria, objetivo, control) |
| 3 | **b** | Decidir el siguiente paso con el contexto disponible es razonamiento, no percepción ni acción |
| 4 | **d** | El sistema de facturación es el entorno: el sistema real que responde a la acción del agente |
| 5 | **b** | Pasos fijos que deben garantizarse siempre son la definición de workflow; un agente podría no ejecutar el paso 3 |
| 6 | **a** | Orden impredecible y dependiente del usuario es exactamente cuándo se justifica un agente |
| 7 | **c** | Es una alucinación: el modelo nunca consultó una fuente real. Es el antipatrón central de la sesión |
| 8 | **b** | Pesos abiertos = parámetros públicos y auditables. No implica gratuidad ni velocidad |
| 9 | **c** | La indirección de `comun/provider.py` (D13) es lo que hace posible cambiar de proveedor sin tocar el código del agente |
| 10 | **a** | Si el flujo se puede dibujar de antemano, un workflow es más barato, más rápido y más predecible |

</details>

---

## Siguiente paso

Con el Test 1 resuelto y tu track propuesto, continúa con el laboratorio: [`lab/`](lab/).
