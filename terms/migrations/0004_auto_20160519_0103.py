# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20160519_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='slug',
            field=models.SlugField(blank=True, max_length=512, null=True, unique=True),
        ),
    ]
