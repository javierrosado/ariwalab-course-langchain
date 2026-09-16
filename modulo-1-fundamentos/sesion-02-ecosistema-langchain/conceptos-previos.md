# Conceptos previos · Sesión 2

> Pre-work asíncrono de 1 h. Termina con el **pase de entrada de Pydantic** — sin él no se hace
> el L2 en la sesión en vivo.

---

## 1. Roles de mensaje: `system`, `human`, `ai`, `tool`

Ya los usaste en la Sesión 1 (`SystemMessage`, `HumanMessage`). Es el modelo mental de toda la
librería: una conversación es una **lista** de mensajes con un rol cada uno, no un texto plano.
`tool` se suma en la Sesión 3, cuando el modelo empiece a llamar funciones.

## 2. El historial es una lista de mensajes que tú reenvías

El modelo no guarda nada entre llamadas. "Recordar" es tu código reenviando la lista completa.
Sin entender esto, la memoria de la Sesión 5 (`thread_id`) parece magia; con esto claro, es solo
una lista que crece.

## 3. Pydantic v2: `BaseModel`, `Field`, `Enum`, validación

Prerrequisito **duro** de hoy y de la Sesión 3. Repasa `00-preparacion/conceptos-previos/python-y-entorno.md`
sección 5 si te queda alguna duda antes de hacer el ejercicio de abajo.

## 4. JSON Schema, lectura básica

Cuando pides salida estructurada, el modelo no recibe tu clase Python: recibe el **JSON Schema**
que Pydantic genera (`TuModelo.model_json_schema()`). Es lo que de verdad "ve" el modelo — por
eso el `description` de cada `Field` importa tanto: es texto que el modelo lee para decidir qué
poner en cada campo.

## 5. f-strings y placeholders

Base de cualquier plantilla de prompt: un texto con huecos (`f"Cliente dice: {consulta}"`) que
se rellenan antes de mandarlo al modelo. `PromptTemplate` de LangChain es esto, con utilidades
alrededor.

---

## Pase de entrada · Pydantic

> **Regla decidida: sin este ejercicio entregado, no haces el L2 hoy.** Quien no lo entregue
> antes de la sesión dedica sus 2 h de laboratorio a resolverlo (con el checkpoint de la S1 como
> apoyo) y retoma el L2 en la S3 con el checkpoint de la solución.

Define un modelo Pydantic llamado `Reclamo` con:

- `tipo`: un `Enum` con `FACTURACION`, `AVERIA`, `PORTABILIDAD`
- `descripcion`: texto de entre 10 y 200 caracteres
- `numero_linea`: exactamente 9 dígitos
- `requiere_tecnico`: booleano con valor por defecto `False`

Imprime `Reclamo.model_json_schema()` y comprueba que las 4 restricciones aparecen ahí — eso es
literalmente lo que va a leer el modelo. Entrega el `.py` y la salida del schema **antes** de la
sesión en vivo.

**Verificación automática** (la corre el docente, pero puedes correrla tú mismo antes de entregar):

```bash
python docente/verificar_ejercicio_pydantic.py --archivo <tu_archivo>.py
```

**Por qué es tan exigente y aun así correcto.** La Sesión 3 es el Assignment A1 y ocurre 5 días
después. Un alumno que no sabe definir un `BaseModel` no puede escribir el `args_schema` de una
tool: no es que le cueste el A1, es que no puede empezarlo. Descubrirlo hoy deja margen;
descubrirlo el martes de la semana 2 no.

---

## Test 2 · 10 preguntas

> **Se responde en el bloque 7 de la sesión en vivo** (15 min), después de ver toda la teoría de
> hoy. Formato igual al de sesiones anteriores: opción múltiple con respuestas comentadas.

### Parte A · Mensajes y memoria (preguntas 1-3)

**1.** ¿Qué rol de mensaje representa lo que escribe el usuario?

- a) `system`
- b) **`human`**
- c) `ai`
- d) `tool`

**2.** ¿Cuál de estos NO es un rol de mensaje que ya usaste hasta la Sesión 2?

- a) `system`
- b) `human`
- c) `ai`
- d) **`tool`** (se suma en la Sesión 3, cuando el modelo empieza a llamar funciones)

**3.** Tu agente lleva 9 turnos de conversación. ¿Por qué el turno 10 cuesta más tokens que el
turno 1, si el usuario escribió lo mismo de largo en ambos?

