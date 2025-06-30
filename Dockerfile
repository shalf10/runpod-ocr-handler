FROM runpod/pytorch:2.1.0-py3.10-cuda12.1.0-devel

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
