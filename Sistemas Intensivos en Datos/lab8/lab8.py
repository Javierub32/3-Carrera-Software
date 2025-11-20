import pandas as pd
import numpy as np

datos = {
 'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Tablet'],
 'Precio': [1200, 25, 80, 300, 450],
 'Stock': [15, 100, 50, 30, 25],
 'Categoria': ['Electrónica', 'Accesorio', 'Accesorio', 'Electrónica', 'Electrónica']
}

datos2 = [
 [1, 'Laptop', 1200, 15],
 [2, 'Mouse', 25, 100],
 [3, 'Teclado', 80, 50],
 [4, 'Monitor', 300, 30],
 [5, 'Tablet', 450, 25]
]

# Ejercicio 1
print("=== Ejercicio 1: Crear Dataframe ===")
print("Dataframe Creado")
df1 = pd.DataFrame(datos)

# Ejercicio 2
print("\n\n=== Ejercicio 2: Crear Dataframe ===")
print("Dataframe Creado")
df2 = pd.DataFrame(datos2, columns=['ID', 'Producto', 'Precio', 'Stock'])

# Ejercicio 3
print("\n\n=== Ejercicio 3: Primeros elementos dataframes ===")
print(df1.head(3))
print()
print(df2.head(3))

# Ejercicio 4
print("\n\n=== Ejercicio 4: Características Dataframe 1 ===")
print(f"Shape del dataframe: {df1.shape}")
print(f"Nombre de las columnas: {df1.columns}")
print(f"Estadísticas básicas: \n{df1.describe()}")
print(f"Ultimas dos filas: \n{df1[-2:]}")
print(f"Dos filas aleatorias: \n {df1.sample(2)}")

# Ejercicio 5
print("\n\n=== Ejercicio 5: Selecciones Dataframe 1 ===")
print(f"\nColumna Producto: \n{df1["Producto"]}")
print(f"\nColumna Producto y Precio: \n{df1[['Producto', 'Precio']]}")
print(f"\nPrimera fila: \n{df1.iloc[0, :]}")
print(f"\nElemento en la posición (1,2): \n{df1.iloc[1, 2]}")
print(f"\nDos primeras filas: \n {df1.loc[:1]}")

# Ejercicio 6
print("\n\n=== Ejercicio 6: Filtrar Dataframe Nuevo ===")
np.random.seed(42)
datos_ventas = {
 'Fecha': pd.date_range('2024-01-01', periods=100, freq='D'),
 'Producto': np.random.choice(['Laptop', 'Mouse', 'Teclado', 'Monitor',
'Tablet'], 100),
 'Cantidad': np.random.randint(1, 10, 100),
 'Precio_Unitario': np.random.choice([1200, 25, 80, 300, 450], 100),
 'Region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 100),
 'Vendedor': np.random.choice(['Ana', 'Carlos', 'Maria', 'Pedro'], 100)
}
df_ventas = pd.DataFrame(datos_ventas)
df_ventas['Venta_Total'] = df_ventas['Cantidad'] * df_ventas['Precio_Unitario']

print(f"Ventas de Laptos: \n {df_ventas[df_ventas['Producto'] == 'Laptop']}")
print(f"Ventas mayor 2000: \n {df_ventas[df_ventas['Venta_Total'] > 2000]}")
print(f"Ventas por Maria en el norte: \n {df_ventas[(df_ventas['Vendedor'] == 'Maria') & (df_ventas['Region'] == 'Norte')]}")

# Ejercicio 7
print("\n\n=== Ejercicio 7: Trabajar con nulos ===")
datos_ventas_con_nan = df_ventas.copy()
datos_ventas_con_nan.iloc[1,3] = np.nan
datos_ventas_con_nan.iloc[2,2] = np.nan
datos_ventas_con_nan.iloc[0,1] = np.nan
datos_ventas_con_nan.iloc[1,1] = np.nan
datos_ventas_con_nan.iloc[6,6] = np.nan

nan_por_columa = datos_ventas_con_nan.isnull().sum()
print(nan_por_columa)

df_sin_nulos = datos_ventas_con_nan.dropna()
print(f"\n Shape dataframe original: {datos_ventas_con_nan.shape} | Shape dataframe sin nulos: {df_sin_nulos.shape}")

