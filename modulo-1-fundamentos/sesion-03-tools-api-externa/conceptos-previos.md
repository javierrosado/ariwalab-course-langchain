# Conceptos previos · Sesión 3

> Pre-work asíncrono de 1 h. Termina con una verificación de 2 minutos contra el simulador real.

---

## 1. Docstrings de Python

La docstring de una tool **es el prompt** que el modelo lee para decidir si la usa. No es
documentación para otro programador: es la única información (junto al nombre y al esquema de
argumentos) que el modelo tiene sobre qué hace tu función.

## 2. Decoradores

`@tool` es un decorador: una función que envuelve a otra para darle comportamiento extra (aquí,
convertirla en algo que un modelo puede invocar). Si nunca escribiste un decorador propio, basta
con entender que `@tool` sobre una función normal la convierte en un objeto que expone su
nombre, su docstring y su esquema de argumentos.

## 3. REST con `httpx`: GET, headers, códigos de estado

Tu tool va a llamar a una API real. Repasa: qué es un `GET`, cómo se manda una cabecera de
autenticación (`X-API-Key`), y qué significan los códigos `200`, `404`, `401` y `5xx`.
`comun/api_client.py` ya hace esto por ti — hoy lo lees, no lo reescribes.

## 4. Parsing de JSON, `KeyError`, timeouts

Una respuesta HTTP exitosa no garantiza que el JSON tenga el campo que esperas. Repasa cómo
acceder a un diccionario sin que un campo ausente reviente tu código (`.get()` en vez de `[]`
cuando el campo puede faltar), y qué es un timeout de red.

## 5. `try/except` con mensajes útiles **al modelo**

La diferencia entre capturar una excepción para un log y capturarla para que el modelo la lea y
actúe en consecuencia. Ver `README.md` sección 3 para la tabla completa de ejemplos.

## 6. La guía del simulador y tu API key de equipo

Lee `simulador-industria/docs/GUIA-ALUMNO.md`. Tu equipo debe tener su `SIM_API_KEY` en el
`.env` **antes** de esta sesión.

---

## Verificación de entrada · 2 minutos

```bash
python -c "from comun.api_client import salud; print(salud())"
```

Deberías ver una respuesta del simulador (no requiere API key: `/health` es público). Si no
obtienes respuesta, **avisa antes del martes**, no durante la sesión. Es el mismo principio del
pase de entrada de Pydantic de la Sesión 2: los bloqueos se descubren con margen, no en la
sesión que vale la nota del módulo.

---

## Checklist final antes de la sesión

- [ ] `python -c "from comun.api_client import salud; print(salud())"` responde.
- [ ] Tengo `SIM_API_KEY` en mi `.env`.
- [ ] Puedo explicar con mis palabras la diferencia entre "el modelo genera la llamada" y "mi
  código la ejecuta".
- [ ] Repasé el ejemplo de docstring antes/después de `README.md` sección 2.
