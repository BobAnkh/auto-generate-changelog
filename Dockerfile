FROM python:3.7.8-slim

COPY main.py entrypoint.sh requirements.txt /

ENTRYPOINT ["/entrypoint.sh"]
