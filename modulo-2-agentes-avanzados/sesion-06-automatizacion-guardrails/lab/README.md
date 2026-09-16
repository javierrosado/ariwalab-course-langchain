# Laboratorio L6 · Guardrails y límites

**Objetivo:** que tu agente sea desplegable en una industria regulada.

**Duración:** 2 h.

---

## Parte 1 · `guardrails.py` (50 min guiados)

Escribe los 3 guardrails de la sesión (entrada, acción, salida — ver `code/01` a `03` como
punto de partida) más la lista de prohibidos de tu track (en tu enunciado). Engánchalos
alrededor de tu `agent.py` del L5, siguiendo el patrón de `code/04_middleware.py`: **no
reescribas la lógica interna del agente**, envuélvela.

## Parte 2 · Correr la batería (20 min)

```bash
python docente/verificar_guardrails.py --track <tu-track> --agente lab/<tu-track>/agent.py
```

El script te dice, por categoría, qué guardrail revisar si algo filtró. Corrige y vuelve a
correr hasta llegar a **0 filtraciones** sobre los 15 ataques del curso.

**Que un ataque pase en el primer intento es lo esperado, no un fracaso.** Un equipo con
15/15 sin fallar nunca probablemente no entendió los ataques.

## Parte 3 · Tus 5 ataques propios

Añade 5 ataques **nuevos** (no una variante léxica de los 15) a tu propio archivo
`recursos/ataques/bateria-<tu-track>-equipo.json`, con el mismo formato que
`recursos/ataques/bateria-<tu-track>.json` (`ataque`, `categoria`, `filtracion_si`). Corre de
nuevo `verificar_guardrails.py` sobre el archivo combinado.

## Parte 4 · Avance 3 del proyecto (10 min, en la sesión en vivo)

Prototipo funcional declarado: tools + RAG + memoria + guardrails, todo enganchado.

---

## Entregables

| Archivo | Qué contiene |
|---|---|
| `guardrails.py` | Los 3 guardrails + la lista de prohibidos del track |
| `agent.py` (v4) | El agente con el middleware enganchado |
| `recursos/ataques/bateria-<tu-track>-equipo.json` | Tus 5 ataques propios |
| `INFORME-L6.md` | Ver plantilla abajo |

### Plantilla de `INFORME-L6.md`

```markdown
# INFORME-L6 — Guardrails · [equipo] · [track]

## Resultado de la batería
- Ataques del curso (15): [N]/15 sin filtración en el primer intento
- Ataques propios (5): [N]/5 sin filtración

## Qué ataque pasó primero
[Cuál, de qué categoría, y la respuesta exacta que filtró algo]

## Qué se cambió
[El guardrail o la docstring que se corrigió]

## Escalamiento
[Qué condición lo dispara en tu track, y en qué ataque de la batería se activó]
```

---

## Criterio de aceptación

- **0 filtraciones** sobre los 15 ataques del curso.
- Los 5 ataques propios son genuinamente nuevos, no una variante léxica de los 15.
- Existe un camino de escalamiento a humano, y se dispara al menos una vez en la batería.

## Dónde mirar si te atoras

- [`../solucion/<tu-track>/`](../solucion/) — checkpoint de referencia.
- Tabla de errores esperables en el `README.md` de la sesión.
