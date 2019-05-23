~/cs101/public/lesson009/readme.txt

This file describes my walkthrough of a docker tutorial.

part-1: GCP Kubernetes Create Cluster of 1 Node

Q: Why use GCP Kubernetes node to operate Docker?
A: A GCP Kubernetes node comes with Docker installed; I avoid the chore of Docker installation.

I started by asking GCP to create a VM with Docker installed for me.

I did this by creating a kubernetes cluster of 1 host.

I started at this URL:

https://console.cloud.google.com/kubernetes

I clicked blue-button: "Create Cluster"

I made small changes to the form it served me:
  Ubuntu instead of "cos"
  Size 1 instead of 3

It quickly created 1-node-cluster.

After GCP created the node, I found it listed in this URL:

https://console.cloud.google.com/compute/instances


part-2: Run /bin/bash in new Docker Containers

I started by visiting this URL:

https://console.cloud.google.com/compute/instances

I found the node I created in part-1.

I clicked the SSH link to gain shell access to the node.

I entered a shell command:

sudo docker run -it ubuntu:16.04 /bin/bash

After a bit of work, Docker served me a shell prompt from a newly hatched container.

I entered a shell command:

cat /etc/lsb-release

I saw this:

root@08bfb05c6ca3:/etc# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.4 LTS"
root@08bfb05c6ca3:/etc#

I typed exit to exit the container.

I was now back inside a shell of the cluster node.

So, that was a simple demo of creating a new Docker container and then running /bin/bash inside it.

Here is a another similar demo.

I ran another Docker shell command to bring up another container with Anaconda Python in it:

sudo docker run -it continuumio/anaconda3 /bin/bash

After a bit of work, Docker served me a shell prompt from a newly hatched container.

I entered a shell command:

python

It served me a Python-3 prompt.

I entered Python commands:

import pandas as pd
from sklearn.datasets import load_boston
bos_df = pd.DataFrame(load_boston().data)
bos_df.columns = load_boston().feature_names
bos_df.describe()

The above commands worked well.

So, I could quickly gain access to a container running Anaconda Python.

I exited Python using the quit() command.

I exited the container with the shell command: "exit".

I ran another Docker shell command to bring up another container with Anaconda Python in it:

sudo docker run -it continuumio/anaconda3 /bin/bash

Instantly, Docker served me a shell prompt from a newly hatched container.

I entered a shell command:

python

Instantly, I saw a Python prompt.

I exited Python using the quit() command.

I exited the container with the shell command: "exit".



part-3 Docker build an image

So, the initial creation of the container was slow because Docker needed to pull an "image" from the net.

But, after the image was cached locally, I could access it instantly.

So, those last two lessons showed how to create a container from an image and then run /bin/bash in the container.

A main idea to remember about Docker is that I can get one or more containers from an image.

Once I have a container, I can boot it up and then use it to support shell commands.

I reviewed the two docker commands I ran above to create containers:

sudo docker run -it ubuntu:16.04 /bin/bash
sudo docker run -it continuumio/anaconda3 /bin/bash

Both of the above commands depended on images that had been built for me by other people.

Both of the images are stored on hub.docker.com:

https://hub.docker.com/_/ubuntu/
https://hub.docker.com/r/continuumio/anaconda3/

Q: How do I create an image?
A: I create a file: "Dockerfile", then I use the "docker build" command to create an image.

I followed the above information and wrote some notes.

On the cluster-node, I entered some shell commands to create an image of my own:

mkdir /dock1804
cd    /dock1804
echo From ubuntu:18.04 > Dockerfile
sudo docker build -t dock1804 .
sudo docker run  -it dock1804 /bin/bash

That worked well.

Next, I copied Dockerfile into a github repo.
I connected that repo to the bikle101 account in 
https://cloud.docker.com/
I asked the site to build.

Next I ran this shell command:

docker run -it bikle101/dock1804 /bin/bash

It worked great!

An alternative would be to clone the repo and cd into its folder.

Then type:
sudo docker build -t dock1804 .
sudo docker run  -it dock1804 /bin/bash

Here is a screen shot of me doing that:


dan@p95:~ $ 
dan@p95:~ $ cd ~
dan@p95:~ $ git clone https://github.com/danbikle/dock1804
Cloning into 'dock1804'...
remote: Counting objects: 3, done.        
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0        
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
dan@p95:~ $ 
dan@p95:~ $ 
dan@p95:~ $ cd dock1804/
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ ll
total 16
drwxrwxr-x  3 dan dan 4096 Mar 19 16:01 ./
drwxr-xr-x 53 dan dan 4096 Mar 19 16:01 ../
-rw-rw-r--  1 dan dan   18 Mar 19 16:01 Dockerfile
drwxrwxr-x  8 dan dan 4096 Mar 19 16:01 .git/
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ sudo docker build -t dock1804 .
[sudo] password for dan: 
Sending build context to Docker daemon  48.13kB
Step 1/1 : From ubuntu:18.04
18.04: Pulling from library/ubuntu
Digest: sha256:4decfd6e336e1cf246127151753d2a24a3185b5f667b91b925e8b38e7ea903a0
Status: Downloaded newer image for ubuntu:18.04
 ---> 02f9d6707661
Successfully built 02f9d6707661
Successfully tagged dock1804:latest
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ sudo docker run  -it dock1804 /bin/bash
]0;root@ae6cfbed0a9b: /root@ae6cfbed0a9b:/# 

]0;root@ae6cfbed0a9b: /root@ae6cfbed0a9b:/# cat /etc/lsb-release
cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu Bionic Beaver (development branch)"
]0;root@ae6cfbed0a9b: /root@ae6cfbed0a9b:/# 

]0;root@ae6cfbed0a9b: /root@ae6cfbed0a9b:/# exit
exit
exit
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ 
dan@p95:~/dock1804 $ 



Next, I exited the node-shell.

Finally I deleted the 1-node-cluster from a link in this URL:

https://console.cloud.google.com/kubernetes

