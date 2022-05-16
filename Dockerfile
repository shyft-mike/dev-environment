FROM python:3.7

WORKDIR /root/dev

COPY python/requirements .

RUN python -m pip install -r requirements
