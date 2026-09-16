# Esqueleto · Bonus — El mismo agente en Microsoft Foundry

> Contrato del bloque bonus. Insumo de la sesión de Claude Code que escribe la Fase 6.
> No es material de alumno.
>
> Decidido con Javier el 2026-09-16 · Módulo 4 · **fuera de las 72 h**

---

## 1. Ficha

| Campo | Valor |
|---|---|
| Carpeta destino | `modulo-4-plus-foundry/` |
| Cuándo | **Asíncrono**, liberado al cerrar la S11 |
| Horas | ~2 h teoría · ~4 h práctica ≈ 6 h · **no computan horas lectivas** (D17) |
| Laboratorio | **L12 · El mismo agente en Foundry** |
| Evaluación | **No ponderado.** Certificación adicional |
| Estado en el mapeo | `COMPLETA` — repo `09-deploy-to-microsoft-foundry` |

> **Por qué es bonus y no sesión.** La malla oficial son 72 h y añadir una sesión formal la llevaba
> a 78, lo que exigía aprobación académica (D17 v2). Como bloque asíncrono, la malla queda intacta
> y el alumno que quiera lo hace a su ritmo. Habrá un **Curso 2 que es 100 % Foundry**: este bloque
> es el puente, no el sustituto.

---

## 2. La lección, en una línea

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

> **Esta promesa es literalmente cierta gracias a D21.** Si el curso hubiera afinado un modelo por
> industria, apuntar a Foundry habría cambiado el cerebro del agente y la frase "no cambió nada"
> habría sido refutable mirando la pantalla. Conviene decirlo en el bloque: es la consecuencia
> práctica de una decisión de diseño tomada en la semana 0.

---

## 3. Objetivos

1. Situar el **modelo de recursos de Azure**: suscripción → grupo → recurso → proyecto → deployment.
2. Ejecutar el mismo agente contra Foundry cambiando **una variable de entorno**.
3. Explicar qué es un *hosted agent* y el protocolo **Responses**.
4. Desplegar con `azd` y obtener un endpoint gestionado.
5. **Comparar con evidencia** Hugging Face y Foundry en 7 dimensiones.

---

## 4. Acceso a Azure · decidido: ambas vías, documentadas

| Vía | Para quién | Qué implica |
|---|---|---|
| **A · Suscripción propia** *(recomendada)* | Quien pueda registrar una tarjeta | Usa el crédito inicial gratuito. Aprende el modelo de recursos completo — que es **prerrequisito del Curso 2** — y queda con su propio entorno |
| **B · Proyecto del docente** | Quien no quiera o no pueda registrar tarjeta | Javier despliega un proyecto y reparte claves temporales. Se salta la parte de creación de recursos: se lee, no se hace |

> **Es la primera y única vez que el curso menciona una tarjeta de crédito.** Hay que decirlo sin
> rodeos en la primera línea del bloque, junto con la vía B, para que nadie llegue a la mitad de la
> guía y se encuentre con el muro. Las 11 sesiones lectivas siguen sin pedir tarjeta: el principio
> P2 se mantiene íntegro dentro de las 72 h.

### Operación de la vía B

| Qué | Detalle |
|---|---|
| Quién paga | Javier, con el consumo del proyecto compartido |
| Claves | Temporales, rotadas al cerrar el periodo del bonus |
| Límite | Un `deployment` pequeño; se anuncia la cuota disponible |
| Qué se pierde | La creación de recursos. Se sustituye por un recorrido guiado del portal, en capturas |

---

## 5. Estructura del bloque · autoguiado

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

≈ 2 h teoría · 4 h práctica.

### Paso 4 — el momento del bloque

Se hace **antes** de todo lo de hosting, y a propósito: es el paso más corto y el más revelador.

```
   1.  Correr la batería de 5 consultas del track contra HF     → anotar respuestas
   2.  Cambiar UNA línea del .env
   3.  Correr LA MISMA batería contra Foundry                   → anotar respuestas
   4.  Comparar: el código es idéntico, la infraestructura no, el comportamiento difiere un poco
```

**La pregunta que cierra el paso:** *¿qué habría hecho falta cambiar si el agente hubiera
instanciado `ChatOpenAI` directamente en cada archivo?* La respuesta —11 laboratorios— es el
argumento entero a favor de la indirección que arrastran desde el L1 sin entender del todo por qué.

