import pandas as pd

datos = pd.read_csv("Transformacion_de_datos/datos_2.csv")


#Reemplazar los valores nulos por valores mas compresibles o manejables
datos['APELLIDO'].fillna("Desconocido", inplace=True)
datos['EDAD'].fillna(datos['EDAD'].mean(), inplace=True)
datos['CARRERA_PROFESIONAL'].fillna("No Aplica", inplace=True)
datos['CIUDAD'].fillna("Desconocido", inplace=True)

print(datos)