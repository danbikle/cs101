~/cs101/public/lesson008/readme.txt

This file shows some of my efforts to learn about Docker.

How I installed Docker on Ubuntu 16:

ref:
  https://docs.docker.com/install/linux/docker-ce/ubuntu/

sudo bash


apt-get remove docker docker-engine docker.io

apt-get update

apt-get install apt-transport-https ca-certificates software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   
apt-get update

apt-get install docker-ce

systemctl enable docker

docker run hello-world

usermod -aG docker bikle101

ssh bikle101@ub10

docker run hello-world


ref:
  https://docs.docker.com/get-started/

docker ps # what is docker doing now?

docker --version

docker info

docker run hello-world
docker image ls # I should see hello-world image

# image gives me many containers:
## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq

mkdir ~/dock10
cd    ~/dock10

cat>Dockerfile<<EOF
# ref:
# https://docs.docker.com/get-started/part2/#dockerfile

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

EOF

cat>requirements.txt<<EOF
Flask
Redis
EOF

"""
app.py
Ref:
https://docs.docker.com/get-started/part2/#the-app-itself
"""

from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
# end



docker build -t danhello .       # I can call it this
docker build -t friendlyhello .  # I can call it this too

docker image ls

docker run    -p 4000:80 friendlyhello
docker run -d -p 4000:80 friendlyhello # I can detach

docker ps
docker container ls
docker container ls -a

How to kill detached container?
A:
docker container stop id # partial hash ok
demo:
docker container stop 2a4

Demo of how I deployed/ran a shell script:

mkdir ~/dock12
cd    ~/dock12
cat>Dockerfile<<EOF
FROM ubuntu:16.04

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

CMD ["/bin/bash", "hello.bash"]
EOF

#hello.bash
echo hello docker

docker build -t dock12 .

That works well!

I tried this:
cd ~/dock12
docker run -i -t dock12 /bin/bash

That worked well!

I tried this:
mkdir ~/dock11
cd    ~/dock11
ref:
  https://hub.docker.com/r/continuumio/anaconda/
  https://www.google.com/search?q=what+does+docker+pull+do
docker pull continuumio/anaconda
docker run -i -t continuumio/anaconda /bin/bash

That works well!


I tried this:
mkdir ~/dock13
cd    ~/dock13
ref:
  https://hub.docker.com/r/continuumio/anaconda3/
  https://www.google.com/search?q=what+does+docker+pull+do
docker pull continuumio/anaconda3
docker run -i -t continuumio/anaconda3 /bin/bash

conda update conda
conda install keras

That works well!

This works well too:
docker run -it hello-world  /bin/bash
docker run -it ubuntu:16.04 /bin/bash




I tried this:
mkdir ~/dock14
cd    ~/dock14

cat>Dockerfile<<EOF
FROM continuumio/anaconda3

# Set the working directory to /app
WORKDIR /app
ADD . /app

RUN conda update conda
RUN conda install keras
EOF

docker build -t dock14 .

docker run -it dock14 /bin/bash

That worked well!


I tried this:

ref:
  https://hub.docker.com/r/continuumio/anaconda3/~/dockerfile/
  
mkdir ~/dock15
cd    ~/dock15

cat>Dockerfile<<EOF
FROM ubuntu:16.04

# Set the working directory to /app
WORKDIR /app
ADD . /app

RUN apt-get update --fix-missing
RUN apt-get install -y wget bzip2 ca-certificates

RUN echo 'export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' >> /root/.bashrc
RUN cd /opt && tar xf /app/conda.tar.bz2
EOF


RUN wget --quiet https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
RUN /bin/bash Anaconda3-5.1.0-Linux-x86_64.sh -b -p /opt/conda
RUN /opt/conda/bin/conda update conda -y
RUN conda install keras -y
EOF

docker build -t dock15 .

docker run -it dock15 /bin/bash

tried docker cp:

docker container ls
docker cp e6:/opt/conda/LICENSE.txt .

It worked!

experiment:
  see if I can back/restore /opt/conda from container1 to container2
  
It worked!

