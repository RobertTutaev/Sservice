from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from service.models import SDb, SQuery, SPage, SUserService, SService
from service.dbs import Query
from api.resp import Resp

def index(request):
    resp = Resp()
    resp.resp['data'] = [
        {'is_authenticated':    {'type_query': 'GET',       'url': '/api/authenticated',   'input_values': None,               'output_values': 'boolean'}},
        {'get_services':        {'type_query': 'GET',       'url': '/api/services',        'input_values': None,               'output_values': '[ { id (integer), name (string) } ]'}},
        {'get_databases':       {'type_query': 'GET',       'url': '/api/databases/:id',   'input_values': 'id (integer)',     'output_values': '[ { id (integer), name (string) } ]'}},
    ]
    return resp.getJsonResponse()

def authenticated(request):
    resp = Resp()
    resp.resp['data'] = request.user.is_authenticated()
    return resp.getJsonResponse()

@login_required
def services(request):
    try:
        resp = Resp()
        sServices = SService.objects.values('id', 'name').filter(suserservice__user=request.user)
        resp.resp['data'] = list(sServices)
    except BaseException as e:
        resp.resp['status'] = 500
        resp.resp['rslt'] = False
        resp.resp['msg'] =  e.message
    finally:
        return resp.getJsonResponse()

@login_required
def databases(request, id):
    try:
        resp = Resp()
        sService = SService.objects.values('id', 'name').filter(pk=id, suserservice__user=request.user).first()
        sDbs = SDb.objects.values('id', 'name').filter(sservicedb__s_service = sService)
        resp.resp['data'] = list(sDbs)
    except BaseException as e:
        resp.resp['status'] = 500
        resp.resp['rslt'] = False
        resp.resp['msg'] =  e.message
    finally:
        return resp.getJsonResponse()

@login_required
def service(request, id, db, snils):    
    try:        
        resp = Resp()
        service = SService.objects.filter(pk=id, suserservice__user=request.user).first()
        query = Query(service, db, snils)
        resp.resp['data'] = list(query.getData())
    except BaseException as e:
        resp.resp['status'] = 500
        resp.resp['rslt'] = False
        resp.resp['msg'] =  e.message
    finally:
        return resp.getJsonResponse()


