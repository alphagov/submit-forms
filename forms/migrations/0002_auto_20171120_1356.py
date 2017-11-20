# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-20 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('datatype', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='FieldGroup',
            fields=[
                ('fieldgroup', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='FieldGroupField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('fieldtype', models.CharField(default='', max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('description', models.TextField(blank=True, default='')),
                ('datatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.DataType')),
            ],
        ),
        migrations.CreateModel(
            name='InputType',
            fields=[
                ('inputtype', models.CharField(blank=True, default='', max_length=256, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('description', models.TextField(blank=True, default='')),
                ('datatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.DataType')),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('text', models.TextField(blank=True, default='')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.List')),
            ],
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('validation', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('description', models.TextField(blank=True, default='')),
                ('min_length', models.PositiveIntegerField(default=0)),
                ('max_length', models.PositiveIntegerField(blank=True, default='')),
                ('regex', models.CharField(blank=True, default='', max_length=512)),
            ],
        ),
        migrations.RemoveField(
            model_name='field',
            name='max_length',
        ),
        migrations.RemoveField(
            model_name='field',
            name='min_length',
        ),
        migrations.RemoveField(
            model_name='field',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='field',
            name='regex',
        ),
        migrations.RemoveField(
            model_name='question',
            name='field',
        ),
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='form',
            name='reference',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='max_length',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='question',
            name='min_length',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Pattern',
        ),
        migrations.AddField(
            model_name='fieldtype',
            name='inputtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.InputType'),
        ),
        migrations.AddField(
            model_name='fieldtype',
            name='validation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Validation'),
        ),
        migrations.AddField(
            model_name='fieldgroupfield',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Field'),
        ),
        migrations.AddField(
            model_name='fieldgroupfield',
            name='fieldgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.FieldGroup'),
        ),
        migrations.AddField(
            model_name='question',
            name='fieldgroup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='forms.FieldGroup'),
        ),
    ]
