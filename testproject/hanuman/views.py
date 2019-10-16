from django.shortcuts import render

from django.views import generic

from django.utils import timezone

from django.http import HttpResponse


# Create your views here.

from .models import Programmer


#class IndexView(generic.ListView):

def index(request):
	print('Hanu - Index')


	#return HttpResponse("Hello World ! You are at the Hanuman index page.")


	latest_programmer_list = Programmer.objects.order_by('-pub_date')[:5]
	
	print(latest_programmer_list)

	
	ctx = {'latest_programmer_list': latest_programmer_list,}
	
	output = render(request, 'hanuman/index.html', ctx)

	#output = 'output'
	return HttpResponse(output)

