from typing import MutableMapping, Any

from django import forms

from django.forms.renderers import BaseRenderer


from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'auth-field__input {existing}'.strip()
