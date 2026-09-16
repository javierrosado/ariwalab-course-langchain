# DESPLIEGUE — [equipo] · banca

> Plantilla. Completa cada campo con los datos reales de tu Space. No dejes ningún
> placeholder entre `< >` en la versión que entregas al evaluador.

## URL y credencial

| Campo | Valor |
|---|---|
| URL pública del Space | `<https://tu-usuario-tu-space.hf.space>` |
| API key para el evaluador (`AGENT_API_KEY`) | `<pégala aquí solo en tu copia privada, nunca en el repo público>` |

## Verificación

Salida de `python docente/verificar_despliegue.py --url <tu-url> --key <tu-key>`:

```
<pega aquí la salida completa del comando>
```

## Cold start

| Medición | Segundos |
|---|---|
| Primer request tras ≥15 min sin tráfico | `<N>` |
| Segundo request, inmediato | `<N>` |

¿Qué tan aceptable te parece esa latencia para tu caso de uso? `<1-2 frases>`

## Secretos cargados (nombres, nunca valores)

- [ ] `HF_TOKEN`
- [ ] `QDRANT_URL`
- [ ] `QDRANT_API_KEY`
- [ ] `AGENT_API_KEY`
- [ ] `COURSE_TRACK`
- [ ] `DATA_SOURCE`
- [ ] `SIM_BASE_URL`
- [ ] `SIM_API_KEY`

## Confirmación de higiene

- [ ] `git log -p | grep -i "hf_\|sk-lf\|api_key"` sobre el repo del equipo no devuelve nada.
