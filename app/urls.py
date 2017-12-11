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
    url(r'^form/(?P<key>[\d]{1,16})/preview/(?P<runner>[\w]{1,256})$', forms.views.form_preview, name='form_preview'),

    url(r'^pages/$', forms.views.pages, name='pages'),
    url(r'^page/(?P<key>[\d]{1,16})/$', forms.views.page, name='page'),
    url(r'^page/(?P<key>[\d]{1,16})/preview/(?P<runner>[\w]{1,256})$', forms.views.page_preview, name='page_preview'),

    url(r'^fields/$', forms.views.fields, name='fields'),
    url(r'^field/(?P<key>[\w\d-]{1,32})/$', forms.views.field, name='field'),
    # url(r'^field/(?P<key>[\d]{1,16})/preview/(?P<runner>[\w]{1,256})$', forms.views.field_preview, name='field_preview'),

    url(r'^inputtypes/$', forms.views.inputtypes, name='inputtypes'),
    url(r'^inputtype/(?P<key>[\w\d-]{1,32})/$', forms.views.inputtype, name='inputtype'),

    url(r'^pagetypes/$', forms.views.pagetypes, name='pagetypes'),
    url(r'^pagetype/(?P<key>[\w\d-]{1,32})/$', forms.views.pagetype, name='pagetype'),

    url(r'^datatypes/$', forms.views.datatypes, name='datatypes'),
    url(r'^datatype/(?P<key>[\w\d-]{1,32})/$', forms.views.datatype, name='datatype'),

    url(r'^lists/$', forms.views.lists, name='lists'),
    url(r'^list/(?P<key>[\w\d-]{1,32})/$', forms.views.list_, name='list'),
]
