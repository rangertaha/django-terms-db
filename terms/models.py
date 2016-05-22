# -*- coding:utf-8 -*-
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

ICONS = (
    ('fa-linux', 'Linux'),
    ('fa-windows ', 'Windows'),
    ('fa-apple', 'Apple'),

    ('fa-firefox', 'Firefox'),
    ('fa-chrome ', 'Chrome'),
    ('fa-internet-explorer', 'Internet Explorer'),

    ('fa-file', 'Physical File'),
    ('fa-file-o', 'Virtual File'),

    ('fa-folder', 'Folder'),
    ('fa-folder-o', 'Folder White'),

)


class Category(models.Model):
    slug = models.SlugField(max_length=32, unique=True, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    count = models.IntegerField(default=0)

    parent = models.ForeignKey('self', blank=True, related_name='children')

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Term(models.Model):
    rank = models.IntegerField(blank=True, null=True, default=0)
    slug = models.SlugField(max_length=512, unique=True, blank=True, null=True)
    short = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    long = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True, related_name='terms')

    # Metadata
    created = models.DateTimeField(_('Created'), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_('Updated'), auto_now=False, auto_now_add=True)
    active = models.BooleanField(_('Active'), default=False)

    class Meta:
        ordering = ('rank',)

    def __unicode__(self):
        return self.title

    def alphabet(self):
        alphabet, created = Category.objects.get_or_create(name='alphabet')
        if 0 < len(self.short) > 2:
            cat1, created = Category.objects.get_or_create(name=self.short[0], parent=alphabet)
            cat2, created = Category.objects.get_or_create(name=self.short[0], parent=alphabet)
            if cat1 not in self.categories:
                self.categories.add(cat1)
            if cat2 not in self.categories:
                self.categories.add(cat2)


@receiver(pre_save, sender=Term)
def pre_term(sender, **kwargs):
    term = kwargs['instance']
    if not term.slug:
        term.slug = slugify(term.title)


@receiver(pre_save, sender=Category)
def slugify_category_name(sender, **kwargs):
    category = kwargs['instance']
    if not category.slug:
        category.slug = slugify(category.name)
