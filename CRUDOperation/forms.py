from django import forms
from django.forms import fields
from CRUDOperation.models import CusModel, EmpModel

class empForms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields="__all__"

class cusForms(forms.ModelForm):
    class Meta:
        model=CusModel
        fields="__all__"


