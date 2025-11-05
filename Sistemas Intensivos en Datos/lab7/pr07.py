import pymongo
from pymongo import MongoClient
from datetime import datetime
import pprint

pp = pprint.PrettyPrinter(indent=2)

"""

import pprint

pp = pprint.PrettyPrinter(indent=2)

pp.print(resultado)

"""


def crear_conexion():
    client = MongoClient("mongodb://admin:admin@localhost:27017/")
    db = client["pr07"]
    db.categorias.drop()
    db.estudiantes.drop()
    db.libros.drop()
    db.prestamos.drop()
    return client, db


def insertar_categorias(db):
    categorias = [
        {
            "_id": 1,
            "nombre": "Ciencia Ficción",
            "descripcion": "Novelas de ciencia ficción y fantasía",
            "libros_count": 0,
            "ubicacion": "Ala A"
        },
        {
            "_id": 2,
            "nombre": "Literatura Clásica", 
            "descripcion": "Obras clásicas de la literatura universal",
            "libros_count": 0,
            "ubicacion": "Ala B"
        },
        {
            "_id": 3,
            "nombre": "Tecnología",
            "descripcion": "Libros de programación y tecnología",
            "libros_count": 0,
            "ubicacion": "Ala C"
        },
        {
            "_id": 4,
            "nombre": "Ciencias Sociales",
            "descripcion": "Sociología, psicología y antropología",
            "libros_count": 0,
            "ubicacion": "Ala D"
        }
    ]
    db.categorias.insert_many(categorias)


def insertar_estudiantes(db):
    estudiantes = [
        {
            "nombre": "Ana García López",
            "email": "ana.garcia@universidad.edu",
            "carrera": "Ingeniería Informática",
            "semestre": 5,
            "edad": 21,
            "ciudad": "Madrid",
            "fecha_registro": datetime(2022, 9, 1),
            "activo": True
        },
        {
            "nombre": "Carlos Rodríguez Martín",
            "email": "carlos.rodriguez@universidad.edu", 
            "carrera": "Literatura",
            "semestre": 3,
            "edad": 20,
            "ciudad": "Barcelona",
            "fecha_registro": datetime(2023, 1, 15),
            "activo": True
        },
        {
            "nombre": "María Chen Wang",
            "email": "maria.chen@universidad.edu",
            "carrera": "Psicología", 
            "semestre": 7,
            "edad": 23,
            "ciudad": "Valencia",
            "fecha_registro": datetime(2021, 9, 1),
            "activo": True
        },
        {
            "nombre": "David Martínez Ruiz",
            "email": "david.martinez@universidad.edu",
            "carrera": "Ingeniería Informática",
            "semestre": 6,
            "edad": 22,
            "ciudad": "Madrid",
            "fecha_registro": datetime(2022, 2, 1),
            "activo": False
        }
    ]
    db.estudiantes.insert_many(estudiantes)


def insertar_libros(db):
    libros = [
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "genero": "Ciencia Ficción",
            "año_publicacion": 1949,
            "isbn": "978-0451524935",
            "editorial": "Signet Classics",
            "paginas": 328,
            "precio": 12.99,
            "stock": 5,
            "disponible": True,
            "tags": ["distopía", "política", "clásico"],
            "fecha_ingreso": datetime(2023, 1, 15),
            "categoria_id": 1
        },
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez", 
            "genero": "Realismo Mágico",
            "año_publicacion": 1967,
            "isbn": "978-0307474728",
            "editorial": "Penguin Random House",
            "paginas": 417,
            "precio": 15.50,
            "stock": 3,
            "disponible": True,
            "tags": ["realismo mágico", "latinoamericano", "clásico"],
            "fecha_ingreso": datetime(2023, 2, 20),
            "categoria_id": 2
        },
        {
            "titulo": "Python Crash Course",
            "autor": "Eric Matthes",
            "genero": "Programación",
            "año_publicacion": 2019,
            "isbn": "978-1593279288",
            "editorial": "No Starch Press",
            "paginas": 544,
            "precio": 39.99,
            "stock": 8,
            "disponible": True,
            "tags": ["python", "programación", "aprendizaje"],
            "fecha_ingreso": datetime(2023, 3, 10),
            "categoria_id": 3
        },
        {
            "titulo": "El Principito",
            "autor": "Antoine de Saint-Exupéry",
            "genero": "Literatura Infantil",
            "año_publicacion": 1943,
            "isbn": "978-0156012195",
            "editorial": "Harcourt Brace",
            "paginas": 96,
            "precio": 9.99,
            "stock": 0,
            "disponible": False,
            "tags": ["infantil", "filosofía", "clásico"],
            "fecha_ingreso": datetime(2023, 1, 5),
            "categoria_id": 2
        },
        {
            "titulo": "Clean Code",
            "autor": "Robert C. Martin",
            "genero": "Programación",
            "año_publicacion": 2008,
            "isbn": "978-0132350884",
            "editorial": "Prentice Hall",
            "paginas": 464,
            "precio": 47.99,
            "stock": 6,
            "disponible": True,
            "tags": ["programación", "calidad", "best practices"],
            "fecha_ingreso": datetime(2023, 4, 15),
            "categoria_id": 3
        }
    ]
    db.libros.insert_many(libros)


