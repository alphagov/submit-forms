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
]
