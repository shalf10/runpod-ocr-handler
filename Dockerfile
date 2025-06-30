FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# Instalar dependências para compilar sentencepiece
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
