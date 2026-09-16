# Datasets sintéticos del curso

Todos los datos de esta carpeta son **sintéticos y generados por script**. Las empresas son
ficticias (AndesMóvil, Banco Inti, MercaSur, Andina Seguros) y ninguna persona, cuenta, placa o
documento corresponde a alguien real. Decisión D12 del ADR.

## Cómo se usa cada tipo de archivo

| Tipo | Destino | Sesión |
|---|---|---|
| `.csv` / `.json` | Respaldan las **tools** del agente (APIs mock del dominio) | L3, L4 |
| `.md` | Se indexan en **Qdrant Cloud** como base de conocimiento del RAG | L5 |

La separación es deliberada y es la lección de la sesión 5: **los datos transaccionales se
consultan con una tool; las políticas, tarifarios y condicionados se recuperan con RAG.** Un agente
que intenta recordar un tarifario en vez de recuperarlo es el error que el curso enseña a evitar.

## Contenido por track

### telecomunicaciones · AndesMóvil
| Archivo | Filas | Uso |
|---|---|---|
| `clientes.csv` | 50 | tool `get_customer_plan` |
| `planes.json` | 5 | tool `get_customer_plan` |
| `consumo_datos.csv` | 100 | tool `get_data_usage` |
| `cobertura_distritos.csv` | 20 | tool `run_line_diagnostics` |
| `tickets_reclamos.csv` | 40 | tool `create_complaint_ticket` |
| `tarifario_planes.md` | — | RAG |
| `reglamento_reclamos.md` | — | RAG |
| `condiciones_portabilidad.md` | — | RAG |

### banca · Banco Inti
| Archivo | Filas | Uso |
|---|---|---|
| `cuentas.csv` | 40 | tool `get_account_balance` |
| `movimientos.csv` | 400 | tool `list_transactions` |
| `tarjetas.csv` | 30 | tools de tarjeta |
| `alertas_riesgo.csv` | 25 | tool `score_transaction_risk` |
| `tarifario_comisiones.md` | — | RAG |
| `politica_fraude.md` | — | RAG |
| `contrato_tarjeta.md` | — | RAG |

### retail · MercaSur
| Archivo | Filas | Uso |
|---|---|---|
| `pedidos.csv` | 50 | tool `track_order` |
| `catalogo_productos.csv` | 42 | tool `get_product_details` |
| `stock_tiendas.csv` | 252 | tool `check_stock_by_store` |
| `devoluciones.csv` | 30 | tool `start_return_request` |
| `politica_devoluciones.md` | — | RAG |
| `faq_despacho.md` | — | RAG |
| `terminos_garantia.md` | — | RAG |

### seguros · Andina Seguros
| Archivo | Filas | Uso |
|---|---|---|
| `polizas.csv` | 45 | tool `get_policy_by_plate` |
| `vehiculos.csv` | 45 | tool `quote_soat` |
| `siniestros.csv` | 35 | tool `open_claim` |
| `red_clinicas.csv` | 8 | tool opcional `list_affiliated_clinics` |
| `condicionado_soat.md` | — | RAG |
| `tabla_coberturas.md` | — | RAG |
| `procedimiento_siniestro.md` | — | RAG |

## Nota para el fine-tuning de los modelos

Si se sigue el camino B de `_memoria/ESPEC-MODELOS-INDUSTRIA.md`, el dataset de entrenamiento
**no debe contener** las tarifas, coberturas ni políticas de los archivos `.md` de esta carpeta.
Ese conocimiento vive en el RAG. Si el modelo lo memoriza, dejará de llamar al retriever y se
romperá el criterio de aceptación C6 y la lección central de la sesión 5.

## Política de marcas (decisión D12)

Ninguna empresa, comercio, courier, tienda, billetera ni clínica de estos datos es real. Dos
excepciones deliberadas y documentadas:

| Excepción | Por qué se permite |
|---|---|
| **Marcas de vehículos** en el track de seguros (Toyota, Kia, …) | La marca de un auto es un atributo factual del bien asegurado, como el año o el número de asientos. No es un proveedor de servicio suplantado |
| **Reguladores y organismos públicos** (OSIPTEL, Indecopi, SBS, UIT) | Son el marco normativo real del caso peruano y su conocimiento es parte del valor formativo del curso. No son marcas comerciales |

`verificar_datasets.py` comprueba automáticamente que no se cuelen marcas comerciales reales.

## Scripts

| Script | Qué hace |
|---|---|
| `generar_datasets.py` | Regenera todos los archivos estructurados. Semilla fija |
| `verificar_datasets.py` | Coherencia referencial, rangos válidos y política de marcas. Sale con código 1 si algo falla |

```bash
python recursos/datasets/generar_datasets.py
python recursos/datasets/verificar_datasets.py
```

## Reproducibilidad

Los archivos estructurados se generaron con semilla fija (`random.seed(20260905)`), de modo que
regenerarlos produce exactamente los mismos datos.
