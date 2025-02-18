import pandas as pd
import logging as log

# Configuración básica de logging
log.basicConfig(filename='error_log.log', level=log.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

data = pd.read_csv('datos_2.csv')

#se almacenan en otro Data Frame los valores de la edad menor a 18 y mayor a 60
valores_edad_errados = data[(data['EDAD']<18)|(data['EDAD']>60)]

if not valores_edad_errados.empty:

    edad_errados = pd.DataFrame(valores_edad_errados['EDAD'].values,valores_edad_errados['NOMBRE'])

    for index,row in edad_errados.iterrows():
       log.error(f'El valor de la edad de {index} : {row.values} es incorrecto, la EDAD debe ser mayor a 18 y menor a 60')

#Funcion para validar valores nulos dentro de las columnas
def validar_valores_nulos(indice,campo):

    valores_nulos = data[data[campo].isnull()]

    if not valores_nulos.empty:
        validar_valores_nulos = pd.DataFrame(valores_nulos[campo].values, valores_nulos[indice])

        for index,row in validar_valores_nulos.iterrows():
            log.error(f'{campo} de {index} es {row.values}, {campo} no puede ser nula')

#Validar valores duplicados
def validar_valores_duplicados(campo):
    valor_duplicado = data[campo][data[campo].duplicated()]

    for index in valor_duplicado:
        log.error(f'el nombre {index} esta duplicado')



validar_valores_nulos('NOMBRE','EDAD')
validar_valores_nulos('NOMBRE','CARRERA_PROFESIONAL')
validar_valores_nulos('NOMBRE','CIUDAD')
validar_valores_duplicados('NOMBRE')
#print(data)
