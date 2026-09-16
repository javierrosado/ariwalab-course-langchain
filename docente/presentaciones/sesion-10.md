# Sesión 10 — Optimización continua y evaluación

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-10.md`.

---

## Sesión 10 · Evaluación y optimización
- Semana 5 · jueves · 6 h (2.5 T / 3.5 P)
- Hito: Avance 3 del Módulo 3
- La espina dorsal del curso se cierra hoy

---

## Mejorar con evidencia, no con intuición
- Retomar los 2 cuellos del Avance 2 — hoy se atacan

---

## El golden dataset era el de siempre
- Las mismas 30 consultas del L2/L4/L5, usadas por 4ª vez, completas
- 20 con tool esperada + 10 OTRO
- Un conjunto de evaluación no se improvisa al final: se construye mientras se construye el
  sistema

---

## Los 3 evaluators determinísticos
- Uso correcto de tool (= `matriz_seleccion.py`)
- Exactitud (¿aparece el dato correcto?)
- Groundedness por cita (¿la cita existe y sostiene la afirmación?)
- Se pueden correr mil veces y dan lo mismo

---

## LLM-as-judge y sus sesgos
- El juez es demo; la nota la sostienen los 3 evaluators determinísticos
- Sesgos: autoevaluación, verbosidad, posición, autocomplacencia

---

## A/B de prompts: cuándo una mejora es real
- v1: 80 % · v2: 86.7 % — ¿mejoró? Depende: ¿se corrió dos veces? ¿se sabe qué la causó?
- Con 30 casos, 2 aciertos de diferencia pueden ser ruido

*(Pausa · 10 min)*

---

## Práctica: los 30 casos en Langfuse Datasets
- Cargar y correr la línea base v1

---

## Optimizar y medir v2
- Un cambio, una medición, una fila en la tabla
- Un cambio por medición: si cambias tres cosas y mejora, no sabes cuál sirvió

---

## Qué NO entra hoy
- El cliente web y la demo final → S11
- RAGAS en profundidad → mención y enlace
- Fine-tuning como vía de mejora → descartado por D21
