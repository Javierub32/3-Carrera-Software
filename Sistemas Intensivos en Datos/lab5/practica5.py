import pymongo
from pymongo import MongoClient

def crear_conexion():
	client = MongoClient("mongodb://admin:admin@localhost:27017/")
	db = client["pr05"]
	return client, db

def insertar_cursos(db):
	cursos = [{
	"_id": 1,
	"nombre": "Python Básico",
	"profesor": "Ana García",
	"duracion_horas": 40,
	"nivel": "Principiante"
	},
	{
	"_id": 2, 
	"nombre": "Web Development",
	"profesor": "Carlos López",
	"duracion_horas": 60,
	"nivel": "Intermedio"
	},
	{
	"_id": 3,
	"nombre": "Data Science",
	"profesor": "María Rodríguez", 
	"duracion_horas": 80,
	"nivel": "Avanzado"
	}
	]
	db.cursos.insert_many(cursos)

def insertar_estudiantes(db):
    estudiantes = [{
	"_id": 1,
	"nombre": "Laura Martínez",
	"edad": 22,
	"email": "laura@email.com",
	"ciudad": "Madrid",
	"curso_id": 1
	},
	{
	"_id": 2,
	"nombre": "David Chen",
	"edad": 25, 
	"email": "david@email.com",
	"ciudad": "Barcelona",
	"curso_id": 2
	},
	{
	"_id": 3,
	"nombre": "Sofía Pérez",
	"edad": 20,
	"email": "sofia@email.com", 
	"ciudad": "Madrid",
	"curso_id": 1
	},
	{
	"_id": 4,
	"nombre": "Javier Ruiz",
	"edad": 28,
	"email": "javier@email.com",
	"ciudad": "Valencia", 
	"curso_id": 3
	}]
    db.estudiantes.insert_many(estudiantes)

def insertar_calificaciones(db):
	calificaciones = [{"estudiante_id": 1, "curso_id": 1, "calificacion": 8.5},
	{"estudiante_id": 2, "curso_id": 2, "calificacion": 9.0},
	{"estudiante_id": 3, "curso_id": 1, "calificacion": 7.5},
	{"estudiante_id": 4, "curso_id": 3, "calificacion": 8.0}]
	db.calificaciones.insert_many(calificaciones)

if __name__ == "__main__":
	try:
		client, db = crear_conexion()
		insertar_cursos(db)
		insertar_estudiantes(db)
		insertar_calificaciones(db)
		print("Documentos insertados correctamente.")
	except Exception as e:
		print("Error al insertar documentos:", e)
	finally:
		client.close()