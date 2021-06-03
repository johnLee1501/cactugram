FROM python:3

RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /www/

