# Especificación de las tools del curso

> **Generado automáticamente** por `docente/generar_especificacion_tools.py` a partir del código
> real. No editar a mano: regenerar tras cualquier cambio en las tools.
>
> **Para el profesor:** el curso usa un modelo genérico sin afinar (decisión D21), así que
> **la única guía que tiene el modelo para elegir bien una herramienta es lo que está escrito
> aquí**. Si `docente/matriz_seleccion.py` reporta una confusión entre dos tools, la corrección
> se hace sobre la docstring de este documento, no sobre el modelo.

## Reglas de diseño aplicadas

| Regla | Qué exige | Por qué |
|-------|-----------|---------|
| **A1** | Máximo **4 tools núcleo** enlazadas a la vez | La precisión de selección cae pasadas 4-5 herramientas y los errores se componen |
| **A2** | Toda docstring dice **cuándo NO** usar la tool | Una descripción ambigua se paga en cada paso del bucle |
| **A4** | Los errores se devuelven como **texto legible**, nunca como excepción | El agente necesita leer "no existe esa línea" para replantear su plan |

Las 2 tools opcionales de cada track quedan como reto del Laboratorio 4 y **no** deben
enlazarse junto a las 4 núcleo.

---


## Track `telecomunicaciones` — AndesMóvil

*Atención al cliente móvil postpago*


### Tools núcleo (Laboratorio 4)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `get_customer_plan` | `numero_linea` | Devuelve el plan contratado, el estado y el distrito de una línea móvil. |
| `get_data_usage` | `numero_linea`, `periodo` | Devuelve el consumo de datos, minutos y SMS de una línea en un periodo. |
| `run_line_diagnostics` | `numero_linea` | Ejecuta un diagnóstico técnico de la línea y de la cobertura de su distrito. |
| `create_complaint_ticket` | `numero_linea`, `tipo`, `descripcion` | Registra un reclamo formal y devuelve su código de seguimiento. |

### Tools opcionales (reto)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `check_portability_eligibility` | `numero_linea` | Verifica si una línea puede portarse a otra operadora y qué obligaciones quedan pendientes. |
| `get_coverage_by_district` | `distrito` | Consulta la cobertura y las incidencias activas de un distrito. |

<details>
<summary><b>Esquemas JSON completos (formato OpenAI)</b></summary>

```json
[
  {
    "type": "function",
    "function": {
      "name": "get_customer_plan",
      "description": "Devuelve el plan contratado, el estado y el distrito de una línea móvil.\n\n    Úsala cuando el cliente pregunte qué plan tiene, cuánto paga, desde cuándo es\n    cliente, o si su línea está activa o suspendida.\n    NO la uses para consultar consumo de datos: para eso usa get_data_usage.\n    NO la uses para preguntas generales sobre el catálogo de planes de AndesMóvil:\n    esa información está en la base de conocimiento, no aquí.",
      "parameters": {
        "properties": {
          "numero_linea": {
            "description": "Número de línea móvil de 9 dígitos, sin espacios ni guiones",
            "type": "string"
          }
        },
        "required": [
          "numero_linea"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_data_usage",
      "description": "Devuelve el consumo de datos, minutos y SMS de una línea en un periodo.\n\n    Úsala cuando el cliente pregunte cuántos gigas ha consumido, cuánto le queda,\n    o por qué se le acabaron los datos.\n    NO la uses para saber qué plan tiene: para eso usa get_customer_plan.",
      "parameters": {
        "properties": {
          "numero_linea": {
            "description": "Número de línea móvil de 9 dígitos",
            "type": "string"
          },
          "periodo": {
            "default": "2026-08",
            "description": "Periodo de facturación en formato AAAA-MM",
            "type": "string"
          }
        },
        "required": [
          "numero_linea"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "run_line_diagnostics",
      "description": "Ejecuta un diagnóstico técnico de la línea y de la cobertura de su distrito.\n\n    Úsala cuando el cliente reporte que no tiene señal, que la navegación está lenta,\n    que se cortan las llamadas, o cualquier falla técnica del servicio.\n    NO la uses para consultas de facturación ni de consumo.",
      "parameters": {
        "properties": {
          "numero_linea": {
            "description": "Número de línea móvil de 9 dígitos, sin espacios ni guiones",
            "type": "string"
          }
        },
        "required": [
          "numero_linea"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "create_complaint_ticket",
      "description": "Registra un reclamo formal y devuelve su código de seguimiento.\n\n    Úsala SOLO cuando el cliente pida explícitamente registrar un reclamo o manifieste\n    disconformidad que no se resolvió con la información entregada.\n    NO la uses para consultas ni para pedidos de información: eso no es un reclamo.\n    NO la uses más de una vez por conversación sin confirmarlo con el cliente.",
      "parameters": {
        "properties": {
          "numero_linea": {
            "description": "Número de línea móvil de 9 dígitos",
            "type": "string"
          },
          "tipo": {
            "description": "FACTURACION, CALIDAD_SERVICIO, AVERIA, PORTABILIDAD, CONTRATACION o SUSPENSION",
            "type": "string"
          },
          "descripcion": {
            "description": "Descripción del problema en palabras del cliente, máximo 200 caracteres",
            "type": "string"
          }
        },
        "required": [
          "numero_linea",
          "tipo",
          "descripcion"
        ],
        "type": "object"
      }
    }
  }
]
```
</details>


