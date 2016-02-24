from django.shortcuts import render

from vahan.models import *
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from django.core.cache import cache


# Create your views here.

#import wit
#wit_access_token = 'ACCESS_TOKEN'
#wit.init()
#response = wit.voice_query_auto(wit_access_token)
#print("Response: {}".format(response) )
#wit.close()


def list_all(request):
	print "hi there"
	pass
	
	d = {}
	return render_to_response('v_list.html', d, context_instance=RequestContext(request) )
