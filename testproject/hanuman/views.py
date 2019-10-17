from django.shortcuts import render

from django.views import generic

from django.utils import timezone

from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404


# Create your views here.

from .models import Programmer


#class IndexView(generic.ListView):

def index(request):
	print('Hanu - Index')


	#return HttpResponse("Hello World ! You are at the Hanuman index page.")


	#latest_programmer_list = Programmer.objects.order_by('-pub_date')[:5]
	latest_programmer_list = Programmer.objects.all()
	print(latest_programmer_list)

	
	ctx = {'latest_programmer_list': latest_programmer_list,}
	
	#output = 'output'
	output = render(request, 'hanuman/index.html', ctx)
	print(output)


	return HttpResponse(output)



def detail(request, programmer_id):
	print()
	print('Hanu - Detail')


	# Get Object
	programmer = get_object_or_404(Programmer, pk=programmer_id)  		# Shortcut !

	print(programmer)


	ctx = {'programmer': programmer,}

	return	render(request, 'hanuman/detail.html', ctx)





