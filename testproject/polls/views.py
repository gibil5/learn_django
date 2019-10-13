"""
	Polls - Views

	Created on: 	11 Oct 2019

	Last up: 		11 Oct 2019

	Important:
		- Try for exceptions.
		- Use shortcuts.
"""

from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse, Http404


from django.http import HttpResponseRedirect

#from django.core.urlresolvers import reverse
from django.urls import reverse


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

	question = get_object_or_404(Question, pk=question_id)  		# Shortcut !

	ctx = {'question': question,}
	return	render(request, 'polls/results.html', ctx)




def vote(request, question_id):
	print()
	print('Polls - Vote')


	p = get_object_or_404(Question, pk=question_id)  		# Shortcut !


	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice']) 


	except (KeyError, Choice.DoesNotExist):
		context = {
					'question': p,
					'error_message': 'You didnt select a choice yet !',
		}
		return render(request, 'polls/detail.html', context)
	

	else:

		selected_choice.votes += 1

		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
	







