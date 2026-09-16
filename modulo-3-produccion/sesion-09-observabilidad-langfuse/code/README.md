# Demos de la Sesión 9

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python modulo-3-produccion/sesion-09-observabilidad-langfuse/code/01_traza_minima.py` | `HF_TOKEN` + Langfuse | El callback puesto y una traza apareciendo en el dashboard en vivo |
| 2 | `python modulo-3-produccion/sesion-09-observabilidad-langfuse/code/02_anatomia_spans.py` | `HF_TOKEN` + Qdrant + Langfuse | Un run con tool + retriever, y los spans que produce |
| 3 | `python modulo-3-produccion/sesion-09-observabilidad-langfuse/code/03_pii_en_traza.py` | No | La misma consulta con y sin el enmascarador: lo que Langfuse llega a almacenar |

La demo 3 se corre **antes** de que instrumentes tu propio agente (parte 1 del lab). Ver el DNI
completo dentro de una traza de un servicio ajeno es más convincente que cualquier explicación.

## Qué deberías notar en cada una

**Demo 1 — Traza mínima.** Que "ver que funcionó" hoy significa abrir un dashboard, no leer la
consola. Es un cambio de hábito, no solo de herramienta.

**Demo 2 — Anatomía de spans.** Suma cuánto tiempo se llevó el modelo contra el resto de la
traza. La respuesta, casi siempre, es "la mayoría": el cuello no son las tools ni Qdrant.

**Demo 3 — PII en traza.** El costo real de enmascarar: ya no puedes ver el dato completo ni tú
mismo depurando. Es el precio correcto a pagar.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `RuntimeError: Falta la variable LANGFUSE_PUBLIC_KEY` | Falta configurar Langfuse en `.env` | Revisa `.env.example` y tu proyecto en cloud.langfuse.com |
| No aparece ningún trace nuevo | El proyecto de Langfuse del `.env` no es el que estás mirando en el dashboard | Verifica que las claves correspondan al mismo proyecto |
| Las demos 1 y 2 tardan | Cola del *inference provider* | Normal, no es un error de tu código |
