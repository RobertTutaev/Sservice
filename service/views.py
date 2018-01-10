from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import Context
from django.contrib.auth.decorators import login_required

from service.models import SPage, SUserService, SService
from service.forms.main import ServiceForm

# Create your views here.

def index(request):
    sPage = get_object_or_404(SPage, id=1)

    if request.user.is_authenticated():
        services = SService.objects.filter(suserservice__user=request.user)
    else:
        services = SService.objects.none()
    
    return render(request, 'page.html', {'page': sPage, 'services': services})

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

@login_required
def service(request, id):
    service = SService.objects.filter(pk=id, suserservice__user=request.user).first()
    form = ServiceForm()
    
    return render(request, 'service.html', {'service': service, 'form': form})