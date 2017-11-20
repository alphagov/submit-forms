from django.core.management.base import BaseCommand

import io
import os
import csv
import requests

from ...models import Organisation, Phase, DataType, InputType

from django.utils.dateparse import parse_datetime
from django.core.exceptions import ObjectDoesNotExist

url = 'https://raw.githubusercontent.com/alphagov/submit-forms/master/data/%s.tsv'
field_sep = ';'
sep = '\t'


def tsv_reader(name):
    """ read register-like data from government-form-data TSV"""
    resp = requests.get(url=url % (name))
    resp.raise_for_status()
    return csv.DictReader(io.StringIO(resp.text), delimiter=sep)


def load_organisation():
    print("loading organisation data")
    for row in tsv_reader('organisation'):
        o = Organisation(organisation=row['organisation'], name=row['name'], website=row['website'])
        o.save()


def load_phase():
    print("loading phase data")
    for row in tsv_reader('phase'):
        o = Phase(phase=row['phase'])
        o.save()


def load_datatype():
    print("loading datatype data")
    for row in tsv_reader('datatype'):
        o = DataType(datatype=row['datatype'])
        o.save()


def load_inputtype():
    print("loading inputtype data")
    for row in tsv_reader('inputtype'):
        o = InputType(inputtype=row['inputtype'])
        o.save()


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
        else:
            raise ValueError('Unknown table', options['table'])
