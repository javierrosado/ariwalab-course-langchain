# -*- coding: utf-8 -*-
"""Generador de los datasets sintéticos del curso.

Ejecutar desde la raíz del curso:
    python recursos/datasets/generar_datasets.py

Semilla fija: regenerar produce exactamente los mismos datos.

REGLA DE MARCAS: todas las empresas, comercios, couriers, tiendas,
billeteras y clínicas son FICTICIAS. La única excepción son las marcas de vehículos
en el track de seguros, porque la marca de un auto es un atributo factual del bien
asegurado (como el año o el color), no un proveedor de servicio suplantado.
"""
import csv, json, random, pathlib
from datetime import date, timedelta

random.seed(20260905)
ROOT = pathlib.Path(__file__).resolve().parent

NOMBRES = ["Ana","Carlos","María","José","Rosa","Luis","Carmen","Jorge","Patricia","Miguel","Elena",
           "Ricardo","Sofía","Fernando","Lucía","Andrés","Gabriela","Diego","Valeria","Raúl","Milagros",
           "César","Karina","Álvaro","Pilar","Renzo","Claudia","Mauricio","Silvia","Iván"]
APELLIDOS = ["Quispe","Ramírez","Flores","Huamán","Vargas","Rojas","Mendoza","Castillo","Torres","Chávez",
             "Salazar","Paredes","Cárdenas","Espinoza","Villanueva","Ríos","Alarcón","Bustamante","Ccahuana",
             "Ninahuanca","Delgado","Zegarra","Loayza","Ampuero","Yupanqui"]
DISTRITOS = ["Miraflores","San Isidro","Santiago de Surco","La Molina","San Borja","Jesús María","Lince",
             "Magdalena del Mar","Pueblo Libre","San Miguel","Comas","San Juan de Lurigancho",
             "Villa El Salvador","Ate","Callao","Chorrillos","Barranco","Surquillo","Los Olivos","Independencia"]

def persona(): return f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)} {random.choice(APELLIDOS)}"
def dni(): return f"{random.randint(10000000, 79999999)}"
def fecha(d1=-720, d2=-10): return (date(2026, 9, 5) + timedelta(days=random.randint(d1, d2))).isoformat()

