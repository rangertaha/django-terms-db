# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='System',
        ),
    ]
