# Conceptos previos · Sesión 5

> Pre-work asíncrono de 1 h. Termina con el pase de entrada: `check_stack` en verde.

---

## 1. Similitud coseno, otra vez, con tu propio dominio

Ya la viste en la Sesión 0. Hoy la aplicas a preguntas reales de tu track: escribe dos formas
distintas de preguntar lo mismo (con y sin palabras compartidas) y compáralas mentalmente antes
de la sesión. Ejemplo genérico: "¿cuántos gigas me quedan?" vs. "consulta de mi consumo de datos
disponible" — significan lo mismo, comparten casi ninguna palabra.

## 2. Chunking: por qué partir y qué se pierde al partir

Un documento completo no cabe (ni conviene) meterlo entero en cada llamada: cuesta tokens y
diluye la relevancia. Se parte en **chunks** (fragmentos) que se embeben e indexan por separado.
El tamaño del chunk es un trade-off: muy chico, pierde contexto; muy grande, arrastra ruido. Hoy
usas los tamaños ya fijados por el curso (ver `README.md` sección 3) — pero debes entender el
porqué, no solo copiar el número.

## 3. Vocabulario de Qdrant: colección, punto, vector, payload, filtro

Ver `README.md` sección 4. Si nunca usaste una base vectorial gestionada, piensa la colección
como una tabla y el payload como las columnas adicionales de cada fila (más allá del vector).

## 4. Verificación: pase de entrada

```bash
python -m comun.check_stack
```

Antes de la sesión, comprobaciones **6 (Embeddings)** y **7 (Qdrant Cloud)** deben estar en
verde. Si alguna falla, avisa **hoy**, no en el laboratorio — hay margen para usar la colección
de respaldo, pero necesitas saberlo antes de empezar.

---

## Checklist final

- [ ] `python -m comun.check_stack` con las comprobaciones 6 y 7 en verde.
- [ ] Sabes explicar, con tus palabras, la diferencia entre "no recuerda" y "no sabe" (sección 0
  del `README.md`).
- [ ] Repasaste tu Avance 1 del proyecto (L4): las preguntas que ninguna tool resolvía son
  exactamente las que resuelve el RAG de hoy.
