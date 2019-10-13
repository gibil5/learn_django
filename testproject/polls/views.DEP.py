# 12 Oct 2019

#from django.template import loader, RequestContext

#from django.template.loader import render_to_string



def index(request):

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


def detail(request, question_id):

	#return HttpResponse('This the detail view of the question: %s ' % question_id)

	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#else:
	#	ctx = {'question': question,}
	#	return	render(request, 'polls/detail.html', ctx)
	



def vote(request, question_id):
	#return HttpResponse('Vote on question: %s ' % question_id)



def results(request, question_id):
	return HttpResponse('This the results of the question: %s ' % question_id)



