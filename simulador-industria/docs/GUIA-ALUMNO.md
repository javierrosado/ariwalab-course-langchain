# Guía del alumno · Conectar tu agente al simulador

> Desde el **Laboratorio 3**, tus herramientas dejan de leer archivos y empiezan a consultar un
> servicio real. Esta guía explica cómo, y qué cambia en tu código.
>
> Respuesta corta a lo segundo: **nada**. Y esa es la lección.

---

## 1. Qué es el simulador

Es un servicio que se comporta como la empresa de tu industria. Tiene clientes, pólizas, pedidos
o cuentas, según tu track, y responde por HTTP como lo haría un sistema real: con autenticación,
con códigos de error y, a veces, con fallos.

| Tu track | Empresa que simula |
|----------|--------------------|
| `telecomunicaciones` | AndesMóvil |
| `banca` | Banco Inti |
| `retail` | MercaSur |
| `seguros` | Andina Seguros |

Todas son ficticias y todos los datos son sintéticos.

---

## 2. Configuración

Tu docente te dará dos datos. Ponlos en tu `.env`:

```dotenv
DATA_SOURCE=api
SIM_BASE_URL=https://<usuario>-simulador-industria.hf.space
SIM_API_KEY=eq03-a1b2c3d4
SIM_TIMEOUT=10
```

Comprueba que llegas:

```bash
curl $SIM_BASE_URL/health
```

Y que tu clave funciona:

```bash
curl -H "X-API-Key: $SIM_API_KEY" "$SIM_BASE_URL/telco/clientes/988837195"
```

> Tu API key es **personal de tu equipo**. Identifica quién eres y aísla lo que creas: los
> reclamos, devoluciones o siniestros que registres no los ve ningún otro equipo. No la compartas
> ni la subas al repositorio.

---

## 3. El momento en que cambia todo (y no cambia nada)

En el Laboratorio 2 tus tools leían archivos. En el Laboratorio 3 consultan una API. Lo único que
haces es cambiar una línea:

```dotenv
DATA_SOURCE=csv     # Laboratorios 1 y 2
DATA_SOURCE=api     # Laboratorio 3 en adelante
```

**Tus herramientas no se tocan.** Siguen llamando a lo mismo:

```python
from comun import datos

fila = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
```

Por dentro, `comun/datos.py` decide si eso es una lectura de archivo o una petición HTTP.

```
   domain_tools.py          ← tu código, no cambia
          │
   comun/datos.py           ← decide la fuente según DATA_SOURCE
          │
     ┌────┴────┐
     ▼         ▼
   CSV      API REST
```

Esa indirección parecía innecesaria en el Laboratorio 2. Ahora entiendes para qué era.

Comprueba desde qué fuente estás leyendo:

```python
from comun.datos import describe_fuente
print(describe_fuente())
# Simulador de industria · https://... · track=telecomunicaciones
```

---

## 4. Lo nuevo: ahora las cosas fallan

Un archivo local siempre está ahí. Un servicio, no. Tu tool debe distinguir **dos situaciones que
antes eran una sola**:

| Excepción | Qué significa | Qué debe responder tu tool |
|-----------|---------------|----------------------------|
| `DatoNoEncontrado` | El dato no existe | *"No existe la línea 999999999, verifica el número"* |
| `FuenteNoDisponible` | No se pudo consultar | *"El sistema no responde, intenta más tarde"* |

La diferencia importa porque **el agente actúa distinto** ante cada una. Ante la primera le pide
otro dato al usuario; ante la segunda, informa y no insiste.

### El patrón que debes usar

```python
from langchain_core.tools import tool
from comun import datos
from comun.datos import DatoNoEncontrado, FuenteNoDisponible

@tool(args_schema=LineaInput)
def get_customer_plan(numero_linea: str) -> str:
    """Devuelve el plan contratado, el estado y el distrito de una línea móvil.

    Úsala cuando el cliente pregunte qué plan tiene o si su línea está activa.
    NO la uses para consultar consumo de datos: para eso usa get_data_usage.
    """
    try:
        c = datos.buscar_uno("clientes.csv", "numero_linea", numero_linea, TRACK)
    except DatoNoEncontrado:
        return (f"No existe la línea {numero_linea} en los registros. "
                f"Verifica el número con el cliente: debe tener 9 dígitos.")
    except FuenteNoDisponible as e:
        return f"No pude consultar el sistema en este momento. {e}"

    return (f"Línea {c['numero_linea']} · Plan: {c['plan_nombre']} · "
            f"Estado: {c['estado']}")
```

