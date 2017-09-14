# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('form', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('organisation', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('website', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='organisations',
            field=models.ManyToManyField(to='forms.Organisation'),
        ),
    ]
