from django.shortcuts import render
from django.db.models import Count
from django.http import Http404

from ..models import Page


def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages': pages})


def page(request, key=None, runner=None, template=None):
    page = Page.objects.get(page=key)

    if not runner:
        template = 'page.html'
    elif runner in ['elements']:
        template = 'runner/%s/page.html' % (runner)

    if template:
        return render(request, template, {
            'page': page,
        })

    raise Http404("Not found")
