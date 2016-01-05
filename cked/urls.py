# coding: utf8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^elfinder/$', views.elfinder, name='cked_elfinder'),
    url(r'^elfinder/connector/$', views.elfinder_connector, name='cked_elfinder_connector')
]
