FROM python:3.7-alpine

RUN apk add --no-cache --update python3-dev  gcc build-base

RUN apk add --no-cache libffi-dev openssl-dev

RUN apk add --update bash

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000

RUN python "NLP Classifier.py"