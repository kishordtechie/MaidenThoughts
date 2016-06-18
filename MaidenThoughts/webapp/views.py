from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from .models import Articles,Types
# Create your views here.

def index(request):
	articles = Articles.objects.all()[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request, 'webapp/index.html', context)
	
def skin_care_article(request):
	articles = Articles.objects.all().filter(type__name__startswith="skin")[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request,'webapp/skin_care.html',context)
	
def hair_care_article(request):
	articles = Articles.objects.all().filter(type__name__startswith="hair")[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request,'webapp/hair_care.html',context)
	
def health_care_article(request):
	articles = Articles.objects.all().filter(type__name__startswith="health")[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request,'webapp/health_care.html',context)
	
def lifestyle_care_article(request):
	articles = Articles.objects.all().filter(type__name__startswith="lifestyle")[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request,'webapp/lifestyle_care.html',context)
	
def product_reviews(request):
	articles = Articles.objects.all().filter(type__name__startswith="product")[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request,'webapp/product_reviews.html',context)
	
def accessories(request):
	articles = Articles.objects.all().filter(type__name__startswith="accessories")[:3]
	related_articles = Articles.objects.all()
	popular_articles = Articles.objects.order_by('viewed_count')[:5]
	context = {'articles':articles,'related_articles':related_articles,'popular_articles':popular_articles}
	return render(request,'webapp/accessories.html',context) 