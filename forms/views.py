from django.shortcuts import render
from django.contrib import admin
from django.db.models import Count
from django.http import Http404

from .models import Organisation, Form

admin.autodiscover()

# TBD: plugin architecture / separate runner application ..
runners = {
    'elements': {
        'name': 'GOV.UK form elements',
        'url': 'http://govuk-elements.herokuapp.com/form-elements/',
        'media': 'a single web page',
    }
}


def home(request):
    return render(request, 'home.html')


def forms(request):
    forms = Form.objects \
        .annotate(n_sections=Count('sections', distinct=True)) \
        .annotate(n_questions=Count('sections__questions', distinct=True))
    return render(request, 'forms.html', {'forms': forms})


def form(request, key=None, template='form.html'):
    form = Form.objects.get(form=key)
    organisations = Organisation.objects.filter(
        organisation__in=form.organisations.all())

    return render(request, template, {
        'form': form,
        'organisations': organisations,
        'runners': runners,
    })


def preview(request, key=None, runner=None):
    if runner not in runners:
        raise Http404("Not found")
    template = 'runner/%s/preview.html' % (runner)
    return form(request, key, template)
