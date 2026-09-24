# -*- coding: utf-8 -*-
"""Validación integral de los esqueletos de sesión.

Ejecutar desde la raíz del curso:

    python docente/validar_coherencia.py
    python docente/validar_coherencia.py --verbose

QUÉ VALIDA
----------
Que las 11 sesiones + el seminario + el bonus formen **un curso**, y no doce diseños
independientes que coinciden en la carpeta. Comprueba lo que se puede comprobar de
forma mecánica:

  C1  estructura       cada esqueleto tiene sus secciones obligatorias
  C2  horas            el reparto declarado por sesión cuadra con la malla (29 T / 43 P / 72)
  C3  guion            los bloques del guion en vivo suman los minutos declarados
  C4  coherencia T/P   el reparto del guion coincide con el de la ficha
  C5  referencias      "no entra aquí, va en S<N>" siempre apunta hacia adelante
  C6  laboratorios     cada L1..L12 pertenece a exactamente una sesión
  C7  incrementalidad  cada sesión se apoya explícitamente en la anterior
  C9  herramientas     toda tool nombrada existe en el catálogo real
  C10 bloqueantes      todo bloqueante declara un vencimiento

Lo que NO puede validar un script —si un concepto se enseña antes de usarse, si la
carga semanal es humana, si la narrativa se sostiene— está en
`docente/esqueletos/VALIDACION-INTEGRAL.md`, como guía de preparación docente.

No requiere red ni credenciales.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
from collections import Counter, defaultdict

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ESQ = RAIZ / "docente" / "esqueletos"

# Malla oficial: sesión -> (teoría, práctica). Fuente: PLAN-CURRICULAR.md §4
MALLA = {
    1: (3.5, 2.5), 2: (3.0, 3.0), 3: (2.5, 3.5), 4: (2.5, 3.5),
    5: (3.0, 3.0), 6: (2.5, 3.5), 7: (1.5, 4.5), 8: (2.5, 3.5),
    9: (2.5, 3.5), 10: (2.5, 3.5), 11: (1.5, 4.5),
    "seminario": (1.5, 4.5),
}
TOTAL_TEORIA, TOTAL_PRACTICA, TOTAL_HORAS = 29.0, 43.0, 72.0

SECCIONES = ["Ficha", "Objetivos", "no** entra", "evaluaci"]

TOOLS = {
    "get_customer_plan", "get_data_usage", "run_line_diagnostics", "create_complaint_ticket",
    "check_portability_eligibility", "get_coverage_by_district",
    "get_account_balance", "list_transactions", "get_card_info", "score_transaction_risk",
    "get_transfer_limits", "request_card_block",
    "track_order", "get_product_details", "check_stock_by_store", "start_return_request",
    "estimate_delivery", "get_return_status",
    "get_policy_by_plate", "quote_soat", "get_claim_status", "open_claim",
    "list_affiliated_clinics", "get_vehicle_info",
}

ok = True
avisos = 0


def chk(codigo, label, cond, extra=""):
    global ok
    print(f"  [{'OK  ' if cond else 'FALLA'}] {codigo} · {label}{(' — ' + str(extra)[:78]) if extra else ''}")
    ok &= bool(cond)


def aviso(codigo, label, extra=""):
    global avisos
    avisos += 1
    print(f"  [AVISO] {codigo} · {label}{(' — ' + str(extra)[:78]) if extra else ''}")


def cargar():
    docs = {}
    for n in range(1, 12):
        ruta = ESQ / f"sesion-{n:02d}.md"
        docs[n] = ruta.read_text(encoding="utf-8") if ruta.exists() else None
    for nombre in ("seminario", "bonus-foundry"):
        ruta = ESQ / f"{nombre}.md"
        docs[nombre] = ruta.read_text(encoding="utf-8") if ruta.exists() else None
    return docs


def etiqueta(k):
    return f"S{k}" if isinstance(k, int) else k


# ─────────────────────────────────────────────────────────────────────────────
def c1_estructura(docs):
    print("\nC1 · ESTRUCTURA")
    for k, txt in docs.items():
        if txt is None:
            chk("C1", f"{etiqueta(k)} existe", False, "archivo ausente")
            continue
        faltan = [s for s in SECCIONES if s not in txt]
        chk("C1", f"{etiqueta(k)} tiene sus secciones", not faltan, f"faltan: {faltan}" if faltan else "")


def _horas_declaradas(txt):
    m = re.search(r"\*\*([\d.]+)\s*h teoría\s*·\s*([\d.]+)\s*h práctica", txt)
    return (float(m.group(1)), float(m.group(2))) if m else None


def c2_horas(docs):
    print("\nC2 · HORAS CONTRA LA MALLA")
    suma_t = suma_p = 0.0
    for k, esperado in MALLA.items():
        txt = docs.get(k)
        if not txt:
            chk("C2", f"{etiqueta(k)} declara horas", False, "sin esqueleto")
            continue
        decl = _horas_declaradas(txt)
        if decl is None:
            chk("C2", f"{etiqueta(k)} declara horas", False, "no se encontró el patrón en la ficha")
            continue
        chk("C2", f"{etiqueta(k)} {decl[0]}T/{decl[1]}P", decl == esperado,
            "" if decl == esperado else f"la malla dice {esperado[0]}T/{esperado[1]}P")
        suma_t += decl[0]
        suma_p += decl[1]
    chk("C2", f"total teoría = {TOTAL_TEORIA}", abs(suma_t - TOTAL_TEORIA) < 0.01, f"{suma_t}")
    chk("C2", f"total práctica = {TOTAL_PRACTICA}", abs(suma_p - TOTAL_PRACTICA) < 0.01, f"{suma_p}")
    chk("C2", f"total = {TOTAL_HORAS} h", abs(suma_t + suma_p - TOTAL_HORAS) < 0.01, f"{suma_t + suma_p}")
    pct = 100 * suma_t / (suma_t + suma_p) if (suma_t + suma_p) else 0
    chk("C2", "balance 40/60 (±1 pto)", abs(pct - 40) <= 1.0, f"{pct:.1f} % teoría")


def _bloques_guion(txt):
    """Devuelve [(min, tipo)] de las filas del guion: | n | texto | 25 | T | ... |"""
    filas = []
    for linea in txt.splitlines():
        m = re.match(r"\|\s*[\d—-]+\s*\|[^|]+\|\s*(\d+)\s*\|\s*([^|]*)\|", linea)
        if m:
            # "T + demo" y "T/P" cuentan como su primera letra; la pausa no cuenta
            tipo = next((c for c in m.group(2) if c in "TP"), "")
            filas.append((int(m.group(1)), tipo))
    return filas


def c3_guion(docs):
    print("\nC3 · EL GUION SUMA 180 MIN")
    for k in list(range(1, 12)) + ["seminario"]:
        txt = docs.get(k)
        if not txt:
            continue
        filas = _bloques_guion(txt)
        if not filas:
            aviso("C3", f"{etiqueta(k)} sin tabla de guion reconocible")
            continue
        total = sum(m for m, _ in filas)
        if total != 180 and "Preparación del horario" in txt:
            aviso("C3", f"{etiqueta(k)} guion = {total} min",
                  "confirmar y comunicar la franja adicional antes de clase")
            continue
        chk("C3", f"{etiqueta(k)} guion = {total} min", total == 180,
            "" if total == 180 else f"{len(filas)} bloques suman {total}, no 180")


def c4_reparto(docs):
    print("\nC4 · EL GUION CUADRA CON LA FICHA")
    for k in list(range(1, 12)) + ["seminario"]:
        txt = docs.get(k)
        if not txt:
            continue
        decl = _horas_declaradas(txt)
        filas = _bloques_guion(txt)
        if not decl or not filas:
            continue
        t_guion = sum(m for m, tipo in filas if tipo == "T")
        p_guion = sum(m for m, tipo in filas if tipo == "P")
        # teoría total = 60 min de pre-work + teoría del guion
        t_total = (60 + t_guion) / 60
        p_total = (p_guion + 120) / 60
        cuadra_t = abs(t_total - decl[0]) <= 0.34   # tolerancia: la pausa redondea
        cuadra_p = abs(p_total - decl[1]) <= 0.34
        chk("C4", f"{etiqueta(k)} T {t_total:.2f}h vs ficha {decl[0]}h", cuadra_t,
            "" if cuadra_t else f"guion aporta {t_guion} min de teoría")
        chk("C4", f"{etiqueta(k)} P {p_total:.2f}h vs ficha {decl[1]}h", cuadra_p,
            "" if cuadra_p else f"guion aporta {p_guion} min de práctica")


def c5_referencias(docs):
    print("\nC5 · LAS REFERENCIAS APUNTAN HACIA ADELANTE")
    for n in range(1, 12):
        txt = docs.get(n)
        if not txt:
            continue
        bloque = txt.split("no** entra")
        if len(bloque) < 2:
            continue
        cuerpo = bloque[1].split("\n## ")[0]
        # Solo la SEGUNDA columna de la tabla es el destino. Una mención a S<n> en la
        # prosa de la sección no es un reenvío: es una referencia.
        destinos = set()
        for fila in re.findall(r"^\|([^|\n]+)\|([^|\n]+)\|\s*$", cuerpo, re.M):
            destinos |= {int(d) for d in re.findall(r"\bS(\d{1,2})\b", fila[1])}
        hacia_atras = sorted(d for d in destinos if d <= n)
        chk("C5", f"S{n} no pospone hacia atrás", not hacia_atras,
            "" if not hacia_atras else f"apunta a {hacia_atras}, que ya ocurrió")


def c6_laboratorios(docs):
    print("\nC6 · CADA LABORATORIO EN UNA SOLA SESIÓN")
    dueno = defaultdict(list)
    for k, txt in docs.items():
        if not txt:
            continue
        m = re.search(r"\|\s*Laboratorio\s*\|([^|]+)\|", txt)
        if not m:
            continue
        for lab in re.findall(r"\bL(\d{1,2})\b", m.group(1)):
            dueno[int(lab)].append(etiqueta(k))
    for lab in range(1, 13):
        duenos = dueno.get(lab, [])
        chk("C6", f"L{lab} tiene un solo dueño", len(duenos) == 1,
            f"{duenos}" if len(duenos) != 1 else duenos[0])


def c7_incrementalidad(docs):
    print("\nC7 · CADA SESIÓN SE APOYA EN LA ANTERIOR")
    for n in range(2, 12):
        txt = docs.get(n)
        if not txt:
            continue
        referencias = [f"S{n-1}", f"L{n-1}"]
        apoya = any(r in txt for r in referencias)
        chk("C7", f"S{n} menciona S{n-1} o L{n-1}", apoya,
            "" if apoya else "no hay rastro de la sesión previa: revisar la continuidad")


def c9_tools(docs):
    print("\nC9 · LAS HERRAMIENTAS NOMBRADAS EXISTEN")
    NO_SON_TOOLS = {"check_stack", "get_system_prompt", "get_chat_model", "get_embeddings",
                    "start_return_request_test", "list_legacy"}
    patron = re.compile(r"`((?:get|create|run|list|check|track|start|score|quote|open|request|estimate)_[a-z_]+)`")
    for k, txt in docs.items():
        if not txt:
            continue
        nombradas = set(patron.findall(txt))
        invalidas = sorted(n for n in nombradas if n not in TOOLS and n not in NO_SON_TOOLS)
        chk("C9", f"{etiqueta(k)} ({len(nombradas)} tools)", not invalidas, f"no existen: {invalidas}")


def c10_bloqueantes(docs):
    print("\nC10 · LOS BLOQUEANTES TIENEN VENCIMIENTO")
    for k, txt in docs.items():
        if not txt or "loqueante" not in txt:
            continue
        cuerpo = txt.split("loqueante", 1)[1].split("\n## ")[0]
        tiene_fecha = bool(re.search(r"[Ss]emana \d|[Ll]unes|[Mm]artes|[Mm]iércoles|[Jj]ueves|"
                                     r"\d{4}-\d{2}-\d{2}|semanas antes|h antes", cuerpo))
        chk("C10", f"{etiqueta(k)} fecha su bloqueante", tiene_fecha,
            "" if tiene_fecha else "declara un bloqueante sin decir para cuándo")


def main():
    p = argparse.ArgumentParser(description="Validación integral de los esqueletos")
    p.add_argument("--verbose", action="store_true")
    a = p.parse_args()

    print("\n" + "=" * 80)
    print("  VALIDACIÓN INTEGRAL DE LOS ESQUELETOS DE SESIÓN")
    print("=" * 80)
    if not ESQ.exists():
        print(f"  ERROR: no existe {ESQ}")
        return 2

    docs = cargar()
    presentes = sum(1 for v in docs.values() if v)
    print(f"  {presentes} de {len(docs)} esqueletos encontrados en {ESQ.relative_to(RAIZ)}")

    for f in (c1_estructura, c2_horas, c3_guion, c4_reparto, c5_referencias,
              c6_laboratorios, c7_incrementalidad, c9_tools, c10_bloqueantes):
        f(docs)

    print("\n" + "=" * 80)
    if ok:
        print(f"  COHERENCIA VERIFICADA{f' · {avisos} aviso(s)' if avisos else ''}")
        print("  Recuerda: esto valida lo mecánico. Lo pedagógico está en")
        print("  docente/esqueletos/VALIDACION-INTEGRAL.md y se revisa a mano.\n")
        return 0
    print(f"  HAY INCOHERENCIAS{f' · {avisos} aviso(s)' if avisos else ''}")
    print("  Corrige los FALLA de arriba antes de dictar esas sesiones.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
