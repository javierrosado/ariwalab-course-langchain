# Guía del docente · Simulador de industria

> Cómo desplegar, configurar y operar el simulador durante las 12 semanas del curso.
> Público: quien dicta el curso. El alumno no necesita leer esto.

---

## 1. Qué es y por qué existe

El simulador es **infraestructura del curso**, no contenido que el alumno construya. Simula cuatro
empresas peruanas ficticias y expone su dominio por tres superficies (REST, SQL y MCP). Los
alumnos construyen el **agente** que se integra contra él.

```
        SIMULADOR (tú lo despliegas una vez)
                    │
        REST ───────┼─────── MCP
                    │
            comun/datos.py
                    │
         EL AGENTE DEL ALUMNO (esto es lo que él construye)
```

Sin simulador, el Laboratorio 3 sería artificial: el alumno escribiría una "tool contra API
externa" que en realidad lee un CSV. Con simulador, aprende autenticación, timeouts, códigos de
error y aislamiento multi-tenant contra un servicio real.

---

## 2. Despliegue en Hugging Face Spaces

### Paso 1 · Crear el Space

1. En `huggingface.co`, **New Space**.
2. Nombre sugerido: `simulador-industria-<tu-usuario>`.
3. SDK: **Docker**.
4. Visibilidad: **Public** si quieres que los alumnos lo consuman sin token de HF, **Private**
   si prefieres controlarlo (requiere que los alumnos autentiquen también contra HF).

### Paso 2 · Preparar el contenido

El `Dockerfile` espera el contexto en la **raíz del curso**, porque necesita copiar tanto
`simulador-industria/` como `recursos/datasets/`.

```bash
# Desde la raíz del curso
git clone https://huggingface.co/spaces/<usuario>/simulador-industria-<usuario> /tmp/space
cp -r simulador-industria/* /tmp/space/
mkdir -p /tmp/space/datasets
cp -r recursos/datasets/* /tmp/space/datasets/
```

Ajusta el `Dockerfile` copiado al Space para que las rutas sean planas:

```dockerfile
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
ENV DATASETS_DIR=/app/datasets
```

### Paso 3 · Verificar

```bash
curl https://<usuario>-simulador-industria.hf.space/health
```

Debe responder `{"estado":"ok", ...}`. Si responde `degradado`, revisa que `datasets/` se haya
copiado dentro de la imagen.

### Paso 4 · Probar en local antes de desplegar

```bash
cd simulador-industria
pip install -r requirements.txt
PYTHONPATH=. python verificar_simulador.py
```

**33 comprobaciones. No despliegues si alguna falla.**

---

## 3. Generar las API keys de los equipos

Cada equipo necesita su propia clave: es lo que aísla sus escrituras y lo que enseña
autenticación real.

```bash
python - <<'PY'
import json, secrets
equipos = {"demo-key-0000": "demo", "docente-key-9999": "docente"}
for i in range(1, 16):                       # ajusta al número de equipos
    equipos[f"eq{i:02d}-{secrets.token_hex(4)}"] = f"equipo-{i:02d}"
print(json.dumps(equipos, ensure_ascii=False, indent=2))
PY
```

Guarda el resultado como `equipos.json` en el Space y **reparte a cada equipo solo su clave**.

> Conserva la clave `docente-key-9999`: te permite inspeccionar el estado de cualquier equipo
> desde tu propia terminal durante la clase.

---

## 4. Variables de entorno del Space

| Variable | Valor recomendado | Para qué |
|----------|-------------------|----------|
| `DATASETS_DIR` | `/app/datasets` | Dónde están los CSV semilla |
| `DB_PATH` | `/tmp/simulador.db` | Archivo SQLite |
| `EQUIPOS_FILE` | `/app/equipos.json` | Mapa de API keys |
| `CHAOS_RATE` | `0.0` | Fallos espontáneos — súbelo solo en el L7 |
| `HABILITAR_MCP_HTTP` | `1` | Monta el endpoint `/mcp` |

En Spaces, `equipos.json` con claves reales conviene cargarlo como **Secret** y no como archivo
del repositorio.

---

## 5. Operación durante el curso

### Cuándo se usa cada superficie

| Semana | Laboratorio | Qué usa del simulador |
|--------|-------------|-----------------------|
| 1-2 | L1, L2 | Nada: `DATA_SOURCE=csv` |
| **3** | **L3** | **REST** — primera integración real |
| **4** | **L4** | **REST + MCP** (stdio y HTTP) |
| 5 | L5 | REST + Qdrant para lo documental |
| 6 | L6 | REST + guardrails sobre las respuestas |
| **7** | **L7** | REST con `CHAOS_RATE=0.1` — pruebas de estrés |
| 8-11 | L8-L11 | REST desde el agente ya desplegado |

