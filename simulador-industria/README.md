# Simulador de Industria

Servicio que simula **cuatro empresas peruanas ficticias** y sirve de base para todos los
laboratorios del curso. Los alumnos no construyen el simulador: construyen el **agente** que se
integra contra él.

```
              SIMULADOR DE INDUSTRIA          ← infraestructura del curso
       (SQLite cargado desde los datasets)       lo despliega el docente
                       │
    ┌──────────────────┼──────────────────┐
    ▼                  ▼                  ▼
 API REST         Base de datos      Servidor MCP
 servicios de     datos              capacidades
 terceros         transaccionales    reutilizables
    │                  │                  │
    └──────────────────┼──────────────────┘
                       ▼
             comun/datos.py  ← adaptadores
                       │
                domain_tools.py
                       │
             EL AGENTE DEL ALUMNO            ← esto es lo que él construye
```

---

## Documentación

| Documento | Para quién | Qué contiene |
|-----------|-----------|--------------|
| [`docs/GUIA-ALUMNO.md`](docs/GUIA-ALUMNO.md) | **Alumnos** | Cómo conectar tu agente, manejo de errores, provocar fallos |
| [`docs/REFERENCIA-API.md`](docs/REFERENCIA-API.md) | **Alumnos y docente** | Las 18 rutas con peticiones y respuestas reales |
| [`docs/GUIA-MCP.md`](docs/GUIA-MCP.md) | **Alumnos** | Transportes stdio y HTTP, código de conexión |
| [`docs/GUIA-DOCENTE.md`](docs/GUIA-DOCENTE.md) | **Docente** | Despliegue, API keys, operación en clase, diagnóstico |
| Este archivo | Quien mantenga el código | Arquitectura interna |

---

## Arranque rápido

```bash
cd simulador-industria
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

```bash
curl -H "X-API-Key: demo-key-0000" http://localhost:8000/telco/clientes/988837195
```

Documentación interactiva en `http://localhost:8000/docs`.

---

## Las cuatro industrias

| Prefijo | Empresa ficticia | Dominio |
|---------|------------------|---------|
| `/telco` | AndesMóvil | Atención al cliente móvil postpago |
| `/banca` | Banco Inti | Banca personal y detección de operación sospechosa |
| `/retail` | MercaSur | Post-venta de e-commerce |
| `/seguros` | Andina Seguros | SOAT y siniestros vehiculares |

Todos los datos son sintéticos y todas las empresas son ficticias (decisión D12).

---

## Las tres superficies

El mismo dominio, expuesto de tres formas. La redundancia es deliberada: es lo que permite
enseñar que **la fuente de datos cambia y la tool no**.

| Superficie | Cómo se accede | Laboratorio |
|------------|----------------|-------------|
| **REST** | `GET /telco/clientes/{linea}` con `X-API-Key` | L3 |
| **SQL** | SQLite interno, consultado por las rutas REST | L6 opcional |
| **MCP stdio** | `python mcp_server.py` como subproceso | L4 |
| **MCP HTTP** | `POST /mcp` | L4 |

---

## Arquitectura interna

| Archivo | Responsabilidad |
|---------|-----------------|
| `app.py` | Aplicación FastAPI; monta routers y MCP HTTP |
| `db.py` | Carga los CSV en SQLite y aísla escrituras por equipo |
| `auth.py` | Valida `X-API-Key` y resuelve el equipo |
| `chaos.py` | Provoca los 6 fallos simulables |
| `routers.py` | Las 18 rutas de las 4 industrias, en paralelo |
| `mcp_server.py` | Servidor MCP, transportes stdio y HTTP |
| `equipos.json` | Mapa de API keys a equipos |
| `verificar_simulador.py` | 33 comprobaciones, sin credenciales externas |
| `generar_referencia_api.py` | Regenera `docs/REFERENCIA-API.md` desde el código |

### Decisiones de diseño

**Un solo servicio para las 4 industrias** (D22). Un despliegue, un mantenimiento, una guía.

**SQLite reconstruido en cada arranque** (D24). El simulador vuelve a un estado conocido al
reiniciarse y los datos base nunca se corrompen. Las escrituras de los equipos se pierden en un
reinicio, y ningún laboratorio depende de datos creados en la sesión anterior.

**Aislamiento por equipo.** Los datos base son compartidos y de solo lectura; lo que cada equipo
crea queda en su propio espacio, con su propia numeración correlativa. Sin esto, 15 equipos
compartiendo un simulador se pisan desde el primer laboratorio.

**El simulador no expone PII.** `/banca/cuentas` y `/seguros/polizas` eliminan el DNI antes de
responder; las tarjetas solo devuelven los últimos 4 dígitos. La fuente ya viene saneada, así
que los guardrails del L6 no parten de cero.

---

## Verificación

```bash
PYTHONPATH=. python verificar_simulador.py
```

33 comprobaciones contra los datasets reales: rutas de las 4 industrias, autenticación,
aislamiento por equipo, no exposición de PII y simulación de fallos. No requiere red ni
credenciales de ningún servicio externo. Sale con código `1` si algo falla.

```bash
PYTHONPATH=. python generar_referencia_api.py
```

Regenera `docs/REFERENCIA-API.md` ejecutando el simulador de verdad. **Ejecútalo después de
cualquier cambio en las rutas**, o la referencia queda desactualizada sin que nadie lo note.

---

## Variables de entorno

| Variable | Por defecto | Para qué |
|----------|-------------|----------|
| `DATASETS_DIR` | `../recursos/datasets` | Dónde están los CSV semilla |
| `DB_PATH` | `/tmp/simulador.db` | Archivo SQLite |
| `EQUIPOS_FILE` | `./equipos.json` | Mapa de API keys a equipos |
| `CHAOS_RATE` | `0.0` | Probabilidad de fallo espontáneo |
| `HABILITAR_MCP_HTTP` | `1` | Monta o no el endpoint `/mcp` |

---

## Despliegue

Ver [`docs/GUIA-DOCENTE.md`](docs/GUIA-DOCENTE.md) §2. El `Dockerfile` espera el contexto en la
**raíz del curso**, no en esta carpeta, porque la imagen necesita copiar también
`recursos/datasets/`.
