# Laboratorio L4 · Catálogo de 4 tools

**Objetivo:** que tu agente elija bien entre cuatro herramientas, y que tú lo **midas** — no que
lo supongas.

**Duración:** 2 h.

---

## Antes de empezar

Recuerda la aclaración de la sección "`proyecto-final/`: qué es y qué no es" del `README.md` de
esta sesión: `proyecto-final/<track>/` es la **referencia del docente**, no tu repositorio. Tu
trabajo de hoy va en `lab/<track>/domain_tools.py` (tu copia, en tu propio proyecto), y lo que
mides con `docente/matriz_seleccion.py` es **ese** archivo.

Ya tienes, de tu Laboratorio 3, la primera tool de tu track (la de solo consulta). Hoy añades las
otras tres.

---

## Las 4 tools núcleo por track

| Track | Tool 1 (ya la tienes, del L3) | Tool 2 | Tool 3 | Tool 4 (de escritura) |
|---|---|---|---|---|
| telecomunicaciones | `get_customer_plan` | `get_data_usage` | `run_line_diagnostics` | `create_complaint_ticket` |
| banca | `get_account_balance` | `list_transactions` | `get_card_info` | `score_transaction_risk` *(lectura — ver nota abajo)* |
| retail | `track_order` | `get_product_details` | `check_stock_by_store` | `start_return_request` |
| seguros | `get_policy_by_plate` | `quote_soat` | `get_claim_status` | `open_claim` |

> **Nota — banca no tiene tool de escritura en su núcleo.** Sus 4 tools son de solo lectura a
> propósito: la única acción de escritura del track (`request_card_block`, bloqueo de tarjeta) es
> irreversible, así que queda como **tool opcional** de reto, no como núcleo. Si tu track es
> banca, tu criterio de confirmación (más abajo) no aplica hoy — lo retomas si implementas el
> reto opcional.

---

## Parte 1 · Completa tu catálogo (45 min guiados)

1. Abre tu `lab/<track>/domain_tools.py` (el que empezaste en el L3).
2. Añade las 3 tools que faltan, con su `args_schema` en Pydantic y su docstring completa: qué
   hace, cuándo usarla y **cuándo NO** usarla (regla A2). Usa `comun.datos` para leer los datos
   del track — no inventes un dato que no esté en `recursos/datasets/<tu-track>/`.
3. **Si tu track tiene una tool de escritura en el núcleo** (todos menos banca): antes de
   ejecutar la acción, la tool debe devolver un mensaje de confirmación y solo ejecutarse de
   verdad si el agente la vuelve a llamar con una confirmación explícita del cliente. Mismo
   patrón que ya usa `request_card_block` en banca — mira `solucion/banca/domain_tools.py` como
   referencia de la mecánica, aunque tu tool sea distinta.

## Parte 2 · Ensambla el agente (guiado en la sesión en vivo)

Escribe `lab/<track>/agent.py`: enlaza tus 4 tools al modelo con `bind_tools()`, y arma el bucle
manual (Thought → Action → Observation) con un **tope de iteraciones** — el mismo patrón de
`code/01_multi_tool.py` y `code/03_tope_iteraciones.py`. Sin tope, no se acepta.

## Parte 3 · Mide tu catálogo (25 min)

```bash
python docente/matriz_seleccion.py --track <tu-track> --tools lab/<tu-track>/domain_tools.py
```

Lee la matriz de confusión, no solo el porcentaje. Si algo falla, el propio script te dice qué
docstring corregir (solapamiento, vacío o sobre-uso — ver `README.md` sección 2). Corrige y
vuelve a correr hasta llegar a **≥ 85 %**.

## Parte 4 · Avance 1 del proyecto (10 min)

Media página, entregada al cerrar la sesión:

1. El caso de uso concreto que resuelve tu agente, en una frase.
2. Las 4 tools y **por qué esas cuatro y no otras**.
3. Qué preguntas del cliente **no** resuelve ninguna tool — y qué harás con ellas (pista: la
   respuesta es RAG, y la construyes en la Sesión 5. Anotar el hueco hoy es lo que prepara esa
   sesión).

---

## Criterio de aceptación

- **≥ 85 % de selección correcta** en `docente/matriz_seleccion.py` sobre tu propio catálogo.
- La tool de escritura de tu track (si la tienes) **no se ejecuta sin confirmación**.
- Hay tope de iteraciones y los errores de tool están redactados para que el modelo los entienda
  (regla A4, heredada del L3).

## Reto opcional · no evaluado

Las 2 tools opcionales de tu track (ver `docente/casos-de-uso-industrias.md`), y exponer 2 de tus
propias tools como servidor MCP (ver `pre-work-mcp.md` — hoy te conectaste a uno ajeno; el reto es
construir el tuyo).

---

## Dónde mirar si te atoras

- [`../solucion/<tu-track>/`](../solucion/) — checkpoint de referencia. Compáralo **después** de
  intentarlo, no antes.
- Tabla de errores esperables en el `README.md` de la sesión.
