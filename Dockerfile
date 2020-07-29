FROM python:3.7.8-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY main.py entrypoint.sh requirements.txt /

ENTRYPOINT ["/entrypoint.sh"]
