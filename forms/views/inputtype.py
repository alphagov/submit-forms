from django.shortcuts import render

from ..models import InputType


def inputtypes(request):
    inputtypes = InputType.objects.all()
    return render(request, 'inputtypes.html', {'inputtypes': inputtypes})


def inputtype(request, key=None, template='inputtype.html'):
    inputtype = InputType.objects.get(inputtype=key)

    return render(request, template, {
        'inputtype': inputtype,
    })
