# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-06 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20171205_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
