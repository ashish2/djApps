import json

from django.db import models
from tastypie.paginator import Paginator
from tastypie.resources import Resource, ModelResource
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.authentication import *
from tastypie.authorization import Authorization, DjangoAuthorization

from tastypie.bundle import Bundle

from vahan.models import *

class QueryResource(ModelResource):
	class Meta:
		serializer = Serializer()
		queryset = Query.objects.all()
		resource_name = 'query'
		excludes = ['created_at']
		allowed_methods = ['get', 'post']
		paginator_class = Paginator
		ordering = ['length', 'release_date']
		filtering = {
			"slug": ('exact', 'startswith',),
			"id": ('exact', 'startswith',),
			"title": ALL,
			"languages": ALL_WITH_RELATIONS,
			"categories": ALL_WITH_RELATIONS,
		}
	
	
	def hydrate(self, bundle):
		# It came here
		print "Query bundle.request"
		print bundle.request
		print "dir(bundle.request)"
		print dir(bundle.request)
		print "bundle.data"
		print bundle.data
		print type(bundle.data)
		pass
	
	


class DecisionResource(Resource):
	""" Make a decision here about what is the intent & then,
	send an Http Redirect to the appropriate resource
	Eg. if intent concluded as send_sms then redirect to Sms api, if, `search` redirect to search api
	
	Eg. 
	di = dict()
	di["send_sms"] = "/api/v1/sms"
	di["search"] = "/api/v1/search"
	
	url = di[intent]
	HttpRedirect(url)
	"""
	
	class Meta:
		resource_name = "decision"
		allowed_methods = ['post']
	
	#def __init__(self):
		#if request.data.intent == "get_search":
			## Initiate the Search object
			#SearchResource(request.data)
		#elif request.data.intent == "send_sms":
			## Initiating the Sms object
			#SmsResource(request.data)
		#pass
	
	def hydrate(self, bundle):
		# access request from bundle.request
		print "bundle.request"
		print bundle.request
		print "dir(bundle.request)"
		print dir(bundle.request)
		print "bundle.request.data"
		print bundle.request.data
		pass
	


class SmsResource(ModelResource):
	class Meta:
		resource_name = "sms"
	
	def __init__(self, data):
		self.data = data
		self.url = "http://domain/some/telecom/service/sms/api/url"


class SearchObject(object):
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


