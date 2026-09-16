# Verificación del stack — hazlo antes de construir los laboratorios

> **Por qué existe este paso.** Todo el curso, de la sesión 3 en adelante, depende de que el
> modelo haga *tool calling* de forma confiable. No todos los modelos ni todos los proveedores
> de inferencia lo soportan bien. Construir 44 laboratorios sobre un modelo no verificado es
> el riesgo R1 del ADR, y es el único bloqueante técnico del proyecto.
>
> **No pude ejecutarlo por ti:** el entorno de trabajo tiene bloqueado el acceso de red a
> `huggingface.co`, `cloud.qdrant.io` y `cloud.langfuse.com`. Tienes que correrlo desde tu
> terminal normal de Windows, que sí tiene salida a internet.

---

## Paso 1 · Crear las tres cuentas (10 min)

| Servicio | URL | Qué copiar |
|---|---|---|
| Hugging Face | https://huggingface.co/settings/tokens | Token con permiso de **inferencia** |
| Qdrant Cloud | https://cloud.qdrant.io | URL del cluster + API key |
| Langfuse Cloud | https://cloud.langfuse.com | Public key + Secret key |

## Paso 2 · Preparar el entorno

```powershell
cd C:\personal\microsoft\ariwalab-course-langchain
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env
```

## Paso 3 · Ejecutar el verificador

```powershell
python -m comun.check_stack
```

Si aún no tienes Qdrant ni Langfuse y solo quieres validar lo crítico:

```powershell
python -m comun.check_stack --solo-modelo
```

Para ver el traceback completo de un fallo:

```powershell
python -m comun.check_stack --debug
```

---

## Qué comprueba

| # | Comprobación | Crítica | Si falla… |
|---|---|---|---|
| 1 | Variables de entorno | — | Falta completar el `.env` |
| 2 | El modelo de chat responde | — | Token inválido o modelo no disponible en el router |
| 3 | **Tool calling** | ⚠️ **Sí** | **Cambiar de modelo. Sin esto no hay curso** |
| 4 | **Agente con `create_agent()`** | ⚠️ **Sí** | El bucle ReAct no cierra con este modelo |
| 5 | Structured output con Pydantic | — | Afecta la sesión 2 y el clasificador de intención |
| 6 | Embeddings | — | Afecta la sesión 5; probar otro modelo de embeddings |
| 7 | Qdrant: indexar y recuperar | — | Revisar URL y API key del cluster |
| 8 | Langfuse: enviar traza | — | Afecta las sesiones 9 y 10 |

**Códigos de salida:** `0` stack verificado · `1` parcial (el modelo sirve, algún servicio falla) ·
`2` bloqueante (falló una comprobación crítica).

---

## Si la comprobación 3 o 4 falla

No los pruebes de uno en uno: usa el modo comparativa, que corre los cuatro de una pasada y
te dice cuál sirve.

```powershell
python -m comun.check_stack --candidatos
```

La escalera por defecto, en orden de preferencia:

```dotenv
HF_CHAT_MODEL=Qwen/Qwen3-32B                      # ✅ verificado 2026-09-10
HF_CHAT_MODEL=Qwen/Qwen3-30B-A3B                  # ❌ falló la verificación
HF_CHAT_MODEL=Qwen/Qwen3-8B                       # ❌ falló la verificación
HF_CHAT_MODEL=meta-llama/Llama-3.3-70B-Instruct   # ❌ falló la verificación
```

Si **ninguno** funciona por el router de HF, el diseño del curso necesita revisión:
la alternativa sería usar Foundry como proveedor troncal (rompiendo el principio open source)
o buscar otro proveedor de inferencia de modelos abiertos.

---

## Qué hacer con el resultado

Pégame la salida completa del comando en el chat. Con eso:

- cierro los riesgos **R1, R2, R4 y R5** del ADR con evidencia real;
- fijo el modelo definitivo en todo el material;
- arranco la construcción del Módulo 1.


---

## Resultado de la verificación · 2026-09-10

```
VEREDICTO: 1 de 4 candidatos sirven para el curso.
Recomendado por velocidad: Qwen/Qwen3-32B
```

`Qwen3-32B` quedó fijado como modelo del curso (decisión D28). Los otros tres candidatos no
superaron las comprobaciones críticas contra el endpoint real.

**Repetir esta verificación 2 semanas antes de cada dictado.** La disponibilidad de un modelo en
los *inference providers* de Hugging Face puede cambiar entre ediciones del curso, y un modelo
que hoy responde puede dejar de hacerlo.

---

## Los otros verificadores

`check_stack` comprueba que los **servicios** respondan. Estos comprueban que el **material**
esté bien, y ninguno necesita red ni credenciales: puedes correrlos ahora mismo.

| Comando | Qué comprueba | Comprobaciones |
|---------|----------------|----------------|
| `python docente/verificar_tools.py` | Las 24 tools corren contra los datasets reales, ninguna revienta con datos inexistentes, toda docstring cumple A2 y ningún track pasa de 4 tools núcleo | 24 tools |
| `python docente/verificar_structured.py` | La regla A3: validación, reintento con instrucción correctiva, presupuesto de reintentos, few-shot y fallo con `ExtraccionFallida` | 36 |
| `python recursos/datasets/verificar_datasets.py` | Integridad referencial de los 32 datasets y **ausencia de marcas peruanas reales** | 22 |
| `cd simulador-industria && PYTHONPATH=. python verificar_simulador.py` | Las 18 rutas, la autenticación, el aislamiento por equipo, la no exposición de PII y los 6 fallos inyectables | 33 |

---

## Paso 4 · Matriz de selección de herramientas — **pendiente, la corres tú**

Es lo único que queda para cerrar el riesgo **R11**, y es la pregunta que `check_stack` no
responde: *el modelo hace tool calling, sí — pero ¿elige la herramienta correcta?*

Primero pruébalo sin gastar cuota, para ver la forma de la salida:

```powershell
python docente/matriz_seleccion.py --simular
```

Y luego, con el `.env` completo, el de verdad:

```powershell
python docente/matriz_seleccion.py --track telecomunicaciones     # 20 llamadas
python docente/matriz_seleccion.py --csv salida/matriz.csv        # los 4 tracks, 80 llamadas
```

**Lo que hay que mirar no es el porcentaje, es la matriz de confusión.** "El modelo elige mal"
no se puede corregir; *"eligió `get_data_usage` 3 veces donde esperábamos `get_customer_plan`"*
sí: se separan esas dos docstrings diciendo en cada una cuándo NO usarla. El script imprime
esa recomendación por ti.

| Resultado | Qué significa | Qué hacer |
|-----------|----------------|-----------|
| Los 4 tracks ≥ 85 % | La selección es suficiente para el laboratorio 4 | Seguir |
| Un track entre 70 % y 85 % | Docstrings que se solapan | Corregir las señaladas y volver a correr |
| Algún track < 70 % | El problema es de diseño, no de redacción | Revisar si esas 4 tools deberían ser 3 |

**Códigos de salida:** `0` todos los tracks pasan · `1` algún track por debajo del umbral ·
`2` fallo de configuración o de infraestructura.

> Las 4 últimas consultas de cada track **no deben provocar ninguna llamada a tool**: son
> tarifas, coberturas y políticas, que en la sesión 5 se responden con RAG. Si el modelo llama
> a una tool ahí, la docstring no dice **cuándo NO** usarla (regla A2) y el laboratorio 5
> arrancará torcido.
