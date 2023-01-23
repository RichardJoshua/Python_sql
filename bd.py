"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    
    @author parzibyte
    Más tutoriales en:

https://parzibyte.me/blog/2019/06/14/conexion-sql-server-python-pyodbc-crud/#Instalacion_de_PyODBC
                        
"""
import pyodbc

# spy_conn = pyodbc.connect(
#             "DRIVER={ODBC Driver 13 for SQL Server};"
#             "SERVER = SNMXLAP187\SQLEXPRESS;"
#             "DATABASE = prueba;"
#             "Trusted_Connection = yes;")


# ----- otro ------------------------
# "DRIVER={SQL Server};" 
# "SERVER=SNMXLAP187\SQLEXPRESS;"
# "DATABASE=prueba;"
# "Trusted_Connection=yes;")


direccion_servidor = 'DESKTOP-C5OPVAC\MSSQLSERVER1'     #'127.0.0.1'
nombre_bd = 'italgas'              #'pruebas_parzibyte'
nombre_usuario = 'sa'
password = 'pass'
try:
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # conexion = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("OK! conexión exitosa")
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
