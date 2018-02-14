from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from service.models import SDb, SQuery, SPage, SUserService, SService
from service.forms.main import ServiceForm
from service.dbs import Query

def index(request):
    sPage = get_object_or_404(SPage, id=1)

    if request.user.is_authenticated():
        services = SService.objects.filter(suserservice__user=request.user, checked=True)
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
    services = SService.objects.filter(suserservice__user=request.user, checked=True)
    
    return render(request, 'services.html', {'services': services})

@login_required
def service(request, id):
    result = ''
    service = SService.objects.filter(pk=id, suserservice__user=request.user).first()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ServiceForm(request.POST)
        # check whether it's valid:
        if form.is_valid() and service:
            query = Query(SDb.objects.filter(sservicedb__pk=1).first())
            result = query.execSQLs(SQuery.objects.filter(pk=1).first(), form.cleaned_data['snils'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ServiceForm(request)
    
    return render(request, 'service.html', {'service': service, 'form': form, 'result': result})