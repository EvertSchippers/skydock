FROM python:3.15.0a1-slim-bookworm

RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /repo

WORKDIR /repo

COPY loop.sh /repo/
RUN chmod +x /repo/loop.sh
CMD ./loop.sh