# ubuntu:20.04
FROM ubuntu:focal
#FROM python:3.12

ENV PYTHONUNBUFFERED 1

# install python 3.12
#RUN apt update && apt install software-properties-common -y

RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update -y
RUN apt install python3.12 -y
RUN apt install python3-pip -y

# Create a folder named 'app' inside docker container:
RUN mkdir /app
COPY ./app /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN apt update && apt install wget unzip -y && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt clean

#CMD ["python", "main.py"]