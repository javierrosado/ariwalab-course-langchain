# Demos de la Sesión 0

Cuatro experimentos para **ver** el comportamiento del que habla la teoría. No hay que escribir
código: se ejecutan y se observa la salida.

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|---------------|
| 1 | `python 00-preparacion/code/01_tokens.py` | No | El español cuesta más tokens que el inglés |
| 2 | `python 00-preparacion/code/02_temperatura.py` | `HF_TOKEN` | La misma pregunta da respuestas distintas |
| 3 | `python 00-preparacion/code/03_embeddings.py` | `HF_TOKEN` | Se puede buscar por significado, no por palabras |
| 4 | `python 00-preparacion/code/04_costo.py` | No | El historial es lo caro, no la última pregunta |

## Antes de empezar

```powershell
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
```

La demo 1 muestra la tokenización real si tienes `transformers` instalado; si no, cae a una
estimación por caracteres y lo advierte. Para ver los tokens reales:

```powershell
pip install transformers
```

La demo 4 es una simulación aritmética: no llama a ningún servicio y por eso no gasta cuota.

## Qué deberías notar en cada una

**Demo 1 — Tokenización.** Que `portabilidad` no es un token sino varios, y que el mismo
significado cuesta entre 20 % y 40 % más en español. Como el costo, el límite de contexto y la
latencia se miden en tokens, un curso en español opera con menos margen.

**Demo 2 — Temperatura.** Que a `temperature=0` las tres ejecuciones se parecen mucho y a `1.5`
divergen. Y que ni siquiera a 0 son necesariamente idénticas: por eso la sesión 10 evalúa con
métricas y no con `assert`.

**Demo 3 — Embeddings.** Fíjate en la columna *palabras comunes*: la frase más parecida a la
consulta comparte casi ninguna palabra con ella. Eso es lo que una búsqueda con `LIKE` jamás
podría encontrar, y es la razón de existir del RAG.

**Demo 4 — Costo.** Que la entrada crece turno a turno aunque el usuario escriba siempre lo
mismo, y que las cuatro palancas de optimización atacan la entrada. Optimizar la salida es lo
primero que intenta todo el mundo y lo que menos rinde.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta desde la raíz del curso |
| `ModuleNotFoundError: langchain` | El `venv` no está activado | Actívalo; el prompt debe mostrar `(.venv)` |
| `401 Unauthorized` | Token sin permiso de inferencia | Regenera el token con ese permiso |
| La demo 2 tarda mucho la primera vez | Arranque en frío del endpoint | Es normal; reintenta a los 2 minutos |
| Acentos rotos en Windows | Codificación de la consola | `chcp 65001` antes de ejecutar |
