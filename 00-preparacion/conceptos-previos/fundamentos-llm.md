# Fundamentos de modelos de lenguaje

> Sesión 0 · lectura principal · 60 minutos
> Escrito para quien programa hace años pero nunca trabajó con un LLM.

---

## 1. Lo primero: esto no es una API normal

Un servicio REST tiene contrato, es determinístico y falla de forma predecible. Un modelo de
lenguaje no cumple ninguna de las tres.

| | API tradicional | LLM |
|---|-----------------|-----|
| Misma entrada, misma salida | Sí | **No garantizado** |
| Contrato de salida | Fijo | Probabilístico, hay que forzarlo |
| Errores | Códigos de estado | **Respuestas seguras pero falsas** |
| Costo | Por llamada | Por token, entrada y salida |
| Latencia | Milisegundos | Segundos |

El error más caro que comete un ingeniero senior al empezar es asumir que puede probar un agente
con `assert respuesta == "esperado"`. No puede. Por eso este curso dedica una sesión entera a
evaluación con métricas.

---

## 2. Qué hace realmente un modelo de lenguaje

Un LLM predice el siguiente fragmento de texto dado el texto previo. Nada más.

```
   "El SOAT cubre gastos médicos hasta"  ──►  modelo  ──►  " 5 UIT"  (78 % de probabilidad)
                                                            " cinco" (11 %)
                                                            " el"    ( 4 %)
                                                            ...
```

Repite esa operación token a token hasta terminar. No consulta una base de datos, no razona con
reglas, no verifica nada. Toda la aparente inteligencia sale de haber visto muchísimo texto.

**Consecuencia inmediata:** el modelo no distingue entre lo que sabe y lo que suena plausible.
Genera ambas cosas con el mismo mecanismo, y con la misma confianza aparente.

---

## 3. Token: la unidad que gobierna todo

Un token es un fragmento de texto, no una palabra.

```
   "portabilidad numérica"  ──►  ["port", "abil", "idad", " num", "érica"]   = 5 tokens
   "phone number"           ──►  ["phone", " number"]                        = 2 tokens
```

Regla práctica en español: **1 token ≈ 0.75 palabras**. El español consume entre 20 % y 40 %
más tokens que el inglés para decir lo mismo, porque los tokenizadores se entrenaron
mayoritariamente con texto en inglés.

### Por qué importa

Los tokens determinan tres cosas a la vez:

1. **El costo.** Se paga por token de entrada y por token de salida.
2. **El límite.** Todo lo que envías debe caber en la ventana de contexto.
3. **La latencia.** El modelo genera un token por vez: respuestas largas tardan más.

> **Ejercicio mental:** un agente con historial de 10 turnos, 4 esquemas de herramientas y
> 4 fragmentos recuperados envía unos 6 000 tokens **en cada llamada**, aunque el usuario solo
> haya escrito "¿y el mes pasado?". El historial se reenvía completo cada vez.

Ejecuta `code/01_tokens.py` para verlo.

---

## 4. Ventana de contexto: memoria RAM, no disco

La ventana de contexto es cuánto puede "ver" el modelo en una sola llamada.

```
   ┌──────────────── ventana de contexto (32 768 tokens) ────────────────┐
   │ system prompt │ historial │ herramientas │ documentos │  respuesta  │
   │   ~1 000      │  ~1 500   │   ~1 200     │   ~2 000   │   variable  │
   └─────────────────────────────────────────────────────────────────────┘
```

Lo que no entra en esa ventana **no existe** para el modelo. Cuando la conversación crece, hay
que decidir qué se recorta: los turnos más antiguos, los documentos menos relevantes, o
resumir el historial.

**El modelo es stateless.** No recuerda nada entre llamadas. Lo que llamamos "memoria" de un
agente es simplemente que tu código le vuelve a enviar la lista completa de mensajes cada vez.
Esa es toda la magia.

---

## 5. Temperatura: por qué la misma pregunta da respuestas distintas

