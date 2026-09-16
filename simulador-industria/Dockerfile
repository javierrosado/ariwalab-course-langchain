# Simulador de industria — imagen para Hugging Face Spaces (SDK: docker)
#
# Construir y ejecutar en local:
#   docker build -t simulador-industria -f simulador-industria/Dockerfile .
#   docker run -p 7860:7860 simulador-industria
#
# Nota: el contexto de construcción es la RAÍZ DEL CURSO, no esta carpeta,
# porque la imagen necesita copiar también recursos/datasets/.

FROM python:3.13-slim

WORKDIR /app

# Hugging Face Spaces expone el puerto 7860
ENV PORT=7860 \
    PYTHONUNBUFFERED=1 \
    DB_PATH=/tmp/simulador.db \
    DATASETS_DIR=/app/datasets

COPY simulador-industria/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Código del simulador
COPY simulador-industria/ ./

# Datos sintéticos de las 4 industrias
COPY recursos/datasets/ ./datasets/

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
