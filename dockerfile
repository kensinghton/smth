FROM ubuntu

LABEL vendor1="me"
LABEL vendor2="not me"


RUN apt-get update && apt-get -y install wget lsb-release apt-transport-https debconf
RUN wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
RUN apt-get -y install mysql-common libjemalloc1 libaio1 libmecab2
RUN dpkg -i percona-release_latest*.deb || true 
RUN percona-release setup ps80
#RUN apt-get update 
RUN echo "percona-server-server-8.0 percona-server-server/root_password password root" | debconf-set-selections
RUN echo "percona-server-server-8.0 percona-server-server/root_password_again password root" | debconf-set-selections
RUN apt-get -qq -y install percona-server-server

EXPOSE 3306
