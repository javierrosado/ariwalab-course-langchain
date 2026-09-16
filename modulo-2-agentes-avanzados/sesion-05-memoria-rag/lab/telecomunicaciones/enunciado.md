# L5 · Telecomunicaciones — AndesMóvil

Sigue las 5 partes de [`../README.md`](../README.md). Tu corpus son los 3 `.md` de
`recursos/datasets/telecomunicaciones/`: `tarifario_planes.md`, `condiciones_portabilidad.md`,
`reglamento_reclamos.md`. `chunk_size=400`, `overlap=60` (ver `README.md` de la sesión, sección 3).

Tu retriever se llama `retrieve_knowledge_base` y debe decir en la docstring que es para tarifas,
portabilidad y reclamos — **no** para plan, consumo, diagnóstico o reclamos ya registrados (eso
lo resuelven tus tools del L4).

Referencia: `solucion/telecomunicaciones/`.
