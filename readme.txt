
Learn Django - With Udemy
---------------------------
Oct 2019 
14


Rutter
--------
python manage.py shell 
python manage.py runserver 
python manage.py createsuperuser

http://127.0.0.1:8000
http://127.0.0.1:8000/admin


Test views
------------

from django.test.utils import setup_test_environment

setup_test_environment()

from django.test import Client

client = Client()

response = client.get('https://127.0.0.1:8000/polls/')

response.status_code

response.content