def insertar_prestamos(db):
    # Obtenemos los IDs que necesitamos
    libro_1984 = db.libros.find_one({"titulo": "1984"})
    libro_python = db.libros.find_one({"titulo": "Python Crash Course"})
    estudiante_ana = db.estudiantes.find_one({"email": "ana.garcia@universidad.edu"})
    estudiante_carlos = db.estudiantes.find_one({"email": "carlos.rodriguez@universidad.edu"})
    
    prestamos = [
        {
            "libro_id": libro_1984["_id"],
            "estudiante_id": estudiante_ana["_id"],
            "fecha_prestamo": datetime(2024, 1, 10),
            "fecha_devolucion": datetime(2024, 1, 24),
            "fecha_devolucion_real": None,
            "estado": "activo",
            "multa": 0
        },
        {
            "libro_id": libro_python["_id"],
            "estudiante_id": estudiante_carlos["_id"],
            "fecha_prestamo": datetime(2024, 1, 5),
            "fecha_devolucion": datetime(2024, 1, 19),
            "fecha_devolucion_real": datetime(2024, 1, 18),
            "estado": "devuelto",
            "multa": 0
        }
    ]
    db.prestamos.insert_many(prestamos)

def ejercicio1_actualizarStock(db):
    print("\nEjercicio 1 - Actualizar Stock")
    resultado1 = list(db.libros.find({"titulo": "1984"}))
    db.libros.update_many({"titulo": "1984"}, {"$inc": {"stock": -3}})
    resultado2 = list(db.libros.find({"titulo": "1984"}))
    
    print("Antes del cambio")
    for libro in resultado1:
        print(libro["titulo"] + " - " + "Stock: " + str(libro["stock"]))
        
    print("Despues del cambio")
    for libro in resultado2:
        print(libro["titulo"] + " - " + "Stock: " + str(libro["stock"]))

def ejercicio2_descuento(db):
    print("\nEjercicio 2 - Añadir Descuento")
    db.libros.update_many({"año_publicacion": {"$lt": 2000}},{"$set": {"descuento": "Descuento 15%"}})
    
    resultado = db.libros.find()
    
    for libro in resultado:
        if "descuento" in libro:
            print(libro["titulo"] + " - " + "Año: " + str(libro["año_publicacion"]) + " Descuento: " + libro["descuento"])
        elif "descuento" not in libro:
            print(libro["titulo"] + " - " + "Año: " + str(libro["año_publicacion"]))

def ejercicio3_actualizar_o_crear_categoria(db):
    print("\nEjercicio 3 - Upsert Categoría")
    resultado = db.categorias.update_one(
        {"nombre": "Matemáticas"}, 
        {
            "$set": {
                "ubicacion": "Ala E"
            },
            "$setOnInsert": { # Solo si se crea
                "descripcion": "Libros de matemáticas y cálculo",
                "libros_count": 0
            }
        },
        upsert=True
    )

def ejercicio4_librosPrestamosDisponibles(db):
    print("\nEjercicio 4 - Libros Prestados")
    prestamos = list(db.prestamos.find({}))
    
    ids_libros_prestados = [prestamo["libro_id"] for prestamo in prestamos]

    libros = db.libros.find({"_id": {"$in": ids_libros_prestados}})
    
    print("Libros que tienen préstamos:")
    for libro in libros:
        print(f"  - {libro['titulo']} (ID: {libro['_id']})")

