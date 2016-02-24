:/usr/lib/python2.7/dist-packages:/usr/lib/pymodules/python2.7

import json

from django.db import models
from tastypie.paginator import Paginator
from tastypie.resources import Resource, ModelResource
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie import fields
#from tastypie.serializers import Serializer
from tastypie.authentication import *
from tastypie.authorization import Authorization, DjangoAuthorization

from tastypie.bundle import Bundle

from vahan.models import *

class QueryResource(ModelResource):
	class Meta:
		queryset = Query.objects.all()
		resource_name = 'query'
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
	
	def __init__(self):
		#if request.data.intent == "get_search":
			## Initiate the Search object
			#SearchResource(request.data)
		#elif request.data.intent == "send_sms":
			## Initiating the Sms object
			#SmsResource(request.data)
		pass
	
	def hydrate(self, bundle):
		# access request from bundle.request
		pass
	


class SmsResource(ModelResource):
	class Meta:
		resource_name = "sms"
	
	def __init__(self, data):
		self.data = data
		self.url = "http://domain/some/telecom/service/sms/api/url"


class SearchResource(ModelResource):
	class Meta:
		resource_name = "search"
	
	def __init__(self, data):
		self.data = data
		
		transcript = self.data.entities.results[0][0].transcript
		self.url = "https://google.com/search#q="+transcript
		
	

