import pyodbc
from service.models import SDb, SQuery

class Query:

    def __init__(self, sDb: SDb):
        cnxn = pyodbc.connect(sDb.connect)        
        self.cursor = cnxn.cursor()

    def _bool(self, value):
        try:
            return bool(value)
        except ValueError:
            return False

    def _bool_val(self, value, compare_value):
        try:
            return int(value) == int(compare_value)
        except ValueError:
            return False

    def execSQLs(self, sQuery: SQuery, *args):
        self.cursor.execute(sQuery.script, *args)

        result = {
        # Возвращается строка из выборки (одна)
        1: lambda: self.cursor.fetchone(),
        # Возвращаются строки из выборки (все)
        2: lambda: self.cursor.fetchall(),
        # Возвращается ответ, если в первом поле выборки значение >0, иначе далее
        3: lambda: self._bool( self.cursor.fetchone()[0] ),
        # Возвращается ответ, если в первом поле выборки значение =0, иначе далее
        4: lambda: self._bool_val( self.cursor.fetchone()[0], 0 ),
        # Возвращается ответ, если в первом поле выборки значение =1, иначе далее
        5: lambda: self._bool_val( self.cursor.fetchone()[0], 1 ),
        # Возвращается ответ, если записей в выборке >0, иначе далее
        6: lambda: len( self.cursor.fetchall() ) > 0,
        # Возвращается ответ, если записей в выборке =0, иначе далее
        7: lambda: len( self.cursor.fetchall() ) == 0,
        # Возвращается ответ, если записей в выборке =1, иначе далее
        8: lambda: len( self.cursor.fetchall() ) == 1
        }[sQuery.s_type.id]()

        return result