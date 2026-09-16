# -*- coding: utf-8 -*-
"""Genera docs/REFERENCIA-API.md ejecutando el simulador de verdad.

Ejecutar desde la carpeta simulador-industria/:
    PYTHONPATH=. python generar_referencia_api.py

Cada ejemplo del documento es una petición REAL contra los datasets del curso,
con su respuesta REAL. No hay ejemplos inventados: si una ruta cambia, la
referencia cambia con ella al regenerarla.
"""

from __future__ import annotations

import csv
import json
import pathlib
import sys

from fastapi.testclient import TestClient

import app as A
import chaos

RAIZ = pathlib.Path(__file__).resolve().parent
DATASETS = RAIZ.parent / "recursos" / "datasets"
DEMO_KEY = "demo-key-0000"


def primera(track: str, archivo: str, filtro=None) -> dict:
    with open(DATASETS / track / archivo, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            if filtro is None or filtro(fila):
                return fila
    raise RuntimeError(f"Sin filas en {track}/{archivo}")


def bloque(titulo: str, metodo: str, ruta: str, respuesta, codigo: int,
           cuerpo: dict | None = None, nota: str = "") -> list[str]:
    out = [f"#### `{metodo} {ruta}`", ""]
    if nota:
        out += [nota, ""]
    out += ["**Petición**", "", "```bash"]
    if metodo == "GET":
        out.append(f'curl -H "X-API-Key: $SIM_API_KEY" \\\n  "$SIM_BASE_URL{ruta}"')
    else:
        payload = json.dumps(cuerpo, ensure_ascii=False)
        out.append(f'curl -X {metodo} -H "X-API-Key: $SIM_API_KEY" \\\n'
                   f'  -H "Content-Type: application/json" \\\n'
                   f"  -d '{payload}' \\\n  \"$SIM_BASE_URL{ruta}\"")
    out += ["```", "", f"**Respuesta** · `{codigo}`", "", "```json",
            json.dumps(respuesta, ensure_ascii=False, indent=2)[:1400], "```", ""]
    return out


def main() -> None:
    C = TestClient(A.app)
    K = {"X-API-Key": DEMO_KEY}
    doc: list[str] = []

    with C:
        ln = primera("telecomunicaciones", "clientes.csv")["numero_linea"]
        cta = primera("banca", "cuentas.csv")["numero_cuenta"]
        mov = primera("banca", "movimientos.csv")["movimiento_id"]
        sku = primera("retail", "catalogo_productos.csv")["sku"]
        ped = primera("retail", "pedidos.csv", lambda f: f["estado"] == "ENTREGADO")["pedido_id"]
        placa = primera("seguros", "polizas.csv")["placa"]

        doc += [
            "# Referencia de la API del simulador",
            "",
            "> **Generado automáticamente** por `generar_referencia_api.py` ejecutando el",
            "> simulador contra los datasets reales del curso. No editar a mano.",
            "",
            "Todos los ejemplos de esta página son peticiones reales con respuestas reales.",
            "",
            "## Antes de empezar",
            "",
            "```bash",
            'export SIM_BASE_URL="http://localhost:8000"   # o la URL de tu Space',
            'export SIM_API_KEY="demo-key-0000"            # la clave de tu equipo',
            "```",
            "",
            "Todas las rutas de industria exigen la cabecera `X-API-Key`. Las rutas meta",
            "(`/`, `/health`, `/fallos`, `/docs`) no la piden.",
            "",
            "---",
            "",
            "## Índice",
            "",
            "| Industria | Rutas |",
            "|-----------|-------|",
            "| [Telecomunicaciones](#telecomunicaciones--andesmóvil) | 4 |",
            "| [Banca](#banca--banco-inti) | 5 |",
            "| [Retail](#retail--mercasur) | 5 |",
            "| [Seguros](#seguros--andina-seguros) | 5 |",
            "| [Meta y errores](#meta-y-manejo-de-errores) | 3 |",
            "",
            "---",
            "",
            "## Telecomunicaciones · AndesMóvil",
            "",
        ]

        r = C.get(f"/telco/clientes/{ln}", headers=K)
        doc += bloque("cliente", "GET", f"/telco/clientes/{ln}", r.json(), r.status_code,
                      nota="Devuelve el titular, el plan contratado y el estado de la línea. "
                           "El objeto `plan` viene anidado con las condiciones completas.")

        r = C.get(f"/telco/consumo/{ln}?periodo=2026-08", headers=K)
        doc += bloque("consumo", "GET", f"/telco/consumo/{ln}?periodo=2026-08", r.json(), r.status_code,
                      nota="El parámetro `periodo` usa formato `AAAA-MM`. Si no existe, "
                           "el 404 indica qué periodos sí tienen datos.")

        r = C.get("/telco/cobertura/Miraflores", headers=K)
        doc += bloque("cobertura", "GET", "/telco/cobertura/Miraflores", r.json(), r.status_code,
                      nota="`incidencia_activa` en `SI` significa que hay una avería general "
                           "en la zona: explica por sí sola la falla que reporta el cliente.")

        cuerpo = {"numero_linea": ln, "tipo": "AVERIA", "descripcion": "Sin señal desde ayer"}
        r = C.post("/telco/reclamos", headers=K, json=cuerpo)
        doc += bloque("reclamo", "POST", "/telco/reclamos", r.json(), r.status_code, cuerpo,
                      nota="Registra un reclamo formal. El `ticket_id` es la constancia del "
                           "cliente y **debe entregarse siempre**. Tipos válidos: "
                           "`FACTURACION`, `CALIDAD_SERVICIO`, `AVERIA`, `PORTABILIDAD`, "
                           "`CONTRATACION`, `SUSPENSION`.")

        doc += ["---", "", "## Banca · Banco Inti", ""]

        r = C.get(f"/banca/cuentas/{cta}", headers=K)
        doc += bloque("cuenta", "GET", f"/banca/cuentas/{cta}", r.json(), r.status_code,
                      nota="**El simulador nunca devuelve el DNI del titular.** La fuente ya "
                           "viene saneada, así que los guardrails del L6 no parten de cero.")

        r = C.get(f"/banca/movimientos/{cta}?dias=30", headers=K)
        cuerpo_rec = r.json()
        cuerpo_rec["movimientos"] = cuerpo_rec["movimientos"][:3]
        doc += bloque("movimientos", "GET", f"/banca/movimientos/{cta}?dias=30", cuerpo_rec, r.status_code,
                      nota="`dias` acepta entre 1 y 90. *(Ejemplo recortado a 3 movimientos.)*")

        r = C.get(f"/banca/tarjetas/{cta}", headers=K)
        doc += bloque("tarjetas", "GET", f"/banca/tarjetas/{cta}", r.json(), r.status_code,
                      nota="Solo los **últimos 4 dígitos**, nunca el número completo. Si el "
                           "equipo bloqueó la tarjeta, el estado aparece como `BLOQUEADA`.")

        r = C.get(f"/banca/riesgo/{mov}", headers=K)
        doc += bloque("riesgo", "GET", f"/banca/riesgo/{mov}", r.json(), r.status_code,
                      nota="`nivel` es `ALTO` con puntaje ≥ 80, `MEDIO` entre 55 y 79, "
                           "`BAJO` por debajo. Un riesgo ALTO exige derivación a un humano.")

        doc += ["---", "", "## Retail · MercaSur", ""]

        r = C.get(f"/retail/pedidos/{ped}", headers=K)
        doc += bloque("pedido", "GET", f"/retail/pedidos/{ped}", r.json(), r.status_code,
                      nota="Estados posibles: `EN_PREPARACION`, `EN_RUTA`, `ENTREGADO`, "
                           "`LISTO_PARA_RECOJO`, `DEVUELTO`, `CANCELADO`.")

        r = C.get(f"/retail/productos/{sku}", headers=K)
        doc += bloque("producto", "GET", f"/retail/productos/{sku}", r.json(), r.status_code)

        r = C.get(f"/retail/stock/{sku}", headers=K)
        doc += bloque("stock", "GET", f"/retail/stock/{sku}", r.json(), r.status_code)

        cuerpo = {"pedido_id": ped, "motivo": "Llegó dañado", "tipo_solucion": "CAMBIO"}
        r = C.post("/retail/devoluciones", headers=K, json=cuerpo)
        doc += bloque("devolucion", "POST", "/retail/devoluciones", r.json(), r.status_code, cuerpo,
                      nota="**Solo procede sobre pedidos `ENTREGADO`.** Si el pedido está en "
                           "otro estado, el simulador devuelve `409` con la explicación.")

        doc += ["---", "", "## Seguros · Andina Seguros", ""]

        r = C.get(f"/seguros/polizas/{placa}", headers=K)
        doc += bloque("poliza", "GET", f"/seguros/polizas/{placa}", r.json(), r.status_code,
                      nota="`dias_para_vencer` viene calculado. Negativo significa vencida. "
                           "Tampoco expone el DNI del titular.")

        r = C.get(f"/seguros/vehiculos/{placa}", headers=K)
        doc += bloque("vehiculo", "GET", f"/seguros/vehiculos/{placa}", r.json(), r.status_code)

        cuerpo = {"placa": placa, "tipo": "CHOQUE_SIMPLE", "distrito": "Ate", "cantidad_lesionados": 2}
        r = C.post("/seguros/siniestros", headers=K, json=cuerpo)
        doc += bloque("siniestro", "POST", "/seguros/siniestros", r.json(), r.status_code, cuerpo,
                      nota="`prioridad_alta` llega en `true` cuando hay lesionados: es la señal "
                           "de que el agente **debe derivar al canal humano de inmediato**.")
        sid = r.json()["siniestro_id"]

        r = C.get(f"/seguros/siniestros/{sid}", headers=K)
        doc += bloque("consulta siniestro", "GET", f"/seguros/siniestros/{sid}", r.json(), r.status_code,
                      nota="Un equipo solo ve **sus propios** expedientes y los de la semilla.")

        r = C.get("/seguros/clinicas?distrito=Ate", headers=K)
        doc += bloque("clinicas", "GET", "/seguros/clinicas?distrito=Ate", r.json(), r.status_code)

        doc += ["---", "", "## Meta y manejo de errores", ""]

        r = C.get("/health")
        doc += bloque("health", "GET", "/health", r.json(), r.status_code,
                      nota="No requiere API key. Úsala en el checklist previo a cada sesión.")

        doc += ["### Códigos de error y qué debe hacer la tool", "",
                "| Código | Significado | Qué debe hacer tu tool |",
                "|--------|-------------|------------------------|"]

        r = C.get(f"/telco/clientes/{ln}")
        doc.append(f"| `401` | Falta o es inválida la API key | Mensaje claro al agente. **Reintentar no sirve** |")
        r404 = C.get("/telco/clientes/999999999", headers=K)
        doc.append("| `404` | El recurso no existe | Devolver *\"no existe X, verifica el dato\"* |")
        doc.append("| `409` | Conflicto de estado del negocio | Explicar la regla que se incumplió |")
        doc.append("| `422` | Argumento inválido | Indicar los valores admitidos |")
        doc.append("| `500` / `503` | Fallo del servicio | *\"el sistema no responde, reintenta más tarde\"* |")
        doc.append("| *timeout* | El servicio no respondió | Cortar y avisar; nunca colgar el agente |")
        doc += [""]

        doc += ["**Ejemplo de 401** (sin cabecera `X-API-Key`)", "", "```json",
                json.dumps(C.get(f"/telco/clientes/{ln}").json(), ensure_ascii=False, indent=2), "```", "",
                "**Ejemplo de 404**", "", "```json",
                json.dumps(r404.json(), ensure_ascii=False, indent=2), "```", ""]

        doc += ["### Provocar fallos a voluntad", "",
                "Cualquier ruta acepta el parámetro `_fallo`. Existe para que puedas documentar",
                "el escenario *\"API caída\"* que exige la Sesión 3 en vez de simularlo de mentira.", "",
                "| Valor | Qué ocurre |", "|-------|------------|"]
        for k, v in chaos.FALLOS_DISPONIBLES.items():
            doc.append(f"| `{k}` | {v} |")
        doc += ["", "```bash",
                'curl -H "X-API-Key: $SIM_API_KEY" \\\n  "$SIM_BASE_URL/telco/clientes/'
                + ln + '?_fallo=error503"', "```", ""]

        r = C.get(f"/telco/clientes/{ln}?_fallo=error503", headers=K)
        doc += [f"Respuesta · `{r.status_code}`", "", "```json",
                json.dumps(r.json(), ensure_ascii=False, indent=2), "```", ""]

        doc += ["---", "",
                "## Nota sobre los datos", "",
                "Todas las empresas son ficticias y todos los datos son sintéticos (decisión D12).",
                "Los identificadores de los ejemplos provienen de los datasets del curso, así que",
                "puedes copiarlos y ejecutarlos tal cual.", ""]

    destino = RAIZ / "docs" / "REFERENCIA-API.md"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text("\n".join(doc), encoding="utf-8")
    print(f"Generado: {destino.relative_to(RAIZ)} ({destino.stat().st_size:,} bytes)")


if __name__ == "__main__":
    sys.exit(main())
