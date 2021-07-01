FROM python:3.8-alpine

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
COPY ./auth /app

CMD python manage.py runserver 0.0.0.0:8000