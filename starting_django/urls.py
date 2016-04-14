# -*- coding: utf-8 -*-
"""starting_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from application1.views import index
from application1.views import index, detalle, categorias
admin.autodiscover() #Método de las URLS para mapear en base a la config

'''
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
'''

urlpatterns = patterns('',
    #----1ªforma
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', index),
    #---2ªforma
    (r'^index$', index),
    (r'^detalle$', detalle),
    (r'^categorias/(?P<categoria_id>\d+)/$', categorias),
    )