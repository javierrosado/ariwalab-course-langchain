# Design System AriwaLabs — PPTX editable

## Identidad visual

- Formato 16:9, lienzo 1600 × 900; todos los objetos conservan geometría editable.
- Fondo #F4F6F8; estructura y texto principal #1E293B; contenedores #FFFFFF; foco #FF5733.
- Apoyos: azul claro #E9F0F7, coral claro #FFF0EB, texto secundario #526277 y bordes #CED8E3.
- DejaVu Sans: título 37 px, cuerpos principales 25–28 px, tablas 25 px, notas visuales 17–23 px.
- Contenedores redondeados, líneas visibles, sin fotografías, robots decorativos, gradientes ni sombras pesadas.

## Gramática

Cabecera: sesión, capítulo y título. Indicador de progreso: concepto / desarrollo / ejemplo. Pie: mensaje central y número local de diapositiva.

Las arquitecturas usan objetos nativos unidos mediante conectores. LLM nombra al modelo; Agente a la coordinación; Tool a la capacidad ejecutada por código; Memoria al contexto administrado por la aplicación; Retriever/RAG a la recuperación documental; API a una frontera de servicio; Qdrant a la base vectorial; Guardrail/Control a un punto que limita entrada, acción o salida. Observabilidad registra el recorrido. El color coral destaca control o el paso focal, sin representar por sí solo éxito o error.

Los cuadros comparativos usan tablas nativas. Los ejemplos avanzan por tres pasos y terminan en un resultado esperado. Las flechas deben conservar la dirección conceptual al editar o mover objetos.

## Reutilización

La identidad de cada componente permanece a través de las sesiones. Se reutiliza la arquitectura para explicar responsabilidades diferentes, sin afirmar que todas están implementadas en el primer laboratorio. El diseño diferencia memoria en proceso de persistencia duradera, dato consultado de texto generado y un aviso de derivación de una integración real con un asesor.
