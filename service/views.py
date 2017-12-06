from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import Context
from django.contrib.auth.decorators import login_required

from service.models import SPage, SUserService, SService

# Create your views here.

def index(request):
    sPage = get_object_or_404(SPage, id=1)
    return render(request, 'page.html', {'page': sPage})

def about(request):
    sPage = get_object_or_404(SPage, id=2)
    return render(request, 'page.html', {'page': sPage})

def contacts(request):
    sPage = get_object_or_404(SPage, id=3)
    return render(request, 'page.html', {'page': sPage})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def services(request):    
    #sUserServices = SUserService.objects.filter(user=request.user)
    #services = SService.objects.filter(pk__in = sUserServices)

    #sUserServices = SUserService.objects.get(user=request.user)
    #services = sUserServices.sService.all()

    services = SService.objects.filter(suserservice__user=request.user)
    
    return render(request, 'services.html', {'services': services})