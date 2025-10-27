import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def crear_equipo(id, nombre, ciudad, entrenador, fundacion):
	r.hset(f'equipo:{id}', mapping={
		'nombre': nombre,
		"ciudad": ciudad,
		"entrenador": entrenador,
		"fundacion": fundacion
	})

def crear_jugador(id, nombre, edad, posicion, nombre_equipo):
	r.hset(f'jugador:{id}', mapping={
		'nombre': nombre,
		"edad": edad,
		"posicion": posicion,
		"nombre_equipo": nombre_equipo
	})

def crear_partido(id, equipo_local, equipo_visitante, fecha, resultado):
	r.hset(f'partido:{id}', mapping={
		'equipo_local': equipo_local,
		'equipo_visitante': equipo_visitante,
		'fecha': fecha,
		'resultado': resultado
	})

def leer_datos_equipo(id):
	return r.hgetall(f'equipo:{id}')

def leer_datos_jugador(id):
	return r.hgetall(f'jugador:{id}')

def leer_datos_partido(id):
	return r.hgetall(f'partido:{id}')


# Ejercicio 2
def agregar_puntos_equipo(id_equipo, puntos):
    r.zadd('clasificacion:liga', {id_equipo: puntos})

def obtener_clasificacion():
    return r.zrevrange('clasificacion:liga', 0, -1, withscores=True)


# Ejercicio 4
def agregar_goles_jugador(id_jugador, goles):
	r.zadd('ranking:goleador', {id_jugador: goles})
 
def obtener_ranking_goleadores():
	return r.zrevrange('ranking:goleador', 0, -1, withscores=True)


# Ejercicio 5
def registrar_partido_cronologico(id_partido):
	r.rpush('partidos:cronologico', id_partido)

def obtener_partidos_cronologicos():
	ids_partidos = r.lrange('partidos:cronologico', 0, -1)
	partidos = []
	for id_partido in ids_partidos:
		partido = leer_datos_partido(int(id_partido))
		partidos.append((id_partido, partido))
	return partidos


# Ejercicio 10
def registrar_traspaso(id_jugador, equipo_origen, equipo_destino):
	"""Registra un traspaso en el historial de traspasos usando una lista"""
	traspaso = f"{id_jugador}|{equipo_origen}|{equipo_destino}"
	r.rpush('historial:traspasos', traspaso)

def actualizar_equipo_jugador(id_jugador, nuevo_equipo):
	r.hset(f'jugador:{id_jugador}', 'nombre_equipo', nuevo_equipo)

def obtener_historial_traspasos():
	return r.lrange('historial:traspasos', 0, -1)


if __name__ == "__main__":
    r.flushall()

	# Ejercicio 1
    crear_equipo(1, "Leones FC", "Madrid", "Carlos Ruiz", 1920)
    crear_equipo(2, "Águilas Deportivas", "Barcelona", "Ana Martínez", 1935)
    crear_equipo(3, "Tiburones FC", "Valencia", "David González", 1948)
    
    print("Equipos creados correctamente")
    print("Equipo 1:", leer_datos_equipo(1))
    print("Equipo 2:", leer_datos_equipo(2))
    print("Equipo 3:", leer_datos_equipo(3))
    print("\n")


    # Ejercicio 2
    agregar_puntos_equipo(1, 0)
    agregar_puntos_equipo(2, 0)
    agregar_puntos_equipo(3, 0)


    # Ejercicio 3
    crear_jugador(1, "Luis Torres", 25, "delantero", "Leones FC")
    crear_jugador(2, "María Rodríguez", 28, "centrocampista", "Águilas Deportivas")
    crear_jugador(3, "Javier López", 22, "defensa", "Tiburones FC")
    crear_jugador(4, "Sofía García", 26, "delantero", "Leones FC")
    
    print("Jugadores creados correctamente")
    print("Jugador 1:", leer_datos_jugador(1))
    print("Jugador 2:", leer_datos_jugador(2))
    print("Jugador 3:", leer_datos_jugador(3))
    print("Jugador 4:", leer_datos_jugador(4))
    print("\n")
    
    
    # Ejercicio 4
    agregar_goles_jugador(1, 0)
    agregar_goles_jugador(2, 0)
    agregar_goles_jugador(3, 0)
    agregar_goles_jugador(4, 0)
    
    
    # Ejercicio 5 - Registrar primeros partidos
    crear_partido(1, "Leones FC", "Águilas Deportivas", "15/10/2025", "2-1")
    crear_partido(2, "Tiburones FC", "Leones FC", "16/10/2025", "0-0")
    crear_partido(3, "Águilas Deportivas", "Tiburones FC", "17/10/2025", "3-2")
    registrar_partido_cronologico(1)
    registrar_partido_cronologico(2)
    registrar_partido_cronologico(3)
    
    
    # Ejercicio 6
    agregar_puntos_equipo(1, 4)
    agregar_puntos_equipo(3, 1)
    agregar_puntos_equipo(2, 3)
    

    # Ejercicio 7
    agregar_goles_jugador(1, 2)
    agregar_goles_jugador(2, 3)
    agregar_goles_jugador(4, 1)
    
    
    # Ejercicio 8
    crear_partido(4, "Leones FC", "Tiburones FC", "20/10/2025", "Próximo")
    crear_partido(5, "Aguilas Deportivas", "Leones FC", "25/10/2025", "Próximo")
    registrar_partido_cronologico(4)
    registrar_partido_cronologico(5)
    
    # Ejercicio 9
    print("Clasificación actualizada después de los partidos:")
    clasificacion = obtener_clasificacion()
    for posicion, (id_equipo, puntos) in enumerate(clasificacion, 1):
        equipo = leer_datos_equipo(int(id_equipo))
        print(f"{posicion}. {equipo['nombre']} - {int(puntos)} puntos")
    print("\n")
    
    print("Ranking de los tres mejores goleadores:")
    ranking = obtener_ranking_goleadores()
    for posicion, (id_jugador, goles) in enumerate(ranking, 1):
        if (posicion < 4):
            jugador = leer_datos_jugador(int(id_jugador))
            equipo_nombre = jugador['nombre_equipo']
            print(f"{posicion}. {jugador['nombre']} ({equipo_nombre}) - {int(goles)} goles")
    print("\n")
    
    print("Partidos registrados en orden cronológico:")
    partidos = obtener_partidos_cronologicos()
    for id_partido, partido in partidos:
        print(f"Partido {id_partido}: {partido['equipo_local']} {partido['resultado']} {partido['equipo_visitante']} ({partido['fecha']})")
    print("\n")
    
    
    # Ejercicio 10: Traspaso de jugador
    registrar_traspaso(4, "Leones FC", "Aguilas Deportivas")
    actualizar_equipo_jugador(4, "Aguilas Deportivas")

    print("Historial de traspasos:")
    historial = obtener_historial_traspasos()
    for traspaso in historial:
        id_jugador, equipo_origen, equipo_destino = traspaso.split('|')
        jugador = leer_datos_jugador(int(id_jugador))
        print(f"Jugador: {jugador['nombre']}, De: {equipo_origen}, A: {equipo_destino}")
    print("\n")

    r.close()
