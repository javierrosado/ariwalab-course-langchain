# Autoevaluación · Sesión 0

> **Bloqueante.** Necesitas **8 de 10** para entrar a la Sesión 1.
> Responde sin consultar el material. Las respuestas están al final.
> Tiempo estimado: 30 minutos.

No es un trámite: cada pregunta corresponde a algo que usarás desde el primer laboratorio.

---

## Parte A · Fundamentos (6 preguntas)

**1.** Un cliente escribe la frase *"Quiero solicitar la portabilidad numérica de mi línea."*
¿Cuál de estas afirmaciones es correcta?

- a) Consume 8 tokens, uno por palabra
- b) Consume aproximadamente 13 tokens, porque las palabras largas se parten en fragmentos
- c) Consume 55 tokens, uno por carácter
- d) El número de tokens es igual en cualquier modelo

---

**2.** Tu agente lleva 10 turnos de conversación. El usuario escribe solo *"¿y el mes pasado?"*.
¿Qué se envía al modelo en esa llamada?

- a) Solo esas cuatro palabras: el modelo recuerda el resto
- b) El system prompt, las herramientas, los fragmentos recuperados **y toda la conversación previa**
- c) Un identificador de sesión que el modelo usa para recuperar el historial de su memoria
- d) Solo los últimos dos turnos, porque el modelo descarta lo antiguo automáticamente

---

**3.** Ejecutas el mismo prompt tres veces con `temperature=0` y obtienes respuestas ligeramente
distintas. ¿Qué concluyes?

- a) Hay un error en tu código: con temperatura 0 debe ser idéntico
- b) El modelo está mal configurado
- c) Es esperable: `temperature=0` reduce mucho la variabilidad pero no la elimina
- d) Necesitas bajar la temperatura a un valor negativo

---

**4.** El agente responde con total seguridad que *"el SOAT cubre 2 UIT por gastos de sepelio"*,
cuando en realidad es 1 UIT. ¿Qué ocurrió y por qué es peligroso?

- a) Una excepción silenciosa; se detecta con `try/except`
- b) Un timeout del servicio; se detecta por el código de estado
- c) Una alucinación; es peligrosa porque **no hay ninguna señal de error**
- d) Un error de red; se detecta reintentando

---

**5.** Estas dos frases no comparten ninguna palabra significativa:
*"¿Cuántos gigas me quedan?"* y *"Consulta del consumo de datos disponibles"*.
Su similitud coseno es 0.87. ¿Qué significa?

- a) Que el sistema falló: sin palabras comunes la similitud debe ser baja
- b) Que sus embeddings están cerca porque **significan algo parecido**
- c) Que ambas tienen la misma cantidad de caracteres
- d) Que el modelo memorizó ambas frases durante el entrenamiento

---

**6.** El tarifario de tu empresa cambia cada trimestre. ¿Dónde debe vivir esa información?

- a) En el fine-tuning del modelo, para que la sepa de memoria
- b) En el system prompt, copiada completa
- c) En el **RAG**, porque cambia, debe citarse y debe poder auditarse
- d) En el nombre de las herramientas

---

## Parte B · Agentes y arquitectura (2 preguntas)

**7.** El modelo genera `consultar_saldo(numero_linea="987654321")`. ¿Qué pasó exactamente?

- a) El modelo ejecutó la función y ya tiene el resultado
- b) El modelo **generó una petición**; tu código decide si la ejecuta y le devuelve el resultado
- c) El modelo se conectó a la base de datos de la empresa
- d) El modelo inventó un dato con formato de función

---

**8.** ¿Por qué en este curso las docstrings de las herramientas dicen explícitamente
*"NO la uses para..."*?

- a) Por convención de estilo de Python
- b) Para la documentación técnica del proyecto
- c) Porque **la docstring es el prompt** que el modelo lee para decidir, y un modelo de 7B se
  confunde con descripciones ambiguas
- d) Porque lo exige LangChain

---

## Parte C · Entorno (2 preguntas)

**9.** Al ejecutar un script obtienes `ModuleNotFoundError: No module named 'langchain'`.
¿Cuál es la causa más probable?

- a) Falta instalar Python
- b) El entorno virtual no está activado en esa terminal
- c) El token de Hugging Face expiró
- d) El cluster de Qdrant está caído

---

**10.** Vas a subir tu proyecto a GitHub. ¿Qué haces con el archivo `.env`?

- a) Lo subo: así mi compañero tiene las credenciales
- b) Lo subo pero renombrado a `env.txt`
- c) **No lo subo nunca**; está en `.gitignore` y cada persona usa su propio token
- d) Lo subo con las claves parcialmente ocultas

---

## Autocorrección

<details>
<summary><b>Ver respuestas y explicaciones</b></summary>

| # | Respuesta | Por qué |
|---|-----------|---------|
| 1 | **b** | Un token es un fragmento, no una palabra. `portabilidad` se parte en varios trozos, y cada tokenizador produce un conteo distinto |
| 2 | **b** | El modelo es *stateless*. La "memoria" es que tu código reenvía todo el historial en cada llamada. Por eso el costo crece turno a turno |
| 3 | **c** | Hay no determinismo en el hardware y el paralelismo del servidor. Por eso la evaluación de la sesión 10 usa métricas y no comparación exacta de texto |
| 4 | **c** | Una alucinación llega sin excepción, sin código de error y con el mismo tono de seguridad que una respuesta correcta. Las tres defensas del curso son tools, RAG y guardrails |
| 5 | **b** | Los embeddings representan significado, no forma. Esto es justamente lo que una búsqueda por palabras clave no puede hacer |
| 6 | **c** | El conocimiento va al RAG; el estilo va al modelo. Un dato que cambia cada trimestre no puede vivir en los pesos |
| 7 | **b** | El LLM **genera** la llamada, tu código la **ejecuta**. Esa separación es lo que permite validar, autorizar y auditar |
| 8 | **c** | La docstring se envía al modelo dentro del esquema. Decir cuándo NO usar una tool reduce las confusiones, y con 7B esa diferencia decide si el laboratorio funciona |
| 9 | **b** | Es el error más frecuente del curso. El `venv` se activa en cada terminal nueva; verifica que el prompt muestre `(.venv)` |
| 10 | **c** | Un token publicado en GitHub se detecta y se abusa en minutos. Si lo expones, revócalo y genera otro |

</details>

---

## Resultado

| Aciertos | Qué hacer |
|----------|-----------|
| **10** | Listo. Nos vemos en la Sesión 1 |
| **8-9** | Aprobado. Repasa las secciones de las que fallaste |
| **6-7** | Vuelve a `fundamentos-llm.md` y ejecuta otra vez las 4 demos |
| **< 6** | Rehaz la sesión 0 completa y avisa al docente para una sesión de apoyo |

---

## Checklist final antes de la Sesión 1

- [ ] Entorno virtual creado y `requirements.txt` instalado
- [ ] `.env` creado a partir de `.env.example`, con `HF_TOKEN` válido
- [ ] Cuenta de Hugging Face con token **con permiso de inferencia**
- [ ] Cluster de Qdrant Cloud creado y en estado *Healthy*
- [ ] Proyecto de Langfuse Cloud creado, con tu compañero de equipo invitado
- [ ] Las 4 demos ejecutadas y comprendidas
- [ ] `python -m comun.check_stack` ejecutado sin errores críticos
- [ ] Autoevaluación con 8 o más aciertos
- [ ] Una industria en mente: **telecomunicaciones, banca, retail o seguros**
