import psycopg2

# Global constant
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = ""
PSQL_DB = "test"
conn = psycopg2.connect(dbname=PSQL_DB, user=PSQL_USER, password=PSQL_PASS, host=PSQL_HOST, port=PSQL_PORT)
cursor = conn.cursor()
cursor.execute('select * from "TBLS_LOG_PROCESOS"')
all = cursor.fetchall()
cursor.close()
conn.close()
print(type(all))

for a in all:
    print(a)
