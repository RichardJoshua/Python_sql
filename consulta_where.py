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

        consulta = "SELECT id, titulo, anio FROM peliculas WHERE anio > ?;"
        cursor.execute(consulta, (2000))

        # Con fetchall traemos todas las filas
        peliculas = cursor.fetchall()

        # Recorrer e imprimir
        for pelicula in peliculas:
            print(pelicula)
except Exception as e:
    print("Ocurrió un error al consultar con where: ", e)
finally:
    conexion.close()