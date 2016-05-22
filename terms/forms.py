# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Term


class TermForm(ModelForm):
    class Meta:
        model = Term
        fields = ['categories', 'title', 'code', 'description']