- a) El modelo "aprendió" durante la conversación y ahora piensa más
- b) **Tu código reenvía el historial completo en cada llamada; el turno 10 arrastra los 9 anteriores**
- c) Los mensajes más recientes cuestan más tokens por definición
- d) Es un error de configuración

### Parte B · Rol + Contexto + Tarea + Formato (preguntas 4-5)

**4.** A este prompt le falta una parte: *"Eres el asistente de AndesMóvil. Clasifica la consulta
del cliente."* ¿Cuál?

- a) Rol
- b) Contexto
- c) Tarea
- d) **Formato** (no dice cómo debe verse la salida)

**5.** ¿Qué parte de Rol+Contexto+Tarea+Formato es la que más se degrada al quitarla, cuando ya
existe un esquema Pydantic detrás?

- a) Rol
- b) Contexto
- c) Tarea
- d) **Formato** — sin especificarlo, el modelo no sabe que debe ceñirse a la estructura pedida

### Parte C · Few-shot (pregunta 6)

**6.** ¿En cuál de estos casos el few-shot **no** conviene?

- a) Un Enum con categorías parecidas entre sí
- b) Un campo con un formato específico que hay que replicar
- c) **Una categoría que ya es obvia por el vocabulario de la consulta** — el few-shot solo
  gastaría tokens sin mejorar el acierto
- d) Un campo ambiguo que el modelo confunde seguido

### Parte D · Structured output (preguntas 7-9)

**7.** ¿Qué recibe el modelo cuando le pides una salida con un esquema Pydantic?

- a) Tu clase Python tal cual
- b) **El JSON Schema que Pydantic genera a partir de la clase**
- c) Un archivo `.py` serializado
- d) Nada especial: el modelo adivina la estructura

**8.** ¿Por qué `with_structured_output()` de LangChain, usado solo, no basta?

- a) Es una función experimental que no funciona
- b) No existe en la versión del curso
- c) **Funciona la mayoría de las veces, pero la minoría de fallos (enum inventado, campo vacío)
  no se valida ni se reintenta: el error revienta más adelante en el código**
- d) Solo funciona con modelos cerrados

**9.** `comun/structured.py` reintenta como máximo **una vez** tras un fallo. ¿Por qué no cinco?

- a) Por limitar el costo de infraestructura del curso
- b) **Si el segundo intento también falla, el problema es el esquema o el prompt, no la suerte:
  reintentar más veces esconde un defecto de diseño y multiplica el costo**
- c) Por una limitación técnica de LangChain
- d) Porque el modelo se satura después de dos intentos

### Parte E · Costo (pregunta 10)

**10.** En una conversación de 10 turnos con few-shot en el prompt, ¿qué componente domina el
costo total en tokens?

- a) La última pregunta del usuario
- b) La respuesta del modelo
- c) **El historial acumulado (incluido el few-shot, que se reenvía en cada llamada)**
- d) El nombre de las herramientas

---

## Autocorrección

<details>
<summary><b>Ver respuestas y explicaciones</b></summary>

| # | Respuesta | Por qué |
|---|-----------|---------|
| 1 | b | `human` es el mensaje del usuario |
| 2 | d | `tool` aparece recién en la Sesión 3 |
| 3 | b | El modelo es stateless: "recordar" es tu código reenviando todo el historial |
| 4 | d | Falta decir cómo debe verse la salida |
| 5 | d | Sin el Formato, un esquema Pydantic detrás no tiene ancla en el prompt |
| 6 | c | El few-shot rinde en lo ambiguo, no en lo ya obvio |
| 7 | b | El modelo ve el JSON Schema, no la clase Python |
| 8 | c | Falla en la minoría de casos, y esa minoría es la que rompe un agente real |
| 9 | b | Un segundo fallo indica un problema de diseño, no de suerte |
| 10 | c | El historial (con el few-shot dentro) se paga en cada llamada, no una sola vez |

</details>

---

## Checklist final antes de la sesión

- [ ] `Reclamo` entregado y verificado con `docente/verificar_ejercicio_pydantic.py`.
- [ ] Puedo explicar por qué el modelo es *stateless* con mis propias palabras.
- [ ] Sé nombrar las 4 partes de Rol+Contexto+Tarea+Formato.
- [ ] Entiendo qué diferencia a `with_structured_output()` de `extraer()`.
