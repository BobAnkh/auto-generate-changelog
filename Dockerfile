FROM python:3.10.5-slim

RUN apt-get update && \
    apt-cache madison git | awk '{print $3}'| xargs -i apt-get install -y --no-install-recommends git={} && \
    rm -rf /var/lib/apt/lists/*

COPY main.py entrypoint.sh requirements.txt /
RUN chmod +x /entrypoint.sh /main.py
ENTRYPOINT ["/entrypoint.sh"]
