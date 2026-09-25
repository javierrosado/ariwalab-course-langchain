# Prompts de imágenes — 00-preparacion

Base común de los prompts: infografía técnica educativa para AriwaLabs, en español,
16:9, objetivo 1672 × 941 (catálogo), fondo #F4F6F8, texto #1E293B, tarjetas #FFFFFF,
acento #FF5733. Toda cifra visible procede de la fuente indicada y lleva la etiqueta
*ejemplo ilustrativo*; ninguna es una medición.

## IMG-S00-001 — Ruta de la Sesión 0

- **Fuente:** [`00-preparacion/README.md`](../../00-preparacion/README.md), secciones «Ruta de estudio» y «Cuando termines»; [`autoevaluacion.md`](../../00-preparacion/autoevaluacion.md), sección «Resultado».
- **Objetivo pedagógico:** Mostrar el orden de estudio de S0, su duración y la condición bloqueante para entrar a S1.
- **Composición:** Tres bloques en secuencia: LEER (1 Fundamentos LLM → 2 Glosario), PREPARAR (3 Python y entorno → 4 3 cuentas), COMPROBAR (5 4 demos → 6 Autoevaluación) → rombo «≥ 8/10» → «aprobado» → Sesión 1. Flecha discontinua de retorno desde el rombo a LEER. Banda inferior con las condiciones de llegada.
- **Elementos y texto visible:** Sesión 0 · Ruta de nivelación; Obligatoria y asíncrona · 4 a 5 horas · antes de la Sesión 1 · no computa en las 66 h; LEER, PREPARAR, COMPROBAR; los seis pasos con archivo y tiempo (60, según necesites, 45, 40, 60 y 30 min); Bloqueante; ≥ 8/10; aprobado; Sesión 1 síncrona; < 8/10 · repasar y repetir la autoevaluación; Llegas a la Sesión 1 con: Entorno Python, .env con HF_TOKEN, 3 cuentas creadas, 4 demos ejecutadas, Autoevaluación ≥ 8/10, Industria elegida.
- **Flujo:** los pasos siguen el orden 1→6; el glosario lleva borde discontinuo porque se consulta según se necesite.
- **Jerarquía:** título, secuencia de pasos, compuerta, condiciones de llegada.
- **Iconos:** chip, libro, terminal, llave, reproducir, checklist, grupo de personas.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** no sumar tiempos ni añadir pasos; la compuerta es la autoevaluación.
- **NO deben aparecer:** fotografías, robots, 3D, sombras pesadas, gradientes, logos reales, credenciales o cifras fuera del README.
- **Archivo:** `01-ruta-sesion-0.png`.
- **Uso:** Recurso disponible para las diapositivas y para el README de S0.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941. Finished PNG, crisp vector-like flat design, rounded white cards, generous whitespace, clear labelled arrows, high legibility for projected PowerPoint. Background #F4F6F8, text and outlines #1E293B, cards #FFFFFF, accent #FF5733. Title: "Sesión 0 · Ruta de nivelación". Subtitle: "Obligatoria y asíncrona · 4 a 5 horas · antes de la Sesión 1 · no computa en las 66 h". Three phase containers left to right with orange tabs LEER, PREPARAR, COMPROBAR. Each holds two numbered step cards stacked vertically with icon, file name in monospace and a time pill: 1 Fundamentos LLM, fundamentos-llm.md, 60 min; 2 Glosario, recursos/glosario.md, según necesites (dashed border); 3 Python y entorno, python-y-entorno.md, 45 min; 4 3 cuentas, alta-de-cuentas.md, 40 min; 5 4 demos, code/, 60 min; 6 Autoevaluación, autoevaluacion.md, 30 min. Orange arrows between containers lead to a diamond gate "≥ 8/10" labelled "Bloqueante", then an arrow labelled "aprobado" to a card "Sesión 1 · síncrona". A dashed grey return arrow from the diamond back to LEER labelled "< 8/10 · repasar y repetir la autoevaluación". Bottom soft-orange band "Llegas a la Sesión 1 con" and six check chips: Entorno Python, .env con HF_TOKEN, 3 cuentas creadas, 4 demos ejecutadas, Autoevaluación ≥ 8/10, Industria elegida. Footnote: "Industria: telecomunicaciones, banca, retail o seguros · se formaliza en el Laboratorio 1". No photographs, robots, 3D, heavy shadows, gradients, logos, extra steps or totals.
```

## IMG-S00-002 — Un LLM no es una API normal

- **Fuente:** [`fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 1, 2 y 5.
- **Objetivo pedagógico:** Romper la expectativa de determinismo y contrato fijo antes del primer laboratorio.
- **Composición:** Izquierda: comparación de cinco filas API tradicional vs LLM, con la columna LLM resaltada. Derecha: entrada de texto → LLM → distribución del siguiente token (ejemplo ilustrativo) → tres tarjetas de temperatura (0.0, 0.7, 1.5), resaltando 0.0 para los labs.
- **Elementos y texto visible:** filas «Misma entrada, misma salida: Sí / No garantizado», «Contrato de salida: Fijo / Probabilístico, hay que forzarlo», «Errores: Códigos de estado / Respuestas seguras pero falsas», «Costo: Por llamada / Por token, entrada y salida», «Latencia: Milisegundos / Segundos»; «El SOAT cubre gastos médicos hasta…»; 5 UIT 78 %, cinco 11 %, el 4 %; temperaturas y usos de la tabla de la sección 5.
- **Flujo:** texto previo → LLM → distribución; el token elegido se agrega y se repite.
- **Jerarquía:** título, comparación, mecanismo, nota.
- **Iconos:** API, chip, burbuja de texto.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** los porcentajes son los del texto y llevan «ejemplo ilustrativo»; no afirmar reproducibilidad total a temperatura 0.
- **NO deben aparecer:** fotografías, robots, 3D, gradientes, logos reales, métricas nuevas.
- **Archivo:** `02-llm-no-es-una-api.png`.
- **Uso:** Recurso disponible para las diapositivas y para `fundamentos-llm.md`.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Un LLM no es una API normal". Subtitle: "Predice el siguiente token con probabilidades: no consulta, no razona con reglas, no verifica". Left: a comparison table with columns "API tradicional" (API icon) and "LLM" (chip icon, highlighted with soft orange fill and orange border) and rows: Misma entrada, misma salida: Sí / No garantizado; Contrato de salida: Fijo / Probabilístico, hay que forzarlo; Errores: Códigos de estado / Respuestas seguras pero falsas; Costo: Por llamada / Por token, entrada y salida; Latencia: Milisegundos / Segundos. Right, heading "Qué hace realmente": a text card "El SOAT cubre gastos médicos hasta…" with an arrow to a card "LLM predice", then a card "Siguiente token" with a horizontal bar chart: 5 UIT 78 % (orange), cinco 11 %, el 4 % (grey), a dashed tag "ejemplo ilustrativo", and the caption "Se agrega el token elegido y se repite, token a token, hasta terminar". Below: "La temperatura decide cuánto sigue esa distribución" with three cards: 0.0 El más probable casi siempre · Agentes y tools · labs del curso (highlighted); 0.7 Variedad controlada · Conversación; 1.5 Muy aleatorio · Redacción creativa. Footer band: "temperature=0 reduce la variabilidad, no la elimina: se evalúa con métricas, no con assert". No other numbers, logos, robots, 3D or gradients.
```

## IMG-S00-003 — Tokens, contexto y costo

- **Fuente:** [`fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 3, 4 y 8; [`code/README.md`](../../00-preparacion/code/README.md), demo 4.
- **Objetivo pedagógico:** Explicar que el modelo es stateless y que el historial reenviado domina el costo.
- **Composición:** Fila superior: partición en tokens y los tres efectos (costo, límite, latencia). Fila media: ventana de contexto de 32 768 tokens con sus partes (no a escala). Fila inferior: tokens de entrada y salida en los turnos 1, 5 y 10, y las cuatro palancas de ahorro.
- **Elementos y texto visible:** portabilidad numérica → port, abil, idad, num, érica = 5 tokens; phone number → phone, number = 2 tokens; Costo, Límite, Latencia; System prompt ~1 000, Historial ~1 500, Herramientas ~1 200, Documentos ~2 000, Respuesta variable; Turno 1 entrada 1 200 salida 150; Turno 5 entrada 4 800 salida 180; Turno 10 entrada 9 100 salida 160; Recortar el historial, Resumir el historial, Recuperar menos fragmentos, Modelo pequeño para tareas simples.
- **Flujo:** la entrada crece con el historial; las palancas actúan sobre la entrada.
- **Jerarquía:** título, token, ventana, crecimiento del costo, mensaje final.
- **Iconos:** monedas, ventana, reloj.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** toda cifra lleva «ejemplo ilustrativo»; la ventana se rotula «no a escala»; las barras de entrada son proporcionales entre sí.
- **NO deben aparecer:** precios, monedas reales, cifras nuevas, logos.
- **Archivo:** `03-tokens-contexto-costo.png`.
- **Uso:** Recurso disponible para las diapositivas y para `fundamentos-llm.md`.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Tokens, contexto y costo". Subtitle: "El modelo es stateless: tu código le reenvía todo en cada llamada". Top-left card "Un token es un fragmento, no una palabra": "portabilidad numérica" → chips port | abil | idad | num | érica "= 5 tokens"; "phone number" → chips phone | number "= 2 tokens"; dashed tag "ejemplo ilustrativo". Top-right card "Los tokens determinan": Costo (entrada y salida), Límite (ventana de contexto), Latencia (un token por vez). Middle: "Ventana de contexto de Qwen3-32B: 32 768 tokens" as one outlined bar split in five equal labelled segments: System prompt ~1 000 tokens; Historial ~1 500 tokens (highlighted orange); Herramientas ~1 200 tokens; Documentos ~2 000 tokens; Respuesta variable. Tag "ejemplo ilustrativo · no a escala". Captions: "Lo que no entra en la ventana no existe para el modelo" and "«Memoria» del agente = tu código reenvía la lista de mensajes". Bottom-left card "Tokens por llamada a lo largo de una conversación": proportional dark bars for input and small orange bars for output: Turno 1 entrada 1 200 salida 150; Turno 5 entrada 4 800 salida 180; Turno 10 entrada 9 100 salida 160; tag "ejemplo ilustrativo". Bottom-right orange-bordered card "Palancas: todas atacan la entrada": 1 Recortar el historial, 2 Resumir el historial, 3 Recuperar menos fragmentos, 4 Modelo pequeño para tareas simples. Footer band: "El historial es lo que encarece una conversación, no la última pregunta". No prices, logos, robots, 3D or gradients.
```

## IMG-S00-004 — Embeddings: buscar por significado

- **Fuente:** [`fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md), sección 7; [`code/README.md`](../../00-preparacion/code/README.md), demo 3.
- **Objetivo pedagógico:** Mostrar que la cercanía entre embeddings refleja significado y no palabras compartidas.
- **Composición:** Izquierda: tres frases A, B, C → modelo de embeddings → tres vectores. Derecha: proyección 2D simplificada con A y B cerca (0.87) y C lejos (0.12). Abajo: escala de similitud coseno de -1 a 1 con los tres rangos y la posición de A–B y A–C.
- **Elementos y texto visible:** ¿cuántos gigas me quedan?; consulta de datos disponibles; quiero cancelar mi contrato; los tres vectores del texto; Modelo de embeddings; Espacio de significado; proyección 2D simplificada; 0.87; 0.12; < 0.5 poco o nada relacionados; 0.5 – 0.8 relacionados; > 0.8 muy relacionados.
- **Flujo:** texto → modelo → vector → cercanía en el espacio.
- **Jerarquía:** título, transformación, espacio, escala, mensaje final.
- **Iconos:** chip; puntos con letra.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** las similitudes y los vectores son los del texto y llevan «ejemplo ilustrativo»; la proyección 2D no representa distancias exactas.
- **NO deben aparecer:** nubes de puntos inventadas, nombres de modelos no citados, logos.
- **Archivo:** `04-embeddings-significado.png`.
- **Uso:** Recurso disponible para las diapositivas y reutilizable como anticipo de S5.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Embeddings: buscar por significado". Subtitle: "Un embedding convierte un texto en un vector de cientos de números que representa su significado". Left: three phrase cards with letter badges A "¿cuántos gigas me quedan?", B "consulta de datos disponibles" (orange badges), C "quiero cancelar mi contrato" (dark badge), each with an arrow into one tall orange-bordered card "Modelo de embeddings" (chip icon), and arrows out to monospace vectors [0.21, -0.08, 0.44, …], [0.19, -0.11, 0.41, …], [-0.55, 0.72, -0.03, …]. Caption: "Textos parecidos quedan cerca en ese espacio". Right card "Espacio de significado · proyección 2D simplificada" with a light grid: points A and B close together joined by a solid orange line labelled 0.87; point C far away joined to A by a dashed grey line labelled 0.12; caption "A y B: cerca · A y C: lejos"; dashed tag "ejemplo ilustrativo". Bottom: "Similitud coseno: de -1 a 1" as a proportional bar from -1 to 1 with segments "< 0.5 · poco o nada relacionados" (grey), "0.5 – 0.8 · relacionados" (light orange), "> 0.8 · muy relacionados" (orange), and markers "A–C = 0.12" and "A–B = 0.87". Footer band: "A y B no comparten ni una palabra y aun así están cerca: base del RAG (Sesión 5)". No other numbers, logos, robots, 3D or gradients.
```

## IMG-S00-005 — Alucinación y dónde vive el conocimiento

- **Fuente:** [`fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 6 y 10.
- **Objetivo pedagógico:** Reconocer la alucinación como fallo sin señal, ubicar las tres defensas del curso y separar estilo de conocimiento.
- **Composición:** Izquierda: pregunta del usuario → respuesta segura y falsa del LLM (2 UIT; correcto: 1 UIT) → ausencia de señales → tres defensas (Tools S3–S4, RAG S5, Guardrails S6). Derecha: comparación fine-tuning vs RAG en cuatro filas y la composición del agente: Qwen3-32B + system prompt (S2) + colección Qdrant (S5).
- **Elementos y texto visible:** los textos de las secciones 6 y 10: pregunta y respuesta del SOAT, «Es 1 UIT: el modelo no lo sabe, lo generó», las tres defensas con su sesión, filas «Qué mejora», «Actualizar un dato», «Citar la fuente», «Costo de un cambio», «Este curso no afina ningún modelo», «Agente de AndesMóvil =».
- **Flujo:** pregunta → respuesta; las defensas se presentan en paralelo, sin orden de ejecución.
- **Jerarquía:** título, caso, defensas, comparación, composición, mensaje final.
- **Iconos:** advertencia, persona, chip, llave inglesa, documento, escudo, cilindro con puntos.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** no presentar ninguna defensa como garantía; el curso no afina modelos.
- **NO deben aparecer:** logos de aseguradoras u operadores reales, robots, 3D.
- **Archivo:** `05-alucinacion-conocimiento.png`.
- **Uso:** Recurso disponible para las diapositivas; anticipa S3–S6.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Alucinación y dónde vive el conocimiento". Subtitle: "El modelo no distingue lo que sabe de lo que suena plausible". Left panel "Alucinación: respuesta fluida, segura y falsa" (warning icon): user bubble "¿Cuánto cubre el SOAT por gastos de sepelio?"; LLM bubble with orange border "El SOAT cubre hasta 2 UIT por gastos de sepelio." with "2 UIT" in orange and an orange pointer note "Es 1 UIT: el modelo no lo sabe, lo generó"; text "Llega sin excepción y sin código de error, con el mismo tono seguro que una respuesta correcta". Then "Las tres defensas del curso": three orange-bordered cards Tools (wrench, S3–S4, "El dato viene de tu sistema"), RAG (document, S5, "Se apoya en un documento y lo cita"), Guardrails (shield, S6, "El código impide lo que está fuera de política"); note "Ninguna lo elimina sola; las tres juntas lo vuelven manejable". Right panel "Fine-tuning vs RAG" table with RAG column highlighted: Qué mejora: Estilo: tono, jerga, formato / Conocimiento: datos, políticas, tarifas; Actualizar un dato: Reentrenar / Reindexar; Citar la fuente: Imposible / Obligatorio; Costo de un cambio: Alto / Casi cero. Below: "Este curso no afina ningún modelo:" "Agente de AndesMóvil =" three cards joined by plus signs: Qwen3-32B (chip, genérico, sin afinar) + System prompt (document, S2, tono, jerga, límites) + Colección Qdrant (vector database, S5, tarifas, coberturas); note "Cambiar el tono del agente es editar un texto, no reentrenar". Footer band: "Un dato que cambia no puede vivir en los pesos: el conocimiento va al RAG". No real logos, robots, 3D or gradients.
```

## IMG-S00-006 — Entorno, secretos y configuración

- **Fuente:** [`python-y-entorno.md`](../../00-preparacion/conceptos-previos/python-y-entorno.md), secciones 2 a 6; `comun/settings.py` y `comun/provider.py`.
- **Objetivo pedagógico:** Situar `.env`, `comun/settings.py` y `comun/provider.py`, y mostrar por qué el cambio de proveedor es de configuración.
- **Composición:** `.env` (fuera del repositorio) → dentro del contenedor «(.venv) entorno virtual»: settings.py → provider.py → Labs S1–S11. provider.py → Hugging Face · Qwen3-32B (sólida) y → Microsoft Foundry (discontinua, bonus). Abajo: Pydantic (`description` → `model_json_schema()` → LLM) y la comprobación `check_stack --solo-modelo`.
- **Elementos y texto visible:** .env, copia de .env.example, AI_PROVIDER=…, HF_TOKEN=hf_…, en .gitignore: nunca al repositorio; settings.py; provider.py; get_chat_model(); describe_provider(); Labs S1–S11; Actívalo en cada terminal nueva; AI_PROVIDER=huggingface; AI_PROVIDER=foundry; el fragmento `Consulta`/`urgencia` de la sección 5; Comprobaciones 1 a 5 en verde; Si fallan la 3 o la 4 (tool calling), avisa al docente.
- **Flujo:** la configuración entra solo por settings.py; los labs reciben el modelo desde provider.
- **Jerarquía:** título, arquitectura, Pydantic y verificación, mensaje final.
- **Iconos:** llave, candado, engranaje, chip, código, terminal, llaves, checklist.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** ningún token real; Foundry se marca como bonus con línea discontinua.
- **NO deben aparecer:** logos de Hugging Face o Microsoft, claves reales, capturas.
- **Archivo:** `06-entorno-configuracion.png`.
- **Uso:** Recurso disponible para las diapositivas y para `python-y-entorno.md`.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Entorno, secretos y configuración". Subtitle: "Ningún archivo del curso llama a os.getenv(): todo pasa por comun/settings.py". Left: orange-bordered card ".env" (key icon) "copia de .env.example", monospace "AI_PROVIDER=…" and "HF_TOKEN=hf_…", lock note "en .gitignore: nunca al repositorio". A dashed container with dark tab "(.venv) entorno virtual" holds: card "settings.py · comun/ · Único lugar que declara qué variables existen" (gear), arrow to orange-bordered card "provider.py · comun/ · get_chat_model() · describe_provider()" (chip), arrow down labelled "modelo" to card "Labs S1–S11 · no saben de qué proveedor viene"; plus a grey note card "Actívalo en cada terminal nueva" (terminal icon). Arrow from .env into settings.py. From provider.py: solid arrow to card "Hugging Face · Qwen3-32B · AI_PROVIDER=huggingface · Sesiones 1 a 11" and dashed grey arrow to dashed card "Microsoft Foundry · AI_PROVIDER=foundry · Solo bonus final". Bottom-left card "Pydantic v2: el description no es documentación, es prompt": code block "class Consulta(BaseModel): urgencia: Urgencia = Field(description="Nivel de urgencia")" → block "model_json_schema()" showing "urgencia": { "description": "Nivel…" … } → chip "lo lee". Bottom-right orange card "Comprobación final": dark command bar "python -m comun.check_stack --solo-modelo", check "Comprobaciones 1 a 5 en verde", warning "Si fallan la 3 o la 4 (tool calling), avisa al docente: no dependen de ti". Footer band: "Esta indirección permite migrar a Foundry cambiando una línea del .env". No logos, real keys, robots, 3D or gradients.
```

