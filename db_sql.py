import pymssql


# direccion_servidor = 'DESKTOP-C5OPVAC\MSSQLSERVER1'     #'127.0.0.1'
# nombre_bd = ''              #'pruebas_parzibyte'
# nombre_usuario = ''
# password = ''

query = "SELECT * FROM italgas"
conn = pymssql.connect('DESKTOP-C5OPVAC\MSSQLSERVER1', 'sa', 'pass', 'nomb_tb')
cursor = conn.cursor(as_dict=True)
cursor.execute(query)
for row in cursor:
    print(row)
conn.close()



# --------------------------------------------
# spy_conn = pyodbc.connect(
#             "DRIVER={ODBC Driver 13 for SQL Server};"
#             "SERVER = SNMXLAP187\SQLEXPRESS;"
#             "DATABASE = prueba;"
#             "Trusted_Connection = yes;")


