### flask-app

Лабораторные работы по РСОИ (распределенные системы обработки информации)

Github -> Travic CI -> Heroku

#### App:

- https://flask-app-rsoi.herokuapp.com/


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