df_rellenado = datos_ventas_con_nan.copy()
df_rellenado['Cantidad'].fillna(df_rellenado['Cantidad'].mean(), inplace=True)
df_rellenado['Precio_Unitario'].fillna(df_rellenado['Precio_Unitario'].median(), inplace=True)

df_ordenado = df_rellenado.sort_values(by='Venta_Total', ascending=False)

# Ejercicio 8
print("\n\n=== Ejercicio 8: Estadísticas resumen ===")
venta_total_global = df_ventas['Venta_Total'].sum()
venta_promedio_global = df_ventas['Venta_Total'].mean()
venta_maxima_global = df_ventas['Venta_Total'].max()
num_ventas = len(df_ventas)

print("Venta total:", venta_total_global)
print("Venta promedio:", venta_promedio_global)
print("Venta máxima:", venta_maxima_global)
print("Número de ventas:", num_ventas)

ventas_por_producto = df_ventas.groupby('Producto')['Venta_Total'].sum()
print()
print(ventas_por_producto)

ventas_region = df_ventas.groupby('Region')['Venta_Total'].sum()
ventas_region_media = df_ventas.groupby('Region')['Venta_Total'].mean()
ventas_region_max = df_ventas.groupby('Region')['Venta_Total'].max()
ventas_region_cantidad = df_ventas.groupby('Region')['Venta_Total'].count()

print("\nVenta total:", ventas_region)
print("\nVenta promedio:", ventas_region_media)
print("\nVenta máxima:", ventas_region_max)
print("\nNúmero de ventas:", ventas_region_cantidad)

# Ejercicio 9
df_ventas['Venta_Con_IVA'] = df_ventas['Venta_Total'] * 1.21

df_ventas['Categoria_Precio'] = np.where(
    df_ventas['Precio_Unitario'] > 500,
    'Alto',
    'Bajo'
)

def clasificar_venta(venta_total):
    if venta_total < 500:
        return 'Pequeña'
    elif venta_total < 2000:
        return 'Mediana'
    else:
        return 'Grande'

df_ventas['Tipo_Venta'] = df_ventas['Venta_Total'].apply(clasificar_venta)

# Ejercicio 10
info_producto= {
 'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Tablet', 'Auriculares'],
 'Categoria': ['Electrónica', 'Accesorio', 'Accesorio', 'Electrónica',
'Electrónica', 'Accesorio'],
 'Costo': [800, 15, 40, 200, 300, 20]
}
info_vendedores = {
 'Vendedor': ['Ana', 'Carlos', 'Maria', 'Pedro', 'Laura'],
 'Departamento': ['Ventas', 'Tecnología', 'Ventas', 'Marketing', 'Ventas'],
 'Salario_Base': [30000, 35000, 32000, 28000, 31000]
}

df_productos = pd.DataFrame(info_producto)
df_vendedores = pd.DataFrame(info_vendedores)

df_ventas_productos = pd.merge(
    df_ventas,
	df_productos,
	left_index=True,
    right_index=True,
	how='inner',
    indicator=True
)

df_ventas_vendedores = pd.merge(
	df_ventas,
    df_vendedores,
	left_index=True,
    right_index=True,
	how='left',
    indicator=True
)

nueva_venta = {
    'Fecha': ['2024-04-01'],
    'Producto': ['Auriculares'],
    'Cantidad': [2],
    'Precio_Unitario': [50],
    'Region': ['Norte'],
    'Vendedor': ['Laura'],
    'Venta_Total': [100]
}

df_nueva_venta = pd.DataFrame(nueva_venta)
df_nueva_venta['Fecha'] = pd.to_datetime(df_nueva_venta['Fecha'])
df_ventas_actualizado = pd.concat([df_ventas, df_nueva_venta], ignore_index=True)

# Ejercicio 11: Concatenar nueva información
print("\n\n=== Ejercicio 11: Concatenar nueva venta ===")
ventas = df_ventas_actualizado[(df_ventas_actualizado['Fecha'] >= '2024-01-15') & (df_ventas_actualizado['Fecha'] <= '2024-01-31')]
print(f"Han habido {len(ventas)} ventas en la segunda quincena de enero de 2024.")