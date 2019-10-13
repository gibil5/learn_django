"""
	Polls - Views

	Created on: 	11 Oct 2019

	Last up: 		11 Oct 2019

	Important:
		- Try for exceptions.
		- Use shortcuts.
"""

from django.http import HttpResponse, Http404

from django.shortcuts import render, get_object_or_404

from .models import Question



# Create your views here.

def index(request):
	print()
	print('Polls - Index')

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	print(latest_question_list)

	ctx = {'latest_question_list': latest_question_list,}
	output = render(request, 'polls/index.html', ctx)

	return HttpResponse(output)




def detail(request, question_id):
	print()
	print('Polls - Detail')


	question = get_object_or_404(Question, pk=question_id)  		# Shortcut !


	ctx = {'question': question,}
	return	render(request, 'polls/detail.html', ctx)







def results(request, question_id):
	print()
	print('Polls - Results')
	return HttpResponse('This the results of the question: %s ' % question_id)

def vote(request, question_id):
	print()
	print('Polls - Vote')
	return HttpResponse('Vote on question: %s ' % question_id)

