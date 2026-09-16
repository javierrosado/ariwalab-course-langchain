# Rúbrica · Proyecto M2 — 100 % del Módulo 2

> La cita `modulo-2-agentes-avanzados/sesion-07-hackathon-m2/proyecto-m2.md`. La usa el docente
> para calificar la sustentación de la Sesión 7 (`docente/esqueletos/sesion-07.md`, sección 6).
>
> **Vocabulario de los 4 niveles**, común a las rúbricas del curso: **Insuficiente** (no cumple
> el mínimo) · **Básico** (cumple lo mínimo, con huecos visibles) · **Competente** (cumple todo lo
> pedido, sin lujos) · **Sobresaliente** (cumple todo y además defiende decisiones no obvias).
>
> **Regla del piso, vigente aquí** (heredada del Assignment A1, `sesion-03.md`, adaptada por
> `sesion-07.md` §6): si `tests/` pasa invocando el agente directamente y `INFORME-L7.md`
> documenta los 10 casos con evidencia real, el equipo **no baja de Competente** aunque el caos
> le arruine un turno en la demo en vivo. Un sistema no determinístico se juzga por su diseño y
> su evidencia, no por una sola ejecución.

---

## Los 5 criterios y su peso

| Criterio | Peso | Qué se mira |
|---|---|---|
| Funcionalidad | 25 % | El agente resuelve el caso de uso con tools + RAG + memoria, con el caos activo |
| Diseño de tools y prompts | 20 % | Las 4 tools, el retriever, el system prompt del track |
| Guardrails y manejo de errores | 25 % | 0 filtraciones se sostiene (L6), y los 4 tipos de caso borde del L7 están cubiertos |
| Evidencia de pruebas | 20 % | `INFORME-L7.md` con ≥ 10 casos reales, no descritos. Las pruebas de `tests/` corren |
| Comunicación técnica | 10 % | La demo y la defensa del documento de diseño |

---

## Funcionalidad — 25 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | El agente no completa el caso de uso, o necesita que el docente intervenga para que funcione |
| Básico | Resuelve el camino feliz; con `CHAOS_RATE=0.1` activo pierde el hilo de la conversación o repite pasos |
| Competente | Resuelve el caso de uso con las 4 tools + RAG + memoria funcionando juntos, y sobrevive a la mayoría de fallos del caos sin perder el hilo |
| Sobresaliente | Además de lo anterior, el agente **explica** al usuario cuando algo falló ("el sistema no respondió, ¿lo intento de nuevo?") en vez de fallar en silencio o inventar una respuesta |

## Diseño de tools y prompts — 20 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | Alguna tool no tiene `args_schema`, o el system prompt no usa `get_system_prompt(track)` |
| Básico | Las 4 tools funcionan, pero al menos una docstring no dice "cuándo NO usarla" (regla A2) |
| Competente | Las 4 tools núcleo + el retriever cumplen A2, y el system prompt del track está intacto (identidad, jerga, límites, A6) |
| Sobresaliente | El equipo puede señalar, con la matriz de `docente/matriz_seleccion.py`, exactamente qué docstring corrigieron y por qué subió el acierto |

## Guardrails y manejo de errores — 25 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | Hay al menos una filtración de los 15 ataques del L6 sin corregir, o ningún caso borde del L7 está cubierto |
| Básico | 0 filtraciones del L6 se sostiene, pero el L7 solo cubre 1 o 2 de las 4 familias de caso borde |
| Competente | 0 filtraciones se sostiene y las 4 familias de caso borde (entrada ambigua, dato ausente, servicio caído, salida fuera de formato) están cubiertas con al menos 2 casos cada una |
| Sobresaliente | Además, el escalamiento a humano se dispara correctamente y el equipo explica la diferencia entre el adversario deliberado del L6 y el entorno sin malicia del L7 |

## Evidencia de pruebas — 20 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | `INFORME-L7.md` describe menos de 10 casos, o los describe sin trazas reales ("probamos varios escenarios y funcionó") |
| Básico | 10 casos documentados, pero concentrados en 1 o 2 familias, o `tests/` no corre sin intervención manual |
| Competente | ≥ 10 casos, al menos 2 por familia, con traza real (entrada, salida, qué se cambió) y `tests/` corre de punta a punta con invariantes (no `assert ==`) |
| Sobresaliente | El informe abre con el peor fallo encontrado y resuelto (no con el camino feliz), como pide `sesion-07.md` §7 |

## Comunicación técnica — 10 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | La demo se pasa del tiempo asignado o el equipo no puede explicar una decisión de arquitectura básica |
| Básico | Cumple el tiempo, pero las respuestas a preguntas técnicas son vagas ("lo hicimos así porque sí") |
| Competente | Cumple el tiempo y defiende con claridad las 4 tools, el RAG y los guardrails ante preguntas del panel |
| Sobresaliente | Además, conecta sus decisiones con las restricciones del curso (P1–P6, D20, A1–A6) sin que se lo pidan |

---

## Cómo se calcula la nota final

Nota = suma ponderada de los 5 criterios, cada uno en escala 1 (Insuficiente) a 4 (Sobresaliente),
sobre 4, salvo que la **regla del piso** aplique — en ese caso el criterio de Funcionalidad no
puede quedar por debajo de Competente (3) si la evidencia de `tests/` e `INFORME-L7.md` lo
sostiene, aunque la demo en vivo haya salido mal por el caos.
