# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20160519_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='code',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]