# Demo 2 · El Dockerfile del curso, línea por línea

No es un script: es el `Dockerfile` de referencia (idéntico al de
[`../solucion/telecomunicaciones/Dockerfile`](../solucion/telecomunicaciones/Dockerfile)),
explicado línea por línea. **No se ejecuta en local** (principio P2) — se lee en clase, y lo
construye la plataforma al recibir el `git push`.

```dockerfile
# 1. Imagen base: Python 3.11, variante "slim" (menos capas, arranca más rápido en un
#    tier gratuito con recursos limitados — no necesitamos las herramientas de compilación
#    de la imagen completa).
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor. Todo lo que sigue es relativo a esto.
WORKDIR /app

# 3. Copiar SOLO requirements.txt primero, no todo el repo. Docker cachea por capa: si el
#    código cambia pero las dependencias no, esta capa se reusa y el build es mucho más
#    rápido. Copiar todo de una vez invalidaría el caché en cada commit.
COPY requirements.txt .

# 4. Instalar dependencias. --no-cache-dir: no guardar la caché de pip dentro de la imagen
#    (la imagen final pesa menos; no hay una segunda instalación que se beneficie de ella).
RUN pip install --no-cache-dir -r requirements.txt

# 5. Ahora sí, copiar el resto del código. Si solo cambia una línea de agent.py, únicamente
#    esta capa (y las siguientes) se reconstruyen — el paso 4 sigue en caché.
COPY . .

# 6. Documenta el puerto que escucha el contenedor. HF Spaces espera el puerto 7860 por
#    convención (es lo que su proxy inverso reenvía) — revisa la doc de tu SDK si cambia.
EXPOSE 7860

# 7. El comando que arranca el proceso. --host 0.0.0.0 es obligatorio: 127.0.0.1
#    (localhost) solo aceptaría conexiones DESDE DENTRO del contenedor, y el proxy de la
#    plataforma llega desde fuera.
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "7860"]
```

## Lo que NO lleva este Dockerfile, y por qué

| No lleva | Por qué |
|---|---|
| Ninguna credencial (`ARG`, `ENV` con secretos) | Las credenciales van como *Space secrets*, nunca horneadas en la imagen — una imagen se puede exportar y compartir; un secreto horneado viaja con ella |
| `USER root` explícito, ni la creación de un usuario no-root | Fuera de alcance de esta sesión (endurecimiento de contenedores es Curso 2); se documenta la omisión para no dar una falsa sensación de "ya está asegurado" |
| `HEALTHCHECK` de Docker | HF Spaces usa **su propio** mecanismo de health check contra `/health`; un `HEALTHCHECK` de Docker sería redundante en este proveedor concreto |

## La pregunta que cierra la demo

Si moviste este mismo `Dockerfile` a otra plataforma (Render, Railway, un servidor propio),
¿qué línea cambiarías? Respuesta: en principio, ninguna del `Dockerfile` — cambiarías el
`CMD`'s puerto si la plataforma exige otro, y la forma de inyectar secretos. Es la misma
lección de la portabilidad que vuelve en el bonus de Foundry.
