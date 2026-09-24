# Guía de MCP · Conectar herramientas que no escribiste

> Laboratorio 4. El simulador expone 6 herramientas por **Model Context Protocol**, y las expone
> por **dos transportes distintos a propósito**, para que compares.

---

## 1. Qué problema resuelve MCP

Hasta el Laboratorio 3, cada herramienta de tu agente era una función que escribiste tú, con su
`@tool` y su schema. Eso funciona mientras las herramientas sean tuyas.

En una empresa real no lo son. El equipo de fraude tiene su servicio, el de logística el suyo, y
ninguno va a reescribir sus funciones dentro de tu agente.

```
   SIN MCP                          CON MCP
   ───────                          ───────
   agente ──► integración a medida  agente ──► MCP ──► servidor de fraude
          ──► integración a medida         └──► MCP ──► servidor de logística
          ──► integración a medida         └──► MCP ──► servidor de inventario

   N integraciones distintas        Un protocolo, N servidores
```

MCP es un estándar abierto: el agente **descubre** qué herramientas hay en tiempo de ejecución,
con sus nombres, descripciones y esquemas. No las conoce de antemano.

> Analogía para la clase: MCP es el **USB-C** de las herramientas de IA. Un conector, muchos
> dispositivos.

---

## 2. Las 6 herramientas que expone el simulador

Son las **tools opcionales** de los cuatro tracks — las que en el Laboratorio 4 son el reto.

| Herramienta | Industria | Qué hace |
|-------------|-----------|----------|
| `check_portability_eligibility` | Telco | Evalúa si una línea puede portarse |
| `get_coverage_by_district` | Telco | Cobertura e incidencias de un distrito |
| `get_transfer_limits` | Banca | Límites de transferencia de una cuenta |
| `estimate_delivery` | Retail | Costo y plazo de despacho |
| `list_affiliated_clinics` | Seguros | Red de clínicas por distrito |
| `get_vehicle_info` | Seguros | Datos del vehículo por placa |

Fíjate en algo: **tú no escribiste ninguna**, y aun así tu agente va a poder usarlas.

---

## 3. Los dos transportes

| | **stdio** | **HTTP** |
|---|-----------|----------|
| Cómo corre | Subproceso que tu agente lanza | Servicio remoto ya en marcha |
| Cómo se conecta | Por entrada y salida estándar | Por peticiones HTTP |
| Latencia | Mínima | La de la red |
| Quién lo usa | Un solo agente, en una máquina | Varios agentes y equipos a la vez |
| Cuándo conviene | Herramientas propias, sin red | Herramientas compartidas |
| Autenticación | La del proceso | La del servicio |

**Lo que debes observar en el laboratorio:** el código de tu agente es **idéntico** en los dos
casos. Solo cambia cómo se declara la conexión. El agente no sabe ni le importa por dónde viajan
los mensajes.

---

## 4. Conectar por stdio

El agente lanza `mcp_server.py` como subproceso.

```python
import asyncio
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient

from comun.provider import get_chat_model

async def main():
    cliente = MultiServerMCPClient({
        "simulador": {
            "transport": "stdio",
            "command": "python",
            "args": ["simulador-industria/mcp_server.py"],
        }
    })

    herramientas = await cliente.get_tools()
    print(f"Descubiertas {len(herramientas)} herramientas:")
    for h in herramientas:
        print(f"  · {h.name}")

    agente = create_agent(get_chat_model(), tools=herramientas)
    salida = await agente.ainvoke(
        {"messages": [HumanMessage(content="¿Hay cobertura en Los Olivos?")]}
    )
    print(salida["messages"][-1].content)

asyncio.run(main())
```

Ejecuta esto desde la **raíz del curso**, no desde `simulador-industria/`.

---

## 5. Conectar por HTTP

El mismo servidor, montado dentro del simulador desplegado.

