# QUEUE API
Queue API is a application can simulate a queue.

## Getting Started
### Pre Requisites
First of all you need to installing the pre requisites modules and frameworks of application:
- [Django Framework](https://www.djangoproject.com/download/)
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/#installation)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Installing
To install it´s simple, first create a venv ambient
```
python -m venv Venv
```
After that install the packages needed
```
pip install Django
```
```
pip install -U drf-yasg
```
```
pip install djangorestframework
```
```
pip install python-dotenv
```
And for the last installation package, if the django project warns you that you need ``psycopg2`` module just run
```
pip install psycopg2-binary
```

And that´s it, now your project have all the packages that needs

## Setup Database
The base of project have PostgreSQL Database, so to create the database you need to access the PSQL shell and just use the command:
```
CREATE DATABASE my_db;
```
and for `.env` file just follow this example
```js
SECRET_KEY=djangokey
DB_NAME=name
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```
Now your database is setup!

## Start Project
After all application is configured just start the project with 
```
python manage.py runserver
```
use the command on the root of project

## Built With
- [Python 3.11.9](https://www.python.org/downloads/)
- [Django Framework](https://www.djangoproject.com/download/)
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/#installation)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html)

## Authors
- Juan Trindade 🖥️
