# -*- coding:utf-8 -*-
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_alphabet():
    for a in ALPHABET:
        for b in ALPHABET:
            yield a+b

ALPHABET_CHOICES = tuple((a, a) for a in get_alphabet())


class Category(models.Model):
    slug = models.SlugField(max_length=32, unique=True, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Term(models.Model):
    alphabet = models.CharField(max_length=4, blank=True, null=True, choices=ALPHABET_CHOICES)
    rank = models.IntegerField(blank=True, null=True, default=0)
    slug = models.SlugField(max_length=512, unique=False, blank=True, null=True)
    short = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    long = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True, null=True, related_name='terms')

    # Metadata
    created = models.DateTimeField(_('Created'), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_('Updated'), auto_now=False, auto_now_add=True)
    active = models.BooleanField(_('Active'), default=False)

    class Meta:
        ordering = ('rank',)

    def __unicode__(self):
        return self.long


@receiver(pre_save, sender=Term)
def pre_term(sender, **kwargs):
    term = kwargs['instance']
    if not term.slug:
        term.slug = slugify(term.long)



@receiver(pre_save, sender=Category)
def slugify_category_name(sender, **kwargs):
    category = kwargs['instance']
    if not category.slug:
        category.slug = slugify(category.name)
