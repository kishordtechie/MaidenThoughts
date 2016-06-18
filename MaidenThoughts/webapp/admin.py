from django.contrib import admin
from .models import Articles,Reviews,Authors,Types
from ckeditor.fields import RichTextField
from django import forms
from django.db import models

# class ArticlesAdmin(admin.ModelAdmin):
	# formfield_overrides = { models.TextField: {'widget':forms.Textarea(attrs={'class':'ckeditor'})}, }
    
	# class Media:
		# js =('/ckeditor/ckeditor.js','filebrowser/js/FB_CKeditor.js',)
# # The , at the end of this list IS important.
admin.site.register(Articles)
admin.site.register(Reviews)
admin.site.register(Authors)
admin.site.register(Types)
