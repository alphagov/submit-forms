from django.shortcuts import render
from django.db.models import Count
from django.http import Http404

from ..models import Page
from ..runner import runners


def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages': pages})


def page(request, key=None, template='page.html'):
    page = Page.objects.get(page=key)

    return render(request, template, {
        'page': page,
        'runners': runners,
    })


def page_preview(request, key=None, runner=None):
    if runner not in runners:
        raise Http404("Not found")
    template = 'runner/%s/page.html' % (runner)
    return page(request, key, template)
