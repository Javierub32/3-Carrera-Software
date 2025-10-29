import pymongo
from pymongo import MongoClient
from datetime import datetime

"""

import pprint

pp = pprint.PrettyPrinter(indent=2)

pp.print(resultado)

"""


def crear_conexion():
    client = MongoClient("mongodb://admin:admin@localhost:27017/")
    db = client["pr06"]
    db.clientes.drop()
    db.productos.drop()
    db.ventas.drop()
    return client, db


def insertar_clientes(db):
    clientes = [
        {
            "nombre": "Ana García",
            "email": "ana@techworld.com",
            "ciudad": "Madrid",
            "premium": True,
            "fecha_registro": datetime(2023, 12, 1),
        },
        {
            "nombre": "Carlos López",
            "email": "carlos@techworld.com",
            "ciudad": "Barcelona",
            "premium": False,
            "fecha_registro": datetime(2024, 1, 15),
        },
        {
            "nombre": "María Rodríguez",
            "email": "maria@techworld.com",
            "ciudad": "Madrid",
            "premium": True,
            "fecha_registro": datetime(2023, 11, 20),
        },
    ]
    db.clientes.insert_many(clientes)


def insertar_productos(db):
    productos = [
        {
            "_id": 1,
            "nombre": "Laptop Gaming Pro",
            "categoria": "computadoras",
            "precio": 1500,
            "stock": 8,
            "marca": "ASUS",
            "tags": ["gaming", "portatil", "rendimiento"],
            "fecha_ingreso": datetime(2024, 1, 10),
            "activo": True,
        },
        {
            "_id": 2,
            "nombre": "Smartphone Galaxy",
            "categoria": "moviles",
            "precio": 799,
            "stock": 25,
            "marca": "Samsung",
            "tags": ["android", "5G", "camara"],
            "fecha_ingreso": datetime(2024, 2, 15),
            "activo": True,
        },
        {
            "_id": 3,
            "nombre": "Tablet iPad",
            "categoria": "tablets",
            "precio": 599,
            "stock": 15,
            "marca": "Apple",
            "tags": ["apple", "creatividad", "portatil"],
            "fecha_ingreso": datetime(2024, 1, 25),
            "activo": True,
        },
        {
            "_id": 4,
            "nombre": "Auriculares Bluetooth",
            "categoria": "audio",
            "precio": 299,
            "stock": 0,
            "marca": "Sony",
            "tags": ["audio", "inalambrico", "calidad"],
            "fecha_ingreso": datetime(2024, 3, 1),
            "activo": False,
        },
    ]
    db.productos.insert_many(productos)


def insertar_ventas(db):
    ventas = [
        {
            "producto_id": 1,
            "cliente_email": "ana@techworld.com",
            "cantidad": 1,
            "total": 1500,
            "fecha": datetime(2024, 3, 15),
            "ciudad": "Madrid",
        },
        {
            "producto_id": 2,
            "cliente_email": "carlos@techworld.com",
            "cantidad": 2,
            "total": 1598,
            "fecha": datetime(2024, 3, 16),
            "ciudad": "Barcelona",
        },
        {
            "producto_id": 3,
            "cliente_email": "maria@techworld.com",
            "cantidad": 1,
            "total": 599,
            "fecha": datetime(2024, 3, 17),
            "ciudad": "Madrid",
        },
    ]
    db.ventas.insert_many(ventas)


def ej01_consultaclientes(db):
    resultados = db.clientes.find({}, {"_id": 0})
    print("Tipo de dato de resultados:", type(resultados))

    for cliente in resultados:
        print(cliente["nombre"] + " - " + cliente["email"])

    listado_resultados = list(resultados)
    print("Tipo de dato de listado_resultados:", type(listado_resultados))


def consultas_madrid(db):
    resultados = db.estudiantes.find(
        {"ciudad": "Madrid"}, {"_id": 0, "nombre": 1, "ciudad": 1}
    )
    for estudiante in resultados:
        print(estudiante["nombre"] + " - " + estudiante["ciudad"])


def consultar_cursos_mas_50Horas(db):
    resultados = db.cursos.find(
        {"duracion_horas": {"$gt": 50}}, {"_id": 0, "nombre": 1, "duracion_horas": 1}
    )
    for curso in resultados:
        print(curso["nombre"] + " - " + str(curso["duracion_horas"]) + " horas")


def actualizar_edad_Laura_23(db):
    resultado = db.estudiantes.update_one(
        {"nombre": "Laura Martínez"}, {"$set": {"edad": 23}}
    )
    print("Documentos actualizados:" + str(resultado.modified_count))


def ejercicio5_actualizar_todos_estudiantes_activos(db):
    resultado = db.estudiantes.update_many({}, {"$set": {"activo": True}})
    print("Documentos actualizados:" + str(resultado.modified_count))


def ejercicio6_infoCurso_porEstudiante(db, estudiante_nombre):
    resultado = db.estudiantes.aggregate(
        [
            {"$match": {"nombre": estudiante_nombre}},
            {
                "$lookup": {
                    "from": "cursos",
                    "localField": "curso_id",
                    "foreignField": "_id",
                    "as": "info_curso",
                }
            },
            {"$unwind": "$info_curso"},
            {
                "$project": {
                    "_id": 0,
                    "nombre_estudiante": "$nombre",
                    "nombre_curso": "$info_curso.nombre",
                    "profesor": "$info_curso.profesor",
                    "duracion_horas": "$info_curso.duracion_horas",
                    "nivel": "$info_curso.nivel",
                }
            },
        ]
    )
    for info in resultado:
        print(info)


