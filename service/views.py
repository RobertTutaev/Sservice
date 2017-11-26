from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def index(request):
    view = "index"
    return render(request, 'index.html', {'name': view})

def about(request):
    view = "index"
    return render(request, 'about.html', {'name': view})
