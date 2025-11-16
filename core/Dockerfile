FROM python:3.15.0a1-slim-bookworm

RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /skydock

WORKDIR /skydock

COPY launch.sh /skydock/
RUN chmod +x /skydock/launch.sh
CMD ./launch.sh