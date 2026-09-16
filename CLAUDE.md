# Contexto del proyecto — léeme antes de tocar nada

Este archivo lo carga Claude Code automáticamente al abrir la carpeta. Es el punto de entrada:
resume qué es el proyecto, qué está decidido y dónde está el detalle. **No duplica el estado**;
apunta a los archivos que lo llevan.

---

## Regla #0 — instrucción permanente de Javier

> **No asumas nada.** Si hay una duda, una ambigüedad o falta un dato para entender bien algo,
> **pregúntale antes de avanzar**. Vale más una pregunta que una entrega en la dirección
> equivocada.

Aplica siempre, incluso cuando la respuesta "obvia" parezca segura. Y cuando detectes que una
instrucción admite dos lecturas, di cuáles son las dos y pide que elija — no elijas tú.

**Formato de respuesta que prefiere Javier** (es ingeniero de sistemas): bullets, cuadros
comparativos cuando haya que decidir, diagramas ASCII cuando ayuden, y ejemplos concretos.

---

## Qué es este proyecto

Curso en español **"Construcción de agentes de IA con LangChain"**, de 12 sesiones y 72 horas,
para ingenieros de software con poca o ninguna experiencia previa en LLM.

- **Insumos de origen:** el repo `../langchain-for-beginners` (Microsoft) y el sílabo en PDF de
  *IA Agent Building* (Continental Florida University).
- **4 tracks de industria** con marcas ficticias peruanas: telecomunicaciones (AndesMóvil),
  banca (Banco Inti), retail (MercaSur), seguros (Andina Seguros).
- **Laboratorios incrementales:** L1 → L8 construyen una sola aplicación; el proyecto final es
  el resultado acumulado, no un trabajo aparte.
- **40 % teoría / 60 % práctica** (29 h / 43 h). Esta proporción es un requisito, no una meta.

---

## Restricciones duras — violarlas invalida el diseño

| # | Restricción | Consecuencia práctica |
|---|-------------|------------------------|
| **P1** | **100 % open source** durante todo el curso | Nada de LangSmith, Azure AI Search ni servicios propietarios en la troncal |
| **P2** | **Nada corre en local.** Todo SaaS, en línea, gratis o de costo mínimo | Nada de Chroma embebido, `sentence-transformers` local ni `localhost` |
| **P3** | **Foundry es solo un bonus final**, asíncrono y opcional | Habrá un Curso 2 que sí es 100 % Foundry. Aquí no se adelanta |
| **P4** | **Todo en español**: prosa, docstrings, comentarios, datasets | Identificadores del código en inglés (D11) |
| **P5** | **Marcas ficticias.** Cero marcas peruanas reales | `recursos/datasets/verificar_datasets.py` lo comprueba con regex de límite de palabra |
| **P6** | El repo base de Microsoft **no se modifica** | La memoria y el curso viven en esta carpeta (D04) |

---

## Decisiones que no se renegocian

El registro completo está en `_memoria/DECISIONES.md` (D01–D28 con alternativas y motivos).
Las que más condicionan el trabajo diario:

| ID | Decisión | Por qué importa al escribir código |
|----|----------|-------------------------------------|
| **D28** | Modelo **`Qwen/Qwen3-32B`** con `HF_ENABLE_THINKING=false` | Elegido **por medición**: de 4 candidatos probados contra el endpoint real, fue el único que pasó tool calling. No lo cambies sin volver a medir con `check_stack --candidatos` |
| **D21** | **Sin fine-tuning** (Camino A) | La personalización por industria vive en el system prompt y en Qdrant. Si escribes que el modelo "sabe" de un sector, está mal |
| **D20** | **La fiabilidad se compone** | 93 % por llamada = 80 % en 3 pasos. De aquí salen las reglas A1–A6 |
| **D13** | `comun/provider.py` abstrae el proveedor | Ningún archivo del curso instancia el modelo directamente ni llama a `os.getenv()` |
| **D09/D10** | **Qdrant Cloud, sin fallback** | Un solo backend en `comun/vectorstore.py`. No añadas Chroma ni FAISS "por si acaso" |
| **D19** | **Equipos de 2 personas** | Impuesto por el límite de 2 usuarios de Langfuse Hobby. No es pedagógico, es una restricción de plan |
| **D27** | **2 sesiones/semana × 3 h → 6 semanas** | 12 h semanales por alumno |
| **D22/D23** | Simulador único en HF Spaces, con API key por equipo | Los alumnos construyen el agente, nunca el simulador |

### Las 6 reglas de calibración (A1–A6)

Salen de D20 y se aplican a todo el código de laboratorio:

