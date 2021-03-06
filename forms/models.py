from django.db import models
from django.utils.translation import ugettext_lazy as _


class Organisation(models.Model):
    organisation = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=256)
    website = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Phase(models.Model):
    phase = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return self.phase


class DataType(models.Model):
    datatype = models.CharField(max_length=32, primary_key=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.datatype


class InputType(models.Model):
    inputtype = models.CharField(max_length=256, blank=True, default='', primary_key=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.inputtype


class PageType(models.Model):
    pagetype = models.CharField(max_length=256, blank=True, default='', primary_key=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.pagetype


class Item(models.Model):
    label = models.CharField(max_length=256, blank=True, default='')
    value = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return self.value + " " + self.label


class List(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, default='')
    datatype = models.ForeignKey(DataType)
    items = models.ManyToManyField(Item, through='ListItem')

    def __str__(self):
        return self.name


class ListItem(models.Model):
    _list = models.ForeignKey(List)
    item = models.ForeignKey(Item)
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ['number']


class Field(models.Model):
    field = models.CharField(primary_key=True, max_length=32)
    label = models.CharField(max_length=256, blank=True, default='')
    hint = models.TextField(blank=True, default='')
    inputtype = models.ForeignKey(InputType, default='text')
    datatype = models.ForeignKey(DataType, default='string')
    whitelists = models.ManyToManyField(List, related_name='whitelists', blank=True)
    blacklists = models.ManyToManyField(List, related_name='blacklists', blank=True)

    def __str__(self):
        return self.field


class Page(models.Model):
    page = models.AutoField(primary_key=True)
    pagetype = models.ForeignKey(PageType, default='question')
    description = models.TextField(blank=True, default='')
    heading = models.TextField(blank=True, default='')
    guidance = models.TextField(blank=True, default='')
    warning = models.TextField(blank=True, default='')
    detail = models.TextField(blank=True, default='')
    fields = models.ManyToManyField(Field, through='PageField')

    def __str__(self):
        return self.heading


class PageField(models.Model):
    page = models.ForeignKey(Page)
    field = models.ForeignKey(Field)
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ['number']


class Section(models.Model):
    section = models.AutoField(primary_key=True)
    heading = models.TextField(blank=True, default='')
    guidance = models.TextField(blank=True, default='')
    pages = models.ManyToManyField(Page, through='SectionPage')

    def __str__(self):
        return self.heading


class SectionPage(models.Model):
    section = models.ForeignKey(Section)
    page = models.ForeignKey(Page)
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ['number']


class Form(models.Model):
    form = models.AutoField(primary_key=True)
    heading = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    phase = models.ForeignKey(Phase, default='alpha')
    reference = models.CharField(max_length=32, blank=True, default='')
    organisations = models.ManyToManyField(Organisation)
    sections = models.ManyToManyField(Section, through='FormSection')


class FormSection(models.Model):
    form = models.ForeignKey(Form)
    section = models.ForeignKey(Section)
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ['number']
