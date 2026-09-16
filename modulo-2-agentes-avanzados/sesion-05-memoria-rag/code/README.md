# Demos de la Sesión 5

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado, y **en orden**:
las demos 2, 3, 4 y la demo clave reutilizan la colección que crea la demo 1.

| Demo | Comando | Qué demuestra |
|------|---------|----------------|
| 1 | `python .../code/01_ingesta.py` | Carga, chunking, embeddings e indexación en Qdrant |
| 2 | `python .../code/02_similitud.py` | Las preguntas del track contra la colección, con su puntaje |
| 3 | `python .../code/03_rag_tradicional.py` | Buscar siempre y pegar el contexto |
| 4 | `python .../code/04_rag_agentico.py` | El retriever como tool: el agente decide si buscar |
| **clave** | `python .../code/demo-parametrico-vs-recuperable.py` | **La demo del curso**: por qué el conocimiento va al RAG y no al fine-tuning |

Todas usan la implementación de referencia del docente (track telecomunicaciones, colección
`kb-telecomunicaciones-demo`, separada de la de tu laboratorio) y requieren `HF_TOKEN`,
`QDRANT_URL` y `QDRANT_API_KEY` en el `.env`.

## Antes de empezar

```bash
python -m comun.check_stack
```

Comprobaciones 6 (Embeddings) y 7 (Qdrant) en verde. Si Qdrant falla, no corras estas demos:
usa la colección de respaldo (`kb-<track>-respaldo`) solo para el laboratorio, no para estas
demos de docente.

## Qué deberías notar en cada una

**Demo 1 — Ingesta.** El número de chunks es mayor al número de documentos: un `.md` de pocas
líneas puede seguir produciendo 3-4 chunks si su `chunk_size` es pequeño.

**Demo 2 — Similitud.** La columna "palabras comunes" suele ser baja incluso en los mejores
resultados — el buscador encuentra significado, no coincidencia de texto.

**Demo 3 — RAG tradicional.** Que "hola, buenos días" también dispara una búsqueda en Qdrant:
el patrón tradicional no decide, siempre busca.

**Demo 4 — RAG agéntico.** Que la misma pregunta de saludo, aquí, **no** dispara la búsqueda: el
agente decidió que no la necesitaba. Compáralo directamente con la demo 3.

**Demo clave — Paramétrico vs recuperable.** El precio cambia con solo editar un documento. La
pregunta que cierra la demo (¿qué habría hecho falta si el precio estuviera en los pesos del
modelo?) es la que hay que dejar resonando en el aula.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ResponseHandlingException` / `getaddrinfo failed` | `QDRANT_URL` no resuelve | Verifica que el cluster exista y esté *Healthy* en cloud.qdrant.io |
| La demo 2, 3 o 4 no encuentran nada | No corriste la demo 1 primero | Corre `01_ingesta.py` antes |
| `401` de Hugging Face | Token sin permiso de inferencia | Regenera el token |
| La ingesta tarda o falla a mitad | Cuota de embeddings agotada | Usa la colección de respaldo y reintenta más tarde |
