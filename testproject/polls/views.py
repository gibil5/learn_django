
#from django.template import loader, RequestContext

from django.http import HttpResponse, Http404


from django.shortcuts import render, get_object_or_404


from .models import Question


#from django.template.loader import render_to_string



# Create your views here.


def index(request):
	print()
	print('Polls - Index')

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	print(latest_question_list)


	#template = loader.get_template('polls/index.html')
	#print(template)
	#print()
	#context = RequestContext(request, {'latest_question_list':	latest_question_list,})
	#print(context)
	#print()
	#output = render_to_string('polls/index.html', ctx)
	#output = ', '.join([p.question_text for p in latest_question_list])
	#print(output)

	#return HttpResponse("Hello World ! You are at the polls index page.")
	#return HttpResponse(template.render(context))


	ctx = {'latest_question_list': latest_question_list,}
	output = render(request, 'polls/index.html', ctx)
	return HttpResponse(output)




def detail(request, question_id):

	#return HttpResponse('This the detail view of the question: %s ' % question_id)

	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#else:
	#	ctx = {'question': question,}
	#	return	render(request, 'polls/detail.html', ctx)
	

	# Shortcut !
	question = get_object_or_404(Question, pk=question_id)

	ctx = {'question': question,}
	return	render(request, 'polls/detail.html', ctx)






def results(request, question_id):
	return HttpResponse('This the results of the question: %s ' % question_id)





def vote(request, question_id):
	return HttpResponse('Vote on question: %s ' % question_id)

