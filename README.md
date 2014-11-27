SADI-Galaxy-Docker
==================

Docker image for executing SADI services in a Galaxy server

Copy from SADI-CLI-Docker readme

Run galaxy 

/home/mikel/UPV-EHU/SADI-Galaxy-Docker/galaxy-dist-2/./run.sh

PORT!!!!! -p



















About
-----

[SADI](http://sadiframework.org/content/about-sadi/) is a framework to define Semantic Web Services that consume and output RDF, making it very light. On the other hand, [Docker](https://www.docker.com/whatisdocker/) is a sort of "virtualisation" environment for deploying applications very easily, without configuration. So I have created a Docker image for testing SADI services through the command line.   

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

```
$ docker run -t -i mikeleganaaranguren/sadi-bash:v1 /bin/bash
```

Within the container, change to the directory and see what's inside:

```
root@xxxxxxxxxxx:/# cd SADI-CLI-Docker/
root@xxxxxxxxxxx:/SADI-CLI-Docker# ls
LICENSE  README.md  hello_input.rdf  sadi_generic_client.jar  test_hello_output.rdf  test_hello_sadi_service.sh
```

Have a look into the input RDF: 

```
root@xxxxxxxxxxx:/SADI-CLI-Docker#less hello_input.rdf

<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:j.0="http://xmlns.com/foaf/0.1/"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" > 
  <rdf:Description rdf:about="http://example.com/guy">
    <j.0:name>Guy Incognito</j.0:name>
  </rdf:Description>
</rdf:RDF>

```

So the input RDF contains one triple, `http://example.com/guy foaf:name "Guy Incognito"`. To submit it to the service http://sadiframework.org/examples/hello:

```
root@xxxxxxxxxxx:/SADI-CLI-Docker# sh test_hello_sadi_service.sh
```
The shell script only contains the following line: `java -jar sadi_generic_client.jar http://sadiframework.org/examples/hello hello_input.rdf`. The SADI client outputs some logging and warning info (ignore safely):

```
SLF4J: The requested version 1.6 by your slf4j binding is not compatible with [1.5.5, 1.5.6, 1.5.7, 1.5.8]
SLF4J: See http://www.slf4j.org/codes.html#version_mismatch for further details.
 WARN [main] (RDFDefaultErrorHandler.java:36) - http://sadiframework.org/examples/hello(line 2 column 48): {W119} A processing instruction is in RDF content. No processing was done. 
``` 
 
And the output RDF should resemble something like this: 

```
<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:hello="http://sadiframework.org/examples/hello.owl#" > 
  <rdf:Description rdf:about="http://example.com/guy">
    <hello:greeting rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Hello, Guy Incognito!</hello:greeting>
    <rdf:type rdf:resource="http://sadiframework.org/examples/hello.owl#GreetedIndividual"/>
  </rdf:Description>
</rdf:RDF>
```
The SADI service has added a further triple to http://example.com/guy, `hello:greeting "Hello, Guy Incognito!"`. To run a different service simply change the service URL and the RDF input.
