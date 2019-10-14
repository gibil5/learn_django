from django.test import TestCase

from .models import Question

import datetime

from django.utils import timezone


# Create your tests here.


class QuestionMethodTest(TestCase):


	def test_was_published_recently_with_future_question(self):

		time = timezone.now() + datetime.timedelta(days=30)

		future_question = Question(pub_date=time)

		self.assertEqual(future_question.was_published_in_the_last_7_days(), False)



	def test_was_published_recently_with_recent_question(self):

		time = timezone.now() - datetime.timedelta(hours=1)

		recent_question = Question(pub_date=time)

		self.assertEqual(recent_question.was_published_in_the_last_7_days(), True)
