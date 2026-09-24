# Sesión 0 · Nivelación en modelos de lenguaje

> **Obligatoria y asíncrona.** Se completa antes de la Sesión 1.
> Duración estimada: **4 a 5 horas**, repartibles en varios días.
> No computa dentro de las 66 horas lectivas: es preparación.

---

## Por qué existe esta sesión

Este curso está diseñado para **ingenieros de software**. Se asume que dominas Python, REST,
git y línea de comandos. **No se asume nada sobre modelos de lenguaje.**

Esa asimetría es deliberada y trae un riesgo concreto: un ingeniero con experiencia tiende a
tratar al LLM como una API más — determinística, con contrato estable y errores predecibles.
No lo es. Esta sesión existe para romper esa expectativa **antes** de que te cueste un
laboratorio.

---

## Qué vas a poder hacer al terminar

- [ ] Explicar qué es un token y por qué determina el costo y los límites de tu aplicación
- [ ] Predecir por qué el mismo prompt puede dar dos respuestas distintas
- [ ] Explicar qué es un embedding y por qué permite buscar por significado
- [ ] Reconocer una alucinación y explicar por qué el modelo no sabe que está alucinando
- [ ] Estimar el costo aproximado de una conversación
- [ ] Tener las **3 cuentas del curso** creadas y funcionando
- [ ] Tener tu entorno de Python listo y el `.env` configurado
- [ ] Aprobar la autoevaluación con **80 % o más**

> ⚠️ **La autoevaluación es bloqueante.** Sin 80 % no entras a la sesión síncrona 1.
> No es un trámite: cada pregunta corresponde a algo que se usa desde el primer laboratorio.

---

## Ruta de estudio

Sigue este orden. Cada paso supone el anterior.

| # | Paso | Archivo | Tiempo |
|---|------|---------|--------|
| 1 | Leer los fundamentos de LLM | [`conceptos-previos/fundamentos-llm.md`](conceptos-previos/fundamentos-llm.md) | 60 min |
| 2 | Consultar el glosario según lo necesites | [`../recursos/glosario.md`](../recursos/glosario.md) | — |
| 3 | Preparar Python y el entorno | [`conceptos-previos/python-y-entorno.md`](conceptos-previos/python-y-entorno.md) | 45 min |
| 4 | Crear las 3 cuentas del curso | [`conceptos-previos/alta-de-cuentas.md`](conceptos-previos/alta-de-cuentas.md) | 40 min |
| 5 | Ejecutar las 4 demos | [`code/`](code/) | 60 min |
| 6 | Resolver la autoevaluación | [`autoevaluacion.md`](autoevaluacion.md) | 30 min |

---

## Las 4 demos

No son ejercicios de escribir código: son experimentos para **ver** el comportamiento del que
habla la teoría. Ejecuta cada uno y observa la salida antes de seguir.

| Demo | Qué demuestra | Qué deberías notar |
|------|---------------|--------------------|
| `01_tokens.py` | Cómo se parte el texto en tokens | Que el español cuesta más tokens que el inglés |
| `02_temperatura.py` | El mismo prompt con distintas temperaturas | Que a temperatura 0 las respuestas se parecen mucho, y a 1.5 divergen |
| `03_embeddings.py` | Cercanía semántica entre frases | Que dos frases sin palabras en común pueden estar muy cerca |
| `04_costo.py` | Estimación de costo de una conversación | Que el historial es lo que encarece, no la última pregunta |

La demo 4 corre **sin conexión y sin credenciales**. La demo 1 tampoco necesita credenciales,
pero descarga el tokenizador la primera vez. Las demos 2 y 3 requieren tu token de Hugging Face,
que obtienes en el paso 4.

---

## Las 3 cuentas del curso

Todas tienen plan gratuito y **ninguna pide tarjeta de crédito**.

| Servicio | Para qué se usa | Desde qué sesión |
|----------|-----------------|------------------|
| **Hugging Face** | Modelo de chat y embeddings | Sesión 1 |
| **Qdrant Cloud** | Base vectorial del RAG | Sesión 5 |
| **Langfuse Cloud** | Trazabilidad y evaluación | Sesión 9 |

> **Créalas las tres ahora**, aunque dos no se usen hasta la mitad del curso. Un equipo que
> deja la cuenta de Qdrant para la semana 5 llega a esa sesión sin poder hacer el laboratorio.

⚠️ **Sobre Langfuse:** el plan gratuito admite **2 usuarios por proyecto**. Por eso los equipos
del curso son de 2 personas. Verifica esto con tu compañero antes de la Sesión 1.

---

## Qué NO necesitas instalar

Este curso es **100 % en línea**. En tu máquina solo corre Python y tu editor.

| No necesitas | Por qué |
|--------------|---------|
| GPU | Los modelos corren en la nube de Hugging Face |
| Docker | Solo escribirás un `Dockerfile` en la sesión 8; lo construye la plataforma |
| Ollama o LM Studio | No se usan modelos locales |
| Base de datos | Qdrant es gestionado |
| Ninguna herramienta de Azure | Solo en el bonus opcional del final |

---

## Errores frecuentes en esta sesión

| Síntoma | Causa habitual | Solución |
|---------|----------------|----------|
| `ModuleNotFoundError` | El entorno virtual no está activado | Reactiva el `venv` antes de ejecutar |
| `401 Unauthorized` en Hugging Face | El token no tiene permiso de inferencia | Regenera el token marcando ese permiso |
| El `.env` no se lee | Está en otra carpeta que la raíz del curso | Debe estar en la raíz, junto a `requirements.txt` |
| Acentos rotos en la consola de Windows | Codificación de la terminal | `chcp 65001` antes de ejecutar |
| La demo 2 tarda mucho la primera vez | Arranque en frío del endpoint | Es normal: reintenta a los 2 minutos |

---

## Cuando termines

Avisa al docente que completaste la autoevaluación. Llegas a la Sesión 1 con:

- [ ] Entorno de Python funcionando
- [ ] `.env` con tu token de Hugging Face
- [ ] Las 3 cuentas creadas
- [ ] Las 4 demos ejecutadas
- [ ] La autoevaluación aprobada
- [ ] Una idea de qué industria te interesa: **telecomunicaciones, banca, retail o seguros**

Esa última decisión la formalizas en el Laboratorio 1, y te acompaña hasta el proyecto final.
