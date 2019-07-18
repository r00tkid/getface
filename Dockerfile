FROM python:3.7.3
MAINTAINER Polshchyn Kyrylo <abnormally.dev@gmail.com>
ENV PYTHONUNBUFFERED 1
ADD ./project/requirements.txt /var/www/get-face/project/requirements.txt
ADD ./project/get-face.key /var/www/get-face/project/get-face.key
ADD ./project/get-face.pub /var/www/get-face/project/get-face.pub

WORKDIR /var/www/get-face/project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get update && apt-get -y install gcc nodejs npm libxml2-dev libxslt1-dev libxslt-dev fortune-mod cowsay \
                                          python-lxml pgloader build-essential git openssh-server nano
RUN pip install lxml tornado psycopg2-binary inotify

# SSH preparations
RUN mkdir -p ~/.ssh && chmod 0700 ~/.ssh
COPY ./project/get-face.key /root/.ssh/id_rsa
COPY ./project/get-face.pub /root/.ssh/id_rsa.pub
RUN chmod 0600 ~/.ssh/id_rsa && chmod 0600 ~/.ssh/id_rsa.pub
RUN echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config

RUN ssh-keyscan -t rsa bitbucket.org > /root/.ssh/known_hosts
RUN ssh-agent bash -c "ssh-add ~/.ssh/id_rsa"
RUN git config --global user.name "GetFace"
RUN git config --global user.email "getface.development@gmail.com"

WORKDIR /var/www/get-face
ADD .git/ /var/www/get-face/.git/
RUN git config core.filemode false

EXPOSE 8091
WORKDIR /home/shaman/workspace/get-face/
CMD exec gunicorn --pythonpath=./ --bind 0.0.0.0:8000 app.wsgi:get_face
#CMD exec gunicorn app.wsgi:get_face --timeout 30 --bind 0.0.0.0:8000 --workers 3 --chdir /home/shaman/workspace/get-face/
#gunicorn app.wsgi:get_face -c /var/www/get-face/index/gunicorn.py --timeout 30 --graceful-timeout 20
# ENTRYPOINT ["django"]
