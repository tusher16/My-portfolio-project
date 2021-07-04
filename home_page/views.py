from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home_page/index.html')
	

def portfolio(request):
	return render(request, 'home_page/portfolio.html')


def resume(request):
	return render(request, 'home_page/resume.html')


def blog(request):
	return render(request, 'home_page/blog-home.html')


def contact(request):
	return render(request, 'home_page/contact.html')
	