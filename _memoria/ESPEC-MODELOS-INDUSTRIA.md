# Especificación del modelo y de la personalización por industria

> **Decisión tomada: CAMINO A.** No hay fine-tuning. Los cuatro tracks corren sobre el mismo
> modelo base y la personalización por industria vive en el system prompt y en la base de
> conocimiento.
>
> **Destinatario:** el profesor y quien mantenga el curso.
> **Fecha de la decisión:** 2026-09-10 · Javier Rosado · Ariwa Labs
> **Reemplaza:** la versión que evaluaba dos caminos alternativos.

---

## 1. La regla que gobierna todo

```
              ¿Qué se le quiere dar al modelo?
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      CONOCIMIENTO                  ESTILO
   tarifas · pólizas ·        tono · jerga del sector ·
   políticas · catálogos      formato · límites de actuación
             │                         │
             ▼                         ▼
      Base de conocimiento        System prompt
        (Qdrant Cloud)         (comun/prompts_industria.py)
             │                         │
             └────────────┬────────────┘
                          ▼
              Ninguno de los dos vive en los pesos
```

**El conocimiento va al RAG. El estilo va al prompt. Los pesos no se tocan.**

---

## 2. El modelo del curso

| Parámetro | Valor | Por qué |
|---|---|---|
| Modelo | **`Qwen/Qwen3-32B`** | Denso, 32B. Tool calling nativo, 100+ idiomas, 32K contexto, Apache 2.0 |
| **El mismo para las 4 industrias** | **Sí, sin excepción** | Una configuración de servicio, una convención de prompts, un solo playbook de errores |
| Proveedor | Hugging Face Inference (router compatible con OpenAI) | Principio P2: nada corre en local |
| Temperatura en laboratorios | `0.0` | Los agentes deben ser lo más reproducibles posible |
| Modo de razonamiento | **non-thinking** (`HF_ENABLE_THINKING=false`) | Más rápido y barato; las trazas de razonamiento pueden interferir con el parseo de `tool_call` |
| Fine-tuning | **Ninguno** | Ver §3 |

**Un solo modelo que verificar.** Ese es, en una línea, el argumento del camino A.

> **Por qué este modelo y no otro.** El 2026-09-10 se probó una escalera de 4 candidatos con
> `check_stack --candidatos` contra el endpoint real. **Solo `Qwen3-32B` pasó** las
> comprobaciones críticas de tool calling y bucle ReAct. No es una elección de catálogo:
> es el resultado de una medición (D28).

---

## 3. Por qué no hay fine-tuning

| Criterio | Camino A · elegido | Camino B · descartado |
|---|---|---|
| Qué personaliza | System prompt + colección Qdrant | Tono y jerga, en los pesos |
| Modelos a verificar | **1** | 4 |
| Endpoints a operar | **1** | 4 |
| Costo de entrenamiento | **$0** | ~$3-8 por modelo |
| Costo de operación | 1 GPU | 4 GPU |
| Tiempo hasta tener algo usable | **Horas** | 2-3 semanas de armar datasets |
| Riesgo de perder tool calling | **Cero** | Real y difícil de detectar |
| Cambiar el tono de un agente | Editar texto | Reentrenar |
| Portabilidad a otro proveedor | **Total** | Requiere republicar el modelo |
| Riesgo de retrasar el dictado | **Nulo** | Alto |

El 85 % de la sensación de "modelo especializado en seguros" la producen el system prompt y el
RAG, no los pesos. El 15 % restante no justifica cuadruplicar el riesgo, el costo y el trabajo
de verificación.

> Si en una segunda edición del curso se quiere afinar los modelos, el apéndice de este
> documento conserva la especificación técnica para hacerlo sin romper nada.

---

## 4. Cómo se personaliza cada industria

La personalización tiene exactamente **dos piezas**, ambas editables como texto.

### Pieza 1 · System prompt

Vive en `comun/prompts_industria.py`. Cada industria compone cinco bloques, en este orden:

| # | Bloque | Qué fija | ¿Común o propio? |
|---|---|---|---|
| 1 | **Identidad** | Quién es el agente y a quién atiende | Propio de la industria |
| 2 | **Jerga del sector** | El vocabulario que el cliente reconoce | Propio de la industria |
| 3 | **Estilo general** | Español peruano, respuestas breves, sin emojis | Común a las 4 |
| 4 | **Recuperación obligatoria** | Salvaguarda A6: citar antes de afirmar | Común a las 4 |
| 5 | **Límites y escalamiento** | Qué NO puede hacer y cuándo deriva | Propio de la industria |

El orden importa: la identidad al inicio fija el rol; los límites al final quedan cerca de la
consulta del usuario, que es donde más pesan.

```python
from comun.prompts_industria import get_system_prompt

agente = create_agent(
    get_chat_model(),
    tools=TOOLS_NUCLEO,
    system_prompt=get_system_prompt(),   # resuelve por COURSE_TRACK
)
```

### Pieza 2 · Base de conocimiento

Cada industria tiene su colección en Qdrant, alimentada por los documentos `.md` de
`recursos/datasets/<track>/`: tarifarios, condicionados, políticas y reglamentos.

| Track | Colección | Documentos |
|---|---|---|
| `telecomunicaciones` | `kb-telecomunicaciones` | tarifario, reglamento de reclamos, portabilidad |
| `banca` | `kb-banca` | tarifario de comisiones, política de fraude, contrato de tarjeta |
| `retail` | `kb-retail` | política de devoluciones, FAQ de despacho, garantías |
| `seguros` | `kb-seguros` | condicionado SOAT, tabla de coberturas, procedimiento de siniestros |

