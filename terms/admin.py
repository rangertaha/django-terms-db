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
    list_display = ('name', )
    search_fields = ('name', )
    #raw_id_fields = ('parent',)


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('short', 'long', 'description')
    search_fields = ('short', 'long', 'description')
    raw_id_fields = ('categories',)

