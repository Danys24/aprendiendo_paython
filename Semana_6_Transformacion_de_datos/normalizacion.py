import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

datos = pd.read_csv("Semana_6_Transformacion_de_datos/datos_1.csv")

nombres = pd.DataFrame(datos['NOMBRE'])
edades = pd.DataFrame(datos['EDAD'])

#array_edades = np.array(edades).transpose()
#array_nombres = np.array(nombres).transpose()

'''
fig, ax = plt.subplots(figsize=(5, 2.7))   # Create a figure containing a single Axes.
ax.set_title("Edades")
ax.plot(datos["EDAD"])  # Plot some data on the Axes.
plt.show() 


plt.bar(datos["EDAD"],datos["NOMBRE"], color='g')
plt.xlabel("Edades")
plt.ylabel("Nombres")
plt.title("Distribucion Edades")
plt.show()                           # Show the figure.
'''

escaler = preprocessing.StandardScaler()
minmax = preprocessing.MinMaxScaler()

datos_escalados = escaler.fit_transform(edades)
datos_minmax = minmax.fit_transform(edades)

#print(datos_escalados)
#print(datos_minmax)

'''
fig = plt.figure(figsize=(15,3))
ax1 = fig.add_subplot(1,5,1) 
ax2 = fig.add_subplot(1,5,2)

ax1.set_title("Edades estandar escaler")
ax1.hist(datos_escalados)

ax2.set_title("Edades min max escaler")
ax2.hist(datos_minmax)

plt.show() 

'''

# Calcular cuartiles
Q1 = datos['EDAD'].quantile(0.25)
Q3 = datos['EDAD'].quantile(0.75)
IQR = Q3 - Q1

# Definir límites para detectar outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar outliers
outliers = datos[(datos['EDAD'] < limite_inferior) | (datos['EDAD'] > limite_superior)]
print("Outliers detectados:\n", outliers)