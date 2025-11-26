import pandas as pd

# 1. Cargar de datos y exploración inicial
clientes = pd.read_csv(r"C:\Users\javie\Desktop\3 Carrera\Sistemas Intensivos en Datos\lab9\datos\clientes.csv")
pedidos = pd.read_csv(r"C:\Users\javie\Desktop\3 Carrera\Sistemas Intensivos en Datos\lab9\datos\pedidos.csv")

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