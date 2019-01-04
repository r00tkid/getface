FROM python:3.7.1
MAINTAINER Polshchyn Kyrylo <abnormally.dev@gmail.com>

ENV PYTHONUNBUFFERED 1
ADD . /var/www/get-face
EXPOSE 8090

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get -y install gcc nodejs npm libxml2-dev libxslt1-dev libxslt-dev python-lxml pgloader build-essential
RUN pip install lxml gevent psycopg2-binary gunicorn

WORKDIR /var/www/get-face/project
RUN pip install -r requirements.txt

WORKDIR /var/www/get-face/project/assets
RUN npm i && npm run build

WORKDIR /var/www/get-face
RUN ./django collectstatic --noinput
RUN echo "IdentityFile ./project/get-face.key" >> /etc/ssh/ssh_config
