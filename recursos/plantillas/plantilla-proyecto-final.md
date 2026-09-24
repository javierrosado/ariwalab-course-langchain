# Plantilla de proyecto — el repositorio de tu equipo

> Punto de partida para el repositorio que tu equipo crea en el L1 y hace crecer laboratorio a
> laboratorio hasta el L11 (y, si hacen el bonus, el L12). **No es un archivo que se entrega**:
> es la estructura y el `README.md` inicial que copian a **su propio** repositorio — el que
> vive fuera de este curso, en GitHub o donde su equipo prefiera.
>
> ⚠️ **No es `proyecto-final/<track>/` de este repositorio.** Esa carpeta es la implementación de
> referencia del docente (ya escrita, la que usan `docente/verificar_tools.py` y
> `docente/matriz_seleccion.py`) — ver `README.md` raíz, sección "`proyecto-final/`: qué es y
> qué no es". Un equipo nunca la copia: construye la suya con esta plantilla, un laboratorio a
> la vez.

---

## Estructura completa, para saber hacia dónde crece

La tabla completa de qué laboratorio añade qué archivo vive en
[`docente/labs-incrementales.md`](../../docente/labs-incrementales.md) §1-2 — no se duplica
aquí para no desincronizarse si esa cadena cambia. En resumen, el árbol final (después del L11)
tiene esta forma:

```
tu-repositorio/
├── .env                    (nunca commiteado — ver .gitignore abajo)
├── .env.example
├── requirements.txt
├── data/
├── app/
│   ├── provider.py
│   ├── schemas.py
│   ├── prompts.py
│   ├── tools/
│   ├── knowledge/
│   ├── memory.py
│   ├── guardrails.py
│   ├── agent.py
│   ├── api.py
│   ├── observability.py
│   └── web/index.html
├── Dockerfile
├── tests/
├── evals/
├── host/                    (solo si hacen el bonus de Foundry)
└── README.md
```

No crees estas carpetas todas el primer día: cada una aparece cuando el laboratorio que la
introduce lo pide (columna "Base en el repo" de `labs-incrementales.md` §2).

---

## `.gitignore` mínimo, desde el L1

```gitignore
.env
__pycache__/
*.pyc
.venv/
```

**El `.env` nunca se commitea.** Es la primera lección de higiene de secretos del curso
(`00-preparacion/`) y la que la S8 vuelve a poner a prueba con los *Space secrets*.

---

## `README.md` inicial — plantilla

Copia esto como punto de partida y complétalo laboratorio a laboratorio; para el L11 debe leerse
como documentación viva, no como un enunciado sin llenar.

```markdown
# [Nombre del proyecto] — [Track: telecomunicaciones|banca|retail|seguros]

Agente de IA construido para el curso "Construcción de agentes de IA con LangChain".

**Equipo:** [nombre 1] · [nombre 2]

## Qué hace

[1-2 frases: el caso de uso, para quién]

## Cómo correrlo

1. `python -m venv .venv && source .venv/bin/activate` (o el equivalente en Windows)
2. `pip install -r requirements.txt`
3. Copiar `.env.example` a `.env` y completar las credenciales
4. `python -m comun.check_stack --solo-modelo` para verificar el entorno

## Estado del proyecto

| Laboratorio | Estado |
|---|---|
| L1 · Entorno y primer script | ⬜ |
| L2 · Clasificador de intención | ⬜ |
| L3 · Primera tool (Assignment A1) | ⬜ |
| L4 · Catálogo de 4 tools | ⬜ |
| L5 · Memoria + RAG | ⬜ |
| L6 · Guardrails | ⬜ |
| L7 · Pruebas de estrés (Proyecto M2) | ⬜ |
| L8 · Despliegue en HF Spaces | ⬜ |
| L9 · Observabilidad con Langfuse | ⬜ |
| L10 · Evaluación y optimización | ⬜ |
| L11 · Aplicación final (Proyecto Integrador) | ⬜ |
| L12 · Bonus Foundry *(opcional)* | ⬜ |

## Despliegue

- URL pública: `<se completa en el L8>`
- Documentación de despliegue: [`DESPLIEGUE.md`](DESPLIEGUE.md)

## Documento de diseño

Ver [`documento-diseno.md`](documento-diseno.md) (plantilla en
`recursos/plantillas/plantilla-documento-diseno.md` de este curso).
```

---

## Qué NO va en el repositorio del equipo

| Nunca | Por qué |
|---|---|
| `.env` con credenciales reales | Higiene de secretos, desde el L1 |
| Copias de `proyecto-final/<track>/` de este repo | Es la referencia del docente, no el punto de partida — construir desde cero enseña, copiar no |
| Marcas peruanas reales | Restricción P5 del curso, aunque el proyecto sea un ejercicio |
| Datos de clientes reales | El curso usa datos 100 % sintéticos; no hay razón para desviarse |
