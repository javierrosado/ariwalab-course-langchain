# Speaker notes — Sesión 0 · Nivelación

S0 es asíncrona: estas imágenes acompañan la lectura y pueden proyectarse cuando el docente
repase la nivelación. Las cifras que muestran vienen del texto de `fundamentos-llm.md` y
llevan la etiqueta *ejemplo ilustrativo*. Para evidencia, el docente usa las salidas reales
de las cuatro demos de `00-preparacion/code/`, sin capturas con métricas inventadas.
Consultar el estado de cada archivo en el catálogo antes de insertarlo en PPT.

## Slide 01 — Ruta de la Sesión 0

**ID:** IMG-S00-001. **Archivo:** `01-ruta-sesion-0.png`.

**Sección fuente:** [README de S0](../../00-preparacion/README.md), «Ruta de estudio» y «Cuando termines».

**Objetivo pedagógico:** Mostrar el orden de estudio, la duración y la condición bloqueante.

**Mensaje clave:** Sin 8/10 en la autoevaluación no hay Sesión 1.

**Explicación sugerida:** Recorrer LEER → PREPARAR → COMPROBAR; explicar que el glosario se consulta según se necesite y que el retorno desde la compuerta indica repasar antes de repetir.

**Elementos que debe señalar el docente:** los seis pasos con su tiempo, el rombo bloqueante, la flecha de retorno y la banda de condiciones de llegada.

**Ejemplo:** Un alumno con 7/10 vuelve a `fundamentos-llm.md` y ejecuta otra vez las cuatro demos (tabla «Resultado» de la autoevaluación).

**Ejemplo de industria:** Elegir desde ahora una de las cuatro industrias; se formaliza en el Laboratorio 1.

**Pregunta al alumno:** ¿Por qué conviene crear las tres cuentas aunque dos se usen a mitad del curso?

**Error conceptual frecuente:** Tratar la autoevaluación como un trámite.

**Conexión con sesión posterior:** S1 parte de estas condiciones de llegada.

## Slide 02 — Un LLM no es una API normal

**ID:** IMG-S00-002. **Archivo:** `02-llm-no-es-una-api.png`.

