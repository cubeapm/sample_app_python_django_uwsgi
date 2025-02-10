FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /django

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uwsgi", "--http", ":8000", "--module", "sample_app.wsgi:application", "--master", "-p", "4", "--enable-threads", "--need-app"]
