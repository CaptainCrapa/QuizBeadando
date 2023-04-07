# QuizBeadando
Beadandó csoportos feladat. EKKE

# Back-end Part

## Requirements:

    Python version: 3.8.1
    Pip version: 23.0.1
    MySQL workbench version: 8.0

## Installation:
Install the belown steps, if you haven't any of the packages listed below or you
use the back-end application for the first time:
    
    pip install django
    pip install django-ninja
    pip install pymysql
    pip install wheel
    pip install mysqlclient
    pip install cryptography

## Setup:
Use these steps before start the back-end application for test:

    Make the afp2 folder as Source Root for Pycharm
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver HOST:PORT

## Swagger API Documentation

API documentations for end points are available at:

$BASE_URL/api/docs