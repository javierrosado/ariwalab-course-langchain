# Design System AriwaLabs

## Formato y estilo

Lienzo 16:9, objetivo 1536 × 864 o equivalente. PNG para README y PowerPoint.
Fondo `#F4F6F8`, texto/estructura `#1E293B`, tarjetas `#FFFFFF`, acento `#FF5733`.
Ilustración técnica de aspecto vectorial, flat, bordes redondeados, flechas claras y amplio
espacio entre componentes. Sin fotografías, robots humanoides, 3D, sombras pesadas,
gradientes complejos ni párrafos dentro de la imagen.

Título dominante, etiquetas breves y texto legible proyectado. Acento para el mecanismo
que se está explicando; no codificar diferencias únicamente con color. Flecha sólida para
flujo de ejecución/datos; discontinua para contexto, control o telemetría; etiquetar ambas.
No dibujar una flecha desde el modelo hacia la API que omita el runtime ejecutor.

## Vocabulario visual canónico

| Elemento | Representación | Regla semántica |
|---|---|---|
| User | Persona lineal con etiqueta | Inicia consultas; no es el proceso agente |
| LLM | Tarjeta con chip y etiqueta LLM | Propone respuesta o acción |
| Agent | Contenedor que engloba modelo, runtime y bucle | No confundir contenedor con chip |
| Tool | Tarjeta con llave inglesa | La ejecuta el runtime, no el LLM |
| Memory | Tarjetas apiladas con historial | Historial de conversación, distinto del corpus |
| RAG | Documentos → recuperación → contexto | Separar ingesta de consulta |
| MCP | Conector etiquetado cliente/servidor | Protocolo; no una nueva fuente de datos por sí solo |
| Middleware | Banda de intercepción | Distinguir patrón manual de API nativa |
| Guardrail | Escudo abierto con condición | Cobertura limitada; no prometer garantía universal |
| Human Approval | Persona y punto de decisión | No representarla como implementada donde solo hay un booleano |
| API | Tarjeta con extremos de conexión | Frontera del servicio |
| Database | Cilindro | Almacén de datos estructurados |
| External System | Rectángulo fuera del contenedor | Sistema externo al agente |
| Vector Database | Cilindro con puntos | Vectores y payload; mismo espacio de embeddings |
| Observability | Árbol de spans y reloj | Telemetría separada del flujo de respuesta |
| Evaluation | Tabla de casos y marca de comparación | Medición; no mostrar cifras inventadas |

## Reutilización y niveles

L1 explica el concepto; L2 muestra el mecanismo; L3 lo aplica a una industria. No se requieren
los tres niveles para cada tema. El catálogo prioriza seis diagramas que pueden reutilizarse
en distintas sesiones, con speaker notes específicos y progresivos. La reutilización conserva
la misma composición: el docente señala el componente correspondiente, sin inventar conexiones.

Las marcas de industria se introducen verbalmente cuando no ayudan a la arquitectura visual.
AndesMóvil, Banco Inti, MercaSur y Andina Seguros tienen igual jerarquía y no usan logos reales.

## Producción y aceptación

Cada imagen tiene prompt completo, ID, fuente, objetivo, ruta y notas. GENERADO/GENERATED
solo se asigna después de verificar que el archivo existe y revisar visualmente texto,
flechas, mecanismo, legibilidad, formato y correspondencia con la fuente. Si la herramienta
falla, conservar `PENDING_GENERATION`; no crear un placeholder presentado como final.
La generación es estocástica: “reproducible” significa especificación y prompt conservados,
no igualdad de píxeles entre corridas. Reutilizar el PNG aprobado siempre que sirva.
