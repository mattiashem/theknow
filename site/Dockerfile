FROM ubuntu:18.04

EXPOSE 8080


RUN apt-get update && apt-get install -y python-pip python-dev git zlib1g-dev libjpeg-dev libffi-dev telnet curl vim
RUN pip install --upgrade f

RUN mkdir /code
RUN mkdir /files
COPY . /code/
RUN chmod 777 /code/run.sh
WORKDIR /code
RUN pip install -r requirements.txt



CMD /code/run.sh