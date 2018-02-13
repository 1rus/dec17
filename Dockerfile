ARG PYTHON_VERSION=3.6

FROM python:${PYTHON_VERSION}

LABEL maintainer "rusnichkin@gmail.com"

WORKDIR /tmp/app

COPY requirements.txt requirements.txt

RUN python3 -m venv /tmp/venv && \
    . /tmp/venv/bin/activate && \
    pip install -r requirements.txt
