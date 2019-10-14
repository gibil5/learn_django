"""
	Polls - Views

	Created on: 	11 Oct 2019

	Last up: 		11 Oct 2019

	Important:
		- Try for exceptions.
		- Use shortcuts.
"""

#from django.http import HttpResponseRedirect


from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.urls import reverse
#from django.core.urlresolvers import reverse

from .models import Question

from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'






def vote(request, question_id):
	print()
	print('Polls - Vote')


	# Get Object
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
	

