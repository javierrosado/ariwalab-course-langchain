"""Demo 2 · Guardrail de acción: bloquear una tool de escritura no autorizada.

Ejecutar desde la raíz del curso:
    python modulo-2-agentes-avanzados/sesion-06-automatizacion-guardrails/code/02_guardrail_accion.py

No requiere HF_TOKEN: simula la propuesta de tool_call que haría el modelo, para
mostrar el guardrail sin depender de si el modelo "decide" bien o mal ese día.

Qué deberías observar:
  1. El modelo PUEDE proponer una acción prohibida (aquí, simulado) — el guardrail no
     confía en que nunca lo intente.
  2. La acción prohibida se bloquea ANTES de ejecutar la tool, no después.
  3. Una acción permitida, sin confirmación, tampoco se ejecuta si la tool la requiere
     (regla del bloque 4 de la Sesión 4).
"""

from __future__ import annotations

# Lista de prohibidos de banca (ver README.md de la sesión, sección 5).
PROHIBITED_ACTIONS = {"transfer_funds", "execute_transfer", "reveal_full_card_number"}

# Tools que exigen confirmación explícita antes de ejecutarse (ver Sesión 4, bloque 4).
REQUIRES_CONFIRMATION = {"request_card_block"}


class ProposedAction:
    def __init__(self, tool_name: str, args: dict):
        self.tool_name = tool_name
        self.args = args


def check_action(action: ProposedAction) -> tuple[bool, str]:
    """Guardrail de acción. Devuelve (se_ejecuta, motivo_si_no)."""
    if action.tool_name in PROHIBITED_ACTIONS:
        return False, f"'{action.tool_name}' está en la lista de acciones prohibidas de este track."
    if action.tool_name in REQUIRES_CONFIRMATION and not action.args.get("confirmado_por_cliente"):
        return False, f"'{action.tool_name}' exige confirmación explícita del cliente antes de ejecutarse."
    return True, ""


PROPOSED_ACTIONS = [
    ProposedAction("get_account_balance", {"numero_cuenta": "00112233445566"}),
    ProposedAction("transfer_funds", {"origen": "00112233445566", "destino": "00554433221100", "monto": 500}),
    ProposedAction("request_card_block", {"tarjeta_id": "TC-00123", "confirmado_por_cliente": False}),
    ProposedAction("request_card_block", {"tarjeta_id": "TC-00123", "confirmado_por_cliente": True}),
]


def main() -> None:
    print("=" * 72)
    print("  DEMO 2 · Guardrail de acción")
    print("=" * 72)

    for action in PROPOSED_ACTIONS:
        print(f"\n  El modelo propone: {action.tool_name}({action.args})")
        allowed, reason = check_action(action)
        if allowed:
            print(f"  ✔ Se ejecuta.")
        else:
            print(f"  ❌ BLOQUEADO: {reason}")

    print("""

  El punto crítico: el guardrail de acción se ejecuta SIEMPRE, sin importar qué tan
  persuasivo fue el mensaje que llevó al modelo a proponer esa acción. Por más que la
  inyección del guardrail de entrada (demo 1) se hubiera colado, esta segunda capa
  sigue evaluando la acción concreta antes de tocar ningún sistema real.
""")


if __name__ == "__main__":
    main()
