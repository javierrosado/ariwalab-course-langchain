# Conceptos previos — Sesión 10

> Pre-work de 1 h. Tráelo resuelto: la sesión en vivo lo asume leído.

---

## 1. Conjunto de prueba / *golden dataset*

Un conjunto fijo de casos con su respuesta correcta conocida, usado para medir un sistema de
forma repetible. Ver README.md §1: el tuyo existe desde la S2.

## 2. Precisión y recall, nociones

- **Precisión:** de lo que el sistema marcó como correcto, ¿cuánto lo era de verdad?
- **Recall:** de todo lo que era correcto, ¿cuánto encontró el sistema?

Aplicados aquí: la precisión de selección de tool (L4) y el recall del retriever (¿trajo el
chunk que tenía el dato?).

## 3. *Groundedness*: fidelidad a la fuente

Una respuesta está "groundeada" cuando lo que afirma está respaldado por el texto que el
sistema realmente recuperó — no por el conocimiento general del modelo. Es la métrica central
de cualquier sistema RAG: sin ella, no hay forma de distinguir una respuesta correcta por
suerte de una respuesta correcta por evidencia.

## 4. LLM-as-judge y sus sesgos conocidos

Usar un modelo de lenguaje para evaluar la salida de otro (o de sí mismo). Ver README.md §3
para los 4 sesgos que vas a ver en vivo hoy: autoevaluación, verbosidad, posición,
autocomplacencia.

## 5. Prueba A/B y qué significa "mejoró"

Comparar dos versiones (de un prompt, de un modelo, de un flujo) sobre el mismo conjunto de
prueba. "Mejoró" no es "el número subió una vez": es que la mejora se sostiene y se puede
explicar. Ver README.md §4.

## 6. Regresión: por qué se re-evalúa al cambiar algo

Un cambio que arregla un caso puede romper otro que antes funcionaba. Por eso el golden set no
se corre solo cuando algo falla: se corre **cada vez que algo cambia**, para detectar
regresiones antes de que las detecte un cliente. Es el puente hacia integración continua (CI),
que el curso menciona pero no implementa (fuera de alcance).

---

## Verificación de entrada

Confirma que tu `INFORME-L9.md` (S9) tenga los 2 cuellos de botella documentados con evidencia
— hoy vas a atacar uno de ellos, y necesitas saber cuál.
