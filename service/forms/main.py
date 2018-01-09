from django import forms

class QueryForm(forms.Form):
    snils = forms.CharField(label='СНИЛС', max_length=100)