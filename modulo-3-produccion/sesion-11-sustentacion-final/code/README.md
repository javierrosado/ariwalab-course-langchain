# Código de la Sesión 11

| Archivo | Qué es |
|---|---|
| [`index.html`](index.html) | Cliente de referencia con streaming, contra `/chat/stream` |

No hay demos numeradas esta sesión — el esqueleto (`sesion-11.md`) dedica el bloque 0 en vivo a
cómo se argumenta ante un panel, no a contenido técnico nuevo. `index.html` es el único
artefacto de código: ábrelo directamente en el navegador (no necesita servidor propio) y
apúntalo a tu Space desplegado.

## Por qué `fetch()` + `ReadableStream`, y no `EventSource`

`EventSource` (la API nativa del navegador para Server-Sent Events) solo soporta peticiones
`GET` y no permite mandar cabeceras propias — no hay forma de pasarle `X-API-Key` sin ponerla en
la URL como *query param*, lo que la dejaría en logs y en el historial del navegador. Por eso el
cliente usa `fetch()` con método `POST` y decodifica el flujo de eventos a mano.

## Cómo probarlo

1. Abre `index.html` directamente en tu navegador (doble clic, o arrástralo a una pestaña).
2. Completa la URL de tu Space (del L8) y tu `AGENT_API_KEY`.
3. Escribe un mensaje y pulsa Enviar — deberías ver la respuesta aparecer palabra por palabra.

## Si algo falla

| Síntoma | Causa | Solución |
|---|---|---|
| No aparece nada, `estado` se queda en "conectando..." | El Space está dormido (*cold start*) | Espera unos segundos; es la misma latencia del L8 |
| Error 401 | La API key no coincide | Copia el valor exacto de tu `Space secret` |
| La respuesta llega toda de golpe, no palabra por palabra | Tu `/chat/stream` no está transmitiendo por tokens — revisa que uses `model.stream()` y no `model.invoke()` en el último paso | Ver `solucion/<tu-track>/agent.py`, función `responder_streaming` |
| Error de CORS en la consola del navegador | El Space no permite peticiones desde `file://` | Añade `CORSMiddleware` a tu `api.py` (ver el checkpoint de referencia) |
