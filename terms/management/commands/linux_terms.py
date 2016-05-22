# -*- coding:utf-8 -*-
"""

"""
import json
import datetime
import subprocess

from django.template.loader import get_template
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Backup each app's data with the dumpdata command"

    def handle(self, *args, **options):
        pass
