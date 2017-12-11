from django.shortcuts import render

from ..models import Field
from ..runner import runners


def fields(request):
    fields = Field.objects.all()
    return render(request, 'fields.html', {'fields': fields})


def field(request, key=None, template='field.html'):
    field = Field.objects.get(field=key)

    return render(request, template, {
        'field': field,
        'runners': runners,
    })
