# Glosario del curso

> 47 términos en español, pensados para **ingenieros de software que parten de cero en LLMs**.
> Cada entrada trae la definición y, cuando ayuda, una equivalencia con algo que ya conoces.
>
> Este glosario se consulta durante todo el curso. Cada sesión indica qué términos debes
> dominar antes de entrar.

---

## Bloque 1 · Modelos de lenguaje

### LLM (Large Language Model)
Modelo entrenado para predecir el siguiente fragmento de texto a partir del texto previo. No
consulta una base de datos ni razona con reglas: genera la continuación más probable según lo
que aprendió.

> **Para un ingeniero:** no es una API determinística. Es más parecido a una función con
> ruido controlado que a un `SELECT`. La misma entrada puede dar salidas distintas.

### Token
Unidad mínima que el modelo procesa. No es una palabra ni un carácter: es un fragmento. En
español, aproximadamente **1 token ≈ 0.75 palabras**.

> `"portabilidad"` puede ser 3 tokens: `port` + `abil` + `idad`.
> Importa porque **todo se cobra y se limita por tokens**: entrada, salida y contexto.

### Tokenización
Proceso de partir el texto en tokens. Cada familia de modelos tiene su propio tokenizador, así
que el mismo texto no cuesta lo mismo en dos modelos distintos.

### Ventana de contexto
Cantidad máxima de tokens que el modelo puede tener "a la vista" en una llamada: system prompt +
historial + documentos recuperados + herramientas + respuesta.

> **Para un ingeniero:** es memoria RAM, no disco. Lo que no entra, no existe para el modelo.
> `Qwen3-32B` maneja 32 768 tokens nativos; el agente de este curso usa unos 6 000 por llamada.

### Prompt
El texto que se envía al modelo. En una aplicación real casi nunca lo escribe el usuario
completo: se **construye** juntando instrucciones, contexto recuperado y la consulta.

### System prompt
Instrucción de rol y comportamiento que va al inicio y condiciona toda la conversación. Es donde
viven la personalidad, las reglas de negocio y los límites de actuación del agente.

### Inferencia
La ejecución del modelo para producir una respuesta. Es la operación que se paga y la que tarda.

### Temperatura
Parámetro entre 0 y 2 que controla cuánta aleatoriedad se introduce al elegir el siguiente token.

| Valor | Comportamiento | Cuándo usarlo |
|-------|----------------|---------------|
| `0.0` | Casi determinista, elige siempre lo más probable | Tools, clasificación, extracción de datos |
| `0.7` | Equilibrado | Conversación con usuario |
| `1.2+` | Creativo e impredecible | Redacción libre, lluvia de ideas |

> En este curso los laboratorios de agentes usan **siempre `temperature=0`**.

### Top-p (nucleus sampling)
Alternativa a la temperatura: en vez de suavizar las probabilidades, restringe la elección al
conjunto de tokens que acumulan una probabilidad `p`. Se ajusta uno u otro, rara vez ambos.

### Determinismo
Propiedad de dar siempre la misma salida ante la misma entrada. Los LLM **no la garantizan**,
ni siquiera con `temperature=0`, por detalles de hardware y paralelismo.

> **Consecuencia práctica:** la igualdad de toda una respuesta libre suele ser frágil; sí
> son útiles las aserciones exactas sobre contratos determinísticos.
> Por eso el curso dedica la sesión 10 a evaluación con métricas y no con aserciones exactas.

### Alucinación
Respuesta fluida, segura y falsa. El modelo no distingue entre "lo que sabe" y "lo que suena
plausible": ambas cosas se generan con el mismo mecanismo.

> Es el motivo por el que existe el RAG y por el que la sesión 5 obliga a citar la fuente.

### Modelo base vs modelo Instruct
El **base** solo completa texto. El **Instruct** fue post-entrenado para seguir instrucciones y
conversar. Para agentes siempre se usa un Instruct.

> `Qwen3-32B` es el modelo Instruct que usa este curso.

### Open-weights vs propietario
**Open-weights**: los pesos del modelo se pueden descargar, inspeccionar y desplegar donde
quieras. **Propietario**: solo accesible por API de un proveedor.

> No confundir open-weights con open-source estricto: muchos modelos abiertos publican los
> pesos pero no el corpus de entrenamiento.

### Fine-tuning
Continuar el entrenamiento de un modelo con datos propios para ajustar su comportamiento.

> **Regla del curso:** el fine-tuning sirve para el **estilo** (tono, jerga, formato). El
> **conocimiento** (tarifas, políticas, coberturas) va en RAG, porque cambia y debe citarse.
>
> **Este curso no afina ningún modelo.** Usa `Qwen3-32B` tal cual: el estilo de cada industria
> vive en el system prompt y el conocimiento en Qdrant. Ambos se editan en minutos y viajan
> intactos al bonus de Foundry.

### LoRA (Low-Rank Adaptation)
Técnica de fine-tuning que congela el modelo y entrena solo unas matrices pequeñas añadidas.
Es órdenes de magnitud más barata que reentrenar todo y preserva mejor las capacidades
originales, como el tool calling.

---

## Bloque 2 · LangChain

