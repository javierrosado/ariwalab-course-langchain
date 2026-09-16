# Banco de preguntas — autoevaluación, Test 1 y Test 2

> **Qué es esto.** Un índice para el docente de los 3 instrumentos de verificación de
> conocimiento que ya existen en el curso. **No duplica las preguntas** — viven en sus archivos
> originales, y duplicarlas aquí las desincronizaría en cuanto alguien corrija una allá y no acá
> (el mismo error que `CLAUDE.md` pide no repetir con los documentos generados). Este archivo
> dice **dónde está cada uno, cuándo se administra y qué mide**.

---

## Los 3 instrumentos

| # | Instrumento | Ubicación | Preguntas | Umbral | Cuándo |
|---|---|---|---|---|---|
| 1 | **Autoevaluación de la Sesión 0** | [`00-preparacion/autoevaluacion.md`](../00-preparacion/autoevaluacion.md) | 10 (6+2+2, tres partes) | **8/10 — bloqueante** | Antes de entrar a la S1, autoadministrada, sin consultar material |
| 2 | **Test 1** | [`modulo-1-fundamentos/sesion-01-fundamentos-agentes/conceptos-previos.md`](../modulo-1-fundamentos/sesion-01-fundamentos-agentes/conceptos-previos.md) (sección "Test 1") | 10, en 7 partes (A-G) | Ninguno — es verificación, no filtro | En clase, al cierre del bloque teórico de la S1 (bloque 7, 15 min) |
| 3 | **Test 2** | [`modulo-1-fundamentos/sesion-02-ecosistema-langchain/conceptos-previos.md`](../modulo-1-fundamentos/sesion-02-ecosistema-langchain/conceptos-previos.md) (sección "Test 2") | 10, en 5 partes (A-E) | Ninguno | En clase, al cierre del bloque teórico de la S2 (bloque 7, 15 min) |

Los tres siguen el mismo formato: opción múltiple con las respuestas comentadas al final (no
solo la letra correcta), dentro de un `<details>` plegable para no arruinar el intento de quien
lee el archivo antes de responder.

---

## Por qué solo hay 2 tests, no uno por sesión

Los esqueletos de las sesiones 3 en adelante (`docente/esqueletos/sesion-03.md` y siguientes) no
piden un "Test N" — la verificación de aprendizaje pasa a hacerse con el **laboratorio y su
criterio de aceptación** (medido con `docente/matriz_seleccion.py`,
`docente/verificar_guardrails.py`, etc.) o con la **rúbrica del hito de evaluación**
(Assignment A1 en la S3, Proyecto M2 en la S7, Proyecto Integrador en la S11). Es una decisión
de diseño, no un hueco: un test de opción múltiple mide si el alumno entendió un concepto; un
laboratorio medido mide si construyó algo que funciona — y a partir de la S3 eso es lo que
importa. Ver `docente/esqueletos/README.md` para la convención completa de cada sesión.

---

## Qué mide cada instrumento

### Autoevaluación de la Sesión 0

Gate de entrada al curso: fundamentos de LLM (token, ventana de contexto, temperatura,
alucinación, embedding, costo), nociones de agentes y arquitectura, y el entorno (`venv`,
`.env`, las 3 cuentas). Es la única de las tres con umbral bloqueante — sin 8/10, no se avanza a
la S1.

### Test 1 (Sesión 1)

Verifica los objetivos de aprendizaje 1 y 2 de la S1: las 4 piezas que le faltan a un LLM para
ser agente, el bucle percepción→razonamiento→acción→entorno, workflow vs agente, el antipatrón
de tratar al modelo como una API determinística, modelos de pesos abiertos, y por qué existe
`comun/provider.py` (D13).

### Test 2 (Sesión 2)

Verifica los objetivos 1, 2, 3 y 5 de la S2: por qué el modelo es *stateless*, la estructura
Rol+Contexto+Tarea+Formato, cuándo el few-shot rinde y cuándo no (regla A5), qué recibe
realmente el modelo (JSON Schema, no la clase Pydantic), por qué `with_structured_output()` no
basta y qué añade `comun/structured.py` (regla A3), y qué domina el costo de una conversación
larga.

---

## Si se corrige una pregunta

Corrígela **en el archivo original** (nunca aquí) y, si cambia lo que el instrumento mide,
actualiza la fila correspondiente de la tabla de arriba en el mismo commit — es la misma
disciplina que exige `CLAUDE.md` para los documentos generados, aplicada a un índice curado a
mano en vez de a un script.
