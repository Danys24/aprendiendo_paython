import pandas as pd
import numpy as np


data = pd.read_csv('datos.csv')


#print(data.head())       # Muestra las primeras filas del dataset
#print(data.info())       # Información general sobre el dataset
#print(data.describe())   # Estadísticas básicas de las columnas numéricas

#Se eliminan los valores duplicados 
data.drop_duplicates(inplace=True)

data['EDAD'].iloc[0] = 0

# Elimina filas con valores nulos
data.dropna(axis=0, inplace=True)

#Transforma los valores de la columna EDAD en enteros
data['EDAD'] = data['EDAD'].astype('int')

# Obtener los índices de las filas donde 'EDAD' es mayor a 60 y menor a 18
filas_a_eliminar = data[(data['EDAD']<18) | (data['EDAD']>60)].index

# Eliminar esas filas usando drop donde las edades son menores a 18 y mayores a 60
data = data.drop(filas_a_eliminar, axis=0)


print(data)

#Crea el reporte consolidado
#data.to_csv('reporte_consolidado.csv', index=False)