# Laboratorio L2 · Clasificador de intención

**Objetivo:** convertir texto libre del cliente en estructura tipada y **medir** el acierto —no
opinar sobre él.

**Duración:** 2 h. **No llama a ninguna API ni al simulador**: entra texto, sale estructura.

> Si no entregaste el pase de entrada de Pydantic (el ejercicio `Reclamo`), dedica esta hora a
> resolverlo con el checkpoint de la Sesión 1, y retoma el L2 con el checkpoint de la solución.

---

## Taxonomía de tu track — alineada 1:1 con las tools del L4

Tu Enum `categoria` tiene exactamente estas 5 categorías (la 5.ª, `OTRO`, es la que en la
Sesión 5 dispara el RAG — no es un cajón de sastre, es una categoría con destino propio):

| Track | Categorías |
|---|---|
| telecomunicaciones | `CONSULTA_PLAN` · `CONSULTA_CONSUMO` · `AVERIA` · `RECLAMO` · `OTRO` |
| banca | `CONSULTA_SALDO` · `CONSULTA_MOVIMIENTOS` · `CONSULTA_TARJETA` · `SOSPECHA_FRAUDE` · `OTRO` |
| retail | `SEGUIMIENTO_PEDIDO` · `CONSULTA_PRODUCTO` · `CONSULTA_STOCK` · `DEVOLUCION` · `OTRO` |
| seguros | `CONSULTA_POLIZA` · `COTIZACION` · `ESTADO_SINIESTRO` · `REPORTE_SINIESTRO` · `OTRO` |

**Por qué 1:1.** En el L4 no vas a reclasificar nada: la categoría que hoy aprendes a producir
**es** la herramienta que en el L4 tu agente debe elegir. `CONSULTA_PLAN` de hoy es
`get_customer_plan` del L4. La progresión deja de ser temática y pasa a ser mecánica.

---

## Parte 1 · `schemas.py` y `prompts.py` (guiado, ~15 min)

En `solucion/<tu-track>/` tienes la referencia. Tu propia versión va en tu proyecto:

- `schemas.py`: la clase `Intencion` (categoria + urgencia + entidades) y el Enum de tu track.
- `prompts.py`: la plantilla Rol+Contexto+Tarea+Formato + 2 ejemplos few-shot (regla A5).

## Parte 2 · `clasificar.py` (20 min)

Usa **obligatoriamente** `extraer()` de `comun/structured.py`. **Prohibido**
`with_structured_output()` directo — es exactamente lo que la demo 3 de `code/` mostró que
falla en silencio.

```python
from comun.structured import extraer
from .schemas import Intencion
from .prompts import construir_prompt

def clasificar(modelo, consulta: str) -> Intencion:
    return extraer(modelo, Intencion, construir_prompt(consulta))
```

## Parte 3 · `medir_clasificador.py` (15 min)

Corre las 30 consultas de `recursos/golden/consultas-<tu-track>.json` (campo `intencion`) e
imprime: acierto global, matriz de confusión por categoría, y cuántas extracciones necesitaron
reintento (`al_primer_intento`) — es el primer dato de fiabilidad que mides con tus manos, y se
retoma en la Sesión 10.

## Parte 4 · Tus 5 consultas propias

Añádelas al final de tu medición (no al archivo del curso) y reporta el acierto sobre las 35.

---

## Entregables

| Entregable | Ruta | Contenido |
|---|---|---|
| `schemas.py` | tu proyecto | `Intencion`: categoria (Enum de 5) + urgencia + entidades |
| `prompts.py` | tu proyecto | Plantilla Rol+Contexto+Tarea+Formato + 2 ejemplos few-shot |
| `clasificar.py` | tu proyecto | Usa `extraer()`. Prohibido `with_structured_output()` directo |
| `medir_clasificador.py` | tu proyecto | Acierto + matriz de confusión + reintentos sobre el golden set |

## Criterio de aceptación

- **≥ 90 % de acierto** sobre las 30 consultas del golden set del curso.
- Reportas el acierto sobre las 30 + tus 5 propias (35 en total).
- Reportas cuántas extracciones necesitaron reintento.

> ⚠️ **El umbral del 90 % está sin verificar contra el endpoint real** (nota del esqueleto de
> esta sesión). Si tu equipo mide consistentemente por debajo, repórtalo al docente con el
> número delante — puede ajustarse el umbral o mejorarse el few-shot del curso, pero se decide
> con evidencia, no el día de la clase.

## Reto opcional · no evaluado

Si terminas antes: enriquece `entidades` para que extraiga de verdad el identificador mencionado
(número de línea, cuenta, SKU o placa, según tu track) en vez de dejarlo como texto libre.

---

## Si te atoras

- [`../solucion/<tu-track>/`](../solucion/) — checkpoint de referencia.
- Tabla de errores esperables en el `README.md` de la sesión.
