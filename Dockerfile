FROM python:3.13.6-slim

RUN apt-get update && \
    apt-cache madison git | awk 'END {print $3}' | xargs -i apt-get install -y --no-install-recommends git={} && \
    rm -rf /var/lib/apt/lists/*

COPY main.py requirements.txt /

## Install requirements to not need to install them on runtime:
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r /requirements.txt

CMD ["python3", "/main.py"]
