from django import forms
from .models import Trackin


class Traking_forms(forms.ModelForm):
    class Meta:
        model = Trackin
        fields = ['name', 'serial_number', 'value']