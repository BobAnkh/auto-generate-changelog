FROM python:3.7.8-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends git

COPY main.py entrypoint.sh requirements.txt /
RUN chmod +x /entrypoint.sh
RUN chmod +x /main.py
ENTRYPOINT ["/entrypoint.sh"]
