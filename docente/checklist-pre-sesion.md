# Checklist pre-sesión — los 4 servicios SaaS, 24 h antes

> Deriva de `docente/cronograma.md` §"Puntos de control" y de `comun/check_stack.py`. No
> reinventa nada: empaqueta esa verificación en un checklist que se corre **24 h antes de cada
> sesión**, para que un fallo se descubra con margen y no a las 19:05 del día de clase.

---

## El comando único

```bash
python -m comun.check_stack
```

Corre las 9 comprobaciones contra los 4 servicios reales (modelo de HF, embeddings, Qdrant,
Langfuse, simulador de industria) y termina con un veredicto:

| Código de salida | Veredicto | Qué hacer |
|---|---|---|
| `0` | **STACK VERIFICADO** | Dictar sin cambios |
| `1` | **PARCIAL** — el modelo sirve, algún servicio falló | Revisar la comprobación fallida (tabla de abajo) antes de la sesión que dependa de ella |
| `2` | **BLOQUEANTE** — falló una comprobación crítica (tool calling o el bucle ReAct) | No dictar sobre este stack. Correr `python -m comun.check_stack --candidatos` para encontrar un modelo que sirva |

Si una sesión aún no usa un servicio (por ejemplo, Qdrant antes de la S5), una falla ahí **no
bloquea esa sesión concreta** — pero repórtala igual: es la advertencia temprana de un problema
que sí va a bloquear la sesión que sí lo necesita.

---

## Qué comprobación corresponde a qué servicio

| Comprobación de `check_stack` | Servicio | Desde qué sesión importa |
|---|---|---|
| 1. Variables de entorno | — | Siempre |
| 2. El modelo de chat responde | HF Inference | Desde la S1 |
| 3. Tool calling (**crítica**) | HF Inference | Desde la S3 |
| 4. Agente completo con `create_agent` (**crítica**) | HF Inference | Desde la S3 |
| 5. Structured output con Pydantic | HF Inference | Desde la S2 |
| 6. Embeddings | HF Inference | Desde la S5 |
| 7. Qdrant Cloud: indexar y recuperar | Qdrant Cloud | Desde la S5 |
| 8. Langfuse Cloud: enviar una traza | Langfuse Cloud | Desde la S9 |
| 9. Simulador de industria | Simulador (HF Spaces) | Desde la S3 |

---

## Bloqueantes con fecha, por sesión

Estos ya están decididos en los esqueletos (`docente/esqueletos/sesion-NN.md`) con su propio
plazo — no son parte del comando de arriba, pero son parte del mismo hábito de verificar con
margen:

| Sesión | Qué verificar | Para cuándo | Si falla |
|---|---|---|---|
| **S3** | Simulador respondiendo `/health`, API key por equipo repartida, `CHAOS_RATE=0.0` | Lunes semana 2 | `DATA_SOURCE=csv`: se pierde el escenario "servicio caído" del L3 |
| **S5** | Cluster de Qdrant *Healthy* por equipo, colecciones de respaldo `kb-<track>-respaldo` indexadas | Lunes semana 3 | Sin L5 — y el L6/L7 se construyen sobre el agente con RAG |
| **S7** | `CHAOS_RATE=0.1` activado y **anunciado** (nunca sorpresa: la sesión vale el 100 % del M2) | Antes de empezar la S7 | Volver a `0.0` al terminar |
| **S8** | Space de cada equipo creado y `git push` funcionando | Durante la S8 | Alternativa preparada: Render |
| **S9** | Proyecto de Langfuse operativo por equipo (2 integrantes, plan Hobby) | Lunes semana 5 | Bloqueante del L9 y de todo el L10 |
| **S11** | Entrega anticipada de cada equipo: URL, API key, captura de traza, `verificar_despliegue.py` en verde | 24 h antes de la S11 | Sin ella, una caída del Space el día de la demo sí penaliza (regla de contingencia, `recursos/rubricas/rubrica-final.md`) |

---

## Verificaciones específicas de infraestructura del curso (no del alumno)

Además del stack de modelo/Qdrant/Langfuse, antes de las sesiones que dependen de ellas:

```bash
python docente/verificar_despliegue.py --url <url-del-space-de-referencia> --key <key>   # S8 en adelante
python docente/matriz_seleccion.py --simular                                              # sin credenciales, sirve para probar el arnés
python docente/verificar_guardrails.py --simular                                          # ídem, desde la S6
```

---

## Si algo falla y no hay tiempo de arreglarlo

El modo degradado ya está decidido por servicio — no se improvisa:

| Servicio caído | Modo degradado |
|---|---|
| Simulador de industria | `DATA_SOURCE=csv`: las tools siguen funcionando contra los datasets locales |
| Qdrant Cloud (ingesta de un equipo falló) | Apuntar `QDRANT_COLLECTION` a la colección de respaldo `kb-<track>-respaldo`, de solo lectura |
| HF Inference (cuota agotada) | Cuenta PRO del docente para las demos; trabajo asíncrono escalonado para los alumnos |
| Langfuse Cloud | No hay modo degradado documentado: es bloqueante puro para la S9/S10. Verificar con margen suficiente para reaccionar |
