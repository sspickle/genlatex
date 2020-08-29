FROM python:3.8-buster

RUN apt-get update 

RUN pip install -U pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

RUN apt-get install -qy emacs-nox

COPY . /app

CMD [bash]
