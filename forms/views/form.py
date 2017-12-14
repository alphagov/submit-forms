from django.shortcuts import render
from django.db.models import Count
from django.http import Http404, JsonResponse

from ..models import Organisation, Form


def forms(request):
    forms = Form.objects \
        .annotate(n_sections=Count('sections', distinct=True)) \
        .annotate(n_pages=Count('sections__pages', distinct=True))
    return render(request, 'forms.html', {'forms': forms})


def form(request, key=None, runner=None, template=None):
    form = Form.objects.get(form=key)
    organisations = Organisation.objects.filter(
        organisation__in=form.organisations.all())

    if not runner:
        template = 'form.html'
    elif runner in ['elements']:
        template = 'runner/%s/form.html' % (runner)

    if template:
        return render(request, template, {
            'form': form,
            'organisations': organisations,
        })

    raise Http404("Not found")


def form_json(request, key=None, runner=None, template=None):
    form = Form.objects.get(form=key)
    organisations = Organisation.objects.filter(
        organisation__in=form.organisations.all())

    f = {
            'form': form.form,
            'heading': form.heading,
            'description': form.description,
            'phase': form.phase.phase,
            'reference': form.reference,
            'organisations': [],
            'form_sections': [],
    }

    for o in organisations:
        f['organisations'].append({'organisation': o.organisation, 'name': o.name, 'website': o.website})

    return JsonResponse(f)
