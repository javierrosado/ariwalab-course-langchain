# Pre-work · MCP — conectarse, no construir

> 1 hora: 15 min + 15 min de lectura, 30 min de práctica. **Decisión del curso:** el simulador ya
> expone 6 tools por MCP, documentadas y con los dos transportes funcionando. Construir un
> servidor MCP propio no cabe en 1 hora para quien escribió su primera tool hace dos días — y la
> lección central de MCP se aprende igual conectándose: **el agente no nota la diferencia**,
> mismas tools, distinto transporte. Construir tu propio servidor con 2 tools queda como **reto
> opcional del L4**, no como requisito de hoy.

---

## 1. Qué es MCP y qué problema resuelve · 15 min

MCP (Model Context Protocol) es un **protocolo**, no una librería: un formato estándar para que
un cliente (tu agente) descubra y llame herramientas expuestas por un servidor, sin que el
cliente necesite conocer cómo están implementadas. La ventaja frente a escribir `@tool` a mano:
el mismo servidor MCP puede servir a cualquier agente compatible, y el mismo agente puede
conectarse a cualquier servidor MCP, sin reescribir nada — es la misma idea de indirección que ya
viste en `comun/provider.py` (D13), aplicada a herramientas en vez de a modelos.

## 2. Los dos transportes · 15 min

Lee `simulador-industria/docs/GUIA-MCP.md` completo. Quédate con esto:

| Transporte | Cuándo se usa | Cómo se conecta |
|---|---|---|
| **stdio** | Desarrollo local: tu agente lanza el servidor como subproceso | `command="python", args=["simulador-industria/mcp_server.py"]` |
| **streamable_http** | El simulador ya desplegado en HF Spaces | `url=f"{SIM_BASE_URL}/mcp"` |

El resto del código — `get_tools()`, enlazar las tools al modelo, invocar el agente — es
**idéntico** entre los dos transportes. Esa es la lección: MCP separa "cómo hablo con el
servidor" de "qué hace mi agente con las tools", igual que `provider.py` separa "qué modelo uso"
de "qué hace mi agente con el modelo".

## 3. Conectar tu agente · 30 min de práctica

```python
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from comun import settings as cfg

async def main():
    if cfg.MCP_TRANSPORT == "http":
        conexion = {"transport": "streamable_http", "url": cfg.MCP_HTTP_URL}
    else:
        conexion = {"transport": "stdio", "command": cfg.MCP_STDIO_CMD,
                    "args": cfg.MCP_STDIO_ARGS.split()}

    cliente = MultiServerMCPClient({"simulador": conexion})
    herramientas = await cliente.get_tools()

    for h in herramientas:
        print(f"- {h.name}: {h.description}")

asyncio.run(main())
```

Ejecuta esto **desde la raíz del curso** (no desde `simulador-industria/`) con
`MCP_TRANSPORT=stdio` en tu `.env` (el valor por defecto). Deberías ver listadas las 6 tools:
`check_portability_eligibility`, `get_coverage_by_district`, `get_transfer_limits`,
`estimate_delivery`, `list_affiliated_clinics`, `get_vehicle_info`.

**Con qué te quedas:** solo 2 de esas 6 tools son de tu track — las otras 4 son de las otras
industrias. Parte de "conectarte, no construir" es también **filtrar**: tu agente no debería
enlazar las 6, solo las tuyas (regla A1: máximo 4-6 tools en total contando las de MCP).

---

## Antes de la sesión en vivo

- [ ] Ejecutaste el script de arriba y viste las 6 tools listadas.
- [ ] Identificaste cuáles 2 son de tu track.
- [ ] Instalaste `langchain-mcp-adapters` (`pip install -r requirements.txt` ya lo incluye).

## Si algo falla

| Error | Causa | Solución |
|---|---|---|
| `FileNotFoundError` al lanzar el subproceso | Ejecutas desde `simulador-industria/`, no desde la raíz | Ejecuta desde la raíz del curso |
| Lista de tools vacía | El servidor no llegó a arrancar | Revisa que `mcp` esté instalado (`pip show mcp`) |
| Timeout con `MCP_TRANSPORT=http` | El Space está dormido (free tier) | Prueba primero `GET /health`; reintenta en 1-2 min |
| El agente elige mal entre 6+ tools | Demasiadas tools enlazadas a la vez | Filtra: enlaza solo las 2 de tu track + tus 4 núcleo |
