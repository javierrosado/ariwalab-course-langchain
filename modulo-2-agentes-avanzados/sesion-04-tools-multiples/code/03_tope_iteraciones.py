"""Demo 3 · El mismo agente, con y sin tope de iteraciones (regla A4).

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-04-tools-multiples/code/03_tope_iteraciones.py

No requiere HF_TOKEN: la tool "flaky" se simula localmente para no depender del simulador
en vivo ni de la latencia de CHAOS_RATE. La prueba de estrés CONTRA el simulador real, con
`?_fallo=error503` de verdad, es la Sesión 7 (L7) — esto es la versión de bolsillo para ver
el mecanismo hoy, con un modelo simulado en vez de uno real.

Qué deberías observar:
  1. Sin tope, un agente que no logra resolver la tarea puede reintentar para siempre
     (aquí, hasta MAX_ITERATIONS_SIN_TOPE, para no colgar la demo de verdad).
  2. Con tope, el agente se detiene a las pocas vueltas y responde con un mensaje claro
     de derivación en vez de fallar en silencio o repetir indefinidamente.
"""

from __future__ import annotations


class FlakyTool:
    """Una tool que falla las primeras N veces y luego funciona — como un 503 intermitente."""

    def __init__(self, name: str, fails_before_success: int):
        self.name = name
        self.fails_before_success = fails_before_success
        self.calls = 0

    def invoke(self, args: dict) -> str:
        self.calls += 1
        if self.calls <= self.fails_before_success:
            raise RuntimeError("503 Service Unavailable (simulado)")
        return f"Diagnóstico OK tras {self.calls} intento(s): la línea está operativa."


class ModeloTerco:
    """Simula un modelo que, ante un error de tool, siempre decide reintentar la misma tool."""

    def __init__(self, tool_name: str):
        self.tool_name = tool_name
        self.turno = 0

    def invoke(self, messages):
        self.turno += 1
        ultimo = messages[-1]
        contenido = ultimo.get("content", "") if isinstance(ultimo, dict) else str(ultimo)
        if "error" in contenido.lower() or self.turno == 1:
            return {"tool_calls": [{"name": self.tool_name, "args": {}, "id": f"call_{self.turno}"}]}
        return {"tool_calls": [], "content": "Listo, ya lo revisé."}


def run_with_cap(tool: FlakyTool, max_iterations: int | None) -> tuple[str, int]:
    """Bucle manual (mismo patrón de run_agent en 01_multi_tool.py), con tope opcional."""
    modelo = ModeloTerco(tool.name)
    messages = [{"role": "human", "content": "Diagnostica mi línea, por favor"}]
    iteraciones = 0
    limite = max_iterations if max_iterations is not None else 1000  # "sin tope" con techo de seguridad

    while iteraciones < limite:
        iteraciones += 1
        respuesta = modelo.invoke(messages)
        if not respuesta["tool_calls"]:
            return respuesta["content"], iteraciones
        for call in respuesta["tool_calls"]:
            try:
                resultado = tool.invoke(call["args"])
                messages.append({"role": "tool", "content": resultado})
            except RuntimeError as e:
                messages.append({"role": "tool", "content": f"Error: {e}"})

    return ("Se alcanzó el límite de iteraciones. No se pudo completar el diagnóstico: "
            "derivo tu caso a un asesor humano."), iteraciones


def main() -> None:
    print("=" * 72)
    print("  DEMO 3 · Tope de iteraciones (regla A4)")
    print("=" * 72)

    print("\n  Escenario: run_line_diagnostics falla 3 veces (simulando un 503) y al "
          "cuarto intento funciona.\n")

    print("-" * 72)
    print("  SIN TOPE (max_iterations=None, con techo de seguridad de 1000 para la demo)")
    print("-" * 72)
    tool_sin_tope = FlakyTool("run_line_diagnostics", fails_before_success=3)
    respuesta, n = run_with_cap(tool_sin_tope, max_iterations=None)
    print(f"  Resultado tras {n} iteración(es): {respuesta}")
    print("  → Funcionó, pero solo porque tuvo suerte con 3 fallos. Si el servicio hubiera")
    print("    estado caído de verdad (no 3 fallos, sino indefinidos), este bucle habría")
    print("    seguido gastando cuota del modelo sin límite.")

    print("\n" + "-" * 72)
    print("  CON TOPE (max_iterations=2)")
    print("-" * 72)
    tool_con_tope = FlakyTool("run_line_diagnostics", fails_before_success=3)
    respuesta, n = run_with_cap(tool_con_tope, max_iterations=2)
    print(f"  Resultado tras {n} iteración(es): {respuesta}")

    print("""

  La lección: el tope de iteraciones no es "para que no se cuelgue" en abstracto — es lo
  que convierte un 503 intermitente en un mensaje claro al usuario, en vez de en una
  factura de cuota inesperada o un agente que parece congelado. En tu Laboratorio 4, tu
  agent.py debe implementar este mismo tope antes de conectarlo al simulador real.
""")


if __name__ == "__main__":
    main()
