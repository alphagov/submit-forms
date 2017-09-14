from django.db import models
from django.utils.translation import ugettext_lazy as _


class Organisation(models.Model):
    organisation = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=256)
    website = models.CharField(max_length=256)

    def __str__(self):
       return self.organisation + " " + self.name


class Form(models.Model):
    form = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    organisations = models.ManyToManyField(Organisation)
