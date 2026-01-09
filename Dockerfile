FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    libgeos-dev 

WORKDIR /api 
COPY requirements.txt /api/
RUN pip install --no-cache-dir -r requirements.txt  
