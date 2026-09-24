# Laboratorio L1 · Entorno y primer script

**Alcance:** entorno verde y tu primer script del track. **Sin tools, sin Pydantic,
sin agente.** Eso llega en las sesiones 2 y 3 — hoy es, deliberadamente, más simple.

**Duración:** 2 h, en 4 partes.

> **`proyecto-final/` no es tu repositorio.** Vas a ver esa carpeta en la raíz del curso: es la
> **implementación de referencia del docente**, no una plantilla para copiar. Tu propio proyecto
> lo construyes tú, desde hoy, en tu propio repositorio — laboratorio a laboratorio, del L1 al
> L11. Detalle completo en el `README.md` raíz del curso, sección "`proyecto-final/`: qué es y
> qué no es".

---

## 1. Objetivo

Terminar con:

1. Tu entorno verde: `python -m comun.check_stack --solo-modelo` sin errores.
2. Tu propio script, `primer_contacto.py`, que le hace **3 preguntas reales de tu industria** al
   modelo — usando la infraestructura del curso, no una llamada suelta.
3. Tu equipo y tu track registrados con el docente.

---

## 2. Las 4 partes

| Parte | Min | Qué haces |
|---|---|---|
| 1 | 40 | Poner `python -m comun.check_stack --solo-modelo` en verde. Es la única ventana del curso dedicada a arreglar entornos — si te bloqueas, pide ayuda al docente ahora, no después |
| 2 | 50 | Escribir `primer_contacto.py` de tu track: 3 preguntas reales del dominio al modelo |
| 3 | 20 | Registrar tu equipo y tu track en la plantilla del docente |
| 4 | 10 | Verificación cruzada: que tu compañero de equipo corra tu script y tú el suyo |

**Por qué 40 minutos de verificación y no 10.** El primer laboratorio de cualquier curso se
consume arreglando entornos. Reconocerlo en el diseño evita que la Sesión 2 empiece con la mitad
del aula bloqueada — y la Sesión 3 es el **Assignment A1**, el día 3 del curso.

---

## 3. Tu track

Elige tu enunciado según el track que tu equipo propuso al cerrar la sesión en vivo (recuerda:
**el equipo propone, el docente balancea** — ver `README.md` de la sesión, sección 10):

| Track | Enunciado |
|---|---|
| Telecomunicaciones — AndesMóvil | [`telecomunicaciones/enunciado.md`](telecomunicaciones/enunciado.md) |
| Banca — Banco Inti | [`banca/enunciado.md`](banca/enunciado.md) |
| Retail — MercaSur | [`retail/enunciado.md`](retail/enunciado.md) |
| Seguros — Andina Seguros | [`seguros/enunciado.md`](seguros/enunciado.md) |

Cada enunciado tiene las mismas 4 partes de arriba; solo cambian las 3 preguntas de dominio y el
reto opcional, porque son propias de cada industria.

---

## 4. Entregables

| Entregable | Ruta |
|---|---|
| `.env` completo y `python -m comun.check_stack --solo-modelo` en verde | raíz del curso |
| `primer_contacto.py` | `lab/<tu-track>/primer_contacto.py` (créalo dentro de tu carpeta de track) |
| Track declarado por tu equipo | plantilla del docente |

---

## 5. Criterio de aceptación

- El script corre **sin instalar ningún motor de inferencia ni base de datos** en tu laptop.
- Usa `comun.provider.get_chat_model()`; **no** instancia `ChatOpenAI` directamente.
- Las 3 preguntas son del dominio de tu track, no genéricas ("¿qué es un agente?" no cuenta).

Si tu script cumple esto pero además usa `comun.prompts_industria.get_system_prompt()` para
personalizar el tono (como viste en la demo 2 y 3 de `code/`), mejor: es exactamente el patrón
que vas a reutilizar en tu proyecto desde el Laboratorio 2.

---

## 6. Reto opcional · no evaluado

Está detallado en el enunciado de tu track. La idea general: hazle al modelo una **cuarta**
pregunta cuya respuesta solo existe en los datos internos de la empresa — el modelo no tiene
forma de saberla porque todavía no tiene ninguna herramienta. Anota en 5 líneas qué se inventó.
Guarda esa nota: la vas a releer en la Sesión 5 como el "antes" del RAG, cuando tu agente por fin
pueda consultar el dato real en vez de inventarlo.

---

## 7. Errores esperables

| Síntoma | Causa | Qué hacer |
|---|---|---|
| `401` contra Hugging Face | Token sin permiso de inferencia | Regenera el token marcando ese permiso |
| `ModuleNotFoundError: comun` | Ejecutando desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `ModuleNotFoundError: langchain` | `venv` sin activar | Reactívalo; el prompt debe mostrar `(.venv)` |
| Acentos rotos en Windows | Codificación de la consola | `chcp 65001` |
| El modelo responde en inglés | Falta el `system` en español | Revisa la demo 2 de `code/`: úsalo como referencia |
| El modelo tarda 20 s | Cola del *inference provider* | Normal. Se mide y se optimiza en la Sesión 10 |

Si te quedas sin salida después de intentarlo, revisa `solucion/<tu-track>/primer_contacto.py`
— es el checkpoint de referencia, no el punto de partida.
