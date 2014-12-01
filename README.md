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

Pull the [image](https://registry.hub.docker.com/u/mikeleganaaranguren/sadi-galaxy):

```
$ docker pull mikeleganaaranguren/sadi-galaxy
```

Check that it has been pulled (KRAKEN!!!):

```
$  docker images

REPOSITORY                      TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
mikeleganaaranguren/sadi-bash   v1                  xxxxxxxxxxx        17 hours ago        547 MB
```

Run the container:

```
$ docker run -d -p 8080:8080 mikeleganaaranguren/sadi-galaxy
```

If you go to http://127.0.0.1:8080 there should be a Galaxy server runing (SCREENSHOT!!!). Login (user:`user@user.com`, passwd:`useruser`) and a history should appear (SCREENSHOT!!!).







