# Laboratorio L11 · Aplicación final

**Objetivo:** cerrar el proyecto acumulado desde el L1 con un cliente con streaming y un
documento de diseño.

**Duración:** 2 h, **antes** de la sesión en vivo (no durante).

---

## Parte 1 · `app/web/index.html` con streaming (50 min)

Añade `/chat/stream` a tu `api.py` del L8 (ver `solucion/<tu-track>/api.py` como referencia):
usa `model.stream()` en el último paso del bucle —el de redactar la respuesta final, cuando ya
no hay más tool calls— y transmite cada fragmento como un evento Server-Sent Events. Adapta
`code/index.html` a tu proyecto (cambia solo lo necesario; la lógica de `fetch()` +
`ReadableStream` no cambia entre tracks).

## Parte 2 · Documento de diseño (40 min)

Completa [`plantilla-documento-diseno.md`](../../../recursos/plantillas/plantilla-documento-diseno.md),
4 páginas, no más.
La sección 4 (Evidencia) importa más de lo que parece: decir qué falta es señal de que
entendiste el sistema.

## Parte 3 · Verificar y capturar evidencia (20 min)

```bash
python docente/verificar_despliegue.py --url https://<tu-space>.hf.space --key <tu-key>
```

Guarda la salida completa (para la entrega de 24 h antes) y una captura de una traza reciente
en Langfuse.

## Parte 4 · Ensayo cronometrado (10 min)

Corre tu demo una vez, con reloj, siguiendo los 4 movimientos del README.md §0. Ajusta lo que se
pase de tiempo — el día de la sustentación no hay margen para improvisar el timing.

---

## Entregables

| Entregable | Ruta |
|---|---|
| `app/web/index.html` | tu repositorio de equipo |
| `/chat/stream` en tu `api.py` | tu repositorio de equipo |
| Documento de diseño (4 páginas) | `lab/<tu-track>/documento-diseno.md` |
| Evidencia de las 24 h (URL, key, traza, verificación) | según indique el docente |

## Cada track

| Track | Enunciado |
|---|---|
| Telecomunicaciones · AndesMóvil | [`telecomunicaciones/enunciado.md`](telecomunicaciones/enunciado.md) |
| Banca · Banco Inti | [`banca/enunciado.md`](banca/enunciado.md) |
| Retail · MercaSur | [`retail/enunciado.md`](retail/enunciado.md) |
| Seguros · Andina Seguros | [`seguros/enunciado.md`](seguros/enunciado.md) |
