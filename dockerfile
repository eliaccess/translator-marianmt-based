FROM ubuntu:18.04
MAINTAINER Elias Limouni

RUN apt-get update -y && \
    apt-get install -y software-properties-common
RUN add-apt-repository universe
RUN apt-get update -y && apt-get install -y python3.7 python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "Service.py" ]