def ej5_estudiantesInformatica(db):
    print("\nEjercicio 5 - Estudiantes Informática")
    resultado = list(db.estudiantes.find({"carrera": "Ingeniería Informática"}))
    
    if resultado:
        print(f"Se encontraron {len(resultado)} estudiante(s) de Ingeniería Informática:")
        for estudiante in resultado:
            print(f"  • {estudiante['nombre']} - Semestre: {estudiante['semestre']}, Edad: {estudiante['edad']}")
    else:
        print("No se encontraron estudiantes de Ingeniería Informática")
        
def ej6_libroMas20(db):
    print("\nEjercicio 6 - Libros Precio>20")
    resultado = db.libros.find({"precio": {"$gt": 20}})
    
    for libro in resultado:
        print(f"Libro: {libro['titulo']} (Precio: {libro['precio']})")
        
def ej7_estadisticas(db):
    print("\nEjercicio 7 - Estadísticas Género")
    pipeline = [
        {"$match": {"stock": {"$gt": 0}}},
        {"$group": {
			"_id": "$genero",
			"total_libros": {"$sum": 1},
			"stock_total": {"$sum": "$stock"},
			"precio_promedio": {"$avg": "$precio"},
			"lista_libros": {"$push": "$titulo"}
		},
	}, {"$sort": {"total_libros": -1}},]
    
    resultado = db.libros.aggregate(pipeline)
    
    for genero in resultado:
        print(f"\n- Género: {genero['_id']}")
        print(f"   • Total libros: {genero['total_libros']}")
        print(f"   • Stock total: {genero['stock_total']}")
        print(f"   • Precio promedio: {genero['precio_promedio']:.2f}€")
        print(f"   • Libros: {', '.join(genero['lista_libros'])}")


def ej8_intervalosPrecio(db):
    print("\nEjercicio 8 - Intervalos Precio")
    pipeline = [
        {
            "$bucket": {
                "groupBy": "$precio",
                "boundaries": [0, 10, 20, 30, 50],
                "default": "Out of bounds",
                "output": {
                    "cantidad_libros": {"$sum": 1},
                    "precio_promedio": {"$avg": "$precio"},
                    "libros": {"$push": "$titulo"}
                }
            }
        }
    ]
    
    resultado = db.libros.aggregate(pipeline)
    
    # Mapeo de límites a rangos legibles
    rangos_nombres = {
        0: "0-10€",
        10: "10-20€",
        20: "20-30€",
        30: "30-50€",
        "Out of bounds": "Más de 50€"
    }
    
    for rango in resultado:
        nombre_rango = rangos_nombres.get(rango['_id'])
        print(f"\nRango: {nombre_rango}")
        print(f"  Cantidad de libros: {rango['cantidad_libros']}")
        print(f"  Precio promedio: {rango['precio_promedio']:.2f}€")
        print(f"  Libros: {', '.join(rango['libros'])}")
    
    
def ej9_combinarPrestamosLibrosEstudiantes(db):
    print("\nEjercicio 9 - Reporte Préstamos")
    pipeline = [
		{
			# Unimos con estudiantes
			"$lookup": {
				"from": "estudiantes",
				"localField": "estudiante_id",
				"foreignField": "_id",
				"as": "info_estudiante"
			}
		},
        {
            # Unimos con libros
            "$lookup": {
                "from": "libros",
                "localField": "libro_id",
                "foreignField": "_id",
                "as": "info_libro"
            }
        },
        # Descomponer los arrays resultantes
        {
            "$unwind": "$info_estudiante"
        },
        {
            "$unwind": "$info_libro"
		},
        {
			"$project": {
				"_id": 0,
				"nombre_estudiante": "$info_estudiante.nombre",
				"titulo_libro":"$info_libro.titulo",
				"fecha_prestamo": 1,
				"fecha_devolucion": 1,
				"estado": 1,
				"carrera": "$info_estudiante.carrera",
			}
		},
        {
			"$sort": {"fecha_prestamo": -1}
		}
	]

    resultado = db.prestamos.aggregate(pipeline)
    
    for prestamo in resultado:
        print(f"\n- Préstamo:")
        print(f"   • Estudiante: {prestamo['nombre_estudiante']}")
        print(f"   • Carrera: {prestamo['carrera']}")
        print(f"   • Libro: {prestamo['titulo_libro']}")
        print(f"   • Fecha préstamo: {prestamo['fecha_prestamo'].strftime('%d/%m/%Y')}")
        print(f"   • Fecha devolución prevista: {prestamo['fecha_devolucion'].strftime('%d/%m/%Y')}")
        print(f"   • Estado: {prestamo['estado'].upper()}")


