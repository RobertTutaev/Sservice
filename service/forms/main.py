from django import forms
from service.models import Article

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)