# -*- coding: utf-8 -*-


"""eazyliner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    dj  https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from data_rest.views import clients


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    #url(r'^clients/$', clients),

    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='web_home'),

    url(r'^', TemplateView.as_view(template_name='index.html'), name='web_home'),

    #url(r'^polymer_app', TemplateView.as_view(template_name='polymer_app/index.html'), name='polymer_app_index'),
]


