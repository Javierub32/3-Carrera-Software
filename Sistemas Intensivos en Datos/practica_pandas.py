import pandas as pd
import numpy as np

#Lista de diccionario
data ={
    'Nombre': ['Ana', 'Maria', 'Carlos', 'Pedro','Laura'],
    'Edad': [25, 32, 28, 45, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Bilbao'],
    'Salario': [40000,45000,55000,60000,70000]
}
df = pd.DataFrame(data)

print(df)

print("3 Ultimas lineas", df.tail(3))
print("3 primeras lineas", df.head(3))

print(df.info())
print(df.describe())
print(df.shape)
print(df['Nombre'])

sub_df = df[['Nombre', 'Salario']]

mayores_30 = df[df['Edad'] > 30]

madrid = df[df['Ciudad'] == 'Madrid']

madrid_query = df.query("Ciudad == 'Madrid'")

filtro1 = df[(df['Edad'] >= 30) & (df['Salario'] > 50000) & (df['Edad'] < 50)]

filtro1_query = df.query("Edad >= 30 & Salario > 50000 & Edad < 50")

# Personas madrid o barcelona
filtro2 = df[(df['Ciudad'] == 'Madrid') | (df['Ciudad'] == 'Barcelona')]

filtro2_query = df.query("Ciudad == 'Madrid' | Ciudad == 'Barcelona'")

#crear columna salario 
df['salario_anual'] = df['Salario']*14
print(df)

#columna categorica 
#usando numpuy
#df['categoria_salarial'] = np.where(df['salario'] <45000, 'Bajo', np.where(df['salario'] < 60000, 'Alto') )
#print(df)


def clasificar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 40:
        return 'Adulto'
    else:
        return 'Senior'
df['grupo_edad'] = df['Edad'].apply(clasificar_edad)
print(df)





