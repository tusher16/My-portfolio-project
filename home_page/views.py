from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home_page/index.html')
	# remove this line #return HttpResponse("hello. this is test request")


