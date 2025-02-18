import pandas as pd
import numpy as np

data = {'nombre':['Maria','Pedro','Camilo','Daniel'],'Cargo':['Regulador','Impelementador','QA','Desarrollador'],'Correo':['maria@jwprojecthouse','pedro@jwprojecthouse','camilo@jwprojecthouse','daniel@jwprojecthouse']}

empleados = pd.DataFrame(data)

#print(empleados)

df = pd.DataFrame([['Maria',20],['Camilo',28]],columns=['Nombre','Edad']) 
#print(df)

aleatorio = pd.DataFrame(np.random.randn(4,3), columns=['a','b','c']) #np.random.randn(filas,columnas)
print(aleatorio)

