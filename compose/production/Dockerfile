FROM python:3.8-alpine

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements /app/requirements

RUN pip install -r requirements/production.txt
COPY ./auth /app

CMD /usr/local/bin/gunicorn auth.wsgi --bind 0.0.0.0:5000 --chdir=/app