ARG PYTHON_VERSION=3.6

FROM python:${PYTHON_VERSION}

LABEL maintainer "rusnichkin@gmail.com"

WORKDIR /tmp/app

COPY requirements.txt requirements.txt

RUN virtualenv --python=python3 /tmp/venv && \
    . /tmp/venv/bin/activate && \
    pip install -r requirements.txt