import pandas as pd

data_1 = pd.read_csv("Semana_4_procesamiento_de_datos/datos_1.csv")
data_2 = pd.read_csv("Semana_4_procesamiento_de_datos/datos_2.csv")


data_consolidada = data_1.merge(data_2, on='ID', how='outer')

data_final = pd.DataFrame(data_1['ID'])

data_final['NOMBRE_Y_APELLIDO'] = data_1['NOMBRE'] + ' ' + data_1['APELLIDO']

data_final['SALDO_TOTAL'] = (data_consolidada.groupby('ID', as_index=False)['SALDO_CREDITO'].sum())['SALDO_CREDITO']

data_final['CANTIDAD_OBLIDACIONES'] = (data_consolidada.groupby('ID', as_index=False)['OBLIGACIONES'].count())['OBLIGACIONES']

"""
PROMEDIO DE SALDO POR OBLIGACION

Este indicador te da una idea de cuánto saldo está comprometido por cada obligación 
o deuda que la persona tiene. Es útil para entender si la persona tiene deudas pequeñas o grandes
"""
data_final['PROMEDIO_SALDO_OBLIGACION'] = (data_final['SALDO_TOTAL']/data_final['CANTIDAD_OBLIDACIONES']).astype(int)

data_final['CIUDAD'] = data_1['CIUDAD']

print(data_final)

#Descomentar la siguiente linea para crear un csv que contenga la información procesada
#data_final.to_csv('procesamiento_de_datos/data_final.csv', index=None, header=True)