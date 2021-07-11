from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):

	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	return render(request, 'home_page/index.html', context)
	

def portfolio(request):

	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	return render(request, 'home_page/portfolio.html', context)


def resume(request):
	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	return render(request, 'home_page/resume.html', context)


def blog(request):
	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	return render(request, 'home_page/blog-home.html', context)


def contact(request):
	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	return render(request, 'home_page/contact.html', context)
	