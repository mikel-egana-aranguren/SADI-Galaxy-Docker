SADI-Galaxy-Docker
==================


About
-----

[SADI](http://sadiframework.org/content/about-sadi/) is a framework to define Semantic Web Services that consume and output RDF, and [SADI-Galaxy](https://github.com/mikel-egana-aranguren/SADI-Galaxy) makes SADI services available in the [Galaxy](http://galaxyproject.org/) platform. On the other hand, [Docker](http://www.docker.com/whatisdocker/) is a sort of "virtualisation" environment for deploying applications very easily, without configuration. So I have created a Docker image for deploying a Galaxy instance already containing SADI-Galaxy.   

Deploying the container
-----------------------

Install Docker and do the thingy for avoiding sudo access: 

```
$ sudo apt-get install docker.io
$ sudo groupadd docker
$ sudo gpasswd -a your_user docker
$ sudo service docker.io restart
```

(You might need to log out and back in).

Pull the [image](https://registry.hub.docker.com/u/mikeleganaaranguren/sadi-bash/):

```
$ docker pull mikeleganaaranguren/sadi-bash

```

Check that it has been pulled:

```
$  docker images


REPOSITORY                      TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
mikeleganaaranguren/sadi-bash   v1                  xxxxxxxxxxx        17 hours ago        547 MB
```

Run the container:


PORT!!!!! -p



```
$ docker run -t -i mikeleganaaranguren/sadi-bash:v1 /bin/bash
```

Within the container, run the Galaxy server:

/home/mikel/UPV-EHU/SADI-Galaxy-Docker/galaxy-dist-2/./run.sh

```
root@xxxxxxxxxxx:/# cd SADI-CLI-Docker/
```

Go to 127.0.0.1 and check, there is a user ... 

If you want to deploy this in a server, use vim to edit and change 



