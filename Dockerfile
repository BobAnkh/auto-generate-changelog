FROM python:3.9.5-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends git=1:2.20.1-2+deb10u3 && \
    rm -rf /var/lib/apt/lists/*

COPY main.py entrypoint.sh requirements.txt /
RUN chmod +x /entrypoint.sh /main.py
ENTRYPOINT ["/entrypoint.sh"]
