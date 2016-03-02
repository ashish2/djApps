from django.conf.urls import include, url, patterns
from django.contrib import admin

from tastypie.api import Api
from ajency.api import *
from vahan.api import *

import os
cwd = os.getcwd()

v1_api = Api(api_name='v1')
v1_api.register(MoviesResource())
v1_api.register(RedisMoviesResource())
v1_api.register(QueryResource())
v1_api.register(DecisionResource())
#v1_api.register(SmsResource())
v1_api.register(SearchResource())


urlpatterns = [
	# Examples:
	# url(r'^$', 'pysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	
	url(r'^ajency/', include("ajency.urls")),
	url(r'^vahan/', include("vahan.urls")),
	
	# Api
	url(r'^api/', include(v1_api.urls)),
	
	# Static
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': cwd +'/static/'} ),
	# Static/
	
	
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path.join(path.dirname(__file__), 'static')}),
]
