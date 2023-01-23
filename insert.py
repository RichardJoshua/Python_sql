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
        consulta = "INSERT INTO Tanques(Tank) VALUES (?);"
        # Podemos llamar muchas veces a .execute con datos distintos
        cursor.execute(consulta, (1985))
        cursor.execute(consulta, (1994))
        cursor.execute(consulta, (2017))
        cursor.execute(consulta, (2018))
        cursor.execute(consulta, (2019))


except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()