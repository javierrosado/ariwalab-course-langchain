# Design System AriwaLabs

- Formato maestro: PNG RGB, 1536 × 864, 16:9. Márgenes de seguridad: al menos 48 px.
- Fondo `#F4F6F8`; estructura y textos `#1E293B`; contenedores `#FFFFFF`; foco y conectores `#FF5733`; gris de apoyo `#526277`.
- Tipografía DejaVu Sans, titulares 43 px, nodos 27 px, conclusión 26 px. Bordes redondeados; sin fotografías, gradientes ni sombras pesadas.
- Semántica persistente: modelo/LLM = caja de razonamiento; agente = bucle con aplicación; tool = caja de acción; memoria = estado por hilo; RAG = recuperación documental; MCP = cliente/servidor; middleware/guardrail = control entre usuario, agente y salida; aprobación humana = decisión antes de acción; API = frontera de servicio; base de datos = almacén; sistema externo = servicio consultado; observabilidad = trace y spans.
- El coral destaca un control o paso central, nunca indica que el LLM ejecuta una tool por sí mismo. Numeración y flechas marcan secuencia de exposición.
- Evolución: S1 presenta bucle base, S3 separa solicitud/ejecución de tool, S5 añade memoria/RAG, S6 controles, S9 trazabilidad y S11 vista integral.
- Priorizar texto corto dentro del PNG. Ejemplos, excepciones y preguntas se conservan en `NOTAS-SLIDES.md`.
