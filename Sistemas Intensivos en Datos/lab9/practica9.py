import pandas as pd

# 1. Cargar de datos y exploración inicial
clientes = pd.read_csv(r"C:\Users\javie\Desktop\carrera\Sistemas Intensivos en Datos\lab9\datos\clientes.csv")
pedidos = pd.read_csv(r"C:\Users\javie\Desktop\carrera\Sistemas Intensivos en Datos\lab9\datos\pedidos.csv")

print('Primeras 5 filas de clientes:')
print(clientes.head())
print('\nPrimeras 5 filas de pedidos:')
print(pedidos.head())

print('\nInformación de clientes:')
print(clientes.info())
print('Forma:', clientes.shape)

print('\nInformación de pedidos:')
print(pedidos.info())
print('Forma:', pedidos.shape)

# 4. Estadísticas descriptivas básicas
print('\nEstadísticas descriptivas de clientes:')
print(clientes.describe())

print('\nEstadísticas descriptivas de pedidos:')
print(pedidos.describe())


# 2. Consultas básicas
df_mayores_30 = clientes[clientes['edad'] > 30]
print('\nClientes mayores de 30 años:')
print(df_mayores_30)

df_premium = clientes[(clientes['categoria'] == 'premium') | (clientes['puntos_fidelidad'] > 3000)]
print('\nClientes premium o con más de 3000 puntos de fidelidad:')
print(df_premium)

df_mayores500 = pedidos[pedidos['total'] > 500]
print('\nPedidos con total mayor a 500:')
print(df_mayores500)

df_mayores_30 = pedidos[(pedidos['estado'] == 'Pendiente') | (pedidos['fecha_pedido'].str.startswith('2023'))]
print('\nPedidos pendientes o realizados en 2023:')
print(df_mayores_30)


# 3. Operaciones de agregación
clientes_por_ciudad = clientes.groupby('ciudad').size()
print('\nNúmero de clientes por ciudad:')
print(clientes_por_ciudad)

ventas_por_estado = pedidos.groupby('estado')['total'].sum()
print('\n2. Ventas totales por estado de pedido:')
print(ventas_por_estado)

edad_promedio = clientes.groupby('categoria')['edad'].mean()
print('\n3. Promedio de edad por categoría:')
print(edad_promedio)

union = pd.merge(clientes, pedidos, on="cliente_id",how="inner")
result = union['ciudad'].value_counts()
print("\n4. Las 3 ciudades con más pedidos:")
print(result.head(3))


# 4. Joins entre tablas
nombre_y_pedido = pd.merge(clientes, pedidos, on="cliente_id", how="inner" )
result = nombre_y_pedido[["nombre", "producto"]]
print('\nNombres de clientes y productos pedidos:')
print(result)

nombre_y_pedido_conNull = pd.merge(clientes, pedidos, on="cliente_id", how="left" )
result = nombre_y_pedido_conNull[["nombre", "producto"]]
print('\nNombres de clientes y productos pedidos (incluye clientes sin pedido):')
print(result)


nombre_y_pedido_conNull = pd.merge(clientes, pedidos, on="cliente_id", how="right")
result = nombre_y_pedido_conNull[nombre_y_pedido_conNull["nombre"].isna()]
print('\nNombre de pedidos sin cliente:')
print(result["producto"])

nombre_y_pedido_conNull = pd.merge(clientes, pedidos, on="cliente_id", how="left")
result = nombre_y_pedido_conNull[nombre_y_pedido_conNull["producto"].isna()]
print('\nNombre de clientes que nunca han hecho un pedido:')
print(result["nombre"])


# 5. Limpieza de datos
print('\nValores nulos en clientes:')
print(clientes.isna().sum())
print('\nValores nulos en pedidos:')
print(pedidos.isna().sum())

print('\nRellenamos las edades nulas con la media de los clientes:')
clientes["edad"].fillna(clientes["edad"].mean())

print('\nRellenamos los puntos de fidelidad nulos con 0:')
clientes["puntos_fidelidad"].fillna(0)

print('\nEliminamos pedidos donde cantidad nula:')
pedidos_limpios = pedidos.dropna(subset=['cantidad']) 	# Crear un nuevo DataFrame sin filas con cantidad nula
pedidos.dropna(subset=['cantidad'], inplace=True)  		# Modificar el DataFrame original


# 6. Creación de nuevas columnas
def clasificarEdad(edad):
	if edad < 30:
		return "Joven"
	elif edad < 60:
		return "Adulto"
	else:
		return "Senior"
