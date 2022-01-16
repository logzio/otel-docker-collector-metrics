FROM python:3.9-slim

USER root

WORKDIR /

COPY config.yaml ./
COPY requirements.txt ./
COPY app.py ./


RUN apt-get update && \
	apt-get install -y wget && \
	wget https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.42.0/otelcontribcol_linux_amd64 && \
	chmod +x otelcontribcol_linux_amd64 

RUN mv otelcontribcol_linux_amd64 otelcontribcol

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]

