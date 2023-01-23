import pymysql

from db_mysql import conexion1

try:
	# conexion1 = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='',
    #                          db='peliculas')
	try:
		with conexion1.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
            # cursor.execute("SELECT * FROM Italgas;") 
			cursor.execute("select * from u454095589_tecontrol.tk_1;")                
            

			# Con fetchall traemos todas las filas
			datos = cursor.fetchall()
 
			# Recorrer e imprimir
			for dato in datos:
				print(dato)
	finally:
		conexion1.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)