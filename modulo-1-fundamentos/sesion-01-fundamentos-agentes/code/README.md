# Demos de la Sesión 1

Tres scripts que se ejecutan en vivo durante el bloque 6 del guion (`comun/provider.py` en
vivo). Ninguno necesita Qdrant, Langfuse ni el simulador — solo `HF_TOKEN`.

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Qué demuestra |
|------|---------|----------------|
| 1 | `python modulo-1-fundamentos/sesion-01-fundamentos-agentes/code/01_primer_llamado.py` | `describe_provider()` + un llamado real vía `comun/provider.py` |
| 2 | `python modulo-1-fundamentos/sesion-01-fundamentos-agentes/code/02_tipos_de_mensaje.py` | El mismo `human` con y sin `system` |
| 3 | `python modulo-1-fundamentos/sesion-01-fundamentos-agentes/code/03_un_modelo_cuatro_industrias.py` | La misma pregunta contra los 4 `get_system_prompt(track)` |

## Antes de empezar

```powershell
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
```

Necesitas `HF_TOKEN` válido en tu `.env` (lo configuraste en la Sesión 0). Nada más.

## Qué deberías notar en cada una

**Demo 1 — Primer llamado.** Que ningún archivo del curso instancia `ChatOpenAI` directamente:
todo pasa por `comun/provider.py`. Ese es el punto de partida de tu propio `primer_contacto.py`
en el laboratorio de hoy.

**Demo 2 — Tipos de mensaje.** Que el `system` cambia el tono y los límites de la respuesta sin
que la pregunta del cliente (`human`) haya cambiado una sola palabra. Este es el mecanismo exacto
que usa `comun/prompts_industria.py` para "personalizar" el agente por industria.

**Demo 3 — Un modelo, cuatro industrias.** Que **un solo modelo** puede sonar a telco, a banco, a
retailer o a aseguradora según el `system` que reciba. Es la decisión D21 (camino A, sin
fine-tuning) en vivo: la personalización vive en texto editable, no en los pesos del modelo.

## Sustitución respecto del repo de Microsoft

El mapeo original asignaba aquí `01-introduction/code/03_model_comparison.py`, que compara
modelos distintos entre sí. Con la decisión D28 este curso usa **un solo modelo**
(`Qwen/Qwen3-32B`), así que esa comparación perdería sentido: se reemplaza por la comparación de
**prompts de industria**, que enseña la decisión que sí gobierna el curso.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `ModuleNotFoundError: langchain` | El `venv` no está activado | Actívalo; el prompt debe mostrar `(.venv)` |
| `401 Unauthorized` | Token sin permiso de inferencia | Regenera el token de Hugging Face con ese permiso |
| El modelo responde en inglés | Falta el `system` en español | Es justo lo que enseña la demo 2: compáralo con la versión sin `system` |
| El modelo tarda ~20 s | Cola del *inference provider* | Es normal; no es un error de tu código |
| Acentos rotos en Windows | Codificación de la consola | `chcp 65001` antes de ejecutar |