---

## Track `banca` — Banco Inti

*Banca personal y detección de operación sospechosa*


### Tools núcleo (Laboratorio 4)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `get_account_balance` | `numero_cuenta` | Devuelve el saldo, la moneda y el estado de una cuenta. |
| `list_transactions` | `numero_cuenta`, `dias` | Lista los movimientos de una cuenta en los últimos N días, del más reciente al más antiguo. |
| `get_card_info` | `numero_cuenta` | Devuelve los datos de la tarjeta asociada a una cuenta, con el número enmascarado. |
| `score_transaction_risk` | `movimiento_id` | Devuelve el puntaje de riesgo de fraude de un movimiento y el motivo de la alerta. |

### Tools opcionales (reto)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `get_transfer_limits` | `numero_cuenta` | Devuelve los límites de transferencia vigentes de una cuenta. |
| `request_card_block` | `tarjeta_id`, `confirmado_por_cliente` | Prepara el bloqueo de una tarjeta. El bloqueo es IRREVERSIBLE. |

<details>
<summary><b>Esquemas JSON completos (formato OpenAI)</b></summary>

```json
[
  {
    "type": "function",
    "function": {
      "name": "get_account_balance",
      "description": "Devuelve el saldo, la moneda y el estado de una cuenta.\n\n    Úsala cuando el cliente pregunte cuánto tiene, su saldo disponible,\n    o si su cuenta está activa o bloqueada.\n    NO la uses para ver movimientos o consumos: para eso usa list_transactions.",
      "parameters": {
        "properties": {
          "numero_cuenta": {
            "description": "Número de cuenta en formato 191-XXXXXXX-0-XX",
            "type": "string"
          }
        },
        "required": [
          "numero_cuenta"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "list_transactions",
      "description": "Lista los movimientos de una cuenta en los últimos N días, del más reciente al más antiguo.\n\n    Úsala cuando el cliente pregunte por sus consumos, sus últimos movimientos,\n    un cargo que no reconoce, o cuánto gastó en un periodo.\n    NO la uses para consultar el saldo: para eso usa get_account_balance.",
      "parameters": {
        "properties": {
          "numero_cuenta": {
            "description": "Número de cuenta en formato 191-XXXXXXX-0-XX",
            "type": "string"
          },
          "dias": {
            "default": 30,
            "description": "Días hacia atrás a consultar, entre 1 y 90",
            "maximum": 90,
            "minimum": 1,
            "type": "integer"
          }
        },
        "required": [
          "numero_cuenta"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_card_info",
      "description": "Devuelve los datos de la tarjeta asociada a una cuenta, con el número enmascarado.\n\n    Úsala cuando el cliente pregunte por su tarjeta, su línea de crédito,\n    su fecha de facturación o si su tarjeta está activa.\n    NO la uses para bloquear la tarjeta: para eso usa request_card_block.\n    Esta tool NUNCA devuelve el número completo de la tarjeta, solo los últimos 4 dígitos.",
      "parameters": {
        "properties": {
          "numero_cuenta": {
            "description": "Número de cuenta en formato 191-XXXXXXX-0-XX",
            "type": "string"
          }
        },
        "required": [
          "numero_cuenta"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "score_transaction_risk",
      "description": "Devuelve el puntaje de riesgo de fraude de un movimiento y el motivo de la alerta.\n\n    Úsala cuando el cliente diga que no reconoce una operación, sospeche de un cargo,\n    o pregunte por qué le llegó una alerta de seguridad.\n    NO la uses para listar movimientos: primero usa list_transactions para obtener el\n    movimiento_id, y recién entonces evalúa el riesgo de ese movimiento concreto.",
      "parameters": {
        "properties": {
          "movimiento_id": {
            "description": "Identificador del movimiento en formato MOV-NNNNNNN",
            "type": "string"
          }
        },
        "required": [
          "movimiento_id"
        ],
        "type": "object"
      }
    }
  }
]
```
</details>


