from django.conf.urls import patterns, include, url
import os

# Uncomment the next two lines to enable the admin: 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'plag.views.home', name='home'),
    # url(r'^plag/', include('plag.foo.urls')), 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
    { 'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\','/') }), 

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')), 
    (r'^tinymce/', include('tinymce.urls')), 
    url(r'^weblog/', include('plag.weblog.urls')), 

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
