# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.http.response import HttpResponse

admin.autodiscover()


def empty_view(request):
    return HttpResponse

urlpatterns = [
    url(r'^home/', empty_view, name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^djstripe/', include('djstripe.urls',
            namespace="djstripe", app_name="djstripe")),
    url(r'^testapp/', include('tests.apps.testapp.urls')),
    url(r'^__debug__/', include('tests.apps.testapp.urls')),
    url(
        r'^testapp_namespaced/',
        include('tests.apps.testapp_namespaced.urls',
        namespace="testapp_namespaced",
        app_name="testapp_namespaced")),

    # Represents protected content
    url(r'^testapp_content/', include('tests.apps.testapp_content.urls')),
    # For testing fnmatches
    url(
        r"test_fnmatch/extra_text/$",
        empty_view,
        name="test_fnmatch"
    ),
]
