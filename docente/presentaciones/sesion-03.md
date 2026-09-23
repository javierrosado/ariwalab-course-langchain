# Sesión 3 — Herramientas, API externa y Assignment A1

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-03.md`.

---

## Sesión 3 · Tools, API externa y Assignment A1
- Semana 2 · martes · 6 h (2.5 T / 3.5 P)
- Hito: **Assignment A1 — 100 % del Módulo 1**
- La sesión más cara del módulo: primera vez que toca el simulador de verdad

---

## Hoy el modelo deja de saber y empieza a consultar
- Recuperar la alucinación de la S1 y anunciar que hoy se acaba

---

## Function calling: quién genera y quién ejecuta
- El modelo **propone** una llamada en JSON — nunca la ejecuta
- Tu código decide, valida argumentos, aplica permisos
- El paso 3 (tu código decide) es toda la seguridad del sistema — se retoma entero en la S6

---

## La docstring es el prompt (regla A2)
- Verbo + cuándo usarla + cuándo NO
- Reescribir en vivo una docstring mala → buena
- La calidad de una docstring es un número medible (`docente/matriz_seleccion.py`)

---

## Errores redactados para el modelo (regla A4)
- 404 → dato inexistente, dilo claro
- 401 → credencial, reintentar no soluciona
- 503 → servicio caído, ofrece reintentar más tarde
- Para el modelo, no para un log

---

## Demo: bucle ReAct manual → `create_agent()`
- Las ~20 líneas del bucle escrito a mano
- Después, las 3 líneas de la abstracción — no añade inteligencia, quita código repetido

*(Pausa · 10 min)*

---

## Práctica guiada: el primer `@tool` contra el simulador
- Todos escriben la misma tool del track, en clase

---

## Los 3 escenarios con `?_fallo=`
- Éxito · dato inexistente · servicio caído (503)
- El agente no debe inventar ni entrar en bucle de reintentos

---

## Rúbrica del A1 y reparto de trabajo
- Funcionalidad 30 % · Diseño 25 % · Errores 25 % · Evidencia 10 % · Comunicación 10 %
- Regla del piso: si `prueba_tool.py` pasa los 3 escenarios y la docstring cumple A2, no baja de
  Competente aunque el modelo no haya elegido la tool en la demo
- Entrega miércoles 23:59 · sustentación jueves (S4), 4 equipos rotando

---

## Qué NO entra hoy
- Catálogo de varias tools, selección dinámica → S4
- Tools de escritura → S4
- Memoria y RAG → S5
- Guardrails, PII → S6
