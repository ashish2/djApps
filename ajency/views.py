from django.shortcuts import render

from ajency.models import *
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from django.core.cache import cache

# Create your views here.

# Testing Django Local Cache/Memcache
@cache_page(60*5)
def list_all(request):
	#mov = Movies.objects.filter(Q(parent_id=None)).order_by("-date")
	mov = Movies.objects.all()
	
	paginator = Paginator(mov, 1)
	try:
		page = int(request.GET.get("page", "1"))
	except ValueError:
		page = 1
	try:
		mov = paginator.page(page)
	except (InvalidPage, EmptyPage):
		mov = paginator.page(paginator.num_pages)
	
	d = dict(posts=mov,)
	return render_to_response('aj_list.html', d, context_instance=RequestContext(request) )

# Testing Redis
def list(request):
	m= cache.get("m")
	if m:
		mov = m
	else:
		mov = Movies.objects.all()
		cache.set("m", mov)
	
	paginator = Paginator(mov, 1)
	try:
		page = int(request.GET.get("page", "1"))
	except ValueError:
		page = 1
	try:
		mov = paginator.page(page)
	except (InvalidPage, EmptyPage):
		mov = paginator.page(paginator.num_pages)
	
	d = dict(posts=mov,)
	return render_to_response('aj_list.html', d, context_instance=RequestContext(request) )
