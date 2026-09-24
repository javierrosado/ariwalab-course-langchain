# Demos de la Sesión 2

Ejecuta siempre **desde la raíz del curso**, con el entorno virtual activado.

| Demo | Comando | Credenciales | Qué demuestra |
|------|---------|--------------|----------------|
| 1 | `python .../code/01_plantilla_dominio.py` | `HF_TOKEN` | Rol+Contexto+Tarea+Formato: quitar el Formato degrada más que quitar el Rol |
| 2 | `python .../code/02_few_shot.py` | `HF_TOKEN` | El mismo clasificador con 0, 2 y 4 ejemplos |
| 3 | `python .../code/03_structured_crudo_vs_robusto.py` | `HF_TOKEN` | **La demo del fallo**: `with_structured_output()` crudo vs `extraer_con_detalle()` |
| 4 | `python .../code/04_tokens_y_costo.py` | No | El few-shot se paga en cada llamada; el historial crece más rápido |

## Qué deberías notar en cada una

**Demo 1.** La respuesta sin FORMATO puede tener la categoría correcta "escondida" en una frase,
pero no la puedes parsear con confianza. Sin FORMATO no tienes un contrato, tienes una esperanza.

**Demo 2.** El salto de 0 a 2 ejemplos suele corregir la clasificación en las consultas
ambiguas. El salto de 2 a 4 casi nunca cambia nada — y cuesta el doble de tokens de ejemplos.

**Demo 3 — la demo de la sesión.** Compara los dos bloques de salida: el crudo puede devolver
`None` o un objeto con un campo inválido sin ningún aviso; el robusto siempre termina en un
`Intencion` válido o en una `ExtraccionFallida` explícita. Ese es el valor de A3.

**Demo 4.** El few-shot es un costo fijo (igual en el turno 1 y el turno 20); el historial de
conversación es un costo que crece. Para el L2 (un solo turno) el few-shot domina; para un
agente de varios turnos, no.

## Si algo falla

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: comun` | Ejecutas desde otra carpeta | Ejecuta siempre desde la raíz del curso |
| `ExtraccionFallida` en la demo 3 | El modelo no logró producir un `Intencion` válido ni al reintentar | Es un resultado válido de la demo: muéstralo como el "fallo controlado" |
| `401 Unauthorized` | Token sin permiso de inferencia | Regenera el token de Hugging Face |
| La demo 4 usa estimación, no tokens reales | `transformers` no está instalado | `pip install transformers` (opcional, no bloquea la demo) |
