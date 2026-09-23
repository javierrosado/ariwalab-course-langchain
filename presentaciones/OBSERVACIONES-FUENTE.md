# Observaciones de fidelidad y recomendaciones

Fuente analizada: `27c24090f1662f9473b673d2020e7bffee04490b`. Estas observaciones no modifican el material del repositorio.

## Precisiones incorporadas

1. **Calendario.** Las doce sesiones lectivas corresponden a S1–S11 más el Seminario Internacional. Preparación y Foundry se presentan aparte. Algunas frases del bonus mencionan once sesiones al hablar de las 72 horas; se sigue la estructura del cronograma docente.
2. **Memoria de L5.** `solucion/*/memory.py` conserva listas en un diccionario del proceso por `thread_id`. Las diapositivas no lo representan como una base persistente ni como un checkpointer duradero.
3. **Foundry: switch frente a hosting.** El README resume la portabilidad de los guardrails; `host/main.py` explica que memoria y guardrails del bucle manual requieren adaptación al grafo alojado. Las diapositivas separan ambos escenarios.
4. **Demo de middleware.** `code/04_middleware.py` se presenta como ejemplo de tres controles, pero su wrapper engancha entrada y salida. La solución del laboratorio aplica `check_action` dentro del bucle. Se muestra esa diferencia.
5. **Percentiles.** El ejemplo de p95 con diez observaciones da 21.000 ms con rango más próximo. Otros métodos interpolan. p95 no significa máximo en general. El promedio de la muestra es 2.820 ms.
6. **Groundedness.** `comun/evaluadores.py` comprueba presencia del dato esperado en respuesta y contexto. No valida semánticamente toda la afirmación ni identifica una cita completa. Se explica un falso positivo posible con una negación.
7. **Chunking.** El tamaño grande no garantiza conservar toda idea. Los parámetros se describen como configuración del splitter, sin convertir automáticamente sus unidades en tokens.
8. **Fiabilidad compuesta.** Multiplicar tasas es un modelo ilustrativo sujeto a las condiciones del cálculo; no demuestra independencia ni representa una medición universal del modelo.
9. **Instrucciones y garantías.** A6 exige recuperar y citar desde el prompt; su presencia no demuestra cumplimiento en cada ejecución. Los guardrails por patrones y las pruebas finitas tampoco prueban seguridad universal.
10. **Derivación humana.** Un mensaje de derivación en el checkpoint no acredita una integración real con una persona o sistema de tickets. Se distingue aviso, política y efecto externo.
11. **Bonus azd.** El README menciona `azd up` en pasos o acreditación y también presenta `provision` / `deploy`. Las PPTX muestran los comandos del material y explicitan que la configuración y la integración en preview deben comprobarse en el entorno del docente.

## Recomendaciones pedagógicas

- Usar los tres slides como una secuencia de pregunta, comprobación y aplicación. Pedir una predicción antes de revelar el resultado del ejemplo.
- Hacer que cada equipo traduzca un ejemplo de otra industria a su track y explique qué cambia y qué permanece.
- Distinguir siempre resultados ilustrativos, salidas simuladas y mediciones del laboratorio.
- Conservar el fallo inicial y la prueba posterior: ayudan a explicar decisiones sin fingir fiabilidad perfecta.
- Usar notas y capítulos como banco modular. La cantidad de láminas no obliga a ampliar la duración del curso.
- En S11 y el seminario, pedir alternativa descartada, criterio y consecuencia antes de aceptar una lista de tecnologías como argumento.

## Alcance de la verificación de entrega

Se verifican estructura PPTX, cantidad de diapositivas, presencia de notas y tablas nativas, geometría y representación de las presentaciones. La revisión de contenido se basa en la revisión indicada del repositorio; no ejecuta llamadas a modelos, pruebas en cuentas del alumno ni despliegues nuevos. No se ha realizado una sesión de edición manual en Microsoft PowerPoint.
