# Python, entorno y secretos

> Sesión 0 · paso 3 · 45 minutos
> Al terminar tendrás el entorno del curso funcionando y el `.env` configurado.

---

## 1. Requisitos

| Herramienta | Versión | Cómo verificar |
|-------------|---------|----------------|
| Python | 3.10 o superior (3.13 recomendado) | `python --version` |
| pip | cualquiera reciente | `pip --version` |
| git | cualquiera | `git --version` |
| Editor | VS Code recomendado | — |

Si `python` no responde en Windows, prueba `py --version`.

---

## 2. Entorno virtual

Un entorno virtual aísla las dependencias del curso de las de tu sistema. **No es opcional**:
sin él, una versión distinta de `pydantic` en otro proyecto puede romper tus laboratorios.

**Windows (PowerShell):**
```powershell
cd C:\ruta\a\ariwalab-course-langchain
python -m venv .venv
.venv\Scripts\activate
```

**macOS o Linux:**
```bash
cd /ruta/a/ariwalab-course-langchain
python3 -m venv .venv
source .venv/bin/activate
```

Sabes que está activo porque el prompt muestra `(.venv)` al inicio. **Tienes que activarlo cada
vez que abres una terminal nueva.** El error más frecuente del curso es un `ModuleNotFoundError`
causado simplemente por haber olvidado esto.

```powershell
pip install -r requirements.txt
```

---

## 3. Variables de entorno y el archivo `.env`

Las credenciales **nunca** van en el código. Van en un archivo `.env` que git ignora.

```powershell
copy .env.example .env      # Windows
cp .env.example .env        # macOS / Linux
```

Ahora abre `.env` y complétalo. Por ahora solo necesitas `HF_TOKEN`; el resto lo llenarás en la
sesión 4 y en la 9.

```dotenv
AI_PROVIDER=huggingface
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxx
HF_CHAT_MODEL=Qwen/Qwen3-32B
COURSE_TRACK=telecomunicaciones
```

### Reglas de oro sobre secretos

| Regla | Por qué |
|-------|---------|
| El `.env` **nunca** se sube al repositorio | Un token en GitHub se detecta y se abusa en minutos |
| Nunca pegues un token en el chat de clase ni en una captura | Es una credencial, como una contraseña |
| Si lo expusiste, **revócalo** y genera otro | Rotar es barato; una fuga no |
| En producción los secretos van en el gestor de la plataforma | En la sesión 8 usarás *Space secrets* |

El `.gitignore` del curso ya excluye `.env`. Verifica que sigue ahí antes de tu primer commit.

---

## 4. Cómo se lee la configuración en el curso

Ningún archivo del curso llama a `os.getenv()` directamente. Todo pasa por `comun/settings.py`,
que es el único lugar donde se declara qué variables existen.

```python
from comun import settings as cfg
from comun.provider import get_chat_model, describe_provider

print(describe_provider())        # qué modelo estás usando ahora mismo
modelo = get_chat_model()         # el modelo, sin saber de qué proveedor viene
```

Esta indirección parece innecesaria hoy y es la razón por la que, en el bonus final, migrarás
el agente entero a Microsoft Foundry cambiando **una línea del `.env`**.

---

## 5. Pydantic v2 — el prerrequisito que más cuesta

Pydantic es la librería que define esquemas de datos tipados y los valida. En este curso se usa
para dos cosas centrales:

1. Describir los **argumentos de cada herramienta** del agente.
2. Forzar que el modelo devuelva **salida estructurada** en vez de texto libre.

Si no dominas Pydantic, las sesiones 2, 3 y 4 se te van a hacer cuesta arriba.

```python
from enum import Enum
from pydantic import BaseModel, Field

class Urgencia(str, Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"

class Consulta(BaseModel):
    """Consulta clasificada de un cliente."""
    categoria: str = Field(description="Categoría de la consulta")
    urgencia: Urgencia = Field(description="Nivel de urgencia")
    numero_linea: str | None = Field(default=None, description="Línea si el cliente la mencionó")

c = Consulta(categoria="AVERIA", urgencia="ALTA")
print(c.model_dump_json())
print(Consulta.model_json_schema())   # esto es lo que el modelo recibe
```

> **Detalle que importa:** el `description` de cada `Field` **no es documentación**. Se envía al
> modelo dentro del esquema JSON, y es lo que le explica qué poner en cada campo. Un `description`
> vago produce datos malos. Lo verás en la sesión 2.

### Ejercicio obligatorio antes de la Sesión 2

Define un modelo Pydantic llamado `Reclamo` con:

- `tipo`: un `Enum` con `FACTURACION`, `AVERIA`, `PORTABILIDAD`
- `descripcion`: texto de entre 10 y 200 caracteres
- `numero_linea`: exactamente 9 dígitos
- `requiere_tecnico`: booleano con valor por defecto `False`

Luego imprime `Reclamo.model_json_schema()` y comprueba que las restricciones aparecen en el
esquema. Ese esquema es, literalmente, lo que leerá el modelo.

---

## 6. Comprobación final

Con el entorno activo y el `.env` completo:

```powershell
python -m comun.check_stack --solo-modelo
```

Deberías ver las comprobaciones 1 a 5 en verde. Si la 3 o la 4 fallan, avisa al docente: son
las comprobaciones críticas de tool calling y no dependen de ti.

---

## Errores frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Estás ejecutando desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `ModuleNotFoundError: langchain` | El `venv` no está activado | Actívalo y verifica que veas `(.venv)` |
| `Falta la variable HF_TOKEN` | El `.env` está vacío o en otra carpeta | Debe estar en la raíz, junto a `requirements.txt` |
| `401 Unauthorized` | Token sin permiso de inferencia | Regenera el token con ese permiso marcado |
| Acentos rotos en Windows | Codificación de la consola | `chcp 65001` antes de ejecutar |

**Siguiente paso:** [`alta-de-cuentas.md`](alta-de-cuentas.md)
