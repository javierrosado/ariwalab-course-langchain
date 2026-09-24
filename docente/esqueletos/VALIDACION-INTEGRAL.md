# Preparación integral del curso

Guía para el docente antes de iniciar una edición y al preparar cada sesión.

## Continuidad pedagógica

- Consultar el [mapa del curso](../../docs/COURSE-MAP.md) y el [plan curricular](../../PLAN-CURRICULAR.md).
- Verificar que cada práctica use conocimientos ya enseñados y el checkpoint anterior.
- Comunicar objetivos, entregables, criterios de aceptación y rúbrica antes del laboratorio.
- Aplicar observabilidad desde S9 y evaluación formal desde S10; no exigirlas en A1.

## Organización y tiempos

- Formar equipos de dos personas y distribuir los cuatro tracks.
- Comunicar las 12 horas semanales: seis en vivo y seis de trabajo asíncrono.
- La sustentación A1 requiere 20 minutos además de los 180 del guion S4. Confirmar y comunicar
  con coordinación académica una franja compatible antes de convocar al grupo.
- Calcular la ronda S11 con el número real de equipos y publicar el orden de exposición.
- Convocar panelistas del seminario con antelación y confirmar su conexión.

## Servicios y contingencias

Seguir el [checklist previo](../checklist-pre-sesion.md) y la [verificación del entorno](../../VERIFICACION.md).
Comprobar cuotas, credenciales y despliegues con los servicios reales. Preparar las colecciones
Qdrant de respaldo y el Space del docente. Distinguir los resultados simulados de las mediciones.

## Límites que deben explicarse

- El booleano de confirmación del ejemplo no acredita aprobación humana autenticada.
- Los filtros regex cubren patrones concretos; no garantizan protección contra cualquier ataque.
- La memoria vive por proceso y se pierde al reiniciar el servicio.
- La agrupación de llamadas en una traza debe comprobarse en Langfuse.
- S10 no incluye un runner completo de conversaciones; preparar su integración para la práctica.
- Groundedness es una aproximación léxica: revisar afirmaciones y fuentes manualmente.
- En S11 se envían fragmentos de la respuesta después de validarla completa.
- En Foundry, comprobar compatibilidad de embeddings y adaptar memoria y guardrails del host.

## Comprobación de archivos

```bash
python docente/validar_materiales.py
```

Este comando valida sintaxis Python y enlaces Markdown locales. No verifica por sí solo la
exactitud pedagógica, los tiempos de aula ni la disponibilidad de servicios externos.
