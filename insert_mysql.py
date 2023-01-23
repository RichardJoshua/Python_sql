import pymysql

from bd import conexion1

try:
	# conexion = pymysql.connect(host='localhost',
    #                          user='root',
    #                          password='',
    #                          db='peliculas')
    
	try:
		with conexion1.cursor() as cursor:
			consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
			#Podemos llamar muchas veces a .execute con datos distintos
			cursor.execute(consulta, ("Volver al futuro 1", 1985))
			cursor.execute(consulta, ("Ready Player One", 2018))
			cursor.execute(consulta, ("It", 2017))
			cursor.execute(consulta, ("Pulp Fiction", 1994))
		conexion1.commit()
	finally:
		conexion1.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)