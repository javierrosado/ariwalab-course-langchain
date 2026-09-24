# Validación de la revisión

Fecha: 2026-09-24. Rama autorizada: `feature/curso-final`. Revisión sobre el árbol de trabajo,
conservando los cambios previos de finales de línea. No se modificó `main` ni se hizo merge.

## Alcance y límites

Inventario inicial de 425 archivos: 201 Markdown, 183 Python, 16 CSV, 10 JSON y configuración.
Se recorrieron los cuatro módulos, S0, S1–S11, seminario, bonus y recursos compartidos.
La revisión estructural abarca todo el inventario; el análisis semántico se concentra en
progresión, teoría, checkpoints, laboratorios, evaluaciones y las inconsistencias documentadas.
No equivale a una certificación exhaustiva de todos los caminos de ejecución.

La validación sintáctica no ejecuta Python. La validación Markdown comprueba enlaces inline
locales y anclas; omite bloques de código y URLs externas. No comprueba automáticamente
referencias textuales en backticks ni toda variante de sintaxis Markdown. Los enlaces externos
consultados para contrastar APIs figuran en el reporte de consistencia; no se afirma haber
comprobado disponibilidad de todas las URLs del curso.

## Pruebas ejecutadas

Comandos ejecutados con Python 3.12 en un entorno temporal separado del proyecto. Se usó
`DATA_SOURCE=csv` para verificadores offline. No se cambiaron `requirements.txt` ni `.env`.

| Comando | Resultado | Qué permite concluir |
|---|---|---|
| `python recursos/datasets/verificar_datasets.py` | PASS, salida 0 | Integridad y política de marcas del conjunto sintético |
| `python docente/verificar_tools.py` | PASS, salida 0; 24 tools / 4 tracks | Catálogo de referencia contra CSV; no selección del LLM |
| `python docente/verificar_structured.py` | PASS, salida 0 | Contrato del wrapper, recuperación y fallo con modelo simulado |
| `python docente/matriz_seleccion.py --simular` | PASS, salida 0 | Funcionamiento del arnés; el 96.7 % mostrado es simulado |
| `python docente/verificar_guardrails.py --simular` | Salida 1 esperada | Detecta la filtración inyectada deliberadamente en cada track |
| `python docente/verificar_guardrails.py --simular --fallos 0` | PASS, salida 0 | El arnés acepta las respuestas simuladas sin filtración |
| Desde `simulador-industria/`: `PYTHONPATH=. python verificar_simulador.py` | PASS, salida 0 | Rutas, autenticación por equipo, aislamiento y fallos con TestClient |
| `python docente/validar_materiales.py` | PASS | 239 Markdown, 184 Python y 874 enlaces locales; cero errores |

Las simulaciones de guardrails no miden robustez del agente real. No se ejecutaron inferencia,
Qdrant, Langfuse Cloud ni despliegue Foundry/Spaces. Tampoco se enviaron comunicaciones a terceros.
Los bloqueadores operativos del ROADMAP permanecen pendientes.

## Entorno observado

Versiones instaladas en el entorno de validación, sin fijarlas como nuevas dependencias del curso:
LangChain 1.4.2, langchain-core 1.6.5, langchain-openai 1.6.6, Pydantic 2.13.5,
FastAPI 0.141.1, Langfuse 4.15.6, MCP 1.30.0 y langchain-qdrant 1.1.0.
Esto no certifica las integraciones cloud ni compatibilidad de todas las versiones permitidas
por los límites inferiores abiertos de `requirements.txt`.

## Revisión visual

Seis imágenes finales generadas con imagegen integrado, 1672 × 941 píxeles, aproximadamente
16:9. Se inspeccionaron texto, flechas, límites de sistemas, utilidad didáctica y coherencia
del símbolo LLM. Se corrigieron variantes con componentes extra, flechas de telemetría
incorrectas, reintento que omitía el modelo y agente situado fuera del Space.

Los originales de trabajo permanecen fuera del repositorio; los seis PNG seleccionados están
en `imagenes/`. [El catálogo](../imagenes/CATALOGO-IMAGENES.md), los prompts y
`GENERATION-LOG.json` permiten localizar y regenerar assets; las notas están junto a cada sesión.
Hay 14 archivos de notas: S0 no requiere imagen nueva; otras sesiones reutilizan los mecanismos.
El diagrama de evaluación muestra el reporte recomendado de casos no aplicables; no afirma
que el evaluador actual ya los excluya de sus promedios.

## Pendientes para declarar una versión final

Consultar los 27 hallazgos en [COURSE-CONSISTENCY-REPORT](COURSE-CONSISTENCY-REPORT.md):
17 corregidos, 5 abiertos y 5 decisiones requeridas al cierre de esta pasada.
Entre los pendientes figuran embeddings del bonus, aprobación humana verificable, contrato
de métricas, tiempos de S4 y nomenclatura institucional de las rúbricas.
El borrador de PR debe exponer estos límites; no representa aprobación ni autorización de merge.
