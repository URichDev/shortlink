from django import forms
from django.forms import ModelForm

from .models import ShortLink

class ShortLinkForm(ModelForm):
    class Meta:
        model = ShortLink
        fields = ('long_link',)
