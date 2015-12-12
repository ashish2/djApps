from django.contrib import admin

# Register your models here.
from ajency.models import *
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

class CategoriesAdmin(admin.ModelAdmin):
	search_fields = ["id",]

class LanguagesAdmin(admin.ModelAdmin):
	search_fields = ["id",]

class MoviesAdmin(admin.ModelAdmin):
	search_fields = ["id",]

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Movies, MoviesAdmin)
