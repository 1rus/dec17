# escape=`

ARG PYTHON_VERSION=3.6

FROM python:${PYTHON_VERSION}

LABEL maintainer "rusnichkin@gmail.com"

WORKDIR /tmp/dtest

COPY requirements.txt requirements.txt

RUN python -m venv /tmp/dtest/venv && \
    . /tmp/dtest/venv/scripts/activate && \
    pip install -r requirements.txt