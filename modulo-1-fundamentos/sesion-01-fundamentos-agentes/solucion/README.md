# Solución de referencia · L1

Checkpoint de recuperación (invariante I5 de `docente/labs-incrementales.md`): con 4 tracks
avanzando en paralelo, el docente no puede rescatar en vivo a un equipo atrasado. Si tu equipo
se atasca, compara tu script contra el de tu track — **después** de intentarlo, no antes.

| Track | Referencia |
|---|---|
| Telecomunicaciones — AndesMóvil | [`telecomunicaciones/primer_contacto.py`](telecomunicaciones/primer_contacto.py) |
| Banca — Banco Inti | [`banca/primer_contacto.py`](banca/primer_contacto.py) |
| Retail — MercaSur | [`retail/primer_contacto.py`](retail/primer_contacto.py) |
| Seguros — Andina Seguros | [`seguros/primer_contacto.py`](seguros/primer_contacto.py) |

Los 4 scripts comparten el mismo esqueleto (invariante I4): cambian la lista de preguntas y el
track. Ninguno usa Pydantic, tools ni `create_agent()` — eso sale del alcance del L1
(ver `README.md` de la sesión, sección 11).