---

## 6. El entregable · cuadro comparativo

Es lo que acredita el bonus, junto con el agente corriendo. **7 dimensiones**, con evidencia
propia, no copiada de documentación:

| Dimensión | Cómo se mide |
|---|---|
| **Latencia** | La misma batería de 5 consultas en ambos: p50 de cada uno |
| **Costo** | Costo por ejecución en cada plataforma, con la fórmula |
| **Calidad de respuesta** | Las 5 respuestas lado a lado: ¿cuál sirve mejor y por qué? |
| **Soberanía del dato** | Dónde corre el modelo, bajo qué jurisdicción, qué se puede auditar |
| **Portabilidad** | Qué habría que cambiar para volver. Medido en archivos tocados |
| **Curva de puesta en marcha** | Minutos desde cero hasta la primera respuesta, cronometrados |
| **Dependencia del proveedor** | Qué queda atado y qué no |

> **Ninguna dimensión tiene un ganador predeterminado, y el bloque no debe insinuarlo.** Foundry
> gana en gobernanza e integración corporativa; el stack abierto gana en costo y portabilidad. Un
> alumno que termine el bonus creyendo que una de las dos es "la buena" no aprendió a decidir:
> aprendió una preferencia. El objetivo es que sepa **en qué contexto elegiría cada una**.

---

## 7. Criterio de acreditación

| Requisito | Evidencia |
|---|---|
| El agente responde desde Foundry | Captura de las 5 consultas con `AI_PROVIDER=foundry` |
| Se desplegó como *hosted agent* | Salida de `azd up` y el endpoint respondiendo |
| Cuadro comparativo completo | Las 7 dimensiones con datos propios medidos |

**No ponderado.** No afecta ninguna nota del curso. Quien lo complete recibe la certificación
adicional; quien no, se gradúa igual.

---

## 8. Riesgo abierto

| Riesgo | Estado | Qué hacer |
|---|---|---|
| **R8** · `langchain-azure-ai[hosting]` en versión preview | Marcado como resuelto en el ADR, pero **el bonus depende de él** | **Re-verificar antes de liberar el bloque.** Una API en preview cambia entre versiones, y el `ResponsesHostServer` es el núcleo de los pasos 6 y 7 |
| Cuota del proyecto compartido (vía B) | Sin medir | Anunciar el límite y cerrar el periodo del bonus con fecha |
| El crédito gratuito de Azure cambia de condiciones | Fuera de control | La guía nombra el concepto, no la cifra: las cifras caducan |

---

## 9. Qué **no** entra

| No entra | Va en |
|---|---|
| Azure AI Search, Cosmos, Functions, APIM | **Curso 2** |
| Redes, identidad gestionada, políticas de Azure | Curso 2 |
| Comparar precios con cifras concretas | Caducan: se enseña la fórmula, no el número |
| Migrar Qdrant o Langfuse a servicios de Azure | Curso 2. Aquí se demuestra que **no hace falta** |

> **El bonus termina donde empieza el Curso 2, y conviene decirlo explícitamente al cerrar**: aquí
> se movió el modelo; allá se moverá todo lo demás, recurso por recurso.

---

## 10. Archivos a producir

| Archivo | Contenido |
|---|---|
| `README.md` | Los 8 pasos, con el diagrama del switch y la advertencia de la tarjeta en la primera línea |
| `acceso-azure.md` | Las dos vías, paso a paso, con capturas del portal |
| `host/main.py` | `ResponsesHostServer` envolviendo el agente del L11 |
| `host/azure.yaml` | Configuración de `azd` |
| `plantilla-comparativa.md` | Las 7 dimensiones, con cómo medir cada una |
| `puente-curso-2.md` | Qué sigue y por qué se dejó fuera de aquí |

### Tareas previas

| # | Tarea | Por qué |
|---|---|---|
| am | **Re-verificar `langchain-azure-ai[hosting]`** contra un proyecto Foundry real | R8: es preview y sostiene los pasos 6 y 7 |
| an | Desplegar el proyecto Foundry compartido de la vía B y definir su cuota | Sin él, la vía B no existe |
| ao | Capturas del portal de Azure para `acceso-azure.md` | Es lo que sustituye a la creación de recursos en la vía B |
| ap | Definir la fecha de cierre del periodo del bonus | Las claves temporales necesitan vencimiento |
