import redis

class ListaTareas:
    def __init__(self):
        try:
            self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)
            self.r.flushdb()
        except redis.ConnectionError:
            print("Error: No se pudo conectar a Redis. Asegúrate de que el servidor esté en funcionamiento.")
            self.r = None

    def añadir_tarea(self, usuario, tarea):
        self.r.lpush(f"listaTareas:{usuario}", tarea)
    def leer_tareas(self, usuario):
        return self.r.lrange(f"listaTareas:{usuario}", 0, -1)

if __name__ == "__main__":
	lista = ListaTareas()
	if lista.r:
		lista.añadir_tarea(1, "Comprar leche")
		lista.añadir_tarea(1, "Llamar a mamá")
		print("El usuario 1 tiene las siguientes tareas:")
		print(lista.leer_tareas(1))