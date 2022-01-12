FROM alpine:latest

USER root

WORKDIR /

COPY ./config.yaml ./

RUN apk --update add wget && \
	wget https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/download/v0.42.0/otelcontribcol_linux_amd64 && \
	chmod +x otelcontribcol_linux_amd64 

ENTRYPOINT ["/otelcontribcol_linux_amd64"]
CMD ["--config", "/config.yaml"]

