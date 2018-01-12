import pyodbc
from service.models import SDb, SQuery

class Query:

    def __init__(self, sDb: SDb):        
        cnxn = pyodbc.connect(sDb.connect)
        self.cursor = cnxn.cursor()

    def execSQL(self, sQuery: SQuery, *args):
        self.cursor.execute(sQuery.script, *args)
        row = self.cursor.fetchone()
        if row:
            print(row)