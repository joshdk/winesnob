from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# # from django.contrib import admin
# # admin.autodiscover()

# urlpatterns = patterns('',
	# (r'^hello/$', include('winesnob.views.hello')),
	# # Examples:
	# # url(r'^$', 'winesnob_conf.views.home', name='home'),
	# # url(r'^winesnob_conf/', include('winesnob_conf.foo.urls')),

	# # Uncomment the admin/doc line below to enable admin documentation:
	# # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# # Uncomment the next line to enable the admin:
	# # url(r'^admin/', include(admin.site.urls)),
# )
from django.conf.urls.defaults import *
# from winesnob.views import hello
import apps.winesnob.views as views

urlpatterns = patterns('',
	('^$',             views.search),
	('^results/(.*)$', views.results),
)
