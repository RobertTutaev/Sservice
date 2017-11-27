from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from service.models import SPage

# Create your views here.

def index(request):
    sPage = get_object_or_404(SPage, id=1)
    print(sPage)
    return render(request, 'page.html', {'page': sPage})

def about(request):
    sPage = get_object_or_404(SPage, id=2)
    return render(request, 'page.html', {'page': sPage})
