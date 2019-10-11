	if False:
		try:
			question = Question.objects.get(pk=question_id)

		except Question.DoesNotExist:
			raise Http404("Question does not exist")

		else:
			ctx = {'question': question,}
			return	render(request, 'polls/detail.html', ctx)