def ej10_estadisticasPorCiudad(db):
    print("\nEjercicio 10 - Estadísticas Ciudad")
    pipeline = [
		{
			"$match": {"activo": True}
		},
		{
			"$group": {
				"_id" : "$ciudad",
				"total_estudiantes": {"$sum": 1},
				"promedio_edad": {"$avg": "$edad"},
				"lista_estudiantes": {"$push": "$nombre"},
				"lista_carreras": {"$addToSet": "$carrera"}
			}
		},
		{
			"$sort": {"total_estudiantes": -1}
		}
	]
	
    resultado = db.estudiantes.aggregate(pipeline)


    for ciudad in resultado:
        print(f"\n-  Ciudad: {ciudad['_id']}")
        print(f"   • Total estudiantes: {ciudad['total_estudiantes']}")
        print(f"   • Promedio de edad: {ciudad['promedio_edad']:.1f} años")
        print(f"   • Carreras únicas: {', '.join(ciudad['lista_carreras'])}")
        print(f"   • Estudiantes: {', '.join(ciudad['lista_estudiantes'])}")
        
def ej11_estudianteInactivo(db):
    print("\nEjercicio 11 - Estudiante Inactivo")
    estudiante = {
        "nombre": "Carlos Rodríguez Martín",
        "email": "carlos.rodriguez@universidad.edu", 
        "carrera": "Literatura",
        "semestre": 3,
        "edad": 20,
        "ciudad": "Barcelona",
        "fecha_registro": datetime(2023, 1, 15),
        "activo": False
	}
    
    print("Insertando estudiante inactivo...")
    resultado = db.estudiantes.insert_one(estudiante)
    print(f"- Estudiante insertado con ID: {resultado.inserted_id}")
    
    print("Eliminando estudiante recién insertado...")
    db.estudiantes.delete_one({"_id": resultado.inserted_id})
    print(f"-  Estudiante con ID {resultado.inserted_id} eliminado")

def ej12_operacionesProgramacion(db):
    print("\nEjercicio 12 - Actualizar Programación")
    resultado = db.libros.update_many(
        {"genero": "Programación"},
        {
            "$set": {
                "ubicacion": "Sala de ordenadores",
                "etiqueta_especial": "Tecnología"
            }
        }
    )
    
    print(f"- Libros actualizados: {resultado.modified_count}")
    
    # Mostrar los libros actualizados
    libros_actualizados = db.libros.find({"genero": "Programación"})
    
    print("\nLibros de Programación actualizados:")
    for libro in libros_actualizados:
        print(f"  - {libro['titulo']}")
        print(f"     • Ubicación: {libro.get('ubicacion', 'No definida')}")
        print(f"     • Etiqueta especial: {libro.get('etiqueta_especial', 'No definida')}")

if __name__ == "__main__":
    try:
        client, db = crear_conexion()
        insertar_categorias(db)
        insertar_estudiantes(db)
        insertar_libros(db)
        insertar_prestamos(db)
        
        
        ejercicio1_actualizarStock(db)
        ejercicio2_descuento(db)
        ejercicio3_actualizar_o_crear_categoria(db)
        ejercicio4_librosPrestamosDisponibles(db)
        ej5_estudiantesInformatica(db)
        ej6_libroMas20(db)
        ej7_estadisticas(db)
        ej8_intervalosPrecio(db)
        ej9_combinarPrestamosLibrosEstudiantes(db)
        ej10_estadisticasPorCiudad(db)
        ej11_estudianteInactivo(db)
        ej12_operacionesProgramacion(db)



    except Exception as e:
        print("Error al insertar documentos:", e)
    finally:
        client.close()
