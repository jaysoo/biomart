from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'biomart.views.home', name='home'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()  
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
    urlpatterns += patterns('', (r'^(?P<path>ie-css3.htc)?$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
    urlpatterns += patterns('', (r'^(?P<path>humans.txt)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
    urlpatterns += patterns('', (r'^(?P<path>robots.txt)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
    urlpatterns += patterns('', (r'^(?P<path>favicon.ico)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
