# Conceptos previos · Sesión 7 — Testing no determinístico

> Pre-work asíncrono de 1 h.

---

## 1. Por qué falla `assert respuesta == "esperado"`

Ya lo anunciamos en la Sesión 0: un LLM no es una API determinística. Incluso a `temperature=0`,
la misma pregunta puede producir texto ligeramente distinto entre ejecuciones. Un test que
compara texto exacto va a fallar la mayoría de las veces, incluso cuando el agente "acertó" en
todo lo que importa.

## 2. Invariantes en vez de igualdades

Un invariante es una propiedad que debe cumplirse, sin exigir un texto exacto:

- *"la respuesta cita una fuente"* en vez de *"la respuesta dice exactamente X"*.
- *"no aparece un DNI sin enmascarar"* en vez de *"la respuesta no menciona a Juan Pérez"*.
- *"llamó a como máximo 3 tools"* en vez de *"llamó exactamente a estas tools en este orden"*.

Ver `README.md` sección 0 para la tabla completa.

## 3. Las 4 familias de caso borde

Entrada ambigua · dato ausente · servicio caído · salida fuera de formato. Ver `README.md`
sección 0 para el detalle y un ejemplo de cada una.

## 4. Los 6 fallos inyectables del simulador

`timeout` · `error500` · `error503` · `lento` · `vacio` · `malformado`. Se fuerzan con
`?_fallo=<nombre>` contra cualquier endpoint del simulador. Sin ese parámetro, y con
`CHAOS_RATE>0`, el simulador inyecta aleatoriamente `error503` o `lento` — los otros 4 solo se
disparan a propósito, con el parámetro explícito.

---

## Checklist final

- [ ] Puedo explicar, con mis palabras, por qué "pasó 4 de 5 veces" es una medición y no un
  fallo.
- [ ] Repasé las 4 familias de caso borde y tengo un ejemplo propio de cada una en mente.
- [ ] Sé cómo forzar cada uno de los 6 fallos del simulador con `?_fallo=`.
- [ ] Mi agente (con tools + RAG + memoria + guardrails de las sesiones 4 a 6) corre de punta a
  punta antes de la clínica.
