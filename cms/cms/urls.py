from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

##Added custom for relative urls.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
##

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': os.path.join(PROJECT_PATH, '../vendors/tinymce/jscripts/tiny_mce')}),
    #Page 30 has the view as cms.search.views.search, but this makes more sense to me ... and works.
    url(r'^search/$', 'search.views.search'),
    url(r'',include('django.contrib.flatpages.urls'))
)