En cada paso el modelo tiene una distribución de probabilidad sobre el siguiente token. La
temperatura decide qué tan fielmente sigue esa distribución.

| Temperatura | Qué hace | Cuándo usarla en este curso |
|-------------|----------|------------------------------|
| `0.0` | Elige casi siempre el más probable | **Agentes, tools, clasificación, extracción** |
| `0.7` | Introduce variedad controlada | Conversación con el usuario final |
| `1.5` | Muy aleatorio | Redacción creativa |

> Los laboratorios de este curso usan **siempre `temperature=0`**. Un agente que elige
> herramientas debe ser lo más reproducible posible.

Ojo: `temperature=0` reduce muchísimo la variabilidad, pero **no la elimina del todo**. Hay
fuentes de no determinismo en el hardware y el paralelismo del servidor. Diseña asumiéndolo.

Ejecuta `code/02_temperatura.py` para verlo.

---

## 6. Alucinación: el fallo que no parece un fallo

Una alucinación es una respuesta fluida, segura y falsa.

```
   Usuario:  "¿Cuánto cubre el SOAT por gastos de sepelio?"
   Modelo:   "El SOAT cubre hasta 2 UIT por gastos de sepelio."   ← suena perfecto
                                    ▲
                                    └── es 1 UIT. El modelo no lo sabe, lo generó.
```

No hay señal de error, no hay excepción, no hay código 500. La respuesta llega con el mismo tono
de seguridad que una correcta.

### Las tres defensas que enseña el curso

| Defensa | Sesión | Qué hace |
|---------|--------|----------|
| **Tools** | 3 y 4 | El dato viene de tu sistema, no de la memoria del modelo |
| **RAG** | 5 | La respuesta se apoya en un documento, y se cita |
| **Guardrails** | 6 | El código impide afirmaciones y acciones fuera de política |

Ninguna elimina el problema por sí sola. Las tres juntas lo vuelven manejable.

---

## 7. Embeddings: buscar por significado

Un embedding convierte un texto en un vector de varios cientos de números que representan su
significado. Textos parecidos quedan cerca en ese espacio.

```
   "¿cuántos gigas me quedan?"     ──►  [0.21, -0.08, 0.44, ...]  ┐
                                                                   ├─ similitud 0.87
   "consulta de datos disponibles" ──►  [0.19, -0.11, 0.41, ...]  ┘

   "¿cuántos gigas me quedan?"     ──►  [0.21, -0.08, 0.44, ...]  ┐
                                                                   ├─ similitud 0.12
   "quiero cancelar mi contrato"   ──►  [-0.55, 0.72, -0.03, ...] ┘
```

Las dos primeras frases no comparten **ni una palabra**, y aun así están cerca. Eso es lo que la
búsqueda por palabras clave nunca podrá hacer, y es la base del RAG de la sesión 5.

La cercanía se mide con **similitud coseno**, un número de -1 a 1:

| Rango | Interpretación |
|-------|----------------|
| > 0.8 | Muy relacionados |
| 0.5 – 0.8 | Relacionados |
| < 0.5 | Poco o nada relacionados |

Ejecuta `code/03_embeddings.py` para verlo.

---

## 8. Costo: dónde se va el dinero

Se paga por token, y se paga **dos veces**: entrada y salida. La entrada suele ser mucho mayor
que la salida, porque incluye instrucciones, historial, herramientas y documentos.

```
   Turno 1:  entrada  1 200 tokens   salida  150
   Turno 5:  entrada  4 800 tokens   salida  180   ← el historial creció
   Turno 10: entrada  9 100 tokens   salida  160   ← y sigue creciendo
```

**El historial es lo que encarece una conversación, no la última pregunta.** Las estrategias de
control de costo que verás en el curso son: recortar el historial, resumirlo, recuperar menos
fragmentos, y usar un modelo pequeño para las tareas simples.

Ejecuta `code/04_costo.py` para verlo.

---

