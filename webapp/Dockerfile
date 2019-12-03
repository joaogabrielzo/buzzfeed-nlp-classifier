FROM python:3.6-alpine

RUN apk add --no-cache --update python3-dev  gcc build-base

RUN apk add --no-cache libffi-dev openssl-dev

RUN apk add --no-cache openblas-dev

RUN apk add --update bash

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

RUN pip install numpy

RUN pip install --no-cache-dir scipy==1.3

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD ["python", "NLP Classifier.py"]