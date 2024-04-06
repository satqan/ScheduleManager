FROM python:3.10-slim

WORKDIR /core

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev gcc

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY ./core /core/