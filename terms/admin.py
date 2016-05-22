# -*- coding: utf-8 -*-
"""
"""
import logging

from django.contrib import admin

from .models import Term, Category

# Get an instance of a logger
logger = logging.getLogger(__name__)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('rank', 'code', 'title', 'description')
    search_fields = ('rank', 'code', 'title', 'code', 'description')

