"""Verificador del simulador de industria.

Ejecutar desde la carpeta simulador-industria/:
    PYTHONPATH=. python verificar_simulador.py

33 comprobaciones contra los datasets reales: rutas de las 4 industrias,
autenticacion, aislamiento por equipo, no exposicion de PII y simulacion de fallos.
No requiere red ni credenciales de ningun servicio externo.
"""
import csv, sys
from fastapi.testclient import TestClient
import app as A

C = TestClient(A.app)
K = {"X-API-Key": "demo-key-0000"}
K2 = {"X-API-Key": "eq03-banca-g7h8i9"}
ok = True

def chk(label, cond, extra=""):
    global ok
    print(f"  [{'OK  ' if cond else 'FALLA'}] {label}{(' — ' + str(extra)[:70]) if extra else ''}")
    ok &= bool(cond)

def fila(track, arch):
    with open(f"../recursos/datasets/{track}/{arch}", encoding="utf-8") as f:
        return next(csv.DictReader(f))

with C:  # dispara el lifespan (construye la BD)
    print("\nMETA")
    r = C.get("/health"); chk("GET /health sin API key", r.status_code == 200, r.json())
    r = C.get("/"); chk("GET / info del servicio", r.status_code == 200)
    r = C.get("/fallos"); chk("GET /fallos catálogo", r.status_code == 200, len(r.json()["fallos"]))

    print("\nAUTENTICACIÓN")
    ln = fila("telecomunicaciones", "clientes.csv")["numero_linea"]
    r = C.get(f"/telco/clientes/{ln}"); chk("sin API key devuelve 401", r.status_code == 401)
    r = C.get(f"/telco/clientes/{ln}", headers={"X-API-Key": "clave-mala"})
    chk("API key inválida devuelve 401", r.status_code == 401)

    print("\nTELCO")
    r = C.get(f"/telco/clientes/{ln}", headers=K)
    chk("GET cliente existente", r.status_code == 200 and r.json()["plan"] is not None, r.json()["plan_nombre"])
    r = C.get("/telco/clientes/999999999", headers=K); chk("GET cliente inexistente → 404", r.status_code == 404)
    r = C.get(f"/telco/consumo/{ln}?periodo=2026-08", headers=K); chk("GET consumo", r.status_code == 200)
    r = C.get(f"/telco/consumo/{ln}?periodo=1999-01", headers=K); chk("GET consumo periodo inválido → 404", r.status_code == 404)
    r = C.get("/telco/cobertura/Miraflores", headers=K); chk("GET cobertura", r.status_code == 200)
    r = C.post("/telco/reclamos", headers=K, json={"numero_linea": ln, "tipo": "AVERIA", "descripcion": "Sin señal"})
    chk("POST reclamo → 201", r.status_code == 201, r.json())
    t1 = r.json()["ticket_id"]
    r = C.post("/telco/reclamos", headers=K, json={"numero_linea": ln, "tipo": "INVENTADO", "descripcion": "x"})
    chk("POST reclamo tipo inválido → 422", r.status_code == 422)

    print("\nAISLAMIENTO POR EQUIPO")
    r = C.post("/telco/reclamos", headers=K2, json={"numero_linea": ln, "tipo": "AVERIA", "descripcion": "otro equipo"})
    t2 = r.json()["ticket_id"]
    chk("otro equipo obtiene su propio correlativo", r.status_code == 201 and t2 == t1, f"{t1} vs {t2}")

    print("\nBANCA")
    cta = fila("banca", "cuentas.csv")["numero_cuenta"]
    r = C.get(f"/banca/cuentas/{cta}", headers=K)
    chk("GET cuenta", r.status_code == 200)
    chk("la cuenta NO expone el DNI", "dni" not in r.json(), list(r.json())[:6])
    r = C.get(f"/banca/movimientos/{cta}?dias=90", headers=K)
    chk("GET movimientos", r.status_code == 200, f"{r.json()['total']} movimientos")
    r = C.get(f"/banca/tarjetas/{cta}", headers=K); chk("GET tarjetas", r.status_code == 200)
    mov = fila("banca", "movimientos.csv")["movimiento_id"]
    r = C.get(f"/banca/riesgo/{mov}", headers=K)
    chk("GET riesgo", r.status_code == 200, f"nivel {r.json()['nivel']}")

    print("\nRETAIL")
    sku = fila("retail", "catalogo_productos.csv")["sku"]
    r = C.get(f"/retail/productos/{sku}", headers=K); chk("GET producto", r.status_code == 200)
    r = C.get(f"/retail/stock/{sku}", headers=K); chk("GET stock", r.status_code == 200, f"{r.json()['total']} u.")
    with open("../recursos/datasets/retail/pedidos.csv", encoding="utf-8") as f:
        entregado = next(p for p in csv.DictReader(f) if p["estado"] == "ENTREGADO")
        no_entregado = next((p for p in csv.DictReader(open("../recursos/datasets/retail/pedidos.csv", encoding="utf-8")) if p["estado"] == "EN_RUTA"), None)
    r = C.get(f"/retail/pedidos/{entregado['pedido_id']}", headers=K); chk("GET pedido", r.status_code == 200)
    r = C.post("/retail/devoluciones", headers=K, json={"pedido_id": entregado["pedido_id"], "motivo": "Llegó dañado"})
    chk("POST devolución sobre ENTREGADO → 201", r.status_code == 201, r.json())
    if no_entregado:
        r = C.post("/retail/devoluciones", headers=K, json={"pedido_id": no_entregado["pedido_id"], "motivo": "x"})
        chk("POST devolución sobre EN_RUTA → 409", r.status_code == 409, r.json()["detail"][:60])

    print("\nSEGUROS")
    placa = fila("seguros", "polizas.csv")["placa"]
    r = C.get(f"/seguros/polizas/{placa}", headers=K)
    chk("GET póliza", r.status_code == 200, f"vence en {r.json()['dias_para_vencer']} días")
    chk("la póliza NO expone el DNI", "dni" not in r.json())
    r = C.get(f"/seguros/vehiculos/{placa}", headers=K); chk("GET vehículo", r.status_code == 200)
    r = C.get("/seguros/clinicas?distrito=Ate", headers=K); chk("GET clínicas por distrito", r.status_code == 200)
    r = C.post("/seguros/siniestros", headers=K, json={"placa": placa, "tipo": "CHOQUE_SIMPLE", "distrito": "Ate", "cantidad_lesionados": 2})
    chk("POST siniestro → 201", r.status_code == 201, r.json())
    chk("marca prioridad alta con lesionados", r.json().get("prioridad_alta") is True)
    sid = r.json()["siniestro_id"]
    r = C.get(f"/seguros/siniestros/{sid}", headers=K); chk("GET siniestro recién creado", r.status_code == 200)
    r = C.get(f"/seguros/siniestros/{sid}", headers=K2); chk("otro equipo NO ve ese siniestro → 404", r.status_code == 404)

    print("\nSIMULACIÓN DE FALLOS")
    r = C.get(f"/telco/clientes/{ln}?_fallo=error500", headers=K); chk("_fallo=error500", r.status_code == 500)
    r = C.get(f"/telco/clientes/{ln}?_fallo=error503", headers=K); chk("_fallo=error503", r.status_code == 503)
    r = C.get(f"/telco/clientes/{ln}?_fallo=vacio", headers=K); chk("_fallo=vacio → 200 con cuerpo vacío", r.status_code == 200 and r.json() == {})
    r = C.get(f"/telco/clientes/{ln}?_fallo=malformado", headers=K); chk("_fallo=malformado", r.status_code == 200 and "datos" in r.json())
    r = C.get(f"/telco/clientes/{ln}?_fallo=inexistente", headers=K); chk("_fallo desconocido → 400", r.status_code == 400)

print("\n" + ("TODAS LAS VERIFICACIONES PASARON" if ok else "HAY FALLAS"))
sys.exit(0 if ok else 1)
