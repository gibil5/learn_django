
from django.db import models

from django.utils import timezone

import datetime



# Create your models here.

class Programmer(models.Model):

	programmer_text = models.CharField(max_length=200)

	pub_date = models.DateTimeField('date published')




	profession = models.CharField(
		max_length=200,
		default='x',
		)

	skills = models.CharField(
		max_length=200,
		default='',
		)

	education = models.CharField(
		max_length=200,
		default='',
		)




	def __str__(self): 

		return self.programmer_text
