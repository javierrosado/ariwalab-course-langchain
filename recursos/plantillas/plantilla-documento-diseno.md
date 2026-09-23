# Documento de diseño — [equipo] · [track]

> Plantilla del entregable de la Sesión 11 (tarea ae de
> `docente/esqueletos/sesion-11.md`), citada desde
> `modulo-3-produccion/sesion-11-sustentacion-final/README.md` y su `lab/README.md`. Vive en
> `recursos/plantillas/` porque es un archivo compartido, igual que las rúbricas y el golden
> set — no un archivo propio de esa sesión. 4 páginas, no más. Completa cada sección con
> información real de tu proyecto — borra las instrucciones entre `< >`.

---

## 1 · Caso de uso

**Qué resuelve:** `<1-2 frases>`

**Para quién:** `<el perfil del cliente que usaría este agente>`

**Qué NO resuelve** (igual de importante que lo anterior): `<1-2 frases>`

---

## 2 · Arquitectura

```
   [ cliente web (L11) ]
           │ HTTPS + X-API-Key
           ▼
   [ API — FastAPI (L8) ]
           │
           ▼
   [ agente — bucle + guardrails (L4-L6) ]
           │
     ┌─────┼──────────────┬─────────────┐
     ▼     ▼               ▼             ▼
   [ HF Inference ]  [ Qdrant Cloud ]  [ Simulador de industria ]
```

Reemplaza el diagrama si tu arquitectura real difiere. Señala en el diagrama (o en una nota
debajo) dónde vive la observabilidad (L9) y dónde se aplican los guardrails (L6).

---

## 3 · Decisiones (5, con alternativa descartada y criterio)

| # | Decisión | Alternativa descartada | Criterio |
|---|---|---|---|
| 1 | `<qué elegiste>` | `<qué NO elegiste>` | `<por qué>` |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Una decisión útil nombra una alternativa real que consideraron. "Usamos X" no es una decisión;
"usamos X y no Y porque Z" sí lo es (ver el `README.md` de la Sesión 11, §0 — "Cómo se
argumenta ante un panel").

---

## 4 · Evidencia

| Qué | Dato |
|---|---|
| Métricas del L10 (v1 vs v2) | `<tabla o resumen>` |
| Cuellos de botella del L9 | `<los 2, con el número que los evidencia>` |
| Qué se haría con una semana más | `<1-2 frases — decir qué falta es señal de que entendieron el sistema>` |
