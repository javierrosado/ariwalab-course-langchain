# Sesión 5 — Memoria contextual y RAG con Qdrant Cloud

> Esqueleto de diapositivas. Fuente: `docente/esqueletos/sesion-05.md`.

---

## Sesión 5 · Memoria + RAG
- Semana 3 · martes · 6 h (3.0 T / 3.0 P)
- La sesión más frágil operativamente: depende de Qdrant, aprovisionado en la semana 0
- Hito: Avance 2 · Qdrant operativo en todos los equipos

---

## El agente que no recuerda y el que no sabe
- Dos carencias distintas, dos soluciones distintas

---

## Estado conversacional y `thread_id`
- El modelo es *stateless*: la memoria la implementa tu código

---

## Embeddings aplicados al dominio
- Dos preguntas del track sin palabras en común, cerca en el espacio vectorial

---

## Chunking y su trade-off
- Chunk grande: contexto sobrante y se paga en tokens
- Chunk chico: contexto amputado
- Valores fijos por track (telco/banca 400/60 · retail 350/50 · seguros 600/100)

---

## Qdrant: colección, punto, payload, filtros
- El payload es lo que permite **citar**

---

## RAG tradicional vs RAG agéntico
- Tradicional: siempre busca, pega el contexto
- Agéntico: decide si busca, llama al retriever como tool, responde citando
- "Hola, buenos días" no debería disparar una búsqueda

---

## Salvaguarda A6 y la fundamentación
- Ante tarifas, coberturas, plazos o políticas: recuperar y citar, o decir que no se sabe
- Una respuesta sin fuente no se puede auditar

*(Pausa · 10 min)*

---

## Laboratorio guiado: ingesta del corpus del track
- De 3 `.md` a una colección consultable

---

## Demo clave — parametrico vs recuperable (no se recorta)
- Preguntar una tarifa → responde citando el tarifario
- Editar el documento en Qdrant → el precio cambia
- Preguntar lo mismo → responde el nuevo precio, citando el mismo documento
- ¿Qué habría hecho falta cambiar si el precio estuviera en los pesos del modelo?

---

## Avance 2 del proyecto
- Qué preguntas resuelve el RAG y cuáles las tools

---

## Qué NO entra hoy
- Guardrails, PII → S6
- Pruebas de estrés → S7
- Métricas de *groundedness* → S10
