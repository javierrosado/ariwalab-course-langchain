# Modelo y personalización por industria

Los cuatro tracks usan el modelo de chat configurado en `HF_CHAT_MODEL`, a través de
`comun/provider.py`. La configuración de referencia usa `Qwen/Qwen3-32B`.
Antes de clase, comprobar llamadas a herramientas y salida estructurada con la
[guía de verificación](../VERIFICACION.md).

## Qué cambia entre industrias

| Pieza | Ubicación | Uso en clase |
|---|---|---|
| Identidad, vocabulario y límites | `comun/prompts_industria.py` | Comparar cómo cambia el comportamiento al cambiar `COURSE_TRACK` |
| Datos transaccionales | `recursos/datasets/<track>/` y simulador | Consultar herramientas desde L3 |
| Tarifas, coberturas y políticas | Documentos del track indexados en Qdrant | Recuperar y citar desde L5 |

El conocimiento actualizado se recupera mediante RAG; el curso no entrena los pesos del
modelo. La temperatura baja reduce variación, pero no garantiza respuestas idénticas.
Un prompt describe límites de actuación; los controles de la aplicación deben verificarlos.

## Secuencia para el docente

1. En S1, ejecutar la demo de un modelo con cuatro system prompts.
2. En S2, validar la estructura de las respuestas con Pydantic y medir el clasificador.
3. En S3–S4, medir selección y ejecución de herramientas por separado.
4. En S5, comparar una respuesta sin recuperación con otra respaldada por documentos.
5. En S6, probar los controles con la batería de ataques y explicar su cobertura limitada.
6. En S10, evaluar las respuestas y revisar manualmente sus fuentes.

## Preparación del bonus

El cliente de chat puede cambiar de proveedor; los embeddings y el hosting requieren
comprobaciones adicionales. Indexación y consulta deben usar el mismo modelo de embeddings.
Si se cambia, crear una colección compatible y reindexar. El host de ejemplo requiere adaptar
memoria y guardrails antes de compararlo con el agente completo.
