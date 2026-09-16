# L8 · Seguros — Andina Seguros · Dockerfile (checkpoint de referencia)
# Comentado línea por línea en ../../code/02_dockerfile_comentado.md. No se ejecuta en
# local (P2): lo construye HF Spaces al recibir el git push.
#
# Este Dockerfile asume que api.py vive en la RAÍZ del repo del equipo (no anidado bajo
# modulo-3-produccion/... como en este repo de referencia) — el equipo copia api.py y
# Dockerfile a su propio repositorio del proyecto, no despliega este repo del curso.

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]
