# Laboratorio L9 · Trazabilidad del agente desplegado

**Objetivo:** ver por dentro qué hizo tu agente en cada ejecución, ya desplegado.

**Duración:** 2 h.

**Punto de partida:** tu `app/api.py` del L8, ya desplegado en un Space que responde.

---

## Parte 1 · `observability.py` (25 min)

Escribe `solucion/<tu-track>/observability.py` (ver el checkpoint de referencia como punto de
partida): expone `get_callbacks()`, que devuelve el callback de Langfuse con el enmascarador de
PII ya enganchado (`comun.observability`, sesión ya instrumentada centralmente — no reescribas
el enmascarador). Modifica tu `agent.py` (v4 → v5) para pasar
`config={"callbacks": get_callbacks()}` en **cada** `model.invoke()` y `tool.invoke()` del
bucle — es la única forma de que la jerarquía completa (modelo + tools + retriever) aparezca en
un solo trace.

## Parte 2 · Secrets y redespliegue (20 min)

Añade `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY` y `LANGFUSE_HOST` como *Space secrets* (igual
que en el L8) y vuelve a hacer `git push`. Confirma que el Space reconstruyó sin errores.

## Parte 3 · Generar tráfico real (30 min)

```bash
python docente/generar_trafico.py --track <tu-track> --url https://<tu-space>.hf.space --key <tu-key>
```

Envía 20 consultas reales de tu golden set contra tu `/chat` público — sin volumen, p50/p95 no
significan nada (bloque 3 del README).

## Parte 4 · Leer trazas y hallar 2 cuellos de botella (45 min)

Abre tu proyecto en cloud.langfuse.com y lee los 20 traces que acabas de generar. Documenta 2
cuellos de botella reales con evidencia (captura de la traza + el número medido). No se te
adelantan los cuellos típicos — el docente los conoce (ver `README.md` de la sesión), pero
encontrarlos en tu propia traza es el ejercicio.

---

## Entregables

| Entregable | Ruta |
|---|---|
| `app/observability.py` | tu repositorio de equipo |
| Space redesplegado y trazando | URL en tu `DESPLIEGUE.md` (actualízalo) |
| `INFORME-L9.md` con 2 cuellos de botella | `lab/<tu-track>/` |

Ver la plantilla de `INFORME-L9.md` en
[`solucion/telecomunicaciones/INFORME-L9.md`](../solucion/telecomunicaciones/INFORME-L9.md).

## Criterio de aceptación

- Las trazas provienen del **Space desplegado**, no de tu laptop. Se comprueba en el dashboard
  (todas deben tener el tag o el `run_name` que uses para distinguir entornos).
- **Ninguna traza contiene PII sin enmascarar.**
- **2 cuellos de botella documentados** con evidencia: captura de la traza, el número medido, y
  qué se propone cambiar.

## Avance 2 del M3

Media página: los 2 cuellos, el número que los evidencia, y **cuál se va a atacar en la S10** —
es exactamente el insumo del A/B de prompts de la siguiente sesión.

## Cada track

| Track | Enunciado |
|---|---|
| Telecomunicaciones · AndesMóvil | [`telecomunicaciones/enunciado.md`](telecomunicaciones/enunciado.md) |
| Banca · Banco Inti | [`banca/enunciado.md`](banca/enunciado.md) |
| Retail · MercaSur | [`retail/enunciado.md`](retail/enunciado.md) |
| Seguros · Andina Seguros | [`seguros/enunciado.md`](seguros/enunciado.md) |
