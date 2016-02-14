
#Api calls urls

# Limit & offset pagination
#http://localhost:8000/api/v1/movies/?format=json&limit=1&offset=0

# slug, language & categories filtering
#http://localhost:8000/api/v1/movies/?format=json&slug=terminator-2&languages=1&categories=2

#sorting ordering
#http://localhost:8000/api/v1/movies/?format=json&order_by=-length

#filter: language, category
#sort: length, release_date

import json

from django.db import models
from tastypie.paginator import Paginator
from tastypie.resources import Resource, ModelResource
from ajency.models import *
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie import fields
#from tastypie.serializers import Serializer

# N
from tastypie.authentication import *
from tastypie.authorization import Authorization, DjangoAuthorization
#

import redis
redis = redis.StrictRedis(host='localhost', port=6379, db=1)

# Cache
#from django.views.decorators.cache import cache_page
#

class CategoriesResource(ModelResource):
	class Meta:
		queryset = Categories.objects.all()
	

class LanguagesResource(ModelResource):
	class Meta:
		queryset = Languages.objects.all()
	

class RedisObject(object):
	def __init__(self, initial=None):
	#def __init__(self, id=None, title=None):
		self.__dict__['_data'] = {}

		if hasattr(initial, 'items'):
			self.__dict__['_data'] = initial

	def __getattr__(self, title):
		return self._data.get(title, None)

	def __setattr__(self, name, value):
		self.__dict__['_data'][name] = value

	def to_dict(self):
		return self._data

from tastypie.bundle import Bundle

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
		
	def get_object_list(self, request):
		""" Check All or :id of movies in redis & return if it exists else Get from DB """
		redis_key_constant = "movies"
		di = redis.hgetall(redis_key_constant)
		obj = []
		for i in di:
			d = {}
			#m = Movies(id=i, title=di[i])
			d["id"] = i
			d["title"] = di[i]
			obj.append(d)
		res = super(MoviesResource, self).get_object_list(request)
		res.objects = obj
		print res.objects
		return res
		#
		#return super(MoviesResource, self).get_object_list(request)
	
	#def obj_get_list(self, bundle, **kwargs):
		#redis_key_constant = "movies"
		#di = redis.hgetall(redis_key_constant)
		#obj = []
		#for i in di:
			#d = {}
			##m = Movies(id=i, title=di[i])
			#d["id"] = i
			#d["title"] = di[i]
			#obj.append(d)
		##res = super(MoviesResource, self).get_object_list(request)
		#res.objects = obj
		#print res.objects
		#return res
		
	
	def build_filters(self, filters=None):
		if filters is None:
			filters = {}
		orm_filters = super(MoviesResource, self).build_filters(filters)
		#Your filtering
		if 'category' in filters:
			orm_filters['category'] = filters.get('category')
		if 'language' in filters:
			orm_filters['language'] = filters.get('language')
		return orm_filters
	
	
	#@cache_page(60*5)
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
		
	def get_all_movies(self):
		""" Random Redis Testing"""
		ma = cache.get("ma")
		if ma:
			return ma
		ma = self.objects.all()
		cache.set("ma", ma)
		return ma
	

class RedisMoviesResource(Resource):
	id = fields.IntegerField(attribute="id")
	title = fields.CharField(attribute="title")
	
	class Meta:
		queryset = RedisObject
		object_class = RedisObject
		resource_name = 'redismovies'
		
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
		
	
	def detail_uri_kwargs(self, bundle_or_obj):
		kwargs = {}
		if isinstance(bundle_or_obj, Bundle):
			kwargs['pk'] = bundle_or_obj.obj.uuid
		else:
			kwargs['pk'] = bundle_or_obj.uuid
		return kwargs
	
	
	def _client(self):
		return redis
	
	def _bucket(self):
		client = self._client()
		# Note that we're hard-coding the bucket to use. Fine for
		# example purposes, but you'll want to abstract this.
		return client.bucket('messages')
	
	def obj_get(self, bundle, **kwargs):
		bucket = self._client()
		message = bucket.hget( "movies", kwargs['pk'])
		
		#initial=message.get_data()
		ini= {"id": kwargs['pk'], "title": message}
		return RedisObject(initial = ini)
	
	def get_object_list(self, request):
		""" Check All or :id of movies in redis & return if it exists else Get from DB """
		query = self._client()
		res = list()
		redis_key_constant = "movies"
		di = redis.hgetall(redis_key_constant)
		for i in di:
			d = { "id": i, "title": di[i] }
			m = RedisObject()
			m.id = i
			m.title = di[i]
			res.append(m)
		
		return res
	
	def obj_get_list(self, bundle, **kwargs):
		return self.get_object_list(bundle.request)
	
