"""MaidenThoughts URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^skin_care', views.skin_care_article, name='skin_care'),
	url(r'^hair_care', views.hair_care_article, name='hair_care'),
	url(r'^health_care', views.health_care_article, name='health_care'),
	url(r'^lifestyle_care', views.lifestyle_care_article, name='lifestyle_care'),
	url(r'^product_reviews', views.product_reviews, name='product_reviews'),
	url(r'^accessories', views.accessories, name='accessories'),
]
