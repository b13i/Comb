from django.conf.urls import patterns, url
from pdfocr import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))
