from django.test import TestCase

from .models import Question

import datetime

from django.utils import timezone

from django.urls import reverse

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




# ADDED
# https://docs.djangoproject.com/en/2.2/intro/tutorial05/

def create_question(question_text, days):
	"""
	Create a question with the given `question_text` and published the
	given number of `days` offset to now (negative for questions published
	in the past, positive for questions that have yet to be published).
	"""
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)



class QuestionViewTest(TestCase):

	def test_index_view_with_no_questions(self):

		response = self.client.get(reverse('polls:index'))

		self.assertEqual(response.status_code, 200)

		self.assertContains(response, "You haven't uploaded any question yet")

		self.assertQuerysetEqual(response.context["latest_question_list"], [])



# ADDED
class QuestionIndexViewTests(TestCase):


	def test_index_view_with_a_past_question(self):
		"""
		Questions with a pub_date in the past are displayed on the
		index page.
		"""
		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
		)


	def test_index_view_with_a_future_question(self):
		"""
		Questions with a pub_date in the future aren't displayed on
		the index page.
		"""
		create_question(question_text="Future question.", days=30)
		
		response = self.client.get(reverse('polls:index'))
		
		#self.assertContains(response, "No polls are available.")
		self.assertContains(response, "You haven't uploaded any question yet")
		
		self.assertQuerysetEqual(response.context['latest_question_list'], [])





	def test_index_view_with_future_question_and_past_question(self):
		"""
		Even if both past and future questions exist, only past questions
		are displayed.
		"""
		create_question(question_text="Past question.", days=-30)
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question.>']
		)


	def test_index_view_with_two_past_questions(self):
		"""
		The questions index page may display multiple questions.
		"""
		create_question(question_text="Past question 1.", days=-30)
		create_question(question_text="Past question 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_question_list'],
			['<Question: Past question 2.>', '<Question: Past question 1.>']
		)





class QuestionIndexDetailTests(TestCase):


	def test_detail_view_with_a_past_question(self):
		"""
		Questions with a pub_date in the past are displayed on the
		index page.
		"""

		past_question = create_question(question_text="Past question.", days=-5)

		response = self.client.get(reverse('polls:detail', args=(past_question.id,)))


		self.assertContains(
			
			response,
			
			past_question.question_text, 

			status_code=200
		)






