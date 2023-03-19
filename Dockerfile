FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        portaudio19-dev \
        libsndfile1 \
        libasound2-dev

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
