FROM continuumio/miniconda3
MAINTAINER Polshchyn Kyrylo <abnormally.dev@gmail.com>
ENV PYTHONUNBUFFERED 1
ADD ./project/requirements.txt /var/www/get-face/project/requirements.txt
ADD ./project/get-face.key /var/www/get-face/project/get-face.key
ADD ./project/get-face.pub /var/www/get-face/project/get-face.pub
RUN apt-get update && apt-get -y install gcc curl
WORKDIR /var/www/get-face/project
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda
RUN ["conda", "create", "-n", "get_face", "python=3.7.3"]
RUN echo "source activate get_face" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH
RUN /bin/bash -c "source activate get_face && pip install -r requirements.txt"
RUN ["conda", "install", "gunicorn", "django", "psycopg2"]
# RUN pip install --upgrade pip
# RUN ["pip", "install", "django-configurations"]
# RUN pip install django-configurations
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
WORKDIR /
#RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get update && apt-get -y install gcc node-gyp nodejs npm libxml2-dev libxslt1-dev libxslt-dev fortune-mod cowsay \
                                         python-lxml pgloader build-essential git openssh-server nano python3-psycopg2


# RUN pip install lxml tornado psycopg2-binary inotify gunicorn
RUN /bin/bash -c "source activate get_face && pip install lxml tornado psycopg2-binary inotify"
# SSH preparations
# RUN mkdir -p ~/.ssh && chmod 0700 ~/.ssh
COPY ./project/get-face.key /root/.ssh/id_rsa
COPY ./project/get-face.pub /root/.ssh/id_rsa.pub
RUN chmod 0600 ~/.ssh/id_rsa && chmod 0600 ~/.ssh/id_rsa.pub
RUN echo "    IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config

# RUN ssh-keyscan -t rsa bitbucket.org > /root/.ssh/known_hosts
# RUN ssh-agent bash -c "ssh-add ~/.ssh/id_rsa"
RUN git config --global user.name "GetFace"
RUN git config --global user.email "getface.development@gmail.com"

# RUN git clone ssh://git@born2fish.ru:11986/home/git/getface.git
WORKDIR /var/www/get-face
RUN git clone https://r00tkid:AsderQwerty12@github.com/r00tkid/getface.git
# ADD .git/ /var/www/get-face/.git/
# RUN git config core.filemode false

EXPOSE 8091
EXPOSE 8000
# WORKDIR /var/www/get-face/getface/
# RUN /bin/bash -c "source activate get_face"
CMD exec gunicorn --bind 0.0.0.0:8000 app.wsgi:get_face --timeout 30 --graceful-timeout 20

# CMD exec gunicorn --pythonpath=/home/shaman/miniconda3/envs/get_face/bin/ app.wsgi:get_face --timeout 30 --bind 0.0.0.0:8000 --chdir /home/shaman/workspace/get-face/
# CMD exec gunicorn --pythonpath=./ --bind 0.0.0.0:8091 app.wsgi:get_face
# CMD exec gunicorn /home/shaman/workspace/get-face/app.wsgi:get_face --timeout 30 --bind 0.0.0.0:8000 --reload --chdir /home/shaman/workspace/get-face/
# gunicorn app.wsgi:get_face -c /var/www/get-face/index/gunicorn.py --timeout 30 --graceful-timeout 20
# ENTRYPOINT ["django"]
