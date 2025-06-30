FROM runpod/serverless:3.10-pytorch-2.1.0-cuda12.1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
