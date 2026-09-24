# Sesión 4 — Tools e integración de herramientas

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-04.md`.
> ⚠️ Descuadre de 20 min sin resolver (sustentación A1 + guion) — ver `docente/guia-docente.md`,
> sección de decisiones pendientes, antes de dictar.

---

## Sesión 4 · Catálogo de 4 tools
- Semana 2 · jueves · 6 h (2.5 T / 3.5 P)
- Arranca con la sustentación del A1 (4 equipos, 5 min c/u)
- Hito: Avance 1 del proyecto

---

## De una tool a cuatro
- Qué se rompe al añadir herramientas

---

## Catálogo y responsabilidad única
- Una tool, una pregunta
- La tool que hace dos cosas nunca se elige bien

---

## Selección dinámica: cómo elige y por qué falla
- El modelo solo lee nombre + docstring + esquema de argumentos
- 3 tipos de confusión: solapamiento, vacío, sobre-uso

---

## Por qué 4 y no 6 (regla A1)
- Fiabilidad compuesta: 0.93³ ≈ 80 % bajo supuestos de independencia; no tasa universal
- Más tools enlazadas → más pasos potenciales → más error acumulado

---

## Idempotencia y tope de iteraciones (regla A4)
- Leer es reintentable; escribir no
- Primera tool que modifica algo: exige confirmación explícita antes de ejecutarse
- El bucle que no termina ante un 5xx sostenido

*(Pausa · 10 min)*

---

## Laboratorio guiado: completar el catálogo
- Las 4 tools núcleo del track (la 1ª ya existe, del L3)

---

## Medir: correr la matriz de selección propia
- `docente/matriz_seleccion.py --tools lab/<track>/domain_tools.py`
- Leer la matriz de confusión y corregir una docstring
- Aclaración: `proyecto-final/` del repo del curso es la referencia del docente, no el proyecto
  del alumno

---

## Avance 1 del proyecto
- Caso de uso en una frase
- Las 4 tools y por qué esas y no otras
- Qué preguntas no resuelve ninguna tool (→ RAG, S5)

---

## Qué NO entra hoy
- RAG, embeddings, Qdrant → S5
- Guardrails, PII → S6
- Construir un servidor MCP propio → reto opcional
