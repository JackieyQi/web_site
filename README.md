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

Into container, initialize db and configuration

>`$ docker exec -it container_web_id /bin/bash`

>`$ python manage migrate`

>`$ python manage makemigration`

>`$ python manage createsuperuser`


# Database Commands
Run MySQL container in local development environment:
>`$ docker run -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=secret -d mysql:5.7`

Import data to MySQL database in Docker:
>`$ docker exec -i mysql_container mysql -uroot -psecret mysql < db.sql`


# Code Style
To maintain the code consistency, this project uses following tools.

* **[flake8](https://github.com/PyCQA/flake8)**
* **[isort](https://github.com/timothycrosley/isort)**
* **[black](https://github.com/python/black)**


# More
Google site verification:

Http ssl certificate:

Get free ssl/tls certificates by Acme. 
Here are some commands after acme scripts installed.

> acme.sh --issue --domain website.com --standalone -k ec-256

> acme.sh --installcert -d website.com --keypath ./nginx/website.key --fullchainpath ./nginx/website.crt --ecc

