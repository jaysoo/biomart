from django.conf.urls.defaults import *
import views as views
from feeds import ArticlesFeed

urlpatterns = patterns('',

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view=views.article_detail,
        name='news_detail_month_numeric'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view=views.article_detail,
        name='news_detail'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        view=views.article_archive_day,
        name='news_archive_day'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        view=views.article_archive_month,
        name='news_archive_month'),

    url(r'^(?P<year>\d{4})/$',
        view=views.article_archive_year,
        name='news_archive_year'),

    url (r'^search/$',
        view=views.search,
        name='news_search'),

    url(r'^page/(?P<page>\w)/$',
        view=views.article_list,
        name='news_index_paginated'),

    url(r'^$',
        view=views.article_list,
        name='news_index'),

    (r'^feed/$', ArticlesFeed()),
)