### LangChain
Framework de Python que abstrae el trabajo con LLMs: modelos, prompts, herramientas, memoria,
recuperación y agentes, con una interfaz común entre proveedores.

> **Para un ingeniero:** es a los LLM lo que un ORM a las bases de datos. Cambias el proveedor
> sin reescribir la aplicación.

### Chat model
Objeto de LangChain que representa un modelo conversacional. Recibe una lista de mensajes y
devuelve un mensaje.

### Mensaje y roles
La conversación es una **lista de mensajes**, cada uno con un rol:

| Rol | Quién habla | Para qué |
|-----|-------------|----------|
| `system` | La aplicación | Instrucciones y reglas del agente |
| `human` | El usuario | La consulta |
| `ai` | El modelo | La respuesta, o la llamada a una tool |
| `tool` | Tu código | El resultado de ejecutar una tool |

> **Clave:** el modelo es *stateless*. No recuerda nada. La "memoria" es simplemente que le
> vuelves a enviar la lista completa de mensajes en cada llamada.

### Prompt template
Plantilla con variables que se rellenan en tiempo de ejecución. Evita concatenar strings a mano
y permite versionar los prompts como código.

> Patrón que enseña el curso: **Rol + Contexto + Tarea + Formato**.

### Few-shot
Incluir en el prompt 2 a 5 ejemplos resueltos de la tarea. Es la forma más barata de mejorar
la precisión, y **rinde especialmente cuando la tarea es ambigua** para el modelo.

### Structured output
Forzar que el modelo devuelva un objeto tipado (un modelo Pydantic) en vez de texto libre.
Es lo que hace que un agente sea integrable con un sistema real.

### Chain
Composición de pasos: entrada → prompt → modelo → parser → salida. En LangChain moderno se
expresa con el operador `|`.

### Callback
Gancho que se ejecuta en cada paso de la cadena o del agente, sin que estos lo sepan. Es cómo
se instrumenta la observabilidad en la sesión 9.

> **Para un ingeniero:** es un interceptor o un middleware de logging.

### LangGraph
Librería hermana de LangChain para flujos con estado explícito, ciclos y ramificaciones. Se usa
cuando `create_agent()` se queda corto: aprobaciones humanas, reintentos condicionados,
múltiples agentes coordinados.

---

## Bloque 3 · Agentes

### Agente
Sistema en el que **el modelo decide qué hacer**: percibe la consulta, razona sobre ella, elige
y ejecuta acciones mediante herramientas, observa el resultado y repite hasta resolver.

```
   ┌─────────────────────────────────────────────┐
   │  ENTORNO  (APIs · bases de datos · usuario) │
   └───────▲─────────────────────────┬───────────┘
           │ observación             │ acción
   ┌───────┴─────────────────────────▼───────────┐
   │  AGENTE                                      │
   │  percepción → razonamiento → acción          │
   └──────────────────────────────────────────────┘
```

> **La diferencia clave con un workflow:** en un workflow tú decides el orden de los pasos;
> en un agente lo decide el modelo. Esa es toda la diferencia, y también todo el riesgo.

### Tool (herramienta) y function calling
Una función de tu código que el modelo puede pedir que se ejecute. El modelo **no ejecuta
nada**: genera una petición estructurada con el nombre de la función y sus argumentos, y **tu
código decide si la ejecuta**.

```
   1. El LLM GENERA:      consultar_saldo(numero_linea="987654321")
   2. TU CÓDIGO EJECUTA:  → "S/ 45.20"
   3. El LLM RESPONDE:    "Tu saldo es S/ 45.20"
```

> Esa separación es la razón por la que un agente puede ser seguro: entre el paso 1 y el 2
> caben todas las validaciones que quieras.

### Docstring de una tool
La documentación de la función. **No es documentación: es el prompt** que el modelo lee para
decidir si usa esa herramienta. Por eso en este curso toda docstring dice qué hace la tool,
cuándo usarla y **cuándo NO** usarla.

### ReAct (Reasoning + Acting)
Patrón de razonamiento en bucle: *Pensamiento → Acción → Observación*, repetido hasta llegar a
la respuesta. Es lo que `create_agent()` implementa por dentro.

### Iteración y tope de iteraciones
Cada vuelta del bucle ReAct. Se fija un máximo para que un agente confundido no gire
indefinidamente: es un problema frecuente en modelos pequeños.

### Middleware
Capa que intercepta el comportamiento del agente sin modificar sus herramientas: registrar,
validar, cambiar de modelo, manejar errores.

### Guardrail
Restricción que impide que el agente haga algo indebido: validar la entrada, enmascarar datos
personales, prohibir acciones, exigir confirmación, derivar a un humano.

> Un guardrail escrito solo en el system prompt es una sugerencia. Un guardrail en código aplica
> condiciones explícitas, cuya cobertura debe probarse; no garantiza defensa universal. El curso enseña a ponerlos en código.

### MCP (Model Context Protocol)
Estándar abierto para que un agente se conecte a herramientas y fuentes de datos externas sin
integración a medida.

> **Para un ingeniero:** es el USB-C de las herramientas de IA. Un conector, muchos dispositivos.

