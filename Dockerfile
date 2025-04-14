FROM python:3.12-slim

WORKDIR /prep

# Install git and other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt

COPY app/ app/
COPY models/ models/
COPY model_store/ model_store/
COPY ai_models/ ai_models/
COPY output/ output/
COPY .env .env
CMD ["python", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
