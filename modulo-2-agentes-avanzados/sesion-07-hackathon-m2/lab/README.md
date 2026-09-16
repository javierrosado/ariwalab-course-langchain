# Laboratorio L7 · Pruebas de estrés

**Objetivo:** encontrar y resolver al menos 10 casos borde de tu propio agente, y sustentarlo en
vivo. Es el **Proyecto M2** — ver [`../proyecto-m2.md`](../proyecto-m2.md) para el enunciado
completo, la rúbrica y la regla del piso.

---

## Antes de la clínica

- Tu agente (tools del L4 + RAG y memoria del L5 + guardrails del L6) debe correr de punta a
  punta. Si algo del L4-L6 quedó roto, arréglalo **antes** de hoy: la clínica mide robustez, no
  si el agente arranca.
- `CHAOS_RATE` lo activa el docente al empezar la clínica (`0.1`) y lo desactiva al terminar
  (`0.0`) — tú no tienes que tocar esa variable.

## La clínica: 45 min, 4 familias

Sigue el guion de `README.md` de la sesión, sección 2. Por cada familia, documenta el caso en tu
`INFORME-L7.md` (plantilla: [`plantilla-informe-l7.md`](plantilla-informe-l7.md)) con la traza
real — entrada y salida tal cual ocurrieron, no una paráfrasis.

## Ejemplos de arranque por track (para la familia 1, entrada ambigua)

| Track | Ejemplo de las "dos intenciones en un turno" |
|---|---|
| telecomunicaciones | *"Quiero saber cuánto he consumido y también reclamar porque se me cortó el internet"* |
| banca | *"Muéstrame mis movimientos y de paso dime si el último es sospechoso"* |
| retail | *"¿Dónde está mi pedido? Y si llegó dañado, quiero devolverlo ya"* |
| seguros | *"¿Mi SOAT está vigente? Choqué ayer y no sé si reportarlo"* |

Úsalos como punto de partida; la clínica pide que encuentres los tuyos propios también.

## Documento de diseño

[`plantilla-documento-diseno.md`](plantilla-documento-diseno.md) — 2-3 páginas, es el insumo del
Proyecto Integrador de la Sesión 11. Escríbelo pensando en reusarlo, no en entregarlo una vez.

## La demo

4-8 minutos según el tamaño del aula (ver `README.md`, sección 3). **Abre con el peor caso que
encontraste y resolviste**, no con el camino feliz.

---

## Entregables

| Entregable | Ruta |
|---|---|
| Demo en vivo | — |
| `INFORME-L7.md` con ≥ 10 casos borde | `lab/<tu-track>/INFORME-L7.md` |
| `tests/` con pruebas por invariantes | `lab/<tu-track>/tests/` |
| Documento de diseño | `lab/<tu-track>/documento-diseno.md` |

## Criterio de aceptación

Ver la rúbrica completa en `recursos/rubricas/rubrica-m2.md` y el enunciado en
[`../proyecto-m2.md`](../proyecto-m2.md).
