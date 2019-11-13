### flask-app [![Build Status](https://travis-ci.org/darialukash/flask-app.svg?branch=master)](https://travis-ci.org/darialukash/flask-app)

Лабораторные работы по РСОИ (распределенные системы обработки информации)

Github -> Travic CI -> Heroku

#### App:

- https://flask-app-rsoi.herokuapp.com/

#### DB API:

- https://flask-app-rsoi.herokuapp.com/database   


#### local database

- PostgreSql
```
$ psql -h localhost -U postgres
> CREATE database flaskdb;
> CREATE role program WITH password 'qwerty';
> GRANT ALL PRIVILEGES ON database flaskbd TO program;
> ALTER role program WITH login;
> /q
$ psql -h localhost -U program flaskdb
```