- **A1** — máximo 3-4 tools enlazadas por agente. Nunca 6.
- **A2** — cada docstring dice el verbo, cuándo usarla y **cuándo NO** usarla.
- **A3** — `with_structured_output()` siempre con validación y un reintento → usa `comun/structured.py`.
- **A4** — tope duro de iteraciones y errores de tool redactados para que el modelo los entienda.
- **A5** — few-shot en los prompts críticos.
- **A6** — obligar a recuperar antes de afirmar tarifas, coberturas o políticas.

---

## Dónde está el estado

| Archivo | Qué contiene | Cuándo leerlo |
|---------|--------------|----------------|
| `ROADMAP.md` | **La fuente de verdad del avance.** Fases 0–5 con casillas | Siempre, al empezar |
| `_memoria/DECISIONES.md` | ADR completo D01–D28 + riesgos R1–R18 con estado | Antes de proponer un cambio de diseño |
| `_memoria/CONTEXTO-REPO.md` | Análisis del repo de Microsoft, hallazgos H1–H11 | Al mapear contenido al sílabo |
| `_memoria/MAPEO-SYLLABUS-REPO.md` | Trazabilidad sesión por sesión: qué cubre el repo y qué se añade | Al escribir una sesión nueva |
| `_memoria/IMPACTO-LLM-PERSONALIZADOS.md` | Por qué se descartó el fine-tuning | Si alguien vuelve a proponerlo |
| `PLAN-CURRICULAR.md` | El plan del curso, v3.0 | Para el contenido de una sesión |
| `docente/cronograma.md` | Las 6 semanas, sesión por sesión | Para fechas y carga |
| `VERIFICACION.md` | Qué verifica cada script y qué significa cada código de salida | Antes de dar algo por bueno |

---

## Cómo trabajar aquí

**Orden obligatorio:** primero investigar y reunir el contenido, después construir el archivo.
Leer una guía de formato antes de tener los datos ancla el trabajo en la mecánica del documento
en vez de en lo que debe decir.

**Documentos generados — no editarlos a mano:**

| Archivo | Lo genera |
|---------|-----------|
| `docente/especificacion-tools.md` | `python docente/generar_especificacion_tools.py` |
| `simulador-industria/docs/REFERENCIA-API.md` | `python simulador-industria/generar_referencia_api.py` |
| `recursos/datasets/**` | `python recursos/datasets/generar_datasets.py` (semilla 20260905) |

Si editas una docstring de tool o una ruta del simulador, **regenera** el documento en el mismo
commit. Esa es la razón de que se generen: no pueden desincronizarse del código.

**Verificadores.** Todos son deterministas y ninguno depende de un modelo, salvo el último:

```bash
python docente/verificar_tools.py              # 24 tools contra los datasets reales
python docente/verificar_structured.py         # 36 comprobaciones de la regla A3, modelo simulado
python recursos/datasets/verificar_datasets.py # 22 comprobaciones, incluye marcas reales
cd simulador-industria && PYTHONPATH=. python verificar_simulador.py   # 33 comprobaciones
python docente/matriz_seleccion.py --simular   # arnés de selección de tools, sin credenciales
python docente/matriz_seleccion.py             # el de verdad: 80 llamadas, necesita HF_TOKEN
python -m comun.check_stack                    # el stack completo: modelo, Qdrant, Langfuse
```

Códigos de salida: `0` todo bien · `1` falla funcional (por ejemplo, por debajo del umbral) ·
`2` falla de infraestructura o de configuración.

**Al cerrar un entregable:** marca la casilla en `ROADMAP.md` y, si tomaste una decisión de
diseño, añádela a `_memoria/DECISIONES.md` con su ID, sus alternativas y su motivo. El valor de
ese archivo está en las alternativas descartadas, no en la elegida.

---

## Errores ya cometidos — no repetirlos

- **Marcas reales filtradas en datasets generados.** Un chequeo por subcadena da falsos positivos
  ("Lima Metropolitana" contiene "Metro"). Usa límite de palabra, como hace el verificador.
- **Afirmar que una demo corre "sin conexión"** cuando descarga un tokenizer. Verifica antes de
  escribirlo.
- **Prometer reproducibilidad sin dejar el generador.** Si generaste datos con un script inline,
  ese script tiene que quedar como archivo permanente.
- **Justificar A1–A6 diciendo "porque es un modelo pequeño".** La razón correcta es la fiabilidad
  compuesta (D20), y sigue siendo válida con un modelo grande.
- **Escribir en un `.md` que el modelo está "especializado por industria".** Es de la etapa previa
  a D21 y ya no es cierto.

---

## Cosas pendientes que dependen de Javier, no del código

- Desplegar el simulador en HF Spaces y repartir las API keys por equipo (`ROADMAP.md` 2B.19).
- Verificar los límites reales del free tier de HF Inference y HF Spaces (riesgos R2, R5, R18).
- Declarar la dedicación de 12 h semanales antes de la matrícula (riesgo R15).
