from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)