# Non ORM Sources
class SearchResource(Resource):
	"""
	goo_res = { u'cacheId': u'VHU5CiBhkpUJ',
	 u'displayLink': u'www.owlnet.rice.edu',
	 u'fileFormat': u'PDF/Adobe Acrobat',
	 u'formattedUrl': u'www.owlnet.rice.edu/~bioe301/.../Chapter%201%20Homework.pdf',
	 u'htmlFormattedUrl': u'www.owlnet.rice.edu/~bioe301/.../Chapter%201%20Homework.pdf', 
	 u'htmlSnippet': u'Chapter 1 Homework. 1. Advanced breast cancer has a high mortality. Initial <br>\nclinical trials indicated that high dose chemotherapy followed by a bone marrow&nbsp;...',
	 u'htmlTitle': u'Chapter 1 Homework 1. Advanced breast cancer has a high <b>...</b>',
	 u'kind': u'customsearch#result',
	 u'link': u'http://www.owlnet.rice.edu/~bioe301/kortum/class/How%20to%20use%20the%20textbook/Homework/Chapter%201%20Homework.pdf',
	 u'mime': u'application/pdf',
	 u'pagemap': {u'metatags': [{u'author': u'asl4',
		u'creationdate': u"D:20090909165220-05'00'",
		u'creator': u'PScript5.dll Version 5.2.2',
		u'moddate': u"D:20090909165220-05'00'",
		u'producer': u'Acrobat Distiller 7.0.5 (Windows)',
		u'title': u'Microsoft Word - Chapter 1 Homework.doc'}]},
	  u'snippet': u'Chapter 1 Homework. 1. Advanced breast cancer has a high mortality. Initial \nclinical trials indicated that high dose chemotherapy followed by a bone marrow\xa0...',
	 u'title': u'Chapter 1 Homework 1. Advanced breast cancer has a high ...'}
	"""
	
	displayLink = fields.CharField(attribute='displayLink')
	formattedUrl = fields.CharField(attribute='formattedUrl')
	htmlSnippet = fields.CharField(attribute='htmlSnippet')
	htmlTitle = fields.CharField(attribute='htmlTitle')
	link = fields.CharField(attribute='link')
	title = fields.CharField(attribute='title')
	
	_search_url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=017576662512468239146:omuauf_lfve&q=%s"
	# FTM
	_PRIVATE_KEY="AIzaSyAh1deF7TKl6Lu24zU4Ird3AxH8r8MIV4I"
	
	class Meta:
		#resource_name = "search"
		resource_name = "get_search"
		object_class=SearchObject
		authorization = Authorization()
		list_allowed_methods = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		#authorization = DjangoAuthorization()
		
	#def __init__(self, data):
		#self.data = data
		#transcript = self.data.entities.results[0][0].transcript
		#self.url = "https://google.com/search#q="+transcript

	# Specific to this resource, just to get the needed Riak bits.
	def _client(self):
		#return search.googleClient()
		return None
	
	@classmethod
	# This shud be _client
	def makeCall(cls, request):
		query = request.GET.get("search_query")
		import urllib2, json, pprint
		url = cls._search_url % (cls._PRIVATE_KEY, query)
		data = urllib2.urlopen(url)
		d = json.load(data)
		# Make an HTTPResponse in json
		#pprint.PrettyPrinter(indent=4).pprint(d['items'][0])
		#return d
		return d['items']
		
	def _bucket(self):
		client = self._client()
		# Note that we're hard-coding the bucket to use. Fine for
		# example purposes, but you'll want to abstract this.
		return client.bucket('messages')

	# The following methods will need overriding regardless of your
	# data source.
	def detail_uri_kwargs(self, bundle_or_obj):
		kwargs = {}

		if isinstance(bundle_or_obj, Bundle):
			kwargs['pk'] = bundle_or_obj.obj.uuid
		else:
			kwargs['pk'] = bundle_or_obj.uuid

		return kwargs

	def get_object_list(self, request):
		query = self._client()
		print "get_object_list request"
		print request
		print request.__dict__
		print request.GET.get("intent")
		
		query_res = self.makeCall(request)
		
		print "query_res"
		print query_res
		
		results = []
		for result in query_res:
			new_obj = SearchObject(initial=result)
			results.append(new_obj)
		
		print "results"
		print results
		
		return results

	def obj_get_list(self, bundle, **kwargs):
		# Filtering disabled for brevity...
		return self.get_object_list(bundle.request)

	#def obj_get(self, bundle, **kwargs):
		#bucket = self._bucket()
		#message = bucket.get(kwargs['pk'])
		#return SearchObject(initial=message.get_data())

	#def obj_create(self, bundle, **kwargs):
		#bundle.obj = RiakObject(initial=kwargs)
		#bundle = self.full_hydrate(bundle)
		#bucket = self._bucket()
		#new_message = bucket.new(bundle.obj.uuid, data=bundle.obj.to_dict())
		#new_message.store()
		#return bundle

	def obj_update(self, bundle, **kwargs):
		return self.obj_create(bundle, **kwargs)

	def obj_delete_list(self, bundle, **kwargs):
		bucket = self._bucket()

		for key in bucket.get_keys():
			obj = bucket.get(key)
			obj.delete()

	def obj_delete(self, bundle, **kwargs):
		bucket = self._bucket()
		obj = bucket.get(kwargs['pk'])
		obj.delete()

	def rollback(self, bundles):
		pass
	






