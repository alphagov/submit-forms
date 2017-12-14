from django.shortcuts import render

from ..models import DataType


def datatypes(request):
    datatypes = DataType.objects.all()
    return render(request, 'datatypes.html', {'datatypes': datatypes})


def datatype(request, key=None, template='datatype.html'):
    datatype = DataType.objects.get(datatype=key)

    return render(request, template, {
        'datatype': datatype,
    })
