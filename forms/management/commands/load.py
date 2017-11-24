from django.core.management.base import BaseCommand

import io
import os
import csv

from ...models import Organisation, Phase, DataType, InputType, Field, Question, Section, Form

from django.utils.dateparse import parse_datetime
from django.core.exceptions import ObjectDoesNotExist

path = './data/%s.tsv'
field_sep = ';'
sep = '\t'


def tsv_reader(name):
    """ read register-like data from TSV"""
    return csv.DictReader(open(path % (name)), delimiter=sep)


def load_organisation():
    for row in tsv_reader('organisation'):
        o = Organisation(organisation=row['organisation'], name=row['name'], website=row['website'])
        o.save()


def load_phase():
    for row in tsv_reader('phase'):
        o = Phase(phase=row['phase'])
        o.save()


def load_datatype():
    for row in tsv_reader('datatype'):
        o = DataType(datatype=row['datatype'])
        o.save()


def load_inputtype():
    for row in tsv_reader('inputtype'):
        o = InputType(inputtype=row['inputtype'])
        o.save()


def load_field():
    for row in tsv_reader('field'):
        o = Field(field=row['field'],
                  label=row['label'],
                  hint=row['hint'],
                  inputtype=InputType.objects.get(inputtype=row['inputtype']),
                  datatype=DataType.objects.get(datatype=row['datatype']))
        o.save()


def load_question():
    for row in tsv_reader('question'):
        o = Question(question=row['question'],
                       heading=row['heading'],
                       guidance=row['guidance'],
                       warning=row['warning'],
                       detail=row['detail'])
        o.save()


def load_section():
    for row in tsv_reader('section'):
        o = Section(section=row['section'],
                    heading=row['heading'],
                    guidance=row['guidance'])
        o.save()


def load_form():
    for row in tsv_reader('form'):
        o = Form(form=row['form'],
                   heading=row['heading'],
                   description=row['description'],
                   phase=Phase.objects.get(phase=row['phase']),
                   reference=row['reference'])
        o.save()
        for organisation in row['organisations'].split(field_sep):
            o.organisations.add(organisation)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('table', type=str)

    def handle(self, **options):
        if options['table'] == 'organisation':
            load_organisation()
        elif options['table'] == 'phase':
            load_phase()
        elif options['table'] == 'datatype':
            load_datatype()
        elif options['table'] == 'inputtype':
            load_inputtype()
        elif options['table'] == 'field':
            load_field()
        elif options['table'] == 'question':
            load_question()
        elif options['table'] == 'section':
            load_section()
        elif options['table'] == 'form':
            load_form()
        else:
            raise ValueError('Unknown table', options['table'])
