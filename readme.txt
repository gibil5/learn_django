
Learn Django - With Udemy
---------------------------
Oct 2019 
17


Using a Virtual Environment. 
With: 
Python 3.6.4 Anaconda Inc
Django 2.2.6
SQLite3 3.22.0





Rutter
--------


django-admin startproject testproject 

python manage.py startapp polls 

python manage.py startapp hanuman


# Modify settings.py, to include the new app
python manage.py makemigrations
python manage.py migrate 



python manage.py shell 

python manage.py runserver 

python manage.py createsuperuser

python manage.py test



http://127.0.0.1:8000
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/polls




*****************
*	PROTOCOLS
*****************


>>> from hanuman.models import Programmer
>>> all = Programmer.objects.all()
>>> p = Programmer(programmer_text="Javier Revilla", pub_date=timezone.now())
>>> p.save()
>>> p.delete()




Test views- Using the Shell
-----------------------------
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
response = client.get('https://127.0.0.1:8000/polls/')
response.status_code
response.content

