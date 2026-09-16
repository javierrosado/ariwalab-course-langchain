# Bonus — El mismo agente en Microsoft Foundry

> **Antes de empezar: esta es la primera y única vez que el curso menciona una tarjeta de
> crédito.** La Vía A (abajo) usa el crédito inicial gratuito de Azure, pero requiere
> registrar una tarjeta. Si no puedes o no quieres, usa la **Vía B**: el docente despliega un
> proyecto compartido y reparte claves temporales — te saltas la creación de recursos, pero
> puedes hacer todo lo demás. Las 11 sesiones lectivas del curso siguen sin pedir tarjeta: el
> principio P2 se mantiene íntegro dentro de las 72 h.

**Asíncrono, liberado al cerrar la S11. No ponderado — certificación adicional.**
~2 h teoría · ~4 h práctica ≈ 6 h, que **no computan** horas lectivas (decisión D17).

---

## La lección, en una línea

Todo el curso se construyó para que este bloque sea **aburrido**:

```
   .env:   AI_PROVIDER=huggingface   ──────►   AI_PROVIDER=foundry

   Y no se toca ni una línea del código del agente.
```

| Pieza | ¿Porta? | Por qué |
|---|---|---|
| `comun/provider.py` | ✅ | Abstrae la interfaz desde el L1 (D13) |
| System prompt del track | ✅ | Es texto (D21 · camino A) |
| Colección de Qdrant | ✅ | Es un servicio externo, no depende del proveedor del modelo |
| Las 4 tools + retriever | ✅ | Solo hablan HTTP con el simulador |
| Guardrails | ✅ | Código propio |
| **El comportamiento del modelo** | ⚠️ **No** | Otro modelo responde distinto. Es lo único que cambia, y es el contenido del cuadro comparativo |

**Esta promesa es literalmente cierta gracias a D21.** Si el curso hubiera afinado un modelo por
industria, apuntar a Foundry habría cambiado el cerebro del agente y "no cambió nada" habría sido
refutable mirando la pantalla. Es la consecuencia práctica de una decisión de diseño tomada en la
semana 0.

---

## Objetivos

1. Situar el **modelo de recursos de Azure**: suscripción → grupo → recurso → proyecto → deployment.
2. Ejecutar el mismo agente contra Foundry cambiando **una variable de entorno**.
3. Explicar qué es un *hosted agent* y el protocolo **Responses**.
4. Desplegar con `azd` y obtener un endpoint gestionado.
5. **Comparar con evidencia** Hugging Face y Foundry en 7 dimensiones.

---

## Los 8 pasos

| # | Paso | Tipo | Tiempo |
|---|---|---|---|
| 1 | Qué es Foundry y el modelo de recursos de Azure | T | 30 min |
| 2 | Elegir vía de acceso y preparar credenciales | P | 30 min |
| 3 | Crear el *deployment* del modelo y anotar las variables | P | 30 min |
| 4 | **El switch**: `AI_PROVIDER=foundry` y correr el mismo agente | P | 30 min |
| 5 | *Hosted agent* y el protocolo Responses | T | 45 min |
| 6 | Envolver el agente con `ResponsesHostServer` | P | 45 min |
| 7 | Desplegar con `azd up` | P | 45 min |
| 8 | **El cuadro comparativo** | T | 45 min |

Ver [`acceso-azure.md`](acceso-azure.md) para los pasos 1-3.

### Paso 4 — el momento del bloque

Se hace **antes** de todo lo de hosting, y a propósito: es el paso más corto y el más revelador.

```
   1.  Correr la batería de 5 consultas del track contra HF     → anotar respuestas
   2.  Cambiar UNA línea del .env
   3.  Correr LA MISMA batería contra Foundry                   → anotar respuestas
   4.  Comparar: el código es idéntico, la infraestructura no, el comportamiento difiere un poco
```

**La pregunta que cierra el paso:** ¿qué habría hecho falta cambiar si el agente hubiera
instanciado `ChatOpenAI` directamente en cada archivo? La respuesta —11 laboratorios— es el
argumento entero a favor de la indirección que arrastras desde el L1 sin haber entendido del
todo por qué.

### Pasos 5-7 — *hosted agent*

`ResponsesHostServer` (paquete `langchain-azure-ai[hosting]`, en preview) envuelve un grafo de
LangGraph y lo expone por `/responses`, con streaming, historial y sesiones ya resueltos por la
plataforma. Ver [`host/main.py`](host/main.py) — reutiliza `comun.provider.get_chat_model()` y
las tools del L4/L5 tal cual, y documenta explícitamente qué NO porta sin cambios (los
guardrails del L6, escritos como una función Python, no como un grafo).

Despliegue con Azure Developer CLI:

```bash
azd ext install azure.ai.agents
azd auth login
azd ai agent run          # corre local, contra tu deployment de Foundry
azd provision             # si necesitas crear recursos nuevos
azd deploy                # empaqueta y despliega el hosted agent
```

Ver [`host/azure.yaml`](host/azure.yaml) para la configuración completa.

---

## El entregable: cuadro comparativo

Ver [`plantilla-comparativa.md`](plantilla-comparativa.md) — 7 dimensiones, con evidencia
propia medida por ti, no copiada de documentación. **Ninguna dimensión tiene un ganador
predeterminado**: Foundry gana en gobernanza e integración corporativa; el stack abierto gana en
costo y portabilidad. El objetivo es que sepas **en qué contexto elegirías cada una**, no que
memorices cuál es "la buena".

---

## Criterio de acreditación

| Requisito | Evidencia |
|---|---|
| El agente responde desde Foundry | Captura de las 5 consultas con `AI_PROVIDER=foundry` |
| Se desplegó como *hosted agent* | Salida de `azd up` y el endpoint respondiendo |
| Cuadro comparativo completo | Las 7 dimensiones con datos propios medidos |

**No ponderado.** No afecta ninguna nota del curso. Quien lo complete recibe la certificación
adicional; quien no, se gradúa igual.

---

## Qué NO entra

| No entra | Va en |
|---|---|
| Azure AI Search, Cosmos, Functions, APIM | **Curso 2** |
| Redes, identidad gestionada, políticas de Azure | Curso 2 |
| Comparar precios con cifras concretas | Caducan: se enseña la fórmula, no el número |
| Migrar Qdrant o Langfuse a servicios de Azure | Curso 2. Aquí se demuestra que **no hace falta** |

El bonus termina donde empieza el Curso 2 — ver [`puente-curso-2.md`](puente-curso-2.md).
