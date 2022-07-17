from cmath import e
import enum

class Query(enum.Enum):
    SQL_GET_ALL_CLIENTES = 'select * from "TBLS_LOG_PROCESOS"'
    SQL_GET_CLIENTE_BY_ID = 'select * from "TBLS_LOG_PROCESOS" WHERE id='
    