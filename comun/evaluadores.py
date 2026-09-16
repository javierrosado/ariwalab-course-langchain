"""Los 3 evaluators determinísticos de la sesión 10.

Ninguno usa un modelo: se pueden correr mil veces y dan lo mismo (a diferencia del
juez del bloque 3, que sí es un LLM). Por eso son los que sostienen la nota del L10;
el juez es demo.

Los 3 leen del mismo `recursos/golden/consultas-<track>.json` que ya alimentó el L2
(clasificación), el L4 (selección de tool) y el L5 (categoría OTRO). Aquí se usa por
cuarta vez, completo: sus 30 filas son el dataset de evaluación de esta sesión.
"""

from __future__ import annotations

NINGUNA = "(ninguna)"


def evaluar_tool(tool_llamada: str | None, tool_esperada: str | None) -> bool:
    """¿El agente llamó a la tool que el golden set esperaba?

    Es el mismo criterio de `docente/matriz_seleccion.py` (existe desde el L4):
    comparar el nombre de la tool invocada contra `tool_esperada`. `None` en
    cualquiera de los dos lados significa "no llamó a ninguna tool" — así se
    evalúan también las 10 consultas OTRO, donde lo correcto es NO llamar nada.
    """
    return (tool_llamada or None) == (tool_esperada or None)


def evaluar_exactitud(respuesta: str, respuesta_esperada: str | None) -> bool:
    """¿La respuesta contiene el dato correcto?

    Comprueba si `respuesta_esperada` aparece, sin distinguir mayúsculas, dentro del
    texto de la respuesta del agente. `respuesta_esperada is None` significa que la
    fila del golden set no tiene un dato verificable (un saludo, una pregunta
    abierta): en ese caso el evaluator no aplica y se considera aprobado por
    definición — no hay nada que comprobar, no que el agente haya acertado algo.
    """
    if respuesta_esperada is None:
        return True
    return respuesta_esperada.strip().lower() in respuesta.strip().lower()


def evaluar_groundedness(respuesta: str, contexto_recuperado: str | None,
                          respuesta_esperada: str | None) -> bool:
    """¿La cita existe y sostiene la afirmación?

    No basta con que el retriever haya devuelto algo (eso solo prueba que se llamó
    a la tool), y no basta con que el dato correcto exista EN ALGÚN LUGAR del
    corpus (eso no prueba que el agente lo haya usado). Groundedness exige las dos
    cosas a la vez: que la respuesta afirme el dato correcto, Y que ese dato esté
    también en el texto que de verdad se recuperó — si el agente acierta por
    casualidad pero el chunk recuperado no lo respalda, o si el chunk lo respalda
    pero el agente dijo otra cosa, es una alucinación con apariencia de cita.

    `contexto_recuperado` es la salida cruda de `retrieve_knowledge_base` (S5): el
    string con los bloques "[Fuente: archivo]\\ncontenido". Si `respuesta_esperada`
    es `None` (nada verificable en esta fila), no aplica y se considera aprobado —
    igual que en `evaluar_exactitud`.
    """
    if respuesta_esperada is None:
        return True
    if not contexto_recuperado:
        return False
    dato = respuesta_esperada.strip().lower()
    afirmado = dato in respuesta.strip().lower()
    respaldado = dato in contexto_recuperado.strip().lower()
    return afirmado and respaldado


def evaluar_caso(caso: dict, respuesta: str, tool_llamada: str | None = None,
                  contexto_recuperado: str | None = None) -> dict:
    """Corre los 3 evaluators sobre una fila del golden set y su respuesta real.

    `caso` es una entrada de `recursos/golden/consultas-<track>.json`
    (campos: consulta, categoria, tool_esperada, respuesta_esperada).
    """
    return {
        "consulta": caso["consulta"],
        "categoria": caso["categoria"],
        "tool": evaluar_tool(tool_llamada, caso.get("tool_esperada")),
        "exactitud": evaluar_exactitud(respuesta, caso.get("respuesta_esperada")),
        "groundedness": evaluar_groundedness(respuesta, contexto_recuperado,
                                             caso.get("respuesta_esperada")),
    }


def resumen(resultados: list[dict]) -> dict:
    """Tasa de acierto de cada evaluator sobre una corrida completa (v1 o v2)."""
    n = len(resultados)
    if n == 0:
        return {"n": 0, "tool": 0.0, "exactitud": 0.0, "groundedness": 0.0}
    return {
        "n": n,
        "tool": sum(r["tool"] for r in resultados) / n,
        "exactitud": sum(r["exactitud"] for r in resultados) / n,
        "groundedness": sum(r["groundedness"] for r in resultados) / n,
    }
