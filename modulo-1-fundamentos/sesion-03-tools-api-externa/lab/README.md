# Laboratorio L3 = Assignment A1 · Primera tool contra el simulador

**Objetivo:** el modelo deja de "saber" y empieza a "consultar". Esta es la primera de las 4
tools que completarás en el Laboratorio 4 — no un ejercicio aislado.

**Duración:** 2 h. Ver el enunciado completo, con rúbrica y fechas de entrega, en
[`../assignment-a1.md`](../assignment-a1.md).

---

## Tu tool (una sola, de lectura)

| Track | Tool | Ruta del simulador | Categoría del L2 que resuelve |
|---|---|---|---|
| telecomunicaciones | `get_customer_plan` | `GET /telco/clientes/{numero_linea}` | `CONSULTA_PLAN` |
| banca | `get_account_balance` | `GET /banca/cuentas/{numero_cuenta}` | `CONSULTA_SALDO` |
| retail | `track_order` | `GET /retail/pedidos/{pedido_id}` | `SEGUIMIENTO_PEDIDO` |
| seguros | `get_policy_by_plate` | `GET /seguros/polizas/{placa}` | `CONSULTA_POLIZA` |

```
   L2   clasifica  (la categoría de tu track, por ejemplo CONSULTA_PLAN)
   L3   construye  la tool de esa categoría               ← HOY
   L4   completa   + las otras 3 del catálogo
```

Usa `comun.datos.buscar_uno(...)` dentro de tu tool — es lo mismo que ya usaste en la Sesión 1,
pero ahora con `DATA_SOURCE=api` en tu `.env`: la llamada va al simulador real, no al CSV local,
sin que tu tool sepa la diferencia. Esa indirección es la lección del laboratorio.

---

## Parte 1 · Práctica guiada (40 min, en la sesión en vivo)

Escribes la tool junto con el docente, con `args_schema` y docstring completa (regla A2).

## Parte 2 · Los 3 escenarios con `?_fallo=` (25 min)

| # | Escenario | Cómo se provoca | Qué debe hacer el agente |
|---|---|---|---|
| 1 | **Éxito** | Un identificador real del dataset de tu track | Llama la tool y responde citando el dato |
| 2 | **Dato inexistente** | Un identificador que no existe → 404 | La tool dice "no existe"; el agente **no inventa** ni reintenta |
| 3 | **Servicio caído** | `?_fallo=error503` sobre la URL del simulador | El agente avisa al cliente y **no entra en bucle** de reintentos |

## Parte 3 · Rúbrica y reparto (15 min)

Ver [`../assignment-a1.md`](../assignment-a1.md) para la rúbrica completa, la regla del piso y
el calendario de entrega y sustentación.

---

## Entregables

| Entregable | Ruta | Para qué |
|---|---|---|
| `tools/external_api.py` | tu proyecto | La tool, con docstring A2 y `args_schema` |
| `agent.py` v1 | tu proyecto | `create_agent()` con esa única tool y el prompt de tu track |
| **`prueba_tool.py`** | tu proyecto | Llama la tool **directamente**, sin modelo, en los 3 escenarios |
| `EVIDENCIA-A1.md` | tu proyecto | Las 3 trazas reales pegadas + qué se decidió en cada caso |

> **`prueba_tool.py` es la pieza que sostiene la regla del piso.** Separa la calidad de tu
> herramienta de la varianza del modelo: si la tool se comporta bien llamada directamente, tu
> diseño está probado, aunque en la demo el modelo no la haya elegido esa vez.

## Reto opcional · no evaluado

`?_fallo=malformado` — un `200` con un JSON que no cumple el contrato esperado. Es el más
difícil porque **no hay código de error**: solo se detecta validando la forma de la respuesta.
Es el puente hacia los guardrails de la Sesión 6.

---

## Si te atoras

- [`../solucion/<tu-track>/`](../solucion/) — checkpoint de referencia.
- Tabla de errores esperables en el `README.md` de la sesión.
