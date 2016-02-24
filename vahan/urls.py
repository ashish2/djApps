from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView


# Caching
from django.views.decorators.cache import cache_page

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pysite.settings import STATIC_URL

# Api
#from django.conf.urls.defaults import *
from tastypie.api import *
# Api-


urlpatterns = patterns('vahan.views', 
	
	url(r"list_all", "list_all" ),
	url(r"list-all", "list_all" ),
	# Default
	url(r"", "list_all" ),
)
