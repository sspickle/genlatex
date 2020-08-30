FROM python:3.8-buster

RUN apt-get update 

RUN apt-get install -qy emacs-nox

RUN pip install -U pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD [bash]
