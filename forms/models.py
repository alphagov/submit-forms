from django.db import models
from django.utils.translation import ugettext_lazy as _


class Organisation(models.Model):
    organisation = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=256)
    website = models.CharField(max_length=256)

    def __str__(self):
       return self.organisation + " " + self.name


class Phase(models.Model):
    phase = models.CharField(max_length=16, primary_key=True)


class Pattern(models.Model):
    pattern = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')


class Field(models.Model):
    field = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    pattern = models.ForeignKey(Pattern)
    min_length = models.PositiveIntegerField()
    max_length = models.PositiveIntegerField()
    regex = models.CharField(max_length=512, blank=True, default='')


class Question(models.Model):
    question = models.IntegerField(primary_key=True)
    text = models.TextField(blank=True, default='')
    field = models.ForeignKey(Field)


class Section(models.Model):
    section = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    sections = models.ManyToManyField(Question, through='SectionQuestion')


class Form(models.Model):
    form = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, default='')
    phase = models.CharField(max_length=16, default='ALPHA')
    organisations = models.ManyToManyField(Organisation)
    sections = models.ManyToManyField(Section, through='FormSection')


class FormSection(models.Model):
    form = models.ForeignKey(Form)
    section = models.ForeignKey(Section)
    order = models.PositiveIntegerField()


class SectionQuestion(models.Model):
    section = models.ForeignKey(Section)
    question = models.ForeignKey(Question)
    order = models.PositiveIntegerField()
