# Sesión 2 — Ecosistema LangChain: prompts, cadenas y modelos

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-02.md`.

---

## Sesión 2 · Ecosistema LangChain
- Semana 1 · jueves · 6 h (3.0 T / 3.0 P)
- Hitos: Test 2 · pase de entrada de Pydantic (bloqueante)
- Hoy: de texto libre a estructura tipada

---

## De "primer llamado" a "primer contrato"
- Hoy el modelo deja de devolver texto y empieza a devolver estructura

---

## Mensajes, roles y *statelessness*
- `system` / `human` / `ai`
- El historial es una lista que **tú** reenvías
- Por qué el turno 10 cuesta 8× el turno 1

---

## Rol + Contexto + Tarea + Formato
- Las 4 partes, sobre el prompt real del track
- Quitar "Formato" degrada más la salida que quitar "Rol"

---

## Few-shot (regla A5)
- Cuándo rinde: enums y campos ambiguos
- Cuándo solo gasta tokens: se paga en cada llamada, no una sola vez

---

## Structured output: la demo del fallo
- `with_structured_output()` puro, sin few-shot, con una consulta ambigua
- El modelo inventa un valor de Enum o deja un campo vacío
- El fallo no aparece donde se produce — revienta tres líneas más abajo

---

## `comun/structured.py` (regla A3)
- `extraer()`: valida, reintenta UNA vez con el error concreto, o falla con `ExtraccionFallida`
- Por qué un solo reintento: si falla dos veces, el problema es el esquema, no la suerte

*(Pausa · 10 min)*

---

## Práctica guiada: esquema `Intencion` del track
- Cada equipo escribe su Enum de 5 categorías y lo prueba

---

## Test 2
- 10 preguntas, en clase

---

## Qué NO entra hoy
- `@tool`, function calling, `create_agent()` → S3
- RAG, embeddings, Qdrant → S5
- Memoria conversacional real → S5
- Guardrails y PII → S6
