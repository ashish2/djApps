
#Api calls urls

# Limit & offset pagination
#http://localhost:8000/api/v1/movies/?format=json&limit=1&offset=0

# slug, language & categories filtering
#http://localhost:8000/api/v1/movies/?format=json&slug=terminator-2&languages=1&categories=2

#sorting ordering
#http://localhost:8000/api/v1/movies/?format=json&order_by=-length

#filter: language, category
#sort: length, release_date

from django.db import models
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource
from ajency.models import *
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie import fields
#from tastypie.serializers import Serializer

# N
from tastypie.authentication import *
from tastypie.authorization import Authorization, DjangoAuthorization
#

class CategoriesResource(ModelResource):
	class Meta:
		queryset = Categories.objects.all()
	

class LanguagesResource(ModelResource):
	class Meta:
		queryset = Languages.objects.all()
	

class MoviesResource(ModelResource):
	languages = fields.ToManyField('ajency.api.LanguagesResource', 'languages', full=True, null=True)
	categories = fields.ToManyField('ajency.api.CategoriesResource', 'categories', full=True, null=True)
	
	class Meta:
		queryset = Movies.objects.all()
		resource_name = 'movies'
		excludes = ['created_at']
		allowed_methods = ['get']
		paginator_class = Paginator
		ordering = ['length', 'release_date']
		filtering = {
			"slug": ('exact', 'startswith',),
			"id": ('exact', 'startswith',),
			"title": ALL,
			"languages": ALL_WITH_RELATIONS,
			"categories": ALL_WITH_RELATIONS,
		}
		
	#def get_list(self, request, **kwargs):
		#pass
	#
	#def hydrate(self, bundle):
		#"""
			#Hydrate to take from client & send to database
		#"""
		#pass
	#
	#def dehydrate(self, bundle):
		#"""
			#Dehydrate to take from DB & send to client
			#Check, bundle.obj, bundle.data 
		#"""
		#req = bundle.request
		#if req.GET:
			#if req.GET['sort']:
				#bundle.obj
			#print "dehydrate req.GET"
			#print req.GET
			#print req.GET['limit']
			#print req.GET['format']
			#print bundle
			#print bundle.obj
		#return bundle
	
	def alter_list_data_to_serialize(self, request, data_dict):
		print "data_dict"
		print data_dict
		#if isinstance(data_dict, dict):
			#if 'meta' in data_dict:
				#Get rid of the "meta".
				#del(data_dict['meta'])
		return data_dict
	
	#def apply_sorting():
		#pass
		#
	#def apply_filters():
		#pass
		
	def build_filters(self, filters=None):
		if filters is None:
			filters = {}
		orm_filters = super(MoviesResource, self).build_filters(filters)
		# Your filtering
		if 'category' in filters:
			orm_filters['category'] = filters.get('category')
		if 'language' in filters:
			orm_filters['language'] = filters.get('language')
		return orm_filters
	
	
