from django.shortcuts import render

from ..models import List


def lists(request):
    lists = List.objects.all()
    return render(request, 'lists.html', {'lists': lists})


def list_(request, key=None, template='list.html'):
    l = List.objects.get(id=key)

    return render(request, template, {
        'l': l,
    })
