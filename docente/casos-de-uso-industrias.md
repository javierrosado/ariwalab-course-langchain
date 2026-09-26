# Los 4 tracks de industria — casos de uso peruanos

> **Regla de asignación (fijada en la Sesión 1): el equipo propone,
> el docente balancea.** Cada equipo propone su track al cerrar la Sesión 1 en vivo; el
> docente ajusta la propuesta para que los 4 tracks queden representados en la sustentación
> final. Una vez asignado, el track es **irrevocable** y se mantiene hasta la aplicación
> final. Los cuatro tracks comparten el mismo esqueleto de código (`comun/`) y difieren en
> dominio, datos y herramientas.
>
> **4 tools núcleo por track:** la precisión de selección cae pasadas 4-5
> herramientas, y la fiabilidad se compone a lo largo del bucle del agente. Las 2 restantes quedan como reto opcional.
>
> **Marcas ficticias.** Los casos son reconocibles en el mercado peruano,
> pero ninguna empresa real es nombrada ni representada, y todos los datos son sintéticos.

---

## Track A · Telecomunicaciones — "AndesMóvil"

**Caso de uso:** *Agente de atención al cliente de telefonía móvil postpago.*

**Por qué es reconocible en Perú:** la atención al cliente móvil es el sector con mayor volumen
de reclamos ante OSIPTEL. Todo peruano ha pasado por el flujo "consultar mi plan → reportar avería →
generar código de reclamo → evaluar portabilidad".

| Elemento | Definición |
|---|---|
| Usuario final | Titular de línea postpago |
| Objetivo del agente | Resolver en primer contacto consultas de plan, consumo, avería y portabilidad |
| Tools núcleo (L4, máx. 4 por A1) | `get_customer_plan`, `get_data_usage`, `run_line_diagnostics`, `create_complaint_ticket` |
| Tools opcionales (reto) | `check_portability_eligibility`, `get_coverage_by_district` |
| Base de conocimiento (RAG) | Tarifario de planes, condiciones contractuales, procedimiento de reclamos OSIPTEL, cobertura por distrito de Lima |
| Datos sintéticos | `clientes.csv`, `planes.json`, `consumo_datos.csv`, `tickets_reclamos.csv`, `cobertura_distritos.csv`, `tarifario_planes.md`, `condiciones_portabilidad.md`, `reglamento_reclamos.md` |
| API externa (Sesión 3) | Servicio mock REST de estado de red por distrito |
| Guardrail crítico | No prometer compensaciones económicas; no revelar datos de otra línea; enmascarar DNI |
| Métrica de éxito (Sesión 10) | % de consultas resueltas sin escalamiento + uso correcto de la tool de diagnóstico |

---

## Track B · Banca — "Banco Inti"

**Caso de uso:** *Asistente de banca personal con detección de operación sospechosa.*

**Por qué es reconocible en Perú:** la masificación de Yape/Plin disparó tanto las consultas de
movimientos como los intentos de fraude por suplantación. Es el caso con mayor exigencia
regulatoria, ideal para enseñar guardrails.

| Elemento | Definición |
|---|---|
| Usuario final | Cliente de cuenta de ahorros / tarjeta de crédito |
| Objetivo del agente | Consultar movimientos, explicar comisiones, gestionar límites y alertar operaciones sospechosas |
| Tools núcleo (L4, máx. 4 por A1) | `get_account_balance`, `list_transactions`, `get_card_info`, `score_transaction_risk` |
| Tools opcionales (reto) | `get_transfer_limits`, `request_card_block` |
| Base de conocimiento (RAG) | Tarifario de comisiones, contrato de tarjeta, política de fraude |
| Datos sintéticos | `cuentas.csv`, `movimientos.csv`, `tarjetas.csv`, `alertas_riesgo.csv`, `tarifario_comisiones.md`, `politica_fraude.md`, `contrato_tarjeta.md` |
| API externa (Sesión 3) | Servicio mock de tipo de cambio SBS + scoring de riesgo |
| Guardrail crítico | **Nunca ejecutar transferencias**; jamás mostrar número de tarjeta completo (solo últimos 4); doble confirmación antes de bloquear; escalamiento obligatorio ante sospecha de fraude |
| Métrica de éxito (Sesión 10) | Tasa de falsos positivos de fraude + cero fugas de PII en 100 conversaciones de prueba |

> Este track es el que mejor conecta con el enfoque de **gobierno de IA**: se usa para enseñar
> trazabilidad regulatoria (Sesión 9) y evidencia auditable de decisiones del agente.

---

## Track C · Retail — "MercaSur"

