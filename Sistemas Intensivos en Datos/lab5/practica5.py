import pymongo
from pymongo import MongoClient

def crear_conexion():
	client = MongoClient("mongodb://admin:admin@localhost:27017/")
	db = client["pr05"]
	db.cursos.drop()
	db.estudiantes.drop()
	db.calificaciones.drop()
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
 
def ejercicio1_consultaEstudiantes(db):
	resultados = db.estudiantes.find({}, {"_id": 0})
	print("Tipo de dato de resultados:", type(resultados))
	
	for estudiante in resultados:
		print(estudiante["nombre"] + " - " + estudiante["email"])

	listado_resultados = list(resultados)
	print("Tipo de dato de listado_resultados:", type(listado_resultados))

def consultas_madrid(db):
	resultados = db.estudiantes.find({"ciudad": "Madrid"}, {"_id": 0, "nombre": 1, "ciudad": 1})
	for estudiante in resultados:
		print(estudiante["nombre"] + " - " + estudiante["ciudad"])

def consultar_cursos_mas_50Horas(db):
	resultados = db.cursos.find({"duracion_horas": {"$gt": 50}}, {"_id": 0, "nombre": 1, "duracion_horas": 1})
	for curso in resultados:
		print(curso["nombre"] + " - " + str(curso["duracion_horas"]) + " horas")

def actualizar_edad_Laura_23(db):
	resultado = db.estudiantes.update_one({"nombre": "Laura Martínez"}, {"$set": {"edad": 23}})
	print("Documentos actualizados:" + str(resultado.modified_count))
 
def ejercicio5_actualizar_todos_estudiantes_activos(db):
	resultado = db.estudiantes.update_many({}, {"$set": {"activo": True}})
	print("Documentos actualizados:" + str(resultado.modified_count))

def ejercicio6_infoCurso_porEstudiante(db, estudiante_nombre):
	resultado = db.estudiantes.aggregate([
		{"$match": {"nombre": estudiante_nombre}},
		{"$lookup": {
			"from": "cursos",
			"localField": "curso_id",
			"foreignField": "_id",
			"as": "info_curso"
		}},
		{"$unwind": "$info_curso"},
		{"$project": {
			"_id": 0,
			"nombre_estudiante": "$nombre",
			"nombre_curso": "$info_curso.nombre",
			"profesor": "$info_curso.profesor",
			"duracion_horas": "$info_curso.duracion_horas",
			"nivel": "$info_curso.nivel"
		}}
	])
	for info in resultado:
		print(info)


if __name__ == "__main__":
	try:
		client, db = crear_conexion()
		insertar_cursos(db)
		insertar_estudiantes(db)
		insertar_calificaciones(db)

		ejercicio1_consultaEstudiantes(db)
		consultas_madrid(db)
		consultar_cursos_mas_50Horas(db)
		actualizar_edad_Laura_23(db)
		ejercicio5_actualizar_todos_estudiantes_activos(db)
		ejercicio6_infoCurso_porEstudiante(db, "Laura Martínez")
	except Exception as e:
		print("Error al insertar documentos:", e)
	finally:
		client.close()