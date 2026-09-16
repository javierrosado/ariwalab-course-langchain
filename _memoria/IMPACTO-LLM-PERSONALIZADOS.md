# Personalización por industria — evaluación e impacto

> **Estado: RESUELTO.** Se evaluó afinar un modelo por industria y se decidió **no hacerlo**.
> La personalización vive en el system prompt y en la base de conocimiento (camino A).
>
> Este documento conserva el análisis porque explica **por qué** se descartó el fine-tuning y
> qué riesgos concretos se evitaron. Es la justificación de la decisión D21.
>
> Fecha de la decisión: 2026-09-10 · Reemplaza la evaluación previa de dos caminos.

---

## 1. Qué se evaluó

La propuesta original era tener cuatro modelos afinados —uno por industria— desplegados en
Hugging Face, y usarlos como base de los laboratorios.

Se analizó su impacto sobre el curso y se encontró que **rompía dos narrativas pedagógicas** y
**multiplicaba por cuatro el riesgo técnico crítico**. Se descartó.

| Dimensión | Con fine-tuning | Sin fine-tuning *(elegido)* |
|---|---|---|
| Modelos a verificar | 4 | **1** |
| Endpoints a operar | 4 | **1** |
| Riesgo de perder tool calling | Real y difícil de detectar | **Cero** |
| Justificación del RAG (S5) | Comprometida | **Intacta** |
| Portabilidad a Foundry (bonus) | Rota | **Intacta** |
| Tiempo hasta poder construir | 2-3 semanas | **Inmediato** |
| Cambiar el tono de un agente | Reentrenar | Editar texto |

---

## 2. La regla de fondo que sostiene la decisión

```
              ¿Qué se le quiere dar al modelo?
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
      CONOCIMIENTO                  ESTILO
   tarifas · pólizas ·        tono · jerga del sector ·
   políticas · catálogos      formato · límites
             │                         │
             ▼                         ▼
      ✗ NO en los pesos          ✗ Tampoco hace falta
             │                    ponerlo en los pesos
             ▼                         ▼
    Base de conocimiento         System prompt
       (Qdrant Cloud)      (comun/prompts_industria.py)
```

**El 85 % de la sensación de "modelo especializado en seguros" la producen el system prompt y el
RAG.** El 15 % restante —matices de tono en los pesos— no justifica cuadruplicar el riesgo, el
costo y el trabajo de verificación.

---

## 3. Los dos riesgos pedagógicos que se evitaron

### 3.1 · La justificación del RAG

**El problema que habría existido.** La Sesión 5 enseña RAG agéntico: el agente decide *si*
necesita buscar. Con un modelo afinado en la industria, se rompía en dos niveles:

| Nivel | Qué pasaba |
|---|---|
| Pedagógico | El alumno pregunta *"¿para qué RAG si el modelo ya sabe?"* — y tenía razón |
| **Técnico** | **El modelo no llama al retriever.** El laboratorio directamente no funciona |

El nivel técnico tenía una causa mecánica precisa: un dataset de fine-tuning con conocimiento del
dominio enseña el patrón *"pregunta del dominio → respuesta directa"*, y **no** el patrón
*"pregunta del dominio → llamar al retriever → responder citando"*. No es resistencia del modelo:
es la distribución equivocada.

**Por qué ya no ocurre.** Un modelo base no conoce el tarifario de AndesMóvil ni el condicionado
de Andina Seguros. No tiene de dónde responder de memoria, así que recurre a la herramienta.

**Qué se conserva de todos modos.** La salvaguarda A6 sigue en el system prompt de las cuatro
industrias (bloque *"regla de fundamentación"*), y el criterio C6 sigue en la verificación. Son
defensa en profundidad, no redundancia inútil: obligan a citar la fuente, que es un requisito de
auditoría independiente de si el modelo sabe o no.

**Y la lección se mantiene entera.** El cuadro paramétrico vs recuperable sigue siendo el
contenido central de la Sesión 5:

| Criterio | Conocimiento **paramétrico** | Conocimiento **recuperable** |
|---|---|---|
| Actualizar el tarifario de mañana | Reentrenar el modelo | Reindexar un documento |
| Citar la fuente de una respuesta | Imposible | Obligatorio y verificable |
| Auditar por qué respondió eso | Caja negra | Traza + documento fuente |
| Control de acceso por usuario | No existe | Filtro por metadatos |
| Costo de un cambio | Alto | Casi cero |
| Conocer el *estilo* del dominio | Excelente | No aporta |

