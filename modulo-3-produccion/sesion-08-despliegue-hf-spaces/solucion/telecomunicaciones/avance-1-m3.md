# Avance 1 del Módulo 3 — [equipo] · telecomunicaciones

> Plantilla. Media página: el diagrama de arquitectura de despliegue y una frase por pieza.

## Diagrama de arquitectura de despliegue

```
   [ evaluador / cliente HTTP ]
              │
              │ HTTPS + X-API-Key
              ▼
   [ HF Space — contenedor Docker, uvicorn ]
              │
       ┌──────┼──────────────┬─────────────┐
       ▼      ▼              ▼             ▼
   [ HF Inference ]   [ Qdrant Cloud ]  [ Simulador de industria ]
   (modelo Qwen3)     (colección RAG)   (datos del track)
```

Reemplaza el diagrama de arriba solo si tu arquitectura real difiere (por ejemplo, si
agregaste una caché o un componente propio).

## Una frase por pieza

| Pieza | Por qué está ahí |
|---|---|
| HF Space | `<1 frase>` |
| HF Inference | `<1 frase>` |
| Qdrant Cloud | `<1 frase>` |
| Simulador de industria | `<1 frase>` |

## Qué falta para el siguiente avance

`<1-2 frases: trazabilidad (S9), evaluación (S10), o lo que corresponda>`
