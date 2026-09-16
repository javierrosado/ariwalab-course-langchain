# L5 · Seguros — Andina Seguros

Sigue las 5 partes de [`../README.md`](../README.md). Tu corpus son los 3 `.md` de
`recursos/datasets/seguros/`: `condicionado_soat.md`, `procedimiento_siniestro.md`,
`tabla_coberturas.md`. `chunk_size=600`, `overlap=100` (el más grande del curso: una cláusula
partida por la mitad pierde su sentido legal).

Tu retriever debe decir en la docstring que es para coberturas, exclusiones y procedimiento de
siniestro — **no** para vigencia de póliza, cotización, estado de un expediente concreto o apertura
de un siniestro (eso lo resuelven tus tools del L4). Toda cifra de cobertura debe citar el
condicionado: es la salvaguarda A6 aplicada a tu track más estricta.

Referencia: `solucion/seguros/`.
