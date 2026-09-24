# Acceso a Azure — las dos vías

> Sigue los pasos con el docente. Los nombres y la ubicación de las opciones del portal
> pueden cambiar; comprobar el acceso antes de iniciar la práctica.

---

## Vía A · Suscripción propia (recomendada)

Para quien pueda registrar una tarjeta. Usa el crédito inicial gratuito de Azure y te deja con
tu propio entorno — es además **prerrequisito del Curso 2**, que sí usa Azure a fondo.

### El modelo de recursos de Azure

```
   Suscripción
   └── Grupo de recursos
       └── Recurso de Azure AI Foundry
           └── Proyecto
               └── Deployment del modelo (ej. gpt-4.1-mini)
```

Cada nivel existe para agrupar permisos y costos. Un **grupo de recursos** es la unidad que
normalmente se borra entera al terminar (evita dejar recursos huérfanos cobrando).

### Pasos

1. Crea una cuenta de Azure en [azure.microsoft.com/free](https://azure.microsoft.com/free) si
   no tienes una — requiere una tarjeta para verificación, aunque el crédito inicial es gratuito.
2. En el portal, crea un **grupo de recursos** nuevo (nómbralo algo reconocible, ej.
   `rg-curso-langchain-bonus`, para poder borrarlo entero al terminar).
3. Dentro de ese grupo, crea un recurso de **Azure AI Foundry** y, dentro de él, un **proyecto**.
4. En el proyecto, crea un **deployment** de un modelo de chat (ej. `gpt-4.1-mini`) — anota el
   nombre del deployment, lo necesitas como `AZURE_AI_MODEL_DEPLOYMENT_NAME`.
5. Anota el **endpoint del proyecto** (`FOUNDRY_PROJECT_ENDPOINT` / el equivalente a
   `AI_ENDPOINT` de `comun/settings.py`) y genera una **clave de API** del proyecto
   (`AI_API_KEY`).
6. Asegúrate de tener el rol **Foundry Project Manager** en el proyecto — lo exige el despliegue
   de Hosted agents (paso 7 del `README.md`).

### Variables a completar en tu `.env`

```
AI_PROVIDER=foundry
AI_ENDPOINT=<endpoint de tu proyecto>
AI_API_KEY=<tu clave de API>
AI_MODEL=<nombre de tu deployment, ej. gpt-4.1-mini>
```

---

## Vía B · Proyecto del docente

Para quien no quiera o no pueda registrar una tarjeta. El docente despliega un proyecto de Foundry
compartido y reparte claves temporales — te saltas la
creación de recursos y revisas con el docente los pasos de esta guía.

| Qué | Detalle |
|---|---|
| Quién paga | El docente, con el consumo del proyecto compartido |
| Claves | Temporales, rotadas al cerrar el periodo del bonus |
| Límite | Un `deployment` pequeño; se anuncia la cuota disponible al momento de repartir claves |
| Qué se pierde | La creación de recursos (pasos 2-4 de la Vía A) — se sustituye por el recorrido guiado |

Con la Vía B, completas tu `.env` con las variables que el docente reparta directamente
(`AI_ENDPOINT`, `AI_API_KEY`, `AI_MODEL`) y saltas directo al **paso 4** del `README.md` (el
switch).

---

## Verificación de que el switch funciona

```bash
python -m comun.check_stack --solo-modelo
```

Con `AI_PROVIDER=foundry` en el `.env`, esta comprobación debe pasar en verde igual que con
`huggingface` — es la prueba de que `comun/provider.py` está haciendo su trabajo.
