# Alta de las 3 cuentas del curso

> Sesión 0 · paso 4 · 40 minutos
> Las tres tienen plan gratuito y **ninguna pide tarjeta de crédito**.

---

## Resumen

| # | Servicio | Para qué | Desde | Plan gratuito |
|---|----------|----------|-------|---------------|
| 1 | **Hugging Face** | Modelo de chat y embeddings | Sesión 1 | Créditos mensuales de inferencia |
| 2 | **Qdrant Cloud** | Base vectorial del RAG | Sesión 5 | 1 GB RAM / 4 GB disco, **permanente** |
| 3 | **Langfuse Cloud** | Trazabilidad y evaluación | Sesión 9 | 50 000 unidades/mes, **2 usuarios** |

> **Créalas las tres hoy**, aunque dos no se usen hasta la mitad del curso. Un equipo que deja
> Qdrant para la semana 5 llega a esa sesión sin poder hacer el laboratorio, y no hay alternativa
> local: el curso es 100 % en línea por diseño.

---

## 1 · Hugging Face

Es la plataforma de modelos abiertos. Aquí vive el modelo que usarás en todos los laboratorios.

**Pasos**

1. Entra a `huggingface.co` y crea una cuenta con tu correo.
2. Confirma el correo.
3. Ve a **Settings → Access Tokens**.
4. Crea un token nuevo. Ponle un nombre reconocible, por ejemplo `curso-agentes`.
5. ⚠️ **Marca el permiso de inferencia** (*Make calls to Inference Providers* o equivalente).
   Sin ese permiso el token existe pero devuelve `401` en cada llamada. Es el error número
   uno de esta sesión.
6. Copia el token. **Solo se muestra una vez.**

**En tu `.env`**

```dotenv
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
HF_BASE_URL=https://router.huggingface.co/v1
HF_CHAT_MODEL=Qwen/Qwen3-32B
HF_ENABLE_THINKING=false
HF_EMBEDDING_MODEL=intfloat/multilingual-e5-large
```

**Verificación**

```powershell
python -m comun.check_stack --solo-modelo
```

---

## 2 · Qdrant Cloud

Es la base de datos vectorial donde vivirá el conocimiento de tu agente.

**Pasos**

1. Entra a `cloud.qdrant.io` y crea una cuenta.
2. Crea un **cluster gratuito**. Elige la región más cercana disponible.
3. Espera a que el estado pase a *Healthy*: tarda 1 o 2 minutos.
4. Copia la **URL del cluster**. Termina en `:6333`.
5. Genera una **API key** desde la sección de claves del cluster y cópiala.

**En tu `.env`**

```dotenv
QDRANT_URL=https://xxxxxxxx.us-east.aws.cloud.qdrant.io:6333
QDRANT_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
QDRANT_COLLECTION=kb-telecomunicaciones
```

Ajusta `QDRANT_COLLECTION` al track que elijas: `kb-telecomunicaciones`, `kb-banca`,
`kb-retail` o `kb-seguros`.

**Límites del plan gratuito**

| Recurso | Límite | ¿Alcanza para el curso? |
|---------|--------|--------------------------|
| RAM | 1 GB | Sí, de sobra |
| Disco | 4 GB | Sí: el corpus de un track pesa menos de 1 MB |
| Nodos | 1 | Suficiente |
| Duración | **Permanente** | No caduca durante el curso |

---

## 3 · Langfuse Cloud

Es donde verás por dentro lo que hace tu agente: cada paso, cada herramienta, cada milisegundo.

⚠️ **Antes de crear la cuenta, ponte de acuerdo con tu compañero de equipo.** El plan gratuito
admite **2 usuarios por proyecto**, y por eso los equipos del curso son de 2 personas. Uno crea
la organización e invita al otro.

**Pasos**

1. Entra a `cloud.langfuse.com` y crea una cuenta.
2. Crea una organización con el nombre de tu equipo.
3. Invita a tu compañero como segundo usuario.
4. Crea un proyecto, por ejemplo `agente-telco-equipo3`.
5. Ve a **Settings → API Keys** y crea un par de claves.
6. Copia la **public key** (`pk-lf-...`) y la **secret key** (`sk-lf-...`).

**En tu `.env`**

```dotenv
LANGFUSE_PUBLIC_KEY=pk-lf-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
LANGFUSE_SECRET_KEY=sk-lf-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
LANGFUSE_HOST=https://cloud.langfuse.com
```

**Límites del plan gratuito**

| Recurso | Límite | Implicancia |
|---------|--------|-------------|
| Unidades | 50 000 al mes | Suficiente para las sesiones 9 y 10 |
| Retención | 30 días | Descarga lo que quieras conservar |
| Usuarios | **2 por organización** | Determina el tamaño de los equipos |

---

## Verificación completa

Con las tres cuentas creadas y el `.env` completo:

```powershell
python -m comun.check_stack
```

Salida esperada: las 8 comprobaciones en verde y el veredicto **STACK VERIFICADO**.

| Código de salida | Significado | Qué hacer |
|------------------|-------------|-----------|
| `0` | Todo funciona | Continúa con las demos |
| `1` | El modelo funciona, algún servicio falla | Revisa Qdrant o Langfuse; puedes seguir hasta la sesión 4 |
| `2` | Falló una comprobación crítica | Avisa al docente: es del modelo, no tuyo |

---

## Higiene de credenciales

Las tres claves que acabas de generar son credenciales reales.

- [ ] El `.env` está en `.gitignore` y **nunca** se sube al repositorio
- [ ] No compartes tokens por chat, correo ni capturas de pantalla
- [ ] Si expones uno por accidente, lo **revocas** y generas otro
- [ ] Cada integrante del equipo usa su propio token de Hugging Face

Esto no es burocracia: en la sesión 6 vas a construir guardrails contra fuga de datos, y sería
incoherente hacerlo con tus propias claves publicadas en un repositorio.

**Siguiente paso:** ejecutar las demos en [`../code/`](../code/)
