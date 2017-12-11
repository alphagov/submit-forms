from django.shortcuts import render

from ..models import PageType
from ..runner import runners


def pagetypes(request):
    pagetypes = PageType.objects.all()
    return render(request, 'pagetypes.html', {'pagetypes': pagetypes})


def pagetype(request, key=None, template='pagetype.html'):
    pagetype = PageType.objects.get(pagetype=key)

    return render(request, template, {
        'pagetype': pagetype,
        'runners': runners,
    })
