FROM ubuntu:18.04

EXPOSE 8080


RUN apt-get update && apt-get install -y python-pip python-dev git zlib1g-dev libjpeg-dev libffi-dev telnet curl vim
RUN pip install --upgrade falcon gunicorn redis bcrypt rethinkdb falcon-multipart pillow amqplib requests elasticsearch

RUN mkdir /code
COPY . /code/
WORKDIR /code
CMD gunicorn app:api -b 0.0.0.0:8080