## 9. Modelos abiertos: qué usamos y por qué

Este curso corre **100 % sobre modelos de pesos abiertos**, servidos en línea.

| | Modelo abierto | Modelo propietario |
|---|----------------|--------------------|
| Pesos descargables | Sí | No |
| Se puede autohospedar | Sí | No |
| Soberanía del dato | Controlas dónde corre | Depende del proveedor |
| Costo | Pagas cómputo | Pagas por token |
| Capacidad tope | Alta | Normalmente mayor |

El modelo del curso es **`Qwen3-32B`**: licencia Apache 2.0, soporte nativo de function calling,
más de 100 idiomas y 32 768 tokens de contexto. Se eligió midiendo: de cuatro candidatos
probados contra el endpoint real, fue el único que superó las pruebas de uso de herramientas.

> **La fiabilidad se compone.** Un agente encadena varias llamadas al modelo por consulta, y
> los aciertos se multiplican: con 93 % de precisión por llamada, una tarea de tres pasos sale
> bien el 80 % de las veces, y una de cinco pasos solo el 70 %. Por eso el curso limita a 4 las
> herramientas de un agente y exige descripciones muy precisas. No es una limitación que
> sufrimos: es la restricción real de producción.

---

## 10. Fine-tuning vs RAG: la confusión más común

Ambos sirven para "que el modelo sepa de mi negocio". Resuelven cosas distintas.

| | Fine-tuning | RAG |
|---|-------------|-----|
| Qué mejora | **Estilo**: tono, jerga, formato | **Conocimiento**: datos, políticas, tarifas |
| Actualizar un dato | Reentrenar el modelo | Reindexar un documento |
| Citar la fuente | Imposible | Obligatorio |
| Auditar la respuesta | Caja negra | Traza + documento |
| Control de acceso | No existe | Por metadatos |
| Costo de un cambio | Alto | Casi cero |

**La regla del curso:** el estilo va al modelo, el conocimiento va al RAG.

### Cómo se aplica aquí

Este curso **no afina ningún modelo**. Usa `Qwen3-32B` tal como viene, y la especialización de tu
agente por industria sale de dos piezas que construirás en clase:

```
   Agente de AndesMóvil = Qwen3-32B  +  system prompt  +  colección Qdrant
                          (genérico)     (sesión 2)        (sesión 5)
                            estilo        tono, jerga,      tarifas,
                             ─            límites           coberturas
```

Dos razones, y ninguna es el presupuesto:

| Razón | Detalle |
|-------|---------|
| **El laboratorio de RAG funciona** | Un modelo afinado en telecomunicaciones aprende el patrón *"pregunta del sector → respuesta directa"* y deja de llamar al recuperador. El agente no busca porque cree que ya sabe |
| **El bonus de Foundry es cierto** | El prompt y la colección de Qdrant portan tal cual. Si la personalización estuviera en los pesos, apuntar a Foundry cambiaría el comportamiento del agente y la promesa *"solo cambias una línea del `.env`"* sería falsa |

Y hay un beneficio práctico: cambiar el tono de tu agente es editar un texto, no reentrenar nada.
Lo vas a hacer varias veces durante el curso.

---

## Antes de continuar

Comprueba que puedes responder sin mirar:

1. ¿Por qué el español cuesta más tokens que el inglés?
2. Si el modelo es stateless, ¿qué es exactamente la "memoria" de un agente?
3. ¿Por qué `temperature=0` no garantiza reproducibilidad total?
4. ¿Por qué una alucinación es más peligrosa que una excepción?
5. ¿Cómo pueden dos frases sin palabras en común tener similitud 0.87?
6. En una conversación de 10 turnos, ¿qué componente domina el costo?
7. ¿Cuándo usarías fine-tuning y cuándo RAG?

Si alguna te cuesta, vuelve a la sección correspondiente antes de la autoevaluación.

**Siguiente paso:** [`python-y-entorno.md`](python-y-entorno.md)
