FROM ubuntu:16.04

MAINTAINER I Gusti Bagus A

ADD ./src
ADD ./requirements.txt /

RUN apt -y update &&\
    apt -y install python3 python3-pip &&\
    python3 -m pip install --upgrade pip &&\
    python3 -m pip install -r requirements.txt

CMD [ "uvicorn", "src.main:app", "--port 8000" ]