## IMG-S00-007 — Tres cuentas del curso

- **Fuente:** [`alta-de-cuentas.md`](../../00-preparacion/conceptos-previos/alta-de-cuentas.md); [`00-preparacion/README.md`](../../00-preparacion/README.md), sección «Las 3 cuentas del curso».
- **Objetivo pedagógico:** Mostrar que las tres cuentas se crean en S0 aunque se usen en S1, S5 y S9, y cómo se verifica el stack.
- **Composición:** Línea de tiempo S0–S11 y bonus con S0 marcado como «hoy»; tres tarjetas colgadas de S1 (Hugging Face), S5 (Qdrant Cloud) y S9 (Langfuse Cloud) con pasos clave y variables `.env`; banda inferior `check_stack` con los códigos de salida 0, 1 y 2.
- **Elementos y texto visible:** nombres y usos de las tres cuentas; «Token con permiso de inferencia: sin él, 401»; «Cluster gratuito en estado Healthy»; «URL del cluster: termina en :6333»; «2 usuarios en el plan gratuito: equipos de 2»; variables `.env` sin valores reales; 0 Todo funciona; 1 Modelo OK, falla un servicio; 2 Falla crítica.
- **Flujo:** creación en S0 → uso desde la sesión indicada; check_stack → código de salida → acción.
- **Jerarquía:** título, línea de tiempo, tarjetas, verificación, mensaje final.
- **Iconos:** chip (modelo), cilindro con puntos (base vectorial), árbol de trazas (observabilidad), terminal.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** no mostrar límites de cuota del plan gratuito salvo los 2 usuarios, que determinan el tamaño de los equipos.
- **NO deben aparecer:** logos de los servicios, claves reales, capturas de las consolas.
- **Archivo:** `07-tres-cuentas.png`.
- **Uso:** Recurso disponible para las diapositivas y para `alta-de-cuentas.md`.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Tres cuentas hoy, usadas a lo largo del curso". Subtitle: "Plan gratuito · ninguna pide tarjeta de crédito · se crean las tres en la Sesión 0". A horizontal timeline S0 to S11 plus Bonus; S0 dark with label "hoy: crear las 3"; S1, S5 and S9 as orange dots with vertical connectors to three cards, each with an orange pill "Desde la Sesión N". Card Hugging Face (chip icon, "Modelo de chat y embeddings"): warning "Token con permiso de inferencia: sin él, 401", checks "Settings → Access Tokens → nuevo token", "Se muestra una sola vez: cópialo"; grey .env block HF_TOKEN=hf_…, HF_CHAT_MODEL=Qwen/Qwen3-32B, HF_EMBEDDING_MODEL=…. Card Qdrant Cloud (vector database icon, "Base vectorial del RAG"): checks "Cluster gratuito en estado Healthy", "URL del cluster: termina en :6333", "API key generada en el cluster"; .env QDRANT_URL=https://…:6333, QDRANT_API_KEY=…, QDRANT_COLLECTION=kb-<track>. Card Langfuse Cloud (trace tree icon, "Trazabilidad y evaluación"): warning "2 usuarios en el plan gratuito: equipos de 2", checks "Uno crea la organización e invita al otro", "Settings → API Keys: pública y secreta"; .env LANGFUSE_PUBLIC_KEY=pk-lf-…, LANGFUSE_SECRET_KEY=sk-lf-…, LANGFUSE_HOST=https://cloud…. Bottom row: dark terminal card "python -m comun.check_stack" → three cards "0 Todo funciona · sigue con las demos", "1 Modelo OK, falla un servicio · revisa Qdrant o Langfuse; sigues hasta S4", "2 Falla crítica · avisa al docente" (orange). Footer band: "Créalas hoy: quien deja Qdrant para la semana 5 llega a esa sesión sin poder hacer el laboratorio". No service logos, real keys, screenshots, robots, 3D or gradients.
```

## IMG-S00-008 — Anatomía de un LLM

- **Fuente:** complemento de [`fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md), secciones 2, 4 y 5. Los componentes internos (tokenizador, embeddings, bloques transformer, logits) no aparecen en el texto de S0; la imagen los introduce a nivel conceptual.
- **Objetivo pedagógico:** Nombrar las partes de un LLM y ubicar dónde están los pesos y qué controla la aplicación.
- **Composición:** Entrada (ventana de contexto) → 1 Tokenizador → 2 Embeddings → 3 Bloques transformer × N (atención + feed-forward) → 4 Logits → 5 Muestreo → token; bucle de retorno a la entrada. Corchete «contienen los pesos aprendidos» sobre 2, 3 y 4. Tres notas: Pesos, Atención, Lo que controla tu aplicación.
- **Elementos y texto visible:** los nombres de las seis etapas, «contienen los pesos aprendidos», el texto del bucle y las tres notas.
- **Flujo:** izquierda a derecha; el token elegido vuelve a la entrada (generación token a token).
- **Jerarquía:** título, tubería, bucle, notas, mensaje final.
- **Iconos:** chip, lupa, engranaje; minigráfico de barras y medidor de temperatura sin cifras.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** sin cifras (capas, parámetros, vocabulario); la atención mira solo los tokens anteriores.
- **NO deben aparecer:** cerebros, robots, 3D, cifras de un modelo concreto.
- **Archivo:** `08-anatomia-llm.png`.
- **Uso:** Recurso disponible para las diapositivas; complementa la sección 2 de `fundamentos-llm.md`.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Anatomía de un LLM". Subtitle: "Qué ocurre dentro del modelo en cada paso de generación". A left-to-right pipeline of six cards joined by orange arrows: "Entrada · ventana de contexto" with stacked bars System prompt, Historial, Pregunta; "1 Tokenizador" showing «¿cuántos gigas…» → empty token chips → dark ID squares marked #, caption "Texto → tokens → IDs del vocabulario"; "2 Embeddings" showing ID squares → small vector columns, caption "Cada ID se convierte en un vector"; "3 Bloques transformer × N" highlighted, with rows 1, 2, N each split into "Atención" and "Feed-forward", caption "N bloques en serie: cada uno refina los vectores con los tokens anteriores"; "4 Logits" with a small decreasing bar chart without numbers, caption "Un puntaje por token del vocabulario → softmax → probabilidades"; "5 Muestreo" with a temperature gauge and an orange chip "token", caption "La temperatura decide cuánto seguir la distribución". A dark bracket above cards 2 to 4 labelled "contienen los pesos aprendidos". An orange return arrow from Muestreo back to Entrada labelled "El token elegido se agrega a la entrada y el ciclo se repite hasta un token de fin o el límite de salida". Three notes below: Pesos ("Parámetros aprendidos en el entrenamiento, en embeddings, bloques y logits. Fijos al usar el modelo: no aprende de tu conversación"); Atención ("Cada token pondera los tokens anteriores del contexto para decidir qué le es relevante"); Lo que controla tu aplicación ("La entrada (prompt, historial, documentos) y el muestreo (temperatura). Nunca los pesos"). Footer band: "Un LLM no busca ni verifica: convierte la entrada en probabilidades del siguiente token". No numbers, brains, robots, 3D or gradients.
```

## IMG-S00-009 — Ejemplo: la misma consulta, API vs LLM

- **Fuente:** [`fundamentos-llm.md`](../../00-preparacion/conceptos-previos/fundamentos-llm.md), sección 1; `simulador-industria/docs/REFERENCIA-API.md` (respuesta 200 de `GET /telco/consumo/988837195?periodo=2026-08`) y `simulador-industria/routers.py` (mensaje del 404).
- **Objetivo pedagógico:** Mostrar con un caso concreto la diferencia entre un contrato fijo y una salida probabilística sin herramientas.
- **Composición:** Dos columnas (API REST del simulador / LLM sin herramientas) y cuatro filas: llamadas 1, 2 y 3 con la misma consulta, y una línea inexistente. Estado de cada celda: idéntica, error explícito / dato inventado, otra respuesta, sin señal de error.
- **Elementos y texto visible:** la ruta, el JSON 200 con `gb_consumidos` y `gb_incluidos`, el 404 `Sin consumo para 999999999 en 2026-08. Periodos: []` y cuatro respuestas del LLM rotuladas «respuestas ilustrativas».
- **Flujo:** lectura por filas; la comparación es horizontal.
- **Jerarquía:** título, encabezados, filas, conclusión.
- **Iconos:** API, chip.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** la columna API usa solo respuestas del simulador; las del LLM se rotulan como ilustrativas.
- **NO deben aparecer:** logos de operadores reales, datos personales, claves.
- **Archivo:** `09-ejemplo-api-vs-llm.png`.
- **Uso:** Recurso disponible para las diapositivas; anticipa la separación propuesta/ejecución de S1 y S3.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Ejemplo: la misma consulta, API vs LLM". Subtitle: "AndesMóvil · «¿Cuántos gigas me quedan?» · línea 988837195 · periodo 2026-08". Two columns. Left header card (dark outline, API icon): "API REST del simulador" and monospace "GET /telco/consumo/988837195?periodo=2026-08". Right header card (soft orange, chip icon): "LLM sin herramientas", «¿Cuántos gigas me quedan en la línea 988837195?», dashed tag "respuestas ilustrativas". Four rows labelled Llamada 1, Llamada 2, Llamada 3 and "Línea 999999999 · no existe". Left cells (grey, monospace): 200 {"gb_consumidos": "24.88", "gb_incluidos": "60", …} with check chip "idéntica" in rows 1-3; row 4: 404 {"detail": "Sin consumo para 999999999 en 2026-08. Periodos: []"} with chip "error explícito". Right cells (white bubbles): "Te quedan unos 15 GB este mes." (orange chip "dato inventado"); "No tengo acceso a tu línea; revisa la app de AndesMóvil." (grey chip "otra respuesta"); "Según tu plan, tienes 8 GB disponibles." (orange chip "otro dato inventado"); "Tu línea 999999999 tiene 12 GB disponibles." (orange chip "sin señal de error"). Captions: "Contrato fijo: mismo JSON y un 404 explícito cuando falla" and "Sin herramientas no ve tu sistema: redacta, varía o inventa". Footer band: "Por eso el LLM propone la llamada y tu código consulta la API (Sesión 3)". No real logos, personal data, keys, robots, 3D or gradients.
```

