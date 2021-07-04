from django.urls import path

from . import views

urlpatterns = [
	path('home/', views.index, name='index'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('resume/', views.resume, name='resume'),
	path('blog/', views.blog, name='blog'),
	path('contact/', views.contact, name='contact'),
]