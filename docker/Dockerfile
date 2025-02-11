FROM python:3.8-buster

RUN apt-get update 

RUN apt-get install -qy emacs-nox zip

RUN pip install -U pip

RUN mkdir /work

WORKDIR /work

COPY requirements.txt /work

RUN pip install -r requirements.txt

COPY . /work

RUN pip install .

RUN chmod +x *.sh

ENTRYPOINT ["/bin/bash"]

CMD ["buildTeXs.sh"]

