FROM python:3.7

WORKDIR /app

COPY jupyter_lab_config.py /config/
COPY requirements .
COPY start_jupyter.sh .
COPY start_streamlit.sh .

RUN python -m pip install -r requirements
