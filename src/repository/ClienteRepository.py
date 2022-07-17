from .Config import Config
from .Query import Query
import psycopg2

class ClienteRepository(object):
    
    
    
    def __init__(self):
       self.cursor=None
       self.conx =  psycopg2.connect(dbname=Config.PSQL_DB.value, 
                                    user=Config.PSQL_USER.value, 
                                    password=Config.PSQL_PASS.value, 
                                    host=Config.PSQL_HOST.value, 
                                    port=Config.PSQL_PORT.value)
       
    
    def close_conx(self):
        self.conx.close()
        self.cursor.close()

    
    def exec_select(self, query: str):
        self.cursor = self.conx.cursor()
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        #self.close_conx()
        return res 
        
        
    def get_all(self)-> tuple:
        return self.exec_select(Query.SQL_GET_ALL_CLIENTES.value)
        
    
    def find_by_id(self, id: int):
        return self.exec_select(Query.SQL_GET_CLIENTE_BY_ID.value+'{}'.format(id) )
   
    
    def search__by_param(self, param):
        pass