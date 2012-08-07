from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

##Added custom for relative urls.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
##

from coltrane.models import Entry, Link, Category
from tagging.models import Tag

entry_info_dict = {
	'queryset': Entry.live.all(),
	'date_field' : 'pub_date',
}

link_info_dict = {
	'queryset': Link.objects.all(),
	'date_field' : 'pub_date',
}


urlpatterns = patterns('django.views.generic.date_based',
    url(r'^$', 'archive_index',entry_info_dict,'coltrane_entry_archive_index'),
    url(r'^(?P<year>\d{4})/$','archive_year',entry_info_dict,'coltrane_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month',entry_info_dict,'coltrane_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day',entry_info_dict,'coltrane_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)$','object_detail',entry_info_dict,'coltrane_entry_detail'),


    url(r'^links/$','archive_index', link_info_dict,'coltrane_link_archive_index'),
    url(r'^links/(?P<year>\d{4})/$','archive_year', link_info_dict,'coltrane_link_archive_year'),
    url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month', link_info_dict, 'coltrane_link_archive_month'),
    url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day', link_info_dict, 'coltrane_link_archive_day'),
    url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','object_detail', link_info_dict, 'coltrane_link_detail'),

)


urlpatterns += patterns('',
    url(r'^categories/$','django.views.generic.list_detail.object_list',{'queryset': Category.objects.all()}),
    url(r'^categories/(?P<slug>[-\w]+)/$','coltrane.views.category_detail'),
    url(r'^tags/$','django.views.generic.list_detail.object_list',{'queryset': Tag.objects.all()}),
    url(r'^tags/entries/(?P<tag>[-\w]+)/$','tagging.views.tagged_object_list', { 'queryset_or_model': Entry, 'template_name': 'coltrane/entries_by_tag.html' }),
    url(r'^tags/links/(?P<tag>[-\w]+)/$','tagging.views.tagged_object_list', { 'queryset_or_model': Link, 'template_name': 'coltrane/links_by_tag.html' }),
)
