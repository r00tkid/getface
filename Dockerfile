FROM python:3.7.1
MAINTAINER Polshchyn Kyrylo <abnormally.dev@gmail.com>

ENV PYTHONUNBUFFERED 1
ADD . /var/www/get-face

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get -y install gcc nodejs npm libxml2-dev libxslt1-dev libxslt-dev \
                                          python-lxml pgloader build-essential git openssh-server
RUN pip install lxml gevent psycopg2-binary gunicorn

# SSH preparations
RUN mkdir -p /home/root/.ssh && chmod 0700 /home/root/.ssh
COPY ./project/get-face.key /home/root/.ssh/id_rsa
COPY ./project/get-face.pub /home/root/.ssh/id_rsa.pub
RUN chmod 0600 /home/root/.ssh/id_rsa && chmod 0600 /home/root/.ssh/id_rsa.pub
RUN echo "IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config
RUN ssh-keyscan bitbucket.org > /home/root/.ssh/known_hosts

WORKDIR /var/www/get-face/project
RUN pip install -r requirements.txt

WORKDIR /var/www/get-face/project/assets
RUN npm i && npm run build

WORKDIR /var/www/get-face
RUN ./django collectstatic --noinput

EXPOSE 8090