**Caso de uso:** *Agente de post-venta de e-commerce: pedido, cambio y devolución.*

**Por qué es reconocible en Perú:** el pico de Cyber Days y Navidad satura la post-venta;
el Libro de Reclamaciones y las reglas de Indecopi sobre cambios y devoluciones son de
conocimiento general.

| Elemento | Definición |
|---|---|
| Usuario final | Comprador online con pedido en curso |
| Objetivo del agente | Informar estado del pedido, gestionar cambio/devolución, verificar stock y registrar reclamo |
| Tools núcleo (L4, máx. 4 por A1) | `track_order`, `check_stock_by_store`, `start_return_request`, `get_product_details` |
| Tools opcionales (reto) | `estimate_delivery`, `get_return_status` |
| Base de conocimiento (RAG) | Política de cambios y devoluciones, términos de garantía, preguntas frecuentes de despacho, reglas del Libro de Reclamaciones |
| Datos sintéticos | `pedidos.csv`, `catalogo_productos.csv`, `stock_tiendas.csv`, `devoluciones.csv`, `politica_devoluciones.md`, `terminos_garantia.md`, `faq_despacho.md` |
| API externa (Sesión 3) | Servicio mock de courier (estado de tracking) |
| Guardrail crítico | No autorizar devoluciones fuera de política; no prometer fechas de entrega no confirmadas por el courier |
| Métrica de éxito (Sesión 10) | Exactitud de la política aplicada (groundedness contra el documento fuente) |

---

## Track D · Seguros — "Andina Seguros"

**Caso de uso:** *Asesor de SOAT y pre-liquidación de siniestro vehicular.*

**Por qué es reconocible en Perú:** el SOAT es obligatorio para todo vehículo, y el flujo
"cotizar → entender cobertura → reportar siniestro → seguir el trámite" es universal entre
propietarios de auto.

| Elemento | Definición |
|---|---|
| Usuario final | Propietario de vehículo particular |
| Objetivo del agente | Cotizar, explicar coberturas y exclusiones, guiar el reporte de siniestro y consultar el estado del trámite |
| Tools núcleo (L4, máx. 4 por A1) | `get_policy_by_plate`, `quote_soat`, `get_claim_status`, `open_claim` |
| Tools opcionales (reto) | `list_affiliated_clinics`, `get_vehicle_info` |
| Base de conocimiento (RAG) | Condicionado general SOAT, tabla de coberturas y topes en UIT, exclusiones, procedimiento de siniestro, red de clínicas afiliadas |
| Datos sintéticos | `polizas.csv`, `vehiculos.csv`, `red_clinicas.csv`, `siniestros.csv`, `condicionado_soat.md`, `tabla_coberturas.md`, `procedimiento_siniestro.md` |
| API externa (Sesión 3) | Servicio mock de consulta de placa vehicular + valor de la UIT |
| Guardrail crítico | **No liquidar ni aprobar siniestros**: el agente solo pre-califica e informa; toda cifra debe citar el condicionado; derivar lesiones personales a canal humano de inmediato |
| Métrica de éxito (Sesión 10) | Citación correcta de la cláusula del condicionado en el 100 % de las respuestas de cobertura |

---

## Cuadro comparativo de los 4 tracks

| Criterio | Telco (A) | Banca (B) | Retail (C) | Seguros (D) |
|---|---|---|---|---|
| Dificultad técnica | Media | **Alta** | Baja | Media-alta |
| Nº de tools núcleo | 4 | 4 | 4 | 4 |
| Volumen del corpus RAG | Medio | Alto | Bajo | **Alto** (condicionado legal) |
| Exigencia de guardrails | Media | **Máxima** | Baja | Alta |
| Necesidad de structured output | Alta (ticket de reclamo) | Alta (score de riesgo) | Media (solicitud de devolución) | **Máxima** (pre-liquidación) |
| Dificultad de la evaluación (S10) | Media | Alta | **Baja** | Alta |
| Recomendado para equipos | Con experiencia en integración | Con perfil de arquitectura/riesgo | **Que parten de cero** | Con gusto por el dominio legal |

**Regla de balanceo para el docente** (la misma de la Sesión 1, sección "Elección de
track"): el equipo **propone** su track, no se le asigna de entrada. El docente solo ajusta
la propuesta cuando hace falta para que los 4 tracks estén representados en la sustentación
final y para que **Banca** —el más exigente en guardrails y structured output, ver el cuadro
comparativo de arriba— no caiga en el equipo más débil. Retail, por su menor exigencia técnica,
es la opción natural para sugerirle a un equipo que parte de cero si ese equipo no tiene
preferencia propia.
