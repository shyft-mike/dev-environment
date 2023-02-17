FROM python:3.7

WORKDIR /opt/app

COPY requirements .

RUN python -m pip install -r requirements

COPY .vscode /opt/app/.vscode

COPY --chown=python:python docker-entrypoint.sh .