**Sección fuente:** [Fundamentos de LLM](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 1, 2 y 5.

**Objetivo pedagógico:** Romper la expectativa de determinismo y contrato fijo.

**Mensaje clave:** El modelo predice el siguiente token con probabilidades; a temperatura 0 la variabilidad baja, pero no desaparece.

**Explicación sugerida:** Leer la columna LLM de la comparación; luego seguir el ejemplo del SOAT hasta la distribución y relacionarla con las tres temperaturas.

**Elementos que debe señalar el docente:** la fila de errores («respuestas seguras pero falsas»), la barra del token más probable y la tarjeta 0.0 marcada para los labs.

**Ejemplo:** Demo 2 (`02_temperatura.py`): mismas preguntas a 0 y a 1.5.

**Ejemplo de industria:** Andina Seguros: la cobertura del SOAT del texto.

**Pregunta al alumno:** ¿Por qué no se prueba un agente con `assert respuesta == "esperado"`?

**Error conceptual frecuente:** Suponer que `temperature=0` garantiza respuestas idénticas.

**Conexión con sesión posterior:** S10 evalúa con métricas.

## Slide 03 — Tokens, contexto y costo

**ID:** IMG-S00-003. **Archivo:** `03-tokens-contexto-costo.png`.

**Sección fuente:** [Fundamentos de LLM](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 3, 4 y 8; [demos](../../00-preparacion/code/README.md), demo 4.

**Objetivo pedagógico:** Explicar que el modelo es stateless y que el historial reenviado domina el costo.

**Mensaje clave:** El historial es lo que encarece una conversación, no la última pregunta.

**Explicación sugerida:** Partir de la definición de token; mostrar qué ocupa la ventana en cada llamada; comparar las barras de entrada de los turnos 1, 5 y 10 con las de salida.

**Elementos que debe señalar el docente:** la partición de `portabilidad`, el segmento Historial, el rótulo «no a escala» y las cuatro palancas.

**Ejemplo:** Demo 1 (`01_tokens.py`) para tokens y demo 4 (`04_costo.py`) para el costo por turno.

**Ejemplo de industria:** AndesMóvil: «¿y el mes pasado?» tras diez turnos reenvía todo el historial.

**Pregunta al alumno:** Si el modelo no recuerda nada entre llamadas, ¿qué es la memoria de un agente?

**Error conceptual frecuente:** Optimizar primero la longitud de la respuesta.

**Conexión con sesión posterior:** S5 (historial y recuperación) y S10 (optimización).

## Slide 04 — Embeddings: buscar por significado

**ID:** IMG-S00-004. **Archivo:** `04-embeddings-significado.png`.

**Sección fuente:** [Fundamentos de LLM](../../00-preparacion/conceptos-previos/fundamentos-llm.md), sección 7; [demos](../../00-preparacion/code/README.md), demo 3.

**Objetivo pedagógico:** Mostrar que la cercanía entre embeddings refleja significado, no palabras compartidas.

**Mensaje clave:** A y B no comparten palabras y aun así están cerca: esa es la base del RAG.

**Explicación sugerida:** Seguir cada frase hasta su vector; ubicar A, B y C en la proyección; leer 0.87 y 0.12 en la escala de similitud coseno.

**Elementos que debe señalar el docente:** el modelo único de embeddings, el rótulo «proyección 2D simplificada» y los tres rangos de la escala.

**Ejemplo:** Demo 3 (`03_embeddings.py`), columna *palabras comunes*.

**Ejemplo de industria:** AndesMóvil: consulta de saldo de datos.

**Pregunta al alumno:** ¿Qué haría una búsqueda con `LIKE` con las frases A y B?

**Error conceptual frecuente:** Leer la proyección 2D como distancias exactas.

**Conexión con sesión posterior:** S5 construye la ingesta y la recuperación en Qdrant.

## Slide 05 — Alucinación y dónde vive el conocimiento

**ID:** IMG-S00-005. **Archivo:** `05-alucinacion-conocimiento.png`.

**Sección fuente:** [Fundamentos de LLM](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 6 y 10.

**Objetivo pedagógico:** Reconocer la alucinación como un fallo sin señal y separar estilo de conocimiento.

**Mensaje clave:** Un dato que cambia no puede vivir en los pesos: el conocimiento va al RAG.

**Explicación sugerida:** Leer el caso del SOAT y subrayar que no hay excepción; presentar las tres defensas como capas complementarias; cerrar con la composición del agente del curso.

**Elementos que debe señalar el docente:** «2 UIT» frente a «1 UIT», la sesión de cada defensa, la columna RAG y la tarjeta Qwen3-32B «genérico, sin afinar».

**Ejemplo:** Pregunta 4 y pregunta 6 de la autoevaluación.

**Ejemplo de industria:** Andina Seguros (SOAT) y AndesMóvil (composición del agente).

**Pregunta al alumno:** ¿Dónde debe vivir un tarifario que cambia cada trimestre?

**Error conceptual frecuente:** Creer que una sola defensa elimina las alucinaciones.

**Conexión con sesión posterior:** S3–S4 (tools), S5 (RAG), S6 (guardrails).

## Slide 06 — Entorno, secretos y configuración

**ID:** IMG-S00-006. **Archivo:** `06-entorno-configuracion.png`.

**Sección fuente:** [Python, entorno y secretos](../../00-preparacion/conceptos-previos/python-y-entorno.md), secciones 2 a 6.

**Objetivo pedagógico:** Situar `.env`, `comun/settings.py` y `comun/provider.py`.

**Mensaje clave:** La configuración entra solo por `comun/settings.py`; cambiar de proveedor es configuración, no código.

**Explicación sugerida:** Seguir `.env` → settings → provider → labs; señalar la línea discontinua a Foundry como bonus; terminar con el `description` de Pydantic y la comprobación final.

**Elementos que debe señalar el docente:** el candado de `.gitignore`, la pestaña `(.venv)`, `AI_PROVIDER` y las comprobaciones 3 y 4.

**Ejemplo:** Ejercicio obligatorio `Reclamo` antes de la Sesión 2.

**Ejemplo de industria:** `COURSE_TRACK` elige la industria del alumno.

**Pregunta al alumno:** ¿Qué ocurre si un lab llama a `os.getenv()` por su cuenta?

**Error conceptual frecuente:** Olvidar activar el `venv` en una terminal nueva (`ModuleNotFoundError`).

**Conexión con sesión posterior:** S2 (salida estructurada), S8 (*Space secrets*), bonus (Foundry).

## Slide 07 — Tres cuentas del curso

**ID:** IMG-S00-007. **Archivo:** `07-tres-cuentas.png`.

**Sección fuente:** [Alta de las 3 cuentas](../../00-preparacion/conceptos-previos/alta-de-cuentas.md).

**Objetivo pedagógico:** Mostrar cuándo se usa cada cuenta y cómo se verifica el stack.

**Mensaje clave:** Las tres cuentas se crean hoy, aunque se usen en S1, S5 y S9.

**Explicación sugerida:** Recorrer la línea de tiempo; en cada tarjeta, detenerse en la advertencia; cerrar con los códigos de salida de `check_stack`.

**Elementos que debe señalar el docente:** el permiso de inferencia de Hugging Face, el estado *Healthy* de Qdrant, los 2 usuarios de Langfuse y el código 1 («sigues hasta S4»).

**Ejemplo:** Salida real de `python -m comun.check_stack` en la máquina del docente.

**Ejemplo de industria:** `QDRANT_COLLECTION=kb-<track>` según la industria elegida.

**Pregunta al alumno:** ¿Qué haces si `check_stack` termina con código 2?

**Error conceptual frecuente:** Crear el token de Hugging Face sin permiso de inferencia.

**Conexión con sesión posterior:** S1 (modelo), S5 (Qdrant), S9 (Langfuse).

## Slide 08 — Anatomía de un LLM

**ID:** IMG-S00-008. **Archivo:** `08-anatomia-llm.png`.

**Sección fuente:** complemento de [Fundamentos de LLM](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 2, 4 y 5. El texto de S0 no desarrolla los componentes internos; la imagen los presenta a nivel conceptual.

**Objetivo pedagógico:** Nombrar las partes de un LLM y ubicar los pesos y lo que controla la aplicación.

**Mensaje clave:** Un LLM no busca ni verifica: convierte la entrada en probabilidades del siguiente token.

**Explicación sugerida:** Recorrer las cinco etapas numeradas; detenerse en el corchete de los pesos y en el bucle que devuelve el token a la entrada.

**Elementos que debe señalar el docente:** la ventana de contexto como entrada, los bloques repetidos N veces, los logits antes del muestreo y la tarjeta «Lo que controla tu aplicación».

**Ejemplo:** La pregunta «¿cuántos gigas…» recorre la tubería una vez por cada token de la respuesta.

**Ejemplo de industria:** AndesMóvil: la consulta de saldo como entrada.

**Pregunta al alumno:** Si los pesos no cambian al conversar, ¿dónde vive un tarifario que cambia cada trimestre?

**Error conceptual frecuente:** Creer que el modelo consulta una base de datos interna o aprende de cada conversación.

**Conexión con sesión posterior:** S1 (modelo y agente), S5 (el conocimiento va al RAG).

## Slide 09 — Ejemplo: la misma consulta, API vs LLM

**ID:** IMG-S00-009. **Archivo:** `09-ejemplo-api-vs-llm.png`.

**Sección fuente:** [Fundamentos de LLM](../../00-preparacion/conceptos-previos/fundamentos-llm.md), sección 1; respuesta 200 de `simulador-industria/docs/REFERENCIA-API.md`; mensaje 404 de `simulador-industria/routers.py`.

**Objetivo pedagógico:** Ver con un caso concreto la diferencia entre un contrato fijo y una salida probabilística sin herramientas.

**Mensaje clave:** El LLM propone la llamada; tu código consulta la API.

**Explicación sugerida:** Leer por filas: la API repite el mismo JSON y falla con un 404 explícito; el LLM sin herramientas cambia la respuesta e inventa cifras con el mismo tono.

**Elementos que debe señalar el docente:** el rótulo «respuestas ilustrativas», la fila de la línea inexistente y las etiquetas de estado de cada celda.

**Ejemplo:** Ejecutar la ruta del simulador desde `REFERENCIA-API.md` y comparar con una respuesta real del modelo sin tools, rotulando que la del modelo puede variar.

**Ejemplo de industria:** AndesMóvil, línea 988837195, periodo 2026-08.

**Pregunta al alumno:** ¿Qué señal te avisa de que la línea 999999999 no existe en cada columna?

**Error conceptual frecuente:** Suponer que el modelo «sabe» el consumo del cliente.

**Conexión con sesión posterior:** S1 (Agentic Loop) y S3 (tools con API externa).

## Slide 10 — Hugging Face: qué ofrece y qué usamos

**ID:** IMG-S00-010. **Archivo:** `10-hugging-face.png`.

**Sección fuente:** [Alta de las 3 cuentas](../../00-preparacion/conceptos-previos/alta-de-cuentas.md), `comun/provider.py` y [Sesión 8](../../modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md); componentes según la documentación oficial consultada el 24-09-2026.

**Objetivo pedagógico:** Distinguir lo que ofrece Hugging Face de lo que usa el curso.

**Mensaje clave:** Hugging Face pone el modelo y el despliegue; el código lo ve solo a través de `comun/provider.py`.

**Explicación sugerida:** Recorrer la leyenda; nombrar los cinco componentes usados con su sesión; seguir el flujo de la derecha hasta los dos modelos y el despliegue de S8.

**Elementos que debe señalar el docente:** el permiso de inferencia del token, el router compatible con OpenAI y los *Space secrets*.

**Ejemplo:** `python -m comun.check_stack --solo-modelo` confirma el acceso al modelo.

**Ejemplo de industria:** El mismo modelo sirve a las cuatro industrias; cambia el system prompt.

**Pregunta al alumno:** ¿Por qué ningún lab crea su propio cliente de Hugging Face?

**Error conceptual frecuente:** Confundir el Hub (repositorios) con Inference Providers (ejecución del modelo).

**Conexión con sesión posterior:** S1 (modelo), S5 (embeddings), S8 (Spaces).

## Slide 11 — Qdrant Cloud: qué ofrece y qué usamos

**ID:** IMG-S00-011. **Archivo:** `11-qdrant-cloud.png`.

**Sección fuente:** [Alta de las 3 cuentas](../../00-preparacion/conceptos-previos/alta-de-cuentas.md), `comun/vectorstore.py` y [Sesión 5](../../modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md); componentes según la documentación oficial consultada el 24-09-2026.

**Objetivo pedagógico:** Distinguir lo que ofrece Qdrant Cloud de lo que usa el curso, y ubicar ingesta y consulta.

**Mensaje clave:** Qdrant guarda el conocimiento: vectores para buscar, payload para citar la fuente.

**Explicación sugerida:** Nombrar los tres componentes de S0 (consola, cluster, API key) y los tres de S5 (colección, puntos, búsqueda); luego seguir ingesta y consulta sobre la misma colección.

**Elementos que debe señalar el docente:** la colección `kb-<track>` con su respaldo, la dimensión 1024 ligada al modelo de embeddings y el filtro por payload.

**Ejemplo:** El estado *Healthy* del cluster en la consola antes de S5.

**Ejemplo de industria:** `kb-telecomunicaciones`, `kb-banca`, `kb-retail`, `kb-seguros`.

**Pregunta al alumno:** ¿Qué pasa si cambias el modelo de embeddings sin recrear la colección?

**Error conceptual frecuente:** Guardar solo el vector y perder el documento fuente en el payload.

**Conexión con sesión posterior:** S5 (RAG) y S7 (elección de arquitectura).

## Slide 12 — Langfuse Cloud: qué ofrece y qué usamos

**ID:** IMG-S00-012. **Archivo:** `12-langfuse-cloud.png`.

**Sección fuente:** [Alta de las 3 cuentas](../../00-preparacion/conceptos-previos/alta-de-cuentas.md), `comun/observability.py`, [Sesión 9](../../modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) y [Sesión 10](../../modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md); componentes según la documentación oficial consultada el 24-09-2026.

**Objetivo pedagógico:** Distinguir lo que ofrece Langfuse de lo que usa el curso.

**Mensaje clave:** Langfuse observa sin tocar el agente: se engancha por callback y recibe datos ya enmascarados.

**Explicación sugerida:** Nombrar los componentes usados por sesión; seguir el flujo agente → callback → enmascarado → proyecto; leer el árbol de la traza; cerrar con el dataset de S10.

**Elementos que debe señalar el docente:** los 2 usuarios por equipo, el enmascarado antes del envío y el juez de S10 que corre en local.

**Ejemplo:** Demo `01_traza_minima.py` de S9 y `01_dataset_langfuse.py` de S10.

**Ejemplo de industria:** La traza de AndesMóvil con `get_customer_plan` y `kb-telecomunicaciones`.

**Pregunta al alumno:** ¿Por qué el DNI no debe llegar a Langfuse aunque el proyecto sea privado?

**Error conceptual frecuente:** Creer que instrumentar exige modificar el código de negocio del agente.

**Conexión con sesión posterior:** S9 (trazas) y S10 (datasets y evaluación).