---

## Track `retail` — MercaSur

*Post-venta de e-commerce*


### Tools núcleo (Laboratorio 4)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `track_order` | `pedido_id` | Devuelve el estado, el courier y el código de rastreo de un pedido. |
| `get_product_details` | `sku` | Devuelve el nombre, la categoría, el precio, la garantía y si un producto admite cambio. |
| `check_stock_by_store` | `sku` | Devuelve el stock disponible de un producto en cada tienda MercaSur. |
| `start_return_request` | `pedido_id`, `motivo`, `tipo_solucion` | Inicia una solicitud de cambio o devolución y devuelve su código de seguimiento. |

### Tools opcionales (reto)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `estimate_delivery` | `distrito`, `monto_compra` | Calcula el costo y el plazo de despacho para un distrito y un monto de compra. |
| `get_return_status` | `pedido_id` | Consulta el estado de las devoluciones asociadas a un pedido. |

<details>
<summary><b>Esquemas JSON completos (formato OpenAI)</b></summary>

```json
[
  {
    "type": "function",
    "function": {
      "name": "track_order",
      "description": "Devuelve el estado, el courier y el código de rastreo de un pedido.\n\n    Úsala cuando el cliente pregunte dónde está su pedido, cuándo llega,\n    o por qué no lo ha recibido.\n    NO la uses para iniciar una devolución: para eso usa start_return_request.",
      "parameters": {
        "properties": {
          "pedido_id": {
            "description": "Número de pedido en formato MS-2026-NNNNN",
            "type": "string"
          }
        },
        "required": [
          "pedido_id"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_product_details",
      "description": "Devuelve el nombre, la categoría, el precio, la garantía y si un producto admite cambio.\n\n    Úsala cuando el cliente pregunte por las características, el precio o la garantía\n    de un producto concreto.\n    NO la uses para saber si hay stock: para eso usa check_stock_by_store.",
      "parameters": {
        "properties": {
          "sku": {
            "description": "Código de producto en formato MS-NNNN",
            "type": "string"
          }
        },
        "required": [
          "sku"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "check_stock_by_store",
      "description": "Devuelve el stock disponible de un producto en cada tienda MercaSur.\n\n    Úsala cuando el cliente pregunte si hay disponibilidad, en qué tienda puede\n    recogerlo, o si puede cambiar su producto por otro igual.\n    NO la uses para consultar el precio o la garantía: para eso usa get_product_details.",
      "parameters": {
        "properties": {
          "sku": {
            "description": "Código de producto en formato MS-NNNN",
            "type": "string"
          }
        },
        "required": [
          "sku"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "start_return_request",
      "description": "Inicia una solicitud de cambio o devolución y devuelve su código de seguimiento.\n\n    Úsala cuando el cliente pida devolver, cambiar o reembolsar un producto ya recibido.\n    NO la uses si el pedido aún no fue entregado: en ese caso corresponde una anulación,\n    no una devolución.\n    NO apruebes la devolución: esta tool solo registra la solicitud; la autorización\n    corresponde al área de post-venta.",
      "parameters": {
        "properties": {
          "pedido_id": {
            "description": "Número de pedido en formato MS-2026-NNNNN",
            "type": "string"
          },
          "motivo": {
            "description": "Motivo del cliente, por ejemplo 'Producto con falla' o 'Talla incorrecta'",
            "type": "string"
          },
          "tipo_solucion": {
            "default": "CAMBIO",
            "description": "CAMBIO, REEMBOLSO o NOTA_CREDITO",
            "type": "string"
          }
        },
        "required": [
          "pedido_id",
          "motivo"
        ],
        "type": "object"
      }
    }
  }
]
```
</details>


---

## Track `seguros` — Andina Seguros

*Asesoría SOAT y reporte de siniestros*


### Tools núcleo (Laboratorio 4)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `get_policy_by_plate` | `placa` | Devuelve la póliza SOAT asociada a una placa, con su vigencia y estado. |
| `quote_soat` | `placa` | Cotiza la prima del SOAT para un vehículo según su categoría y uso. |
| `get_claim_status` | `siniestro_id` | Consulta el estado de un expediente de siniestro por su código. |
| `open_claim` | `placa`, `tipo`, `distrito`, `cantidad_lesionados` | Registra el reporte inicial de un siniestro y devuelve el código de expediente. |

### Tools opcionales (reto)

| Tool | Parámetros | Qué hace |
|------|-----------|----------|
| `list_affiliated_clinics` | `distrito` | Lista las clínicas de la red afiliada de Andina Seguros en un distrito. |
| `get_vehicle_info` | `placa` | Devuelve los datos del vehículo registrado bajo una placa. |

