FROM python:3.6

WORKDIR tmp\dec17

COPY requirements.txt requirements.txt

RUN python -m venv tmp\venv && \
	tmp\venv\scripts\activate.bat && \
	pip install -r requirements.txt