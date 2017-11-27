from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

import forms.views

from httpproxy.views import HttpProxy

admin.autodiscover()

urlpatterns = [

    url(r'^$', forms.views.home),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^forms/$', forms.views.forms, name='forms'),

    url(r'^form/(?P<key>[\d]{1,16})/$', forms.views.form, name='form'),
    url(r'^form/(?P<key>[\d]{1,16})/preview/(?P<runner>[\w]{1,256})$', forms.views.preview, name='preview'),
]
