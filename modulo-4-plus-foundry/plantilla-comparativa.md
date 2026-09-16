# Cuadro comparativo — Hugging Face vs. Microsoft Foundry

> Plantilla del entregable del bonus (paso 8). 7 dimensiones, con evidencia **propia**, medida
> por ti — no copiada de documentación ni de precios de lista. Completa cada celda; borra las
> instrucciones entre `< >`.

---

## 1 · Latencia

La misma batería de 5 consultas del track, corrida contra ambos proveedores. Reporta p50 (no
promedio — S9 §3).

| | Hugging Face | Foundry |
|---|---|---|
| p50 de las 5 consultas | `<N> s` | `<N> s` |
| Notas | `<cold start, cola del inference provider, etc.>` | `<latencia de red al endpoint, etc.>` |

## 2 · Costo

Costo por ejecución en cada plataforma, **con la fórmula**, no con la cifra (las cifras caducan).

| | Hugging Face | Foundry |
|---|---|---|
| Fórmula | `<tokens de entrada × precio + tokens de salida × precio>` | `<misma fórmula, con el precio del deployment>` |
| Costo estimado de las 5 consultas | `<N>` | `<N>` |

## 3 · Calidad de respuesta

Las 5 respuestas lado a lado — ¿cuál sirve mejor para tu caso de uso, y por qué?

| Consulta | Respuesta HF | Respuesta Foundry | ¿Cuál prefieres y por qué? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## 4 · Soberanía del dato

`<dónde corre el modelo, bajo qué jurisdicción, qué se puede auditar en cada plataforma>`

## 5 · Portabilidad

Qué habría que cambiar para volver de Foundry a Hugging Face (o viceversa). **Medido en
archivos tocados**, no en opinión.

| | Archivos tocados |
|---|---|
| Para volver a Hugging Face | `<N — idealmente solo el .env>` |

## 6 · Curva de puesta en marcha

Minutos desde cero (cuenta creada) hasta la primera respuesta del modelo, cronometrados.

| | Minutos |
|---|---|
| Hugging Face (si lo recuerdas de la S1) | `<N>` |
| Foundry (hoy) | `<N>` |

## 7 · Dependencia del proveedor

`<qué queda atado a Foundry específicamente (protocolo Responses, hosting) y qué no
(comun/provider.py, las tools, el retriever)>`

---

## Conclusión

**No hay ganador predeterminado.** En una frase: ¿en qué contexto elegirías cada una?

- Elegiría **Hugging Face** cuando: `<1 frase>`
- Elegiría **Foundry** cuando: `<1 frase>`
