from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home/', views.index, name='index'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('research_papers/', views.research_papers, name='research_papers'),
	path('resume/', views.resume, name='resume'),
	path('blog/', views.blog, name='blog'),
	path('contact/', views.contact, name='contact'),
]