```python
cliente = MultiServerMCPClient({
    "simulador": {
        "transport": "streamable_http",
        "url": f"{os.environ['SIM_BASE_URL']}/mcp",
    }
})
```

**Y nada más cambia.** `get_tools()`, `create_agent()` y la invocación son exactamente iguales.

Configúralo por `.env` para alternar sin tocar el código:

```dotenv
MCP_TRANSPORT=stdio          # stdio | http
MCP_HTTP_URL=https://<usuario>-simulador-industria.hf.space/mcp
MCP_STDIO_ARGS=simulador-industria/mcp_server.py
```

```python
from comun import settings as cfg

if cfg.MCP_TRANSPORT == "http":
    conexion = {"transport": "streamable_http", "url": cfg.MCP_HTTP_URL}
else:
    conexion = {"transport": "stdio", "command": cfg.MCP_STDIO_CMD,
                "args": cfg.MCP_STDIO_ARGS.split()}

cliente = MultiServerMCPClient({"simulador": conexion})
```

---

## 6. Combinar tus tools con las de MCP

Este es el escenario real: tu agente usa sus propias herramientas **y** las que descubre.

```python
from proyecto_final.app.tools.domain_tools import TOOLS_NUCLEO

herramientas_mcp = await cliente.get_tools()
agente = create_agent(get_chat_model(), tools=TOOLS_NUCLEO + herramientas_mcp)
```

⚠️ **Cuidado con la regla A1.** La precisión de selección cae pasadas 4 o 5 herramientas, y los
errores se multiplican a lo largo del bucle del agente. Si enlazas tus 4 tools núcleo **más** las 6 de MCP, tienes 10 y el
agente empezará a elegir mal.

Para el laboratorio, enlaza **las 4 tuyas más 1 o 2 de MCP**, no todas. Comprobar que la precisión
se degrada al agregar herramientas es, de hecho, parte del ejercicio.

---

## 7. Inspeccionar el servidor sin agente

Antes de conectar el agente, mira qué hay:

```python
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def inspeccionar():
    c = MultiServerMCPClient({"sim": {"transport": "stdio", "command": "python",
                                      "args": ["simulador-industria/mcp_server.py"]}})
    for h in await c.get_tools():
        print(f"\n=== {h.name} ===")
        print(h.description.strip()[:200])
        print("args:", list(h.args_schema.get("properties", {})))

asyncio.run(inspeccionar())
```

Esa descripción que ves es la misma que leerá el modelo para decidir. Compárala con las
docstrings de tus propias tools: **están escritas con la misma regla A2**, diciendo cuándo NO
usarlas.

---

## 8. Errores frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| `FileNotFoundError: mcp_server.py` | Ejecutas desde la carpeta equivocada | Lanza desde la raíz del curso |
| El subproceso muere al arrancar | Falta `mcp` instalado | `pip install mcp` |
| `get_tools()` devuelve lista vacía | El servidor no arrancó | Prueba `python simulador-industria/mcp_server.py` a mano |
| Timeout en transporte HTTP | El Space está dormido | Llama a `/health` primero |
| El agente elige mal la herramienta | Demasiadas tools enlazadas | Baja a 4-6 en total (regla A1) |
| `RuntimeError: no running event loop` | Llamaste a código async sin `asyncio.run` | MCP es asíncrono de punta a punta |

---

## 9. Qué debes entregar en el Laboratorio 4

- [ ] Tu agente funcionando con las 4 tools núcleo de tu track
- [ ] El mismo agente con 1 o 2 herramientas descubiertas por **MCP stdio**
- [ ] El mismo agente con esas herramientas por **MCP HTTP**
- [ ] Evidencia de que el código del agente **no cambió** entre los dos transportes
- [ ] Matriz consulta × herramienta esperada, con ≥ 85 % de acierto
- [ ] Un párrafo comparando los dos transportes: cuándo usarías cada uno

El último punto es el que se evalúa de verdad. Lo demás es la evidencia que lo sostiene.
