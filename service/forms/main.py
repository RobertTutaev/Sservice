from django import forms

class ServiceForm(forms.Form):
    snils = forms.CharField(label='СНИЛС', max_length=100)