**Ninguna cifra de negocio está en el prompt.** Todas viven en los documentos, para que se
puedan citar, auditar y actualizar sin tocar el agente.

---

## 5. Los límites de actuación no son decorativos

El bloque 5 de cada prompt es la primera línea de defensa de los guardrails del Laboratorio 6.
Sale directamente de las secciones *"límites de actuación del asistente"* que ya están escritas
en los documentos RAG de cada industria.

| Industria | Límite más crítico |
|---|---|
| Telco | No prometer ni calcular compensaciones económicas |
| **Banca** | **Nunca ejecutar transferencias. Nunca mostrar la tarjeta completa** |
| Retail | No aprobar devoluciones fuera de política |
| **Seguros** | **Nunca liquidar ni estimar el monto de un siniestro** |

> Un límite escrito solo en el system prompt es una **sugerencia**. En el Laboratorio 6 esos
> mismos límites se implementan en código, donde pasan a ser **garantías**. El prompt es la
> primera capa, no la única.

---

## 6. Consecuencias de diseño derivadas del tamaño del modelo

El curso está calibrado para que **la fiabilidad se componga a favor y no en contra**:

| # | Regla | Dónde aplica |
|---|---|---|
| A1 | **3-4 tools** enlazadas por agente, nunca 6 | L4 en adelante |
| A2 | Docstrings con verbo + cuándo usarla + **cuándo NO** | Todas las tools |
| A3 | `with_structured_output()` con validación y un reintento | L2 en adelante |
| A4 | Tope duro de iteraciones + errores de tool redactados para el modelo | L3 en adelante |
| A5 | Few-shot en los prompts críticos | L2, L4, L6 |
| A6 | Obligar a recuperar ante afirmaciones sobre tarifas o coberturas | L5 |

> **A2 no es una concesión al modelo pequeño, es una mejora del curso.** Un 72B perdona
> descripciones ambiguas y el alumno nunca descubre por qué importan. Un 7B no perdona.

---

## 7. Verificación — una sola, no cuatro

```powershell
python -m comun.check_stack
```

| # | Criterio | Umbral |
|---|---|---|
| C1 | El modelo responde | Binario |
| C2 | Emite `tool_calls` sintácticamente válidos | 20/20 |
| C3 | Elige la tool correcta entre 4 | ≥ 18/20 |
| C4 | `with_structured_output()` devuelve JSON válido | ≥ 19/20 |
| C5 | Cierra un bucle ReAct de 2 pasos sin quedarse en loop | ≥ 18/20 |
| C6 | Con el system prompt de la industria, **llama al retriever en vez de responder de memoria** | ≥ 18/20 |
| C7 | Latencia del primer token, en caliente | < 3 s |

C2, C4 y C5 corresponden a las comprobaciones 3, 4 y 5 de `comun/check_stack.py`.

**C6 sigue siendo relevante aun sin fine-tuning**, aunque su riesgo baja mucho: un modelo base no
conoce el tarifario de AndesMóvil, así que no tiene de dónde responder de memoria. Se verifica
igual, porque la salvaguarda A6 debe funcionar.

---

## 8. Qué se necesita del profesor

Con el camino A la lista es corta:

1. **Un endpoint de Hugging Face** con `Qwen3-32B`, o el uso del router serverless.
2. **Confirmar que expone la ruta compatible con OpenAI** con soporte del parámetro `tools`.
3. Nada más. No hay datasets de entrenamiento, ni chat templates que revisar, ni cuatro modelos
   que mantener.

---

## Apéndice · Especificación de fine-tuning, por si se retoma

> **No aplica al curso actual.** Se conserva para una eventual segunda edición.

Si alguna vez se decide afinar modelos por industria, estas son las condiciones que evitarían
romper el curso:

| Parámetro | Valor |
|---|---|
| Base | El modelo del curso, el mismo para las 4 industrias |
| Técnica | **LoRA**, nunca full fine-tuning |
| `r` / `lora_alpha` / `dropout` | 8-16 / 16-32 / 0.05 |
| `target_modules` | Solo atención: `q_proj, k_proj, v_proj, o_proj` |
| Épocas | 1-2, no más |
| Tamaño del dataset | 400-800 ejemplos por industria |
| **Composición del dataset** | 50 % conversación de dominio · **25 % ejemplos con `tool_call`** · 15 % rechazo y escalamiento · 10 % structured output |
| **Prohibido en el dataset** | Tarifas, coberturas, políticas y cifras de negocio. Eso vive en el RAG |
| `chat_template` | **No modificar.** El bloque de `<tools>` debe sobrevivir al merge |

Verificación obligatoria del template antes de desplegar:

```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("<modelo>")
tools = [{"type": "function", "function": {"name": "consultar_saldo",
          "description": "Consulta el saldo de una línea",
          "parameters": {"type": "object", "properties": {"numero_linea": {"type": "string"}}}}}]
p = tok.apply_chat_template([{"role": "user", "content": "saldo"}],
                            tools=tools, tokenize=False, add_generation_prompt=True)
assert "consultar_saldo" in p, "EL TEMPLATE PERDIÓ EL SOPORTE DE TOOLS"
```

Y el plan de contingencia si un modelo afinado pierde el tool calling: usarlo como **herramienta
de dominio** detrás de un orquestador genérico, en vez de descartarlo.
