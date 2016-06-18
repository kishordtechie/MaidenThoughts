from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Authors(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	def __str__(self):
		return self.name
	

class Types(models.Model):
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=200)
	tags = models.CharField(max_length=200)
	def __str__(self):              # __unicode__ on Python 2
		return self.name
	
class Articles(models.Model):
	header = models.CharField(max_length=200)
	published_on = models.DateTimeField('date published')
	author = models.ForeignKey(Authors)
	type = models.ForeignKey(Types)
	images = models.ImageField(upload_to='photos/%Y/%m/%d',max_length=200)
	content = RichTextField()
	tags = models.CharField(max_length=200)
	viewed_count = models.IntegerField()
	def __str__(self):
		return self.header

class Reviews(models.Model):
	header = models.CharField(max_length=200)
	published_on = models.DateTimeField('date published')
	author = models.ForeignKey(Authors)
	type = models.ForeignKey(Types)
	images = models.ImageField(upload_to='photos/%Y/%m/%d',max_length=200)
	content = models.TextField(max_length=10000)
	tags = models.CharField(max_length=200)
	viewed_count = models.IntegerField()
	def __str__(self):
		return self.header