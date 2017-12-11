from django.shortcuts import render

from ..models import List
from ..runner import runners


def lists(request):
    lists = List.objects.all()
    return render(request, 'lists.html', {'lists': lists})


def list_(request, key=None, template='list.html'):
    l = List.objects.get(id=key)

    return render(request, template, {
        'l': l,
        'runners': runners,
    })
