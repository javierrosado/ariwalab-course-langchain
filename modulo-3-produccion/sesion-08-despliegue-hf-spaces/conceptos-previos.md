# Conceptos previos — Sesión 8

> Pre-work de 1 h. Tráelo resuelto: la sesión en vivo lo asume leído.

---

## 1. 12-Factor App: config por entorno

Un principio de la metodología [12-Factor](https://12factor.net/es/config): la configuración
(credenciales, URLs, nombres de recursos) vive en variables de entorno, nunca en el código
fuente. Es exactamente lo que `comun/settings.py` hace desde el L1 — hoy entiendes **por qué**
se diseñó así: es lo que permite que el mismo código corra en tu laptop y en el Space sin tocar
una línea.

## 2. Contenedores: imagen, capa, `Dockerfile`

Un contenedor empaqueta tu código + sus dependencias + el sistema mínimo para correrlas, en una
unidad portable. El `Dockerfile` es la receta:

| Instrucción | Qué hace |
|---|---|
| `FROM` | La imagen base (ej. `python:3.11-slim`) |
| `COPY` | Copia archivos del repo a la imagen |
| `RUN` | Ejecuta un comando **al construir** la imagen (ej. `pip install`) |
| `EXPOSE` | Documenta qué puerto escucha el contenedor |
| `CMD` | El comando que arranca **al correr** el contenedor |

No necesitas tener Docker instalado para esta sesión (P2): lo escribes, la plataforma lo
construye.

## 3. FastAPI: rutas, Pydantic, ASGI

FastAPI define rutas con decoradores (`@app.get`, `@app.post`), valida el cuerpo de la petición
con modelos Pydantic (lo mismo que ya usaste en `comun/structured.py`, regla A3), y corre sobre
ASGI (el protocolo asíncrono que sucede a WSGI) vía `uvicorn`. Es la decisión D08 del curso.

## 4. Health check: por qué una plataforma lo exige

Una plataforma de hosting no puede adivinar si tu proceso "está bien": necesita un endpoint que
responda rápido y sin dependencias externas. `/health` es ese endpoint — HF Spaces (como
cualquier orquestador) lo consulta periódicamente para decidir si el Space sigue vivo o hay que
reiniciarlo.

## 5. *Space secrets* vs `.env` local

Un *Space secret* es una variable de entorno que la plataforma inyecta al contenedor en
tiempo de ejecución, sin que quede en ningún archivo del repo. Es el equivalente en la nube de tu
`.env` local — mismo propósito (credenciales fuera del código), mecanismo distinto.

## 6. `git push` a un remote que no es GitHub

HF Spaces se despliega con `git push` a un remote propio del Space (no tu repositorio de
GitHub). Puedes tener ambos remotes en el mismo repo local:

```bash
git remote add space https://huggingface.co/spaces/<usuario>/<nombre-del-space>
git push space main
```

---

## Verificación de entrada

Antes de la sesión, confirma:

```bash
git remote -v          # debe listar tu remote "space" (o el nombre que le hayas dado)
```

Si no tienes un Space vacío creado todavía, créalo desde huggingface.co/new-space (SDK: Docker)
antes de la clase — la sesión asume que ese paso ya está hecho.
