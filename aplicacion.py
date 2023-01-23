# /*
# 	Conexión a SQLServer con Python
# 	Ejemplo de CRUD evitando inyecciones SQL
	
# 	@author parzibyte
# 	Más tutoriales en:
# 						
# */
# CREATE TABLE IF NOT EXISTS peliculas(
# 	id bigint identity(1,1) primary key,	
# 	titulo VARCHAR(255) NOT NULL,
# 	anio SMALLINT NOT NULL
# );


# --------------------- Funciona es el archivo db.py --------------------------
# """
#     Conexión a SQLServer con Python
#     Ejemplo de CRUD evitando inyecciones SQL
    
#     @author parzibyte
#     Más tutoriales en:
                        
# """
# import pyodbc
# direccion_servidor = '127.0.0.1'
# nombre_bd = 'pruebas_parzibyte'
# nombre_usuario = 'usuario'
# password = 'hunter2'
# try:
#     conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
#                               direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
#     # OK! conexión exitosa
# except Exception as e:
#     # Atrapar error
#     print("Ocurrió un error al conectar a SQL Server: ", e)

# ------------------ Insertar Datos --------------------------------

"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
    
    @author parzibyte
    Más tutoriales en:

https://parzibyte.me/blog/2019/06/14/conexion-sql-server-python-pyodbc-crud/#Instalacion_de_PyODBC

"""
from bd import conexion
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO peliculas(titulo, anio) VALUES (?, ?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, ("Volver al futuro 1", 1985))
        cursor.execute(consulta, ("Pulp Fiction", 1994))
        cursor.execute(consulta, ("It", 2017))
        cursor.execute(consulta, ("Ready Player One", 2018))
        cursor.execute(consulta, ("Spider-Man: un nuevo universo", 2018))
        cursor.execute(consulta, ("Avengers: Endgame", 2019))
        cursor.execute(consulta, ("John Wick 3: Parabellum", 2019))
        cursor.execute(consulta, ("Toy Story 4", 2019))
        cursor.execute(consulta, ("It 2", 2019))
        cursor.execute(consulta, ("Spider-Man: lejos de casa", 2019))

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()




# import _mssql

# server = 'SERVER_NAME'
# user = 'USER_NAME'
# password = '<PASSWORD>'
# database = 'MY_DATABASE'
# conn = _mssql.connect(server, user, password, database)

# # aqui creamos una tabla de ejemplo

# conn.execute_non_query('CREATE TABLE pets(id INT, name VARCHAR(100))')
# conn.execute_non_query("INSERT INTO pets VALUES(1, 'Firulais')")
# conn.execute_non_query("INSERT INTO pets VALUES(2, 'Pelusa')")

