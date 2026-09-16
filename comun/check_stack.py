"""Verificador del stack del curso.

Ejecuta comprobaciones contra los servicios SaaS reales y dice, con evidencia, si
el stack elegido soporta el curso. Las comprobaciones 3 y 4 son las críticas: de
ellas dependen las sesiones 3 a 11.

Uso, desde la raíz del curso:

    python -m comun.check_stack                  # las 8 comprobaciones
    python -m comun.check_stack --solo-modelo    # omite Qdrant y Langfuse
    python -m comun.check_stack --candidatos     # compara varios modelos
    python -m comun.check_stack --todos-los-tracks
"""

from __future__ import annotations

import argparse
import sys
import time
import traceback
from dataclasses import dataclass

from . import settings as cfg

VERDE, ROJO, AMARILLO, GRIS, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[90m", "\033[0m"

# Escalera de modelos, del que menos riesgo aporta por costo al de mayor techo.
# Todos son de pesos abiertos y tienen tool calling nativo en su chat_template.
CANDIDATOS_POR_DEFECTO = [
    "Qwen/Qwen3-32B",                     # verificado 2026-09-10: el único que pasó
    "Qwen/Qwen3-30B-A3B",                 # MoE, más barato de servir — falló en la prueba
    "Qwen/Qwen3-8B",                      # mínimo costo — falló en la prueba
    "meta-llama/Llama-3.3-70B-Instruct",  # mayor techo — falló en la prueba
]


@dataclass
class Resultado:
    nombre: str
    critico: bool
    ok: bool = False
    detalle: str = ""
    segundos: float = 0.0


RESULTADOS: list[Resultado] = []


def check(nombre: str, critico: bool = False):
    """Decorador: ejecuta la comprobación, mide el tiempo y captura el error."""
    def wrapper(fn):
        def run(*args, **kwargs):
            r = Resultado(nombre=nombre, critico=critico)
            t0 = time.perf_counter()
            try:
                r.detalle = fn(*args, **kwargs) or "OK"
                r.ok = True
            except Exception as exc:  # noqa: BLE001 — queremos ver cualquier fallo
                r.detalle = f"{type(exc).__name__}: {exc}"
                if "--debug" in sys.argv:
                    traceback.print_exc()
            r.segundos = time.perf_counter() - t0
            RESULTADOS.append(r)
            icono = f"{VERDE}PASA{RESET}" if r.ok else f"{ROJO}FALLA{RESET}"
            print(f"  [{icono}] {nombre}  ({r.segundos:.1f}s)")
            if not r.ok:
                print(f"         {GRIS}{r.detalle[:300]}{RESET}")
            return r
        return run
    return wrapper


# ---------------------------------------------------------------- 1
@check("1. Variables de entorno")
def check_env() -> str:
    faltan = []
    if cfg.AI_PROVIDER not in cfg.VALID_PROVIDERS:
        raise ValueError(f"AI_PROVIDER='{cfg.AI_PROVIDER}' inválido")
    if cfg.AI_PROVIDER == "huggingface" and not cfg.HF_TOKEN:
        faltan.append("HF_TOKEN")
    if cfg.AI_PROVIDER == "foundry" and not (cfg.AI_ENDPOINT and cfg.AI_API_KEY):
        faltan.append("AI_ENDPOINT / AI_API_KEY")
    if cfg.COURSE_TRACK not in cfg.VALID_TRACKS:
        faltan.append(f"COURSE_TRACK inválido ({cfg.COURSE_TRACK})")
    if faltan:
        raise RuntimeError("Faltan: " + ", ".join(faltan))
    return f"proveedor={cfg.AI_PROVIDER} track={cfg.COURSE_TRACK}"


# ---------------------------------------------------------------- 2
@check("2. El modelo de chat responde")
def check_chat() -> str:
    from .provider import get_chat_model

    respuesta = get_chat_model().invoke("Responde exactamente con la palabra: LISTO")
    texto = (respuesta.content or "").strip()
    if not texto:
        raise RuntimeError("El modelo devolvió una respuesta vacía")
    return f'respondió "{texto[:40]}"'


# ---------------------------------------------------------------- 3  CRÍTICA
@check("3. TOOL CALLING (crítica)", critico=True)
def check_tool_calling() -> str:
    from langchain_core.tools import tool
    from pydantic import BaseModel, Field

    from .provider import get_chat_model

    class SaldoInput(BaseModel):
        numero_linea: str = Field(description="Número de línea móvil de 9 dígitos")

    @tool(args_schema=SaldoInput)
    def consultar_saldo(numero_linea: str) -> str:
        """Consulta el saldo disponible de una línea móvil postpago."""
        return "S/ 45.20"

    modelo = get_chat_model().bind_tools([consultar_saldo])
    respuesta = modelo.invoke("¿Cuál es el saldo de la línea 987654321?")
    llamadas = getattr(respuesta, "tool_calls", None) or []

    if not llamadas:
        raise RuntimeError(
            "El modelo NO generó tool_calls. Este modelo o proveedor no soporta "
            "function calling de forma utilizable: el curso no puede construirse sobre él."
        )
    nombre = llamadas[0].get("name")
    args = llamadas[0].get("args", {})
    if nombre != "consultar_saldo":
        raise RuntimeError(f"Llamó a la tool equivocada: {nombre}")
    return f'llamó consultar_saldo(numero_linea="{args.get("numero_linea")}")'


# ---------------------------------------------------------------- 4  CRÍTICA
@check("4. Agente completo con create_agent (crítica)", critico=True)
def check_agent() -> str:
    from langchain.agents import create_agent
    from langchain_core.messages import HumanMessage
    from langchain_core.tools import tool

    from .provider import get_chat_model

    @tool
    def consultar_plan(numero_linea: str) -> str:
        """Devuelve el plan contratado de una línea móvil."""
        return "Plan Max 89, 30 GB, renovación el día 12"

    @tool
    def consultar_averia(distrito: str) -> str:
        """Indica si hay una avería reportada en un distrito."""
        return "Sin averías reportadas"

    agente = create_agent(get_chat_model(), tools=[consultar_plan, consultar_averia])
    salida = agente.invoke(
        {"messages": [HumanMessage(content="¿Qué plan tiene la línea 987654321?")]}
    )
    mensajes = salida["messages"]
    uso_tools = [m for m in mensajes if getattr(m, "tool_calls", None)]
    if not uso_tools:
        raise RuntimeError("El agente no invocó ninguna tool en el bucle ReAct")
    return f"{len(mensajes)} mensajes, {len(uso_tools)} paso(s) con tool"


# ---------------------------------------------------------------- 5
@check("5. Structured output con Pydantic")
def check_structured() -> str:
    from pydantic import BaseModel, Field

    from .provider import get_chat_model

    class Intencion(BaseModel):
        """Clasificación de la consulta de un cliente."""

        categoria: str = Field(description="CONSULTA_PLAN, AVERIA, RECLAMO o PORTABILIDAD")
        urgencia: int = Field(description="Urgencia de 1 a 5")

    modelo = get_chat_model().with_structured_output(Intencion)
    salida = modelo.invoke("Mi internet no funciona desde ayer y ya reclamé dos veces")
    return f"categoria={salida.categoria} urgencia={salida.urgencia}"


# ---------------------------------------------------------------- 6
@check("6. Embeddings")
def check_embeddings() -> str:
    from .provider import get_embeddings

    vectores = get_embeddings().embed_documents(
        ["El SOAT cubre gastos médicos", "La póliza vence en marzo"]
    )
    dim = len(vectores[0])
    if dim < 100:
        raise RuntimeError(f"Dimensión sospechosa: {dim}")
    return f"{len(vectores)} vectores de {dim} dimensiones"


# ---------------------------------------------------------------- 7
@check("7. Qdrant Cloud: indexar y recuperar")
def check_qdrant() -> str:
    from .vectorstore import ensure_collection, get_client, get_vector_store, probe_embedding_dim

    dim = probe_embedding_dim()
    coleccion = f"{cfg.QDRANT_COLLECTION}-selftest"

    cliente = get_client()
    if cliente.collection_exists(coleccion):
        cliente.delete_collection(coleccion)

    ensure_collection(coleccion, vector_size=dim)
    store = get_vector_store(coleccion)
    store.add_texts(
        [
            "El plan Max 89 incluye 30 GB de datos y llamadas ilimitadas.",
            "La portabilidad demora 24 horas hábiles.",
            "El SOAT cubre gastos médicos hasta 5 UIT.",
        ]
    )
    resultados = store.similarity_search("¿cuántos gigas trae el plan?", k=1)
    if not resultados:
        raise RuntimeError("La búsqueda semántica no devolvió resultados")
    return f'dim={dim} · recuperó "{resultados[0].page_content[:45]}..."'


# ---------------------------------------------------------------- 8
@check("8. Langfuse Cloud: enviar una traza")
def check_langfuse() -> str:
    from .observability import get_langfuse_handler
    from .provider import get_chat_model

    handler = get_langfuse_handler()
    get_chat_model().invoke("Di 'traza de prueba'", config={"callbacks": [handler]})
    try:
        from langfuse import get_client as lf_client

        lf_client().flush()
    except Exception:  # noqa: BLE001 — el flush varía entre versiones
        if hasattr(handler, "flush"):
            handler.flush()
    return f"traza enviada a {cfg.LANGFUSE_HOST} (verifícala en el dashboard)"


# ---------------------------------------------------------------- 9
@check("9. Simulador de industria")
def check_simulador() -> str:
    from . import api_client

    salud = api_client.salud()
    if salud.get("estado") != "ok":
        raise RuntimeError(f"El simulador responde '{salud}'")
    return f"{cfg.SIM_BASE_URL} · {salud.get('clientes_telco', '?')} clientes cargados"


# ---------------------------------------------------------------- comparativa
def _probar_candidato(modelo: str) -> dict:
    """Corre las comprobaciones de modelo (2 a 5) sobre un candidato concreto."""
    global RESULTADOS
    original = cfg.HF_CHAT_MODEL
    cfg.HF_CHAT_MODEL = modelo
    RESULTADOS = []
    print(f"\n  ── {modelo} " + "─" * max(0, 52 - len(modelo)))
    try:
        check_chat()
        check_tool_calling()
        check_agent()
        check_structured()
    finally:
        cfg.HF_CHAT_MODEL = original

    por_nombre = {r.nombre.split(".")[0]: r for r in RESULTADOS}
    return {
        "modelo": modelo,
        "responde": por_nombre.get("2", Resultado("", False)).ok,
        "tool_calling": por_nombre.get("3", Resultado("", False)).ok,
        "react": por_nombre.get("4", Resultado("", False)).ok,
        "structured": por_nombre.get("5", Resultado("", False)).ok,
        "segundos": sum(r.segundos for r in RESULTADOS),
    }


def _comparar(candidatos: list[str]) -> int:
    print("\n" + "=" * 74)
    print("  COMPARATIVA DE MODELOS — comprobaciones 2 a 5")
    print("=" * 74)
    print(f"  {GRIS}Probando {len(candidatos)} candidatos. Puede tardar unos minutos.{RESET}")

    filas = [_probar_candidato(m) for m in candidatos]

    def marca(v: bool) -> str:
        return f"{VERDE}sí{RESET} " if v else f"{ROJO}NO{RESET} "

    print("\n\n" + "-" * 74)
    print("  RESUMEN")
    print("-" * 74)
    print(f"  {'Modelo':<38} {'resp':<6} {'tools':<7} {'ReAct':<7} {'JSON':<6} {'tiempo'}")
    print("  " + "-" * 70)
    for f in filas:
        print(f"  {f['modelo'][:36]:<38} {marca(f['responde']):<15} "
              f"{marca(f['tool_calling']):<16} {marca(f['react']):<16} "
              f"{marca(f['structured']):<15} {f['segundos']:>5.1f}s")
    print("  " + "-" * 70)

    aptos = [f for f in filas if f["tool_calling"] and f["react"] and f["structured"]]
    print()
    if not aptos:
        print(f"  {ROJO}VEREDICTO: ningún candidato pasó las comprobaciones críticas.{RESET}")
        print("  Revisa que tu token de Hugging Face tenga permiso de inferencia,")
        print("  o prueba otros modelos con --candidatos modelo1,modelo2")
        return 2

    mejor = min(aptos, key=lambda f: f["segundos"])
    print(f"  {VERDE}VEREDICTO: {len(aptos)} de {len(filas)} candidatos sirven para el curso.{RESET}")
    print(f"  Recomendado por velocidad: {VERDE}{mejor['modelo']}{RESET}")
    print(f"\n  Ponlo en tu .env:\n    HF_CHAT_MODEL={mejor['modelo']}")
    return 0


# ---------------------------------------------------------------- main
def main() -> int:
    parser = argparse.ArgumentParser(description="Verificador del stack del curso")
    parser.add_argument("--solo-modelo", action="store_true",
                        help="Omite Qdrant, Langfuse y el simulador")
    parser.add_argument("--todos-los-tracks", action="store_true",
                        help="Repite las comprobaciones de modelo en los 4 tracks")
    parser.add_argument("--candidatos", nargs="?", const="", default=None,
                        help="Compara varios modelos. Sin valor usa la escalera por defecto; "
                             "o pasa una lista separada por comas")
    parser.add_argument("--debug", action="store_true", help="Muestra el traceback")
    args = parser.parse_args()

    print("\n" + "=" * 74)
    print("  VERIFICADOR DEL STACK — Curso IA Agent Building")
    print("=" * 74)
    from .provider import describe_provider

    try:
        print(f"  Proveedor activo: {describe_provider()}")
    except Exception:  # noqa: BLE001
        print("  Proveedor activo: (no se pudo determinar)")
    print("=" * 74 + "\n")

    check_env()
    if not RESULTADOS[-1].ok:
        return 2

    # Modo comparativa: prueba varios modelos y recomienda uno
    if args.candidatos is not None:
        candidatos = ([m.strip() for m in args.candidatos.split(",") if m.strip()]
                      or CANDIDATOS_POR_DEFECTO)
        return _comparar(candidatos)

    tracks = list(cfg.VALID_TRACKS) if args.todos_los_tracks else [cfg.COURSE_TRACK]
    for track in tracks:
        if args.todos_los_tracks:
            cfg.COURSE_TRACK = track
            print(f"\n  --- track: {track} ---")
        check_chat()
        check_tool_calling()
        check_agent()
        check_structured()
    check_embeddings()
    if not args.solo_modelo:
        check_qdrant()
        check_langfuse()
        check_simulador()

    print("\n" + "-" * 74)
    print("  RESUMEN")
    print("-" * 74)
    print(f"  {'Comprobación':<44} {'Estado':<10} {'Tiempo'}")
    print("  " + "-" * 70)
    for r in RESULTADOS:
        estado = f"{VERDE}PASA{RESET}" if r.ok else f"{ROJO}FALLA{RESET}"
        marca = " *" if r.critico else "  "
        print(f"  {r.nombre[:42]:<44} {estado:<19} {r.segundos:>5.1f}s{marca}")
    print("  " + "-" * 70)
    print(f"  {GRIS}* comprobación crítica: si falla, el curso no puede construirse "
          f"sobre este stack{RESET}")

    criticas_fallidas = [r for r in RESULTADOS if r.critico and not r.ok]
    fallidas = [r for r in RESULTADOS if not r.ok]

    print()
    if criticas_fallidas:
        print(f"  {ROJO}VEREDICTO: BLOQUEANTE.{RESET} Falló una comprobación crítica.")
        print(f"  {ROJO}No construir laboratorios sobre este modelo.{RESET}")
        print("  Ejecuta `python -m comun.check_stack --candidatos` para encontrar uno que sirva.")
        return 2
    if fallidas:
        print(f"  {AMARILLO}VEREDICTO: PARCIAL.{RESET} El modelo sirve, pero "
              f"{len(fallidas)} servicio(s) fallaron.")
        print("  Se puede construir el Módulo 1; revisa lo fallido antes de la sesión 5.")
        return 1
    print(f"  {VERDE}VEREDICTO: STACK VERIFICADO.{RESET} "
          f"Se puede construir el curso completo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
