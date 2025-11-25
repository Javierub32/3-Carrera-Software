import pandas as pd
import numpy as np
from datetime import datetime

clientes_data = {
    'cliente_id': [1, 2, 3, 4, 5, 6, 7],
    'nombre': ['Ana García', 'Luis Martínez', 'Carlos Rodríguez', 'María López', 
               'Pedro Sánchez', 'Laura Fernández', 'Sofia Ramirez'],
    'email': ['ana@gmail.com', 'luis@empresa.com', 'carlos@hotmail.com', 
              'maria@gmail.com', 'pedro@yahoo.com', 'laura@gmail.com', 'sofia@empresa.com'],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Sevilla', 'Barcelona', 'Bilbao'],
    'saldo': ['1500.50', '800.75', '2200.00', '950.25', '3000.80', '1200.40', '750.90'],
    'fecha_registro': ['2023-01-15', '2022-03-22', '2023-05-10', '2021-11-30', 
                       '2023-08-14', '2022-01-05', '2023-12-01'],
    'categoria': ['Premium', 'Standard', 'Premium', 'Standard', 'Premium', 'Standard', 'Standard']

}
df_clientes = pd.DataFrame(clientes_data)

pedidos_data = {
    'pedido_id': [101, 102, 103, 104, 105, 106, 107, 108, 109],
    'cliente_id': [1, 2, 1, 3, 4, 2, 1, 8, 3],  # cliente_id 8 no existe en clientes
    'producto': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Teclado', 
                 'Mouse', 'Tablet', 'Monitor', 'Laptop'],
    'cantidad': [1, 2, 1, 1, 3, 2, 1, 1, 1],
    'precio': [800, 300, 500, 250, 50, 25, 300, 250, 800],
    'fecha_pedido': ['2023-02-20', '2023-03-15', '2023-04-10', '2023-05-25', 
                     '2023-06-05', '2023-07-18', '2023-08-20', '2023-09-01', '2023-10-15'],
    'estado': ['Entregado', 'Entregado', 'Pendiente', 'Entregado', 'Cancelado', 
               'Entregado', 'Entregado', 'Pendiente', 'Pendiente']

}

df_pedidos = pd.DataFrame(pedidos_data)

df_pedidos['Total'] = df_pedidos['cantidad'] * df_pedidos['precio']

productos_data = {
    'producto_id': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'nombre': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Teclado'],
    'precio': ['1200.75', '450.50', '799.99', '299.00', '89.95'],
    'categoria': ['Tecnología', 'Tecnología', 'Tecnología', 'Oficina', 'Oficina'],
    'stock': [15, 30, 25, 40, 100]

}

df_productos = pd.DataFrame(productos_data)

# Ejercicio 1 - SELECT nombre, ciudad FROM clientes
ej1 = df_clientes[['nombre', 'ciudad']]
print("\n1", ej1,"\n")
#Query
ej1_query = df_clientes.query("ciudad == ciudad")[['nombre', 'ciudad']]
print("1 - query\n", ej1_query ,"\n")
#loc
ej1_loc = df_clientes.loc[:, ['nombre', 'ciudad']]
print("1 - loc\n", ej1_loc ,"\n")

# Ejercicio 2 - SELECT * FROM clientes WHERE ciudad = 'Madrid'
#columnas
ejercicio2 = df_clientes[df_clientes['ciudad'] == 'Madrid']
print("Ejercicio 2\n", ejercicio2 ,"\n")
#query
res_query2 = df_clientes.query("ciudad == 'Madrid'")
print("Ejercicio 2 - query\n", res_query2 ,"\n")

# Ejercicio 3 - SELECT * FROM clientes WHERE ciudad = 'Madrid' AND categoria = 'Premium'
ejercicio3 = df_clientes[(df_clientes['ciudad'] == 'Madrid') & (df_clientes['categoria'] == 'Premium')]
print("Ejercicio 3\n", ejercicio3 ,"\n")
#query
res_query3 = df_clientes.query("ciudad == 'Madrid' and categoria == 'Premium'")
print("Ejercicio 3 - query\n", res_query3 ,"\n")

# Ejercicio 4 - SELECT * FROM clientes WHERE ciudad = 'Madrid' OR ciudad = 'Barcelona'
ejercicio4 = df_clientes[(df_clientes['ciudad'] == 'Madrid') | (df_clientes['ciudad'] == 'Barcelona')]
ej4 = df_clientes[df_clientes['ciudad'].isin(['Madrid', 'Barcelona'])]
print("Ejercicio 4\n", ejercicio4 ,"\n")

# Ejercicio 5 - SELECT nombre, ciudad FROM clientes ORDER BY ciudad DESC, nombre ASC
ejercicio5 = df_clientes.sort_values(by=['ciudad', 'nombre'], ascending=[False, True])[['nombre', 'ciudad']]
print("Ejercicio 5\n", ejercicio5 ,"\n")

# Ejercicio 6 - SELECT * FROM clientes LIMIT 3
ejercicio6 = df_clientes.head(3)
print("Ejercicio 6\n", ejercicio6 ,"\n")

# Ejercicio 7 - SELECT COUNT(*) FROM clientes
ejercicio7 = len(df_clientes)
print("Ejercicio 7\n", ejercicio7 ,"\n")

# Ejercicio 8 - SELECT ciudad, COUNT(*) FROM clientes GROUP BY ciudad
ejercicio8 = df_clientes.groupby('ciudad').size().reset_index(name='count')
print("Ejercicio 8\n", ejercicio8 ,"\n")

