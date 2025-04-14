FROM python:3.12-slim

WORKDIR /prep

COPY Requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY models/ models/
COPY model_store/ model_store/
COPY ai_models/ ai_models/
COPY output/ output/
COPY .env .env
CMD ["python", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
