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
        'sections': [],
    }

    for org in organisations:
        f['organisations'].append({
            'organisation': org.organisation,
            'name': org.name,
            'website': org.website
        })

    for formsection in form.formsection_set.all():
        section = formsection.section
        s = {
            'number': formsection.number,
            'section': section.section,
            'heading': section.heading,
            'guidance': section.guidance,
            'pages': [],
        }

        for sectionpage in section.sectionpage_set.all():
            page = sectionpage.page
            p = {
                'number': sectionpage.number,
                'page': page.page,
                'pagetype': page.pagetype.pagetype,
                'description': page.description,
                'heading': page.heading,
                'guidance': page.guidance,
                'warning': page.warning,
                'detail': page.detail,
                'fields': [],
            }
            for pagefield in page.pagefield_set.all():
                field = pagefield.field
                p['fields'].append({
                    'number': pagefield.number,
                    'field': field.field,
                    'inputtype': field.inputtype.inputtype,
                    'datatype': field.datatype.datatype,
                })

            s['pages'].append(p)

        f['sections'].append(s)

    return JsonResponse(f)