Se enseña como decisión de arquitectura —*"cuándo afinarías y cuándo recuperarías"*— apoyada en
la demo del cambio en caliente: preguntar una tarifa, cambiar el documento en Qdrant, volver a
preguntar y ver la respuesta nueva con su cita.

### 3.2 · La portabilidad a Foundry

**El problema que habría existido.** El bonus prometía *"cambias `AI_PROVIDER=foundry` y el resto
del código no se toca"*. Esa promesa se apoya en una ambigüedad:

```
   provider.py abstrae la INTERFAZ          ✅ eso sí porta
   provider.py NO abstrae el COMPORTAMIENTO ❌ eso no porta
```

Con un modelo afinado que solo existe en Hugging Face, apuntar a Foundry cambiaba el **cerebro**
del agente: mismo código, otro comportamiento. Si se le dice al alumno *"no cambió nada"* mientras
él ve respuestas distintas en pantalla, detecta la mentira. Una lección refutable mirando la
salida es peor que no darla.

**Por qué ya no ocurre.** Con el camino A, la personalización vive en el system prompt y en
Qdrant. **Ambos portan perfectamente.** El mismo prompt y la misma colección funcionan contra
Foundry, así que la promesa vuelve a ser literalmente cierta.

**Beneficio adicional:** desaparece la necesidad de publicar cuatro modelos custom en Azure, que
habría contradicho la decisión de que el bonus sea opcional, asíncrono y sin fricción.

---

## 4. Riesgos que se disolvieron

| # | Riesgo evaluado | Estado |
|---|---|---|
| R1 | Tool calling: había que verificar 4 modelos afinados | 🟢 **Resuelto**: un solo modelo (`Qwen3-32B`), verificado empíricamente el 2026-09-10 |
| R10 | Structured output degradado por el fine-tuning | 🟢 **Disuelto** |
| R11 | Heterogeneidad entre tracks: 4 modelos con comportamientos distintos | 🟢 **Disuelto**: un modelo, cuatro prompts |
| R12 | El modelo afinado no llama al RAG | 🟢 **Muy reducido**: se conserva A6 y C6 por auditoría |
| R13 | El corpus del fine-tuning contradice los datasets del curso | 🟢 **Disuelto** |
| — | Costo de 4 endpoints dedicados | 🟢 **Disuelto** |
| — | 4 despliegues de GPU en Azure para el bonus | 🟢 **Disuelto** |

Siete riesgos eliminados o reducidos por una sola decisión de diseño.

---

## 5. Lo que sí sigue siendo cierto

La **fiabilidad compuesta** condiciona el curso, y eso **no cambia** con el camino A ni con el
cambio de modelo. Las seis reglas de calibración siguen vigentes:

| # | Regla |
|---|---|
| A1 | 3-4 tools enlazadas por agente, nunca 6 |
| A2 | Docstrings con verbo + cuándo usarla + **cuándo NO** |
| A3 | `with_structured_output()` con validación y un reintento |
| A4 | Tope duro de iteraciones + errores de tool redactados para el modelo |
| A5 | Few-shot en los prompts críticos |
| A6 | Obligar a recuperar ante afirmaciones sobre tarifas o coberturas |

> **A2 no es una concesión, es una mejora del curso.** Un modelo enorme perdona descripciones
> ambiguas y el alumno nunca descubre por qué importan. Con un margen estrecho, diseñar bien las
> herramientas deja de ser opcional — que es exactamente lo que un curso de agentes debe enseñar.

---

## 6. Si en una segunda edición se quiere afinar

No está descartado para siempre: está descartado **para la primera edición**, donde el objetivo
es que el curso funcione y no se retrase.

La especificación técnica para hacerlo sin romper nada —hiperparámetros de LoRA, composición del
dataset, verificación del `chat_template`— se conserva en el apéndice de
[`ESPEC-MODELOS-INDUSTRIA.md`](ESPEC-MODELOS-INDUSTRIA.md).

La condición que no se puede romper, en cualquier edición futura: **el dataset de fine-tuning no
debe contener tarifas, coberturas ni políticas.** Eso vive en el RAG, y si el modelo lo memoriza
se rompe a la vez el criterio C6 y la lección central de la Sesión 5.