### Human-in-the-loop
Diseño en el que ciertas acciones requieren confirmación de una persona antes de ejecutarse.
Obligatorio para operaciones irreversibles.

### Router de modelos
Patrón en el que un modelo orquestador dirige el bucle del agente y delega tareas específicas a
modelos especializados, expuestos como herramientas.

---

## Bloque 4 · Recuperación y RAG

### Embedding
Representación numérica del significado de un texto: un vector de varios cientos de dimensiones.
Textos con significado parecido quedan cerca en ese espacio.

> `"¿cuántos gigas tengo?"` y `"consulta de datos disponibles"` están cerca aunque no compartan
> ni una palabra. Eso es lo que la búsqueda por palabras clave no puede hacer.

### Similitud coseno
Los umbrales de la tabla son ilustrativos, no universales: deben calibrarse con el modelo
de embeddings, la normalización y el corpus usados.

Medida de cercanía entre dos vectores, de -1 a 1. Es cómo se decide qué fragmento responde mejor
a una consulta.

| Valor | Interpretación |
|-------|----------------|
| > 0.8 | Muy relacionados |
| 0.5 – 0.8 | Relacionados |
| < 0.5 | Poco o nada relacionados |

### Vector store (base vectorial)
Base de datos especializada en almacenar embeddings y buscar los más parecidos a una consulta.
En este curso: **Qdrant Cloud**.

### Chunk y chunking
Los documentos se parten en fragmentos (*chunks*) antes de embeberse, porque un documento entero
no cabe en el contexto y diluye el significado.

> **El trade-off:** chunks pequeños dan precisión pero pierden contexto; chunks grandes
> conservan contexto pero traen ruido. No hay valor mágico: se ajusta y se mide.

### Solapamiento (overlap)
Repetir el final de un chunk al inicio del siguiente, para que una idea partida por la mitad no
se pierda en ninguno de los dos.

### Retriever
Componente que, dada una consulta, devuelve los chunks más relevantes del vector store.

### RAG (Retrieval-Augmented Generation)
Recuperar información relevante y dársela al modelo como contexto antes de que responda. El
modelo deja de "recordar" y pasa a "consultar".

### RAG agéntico
Variante en la que **el agente decide** si necesita buscar o puede responder directo, en vez de
buscar siempre.

> Es lo que enseña la sesión 5, y es una de las dos razones por las que el curso usa un modelo
> genérico: un modelo afinado en el sector cree que ya sabe la respuesta y deja de buscar, con lo
> que el laboratorio directamente no funciona.

### Groundedness (fundamentación)
Grado en que una respuesta se apoya realmente en los documentos recuperados y no en invención
del modelo. Es la métrica central para evaluar un sistema RAG.

### Conocimiento paramétrico vs recuperable

| | Paramétrico (en los pesos) | Recuperable (en el RAG) |
|---|---|---|
| Cómo se actualiza | Reentrenando | Reindexando un documento |
| Se puede citar | No | Sí |
| Se puede auditar | No | Sí |
| Control de acceso | No existe | Por metadatos |
| Costo de un cambio | Alto | Casi cero |

---

## Bloque 5 · Producción

### Traza (trace) y span
Una **traza** es el registro completo de una ejecución del agente. Un **span** es cada paso
dentro de ella: una llamada al modelo, una tool, una recuperación.

> **Para un ingeniero:** es exactamente el modelo de una traza distribuida. Un run de agente
> es un árbol de spans.

### Observabilidad
Capacidad de entender qué pasó por dentro sin agregar código nuevo. Con agentes es
imprescindible: sin trazas, un fallo es indistinguible de una alucinación.

### Latencia p50 / p95
Percentiles del tiempo de respuesta. El p50 es el caso típico; el **p95 es el que enoja al
usuario**. Optimizar el promedio y no el p95 es un error clásico.

### Golden dataset
Conjunto de casos de prueba con la respuesta esperada, usado para medir si un cambio mejora o
empeora el sistema.

### Evaluator
Función que puntúa una respuesta. Puede ser determinística (¿llamó a la tool correcta?) o
basada en modelo.

### LLM-as-judge
Usar un modelo para evaluar las respuestas de otro. Es potente y barato, pero tiene sesgos
conocidos: prefiere respuestas largas y tiende a favorecer su propio estilo.

### Hosted agent
Agente desplegado y ejecutado por una plataforma gestionada, que expone un endpoint estándar.
Es lo que se hace en el bonus con Microsoft Foundry.

### Protocolo Responses
Contrato estándar de entrada/salida que usan las plataformas de agentes para invocarlos de forma
uniforme.

---

## Los 5 términos que más cuestan al empezar

Si solo vas a memorizar cinco, que sean estos:

1. **Token** — porque explica el costo, los límites y por qué el modelo "se olvida".
2. **El modelo es stateless** — porque explica qué es realmente la memoria de un agente.
3. **El LLM genera la llamada, tu código la ejecuta** — porque es lo que hace seguro a un agente.
4. **La docstring es el prompt** — porque explica por qué una tool mal descrita nunca se elige.
5. **Paramétrico vs recuperable** — porque explica para qué sirve el RAG.
