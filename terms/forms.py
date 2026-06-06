from django.forms import ModelForm
from .models import Term


class TermForm(ModelForm):
    class Meta:
        model = Term
        fields = ['categories', 'short', 'long', 'description']
