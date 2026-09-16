# Documento de diseño — [nombre del equipo] · [track]

> 2-3 páginas. Es lo que distingue el Proyecto M2 del Assignment A1: el A1 pedía una tool que
> funcionara, este documento pide que **defiendan sus decisiones de arquitectura**. También es
> el insumo directo del Proyecto Integrador de la Sesión 11 — no lo escriban para hoy, escríbanlo
> para poder reutilizarlo ahí con ediciones, no desde cero.

---

## 1. El caso de uso, en una frase

[Qué resuelve el agente, para quién, en una sola oración clara.]

## 2. Arquitectura

[Diagrama (ASCII o imagen) de las piezas: `agent.py`, `tools/`, `knowledge/` (retriever),
`memory.py`, `guardrails.py`, y cómo se conectan. Un lector que no vio el código debe poder
seguir el flujo de una consulta de principio a fin.]

```
[diagrama aquí]
```

## 3. Las 4 tools núcleo — y por qué esas cuatro y no otras

| Tool | Qué resuelve | Por qué es núcleo (y no reto opcional) |
|---|---|---|
| [nombre] | [...] | [...] |
| [nombre] | [...] | [...] |
| [nombre] | [...] | [...] |
| [nombre] | [...] | [...] |

[¿Alguna tool del catálogo es de escritura? ¿Qué confirmación exige antes de ejecutarse, y por
qué esa y no otra salvaguarda?]

## 4. Decisiones de RAG

- **Corpus:** [qué documentos se indexaron].
- **Chunking:** [tamaño y solapamiento usados — recuerden que en la S5 estos valores fueron
  fijados por el curso; aquí digan si los mantuvieron o los ajustaron en la clínica, y por qué].
- **RAG tradicional vs agéntico:** [cuál usaron y por qué].
- **Salvaguarda A6:** [cómo garantizan que el agente cite la fuente antes de afirmar una tarifa,
  cobertura o política].

## 5. Decisiones de guardrails

- **Lista de prohibidos del track:** [copien la lista real que implementaron].
- **Los 3 puntos de enganche:** [qué guardrail corre en cada uno — entrada, acción, salida].
- **Escalamiento a humano:** [qué condición lo dispara].
- **Resultado de la batería de 15 ataques + 5 propios:** [N/20 sin filtración].

## 6. Qué se rompió y cómo se endureció (L7)

[Resumen de 3-5 líneas de los hallazgos de `INFORME-L7.md` — el detalle completo va en ese
archivo, aquí solo el resumen ejecutivo para quien lea este documento sin el informe completo.]

## 7. Qué dejarían para después

[Honestidad técnica: qué saben que falta o que harían distinto con más tiempo. No es una
debilidad admitirlo — es lo que un documento de diseño real hace.]
