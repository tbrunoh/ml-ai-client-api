# syntax=docker/dockerfile:1.4
FROM python:3.12-slim

WORKDIR /prep

# Install git, SSH client, and other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    openssh-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add GitHub to known_hosts to avoid host key verification issues
RUN mkdir -p /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts

# Use BuildKit to mount the SSH key for private repository access
COPY Requirements.txt .
RUN --mount=type=ssh pip3 install --no-cache-dir -r Requirements.txt

COPY app/ app/
COPY models/ models/
COPY model_store/ model_store/
COPY ai_models/ ai_models/
COPY output/ output/
COPY .env .env

CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]