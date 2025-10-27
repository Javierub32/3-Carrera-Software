import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def crear_usuario(id, nombre, email, edad):
	r.hset(f'user:{id}', mapping={
		'name': nombre,
		"email": email,
		"age": edad
	})

def leer_datos_usuario(id):
	return r.hgetall(f'user:{id}')

def añadir_tarea(usuario, tarea):
    r.lpush(f"listaTareas:{usuario}", tarea)
    
def leer_tareas(usuario):
	return r.lrange(f"listaTareas:{usuario}", 0, -1)

def limpiar_tareas(usuario):
    r.delete(f"listaTareas:{usuario}")


if __name__ == "__main__":
    limpiar_tareas(1)
    limpiar_tareas(2)	

    crear_usuario(1, "Juan", "juan@example.com", 30)
    crear_usuario(2, "Ana", "ana@example.com", 25)

    crear_usuario(3, "Luis", "luis@example.com", 28)

    print("Datos de los usuarios:")
    print(leer_datos_usuario(1))
    print(leer_datos_usuario(2))
    print(leer_datos_usuario(3))
    print("\n")
 
    añadir_tarea(1, "Comprar leche")
    añadir_tarea(1, "Llamar a mamá")

    print("El usuario 1 tiene las siguientes tareas:")
    print(leer_tareas(1))
    
    r.close()
