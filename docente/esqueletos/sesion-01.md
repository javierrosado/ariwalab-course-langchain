# Esqueleto · Sesión 1 — Fundamentos de los agentes inteligentes

Guía para el docente: objetivos, secuencia de aula, prácticas y evaluación.

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta | `modulo-1-fundamentos/sesion-01-fundamentos-agentes/` |
| Semana · día | Semana 1 · martes |
| Horas | **3.5 h teoría · 2.5 h práctica = 6 h** |
| Reparto | 1 h pre-work (teoría) + 3 h en vivo (2.5 teoría / 0.5 práctica) + 2 h lab (práctica) |
| Laboratorio | **L1 · Entorno y primer script** |
| Hitos | **Test 1** · **elección de track** |

---

## 2. Objetivos de aprendizaje

Al terminar, el alumno puede:

1. Explicar por qué **un LLM solo no es un agente**, nombrando las cuatro piezas que le faltan.
2. Decidir, ante un problema dado, si necesita un **workflow** o un **agente** — y justificarlo.
3. Situar cada objeto de LangChain 1.x (`model`, `message`, `tool`, `agent`, `middleware`) en el
   mapa de las 11 sesiones.
4. Ejecutar un script que llama a un modelo de pesos abiertos **en línea**, sin instalar ningún
   motor de inferencia.
5. Explicar qué hace `comun/provider.py` y por qué el curso no instancia el modelo en cada archivo.

Los objetivos 1 y 2 se verifican con el **Test 1**; el 4 y el 5 con el **L1**.

---

## 3. Con qué llega el alumno

La Sesión 0 ya cubrió esto. **No se repite en clase**, se da por sabido:

| Ya sabe | Dónde lo aprendió |
|---|---|
| Token, ventana de contexto, temperatura, alucinación, embedding, costo | `00-preparacion/conceptos-previos/fundamentos-llm.md` |
| `venv`, `.env`, higiene de secretos, Pydantic básico | `00-preparacion/conceptos-previos/python-y-entorno.md` |
| Las 3 cuentas creadas y el `.env` completo | `00-preparacion/conceptos-previos/alta-de-cuentas.md` |
| Las 4 demos ejecutadas | `00-preparacion/code/` |

**Pre-work de 1 h** (`conceptos-previos.md` de esta sesión, no de la S0):

| # | Concepto | Por qué antes de la clase |
|---|---|---|
| 1 | *Chat completion* vs **agente** | Es la distinción que estructura toda la sesión |
| 2 | El bucle **percepción → razonamiento → acción** | Se usa como esquema desde el minuto 10 |
| 3 | Determinismo: por qué un LLM no es una API REST | Es el antipatrón que hay que romper |
| 4 | Qué es un modelo de **pesos abiertos** | Justifica el stack del curso |

---

## 4. El antipatrón que hay que romper

> **El ingeniero de software con 10 años de experiencia llega asumiendo que el LLM es una API
> determinística.** Si esa expectativa no se rompe el primer día, arrastra el error hasta la
> sesión 10, cuando intente evaluar el agente con `assert respuesta == "esperado"`.

Se rompe con una **demo en vivo, no con una diapositiva**: preguntarle al modelo una tarifa de
AndesMóvil dos veces y mostrar que responde con total seguridad dos cifras distintas, ninguna
verdadera. El resto de la sesión explica por qué, y las 10 siguientes construyen las defensas.

---

## 5. Guion de la sesión en vivo · 180 min

| # | Bloque | Min | Tipo | Contenido |
|---|---|---|---|---|
| 0 | Apertura y mapa del curso | 10 | T | Qué construirán en 6 semanas. Mostrar la app final funcionando |
| 1 | **Un LLM solo no es un agente** | 30 | T + demo | La demo de la tarifa inventada. Las 4 piezas que faltan: herramientas, memoria, objetivo, control |
| 2 | Agente = percepción → razonamiento → acción → entorno | 30 | T | El marco. Diagrama ASCII. Ejemplos en las 4 industrias |
| 3 | **Workflow vs agente** | 20 | T | Cuadro de decisión. *Cuándo NO necesitas un agente* — la mitad de los casos reales |
| — | **Pausa** | 10 | — | |
| 4 | Anatomía de LangChain 1.x | 30 | T | `model` · `message` · `tool` · `agent` · `middleware`, y en qué sesión se ve cada uno |
| 5 | Modelos abiertos vs cerrados | 20 | T | Pesos abiertos, inferencia remota y verificación con `check_stack` |
| 6 | `comun/provider.py` en vivo | 15 | P | Correr `describe_provider()` y el primer llamado. La indirección y el bonus de Foundry |
| 7 | **Test 1** + **elección de track** | 15 | P | 10 preguntas · cada equipo declara su track |

**Teoría 140 min · práctica 30 min · pausa 10 = 180** → con el pre-work (60 min de teoría) y el
laboratorio (120 min de práctica): **3.33 h teoría / 2.50 h práctica**.

> La malla declara 3.5 h / 2.5 h. La diferencia son los 10 min de pausa, que no se cuentan en
> ninguna de las dos mitades. Es la convención que siguen las 11 sesiones; está en
> `docente/esqueletos/README.md`.

### Contenido del bloque 1 — las 4 piezas que le faltan al LLM

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

Cada flecha se etiqueta con la sesión que la construye. Ese diagrama es el mapa del curso y se
repite en la apertura de las sesiones 3, 4, 5 y 6.

### Contenido del bloque 3 — el cuadro de decisión

