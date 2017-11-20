from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataType(models.Model):
    datatype = models.CharField(max_length=32, primary_key=True)
    description = models.TextField(blank=True, default='')


class InputType(models.Model):
    inputtype = models.CharField(max_length=256, blank=True, default='', primary_key=True)


class List(models.Model):
    name = models.CharField(max_length=256, blank=True, default='')
    description = models.TextField(blank=True, default='')
    datatype = models.ForeignKey(DataType)


class ListItem(models.Model):
    parent = models.ForeignKey(List)
    name = models.CharField(max_length=256, blank=True, default='')
    text = models.TextField(blank=True, default='')


class Organisation(models.Model):
    organisation = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=256)
    website = models.CharField(max_length=256)

    def __str__(self):
       return self.organisation + " " + self.name


class Phase(models.Model):
    phase = models.CharField(max_length=16, primary_key=True)


class Validation(models.Model):
    validation = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    description = models.TextField(blank=True, default='')
    min_length = models.PositiveIntegerField(default=0)
    max_length = models.PositiveIntegerField(blank=True, default='')
    regex = models.CharField(max_length=512, blank=True, default='')
    #whitelist = models.ForeignKey(List)
    #blacklist = models.OneToOneField(List)


class Field(models.Model):
    field = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    description = models.TextField(blank=True, default='')
    inputtype = models.ForeignKey(InputType, default='text')
    datatype = models.ForeignKey(DataType, default='string')
    validation = models.ForeignKey(Validation, default='')


class FieldGroup(models.Model):
    fieldgroup = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')


class FieldGroupField(models.Model):
    fieldgroup = models.ForeignKey(FieldGroup)
    field = models.ForeignKey(Field)
    order = models.PositiveIntegerField()


class Question(models.Model):
    question = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, default='')
    text = models.TextField(blank=True, default='')
    fieldgroup = models.ForeignKey(FieldGroup, default='')
    min_length = models.PositiveIntegerField(default=1, help_text='Minimum number of times the fieldgroup maybe repeated')
    max_length = models.PositiveIntegerField(default=1, help_text='Maximum number of times the fieldgroup maybe repeated')


class Section(models.Model):
    section = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    sections = models.ManyToManyField(Question, through='SectionQuestion')


class SectionQuestion(models.Model):
    section = models.ForeignKey(Section)
    question = models.ForeignKey(Question)
    order = models.PositiveIntegerField()


class Form(models.Model):
    form = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    description = models.TextField(blank=True, default='')
    phase = models.CharField(max_length=16, default='ALPHA')
    reference = models.CharField(max_length=32, blank=True, default='')
    organisations = models.ManyToManyField(Organisation)
    sections = models.ManyToManyField(Section, through='FormSection')


class FormSection(models.Model):
    form = models.ForeignKey(Form)
    section = models.ForeignKey(Section)
    order = models.PositiveIntegerField()
