# Rúbrica · Assignment A1 — 100 % del Módulo 1

> La cita `modulo-1-fundamentos/sesion-03-tools-api-externa/assignment-a1.md`. La usa el docente
> para calificar la sustentación del inicio de la Sesión 4 (`docente/esqueletos/sesion-03.md`,
> sección 7).
>
> **Vocabulario de los 4 niveles**, común a las rúbricas del curso: **Insuficiente** (no cumple
> el mínimo) · **Básico** (cumple lo mínimo, con huecos visibles) · **Competente** (cumple todo lo
> pedido, sin lujos) · **Sobresaliente** (cumple todo y además defiende decisiones no obvias).
>
> ⚠️ **El criterio de observabilidad de la rúbrica institucional no aplica todavía.** Langfuse
> entra recién en la Sesión 9. En este assignment, su lugar lo ocupa el criterio **Evidencia**:
> las 3 trazas de `EVIDENCIA-A1.md`, pegadas a mano, son el precursor de lo que en la S9 se leerá
> en Langfuse. No se penaliza a ningún equipo por no tener trazas de Langfuse en el A1.
>
> **Regla del piso, vigente aquí:** si `prueba_tool.py` pasa los 3 escenarios y la docstring
> cumple la regla A2 (verbo · cuándo usarla · cuándo NO), el equipo **no baja de Competente** en
> Funcionalidad, aunque en la sustentación en vivo el modelo no haya elegido la tool. Con 93 % de
> acierto por llamada, penalizar la varianza del modelo enseñaría exactamente lo contrario de lo
> que este curso quiere enseñar. Lo que sí se evalúa es si el equipo diseñó el sistema para que
> esa varianza no se convierta en un fallo silencioso.

---

## Los 5 criterios y su peso

| Criterio | Peso | Qué se mira |
|---|---|---|
| Funcionalidad | 30 % | Los 3 escenarios (éxito, dato inexistente, servicio caído) corren de punta a punta con el agente |
| Diseño de tool y prompt | 25 % | Docstring A2 (verbo · cuándo · cuándo NO), `args_schema` correcto, nombre claro |
| Manejo de errores | 25 % | Los errores están redactados para el modelo, no para un humano. Hay tope de iteraciones (A4) |
| Evidencia | 10 % | `EVIDENCIA-A1.md` con las 3 trazas reales, no descritas |
| Comunicación técnica | 10 % | La sustentación de 5 min explica la decisión, no narra el código |

---

## Funcionalidad — 30 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | El agente no completa ninguno de los 3 escenarios, o necesita intervención del docente |
| Básico | Completa el escenario de éxito; los de dato inexistente o servicio caído fallan o el agente reintenta sin control |
| Competente | Los 3 escenarios corren de punta a punta con el agente: responde citando el dato, no inventa ante el 404, y no entra en bucle ante el 503 |
| Sobresaliente | Además, resuelve correctamente el reto opcional (`?_fallo=malformado`), el más difícil porque no da código de error |

## Diseño de tool y prompt — 25 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | La tool no tiene `args_schema`, o la docstring no dice qué hace |
| Básico | Tiene `args_schema` y docstring, pero la docstring no dice "cuándo NO usarla" |
| Competente | Docstring completa (verbo, cuándo, cuándo NO — regla A2), `args_schema` con tipos y descripciones correctas, nombre que empieza con verbo |
| Sobresaliente | La docstring anticipa una confusión real de su track y la nombra explícitamente |

## Manejo de errores — 25 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | Un error de la API revienta como traceback, o el agente inventa un dato tras un 404 |
| Básico | Los errores se capturan, pero el mensaje está pensado para un log, no para que el modelo lo lea |
| Competente | Los 3 escenarios devuelven un mensaje redactado para el modelo (regla A3 del bloque 3 del `README.md`) y hay un tope de iteraciones explícito (A4) |
| Sobresaliente | El agente distingue explícitamente entre "no reintentar" (401, dato inexistente) y "se puede reintentar más tarde" (503) |

## Evidencia — 10 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | No hay `EVIDENCIA-A1.md`, o describe los escenarios sin trazas reales |
| Básico | Las 3 trazas están, pero incompletas (falta la entrada real o la salida real) |
| Competente | Las 3 trazas completas (entrada real, salida real) con una frase de qué se decidió en cada caso |
| Sobresaliente | Incluye también la traza del reto opcional (`?_fallo=malformado`) |

## Comunicación técnica — 10 %

| Nivel | Descriptor |
|---|---|
| Insuficiente | La sustentación se pasa del tiempo (5 min) o el equipo no puede explicar su propia tool |
| Básico | Cumple el tiempo, pero narra el código línea por línea en vez de explicar la decisión |
| Competente | Explica con claridad por qué la tool está diseñada así y qué pasó en los 3 escenarios |
| Sobresaliente | Conecta la tool con la separación "el modelo genera, tu código ejecuta" sin que se lo pidan |

---

## Cómo se calcula la nota final

Nota = suma ponderada de los 5 criterios, cada uno en escala 1 (Insuficiente) a 4
(Sobresaliente), sobre 4 — salvo que la regla del piso aplique, en cuyo caso el criterio de
Funcionalidad no baja de 3 (Competente) si `prueba_tool.py` y la docstring lo sostienen.
