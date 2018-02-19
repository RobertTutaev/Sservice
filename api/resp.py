import pyodbc, json, os
from django.http import JsonResponse

class Resp:    
    resp = None
    
    def __init__(self, file_name = 'resp.json'):
        module_dir = os.path.dirname(__file__)
        resp_path = os.path.join(module_dir, file_name)
        self.resp = json.load(open(resp_path))

    def getJsonResponse(self):
        return JsonResponse(self.resp)