# Ejercicio 9 - SELECT cliente_id, COUNT(*), SUM(total), AVG(total) FROM pedidos GROUP BY cliente_id
ejercicio9 = df_pedidos.groupby('cliente_id').agg({
    'pedido_id': 'count',
    'Total': ['sum', 'mean']
}).round(2)
ejercicio9.columns = ['count', 'sum_total', 'avg_total']
print("Ejercicio 9\n", ejercicio9 ,"\n")

ej9 = df_pedidos.groupby('cliente_id').agg(
    conteo_pedidos=('pedido_id', 'count'),
    suma_total=('Total', 'sum'),
    media_total=('Total', 'mean')
).reset_index()
print("\n9. Agregados de pedidos por cliente\n", ej9)

# Ejercicio 10 - SELECT ciudad, COUNT(*) as cnt FROM clientes GROUP BY ciudad HAVING cnt > 1
ejercicio10 = df_clientes.groupby('ciudad').size().reset_index(name='cnt')
ejercicio10 = ejercicio10[ejercicio10['cnt'] > 1]
print("Ejercicio 10\n", ejercicio10 ,"\n")

# Ejercicio 11 - SELECT c.nombre, p.producto, p.total FROM clientes c JOIN pedidos p ON c.cliente_id = p.cliente_id
#join = INNER JOIN
ejercicio11 = pd.merge(df_clientes, df_pedidos, on='cliente_id', how='inner')[['nombre', 'producto', 'Total']]
print("Ejercicio 11\n", ejercicio11 ,"\n")

# Ejercicio 12 - SELECT c.nombre, p.producto FROM clientes c LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
#left join
ejercicio12 = pd.merge(df_clientes, df_pedidos, on='cliente_id', how='left')[['nombre', 'producto']]
print("Ejercicio 12\n", ejercicio12 ,"\n")

# Ejercicio 13 - SELECT c.nombre, p.pedido_id FROM clientes c RIGHT JOIN pedidos p ON c.cliente_id = p.cliente_id
#right join
ejercicio13 = pd.merge(df_clientes, df_pedidos, on='cliente_id', how='right')[['nombre', 'pedido_id']]
print("Ejercicio 13\n", ejercicio13 ,"\n")

# Ejercicio 14 - SELECT nombre, email FROM clientes WHERE UPPER(nombre) LIKE '%A%' OR UPPER(email) LIKE '%GMAIL%'
ejercicio14 = df_clientes[(df_clientes['nombre'].str.upper().str.contains('A')) | (df_clientes['email'].str.upper().str.contains('GMAIL'))][['nombre', 'email']]
print("Ejercicio 14\n", ejercicio14 ,"\n")
#query
res_query14 = df_clientes.query(
  "nombre.str.upper().str.contains('A') or "
  "email.str.upper().str.contains('GMAIL')")
[['nombre', 'email']]
print("Ejercicio 14 - query\n", res_query14 ,"\n")

# Ejercicio 15 - SELECT UPPER(nombre), LOWER(ciudad) FROM clientes
ejercicio15 = df_clientes[['nombre', 'ciudad']].copy()
ejercicio15['nombre'] = ejercicio15['nombre'].str.upper()
ejercicio15['ciudad'] = ejercicio15['ciudad'].str.lower()
print("Ejercicio 15\n", ejercicio15 ,"\n")

# Ejercicio 16 - SELECT TO_CHAR(fecha_registro, 'YYYY-MM') as año_mes, TO_CHAR(fecha_registro, 'DD/MM/YYYY') as fecha FROM clientes
ejercicio16 = df_clientes[['fecha_registro']].copy()
ejercicio16['año_mes'] = pd.to_datetime(ejercicio16['fecha_registro']).dt.strftime('%Y-%m')
ejercicio16['fecha'] = pd.to_datetime(ejercicio16['fecha_registro']).dt.strftime('%d/%m/%Y')
ejercicio16 = ejercicio16[['año_mes', 'fecha']]
print("Ejercicio 16\n", ejercicio16 ,"\n")

# Ejercicio 17 - SELECT ROUND(saldo, 0), FLOOR(saldo) FROM clientes;
ejercicio17 = df_clientes[['saldo']].copy()
ejercicio17['saldo'] = ejercicio17['saldo'].astype(float)
ejercicio17['round_saldo'] = ejercicio17['saldo'].round(0)
ejercicio17['floor_saldo'] = np.floor(ejercicio17['saldo'])
ejercicio17 = ejercicio17[['round_saldo', 'floor_saldo']]
print("Ejercicio 17\n", ejercicio17 ,"\n")

# Ejercicio 18 - SELECT * FROM clientes WHERE ciudad IN ('Madrid', 'Barcelona')
ejercicio18 = df_clientes[df_clientes['ciudad'].isin(['Madrid', 'Barcelona'])]
print("Ejercicio 18\n", ejercicio18 ,"\n")
#query
res_query18 = df_clientes.query("ciudad in ['Madrid', 'Barcelona']")
print("Ejercicio 18 - query\n", res_query18 ,"\n")

# Ejercicio 19 - SELECT nombre FROM clientes c WHERE EXISTS (SELECT 1 FROM pedidos p WHERE p.cliente_id = c.cliente_id AND p.total > 400

# Ejercicio 20 - SELECT nombre FROM clientes WHERE cliente_id NOT IN (SELECT cliente_id FROM pedidos)
