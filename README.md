# Blog web site by Django frame
A simple blog by Python3.7, django, nginx, uwsgi, docker.

host:port

admin uri: host:port/admin


# Start server
Configuration:
>common config: myweb/config/general.ini
>
>nginx config: myweb/nginx/myweb.conf
>
>docker config: Dockerfile, docker-compose.yml

Development environment:
>python manage.py runserver host:port

Production environment:
>`$ docker-compose up`

>into container, initialize db and configuration

>`$ docker exec -it container_web_id /bin/bash`

>`$ python manage migrate`

>`$ python manage makemigration`

>`$ python manage createsuperuser`


# More
Google site verification:

Http ssl certificate:

Get free ssl/tls certificates by Acme. 
Here are some commands after acme scripts installed.

> acme.sh --issue --domain website.com --standalone -k ec-256

> acme.sh --installcert -d website.com --keypath ./nginx/website.key --fullchainpath ./nginx/website.crt --ecc