<details>
<summary><b>Esquemas JSON completos (formato OpenAI)</b></summary>

```json
[
  {
    "type": "function",
    "function": {
      "name": "get_policy_by_plate",
      "description": "Devuelve la póliza SOAT asociada a una placa, con su vigencia y estado.\n\n    Úsala cuando el cliente pregunte si su SOAT está vigente, hasta cuándo,\n    o quiera los datos de su póliza.\n    NO la uses para cotizar una póliza nueva: para eso usa quote_soat.",
      "parameters": {
        "properties": {
          "placa": {
            "description": "Placa del vehículo en formato ABC-123",
            "type": "string"
          }
        },
        "required": [
          "placa"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "quote_soat",
      "description": "Cotiza la prima del SOAT para un vehículo según su categoría y uso.\n\n    Úsala cuando el cliente pregunte cuánto le costaría el SOAT o quiera renovar.\n    NO la uses para consultar una póliza ya contratada: para eso usa get_policy_by_plate.",
      "parameters": {
        "properties": {
          "placa": {
            "description": "Placa del vehículo en formato ABC-123",
            "type": "string"
          }
        },
        "required": [
          "placa"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_claim_status",
      "description": "Consulta el estado de un expediente de siniestro por su código.\n\n    Úsala cuando el cliente pregunte en qué va su trámite o cuándo le pagarán.\n    NO uses esta tool para afirmar montos a pagar: el monto estimado es referencial\n    y la liquidación la determina el área de siniestros, no el asistente.",
      "parameters": {
        "properties": {
          "siniestro_id": {
            "description": "Código de expediente en formato SIN-2026-NNNNN",
            "type": "string"
          }
        },
        "required": [
          "siniestro_id"
        ],
        "type": "object"
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "open_claim",
      "description": "Registra el reporte inicial de un siniestro y devuelve el código de expediente.\n\n    Úsala cuando el cliente comunique un accidente de tránsito que aún no ha reportado.\n    NO la uses para consultar un siniestro existente: para eso usa get_claim_status.\n    Esta tool SOLO registra el reporte: no aprueba, no liquida y no estima indemnizaciones.",
      "parameters": {
        "properties": {
          "placa": {
            "description": "Placa del vehículo asegurado en formato ABC-123",
            "type": "string"
          },
          "tipo": {
            "description": "CHOQUE_SIMPLE, ATROPELLO, VOLCADURA, COLISION_MULTIPLE o DESPISTE",
            "type": "string"
          },
          "distrito": {
            "description": "Distrito donde ocurrió el accidente",
            "type": "string"
          },
          "cantidad_lesionados": {
            "description": "Número de personas lesionadas, 0 si no hay",
            "maximum": 20,
            "minimum": 0,
            "type": "integer"
          }
        },
        "required": [
          "placa",
          "tipo",
          "distrito",
          "cantidad_lesionados"
        ],
        "type": "object"
      }
    }
  }
]
```
</details>


---

## Cómo se ve una llamada a herramienta en el protocolo

Los cinco mensajes de un ciclo ReAct completo, tal como viajan por el cable. Útil para depurar
cuando una traza de Langfuse no cuadra, y para entender qué recibe realmente el modelo:

```jsonl
{"messages": [{"role": "system", "content": "Eres el asistente de AndesMóvil, operador móvil peruano."}, {"role": "user", "content": "¿Qué plan tengo en la 987654321?"}, {"role": "assistant", "content": "", "tool_calls": [{"type": "function", "function": {"name": "get_customer_plan", "arguments": "{\"numero_linea\": \"987654321\"}"}}]}, {"role": "tool", "name": "get_customer_plan", "content": "Línea 987654321 · Plan: Max 89 (AM-MAX-89) · Estado: ACTIVO"}, {"role": "assistant", "content": "Tienes el plan Max 89, que incluye 30 GB de datos. Tu línea está activa."}]}
```

## Verificación

```bash
python docente/verificar_tools.py
```

Comprueba que las 24 tools corren contra los datasets reales, que ninguna lanza excepción ante
datos inexistentes, que toda docstring cumple A2 y que ningún track supera las 4 tools núcleo.
No requiere credenciales ni acceso a un modelo.

```bash
python docente/matriz_seleccion.py --track telecomunicaciones
```

Mide si el modelo **elige** la herramienta correcta: 20 consultas por track contra la tool
esperada, con matriz de confusión. Este sí requiere `HF_TOKEN`; usa `--simular` para probar el
arnés sin gastar cuota.
