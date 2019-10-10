from django.db import models

from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):

	question_text = models.CharField(max_length=200)

	pub_date = models.DateTimeField('date published')


	def __str__(self): 

		return self.question_text


	def was_published_in_the_last_7_days(self):

		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)


	was_published_in_the_last_7_days.admin_order_field = 'pub_date'

	was_published_in_the_last_7_days.boolean = True

	was_published_in_the_last_7_days.short_description = 'Published this week ?'




class Choice(models.Model):

	choice_text = models.CharField(max_length=200)

	votes = models.IntegerField(default=0)

	question = models.ForeignKey(
			Question, 
			on_delete=models.CASCADE
		)


	def __str__(self): 

		return self.choice_text

