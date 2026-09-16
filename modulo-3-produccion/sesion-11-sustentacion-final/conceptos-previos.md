# Conceptos previos — Sesión 11

> Pre-work de 1 h. Tráelo resuelto: la sesión en vivo lo asume leído. Además de estos 4
> conceptos, hoy hay una **entrega anticipada, 24 h antes** — ver README.md §6.

---

## 1. Diagramas de arquitectura (C4, nivel 1 y 2, o equivalente)

Un diagrama C4 nivel 1 (contexto) muestra tu sistema y con qué otros sistemas habla, sin
detalle interno. El nivel 2 (contenedores) abre esa caja: API, agente, base vectorial, modelo.
No necesitas herramientas especiales — un diagrama ASCII o un rectángulo-y-flechas en cualquier
editor cumple, siempre que sea claro.

## 2. OpenAPI / Swagger, que FastAPI ya genera

FastAPI expone automáticamente `/docs` (Swagger UI) y `/openapi.json` a partir de tus modelos
Pydantic — no necesitas escribir la especificación a mano. Es parte del entregable: un
evaluador puede explorar tu API sin leer tu código.

## 3. Server-Sent Events y streaming en el navegador

Un flujo de eventos unidireccional del servidor al cliente sobre una única conexión HTTP: cada
evento es una línea `data: <contenido>\n\n`. A diferencia de WebSockets, es unidireccional y
más simple de implementar sobre HTTP estándar — suficiente para mostrar la respuesta del agente
palabra por palabra en vez de esperar a que termine. Ver `code/README.md` para por qué el
cliente de referencia usa `fetch()` en vez de `EventSource`.

## 4. Cómo se argumenta una decisión: alternativas, criterio, consecuencia

Ver README.md §0. Es el marco que sostiene tanto el movimiento 3 de tu demo como la sección 3
de tu documento de diseño.

---

## Entrega anticipada, 24 h antes

Sube a tu repositorio (o al canal que indique el docente):

- [ ] URL pública de tu Space (L8)
- [ ] API key para el panel
- [ ] Captura de una traza en Langfuse (L9)
- [ ] Salida de `python docente/verificar_despliegue.py --url <tu-url> --key <tu-key>` en verde
