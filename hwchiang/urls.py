"""hwchiang URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import include, url
# from django.contrib import admin
from django.conf.urls import url
from hwchiang import views as home_views
from hwchiang.header import views as header_views

urlpatterns = [
    # disable django default administration page
    # url(r'^admin/', include(admin.site.urls)),

    # index
    url(r'^$', home_views.home, name='home'),

    # about
    url(r'^about/$', header_views.about, name='about'),

    # resume
    url(r'^resume/$', header_views.resume, name='resume'),

    # interests
    url(r'^interests/$', header_views.interests, name='interests')
]