> **Regla de oro:** una tool **nunca** deja escapar una excepción. Una excepción sin capturar
> rompe el bucle ReAct y el agente muere. Un texto explicativo lo deja replantear.

---

## 5. Provocar fallos a propósito

El Assignment A1 te pide documentar **tres escenarios**: éxito, dato inexistente y API caída. El
tercero no tienes que esperarlo: lo provocas.

```bash
curl -H "X-API-Key: $SIM_API_KEY" \
  "$SIM_BASE_URL/telco/clientes/988837195?_fallo=error503"
```

| `_fallo` | Qué ocurre | Qué debes comprobar |
|----------|------------|---------------------|
| `error503` | Service Unavailable | Tu tool devuelve texto, no lanza excepción |
| `error500` | Internal Server Error | Ídem |
| `timeout` | Tarda 30 segundos | Tu cliente corta a los 10 (`SIM_TIMEOUT`) |
| `lento` | Responde en 5 segundos | El agente no se cuelga |
| `vacio` | 200 con cuerpo vacío | Tu tool no revienta con un `KeyError` |
| `malformado` | 200 con un JSON que no cumple el contrato | Ídem |

Los dos últimos son los que más gente falla: un `200` no garantiza que el cuerpo sea el esperado.

### Cómo probarlo desde tu código

```python
import httpx, os

def probar_fallo(fallo: str):
    with httpx.Client(
        base_url=os.environ["SIM_BASE_URL"],
        headers={"X-API-Key": os.environ["SIM_API_KEY"]},
        timeout=10,
    ) as c:
        r = c.get(f"/telco/clientes/988837195?_fallo={fallo}")
        print(f"{fallo:>12} → {r.status_code}")

for f in ["error500", "error503", "vacio", "malformado"]:
    probar_fallo(f)
```

---

## 6. Explorar la API

La documentación interactiva está viva:

```
$SIM_BASE_URL/docs
```

Puedes lanzar peticiones desde el navegador. Pon tu API key en el botón **Authorize**.

Otras rutas útiles:

| Ruta | Para qué |
|------|----------|
| `/` | Qué industrias y superficies hay |
| `/health` | Si el servicio está vivo (no pide API key) |
| `/fallos` | Catálogo de fallos simulables |
| `/docs` | Documentación interactiva |

La lista completa de rutas con ejemplos reales está en
[`REFERENCIA-API.md`](REFERENCIA-API.md).

---

## 7. Errores frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| `401 Falta la cabecera X-API-Key` | `SIM_API_KEY` vacía en tu `.env` | Complétala |
| `401 API key inválida` | Clave mal copiada | Pide a tu docente que te la reenvíe |
| `404` en un dato que existe | Estás mirando otro track | Revisa `COURSE_TRACK` en tu `.env` |
| Todo da timeout | El Space está dormido | Llama a `/health` una vez y reintenta |
| `SimuladorNoDisponible` siempre | `SIM_BASE_URL` mal escrita | Debe llevar `https://` y **sin barra final** |
| Ves datos que no creaste | Estás usando la clave `demo` | Usa la clave de tu equipo |

### Si el simulador se cae en plena clase

No te bloquees. Cambia una línea:

```dotenv
DATA_SOURCE=csv
```

Tus tools vuelven a leer los datasets locales y sigues trabajando. Pierdes la integración por
API, pero el agente funciona. Eso se llama **degradación elegante**, y es exactamente lo que
debe hacer un sistema de producción.

---

## 8. Qué sigue

| Laboratorio | Qué agregas |
|-------------|-------------|
| **L3** | Tu primera tool contra la API + los 3 escenarios del Assignment A1 |
| **L4** | Herramientas por **MCP** — ver [`GUIA-MCP.md`](GUIA-MCP.md) |
| **L5** | RAG: lo documental va a Qdrant, lo transaccional sigue en la API |
| **L6** | Guardrails sobre lo que devuelve la API |
| **L7** | Pruebas de estrés con `CHAOS_RATE` activo |
