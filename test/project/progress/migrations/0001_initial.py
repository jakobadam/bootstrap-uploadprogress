# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 16:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=512, validators=[django.core.validators.RegexValidator(re.compile(b'^[-a-zA-Z0-9_() .]+$'), b'Use ASCII characters only')], verbose_name=b'Software name')),
                ('file', models.FileField(upload_to=b'', verbose_name=b'File')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]