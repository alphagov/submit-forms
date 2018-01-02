from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

import forms.views

from httpproxy.views import HttpProxy

admin.autodiscover()

key = '(?P<key>[\w\d-]{1,32})'
runner = '(?P<runner>[\w\d-]{1,256})'

urlpatterns = [

    url(r'^$', forms.views.home),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^forms/$', forms.views.forms, name='forms'),
    url(r'^form/%s/$' % (key), forms.views.form, name='form'),
    url(r'^form/%s/preview/%s/$' % (key, runner), forms.views.form, name='form_preview'),
    url(r'^form/%s.json$' % (key), forms.views.form_json, name='form_json'),

    url(r'^pages/$', forms.views.pages, name='pages'),
    url(r'^page/%s/$' % (key), forms.views.page, name='page'),
    url(r'^page/%s/preview/%s/$' % (key, runner), forms.views.page, name='page_preview'),

    url(r'^fields/$', forms.views.fields, name='fields'),
    url(r'^field/%s/$' % (key), forms.views.field, name='field'),

    url(r'^inputtypes/$', forms.views.inputtypes, name='inputtypes'),
    url(r'^inputtype/%s/$' % (key), forms.views.inputtype, name='inputtype'),

    url(r'^pagetypes/$', forms.views.pagetypes, name='pagetypes'),
    url(r'^pagetype/%s/$' % (key), forms.views.pagetype, name='pagetype'),

    url(r'^datatypes/$', forms.views.datatypes, name='datatypes'),
    url(r'^datatype/%s/$' % (key), forms.views.datatype, name='datatype'),

    url(r'^lists/$', forms.views.lists, name='lists'),
    url(r'^list/%s/$' % (key), forms.views.list_, name='list'),
]