## IMG-S00-010 — Hugging Face: qué ofrece y qué usamos

- **Fuente:** [documentación del Hub](https://huggingface.co/docs/hub/en/index) y [Inference Providers](https://huggingface.co/docs/hub/en/models-inference), consultadas el 24-09-2026; `comun/provider.py`; [`alta-de-cuentas.md`](../../00-preparacion/conceptos-previos/alta-de-cuentas.md); [Sesión 8](../../modulo-3-produccion/sesion-08-despliegue-hf-spaces/README.md).
- **Objetivo pedagógico:** Distinguir los componentes de Hugging Face que usa el curso de los que ofrece la plataforma.
- **Composición:** Izquierda: nueve componentes; los usados con borde de acento, marca y sesión; los no usados con borde discontinuo gris. Derecha: `.env` → `comun/provider.py` → `get_chat_model()` / `get_embeddings()` → Qwen/Qwen3-32B / multilingual-e5-large; Sesión 8: git push → Space (Docker) → API pública, con Space secrets.
- **Elementos y texto visible:** usados: Access Tokens (S0), Models (S1), Inference Providers (S1–S11), Spaces (Docker) (S8), Repositorios git (S8); no usados: Datasets, Storage Buckets, Organizations, ZeroGPU.
- **Flujo:** la configuración entra por `.env` y el código llega al proveedor solo por `comun/provider.py`.
- **Jerarquía:** título, componentes, uso en el curso, mensaje final.
- **Iconos:** llave, chip, API, código, carpeta, documento, cilindro, grupo.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** sin logos ni límites del plan gratuito; la marca «usa el curso» no depende solo del color (marca + borde sólido).
- **NO deben aparecer:** el logo de Hugging Face, tokens reales, precios.
- **Archivo:** `10-hugging-face.png`.
- **Uso:** Recurso disponible para las diapositivas y para `alta-de-cuentas.md`.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Hugging Face: qué ofrece y qué usamos". Subtitle: "La plataforma de modelos abiertos: pone el modelo del curso y el despliegue del agente". Left panel "Componentes de la plataforma" with legend (orange check = "la usa el curso"; dashed grey box = "no se usa en los labs") and a 3x3 grid. Used cards (orange border, check, session pill): Access Tokens S0 "HF_TOKEN con permiso de inferencia"; Models S1 "Qwen/Qwen3-32B y multilingual-e5-large"; Inference Providers S1–S11 "API serverless para chat y embeddings"; Spaces (Docker) S8 "Despliegue del agente con Space secrets"; Repositorios git S8 "Base de Models, Datasets y Spaces: git push al Space". Not used (dashed grey): Datasets, Storage Buckets, Organizations, ZeroGPU with one-line descriptions. Caption "Según la documentación oficial · consultada el 24-09-2026". Right orange panel "Cómo lo usa el curso": .env (HF_TOKEN · HF_CHAT_MODEL · HF_EMBEDDING_MODEL) → comun/provider.py (highlighted, "el único punto de contacto con el proveedor") → two branches get_chat_model() "router compatible con OpenAI" → Qwen/Qwen3-32B "chat y tool calling", and get_embeddings() "extracción de embeddings" → multilingual-e5-large "embeddings del RAG · S5". Below "Sesión 8 · despliegue": git push → Space (Docker) → API pública del agente; note "Space secrets: HF_TOKEN y AGENT_API_KEY; nunca el .env en el repositorio". Footer band: "Hugging Face pone el modelo y el despliegue; tu código lo ve solo a través de comun/provider.py". No logos, prices, real tokens, robots, 3D or gradients.
```

## IMG-S00-011 — Qdrant Cloud: qué ofrece y qué usamos

- **Fuente:** [documentación de Qdrant Cloud](https://qdrant.tech/documentation/cloud/) y [Cloud Quickstart](https://qdrant.tech/documentation/cloud-quickstart/), consultadas el 24-09-2026; `comun/vectorstore.py`; [Sesión 5](../../modulo-2-agentes-avanzados/sesion-05-memoria-rag/README.md).
- **Objetivo pedagógico:** Distinguir los componentes de Qdrant Cloud que usa el curso y ubicar la ingesta y la consulta del RAG.
- **Composición:** Izquierda: nueve componentes (seis usados, tres no usados). Derecha: `.env` → `comun/vectorstore.py`; ingesta (corpus → chunks → embeddings → upsert) → colección `kb-<track>`; consulta (pregunta → embedding → búsqueda coseno + filtro → fragmentos con su fuente) → contexto del LLM.
- **Elementos y texto visible:** usados: Cloud UI, Cluster gratuito, API key (S0), Colección, Puntos y payload, Búsqueda y filtros (S5); no usados: Cloud Inference, Escalado y backups, Hybrid / Private Cloud. La colección muestra 1024 dimensiones y distancia coseno, valores definidos en `comun/vectorstore.py`.
- **Flujo:** ingesta y consulta comparten la colección y el mismo modelo de embeddings.
- **Jerarquía:** título, componentes, uso en el curso, mensaje final.
- **Iconos:** ventana, cilindro con puntos, llave, cilindro, documento, lupa, chip, árbol, carpeta.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** sin límites de cuota; la dimensión 1024 corresponde al modelo de embeddings configurado.
- **NO deben aparecer:** el logo de Qdrant, URLs o claves reales, precios.
- **Archivo:** `11-qdrant-cloud.png`.
- **Uso:** Recurso disponible para las diapositivas; reutilizable como anticipo de S5.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Qdrant Cloud: qué ofrece y qué usamos". Subtitle: "La base vectorial gestionada: guarda el conocimiento del agente para el RAG". Left panel "Componentes de la plataforma" with legend and a 3x3 grid. Used (orange border, check, session pill): Cloud UI S0 "Consola web para crear y ver el cluster"; Cluster gratuito S0 "Base vectorial gestionada; debe estar en Healthy"; API key S0 "Autentica cada petición al cluster"; Colección S5 "kb-<track> · 1024 dim · distancia coseno"; Puntos y payload S5 "Vector + texto y documento fuente de cada fragmento"; Búsqueda y filtros S5 "Similitud + filtro por metadatos del payload". Not used (dashed grey): Cloud Inference "Embeddings dentro de Qdrant; el curso usa los de HF"; Escalado y backups "Réplicas, shards y recuperación ante desastres"; Hybrid / Private Cloud "Qdrant en infraestructura propia". Caption "Según la documentación oficial · consultada el 24-09-2026". Right orange panel "Cómo lo usa el curso": .env (QDRANT_URL · QDRANT_API_KEY · QDRANT_COLLECTION) → comun/vectorstore.py (get_client() · ensure_collection() · get_vector_store()). "Ingesta · S5": Corpus → Chunks → Embeddings de HF → Upsert puntos, arrow down into a dark-outlined card "Colección kb-<track>" with "respaldo: kb-<track>-respaldo". "Consulta · S5": Pregunta → Embedding de HF → Búsqueda coseno + filtro (highlighted, arrow up to the collection) → Fragmentos con su fuente; note "Los fragmentos y su fuente entran al contexto del LLM, que debe citarla". Footer band: "Qdrant guarda el conocimiento: vectores para buscar, payload para citar la fuente". No logos, real URLs or keys, prices, robots, 3D or gradients.
```

## IMG-S00-012 — Langfuse Cloud: qué ofrece y qué usamos

- **Fuente:** [documentación de Langfuse](https://langfuse.com/docs), consultada el 24-09-2026; `comun/observability.py`; [Sesión 9](../../modulo-3-produccion/sesion-09-observabilidad-langfuse/README.md) y [Sesión 10](../../modulo-3-produccion/sesion-10-evaluacion-optimizacion/README.md).
- **Objetivo pedagógico:** Distinguir los componentes de Langfuse que usa el curso y mostrar cómo llegan las trazas ya enmascaradas.
- **Composición:** Izquierda: nueve componentes (seis usados, tres no usados en los labs). Derecha: `.env` → `comun/observability.py`; agente → callback handler → enmascarar PII → proyecto Langfuse; árbol de la traza de S9; evaluación S10: `evals/dataset.py` → `create_dataset` + items → dataset de 30 casos.
- **Elementos y texto visible:** usados: Organización y proyecto, API keys (S0), Tracing, Enmascarado, Latencia y costo (S9), Datasets (S10); no usados en los labs: Prompt Management, Scores y LLM-as-a-Judge (el juez del curso corre en local), Sessions y Experiments (además Alerts y Annotation Queues).
- **Flujo:** la observabilidad se engancha por callback; el enmascarado ocurre antes de enviar.
- **Jerarquía:** título, componentes, uso en el curso, mensaje final.
- **Iconos:** grupo, llave, árbol de trazas, candado, reloj, checklist, documento, escudo, burbuja.
- **Formato:** 16:9; 1672 × 941; PNG.
- **Restricciones:** el árbol reproduce el de la sección 2 de S9; sin cifras de latencia o costo.
- **NO deben aparecer:** el logo de Langfuse, claves reales, datos personales sin enmascarar.
- **Archivo:** `12-langfuse-cloud.png`.
- **Uso:** Recurso disponible para las diapositivas; anticipa S9 y S10.

### Prompt para adaptar el recurso

```text
Create one educational technical infographic for AriwaLabs, in Spanish, landscape 16:9, 1672x941, flat vector-like style, background #F4F6F8, text #1E293B, white cards, accent #FF5733. Title: "Langfuse Cloud: qué ofrece y qué usamos". Subtitle: "La plataforma de observabilidad: registra qué hizo el agente en cada ejecución". Left panel "Componentes de la plataforma" with legend and a 3x3 grid. Used (orange border, check, session pill): Organización y proyecto S0 "2 usuarios: tú y tu compañero de equipo"; API keys S0 "Pública pk-lf y secreta sk-lf"; Tracing S9 "Traza y spans de cada ejecución"; Enmascarado S9 "mask= en el cliente: la PII no sale del proceso"; Latencia y costo S9 "p50/p95 y costo por ejecución"; Datasets S10 "Los 30 casos del golden set del track". Not used (dashed grey): Prompt Management "Versionar prompts; el curso los versiona en el código"; Scores y LLM-as-a-Judge "El juez del curso corre en local (S10)"; Sessions y Experiments "Alerts y Annotation Queues: fuera del alcance de los labs". Caption "Según la documentación oficial · consultada el 24-09-2026". Right orange panel "Cómo lo usa el curso": .env (LANGFUSE_PUBLIC_KEY · SECRET_KEY · HOST) → comun/observability.py (get_langfuse_handler() · enmascarar_pii()). "Trazas · S9": Agente LangChain → Callback handler → Enmascarar PII (highlighted) → Proyecto Langfuse, then a grey monospace tree: TRACE «consulta de cliente»; SPAN llamada al modelo (decidir); SPAN tool get_customer_plan; SPAN llamada al modelo (decidir); SPAN retriever kb-telecomunicaciones; SPAN llamada al modelo (redactar). "Evaluación · S10": evals/dataset.py → create_dataset + items → Dataset 30 casos (highlighted). Footer band: "Langfuse observa sin tocar el agente: se engancha por callback y recibe datos ya enmascarados". No logos, real keys, unmasked personal data, robots, 3D or gradients.
```

### Criterios visuales comunes

Fondo opaco; LLM representado con chip. Flechas sólidas para flujo de datos o ejecución y
discontinuas para retorno o camino opcional; todas etiquetadas cuando no son obvias.
Las cifras solo aparecen con la etiqueta «ejemplo ilustrativo».
