# -*- coding: utf-8 -*-
"""Genera docente/especificacion-tools.md a partir del código real de las tools.

Ejecutar desde la raíz del curso:
    python docente/generar_especificacion_tools.py

El documento se genera por introspección de los objetos @tool, de modo que nunca
puede desincronizarse del código. Es la referencia que el profesor usa para revisar
el diseño de las herramientas (reglas A1 y A2) y para diagnosticar la matriz de
confusión de docente/matriz_seleccion.py: cuando el modelo elige la tool equivocada,
la causa casi siempre está en la docstring que aparece aquí.
"""

import importlib.util
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

TRACKS = {
    "telecomunicaciones": ("AndesMóvil", "Atención al cliente móvil postpago"),
    "banca": ("Banco Inti", "Banca personal y detección de operación sospechosa"),
    "retail": ("MercaSur", "Post-venta de e-commerce"),
    "seguros": ("Andina Seguros", "Asesoría SOAT y reporte de siniestros"),
}


def cargar(track):
    ruta = RAIZ / "proyecto-final" / track / "app" / "tools" / "domain_tools.py"
    spec = importlib.util.spec_from_file_location(f"tools_{track}", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def esquema_openai(t):
    """Devuelve el bloque de tool en formato OpenAI, que es el que consume el chat_template."""
    schema = t.args_schema.model_json_schema() if t.args_schema else {"type": "object", "properties": {}}
    schema.pop("title", None)
    for p in schema.get("properties", {}).values():
        p.pop("title", None)
    return {"type": "function",
            "function": {"name": t.name, "description": t.description.strip(), "parameters": schema}}


out = ["""# Especificación de las tools del curso

> **Generado automáticamente** por `docente/generar_especificacion_tools.py` a partir del código
> real. No editar a mano: regenerar tras cualquier cambio en las tools.
>
> **Para el profesor:** el curso usa un modelo genérico sin afinar, así que
> **la única guía que tiene el modelo para elegir bien una herramienta es lo que está escrito
> aquí**. Si `docente/matriz_seleccion.py` reporta una confusión entre dos tools, la corrección
> se hace sobre la docstring de este documento, no sobre el modelo.

## Reglas de diseño aplicadas

| Regla | Qué exige | Por qué |
|-------|-----------|---------|
| **A1** | Máximo **4 tools núcleo** enlazadas a la vez | La precisión de selección cae pasadas 4-5 herramientas y los errores se componen |
| **A2** | Toda docstring dice **cuándo NO** usar la tool | Una descripción ambigua se paga en cada paso del bucle |
| **A4** | Los errores se devuelven como **texto legible**, nunca como excepción | El agente necesita leer "no existe esa línea" para replantear su plan |

Las 2 tools opcionales de cada track quedan como reto del Laboratorio 4 y **no** deben
enlazarse junto a las 4 núcleo.

---
"""]

for track, (empresa, caso) in TRACKS.items():
    mod = cargar(track)
    out.append(f"\n## Track `{track}` — {empresa}\n\n*{caso}*\n")

    for etiqueta, lista in [("Tools núcleo (Laboratorio 4)", mod.TOOLS_NUCLEO),
                            ("Tools opcionales (reto)", mod.TOOLS_OPCIONALES)]:
        out.append(f"\n### {etiqueta}\n")
        out.append("| Tool | Parámetros | Qué hace |")
        out.append("|------|-----------|----------|")
        for t in lista:
            props = (t.args_schema.model_json_schema().get("properties", {}) if t.args_schema else {})
            params = ", ".join(f"`{k}`" for k in props) or "—"
            resumen = t.description.strip().split("\n")[0]
            out.append(f"| `{t.name}` | {params} | {resumen} |")

    out.append("\n<details>\n<summary><b>Esquemas JSON completos (formato OpenAI)</b></summary>\n")
    out.append("```json")
    out.append(json.dumps([esquema_openai(t) for t in mod.TOOLS_NUCLEO], ensure_ascii=False, indent=2))
    out.append("```\n</details>\n")
    out.append("\n---")

# Ejemplo de entrenamiento
mod = cargar("telecomunicaciones")
ejemplo = {
    "messages": [
        {"role": "system", "content": "Eres el asistente de AndesMóvil, operador móvil peruano."},
        {"role": "user", "content": "¿Qué plan tengo en la 987654321?"},
        {"role": "assistant", "content": "", "tool_calls": [
            {"type": "function", "function": {"name": "get_customer_plan",
                                              "arguments": "{\"numero_linea\": \"987654321\"}"}}]},
        {"role": "tool", "name": "get_customer_plan",
         "content": "Línea 987654321 · Plan: Max 89 (AM-MAX-89) · Estado: ACTIVO"},
        {"role": "assistant", "content": "Tienes el plan Max 89, que incluye 30 GB de datos. Tu línea está activa."},
    ]
}
out.append(f"""
## Cómo se ve una llamada a herramienta en el protocolo

Los cinco mensajes de un ciclo ReAct completo, tal como viajan por el cable. Útil para depurar
cuando una traza de Langfuse no cuadra, y para entender qué recibe realmente el modelo:

```jsonl
{json.dumps(ejemplo, ensure_ascii=False)}
```

## Verificación

```bash
python docente/verificar_tools.py
```

Comprueba que las 24 tools corren contra los datasets reales, que ninguna lanza excepción ante
datos inexistentes, que toda docstring cumple A2 y que ningún track supera las 4 tools núcleo.
No requiere credenciales ni acceso a un modelo.

```bash
python docente/matriz_seleccion.py --track telecomunicaciones
```

Mide si el modelo **elige** la herramienta correcta: 20 consultas por track contra la tool
esperada, con matriz de confusión. Este sí requiere `HF_TOKEN`; usa `--simular` para probar el
arnés sin gastar cuota.
""")

destino = RAIZ / "docente" / "especificacion-tools.md"
destino.write_text("\n".join(out), encoding="utf-8")
print(f"Generado: {destino.relative_to(RAIZ)} ({destino.stat().st_size} bytes)")
