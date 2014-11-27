# Docker file to run a Galaxy instance preconfigured with SADI-Galaxy and fake user (user useruser) that can run pre-canned history and workflow

FROM ubuntu:14.04
MAINTAINER Mikel Egaña Aranguren <mikel.egana.aranguren@gmail.com>

# Install the necessary stuff 

RUN apt-get update && apt-get install -y git wget vim python python-rdflib raptor2-utils libraptor2-0

# Java is installed from http://www.duinsoft.nl/packages.php?t=en

RUN wget http://www.duinsoft.nl/pkg/pool/all/update-sun-jre.bin
RUN sh update-sun-jre.bin