### El hackathon del Laboratorio 7

Sube `CHAOS_RATE` a `0.1` al inicio de la sesión y **avísalo**. Un 10 % de las peticiones fallará
sin motivo aparente. Es la forma más rápida de descubrir qué agentes manejan bien los errores y
cuáles se cuelgan.

Bájalo a `0.0` al terminar.

### Checklist previo a cada sesión síncrona

Ejecútalo **24 horas antes**, no el mismo día:

- [ ] `curl $SIM_BASE_URL/health` responde `ok`
- [ ] Una ruta de cada industria responde `200` con la clave del docente
- [ ] `CHAOS_RATE` está en el valor que corresponde a la sesión
- [ ] El Space no está dormido (los Spaces gratuitos duermen por inactividad)
- [ ] Los otros tres servicios del curso responden: Hugging Face, Qdrant, Langfuse

---

## 6. Reinicio y estado

La base SQLite **se reconstruye desde los CSV en cada arranque**. Es deliberado:

| Consecuencia | Implicancia para la clase |
|--------------|---------------------------|
| El simulador vuelve a un estado conocido | Un reinicio limpia los tickets y siniestros creados |
| Los datos base nunca se corrompen | Ningún equipo puede romperle el laboratorio a otro |
| Las escrituras de los equipos **se pierden** | Avisa antes de reiniciar durante una sesión |

Si necesitas conservar las escrituras entre reinicios, monta `DB_PATH` en un volumen persistente
del Space. Para el curso no hace falta: ningún laboratorio depende de datos creados en la sesión
anterior.

---

## 7. Modo degradado — qué hacer si el Space cae

Este es el riesgo **R14** del ADR: el simulador es un punto único de fallo. Si cae durante una
sesión, se caen los laboratorios de todos los equipos a la vez.

**La mitigación ya está en el código.** Indica a los alumnos:

```dotenv
DATA_SOURCE=csv
```

Las tools siguen funcionando contra los datasets locales. Se pierde la integración por API, pero
la sesión continúa y el agente sigue respondiendo. Es exactamente el patrón de degradación
elegante que el curso enseña.

---

## 8. Diagnóstico de problemas

| Síntoma que reporta el alumno | Causa probable | Solución |
|-------------------------------|----------------|----------|
| `401 Falta la cabecera X-API-Key` | No configuró `SIM_API_KEY` | Revisar su `.env` |
| `401 API key inválida` | Clave mal copiada o de otro curso | Reenviarle su clave |
| `404` en un dato que sí existe | Está consultando el track equivocado | Revisar `COURSE_TRACK` |
| Todo devuelve timeout | El Space está dormido | Una petición a `/health` lo despierta |
| `503` intermitente | `CHAOS_RATE` está activo | Verificar que sea intencional |
| Ve tickets que no creó | Está usando la clave `demo` | Darle su clave de equipo |
| `SimuladorNoDisponible` en todas las tools | `SIM_BASE_URL` mal escrita | Debe incluir `https://` y sin barra final |

### Inspeccionar el estado de un equipo

```bash
curl -H "X-API-Key: docente-key-9999" \
  "https://<space>.hf.space/retail/devoluciones?pedido_id=MS-2026-00001"
```

---

## 9. Extender el simulador

Si quieres agregar una ruta nueva:

1. Añade el endpoint en `routers.py`, dentro del `APIRouter` de la industria.
2. Si expone una tabla nueva, decláralas en `TABLAS_CSV` de `db.py`.
3. Si es una escritura, agrega la tabla a `TABLAS_ESCRITURA` para que se aísle por equipo.
4. Añade una comprobación en `verificar_simulador.py`.
5. Regenera la referencia: `PYTHONPATH=. python generar_referencia_api.py`.
6. Si quieres que las tools la consuman, mapéala en `comun/api_client.py` (`RUTAS` o
   `RUTAS_LISTA`).

> El paso 5 no es opcional: la referencia de API se genera del código en ejecución, y si no la
> regeneras queda desactualizada sin que nadie lo note.

---

## 10. Documentos relacionados

| Documento | Para quién |
|-----------|-----------|
| [`REFERENCIA-API.md`](REFERENCIA-API.md) | Alumnos y docente — todas las rutas con ejemplos reales |
| [`GUIA-ALUMNO.md`](GUIA-ALUMNO.md) | Alumnos — cómo conectar su agente |
| [`GUIA-MCP.md`](GUIA-MCP.md) | Alumnos — transportes stdio y HTTP |
| [`../README.md`](../README.md) | Arquitectura interna del simulador |
| [`../../_memoria/DECISIONES.md`](../../_memoria/DECISIONES.md) | Decisiones D22 a D25 y riesgo R14 |
