from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage

from .models import *

def index(request):

	My_profile_nav_object = My_profile_nav.objects.all()
	My_profile_home_object = My_profile_home.objects.all()
	test_list = testiomonial.objects.all()

	My_research_object = My_researche.objects.all().filter(Featured=1)[:3]
	My_portfolio_object = My_portfolio.objects.all().filter(Featured=1)[:4]
	My_blog_object = My_blog.objects.all().filter(Featured=1)[:3]


	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_profile_home_object': My_profile_home_object,
		'test_list': test_list,

		'My_research_object': My_research_object,
		'My_portfolio_object': My_portfolio_object,
		'My_blog_object' : My_blog_object,
	}

	return render(request, 'home_page/index.html', context)
	

def research_papers(request):

	My_profile_nav_object = My_profile_nav.objects.all()
	My_research_object = My_researche.objects.all()

	p = Paginator(My_research_object, 6)
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)


	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_research_object': page,
	}

	return render(request, 'home_page/research_papers.html', context)

def portfolio(request):

	My_profile_nav_object = My_profile_nav.objects.all()
	My_portfolio_object = My_portfolio.objects.all()

	p = Paginator(My_portfolio_object, 6)
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_portfolio_object': page,
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
	My_blog_object = My_blog.objects.all()

	p = Paginator(My_blog_object, 6)
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_blog_object': page,
	}

	return render(request, 'home_page/blog-home.html', context)


def contact(request):
	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	if request.method=="POST":
		contact = Contact()
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		contact.con_name = name
		contact.con_email = email
		contact.con_message = message
		contact.save()
		
		return render(request, 'home_page/contact_thank.html', context)
	

	

	return render(request, 'home_page/contact.html', context)
	