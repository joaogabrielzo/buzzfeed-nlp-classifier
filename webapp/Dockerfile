FROM python:3.6-slim

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD ["python", "NLP Classifier.py"]