clientes["rango_edad"] = clientes["edad"].apply(clasificarEdad)
print('\nCreamos columna rango_edad:')
print(clientes[["edad","rango_edad"]].head(5))



pedidos["fecha_pedido"] = pd.to_datetime(pedidos["fecha_pedido"])
pedidos["año_mes_pedido"] = pedidos["fecha_pedido"].dt.strftime('%Y-%m')
print('\nCreamos columna año_mes_pedido:')
print(pedidos[["fecha_pedido","año_mes_pedido"]].head(5))


def clasificarProducto(producto):
    # Verificación de seguridad: si el dato está vacío, es 'Otros'
    if pd.isna(producto):
        return "Otros"
    
    # Convertimos a minúsculas para facilitar la búsqueda
    p = producto.lower() 
    
    # Lógica de categorías
    if "laptop" in p or "smartphone" in p or "tablet" in p or "smartwatch" in p:
        return "Dispositivo"
    elif "teclado" in p or "ratón" in p or "web" in p or "monitor" in p:
        return "Periféricos"
    elif "auriculares" in p or "altavoz" in p:
        return "Audio"
        
    else:
        return "Otros"
pedidos["tipo_producto"] = pedidos["producto"].apply(clasificarProducto)
print('\nCreamos columna tipo_producto:')
print(pedidos[["producto", "tipo_producto"]].head(10))


def clasificarCliente(producto):
      if pd.isna(producto):
          return "Inactivo"
      else:
          return "Activo"

clientes_y_pedidos = pd.merge(clientes, pedidos, on="cliente_id", how="left")
clientes_y_pedidos["cliente_activo"] = clientes_y_pedidos["producto"].apply(clasificarCliente)
datos_unicos = clientes_y_pedidos.drop_duplicates(subset=["cliente_id"])
clientes["cliente_activo"] = datos_unicos["cliente_activo"].values
print('\nCreamos columna cliente_activo:')
print(clientes[["nombre", "cliente_activo"]].head(10))

'''
tienen_pedido = clientes["cliente_id"].isin(pedidos["cliente_id"])
clientes["cliente_activo"] = np.where(tienen_pedido, "Activo", "Inactivo")
'''


# 7. Consultas avanzadas
union = pd.merge(clientes, pedidos, on="cliente_id", how="inner")

ricos_barcelona = union[(union["total"] > 1000) & (union["ciudad"] == "Barcelona")]
print('\nClientes de Barcelona que han hecho pedidos > 1000:')
print(ricos_barcelona[["nombre", "ciudad", "total"]].groupby("nombre").sum())


masVendidos_porCiudad = union.groupby(["ciudad", "producto"])["cantidad"].sum().reset_index()
masVendidos_porCiudad = masVendidos_porCiudad.sort_values(by="cantidad", ascending=False)
top_1_por_ciudad = masVendidos_porCiudad.drop_duplicates(subset="ciudad", keep="first")
print('\Productos más vendidos por ciudad:')
print(top_1_por_ciudad)


clientesPremium = union[union["categoria"] == "Premium"]
clientesPremium = clientesPremium.groupby("nombre")["total"].sum().reset_index()
top_clientes_premium = clientesPremium.sort_values(by="total", ascending=False).head(5)
print('\n Top clientes premium:')
print(top_clientes_premium)


ventas_2023 = pedidos[ pedidos["fecha_pedido"].dt.year == 2023 ]
evolucion = ventas_2023.groupby("año_mes_pedido")["total"].sum().reset_index()
print('\n Evolución de ventas en 2023:')
print(evolucion)


resumen_clientes = union.groupby("nombre").agg(
    gasto_promedio=("total", "mean"), 
    num_pedidos=("pedido_id", "count") 
).reset_index()
resumen_clientes["gasto_promedio"] = resumen_clientes["gasto_promedio"].round(2)
print("\nResumen por Cliente (Media y Cantidad): ")
print(resumen_clientes.head())


rendimiento = union.groupby(["categoria", "producto"])[["total", "cantidad"]].sum().reset_index()
rendimiento_ordenado = rendimiento.sort_values(
    by=["categoria", "total", "cantidad"], 
    ascending=[True, False, False]
)
top_2_productos = rendimiento_ordenado.groupby("categoria").head(2)
print("\nProductos con mejor rendimiento: ")
print(top_2_productos)