def ej01_obtenerProductos(db):
    resultado = db.productos.find()
    for producto in resultado:
        print(producto["nombre"] + " - " + str(producto["precio"]) + " EUR")


def ej02_consultaProductosActivos(db):
    resultado = db.productos.find(
        {"activo": True}, {"_id": 0, "nombre": 1, "precio": 1, "activo": 1}
    )
    for producto in resultado:
        print(
            producto["nombre"]
            + " - "
            + str(producto["precio"])
            + " EUR"
            + " - "
            + str(producto["activo"])
        )


def ej03_consultaProductosComputadores(db):
    resultado = db.productos.find(
        {"categoria": "computadoras"},
        {"_id": 0, "nombre": 1, "categoria": 1, "precio": 1},
    )
    for producto in resultado:
        print(producto["nombre"] + " - " + producto["categoria"])


def ej04_consultaProductosPremium(db):
    resultado = db.productos.find(
        {"precio": {"$gt": 500}}, {"_id": 0, "nombre": 1, "precio": 1}
    )
    for producto in resultado:
        print(producto["nombre"] + " - " + str(producto["precio"]) + " EUR")


def ej05_consultaClientesPremium(db):
    resultado = db.clientes.find(
        {"premium": True}, {"_id": 0, "nombre": 1, "premium": 1}
    )
    for cliente in resultado:
        print(cliente["nombre"] + " - " + str(cliente["premium"]))


def ej06_actualizarPrecioAuriculares(db):
    resultado = db.productos.update_one(
        {"nombre": "Auriculares Bluetooth"}, {"$set": {"precio": 249}}
    )
    print("Documentos actualizados:" + str(resultado.modified_count))


def ej07_activarProductos(db):
    resultado = db.productos.update_many(
        {"activo": False}, {"$set": {"activo": True}, "$set": {"stock": 10}}
    )
    print("Documentos actualizados:" + str(resultado.modified_count))


def ej08_descuentoApple(db):
    resultado = db.productos.update_many({"marca": "Apple"}, {"$mul": {"precio": 0.9}})
    print("Documentos actualizados:" + str(resultado.modified_count))


def ej09_incrementarStock(db):
    resultado = db.productos.update_many(
        {"stock": {"$lt": 10}}, {"$inc": {"stock": 10}}
    )
    print("Documentos actualizados:" + str(resultado.modified_count))


def ej10_crearIndiceNombre(db):
    db.clientes.create_index(["nombre"])


def ej11_crearIndiceAscendente(db):
    db.productos.create_index(
        [("categoria", pymongo.ASCENDING), ("precio", pymongo.DESCENDING)]
    )

def ej12_indiceUnicoEmail(db):
	db.clientes.create_index("email", unique=True)

def ej13_verIndicesProductos(db):
	indices = db.productos.list_indexes()
	for indice in indices:
		print(indice)
  
def ej15_combinaInfo(db):
    pipeline_ventas = [
		{
			"lookup": {
				"from":  "productos",
				"localField": "producto_id",
				"foreignField": "_id",
				"as": "info_producto"
			}
        },
        {
            "$unwind": "$info_producto"
        },
		{
            "$project": {
				"cliente": "$cliente_email",           #!"cliente_email" : 1 si no quiero renombrar
				"producto": "$info_producto.nombre",
				"categoria": "$info_producto.categoria",
				"marca": "$info_producto.marca",
				"cantidad": 1,
				"total": 1,
				"ciudad": 1,
			}
		}
	] 
    resultado = db.ventas.aggregate(pipeline_ventas)

if __name__ == "__main__":
    try:
        client, db = crear_conexion()
        insertar_clientes(db)
        insertar_productos(db)
        insertar_ventas(db)

        print("\n----- Ejercicio 1: Consulta de Productos -----")
        ej01_obtenerProductos(db)

        print("\n----- Ejercicio 2: Consulta de Productos Activos -----")
        ej02_consultaProductosActivos(db)

        print("\n----- Ejercicio 3: Consulta de Productos Computadores-----")
        ej03_consultaProductosComputadores(db)

        print("\n----- Ejercicio 4: Consulta de Productos Premium -----")
        ej04_consultaProductosPremium(db)

        print("\n----- Ejercicio 5: Consulta de Clientes Premium -----")
        ej05_consultaClientesPremium(db)

        print("\n----- Ejercicio 6: Actualizar Precio Auriculares -----")
        ej06_actualizarPrecioAuriculares(db)

        print("\n----- Ejercicio 7: Activar Productos -----")
        ej07_activarProductos(db)

        print("\n----- Ejercicio 8: Descuento Apple -----")
        ej08_descuentoApple(db)

        print("\n----- Ejercicio 9: Incrementar Stock -----")
        ej09_incrementarStock(db)	
  
        print("\n----- Ejercicio 10: Crear Indice Nombre -----")
        ej10_crearIndiceNombre(db)	
  
        print("\n----- Ejercicio 11: Crear Indice Ascendente -----")	
        ej11_crearIndiceAscendente(db)
  
        print("\n----- Ejercicio 12: Indice Unico Email -----")
        ej12_indiceUnicoEmail(db)
  
        print("\n----- Ejercicio 13: Ver Indices Productos -----")
        ej13_verIndicesProductos(db)	

    except Exception as e:
        print("Error al insertar documentos:", e)
    finally:
        client.close()