| Si… | Necesitas | Por qué |
|---|---|---|
| Los pasos son siempre los mismos | **Workflow** | Más barato, más rápido, depurable |
| El orden depende de lo que responda el usuario | **Agente** | El modelo decide la ruta |
| Hay que garantizar que un paso ocurra siempre | **Workflow** | Un agente *puede* saltárselo |
| El número de pasos no se conoce de antemano | **Agente** | El bucle termina cuando el objetivo se cumple |

> Mensaje que el alumno debe llevarse: **un agente es más caro, más lento y menos predecible que
> un workflow.** Solo se justifica cuando la ruta no se puede escribir de antemano.

---

## 6. Las 3 demos · `code/`

| Archivo | Qué demuestra | Qué debe notar el alumno |
|---|---|---|
| `01_primer_llamado.py` | `describe_provider()` + un llamado al modelo vía `comun/provider.py` | Que ningún archivo del curso instancia el modelo directamente |
| `02_tipos_de_mensaje.py` | `system` / `human` / `ai`: el mismo `human` con y sin `system` | Que el `system` cambia el tono y los límites sin cambiar la pregunta |
| `03_un_modelo_cuatro_industrias.py` | La misma pregunta contra los 4 `get_system_prompt(track)` | Que **un solo modelo** suena a telco, banco, retailer o aseguradora mediante el system prompt |

Las tres corren con solo `HF_TOKEN`. Ninguna necesita Qdrant, Langfuse ni el simulador.

---

## 7. Laboratorio L1 · Entorno y primer script

**Alcance:** entorno verde y primer script del track. Sin tools, sin Pydantic, sin agente.

| Parte | Min | Qué hace el alumno |
|---|---|---|
| 1 | 40 | `check_stack --solo-modelo` en verde. El docente desbloquea a quien falle: es la única ventana del curso para arreglar entornos |
| 2 | 50 | Escribir `primer_contacto.py` de su track: 3 preguntas reales del dominio al modelo |
| 3 | 20 | Registrar el equipo y el track en la plantilla del docente |
| 4 | 10 | Verificación cruzada: que el compañero de equipo corra el script del otro |

**Por qué 40 minutos de verificación y no 10.** El primer laboratorio de cualquier curso se
consume arreglando entornos. Reconocerlo en el diseño evita que la S2 empiece con la mitad del
aula bloqueada — y la S3 es el **Assignment A1**, el día 3.

### Entregables

| Entregable | Ruta |
|---|---|
| `.env` completo y `check_stack --solo-modelo` en verde | raíz del curso |
| `primer_contacto.py` | `lab/<track>/primer_contacto.py` |
| Track declarado por el equipo | plantilla del docente |

### Criterio de aceptación

- El script corre **sin instalar ningún motor de inferencia ni base de datos** en la laptop.
- Usa `comun.provider.get_chat_model()`; **no** instancia `ChatOpenAI` directamente.
- Las 3 preguntas son del dominio del track elegido, no genéricas.

### Reto opcional · no evaluado

Para quien termine antes: hacerle al modelo una **cuarta** pregunta cuya respuesta solo existe en
los datos de la empresa (por ejemplo, el consumo de la línea `987654321`), y anotar en 5 líneas
qué se inventó. Esa nota se retoma en la S5 como el "antes" del RAG.

---

## 8. Elección de track

**Regla: el equipo propone, el docente balancea.**

- Cada equipo de 2 declara su track al cerrar la sesión en vivo.
- El docente ajusta para que los **4 tracks estén representados** en la sustentación final y para
  que **Banca** —el más exigente en guardrails y structured output— no caiga en el equipo más débil.
- El track es **irrevocable**: todos los laboratorios del L2 al L11 se construyen sobre él.

---

## 9. Test 1 · 10 preguntas

| # | Evalúa |
|---|---|
| 1-2 | Las 4 piezas que le faltan a un LLM para ser agente |
| 3-4 | Percepción → razonamiento → acción → entorno, aplicado a un caso |
| 5-6 | Workflow vs agente: elegir y justificar |
| 7 | Por qué un LLM no es una API determinística |
| 8 | Qué es un modelo de pesos abiertos |
| 9 | Qué hace `provider.py` y por qué existe la indirección |
| 10 | Cuándo **no** conviene un agente |

Formato igual al de `00-preparacion/autoevaluacion.md`: opción múltiple con respuestas
comentadas al final, no solo la letra correcta.

---

## 10. Qué **no** entra en esta sesión

Mantener la clase dentro de este alcance:

| No entra | Va en |
|---|---|
| `@tool`, function calling | S3 |
| Pydantic y structured output | S2 |
| `create_agent()` | S3 |
| Plantillas de prompt, few-shot | S2 |
| El simulador de industria | S3 |
| Qdrant y Langfuse (más allá de tener la cuenta) | S5 y S9 |
| MCP | S4 |
| Las reglas A1–A6 | Aplicación desde S2; aquí solo se nombran |

> La palabra "agente" se explica en la S1, pero **el alumno no construye uno hasta la S3**. Decirlo
> explícitamente en el README evita la frustración de quien espera un agente el primer día.

---

## 12. Errores esperables y cómo atenderlos

| Síntoma | Causa | Respuesta del docente |
|---|---|---|
| `401` contra Hugging Face | Token sin permiso de inferencia | Regenerar el token marcando ese permiso |
| `ModuleNotFoundError: comun` | Ejecutando desde otra carpeta | Siempre desde la raíz del curso |
| `ModuleNotFoundError: langchain` | `venv` sin activar | Reactivar; el prompt debe mostrar `(.venv)` |
| Acentos rotos en Windows | Codificación de la consola | `chcp 65001` |
| El modelo responde en inglés | Falta el `system` en español | Es la demostración del bloque 2: usarlo como ejemplo |
| El modelo tarda 20 s | Cola del *inference provider* | Normal. Se mide y se optimiza en la S10 |
