# -*- coding: utf-8 -*-
"""Verificador de integridad de los datasets sintéticos.

Ejecutar desde la raíz del curso:
    python recursos/datasets/verificar_datasets.py

Comprueba coherencia referencial entre archivos, rangos válidos y ausencia de
marcas comerciales reales (decisión D12).
"""
import csv, json, pathlib, re, sys

D = pathlib.Path(__file__).resolve().parent
ok = True

def rows(p):
    with open(D / p, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def check(label, cond, extra=""):
    global ok
    print(f"  [{'OK  ' if cond else 'FALLA'}] {label} {extra}")
    ok &= bool(cond)

print("\nCOHERENCIA REFERENCIAL")
planes = {p["plan_id"] for p in json.loads((D / "telecomunicaciones/planes.json").read_text(encoding="utf-8"))}
cli = rows("telecomunicaciones/clientes.csv"); lineas = {c["numero_linea"] for c in cli}
check("telco: plan_id de clientes existe en planes.json", all(c["plan_id"] in planes for c in cli))
check("telco: consumo referencia líneas existentes",
      all(r["numero_linea"] in lineas for r in rows("telecomunicaciones/consumo_datos.csv")))
check("telco: tickets referencian líneas existentes",
      all(r["numero_linea"] in lineas for r in rows("telecomunicaciones/tickets_reclamos.csv")))
check("telco: números de línea únicos", len(lineas) == len(cli), f"({len(lineas)})")

ctas = rows("banca/cuentas.csv"); nums = {c["numero_cuenta"] for c in ctas}
movs = rows("banca/movimientos.csv"); mids = {m["movimiento_id"] for m in movs}
check("banca: movimientos referencian cuentas existentes", all(m["numero_cuenta"] in nums for m in movs))
check("banca: tarjetas referencian cuentas existentes",
      all(t["numero_cuenta"] in nums for t in rows("banca/tarjetas.csv")))
al = rows("banca/alertas_riesgo.csv")
check("banca: alertas referencian movimientos existentes", all(a["movimiento_id"] in mids for a in al))
check("banca: score de riesgo en rango 0-100", all(0 <= int(a["score_riesgo"]) <= 100 for a in al))
check("banca: tarjetas exponen solo 4 dígitos",
      all(len(t["ultimos_4_digitos"]) == 4 for t in rows("banca/tarjetas.csv")))

prod = rows("retail/catalogo_productos.csv"); skus = {p["sku"] for p in prod}
ped = rows("retail/pedidos.csv"); pids = {p["pedido_id"] for p in ped}
check("retail: pedidos referencian SKU existentes", all(p["sku"] in skus for p in ped))
check("retail: stock referencia SKU existentes", all(s["sku"] in skus for s in rows("retail/stock_tiendas.csv")))
dev = rows("retail/devoluciones.csv")
check("retail: devoluciones referencian pedidos existentes", all(d["pedido_id"] in pids for d in dev))
check("retail: devoluciones referencian SKU existentes", all(d["sku"] in skus for d in dev))
check("retail: total = precio × cantidad",
      all(abs(float(p["total_soles"])
              - float(next(x for x in prod if x["sku"] == p["sku"])["precio_soles"]) * int(p["cantidad"])) < 0.02
          for p in ped))

veh = rows("seguros/vehiculos.csv"); placas = {v["placa"] for v in veh}
pol = rows("seguros/polizas.csv"); polids = {p["poliza_id"] for p in pol}
check("seguros: pólizas referencian placas existentes", all(p["placa"] in placas for p in pol))
check("seguros: siniestros referencian pólizas existentes",
      all(s["poliza_id"] in polids for s in rows("seguros/siniestros.csv")))
check("seguros: placas únicas", len(placas) == len(veh), f"({len(placas)})")
check("seguros: vigencia coherente (fin > inicio)",
      all(p["fin_vigencia"] > p["inicio_vigencia"] for p in pol))

print("\nCORPUS RAG")
for t in ["telecomunicaciones", "banca", "retail", "seguros"]:
    mds = sorted((D / t).glob("*.md"))
    total = sum(len(m.read_text(encoding="utf-8").split()) for m in mds)
    print(f"  {t:<20} {len(mds)} docs · {total:>5} palabras · ~{round(total/300)} chunks estimados")

print("\nPOLÍTICA DE MARCAS (decisión D12)")
# Marcas comerciales reales que NO deben aparecer. Se excluyen deliberadamente:
#  - reguladores y organismos públicos (OSIPTEL, Indecopi, SBS): son contexto normativo, no marcas
#  - marcas de vehículos en seguros: atributo factual del bien asegurado
PROHIBIDAS = ["Movistar","Claro","Entel","Bitel","BCP","Interbank","BBVA","Scotiabank","Rimac",
              "Pacífico","Falabella","Ripley","Yape","Plin","Olva","Shalom","Scharff","Wong",
              "Primax","InkaFarma","Rappi","Netflix","Uber","Plaza Vea","Cineplanet","Starbucks",
              "Sodimac","Oechsle","Metro","Jockey Plaza","Mega Plaza","Real Plaza","Mall del Sur"]
# Coincidencia por palabra completa: "Metro" no debe disparar con "Lima Metropolitana"
PATRON = re.compile(r"\b(" + "|".join(re.escape(m) for m in PROHIBIDAS) + r")\b", re.IGNORECASE)
hallazgos = []
for f in sorted(D.rglob("*")):
    if f.is_file() and f.suffix in {".csv", ".json", ".md"}:
        txt = f.read_text(encoding="utf-8", errors="ignore")
        hallazgos += [f"{f.relative_to(D)} → {m}" for m in set(PATRON.findall(txt))]
check("sin marcas comerciales reales", not hallazgos, "\n         " + "\n         ".join(hallazgos[:6]) if hallazgos else "")

print("\n" + ("TODAS LAS VERIFICACIONES PASARON" if ok else "HAY FALLAS — revisar arriba"))
sys.exit(0 if ok else 1)
