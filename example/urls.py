# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('terms.urls')),
]