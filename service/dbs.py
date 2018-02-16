import pyodbc
from service.models import SDb, SQuery

class Query:
    _cursor = None
    _result = False
    _data = str(_result)


    def _bool(self, value):
        try:
            self._result = bool(value)
        except ValueError:
            self._result = False

        self._data = str(self._result)


    def _bool_val(self, value, compare_value):
        try:
            self._result = int(value) == int(compare_value)
        except ValueError:
            self._result = False
        
        self._data = str(self._result)

    def _get_data(self, fetchall = False):
        if fetchall:            
            self._data = self._cursor.fetchall()
        else:
            self._data = self._cursor.fetchone()

        self._result = True

    def _count(self):
        self._result = len(self._cursor.fetchall()) > 0
        self._data = str(self._result)

    def _count_val(self, compare_value):
        self._result = len(self._cursor.fetchall()) == compare_value
        self._data = str(self._result)

    def _execSQLs(self, sQuery: SQuery, *args):        
        
        self._cursor.execute(sQuery.script, *args)
        
        result = {
        # Возвращается строка из выборки (одна)
        1: lambda: self._get_data(),
        # Возвращаются строки из выборки (все)
        2: lambda: self._get_data(True),
        # Возвращается ответ, если в первом поле выборки значение >0, иначе далее
        3: lambda: self._bool(self._cursor.fetchone()[0]),
        # Возвращается ответ, если в первом поле выборки значение =0, иначе далее
        4: lambda: self._bool_val(self._cursor.fetchone()[0], 0),
        # Возвращается ответ, если в первом поле выборки значение =1, иначе далее
        5: lambda: self._bool_val(self._cursor.fetchone()[0], 1),
        # Возвращается ответ, если записей в выборке >0, иначе далее
        6: lambda: self._count(),
        # Возвращается ответ, если записей в выборке =0, иначе далее
        7: lambda: self._count_val(0),
        # Возвращается ответ, если записей в выборке =1, иначе далее
        8: lambda: self._count_val(1),
        }[sQuery.s_type.id]()

    
    def __init__(self, service, idDb, *args):
        sDb = SDb.objects.get(pk=idDb)
        cnxn = pyodbc.connect(sDb.connect)        
        self._cursor = cnxn.cursor()        

        sQueries = SQuery.objects.filter(s_service = service)

        for sQuery in sQueries:
            self._execSQLs(sQuery, *args)
            if self._result:
                break


    def getData(self):
        if self._result:
            return self._data
        else:
            return self._result


    def __str__(self):
        if self._result:
            return str(self._data)
        else:
            return str(self._result)