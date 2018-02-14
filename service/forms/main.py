from django import forms
from django.core.validators import RegexValidator

from service.models import SDb

class ServiceForm(forms.Form, request):
    snils = forms.CharField(label='СНИЛС', max_length=100, validators=[RegexValidator(r"^\d{3}-\d{3}-\d{3} \d{2}$", "Введите корректный СНИЛС в формате 'XXX-XXX-XXX XX'")])
    db = forms.ModelChoiceField(label='БД', queryset=SDb.objects.filter(sservicedb__suserservice__user=request.user))