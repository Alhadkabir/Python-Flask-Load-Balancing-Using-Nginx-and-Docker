FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 main:app