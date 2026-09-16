# L5 · Retail — MercaSur

Sigue las 5 partes de [`../README.md`](../README.md). Tu corpus son los 3 `.md` de
`recursos/datasets/retail/`: `politica_devoluciones.md`, `terminos_garantia.md`, `faq_despacho.md`.
`chunk_size=350`, `overlap=50` (el más chico del curso: fichas y políticas muy breves).

Tu retriever debe decir en la docstring que es para política de devoluciones, garantía y
condiciones de despacho — **no** para estado de pedido, ficha de producto, stock o una devolución
ya iniciada (eso lo resuelven tus tools del L4).

Referencia: `solucion/retail/`.
