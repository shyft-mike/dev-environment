FROM python:3.7

WORKDIR /app

COPY requirements .

RUN python -m pip install -r requirements
