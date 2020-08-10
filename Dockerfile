FROM python:3.7.8-slim

RUN apt-get install -y --no-install-recommends git=2.28.0

COPY main.py entrypoint.sh requirements.txt /
RUN chmod +x /entrypoint.sh
RUN chmod +x /main.py
ENTRYPOINT ["/entrypoint.sh"]