def escribir_csv(track, nombre, cabecera, filas):
    carpeta = ROOT / track; carpeta.mkdir(parents=True, exist_ok=True)
    with open(carpeta / nombre, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(cabecera); w.writerows(filas)
    print(f"  {track}/{nombre:<28} {len(filas):>4} filas")

def escribir_json(track, nombre, data):
    carpeta = ROOT / track; carpeta.mkdir(parents=True, exist_ok=True)
    (carpeta / nombre).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  {track}/{nombre:<28} {len(data):>4} registros")

# ═════════════════ TELECOMUNICACIONES · AndesMóvil ═════════════════
print("\nTELECOMUNICACIONES (AndesMóvil)")
PLANES = [
    {"plan_id":"AM-CTRL-39","nombre":"Control 39","precio_soles":39.0,"gb_datos":8,"minutos":"Ilimitados","sms":100,"roaming_latam":False,"permanencia_meses":12,"redes_sociales_libres":["WhatsApp"]},
    {"plan_id":"AM-MAX-59","nombre":"Max 59","precio_soles":59.0,"gb_datos":18,"minutos":"Ilimitados","sms":"Ilimitados","roaming_latam":False,"permanencia_meses":12,"redes_sociales_libres":["WhatsApp","Facebook"]},
    {"plan_id":"AM-MAX-89","nombre":"Max 89","precio_soles":89.0,"gb_datos":30,"minutos":"Ilimitados","sms":"Ilimitados","roaming_latam":True,"permanencia_meses":18,"redes_sociales_libres":["WhatsApp","Facebook","Instagram","TikTok"]},
    {"plan_id":"AM-PRO-129","nombre":"Pro 129","precio_soles":129.0,"gb_datos":60,"minutos":"Ilimitados","sms":"Ilimitados","roaming_latam":True,"permanencia_meses":18,"redes_sociales_libres":["WhatsApp","Facebook","Instagram","TikTok","YouTube"]},
    {"plan_id":"AM-ILIM-179","nombre":"Ilimitado 179","precio_soles":179.0,"gb_datos":"Ilimitado","minutos":"Ilimitados","sms":"Ilimitados","roaming_latam":True,"permanencia_meses":24,"redes_sociales_libres":["Todas"]},
]
escribir_json("telecomunicaciones", "planes.json", PLANES)

lineas = list(dict.fromkeys(f"9{random.randint(10000000, 89999999)}" for _ in range(60)))[:50]
clientes = []
for ln in lineas:
    p = random.choice(PLANES)
    clientes.append([ln, persona(), dni(), p["plan_id"], p["nombre"],
                     random.choices(["ACTIVO","SUSPENDIDO","BAJA"], weights=[85,10,5])[0],
                     fecha(-1400, -40), random.choice(DISTRITOS)])
escribir_csv("telecomunicaciones","clientes.csv",
             ["numero_linea","nombre_titular","dni","plan_id","plan_nombre","estado","fecha_alta","distrito"], clientes)

consumo = []
for c in clientes:
    plan = next(p for p in PLANES if p["plan_id"] == c[3])
    incl = plan["gb_datos"] if isinstance(plan["gb_datos"], int) else 100
    for periodo in ["2026-07","2026-08"]:
        consumo.append([c[0], periodo, round(random.uniform(0.5, incl * 1.25), 2), incl,
                        random.randint(40, 900), random.randint(0, 60)])
escribir_csv("telecomunicaciones","consumo_datos.csv",
             ["numero_linea","periodo","gb_consumidos","gb_incluidos","minutos_consumidos","sms_enviados"], consumo)

escribir_csv("telecomunicaciones","cobertura_distritos.csv",
             ["distrito","tecnologia","calidad_senal","incidencia_activa","detalle_incidencia"],
             [[d, random.choice(["4G","4G/5G","5G"]),
               random.choices(["EXCELENTE","BUENA","REGULAR"], weights=[45,40,15])[0],
               random.choices(["NO","SI"], weights=[88,12])[0],
               random.choice(["-","Mantenimiento programado","Avería en nodo","Saturación en hora punta"])]
              for d in DISTRITOS])

TIPOS_REC = ["FACTURACION","CALIDAD_SERVICIO","AVERIA","PORTABILIDAD","CONTRATACION","SUSPENSION"]
escribir_csv("telecomunicaciones","tickets_reclamos.csv",
             ["ticket_id","numero_linea","tipo","fecha_registro","estado","codigo_osiptel"],
             [[f"REC-2026-{i:05d}", random.choice(clientes)[0], random.choice(TIPOS_REC), fecha(-180,-1),
               random.choices(["ABIERTO","EN_PROCESO","RESUELTO","ESCALADO_REGULADOR"],weights=[20,30,42,8])[0],
               f"OSI-{random.randint(100000,999999)}"] for i in range(1, 41)])

# ═════════════════════ BANCA · Banco Inti ═════════════════════
print("\nBANCA (Banco Inti)")
cuentas = [[f"191-{random.randint(1000000,9999999)}-0-{random.randint(10,99)}", persona(), dni(),
            random.choices(["AHORROS","CORRIENTE","SUELDO"],weights=[55,15,30])[0],
            random.choices(["PEN","USD"],weights=[85,15])[0],
            round(random.uniform(120, 48000), 2),
            random.choices(["ACTIVA","BLOQUEADA"],weights=[93,7])[0], fecha(-2000,-100)] for _ in range(40)]
escribir_csv("banca","cuentas.csv",
             ["numero_cuenta","titular","dni","tipo_cuenta","moneda","saldo","estado","fecha_apertura"], cuentas)

# Comercios ficticios
COMERCIOS = ["Supermercado Kori","Grifo Wayra","Farmacia Pacha","Delivery Ñam","StreamAndina",
             "TaxiYa","Minimarket Tumi","Mercado Inti","Cine Estelar","Café Andino",
             "Ferretería Nexo","Tienda Aurora","Transferencia P2P","Cajero Banco Inti","Botica Sumaq"]
CANALES = ["APP","WEB","POS","ATM","INTIPAY","TRANSFERENCIA_INMEDIATA","TRANSFERENCIA_DIFERIDA"]
movs, mid = [], 1
for c in cuentas:
    for _ in range(random.randint(6, 14)):
        es_cargo = random.random() < 0.75
        movs.append([f"MOV-{mid:07d}", c[0], fecha(-90,-1), random.choice(COMERCIOS),
                     round(random.uniform(8, 1400), 2) * (-1 if es_cargo else 1),
                     "CARGO" if es_cargo else "ABONO", random.choice(CANALES),
                     random.choice(DISTRITOS) if random.random() < 0.7 else "EN_LINEA"])
        mid += 1
escribir_csv("banca","movimientos.csv",
             ["movimiento_id","numero_cuenta","fecha","descripcion","monto","tipo","canal","ubicacion"], movs)

escribir_csv("banca","tarjetas.csv",
             ["tarjeta_id","numero_cuenta","ultimos_4_digitos","marca","estado","linea_credito","dia_facturacion"],
             [[f"TC-{i:05d}", c[0], f"{random.randint(1000,9999)}", random.choice(["CLASICA","ORO","PLATINUM"]),
               random.choices(["ACTIVA","BLOQUEADA","POR_ACTIVAR"],weights=[85,10,5])[0],
               random.choice([2000,3500,5000,8000,12000,20000]), random.choice([5,10,15,20,25,28])]
              for i, c in enumerate(cuentas[:30], start=1)])

MOTIVOS = ["Monto atípico para el perfil","Operación en ubicación inusual","Múltiples intentos en 5 minutos",
           "Comercio de alto riesgo","Horario atípico (02:00-05:00)","Cambio de dispositivo reciente"]
escribir_csv("banca","alertas_riesgo.csv",
             ["alerta_id","numero_cuenta","movimiento_id","score_riesgo","motivo","estado","fecha"],
             [[f"ALR-{i:05d}", (m := random.choice(movs))[1], m[0], random.randint(55, 98),
               random.choice(MOTIVOS),
               random.choices(["PENDIENTE","CONFIRMADA_FRAUDE","DESCARTADA"],weights=[25,20,55])[0],
               fecha(-60,-1)] for i in range(1, 26)])

# ═════════════════════ RETAIL · MercaSur ═════════════════════
print("\nRETAIL (MercaSur)")
CATS = {"Tecnología":["Laptop","Smartphone","Audífonos","Tablet","Monitor","Teclado"],
        "Hogar":["Licuadora","Aspiradora","Juego de sábanas","Olla arrocera","Ventilador"],
        "Moda":["Zapatillas","Casaca","Polo","Jeans","Mochila"],
        "Electrohogar":["Refrigeradora","Lavadora","Microondas","Televisor","Horno"]}
MARCAS = ["Nexo","Aurora","Kori","Tumi","Wayra","Inti","Pacha"]
productos, sku_n = [], 1000
for cat, items in CATS.items():
    for it in items:
        for _ in range(2):
            sku_n += 1
            productos.append([f"MS-{sku_n}",
                              f"{it} {random.choice(MARCAS)} {random.choice(['Pro','Lite','Max','Plus','Basic'])}",
                              cat, random.choice(MARCAS), round(random.uniform(39, 4200), 2),
                              random.choice([6,12,24,36]),
                              "NO" if cat == "Moda" and random.random() < 0.2 else "SI"])
escribir_csv("retail","catalogo_productos.csv",
             ["sku","nombre","categoria","marca","precio_soles","garantia_meses","permite_cambio"], productos)

TIENDAS = ["MercaSur Surco","MercaSur Norte","MercaSur San Miguel",
           "MercaSur Salaverry","MercaSur Sur","Almacén Central MercaSur"]
escribir_csv("retail","stock_tiendas.csv", ["sku","tienda","stock_disponible"],
             [[p[0], t, random.randint(0, 45)] for p in productos for t in TIENDAS])

COURIERS = ["Andes Courier","Rapidex","Volare Logística","Despacho propio MercaSur"]
ESTADOS_PED = ["EN_PREPARACION","EN_RUTA","ENTREGADO","LISTO_PARA_RECOJO","DEVUELTO","CANCELADO"]
pedidos = []
for i in range(1, 51):
    p = random.choice(productos); cant = random.randint(1,3)
    pedidos.append([f"MS-2026-{i:05d}", persona(), fecha(-60,-1),
                    random.choices(ESTADOS_PED,weights=[15,20,45,10,7,3])[0],
                    p[0], cant, round(float(p[4]) * cant, 2), random.choice(COURIERS),
                    f"TRK{random.randint(10000000,99999999)}", random.choice(TIENDAS),
                    random.choice(DISTRITOS)])
escribir_csv("retail","pedidos.csv",
             ["pedido_id","cliente","fecha_compra","estado","sku","cantidad","total_soles","courier",
              "codigo_tracking","tienda_despacho","distrito_entrega"], pedidos)

MOTIVOS_DEV = ["Producto con falla","Talla incorrecta","No era lo esperado","Llegó dañado",
               "Producto equivocado","Arrepentimiento de compra"]
escribir_csv("retail","devoluciones.csv",
             ["devolucion_id","pedido_id","sku","motivo","estado","fecha_solicitud","tipo_solucion"],
             [[f"DEV-{i:05d}", random.choice(pedidos)[0], random.choice(productos)[0],
               random.choice(MOTIVOS_DEV),
               random.choices(["SOLICITADA","APROBADA","RECHAZADA","COMPLETADA"],weights=[25,30,15,30])[0],
               fecha(-45,-1), random.choice(["CAMBIO","REEMBOLSO","NOTA_CREDITO"])] for i in range(1, 31)])

# ═════════════════════ SEGUROS · Andina Seguros ═════════════════════
print("\nSEGUROS (Andina Seguros)")
L = "ABCDEFGHJKLMNPQRSTUVWXYZ"
placas = list(dict.fromkeys(
    f"{random.choice(L)}{random.choice(L)}{random.choice(L)}-{random.randint(100,999)}" for _ in range(60)))[:45]
# Excepción de la política de marcas: la marca del vehículo es un atributo factual del bien asegurado.
MARCAS_V = [("Toyota",["Yaris","Corolla","Hilux","RAV4"]),("Hyundai",["Accent","Tucson","Elantra"]),
            ("Kia",["Rio","Sportage","Picanto"]),("Nissan",["Versa","Sentra","Frontier"]),
            ("Suzuki",["Swift","Vitara"]),("Chevrolet",["Sail","Onix"])]
CATEGORIAS = [("M1","Automóvil particular hasta 9 asientos",5),("M2","Transporte público hasta 16 asientos",16),
              ("N1","Carga hasta 3.5 toneladas",3),("L5","Mototaxi",4)]
vehiculos = []
for pl in placas:
    marca, modelos = random.choice(MARCAS_V)
    cat, desc, asientos = random.choices(CATEGORIAS, weights=[70,10,15,5])[0]
    vehiculos.append([pl, marca, random.choice(modelos), random.randint(2011, 2026), cat, desc,
                      asientos, random.choices(["PARTICULAR","COMERCIAL","TAXI"],weights=[75,15,10])[0]])
escribir_csv("seguros","vehiculos.csv",
             ["placa","marca","modelo","anio","categoria","descripcion_categoria","asientos","uso"], vehiculos)

polizas = []
for i, v in enumerate(vehiculos, start=1):
    ini = date(2026, 9, 5) + timedelta(days=random.randint(-400, -5)); fin = ini + timedelta(days=365)
    prima = {"M1":92.0,"M2":420.0,"N1":150.0,"L5":210.0}[v[4]] * random.uniform(0.92, 1.18)
    polizas.append([f"SOAT-2026-{i:05d}", v[0], persona(), dni(), "SOAT", ini.isoformat(), fin.isoformat(),
                    round(prima, 2), "VIGENTE" if fin > date(2026,9,5) else "VENCIDA",
                    random.choice(["DIGITAL","FISICO"])])
escribir_csv("seguros","polizas.csv",
             ["poliza_id","placa","titular","dni","tipo_poliza","inicio_vigencia","fin_vigencia",
              "prima_soles","estado","modalidad"], polizas)

TIPOS_SIN = ["CHOQUE_SIMPLE","ATROPELLO","VOLCADURA","COLISION_MULTIPLE","DESPISTE"]
escribir_csv("seguros","siniestros.csv",
             ["siniestro_id","poliza_id","placa","fecha_ocurrencia","tipo","estado","distrito",
              "cantidad_lesionados","monto_estimado_soles"],
             [[f"SIN-2026-{i:05d}", (p := random.choice(polizas))[0], p[1], fecha(-300,-2),
               random.choice(TIPOS_SIN),
               random.choices(["REPORTADO","EN_EVALUACION","APROBADO","LIQUIDADO","OBSERVADO"],
                              weights=[18,27,20,27,8])[0],
               random.choice(DISTRITOS), random.randint(0, 3),
               round(random.uniform(500, 26000), 2)] for i in range(1, 36)])

CLINICAS = [("Clínica Andina Central","Jesús María","Av. Salaverry 1450","01-500-1200","SI"),
            ("Clínica San Marcelo","Miraflores","Av. Benavides 780","01-500-1201","SI"),
            ("Clínica Los Sauces","Santiago de Surco","Av. Caminos del Inca 2100","01-500-1202","SI"),
            ("Policlínico Inti Norte","Los Olivos","Av. Antúnez de Mayolo 990","01-500-1203","NO"),
            ("Clínica Los Andes Este","Ate","Carretera Central km 6.5","01-500-1204","SI"),
            ("Centro Médico Sumaq","Villa El Salvador","Av. Revolución 340","01-500-1205","NO"),
            ("Clínica del Callao Norte","Callao","Av. Sáenz Peña 620","01-500-1206","SI"),
            ("Clínica San Borja Salud","San Borja","Av. San Luis 2030","01-500-1207","SI")]
escribir_csv("seguros","red_clinicas.csv",
             ["clinica","distrito","direccion","telefono","atiende_24h"], [list(c) for c in CLINICAS])

print("\nDATASETS GENERADOS")
